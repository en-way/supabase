-- ==============================================================================
-- Migration: 20260921000001_security_hardening_and_user_presence.sql
-- Description: 
-- 1. Profiles: add last_active_at & create touch_user_activity()
-- 2. Tighten admin_reset_user_password to super_admin only
-- 3. Restrict exam publishing: regular admin cannot update is_published
-- 4. RLS hardening: categories, exams, passages, questions require authenticated role for SELECT
-- ==============================================================================

-- 1. Profiles: Add last_active_at
ALTER TABLE public.profiles
    ADD COLUMN IF NOT EXISTS last_active_at TIMESTAMPTZ DEFAULT now();

UPDATE public.profiles
    SET last_active_at = COALESCE(updated_at, created_at, now())
    WHERE last_active_at IS NULL;

-- Lightweight touch function with 5-minute server-side throttling to save database writes
CREATE OR REPLACE FUNCTION public.touch_user_activity()
RETURNS VOID AS $$
BEGIN
    IF auth.uid() IS NOT NULL THEN
        UPDATE public.profiles
        SET last_active_at = now()
        WHERE id = auth.uid()
          AND (last_active_at IS NULL OR last_active_at < now() - INTERVAL '5 minutes');
    END IF;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

GRANT EXECUTE ON FUNCTION public.touch_user_activity() TO authenticated;

-- 2. Restrict admin_reset_user_password to super_admin only
CREATE OR REPLACE FUNCTION public.admin_reset_user_password(target_user_id UUID, new_plain_password TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    -- Strict security: Only allow if the executing user is super_admin
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员有权执行用户密码重置操作。';
    END IF;

    UPDATE auth.users
    SET encrypted_password = crypt(new_plain_password, gen_salt('bf')),
        updated_at = now()
    WHERE id = target_user_id;

    RETURN true;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- 3. Restrict Exams Update Policy for non-super admins
DROP POLICY IF EXISTS "Admins can update exams" ON public.exams;
CREATE POLICY "Admins can update exams" ON public.exams
    FOR UPDATE TO authenticated 
    USING (public.is_admin())
    WITH CHECK (
        public.is_super_admin() 
        OR (
            public.is_admin() 
            AND is_published = (SELECT e.is_published FROM public.exams e WHERE e.id = exams.id)
        )
    );

-- 4. RLS Hardening: Require authentication for reading categories, exams, passages, questions
-- Categories
DROP POLICY IF EXISTS "Anyone can read categories" ON public.categories;
CREATE POLICY "Authenticated users can read categories" ON public.categories
    FOR SELECT TO authenticated USING (true);

-- Exams
DROP POLICY IF EXISTS "Anyone can read published exams" ON public.exams;
CREATE POLICY "Authenticated users can read published exams" ON public.exams 
    FOR SELECT TO authenticated 
    USING (
        (is_published = true AND approval_status = 'approved') 
        OR public.is_admin()
    );

-- Passages
DROP POLICY IF EXISTS "Anyone can read passages" ON public.passages;
CREATE POLICY "Authenticated users can read passages" ON public.passages 
    FOR SELECT TO authenticated USING (true);

-- Questions
DROP POLICY IF EXISTS "Anyone can read questions" ON public.questions;
CREATE POLICY "Authenticated users can read questions" ON public.questions 
    FOR SELECT TO authenticated USING (true);
