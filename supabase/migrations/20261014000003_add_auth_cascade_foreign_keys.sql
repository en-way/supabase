-- ==============================================================================
-- Migration: 20261014000003_add_auth_cascade_foreign_keys.sql
-- Description:
-- Add ON DELETE CASCADE foreign key constraints from public tables to auth.users(id)
-- Ensures automatic cleanup of profiles and user_backups when an account is deleted
-- ==============================================================================

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints 
        WHERE constraint_schema = 'public' 
          AND table_name = 'profiles' 
          AND constraint_name = 'fk_profiles_user'
    ) THEN
        ALTER TABLE public.profiles
        ADD CONSTRAINT fk_profiles_user
        FOREIGN KEY (id) REFERENCES auth.users(id) ON DELETE CASCADE;
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM information_schema.table_constraints 
        WHERE constraint_schema = 'public' 
          AND table_name = 'user_backups' 
          AND constraint_name = 'fk_user_backups_user'
    ) THEN
        ALTER TABLE public.user_backups
        ADD CONSTRAINT fk_user_backups_user
        FOREIGN KEY (user_id) REFERENCES auth.users(id) ON DELETE CASCADE;
    END IF;
END $$;
