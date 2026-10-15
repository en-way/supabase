-- ==============================================================================
-- Migration: 20261012000001_security_advisor_remediation.sql
-- Description:
-- 1. Pin search_path on super_admin functions to eliminate Function Search Path Mutable warnings
-- 2. Revoke execute privileges from PUBLIC and anon on all SECURITY DEFINER functions
-- 3. Revoke execute on internal trigger functions (handle_new_user, rls_auto_enable) from authenticated
-- 4. Convert touch_user_activity to SECURITY INVOKER (since users only update their own profile)
-- ==============================================================================

-- 1. Fix mutable search paths
ALTER FUNCTION public.super_admin_batch_reset_student_passwords(TEXT) SET search_path = public;
ALTER FUNCTION public.super_admin_handle_approval(UUID, TEXT) SET search_path = public;
ALTER FUNCTION public.super_admin_update_settings(INT, BOOLEAN) SET search_path = public;
ALTER FUNCTION public.super_admin_update_announcement(BOOLEAN, TEXT, TEXT, TEXT, TEXT) SET search_path = public;

-- 2. Revoke execute from PUBLIC and anon on all SECURITY DEFINER functions (prevents unauthenticated API access)
REVOKE EXECUTE ON FUNCTION public.admin_reset_user_password(UUID, TEXT) FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.handle_new_user() FROM PUBLIC, anon, authenticated;
REVOKE EXECUTE ON FUNCTION public.is_admin() FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.is_super_admin() FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.rls_auto_enable() FROM PUBLIC, anon, authenticated;
REVOKE EXECUTE ON FUNCTION public.super_admin_batch_reset_student_passwords(TEXT) FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.super_admin_handle_approval(UUID, TEXT) FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.super_admin_set_user_role(UUID, TEXT) FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.super_admin_transfer_ownership(UUID) FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.super_admin_update_announcement(BOOLEAN, TEXT, TEXT, TEXT, TEXT) FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.super_admin_update_settings(INT, BOOLEAN) FROM PUBLIC, anon;

-- 3. touch_user_activity: switch to SECURITY INVOKER because users only update their own profile
CREATE OR REPLACE FUNCTION public.touch_user_activity()
RETURNS void AS $$
BEGIN
    UPDATE public.profiles
    SET last_seen_at = now()
    WHERE id = auth.uid();
END;
$$ LANGUAGE plpgsql SECURITY INVOKER SET search_path = public;

REVOKE EXECUTE ON FUNCTION public.touch_user_activity() FROM PUBLIC, anon;
GRANT EXECUTE ON FUNCTION public.touch_user_activity() TO authenticated;
