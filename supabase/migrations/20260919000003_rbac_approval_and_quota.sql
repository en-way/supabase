-- ==============================================================================
-- Migration: 20260919000003_rbac_approval_and_quota.sql
-- Description: RBAC (super_admin, admin, student), Exam Approval Flow, System Quotas & Password Batch Reset
-- ==============================================================================

-- 1. Update Profiles Role Constraint & Upgrade Current Admins to super_admin
ALTER TABLE public.profiles DROP CONSTRAINT IF EXISTS profiles_role_check;
ALTER TABLE public.profiles ADD CONSTRAINT profiles_role_check CHECK (role IN ('student', 'admin', 'super_admin'));

-- Ensure user 'enway' or first created admin is upgraded to super_admin
UPDATE public.profiles SET role = 'super_admin' WHERE username = 'enway' OR role = 'admin';

-- 2. Helper Security Definer Functions
CREATE OR REPLACE FUNCTION public.is_super_admin()
RETURNS BOOLEAN AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.profiles
    WHERE id = auth.uid() AND role = 'super_admin'
  );
$$ LANGUAGE sql SECURITY DEFINER SET search_path = public;

CREATE OR REPLACE FUNCTION public.is_admin()
RETURNS BOOLEAN AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.profiles
    WHERE id = auth.uid() AND role IN ('admin', 'super_admin')
  );
$$ LANGUAGE sql SECURITY DEFINER SET search_path = public;

-- 3. System Settings Table (Singleton for Quota & Registration Toggle)
CREATE TABLE IF NOT EXISTS public.system_settings (
    id INT PRIMARY KEY DEFAULT 1 CHECK (id = 1),
    max_students_limit INT NOT NULL DEFAULT 0, -- 0 = unlimited
    registration_enabled BOOLEAN NOT NULL DEFAULT true,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

INSERT INTO public.system_settings (id, max_students_limit, registration_enabled)
VALUES (1, 0, true)
ON CONFLICT (id) DO NOTHING;

ALTER TABLE public.system_settings ENABLE ROW LEVEL SECURITY;

DROP POLICY IF EXISTS "Anyone can read system settings" ON public.system_settings;
CREATE POLICY "Anyone can read system settings" ON public.system_settings
    FOR SELECT USING (true);

DROP POLICY IF EXISTS "Super admins can update system settings" ON public.system_settings;
CREATE POLICY "Super admins can update system settings" ON public.system_settings
    FOR ALL TO authenticated USING (public.is_super_admin());

-- 4. Exams Table Enhancements (Approval Status & Creator Tracking)
ALTER TABLE public.exams 
    ADD COLUMN IF NOT EXISTS approval_status TEXT NOT NULL DEFAULT 'approved' 
    CHECK (approval_status IN ('approved', 'pending_upload', 'pending_delete', 'rejected'));

ALTER TABLE public.exams 
    ADD COLUMN IF NOT EXISTS created_by UUID REFERENCES auth.users(id) ON DELETE SET NULL;

-- Update Exams RLS Policies
DROP POLICY IF EXISTS "Anyone can read published exams" ON public.exams;
CREATE POLICY "Anyone can read published exams" ON public.exams 
    FOR SELECT USING (
        (is_published = true AND approval_status = 'approved') 
        OR public.is_admin()
    );

DROP POLICY IF EXISTS "Admins can manage exams" ON public.exams;
DROP POLICY IF EXISTS "Admins can insert exams" ON public.exams;
DROP POLICY IF EXISTS "Admins can update exams" ON public.exams;
DROP POLICY IF EXISTS "Super Admins can delete exams" ON public.exams;

CREATE POLICY "Admins can insert exams" ON public.exams
    FOR INSERT TO authenticated 
    WITH CHECK (public.is_admin());

CREATE POLICY "Admins can update exams" ON public.exams
    FOR UPDATE TO authenticated 
    USING (public.is_admin())
    WITH CHECK (public.is_admin());

CREATE POLICY "Super Admins can delete exams" ON public.exams
    FOR DELETE TO authenticated 
    USING (public.is_super_admin());

-- 5. Updated handle_new_user Trigger with Quota Enforcement
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
DECLARE
    user_count INT;
    student_count INT;
    assigned_role TEXT;
    raw_user_meta JSONB;
    extracted_username TEXT;
    extracted_nickname TEXT;
    settings_limit INT := 0;
    settings_reg_enabled BOOLEAN := true;
BEGIN
    -- Check system settings
    SELECT max_students_limit, registration_enabled 
    INTO settings_limit, settings_reg_enabled
    FROM public.system_settings 
    WHERE id = 1;

    IF settings_reg_enabled = false THEN
        RAISE EXCEPTION '系统已关闭新用户注册，请联系管理员。';
    END IF;

    SELECT count(*) INTO user_count FROM public.profiles;

    IF user_count = 0 THEN
        assigned_role := 'super_admin';
    ELSE
        assigned_role := 'student';
        
        -- Check quota if limit > 0
        IF settings_limit > 0 THEN
            SELECT count(*) INTO student_count FROM public.profiles WHERE role = 'student';
            IF student_count >= settings_limit THEN
                RAISE EXCEPTION '当前注册学员人数已达系统上限（%人），暂停新用户注册。', settings_limit;
            END IF;
        END IF;
    END IF;

    raw_user_meta := NEW.raw_user_meta_data;
    extracted_username := COALESCE(raw_user_meta->>'username', split_part(NEW.email, '@', 1));
    extracted_nickname := COALESCE(raw_user_meta->>'nickname', extracted_username);

    INSERT INTO public.profiles (id, username, nickname, role, created_at, updated_at)
    VALUES (NEW.id, extracted_username, extracted_nickname, assigned_role, now(), now())
    ON CONFLICT (id) DO UPDATE SET 
        username = EXCLUDED.username,
        updated_at = now();

    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Re-attach trigger
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- 6. Super Admin RPC Functions

-- 6.1 Batch Reset Student Passwords
CREATE OR REPLACE FUNCTION public.super_admin_batch_reset_student_passwords(default_password TEXT)
RETURNS INT AS $$
DECLARE
    affected_count INT := 0;
BEGIN
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员可执行全员密码重置。';
    END IF;

    IF default_password IS NULL OR length(default_password) < 6 THEN
        RAISE EXCEPTION '重置密码长度不能少于6位。';
    END IF;

    UPDATE auth.users
    SET encrypted_password = crypt(default_password, gen_salt('bf')),
        updated_at = now()
    WHERE id IN (
        SELECT id FROM public.profiles WHERE role = 'student'
    );

    GET DIAGNOSTICS affected_count = ROW_COUNT;
    RETURN affected_count;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- 6.2 Set User Role (Assign/Revoke Normal Admin)
CREATE OR REPLACE FUNCTION public.super_admin_set_user_role(target_user_id UUID, new_role TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员可调整用户角色。';
    END IF;

    IF new_role NOT IN ('student', 'admin') THEN
        RAISE EXCEPTION '非法角色设置，仅支持设置为学员(student)或普通管理员(admin)。';
    END IF;

    IF EXISTS (SELECT 1 FROM public.profiles WHERE id = target_user_id AND role = 'super_admin') THEN
        RAISE EXCEPTION '不可修改超级管理员的角色。';
    END IF;

    UPDATE public.profiles
    SET role = new_role,
        updated_at = now()
    WHERE id = target_user_id;

    RETURN true;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- 6.3 Handle Exam Approval
CREATE OR REPLACE FUNCTION public.super_admin_handle_approval(exam_id UUID, action_type TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员可审批试卷。';
    END IF;

    IF action_type = 'approve_upload' THEN
        UPDATE public.exams 
        SET approval_status = 'approved', is_published = true 
        WHERE id = exam_id;
    ELSIF action_type = 'reject_upload' THEN
        UPDATE public.exams 
        SET approval_status = 'rejected', is_published = false 
        WHERE id = exam_id;
    ELSIF action_type = 'approve_delete' THEN
        DELETE FROM public.exams WHERE id = exam_id;
    ELSIF action_type = 'reject_delete' THEN
        UPDATE public.exams 
        SET approval_status = 'approved' 
        WHERE id = exam_id;
    ELSE
        RAISE EXCEPTION '未知的审批操作类型: %', action_type;
    END IF;

    RETURN true;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- 6.4 Update System Settings
CREATE OR REPLACE FUNCTION public.super_admin_update_settings(new_limit INT, is_enabled BOOLEAN)
RETURNS BOOLEAN AS $$
BEGIN
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员可修改系统配置。';
    END IF;

    UPDATE public.system_settings
    SET max_students_limit = GREATEST(0, new_limit),
        registration_enabled = is_enabled,
        updated_at = now()
    WHERE id = 1;

    RETURN true;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
