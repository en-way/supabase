-- ==============================================================================
-- Migration: 20260920000002_enforce_single_super_admin.sql
-- Description: Enforce strictly single super_admin via partial unique index,
--              atomic ownership transfer RPC, and trigger safeguards.
-- ==============================================================================

-- 1. Ensure clean state: if multiple super_admins exist, retain primary 'enway'
UPDATE public.profiles 
SET role = 'admin', updated_at = now() 
WHERE role = 'super_admin' AND username != 'enway';

-- If no 'enway', keep the oldest super_admin and demote others
WITH oldest_super AS (
    SELECT id FROM public.profiles WHERE role = 'super_admin' ORDER BY created_at ASC LIMIT 1
)
UPDATE public.profiles
SET role = 'admin', updated_at = now()
WHERE role = 'super_admin' AND id NOT IN (SELECT id FROM oldest_super);

-- 2. Create Partial Unique Index (Physical DB Engine Hard Enforcement)
-- Under NO circumstances can more than one profile have role = 'super_admin'
DROP INDEX IF EXISTS public.unique_super_admin_idx;
CREATE UNIQUE INDEX unique_super_admin_idx 
ON public.profiles ((role)) 
WHERE role = 'super_admin';

-- 3. Atomic Ownership Transfer RPC (Safe hand-off between super_admin and admin)
CREATE OR REPLACE FUNCTION public.super_admin_transfer_ownership(target_admin_id UUID)
RETURNS JSONB AS $$
DECLARE
    caller_id UUID;
    target_profile RECORD;
BEGIN
    caller_id := auth.uid();

    -- Must be authenticated and currently a super_admin
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅当前超级管理员可执行超级管理员所有权转让。';
    END IF;

    IF target_admin_id IS NULL OR target_admin_id = caller_id THEN
        RAISE EXCEPTION '转让失败：目标用户不能为自己或空。';
    END IF;

    -- Verify target user exists and is a normal administrator
    SELECT id, username, nickname, role INTO target_profile
    FROM public.profiles
    WHERE id = target_admin_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION '转让失败：目标用户不存在。';
    END IF;

    IF target_profile.role != 'admin' THEN
        RAISE EXCEPTION '转让失败：只能将超级管理员权限转让给已存在的普通管理员。请先在列表中将其设为普通管理员。';
    END IF;

    -- Step A: Demote caller to 'admin' first, freeing up the single super_admin slot
    UPDATE public.profiles
    SET role = 'admin', updated_at = now()
    WHERE id = caller_id;

    -- Step B: Promote target to 'super_admin'
    UPDATE public.profiles
    SET role = 'super_admin', updated_at = now()
    WHERE id = target_admin_id;

    RETURN jsonb_build_object(
        'success', true,
        'message', '超级管理员所有权转让成功。原超级管理员已自动调整为普通管理员。',
        'previous_super_admin_id', caller_id,
        'new_super_admin_id', target_admin_id,
        'new_super_admin_username', target_profile.username
    );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- 4. Harden super_admin_set_user_role: Prohibit setting super_admin directly
CREATE OR REPLACE FUNCTION public.super_admin_set_user_role(target_user_id UUID, new_role TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    IF NOT public.is_super_admin() THEN
        RAISE EXCEPTION '权限不足：仅超级管理员可调整用户角色。';
    END IF;

    IF new_role = 'super_admin' THEN
        RAISE EXCEPTION '系统安全限制：全站超级管理员席位绝对唯一，不可直接指定。若需交接，请使用专门的“转让超级管理员”功能。';
    END IF;

    IF new_role NOT IN ('student', 'admin') THEN
        RAISE EXCEPTION '非法角色设置，仅支持设置为学员(student)或普通管理员(admin)。';
    END IF;

    IF EXISTS (SELECT 1 FROM public.profiles WHERE id = target_user_id AND role = 'super_admin') THEN
        RAISE EXCEPTION '不可直接修改超级管理员角色。请通过所有权转让功能完成交接。';
    END IF;

    UPDATE public.profiles
    SET role = new_role,
        updated_at = now()
    WHERE id = target_user_id;

    RETURN true;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;

-- 5. Safeguard handle_new_user: strictly check for existing super_admin
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
DECLARE
    super_admin_count INT;
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

    -- Strictly check if ANY super_admin exists
    SELECT count(*) INTO super_admin_count FROM public.profiles WHERE role = 'super_admin';

    IF super_admin_count = 0 THEN
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
$$ LANGUAGE plpgsql SECURITY DEFINER SET search_path = public;
