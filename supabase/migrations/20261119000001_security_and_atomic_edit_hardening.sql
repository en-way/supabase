-- ==============================================================================
-- Migration: 20261119000001_security_and_atomic_edit_hardening.sql
-- Description:
-- 1. Separate profiles RLS policies & lock super_admin against deletion
-- 2. Add anonymous-safe get_registration_quota_status() RPC
-- 3. Harden exams / passages / questions RLS approval boundaries
-- 4. Restore Storage single-file {auth.uid()}/backup.json lock (with InitPlan)
-- 5. Restore touch_user_activity() 5-min server throttle & tighten user_backups RLS
-- 6. Revoke excessive RPC execute privileges & hide encrypted password request column
-- 7. Add transactional admin_save_exam_payload() RPC preserving existing UUIDs
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 1. public.profiles RLS Separation & super_admin Deletion Protection
-- ------------------------------------------------------------------------------
DROP POLICY IF EXISTS "Authenticated can read profiles" ON public.profiles;
DROP POLICY IF EXISTS "Admins can manage any profile" ON public.profiles;
DROP POLICY IF EXISTS "Users can update own profile" ON public.profiles;
DROP POLICY IF EXISTS "Users can read own profile" ON public.profiles;
DROP POLICY IF EXISTS "Super admins can delete non-super profiles" ON public.profiles;

CREATE POLICY "Users can read own profile" ON public.profiles
    FOR SELECT TO authenticated
    USING (
        ((select auth.uid()) = id)
        OR public.is_admin()
    );

CREATE POLICY "Users can update own profile" ON public.profiles
    FOR UPDATE TO authenticated
    USING (
        ((select auth.uid()) = id)
        OR public.is_super_admin()
    )
    WITH CHECK (
        ((select auth.uid()) = id)
        OR public.is_super_admin()
    );

CREATE POLICY "Super admins can delete non-super profiles" ON public.profiles
    FOR DELETE TO authenticated
    USING (
        public.is_super_admin()
        AND role <> 'super_admin'
    );

CREATE OR REPLACE FUNCTION public.prevent_super_admin_deletion()
RETURNS TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
    IF OLD.role = 'super_admin' AND (select auth.uid()) IS NOT NULL THEN
        RAISE EXCEPTION '安全策略拦截：超级管理员账号受底层保护，禁止通过接口删除。';
    END IF;
    RETURN OLD;
END;
$$;

DROP TRIGGER IF EXISTS trg_prevent_super_admin_deletion ON public.profiles;
CREATE TRIGGER trg_prevent_super_admin_deletion
    BEFORE DELETE ON public.profiles
    FOR EACH ROW
    EXECUTE FUNCTION public.prevent_super_admin_deletion();

REVOKE EXECUTE ON FUNCTION public.prevent_super_admin_deletion() FROM PUBLIC, anon, authenticated;

-- ------------------------------------------------------------------------------
-- 2. Anonymous-Safe Registration Quota RPC
-- ------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.get_registration_quota_status()
RETURNS JSONB
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
    v_limit INT := 0;
    v_enabled BOOLEAN := true;
    v_student_count INT := 0;
BEGIN
    SELECT max_students_limit, registration_enabled
    INTO v_limit, v_enabled
    FROM public.system_settings
    WHERE id = 1;

    v_limit := COALESCE(v_limit, 0);
    v_enabled := COALESCE(v_enabled, true);

    IF v_limit > 0 THEN
        SELECT count(*)::INT INTO v_student_count
        FROM public.profiles
        WHERE role = 'student';
    END IF;

    RETURN jsonb_build_object(
        'registration_enabled', v_enabled,
        'max_students_limit', v_limit,
        'current_student_count', v_student_count,
        'is_full', (v_limit > 0 AND v_student_count >= v_limit)
    );
END;
$$;

REVOKE EXECUTE ON FUNCTION public.get_registration_quota_status() FROM PUBLIC;
GRANT EXECUTE ON FUNCTION public.get_registration_quota_status() TO anon, authenticated;

-- ------------------------------------------------------------------------------
-- 3. Exams / Passages / Questions Approval Boundary Hardening
-- ------------------------------------------------------------------------------
DROP POLICY IF EXISTS "Admins can insert exams" ON public.exams;
CREATE POLICY "Admins can insert exams" ON public.exams
    FOR INSERT TO authenticated
    WITH CHECK (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND is_published = false
            AND approval_status = 'pending_upload'
            AND (created_by IS NULL OR created_by = (select auth.uid()))
        )
    );

DROP POLICY IF EXISTS "Admins can update exams" ON public.exams;
CREATE POLICY "Admins can update exams" ON public.exams
    FOR UPDATE TO authenticated
    USING (public.is_admin())
    WITH CHECK (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND is_published = (SELECT e.is_published FROM public.exams e WHERE e.id = exams.id)
            AND (
                (
                    (SELECT e.approval_status FROM public.exams e WHERE e.id = exams.id) IN ('pending_upload', 'rejected')
                    AND is_published = false
                    AND approval_status IN ('pending_upload', 'rejected')
                )
                OR (
                    (SELECT e.approval_status FROM public.exams e WHERE e.id = exams.id) = 'approved'
                    AND approval_status = 'pending_delete'
                )
            )
        )
    );

DROP POLICY IF EXISTS "Admins can manage passages" ON public.passages;
DROP POLICY IF EXISTS "Admins can insert passages" ON public.passages;
DROP POLICY IF EXISTS "Admins can update passages" ON public.passages;
DROP POLICY IF EXISTS "Admins can delete passages" ON public.passages;

CREATE POLICY "Admins can insert passages" ON public.passages
    FOR INSERT TO authenticated
    WITH CHECK (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND EXISTS (
                SELECT 1 FROM public.exams e
                WHERE e.id = passages.exam_id
                  AND e.is_published = false
                  AND e.approval_status IN ('pending_upload', 'rejected')
            )
        )
    );

CREATE POLICY "Admins can update passages" ON public.passages
    FOR UPDATE TO authenticated
    USING (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND EXISTS (
                SELECT 1 FROM public.exams e
                WHERE e.id = passages.exam_id
                  AND e.is_published = false
                  AND e.approval_status IN ('pending_upload', 'rejected')
            )
        )
    )
    WITH CHECK (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND EXISTS (
                SELECT 1 FROM public.exams e
                WHERE e.id = passages.exam_id
                  AND e.is_published = false
                  AND e.approval_status IN ('pending_upload', 'rejected')
            )
        )
    );

CREATE POLICY "Admins can delete passages" ON public.passages
    FOR DELETE TO authenticated
    USING (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND EXISTS (
                SELECT 1 FROM public.exams e
                WHERE e.id = passages.exam_id
                  AND e.is_published = false
                  AND e.approval_status IN ('pending_upload', 'rejected')
            )
        )
    );

DROP POLICY IF EXISTS "Admins can manage questions" ON public.questions;
DROP POLICY IF EXISTS "Admins can insert questions" ON public.questions;
DROP POLICY IF EXISTS "Admins can update questions" ON public.questions;
DROP POLICY IF EXISTS "Admins can delete questions" ON public.questions;

CREATE POLICY "Admins can insert questions" ON public.questions
    FOR INSERT TO authenticated
    WITH CHECK (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND EXISTS (
                SELECT 1 FROM public.exams e
                WHERE e.id = questions.exam_id
                  AND e.is_published = false
                  AND e.approval_status IN ('pending_upload', 'rejected')
            )
        )
    );

CREATE POLICY "Admins can update questions" ON public.questions
    FOR UPDATE TO authenticated
    USING (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND EXISTS (
                SELECT 1 FROM public.exams e
                WHERE e.id = questions.exam_id
                  AND e.is_published = false
                  AND e.approval_status IN ('pending_upload', 'rejected')
            )
        )
    )
    WITH CHECK (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND EXISTS (
                SELECT 1 FROM public.exams e
                WHERE e.id = questions.exam_id
                  AND e.is_published = false
                  AND e.approval_status IN ('pending_upload', 'rejected')
            )
        )
    );

CREATE POLICY "Admins can delete questions" ON public.questions
    FOR DELETE TO authenticated
    USING (
        public.is_super_admin()
        OR (
            public.is_admin()
            AND EXISTS (
                SELECT 1 FROM public.exams e
                WHERE e.id = questions.exam_id
                  AND e.is_published = false
                  AND e.approval_status IN ('pending_upload', 'rejected')
            )
        )
    );

-- ------------------------------------------------------------------------------
-- 4. Storage Single-File Backup Lock (with InitPlan) & Analytics Snapshot Policy
-- ------------------------------------------------------------------------------
DROP POLICY IF EXISTS "Users can read own backups from storage" ON storage.objects;
DROP POLICY IF EXISTS "Users can upload own backups to storage" ON storage.objects;
DROP POLICY IF EXISTS "Users can update own backups in storage" ON storage.objects;
DROP POLICY IF EXISTS "Users can delete own backups from storage" ON storage.objects;
DROP POLICY IF EXISTS "Super admins can manage admin-analytics snapshot" ON storage.objects;
DROP POLICY IF EXISTS "Super Admins can manage analytics snapshots" ON storage.objects;

CREATE POLICY "Users can read own backups from storage" ON storage.objects
    FOR SELECT TO authenticated
    USING (
        bucket_id = 'user-backups'
        AND name = (((select auth.uid())::text) || '/backup.json')
    );

CREATE POLICY "Users can upload own backups to storage" ON storage.objects
    FOR INSERT TO authenticated
    WITH CHECK (
        bucket_id = 'user-backups'
        AND name = (((select auth.uid())::text) || '/backup.json')
    );

CREATE POLICY "Users can update own backups in storage" ON storage.objects
    FOR UPDATE TO authenticated
    USING (
        bucket_id = 'user-backups'
        AND name = (((select auth.uid())::text) || '/backup.json')
    )
    WITH CHECK (
        bucket_id = 'user-backups'
        AND name = (((select auth.uid())::text) || '/backup.json')
    );

CREATE POLICY "Users can delete own backups from storage" ON storage.objects
    FOR DELETE TO authenticated
    USING (
        bucket_id = 'user-backups'
        AND name = (((select auth.uid())::text) || '/backup.json')
    );

CREATE POLICY "Super admins can manage admin-analytics snapshot" ON storage.objects
    FOR ALL TO authenticated
    USING (
        bucket_id = 'user-backups'
        AND name = 'admin-analytics/snapshot.json'
        AND public.is_super_admin()
    )
    WITH CHECK (
        bucket_id = 'user-backups'
        AND name = 'admin-analytics/snapshot.json'
        AND public.is_super_admin()
    );

-- ------------------------------------------------------------------------------
-- 5. Restore touch_user_activity() 5-Min Server Throttle & Tighten user_backups RLS
-- ------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.touch_user_activity()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
    IF (select auth.uid()) IS NOT NULL THEN
        UPDATE public.profiles
        SET last_active_at = now()
        WHERE id = (select auth.uid())
          AND (last_active_at IS NULL OR last_active_at < now() - INTERVAL '5 minutes');
    END IF;
END;
$$;

DROP POLICY IF EXISTS "Users can manage own backup" ON public.user_backups;
CREATE POLICY "Users can manage own backup" ON public.user_backups
    FOR ALL TO authenticated
    USING ((select auth.uid()) = user_id)
    WITH CHECK ((select auth.uid()) = user_id);

DROP POLICY IF EXISTS "Super admins can read backup metadata" ON public.user_backups;
CREATE POLICY "Super admins can read backup metadata" ON public.user_backups
    FOR SELECT TO authenticated
    USING (public.is_super_admin());

-- ------------------------------------------------------------------------------
-- 6. Revoke Excessive RPC Privileges & Restrict Password Hash Column SELECT
-- ------------------------------------------------------------------------------
REVOKE EXECUTE ON FUNCTION public.sync_exams_to_cloudflare() FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.submit_password_reset_request(TEXT) FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.cancel_own_password_reset_request() FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.super_admin_review_password_reset(UUID, BOOLEAN, TEXT) FROM PUBLIC, anon;
REVOKE EXECUTE ON FUNCTION public.submit_unauthenticated_password_reset_request(TEXT, TEXT) FROM PUBLIC;
GRANT EXECUTE ON FUNCTION public.submit_unauthenticated_password_reset_request(TEXT, TEXT) TO anon, authenticated;
REVOKE EXECUTE ON FUNCTION public.touch_user_activity() FROM PUBLIC, anon;
GRANT EXECUTE ON FUNCTION public.touch_user_activity() TO authenticated;

-- Restore prevent_role_escalation() + trigger if missing on remote DB
CREATE OR REPLACE FUNCTION public.prevent_role_escalation()
RETURNS TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
    IF NEW.role IS DISTINCT FROM OLD.role THEN
        IF NOT public.is_super_admin() THEN
            RAISE EXCEPTION '安全策略拦截：仅超级管理员有权修改用户角色。';
        END IF;
    END IF;
    RETURN NEW;
END;
$$;

DROP TRIGGER IF EXISTS trg_prevent_role_escalation ON public.profiles;
CREATE TRIGGER trg_prevent_role_escalation
    BEFORE UPDATE ON public.profiles
    FOR EACH ROW
    EXECUTE FUNCTION public.prevent_role_escalation();

REVOKE EXECUTE ON FUNCTION public.prevent_role_escalation() FROM PUBLIC, anon, authenticated;

REVOKE SELECT ON public.password_reset_requests FROM anon, authenticated;
GRANT SELECT (id, user_id, username, nickname, role, status, created_at, reviewed_at, review_note)
    ON public.password_reset_requests TO authenticated;

-- ------------------------------------------------------------------------------
-- 7. Transactional Atomic Exam Payload Editor RPC (Preserves Passage/Question UUIDs)
-- ------------------------------------------------------------------------------
CREATE OR REPLACE FUNCTION public.admin_save_exam_payload(
    p_exam_id UUID,
    p_payload JSONB
)
RETURNS JSONB
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
DECLARE
    v_exam RECORD;
    v_title TEXT;
    v_category_id TEXT;
    v_year INT;
    v_exam_type TEXT;
    v_duration INT;
    v_total_score NUMERIC(5,2);
    v_pass_score NUMERIC(5,2);

    v_kept_passage_ids UUID[] := ARRAY[]::UUID[];
    v_kept_question_ids UUID[] := ARRAY[]::UUID[];

    v_p JSONB;
    v_p_ord INT;
    v_raw_p_id TEXT;
    v_p_uuid UUID;
    v_p_section_type TEXT;
    v_p_title TEXT;
    v_p_content TEXT;
    v_p_sort_order INT;

    v_q JSONB;
    v_q_ord INT;
    v_raw_q_id TEXT;
    v_q_uuid UUID;
    v_q_type TEXT;
    v_q_stem TEXT;
    v_q_options JSONB;
    v_q_correct TEXT;
    v_q_explanation TEXT;
    v_q_points NUMERIC(5,2);
    v_q_sort_order INT;
BEGIN
    IF NOT public.is_admin() THEN
        RAISE EXCEPTION '权限不足：仅管理员有权编辑试卷内容。';
    END IF;

    IF p_exam_id IS NULL THEN
        RAISE EXCEPTION '试卷 ID 不能为空。';
    END IF;

    IF p_payload IS NULL OR jsonb_typeof(p_payload) <> 'object' THEN
        RAISE EXCEPTION '提交的试卷 JSON 必须为有效对象。';
    END IF;

    SELECT * INTO v_exam
    FROM public.exams
    WHERE id = p_exam_id
    FOR UPDATE;

    IF NOT FOUND THEN
        RAISE EXCEPTION '未找到指定试卷 (id=%)。', p_exam_id;
    END IF;

    IF NOT public.is_super_admin() AND (v_exam.approval_status = 'approved' OR v_exam.is_published = true) THEN
        RAISE EXCEPTION '权限不足：已审核发布的试卷仅超级管理员可修改内容。';
    END IF;

    v_title := trim(COALESCE(p_payload->>'title', ''));
    IF length(v_title) = 0 THEN
        RAISE EXCEPTION '试卷标题 title 不能为空。';
    END IF;

    v_category_id := trim(COALESCE(p_payload->>'category_id', ''));
    IF length(v_category_id) = 0 OR NOT EXISTS (SELECT 1 FROM public.categories WHERE id = v_category_id) THEN
        RAISE EXCEPTION '试卷科目分类 category_id 无效: %', v_category_id;
    END IF;

    IF (p_payload ? 'year') AND NULLIF(trim(COALESCE(p_payload->>'year', '')), '') IS NOT NULL THEN
        v_year := (p_payload->>'year')::INT;
    ELSE
        v_year := v_exam.year;
    END IF;

    v_exam_type := COALESCE(NULLIF(trim(COALESCE(p_payload->>'exam_type', '')), ''), 'real');
    IF v_exam_type NOT IN ('real', 'mock') THEN
        RAISE EXCEPTION '试卷类型 exam_type 必须为 real 或 mock。';
    END IF;

    v_duration := COALESCE(NULLIF(trim(COALESCE(p_payload->>'duration_minutes', '')), '')::INT, 75);
    IF v_duration <= 0 THEN
        RAISE EXCEPTION '考试时长 duration_minutes 必须大于 0。';
    END IF;

    v_total_score := COALESCE(NULLIF(trim(COALESCE(p_payload->>'total_score', '')), '')::NUMERIC, 60.00);
    IF v_total_score <= 0 THEN
        RAISE EXCEPTION '试卷总分 total_score 必须大于 0。';
    END IF;

    v_pass_score := COALESCE(NULLIF(trim(COALESCE(p_payload->>'pass_score', '')), '')::NUMERIC, 36.00);
    IF v_pass_score < 0 THEN
        RAISE EXCEPTION '及格线 pass_score 不能为负数。';
    END IF;

    IF jsonb_typeof(p_payload->'passages') <> 'array' THEN
        RAISE EXCEPTION 'passages 字段必须为 JSON 数组。';
    END IF;

    -- Update main exam metadata (never alters is_published / approval_status / created_by)
    UPDATE public.exams
    SET title = v_title,
        category_id = v_category_id,
        year = v_year,
        exam_type = v_exam_type,
        duration_minutes = v_duration,
        total_score = v_total_score,
        pass_score = v_pass_score
    WHERE id = p_exam_id;

    -- Upsert passages in place to preserve existing passage UUIDs
    FOR v_p, v_p_ord IN
        SELECT elem, ord::INT
        FROM jsonb_array_elements(p_payload->'passages') WITH ORDINALITY AS t(elem, ord)
    LOOP
        IF jsonb_typeof(v_p) <> 'object' THEN
            RAISE EXCEPTION '第 % 个篇章格式必须为 JSON 对象。', v_p_ord;
        END IF;

        v_p_section_type := COALESCE(NULLIF(trim(COALESCE(v_p->>'section_type', '')), ''), 'reading');
        IF v_p_section_type NOT IN ('reading', 'cloze', 'single') THEN
            RAISE EXCEPTION '第 % 个篇章的 section_type 不合法: %', v_p_ord, v_p_section_type;
        END IF;

        v_p_title := COALESCE(NULLIF(trim(COALESCE(v_p->>'title', '')), ''), 'Passage ' || v_p_ord);
        v_p_content := COALESCE(v_p->>'content', '');
        v_p_sort_order := COALESCE(NULLIF(trim(COALESCE(v_p->>'sort_order', '')), '')::INT, v_p_ord);

        v_raw_p_id := NULLIF(trim(COALESCE(v_p->>'id', '')), '');
        v_p_uuid := NULL;
        IF v_raw_p_id ~* '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$' THEN
            SELECT id INTO v_p_uuid
            FROM public.passages
            WHERE id = v_raw_p_id::UUID AND exam_id = p_exam_id;
        END IF;

        IF v_p_uuid IS NOT NULL THEN
            IF v_p_uuid = ANY(v_kept_passage_ids) THEN
                RAISE EXCEPTION '检测到重复的篇章 ID: %', v_p_uuid;
            END IF;
            UPDATE public.passages
            SET category_id = v_category_id,
                section_type = v_p_section_type,
                title = v_p_title,
                content = v_p_content,
                sort_order = v_p_sort_order
            WHERE id = v_p_uuid AND exam_id = p_exam_id;
        ELSE
            INSERT INTO public.passages (exam_id, category_id, section_type, title, content, sort_order)
            VALUES (p_exam_id, v_category_id, v_p_section_type, v_p_title, v_p_content, v_p_sort_order)
            RETURNING id INTO v_p_uuid;
        END IF;

        v_kept_passage_ids := array_append(v_kept_passage_ids, v_p_uuid);

        -- Upsert child questions under this passage preserving existing question UUIDs
        IF (v_p ? 'questions') AND jsonb_typeof(v_p->'questions') <> 'null' THEN
            IF jsonb_typeof(v_p->'questions') <> 'array' THEN
                RAISE EXCEPTION '第 % 个篇章的 questions 必须为 JSON 数组。', v_p_ord;
            END IF;

            FOR v_q, v_q_ord IN
                SELECT elem, ord::INT
                FROM jsonb_array_elements(v_p->'questions') WITH ORDINALITY AS t(elem, ord)
            LOOP
                IF jsonb_typeof(v_q) <> 'object' THEN
                    RAISE EXCEPTION '第 % 个篇章的第 % 道题目格式必须为 JSON 对象。', v_p_ord, v_q_ord;
                END IF;

                v_q_stem := trim(COALESCE(v_q->>'stem', ''));
                IF length(v_q_stem) = 0 THEN
                    RAISE EXCEPTION '第 % 个篇章的第 % 道题目缺少题干 stem。', v_p_ord, v_q_ord;
                END IF;

                v_q_options := v_q->'options';
                IF v_q_options IS NULL OR jsonb_typeof(v_q_options) = 'null' THEN
                    RAISE EXCEPTION '第 % 个篇章的第 % 道题目缺少 options 选项。', v_p_ord, v_q_ord;
                END IF;

                v_q_correct := trim(COALESCE(v_q->>'correct_answer', ''));
                IF length(v_q_correct) = 0 THEN
                    RAISE EXCEPTION '第 % 个篇章的第 % 道题目缺少正确答案 correct_answer。', v_p_ord, v_q_ord;
                END IF;

                v_q_type := COALESCE(NULLIF(trim(COALESCE(v_q->>'q_type', '')), ''), 'reading_item');
                IF v_q_type NOT IN ('choice', 'cloze_item', 'reading_item') THEN
                    RAISE EXCEPTION '第 % 个篇章的第 % 道题目 q_type 不合法: %', v_p_ord, v_q_ord, v_q_type;
                END IF;

                v_q_explanation := COALESCE(NULLIF(trim(COALESCE(v_q->>'explanation', '')), ''), '暂无详细解析');
                v_q_points := COALESCE(NULLIF(trim(COALESCE(v_q->>'points', '')), '')::NUMERIC, 2.00);
                IF v_q_points < 0 THEN
                    RAISE EXCEPTION '第 % 个篇章的第 % 道题目分值 points 不能为负数。', v_p_ord, v_q_ord;
                END IF;

                v_q_sort_order := COALESCE(NULLIF(trim(COALESCE(v_q->>'sort_order', '')), '')::INT, v_q_ord);

                v_raw_q_id := NULLIF(trim(COALESCE(v_q->>'id', '')), '');
                v_q_uuid := NULL;
                IF v_raw_q_id ~* '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$' THEN
                    SELECT id INTO v_q_uuid
                    FROM public.questions
                    WHERE id = v_raw_q_id::UUID AND exam_id = p_exam_id;
                END IF;

                IF v_q_uuid IS NOT NULL THEN
                    IF v_q_uuid = ANY(v_kept_question_ids) THEN
                        RAISE EXCEPTION '检测到重复的题目 ID: %', v_q_uuid;
                    END IF;
                    UPDATE public.questions
                    SET passage_id = v_p_uuid,
                        category_id = v_category_id,
                        q_type = v_q_type,
                        stem = v_q_stem,
                        options = v_q_options,
                        correct_answer = v_q_correct,
                        explanation = v_q_explanation,
                        points = v_q_points,
                        sort_order = v_q_sort_order
                    WHERE id = v_q_uuid AND exam_id = p_exam_id;
                ELSE
                    INSERT INTO public.questions (
                        exam_id, passage_id, category_id, q_type,
                        stem, options, correct_answer, explanation, points, sort_order
                    )
                    VALUES (
                        p_exam_id, v_p_uuid, v_category_id, v_q_type,
                        v_q_stem, v_q_options, v_q_correct, v_q_explanation, v_q_points, v_q_sort_order
                    )
                    RETURNING id INTO v_q_uuid;
                END IF;

                v_kept_question_ids := array_append(v_kept_question_ids, v_q_uuid);
            END LOOP;
        END IF;
    END LOOP;

    -- Remove omitted questions first, then omitted passages
    DELETE FROM public.questions
    WHERE exam_id = p_exam_id
      AND NOT (id = ANY(v_kept_question_ids));

    DELETE FROM public.passages
    WHERE exam_id = p_exam_id
      AND NOT (id = ANY(v_kept_passage_ids));

    RETURN jsonb_build_object(
        'success', true,
        'exam_id', p_exam_id,
        'passages_count', COALESCE(array_length(v_kept_passage_ids, 1), 0),
        'questions_count', COALESCE(array_length(v_kept_question_ids, 1), 0)
    );
END;
$$;

REVOKE EXECUTE ON FUNCTION public.admin_save_exam_payload(UUID, JSONB) FROM PUBLIC, anon;
GRANT EXECUTE ON FUNCTION public.admin_save_exam_payload(UUID, JSONB) TO authenticated;
