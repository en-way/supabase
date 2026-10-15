-- ==============================================================================
-- Migration: 20261014000006_approval_based_password_reset.sql
-- Description:
-- 1. 创建 password_reset_requests 审批流数据表，支持密文预存
-- 2. 提供登录页未登录学员“忘记密码申请”RPC (submit_unauthenticated_password_reset_request)
-- 3. 提供个人中心学员“改密申请”与“自主撤回”RPC
-- 4. 提供超级管理员专属审批生效 RPC (super_admin_review_password_reset)
-- 5. 彻底废除并删除直接改密 (admin_reset_user_password, super_admin_batch_reset_student_passwords)
-- 6. 彻底废除并删除前台移交超管通道 (super_admin_transfer_ownership)，超管身份底层锁死仅限 Supabase 后台操作
-- ==============================================================================

-- 1. 创建申请表
CREATE TABLE IF NOT EXISTS public.password_reset_requests (
    id UUID PRIMARY KEY DEFAULT extensions.uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    username TEXT NOT NULL,
    nickname TEXT,
    role TEXT NOT NULL DEFAULT 'student',
    requested_encrypted_password TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'approved', 'rejected', 'canceled')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    reviewed_at TIMESTAMPTZ,
    reviewed_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    review_note TEXT
);

-- 索引
CREATE INDEX IF NOT EXISTS idx_pwd_requests_user_status ON public.password_reset_requests(user_id, status);
CREATE INDEX IF NOT EXISTS idx_pwd_requests_pending ON public.password_reset_requests(status, created_at DESC);

-- 启用行级安全 RLS
ALTER TABLE public.password_reset_requests ENABLE ROW LEVEL SECURITY;

-- 允许已登录用户读取自己的申请，超级管理员可读取所有申请
DROP POLICY IF EXISTS "Users can read own password reset requests" ON public.password_reset_requests;
CREATE POLICY "Users can read own password reset requests" ON public.password_reset_requests
    FOR SELECT TO authenticated
    USING (
        ((SELECT auth.uid()) = user_id) 
        OR public.is_super_admin()
    );

-- 2. 登录界面公开忘记密码申请 RPC
CREATE OR REPLACE FUNCTION public.submit_unauthenticated_password_reset_request(
    input_username TEXT, 
    new_plain_password TEXT
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path TO 'public', 'extensions'
AS $$
DECLARE
    v_user RECORD;
    v_hash TEXT;
    v_recent_req TIMESTAMPTZ;
BEGIN
    input_username := trim(COALESCE(input_username, ''));
    IF length(input_username) = 0 THEN
        RAISE EXCEPTION '请输入账号用户名。';
    END IF;

    IF new_plain_password IS NULL OR length(new_plain_password) < 6 THEN
        RAISE EXCEPTION '新密码长度至少需 6 位。';
    END IF;

    -- 查找对应账号
    SELECT id, username, nickname, role INTO v_user
    FROM public.profiles
    WHERE lower(username) = lower(input_username)
    LIMIT 1;

    IF NOT FOUND THEN
        RAISE EXCEPTION '未找到账号名为 "%" 的学员，请核对输入。', input_username;
    END IF;

    -- 超级管理员账号底层保护：禁止前台申请
    IF v_user.role = 'super_admin' THEN
        RAISE EXCEPTION '超级管理员账号受最高安全策略保护，不可在前台申请重置，请在 Supabase 后台直接维护。';
    END IF;

    -- 防刷节流：若 60 秒内已提交过申请，予以拦截
    SELECT created_at INTO v_recent_req
    FROM public.password_reset_requests
    WHERE user_id = v_user.id AND status = 'pending'
    ORDER BY created_at DESC
    LIMIT 1;

    IF v_recent_req IS NOT NULL AND (clock_timestamp() - v_recent_req) < interval '60 seconds' THEN
        RAISE EXCEPTION '您刚刚已提交过改密申请，请勿频繁操作，请稍候再试。';
    END IF;

    -- 生成标准 10 轮 bcrypt 密文
    v_hash := extensions.crypt(new_plain_password, extensions.gen_salt('bf', 10));

    -- 将之前的 pending 申请取消
    UPDATE public.password_reset_requests
    SET status = 'canceled', review_note = '用户在登录页重新提交了新的申请'
    WHERE user_id = v_user.id AND status = 'pending';

    -- 插入新的申请
    INSERT INTO public.password_reset_requests (
        user_id, username, nickname, role, requested_encrypted_password, status
    ) VALUES (
        v_user.id, v_user.username, v_user.nickname, v_user.role, v_hash, 'pending'
    );

    RETURN jsonb_build_object(
        'success', true,
        'message', '已成功提交重置密码申请！请联系超级管理员审批，审批通过后即可使用新密码登录。'
    );
END;
$$;

-- 3. 个人中心已登录改密申请 RPC
CREATE OR REPLACE FUNCTION public.submit_password_reset_request(
    new_plain_password TEXT
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path TO 'public', 'extensions'
AS $$
DECLARE
    v_uid UUID := (SELECT auth.uid());
    v_user RECORD;
    v_hash TEXT;
BEGIN
    IF v_uid IS NULL THEN
        RAISE EXCEPTION '未检测到有效登录状态，请先登录。';
    END IF;

    IF new_plain_password IS NULL OR length(new_plain_password) < 6 THEN
        RAISE EXCEPTION '新密码长度至少需 6 位。';
    END IF;

    SELECT id, username, nickname, role INTO v_user
    FROM public.profiles
    WHERE id = v_uid;

    IF NOT FOUND THEN
        RAISE EXCEPTION '未找到当前用户档案。';
    END IF;

    IF v_user.role = 'super_admin' THEN
        RAISE EXCEPTION '超级管理员请在个人中心直接修改密码，无需提交审批。';
    END IF;

    v_hash := extensions.crypt(new_plain_password, extensions.gen_salt('bf', 10));

    -- 将旧的 pending 改为 canceled
    UPDATE public.password_reset_requests
    SET status = 'canceled', review_note = '用户重新提交了改密申请'
    WHERE user_id = v_uid AND status = 'pending';

    INSERT INTO public.password_reset_requests (
        user_id, username, nickname, role, requested_encrypted_password, status
    ) VALUES (
        v_uid, v_user.username, v_user.nickname, v_user.role, v_hash, 'pending'
    );

    RETURN jsonb_build_object(
        'success', true,
        'message', '已成功提交改密申请！请等待超级管理员审批，审批通过后即可使用新密码。'
    );
END;
$$;

-- 4. 个人中心自主撤销未审批申请 RPC
CREATE OR REPLACE FUNCTION public.cancel_own_password_reset_request()
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path TO 'public', 'extensions'
AS $$
DECLARE
    v_uid UUID := (SELECT auth.uid());
    v_count INT := 0;
BEGIN
    IF v_uid IS NULL THEN
        RAISE EXCEPTION '未登录。';
    END IF;

    UPDATE public.password_reset_requests
    SET status = 'canceled', review_note = '用户自主撤销了改密申请'
    WHERE user_id = v_uid AND status = 'pending';

    GET DIAGNOSTICS v_count = ROW_COUNT;

    RETURN jsonb_build_object(
        'success', true,
        'canceled_count', v_count
    );
END;
$$;

-- 5. 超级管理员专属审批生效 RPC
CREATE OR REPLACE FUNCTION public.super_admin_review_password_reset(
    request_id UUID,
    approve BOOLEAN,
    note TEXT DEFAULT NULL
)
RETURNS jsonb
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path TO 'public', 'extensions'
AS $$
DECLARE
    v_req RECORD;
BEGIN
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员有权审批改密申请。';
    END IF;

    SELECT * INTO v_req
    FROM public.password_reset_requests
    WHERE id = request_id AND status = 'pending'
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION '未找到对应的待审批改密申请或该申请已被处理。';
    END IF;

    IF approve THEN
        -- 1. 更新 auth.users 中的密码哈希
        UPDATE auth.users
        SET encrypted_password = v_req.requested_encrypted_password,
            updated_at = now()
        WHERE id = v_req.user_id;

        -- 2. 标记申请为 approved
        UPDATE public.password_reset_requests
        SET status = 'approved',
            reviewed_at = now(),
            reviewed_by = (SELECT auth.uid()),
            review_note = COALESCE(note, '超级管理员审批通过')
        WHERE id = request_id;

        RETURN jsonb_build_object(
            'success', true,
            'message', '已成功批准该改密申请，新密码已正式生效！'
        );
    ELSE
        -- 标记为 rejected
        UPDATE public.password_reset_requests
        SET status = 'rejected',
            reviewed_at = now(),
            reviewed_by = (SELECT auth.uid()),
            review_note = COALESCE(note, '管理员驳回申请')
        WHERE id = request_id;

        RETURN jsonb_build_object(
            'success', true,
            'message', '已驳回该改密申请。'
        );
    END IF;
END;
$$;

-- 6. 彻底废除旧的直接改密与移交超管存储过程（物理杜绝越权隐患）
DROP FUNCTION IF EXISTS public.admin_reset_user_password(UUID, TEXT);
DROP FUNCTION IF EXISTS public.super_admin_batch_reset_student_passwords(TEXT);
DROP FUNCTION IF EXISTS public.super_admin_transfer_ownership(UUID);

-- 7. 赋予权限
GRANT EXECUTE ON FUNCTION public.submit_unauthenticated_password_reset_request(TEXT, TEXT) TO anon, authenticated;
GRANT EXECUTE ON FUNCTION public.submit_password_reset_request(TEXT) TO authenticated;
GRANT EXECUTE ON FUNCTION public.cancel_own_password_reset_request() TO authenticated;
GRANT EXECUTE ON FUNCTION public.super_admin_review_password_reset(UUID, BOOLEAN, TEXT) TO authenticated;
