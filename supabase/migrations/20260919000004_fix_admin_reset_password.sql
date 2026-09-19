-- ==============================================================================
-- Migration: 20260919000004_fix_admin_reset_password.sql
-- Description: Allow Super Admin to reset individual student passwords
-- ==============================================================================

CREATE OR REPLACE FUNCTION public.admin_reset_user_password(target_user_id UUID, new_plain_password TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员可重置学员密码。';
    END IF;

    IF new_plain_password IS NULL OR length(new_plain_password) < 6 THEN
        RAISE EXCEPTION '重置密码长度不能少于6位。';
    END IF;

    UPDATE auth.users
    SET encrypted_password = crypt(new_plain_password, gen_salt('bf')),
        updated_at = now()
    WHERE id = target_user_id;

    RETURN true;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
