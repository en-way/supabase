-- ==============================================================================
-- Migration: 20260922000002_security_audit_remediation.sql
-- Description:
-- 1. Bulletproof Role Escalation Defense: Trigger on profiles preventing non-super-admin from altering 'role'
-- 2. Passages & Questions RLS Hardening: Enforce exams publication & approval checks
-- 3. Exams Column Defaults Hardening: is_published = false, approval_status = 'pending_upload'
-- 4. Search Path Fix for Privileged RPCs (Eliminate schema hijacking / Security Advisor warnings)
-- 5. Strict User Backup Storage Policy: Lock file path strictly to {auth.uid()}/backup.json
-- ==============================================================================

-- 1. Profiles: Prevent Privilege Escalation Trigger
CREATE OR REPLACE FUNCTION public.prevent_role_escalation()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.role IS DISTINCT FROM OLD.role THEN
        IF NOT public.is_super_admin() THEN
            RAISE EXCEPTION '安全策略拦截：仅超级管理员有权修改用户角色。';
        END IF;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

DROP TRIGGER IF EXISTS trg_prevent_role_escalation ON public.profiles;
CREATE TRIGGER trg_prevent_role_escalation
    BEFORE UPDATE ON public.profiles
    FOR EACH ROW
    EXECUTE FUNCTION public.prevent_role_escalation();

-- 2. Exams Defaults Hardening
ALTER TABLE public.exams 
    ALTER COLUMN is_published SET DEFAULT false;

ALTER TABLE public.exams 
    ALTER COLUMN approval_status SET DEFAULT 'pending_upload';

-- 3. Passages & Questions RLS Hardening (Only approved & published exams or admin)
DROP POLICY IF EXISTS "Authenticated users can read passages" ON public.passages;
DROP POLICY IF EXISTS "Authenticated users can read approved passages" ON public.passages;
CREATE POLICY "Authenticated users can read approved passages" ON public.passages 
    FOR SELECT TO authenticated 
    USING (
        public.is_admin() 
        OR EXISTS (
            SELECT 1 FROM public.exams e 
            WHERE e.id = passages.exam_id 
              AND e.is_published = true 
              AND e.approval_status = 'approved'
        )
    );

DROP POLICY IF EXISTS "Authenticated users can read questions" ON public.questions;
DROP POLICY IF EXISTS "Authenticated users can read approved questions" ON public.questions;
CREATE POLICY "Authenticated users can read approved questions" ON public.questions 
    FOR SELECT TO authenticated 
    USING (
        public.is_admin() 
        OR EXISTS (
            SELECT 1 FROM public.exams e 
            WHERE e.id = questions.exam_id 
              AND e.is_published = true 
              AND e.approval_status = 'approved'
        )
    );

-- 4. Fix search_path = public on Privileged SECURITY DEFINER RPCs

-- 4.1 Batch Reset Student Passwords
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
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- 4.2 Set User Role
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
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- 4.3 Handle Exam Approval
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
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- 4.4 Update System Settings
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
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- 4.5 Update Sitewide Announcement
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
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- 5. Tighten User Backup Storage Policy: Strictly Single Path {auth.uid()}/backup.json
-- Prevents directory bloat or arbitrary multi-file abuse consuming bucket quota

DROP POLICY IF EXISTS "Users can upload own backups to storage" ON storage.objects;
CREATE POLICY "Users can upload own backups to storage" ON storage.objects
    FOR INSERT TO authenticated
    WITH CHECK (
        bucket_id = 'user-backups' 
        AND name = (auth.uid()::text || '/backup.json')
    );

DROP POLICY IF EXISTS "Users can update own backups in storage" ON storage.objects;
CREATE POLICY "Users can update own backups in storage" ON storage.objects
    FOR UPDATE TO authenticated
    USING (
        bucket_id = 'user-backups' 
        AND name = (auth.uid()::text || '/backup.json')
    )
    WITH CHECK (
        bucket_id = 'user-backups' 
        AND name = (auth.uid()::text || '/backup.json')
    );

DROP POLICY IF EXISTS "Users can read own backups from storage" ON storage.objects;
CREATE POLICY "Users can read own backups from storage" ON storage.objects
    FOR SELECT TO authenticated
    USING (
        bucket_id = 'user-backups' 
        AND (
            name = (auth.uid()::text || '/backup.json')
            OR (public.is_super_admin() AND (storage.foldername(name))[1] = 'admin-analytics')
        )
    );

DROP POLICY IF EXISTS "Users can delete own backups from storage" ON storage.objects;
CREATE POLICY "Users can delete own backups from storage" ON storage.objects
    FOR DELETE TO authenticated
    USING (
        bucket_id = 'user-backups' 
        AND name = (auth.uid()::text || '/backup.json')
    );
