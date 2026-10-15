-- 20261014000004_debounce_sync_trigger_and_harden_rpc.sql
-- 1. 为 system_settings 增加 Webhook 同步最后触发时间戳
-- 2. 重写 trig_notify_github_exam_sync() 注入 60 秒冷却防抖（Debounce）保护，并从 Supabase Vault 动态读取 GitHub 密钥
-- 3. 加固 sync_exams_to_cloudflare() 存储过程，强制要求管理员鉴权（is_admin()）并注入防抖防护
-- 4. 回收对底层触发器函数的公共 RPC 执行权限

-- 1. 添加同步触发时间记录列
ALTER TABLE public.system_settings 
ADD COLUMN IF NOT EXISTS last_sync_dispatched_at timestamp with time zone 
DEFAULT '1970-01-01 00:00:00+00';

-- 2. 重写触发器函数：引入 60 秒原子防抖锁与 Vault 动态鉴权
CREATE OR REPLACE FUNCTION public.trig_notify_github_exam_sync()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path TO 'public', 'extensions', 'vault'
AS $function$
DECLARE
  v_last_dispatched timestamptz;
  v_now timestamptz := clock_timestamp();
  v_cooldown interval := interval '60 seconds';
  v_token text;
BEGIN
  -- 获取并加锁 system_settings 对应记录，防止并发事务竞争
  SELECT last_sync_dispatched_at INTO v_last_dispatched
  FROM public.system_settings
  WHERE id = 1
  FOR UPDATE;

  -- 若尚未记录或已超出 60 秒冷却期，则触发同步
  IF v_last_dispatched IS NULL OR (v_now - v_last_dispatched) > v_cooldown THEN
    -- 更新触发时间戳
    UPDATE public.system_settings
    SET last_sync_dispatched_at = v_now
    WHERE id = 1;

    -- 从 Supabase Vault 安全动态检索 GitHub 凭证，杜绝硬编码泄漏风险
    SELECT decrypted_secret INTO v_token
    FROM vault.decrypted_secrets
    WHERE name = 'github_dispatch_token'
    LIMIT 1;

    IF v_token IS NOT NULL AND length(v_token) > 0 THEN
      -- 发射 GitHub repository_dispatch Webhook
      PERFORM net.http_post(
        url := 'https://api.github.com/repos/en-way/supabase/dispatches',
        body := '{"event_type": "supabase_exam_sync"}'::jsonb,
        headers := jsonb_build_object(
          'Content-Type', 'application/json',
          'Authorization', 'Bearer ' || v_token,
          'User-Agent', 'Supabase-Webhook',
          'Accept', 'application/vnd.github.v3+json'
        )
      );
    END IF;
  END IF;

  RETURN NULL;
END;
$function$;

-- 3. 重写管理员手动同步 RPC 函数：注入 is_admin 鉴权、Vault 动态检索与防抖保护
CREATE OR REPLACE FUNCTION public.sync_exams_to_cloudflare()
RETURNS text
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path TO 'public', 'extensions', 'vault'
AS $function$
DECLARE
  req_id bigint;
  v_last_dispatched timestamptz;
  v_now timestamptz := clock_timestamp();
  v_cooldown interval := interval '60 seconds';
  v_token text;
BEGIN
  -- 严格鉴权：仅管理员或超级管理员允许执行
  IF NOT public.is_admin() THEN
    RAISE EXCEPTION '权限不足：仅管理员允许手动触发边缘同步。';
  END IF;

  -- 读取同步时间戳并加锁
  SELECT last_sync_dispatched_at INTO v_last_dispatched
  FROM public.system_settings
  WHERE id = 1
  FOR UPDATE;

  IF v_last_dispatched IS NOT NULL AND (v_now - v_last_dispatched) <= v_cooldown THEN
    RETURN '同步请求已跳过：系统处于 60 秒防抖保护中（已于 ' || to_char(v_last_dispatched, 'HH24:MI:SS') || ' 触发过同步，请勿频繁点击）';
  END IF;

  -- 更新最后触发时间
  UPDATE public.system_settings
  SET last_sync_dispatched_at = v_now
  WHERE id = 1;

  -- 从 Supabase Vault 安全动态检索 GitHub 凭证
  SELECT decrypted_secret INTO v_token
  FROM vault.decrypted_secrets
  WHERE name = 'github_dispatch_token'
  LIMIT 1;

  IF v_token IS NULL OR length(v_token) = 0 THEN
    RAISE EXCEPTION 'Supabase Vault 中未找到配置的 github_dispatch_token 密钥凭据。';
  END IF;

  SELECT net.http_post(
    url := 'https://api.github.com/repos/en-way/supabase/dispatches',
    body := '{"event_type": "supabase_exam_sync"}'::jsonb,
    headers := jsonb_build_object(
      'Content-Type', 'application/json',
      'Authorization', 'Bearer ' || v_token,
      'User-Agent', 'Supabase-Webhook',
      'Accept', 'application/vnd.github.v3+json'
    )
  ) INTO req_id;

  RETURN '已成功向 GitHub Actions 发送构建指令 (Request ID: ' || req_id || ')';
END;
$function$;

-- 4. 权限收敛：剥离对触发器函数的直接 RPC 调用暴露
REVOKE EXECUTE ON FUNCTION public.trig_notify_github_exam_sync() FROM anon, authenticated, public;
GRANT EXECUTE ON FUNCTION public.sync_exams_to_cloudflare() TO authenticated;
