-- ==============================================================================
-- Migration: 20260922000001_performance_indexes_and_storage_policy.sql
-- Description:
-- 1. B-Tree Indexes on Foreign Keys and High-Frequency Query Fields
--    (Eliminates Full Table Scans for exams, passages, questions, profiles)
-- 2. Storage Bucket Policy for 'admin-analytics' (Allows Super Admin snapshot sync)
-- ==============================================================================

-- 1. Questions Table Indexes
-- Critical: Accelerates questions(count) aggregation, passage join, and exam loading
CREATE INDEX IF NOT EXISTS idx_questions_exam_id_sort 
ON public.questions (exam_id, sort_order);

CREATE INDEX IF NOT EXISTS idx_questions_passage_id 
ON public.questions (passage_id);

CREATE INDEX IF NOT EXISTS idx_questions_category_id 
ON public.questions (category_id);

-- 2. Passages Table Indexes
-- Critical: Accelerates passages(count) aggregation and exam detail queries
CREATE INDEX IF NOT EXISTS idx_passages_exam_id_sort 
ON public.passages (exam_id, sort_order);

CREATE INDEX IF NOT EXISTS idx_passages_category_id 
ON public.passages (category_id);

-- 3. Exams Table Indexes
-- Critical: Accelerates lobby querying by approval status and publication state
CREATE INDEX IF NOT EXISTS idx_exams_approval_published_year 
ON public.exams (approval_status, is_published, year DESC);

CREATE INDEX IF NOT EXISTS idx_exams_created_at_desc 
ON public.exams (created_at DESC);

CREATE INDEX IF NOT EXISTS idx_exams_category_id 
ON public.exams (category_id);

-- 4. Profiles Table Indexes
-- Critical: Accelerates presence window scanning (last_active_at >= 5 min ago)
-- and student/admin count filtering
CREATE INDEX IF NOT EXISTS idx_profiles_last_active_at_desc 
ON public.profiles (last_active_at DESC NULLS LAST);

CREATE INDEX IF NOT EXISTS idx_profiles_role 
ON public.profiles (role);

CREATE INDEX IF NOT EXISTS idx_profiles_created_at_desc 
ON public.profiles (created_at DESC);

-- 5. Categories Table Index
CREATE INDEX IF NOT EXISTS idx_categories_sort_order 
ON public.categories (sort_order ASC);

-- 6. Storage Bucket Policy: Allow Super Admins to manage 'admin-analytics' snapshot
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_policies 
        WHERE tablename = 'objects' 
          AND schemaname = 'storage' 
          AND policyname = 'Super admins can manage admin-analytics snapshot'
    ) THEN
        CREATE POLICY "Super admins can manage admin-analytics snapshot" ON storage.objects
            FOR ALL TO authenticated
            USING (
                bucket_id = 'user-backups' 
                AND (storage.foldername(name))[1] = 'admin-analytics'
                AND public.is_super_admin()
            )
            WITH CHECK (
                bucket_id = 'user-backups' 
                AND (storage.foldername(name))[1] = 'admin-analytics'
                AND public.is_super_admin()
            );
    END IF;
END $$;
