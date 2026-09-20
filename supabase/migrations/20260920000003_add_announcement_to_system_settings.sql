-- Migration: Add sitewide announcement support to public.system_settings

ALTER TABLE public.system_settings
  ADD COLUMN IF NOT EXISTS announcement_enabled BOOLEAN DEFAULT false,
  ADD COLUMN IF NOT EXISTS announcement_text TEXT DEFAULT '',
  ADD COLUMN IF NOT EXISTS announcement_type TEXT DEFAULT 'info',
  ADD COLUMN IF NOT EXISTS announcement_link_text TEXT DEFAULT '',
  ADD COLUMN IF NOT EXISTS announcement_link_url TEXT DEFAULT '',
  ADD COLUMN IF NOT EXISTS announcement_updated_at TIMESTAMPTZ DEFAULT now();

COMMENT ON COLUMN public.system_settings.announcement_enabled IS '全站公告置顶展示开关 (true:开启展示 | false:关闭隐藏)';
COMMENT ON COLUMN public.system_settings.announcement_text IS '全站公告正文文案';
COMMENT ON COLUMN public.system_settings.announcement_type IS '全站公告主题级别 (info:信息蓝 | warning:警示黄 | alert:紧急红)';
COMMENT ON COLUMN public.system_settings.announcement_link_text IS '全站公告附带的操作按钮文字 (可选)';
COMMENT ON COLUMN public.system_settings.announcement_link_url IS '全站公告附带的跳转链接 (可选)';
COMMENT ON COLUMN public.system_settings.announcement_updated_at IS '全站公告最后发布或修改时间戳 (用于客户端智能唤醒)';

-- RPC for super admin to update announcement atomically
CREATE OR REPLACE FUNCTION public.super_admin_update_announcement(
    p_enabled BOOLEAN,
    p_text TEXT,
    p_type TEXT,
    p_link_text TEXT,
    p_link_url TEXT
)
RETURNS BOOLEAN AS $$
BEGIN
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员可发布与修改全站公告。';
    END IF;

    UPDATE public.system_settings
    SET announcement_enabled = p_enabled,
        announcement_text = COALESCE(p_text, ''),
        announcement_type = COALESCE(p_type, 'info'),
        announcement_link_text = COALESCE(p_link_text, ''),
        announcement_link_url = COALESCE(p_link_url, ''),
        announcement_updated_at = now(),
        updated_at = now()
    WHERE id = 1;

    RETURN true;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
