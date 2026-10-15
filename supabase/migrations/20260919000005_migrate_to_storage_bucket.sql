-- ==============================================================================
-- Migration: 20260919000005_migrate_to_storage_bucket.sql
-- Description: Setup 'user-backups' Private Storage Bucket & Migrate user_backups table to metadata-only
-- ==============================================================================

-- 1. Create Private Storage Bucket 'user-backups' in storage.buckets
INSERT INTO storage.buckets (id, name, public, file_size_limit, allowed_mime_types)
VALUES (
    'user-backups',
    'user-backups',
    false,
    10485760, -- 10MB limit per backup file (plenty for thousands of entries)
    ARRAY['application/json']
)
ON CONFLICT (id) DO UPDATE SET 
    public = false,
    file_size_limit = EXCLUDED.file_size_limit,
    allowed_mime_types = EXCLUDED.allowed_mime_types;

-- 2. Storage Objects RLS Policies for 'user-backups'
-- Each authenticated user can only access their own directory: user-backups/{auth.uid()}/*

DROP POLICY IF EXISTS "Users can read own backups from storage" ON storage.objects;
CREATE POLICY "Users can read own backups from storage" ON storage.objects
    FOR SELECT TO authenticated
    USING (
        bucket_id = 'user-backups' 
        AND (storage.foldername(name))[1] = auth.uid()::text
    );

DROP POLICY IF EXISTS "Users can upload own backups to storage" ON storage.objects;
CREATE POLICY "Users can upload own backups to storage" ON storage.objects
    FOR INSERT TO authenticated
    WITH CHECK (
        bucket_id = 'user-backups' 
        AND (storage.foldername(name))[1] = auth.uid()::text
    );

DROP POLICY IF EXISTS "Users can update own backups in storage" ON storage.objects;
CREATE POLICY "Users can update own backups in storage" ON storage.objects
    FOR UPDATE TO authenticated
    USING (
        bucket_id = 'user-backups' 
        AND (storage.foldername(name))[1] = auth.uid()::text
    )
    WITH CHECK (
        bucket_id = 'user-backups' 
        AND (storage.foldername(name))[1] = auth.uid()::text
    );

DROP POLICY IF EXISTS "Users can delete own backups from storage" ON storage.objects;
CREATE POLICY "Users can delete own backups from storage" ON storage.objects
    FOR DELETE TO authenticated
    USING (
        bucket_id = 'user-backups' 
        AND (storage.foldername(name))[1] = auth.uid()::text
    );

-- 3. Restructure public.user_backups to be lightweight metadata-only
-- Free up 100% of PostgreSQL row table space by dropping backup_data
ALTER TABLE public.user_backups 
    DROP COLUMN IF EXISTS backup_data;

ALTER TABLE public.user_backups 
    ADD COLUMN IF NOT EXISTS file_path TEXT DEFAULT NULL;
