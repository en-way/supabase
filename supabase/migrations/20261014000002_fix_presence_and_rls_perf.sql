-- ==============================================================================
-- Migration: 20261014000002_fix_presence_and_rls_perf.sql
-- Description:
-- 1. Fix touch_user_activity(): correct typo last_seen_at -> last_active_at
-- 2. Optimize is_admin() and is_super_admin(): mark as STABLE to enable query caching
-- 3. Optimize RLS InitPlan: wrap auth.uid() in (select auth.uid()) for profiles & user_backups
-- 4. Storage Policy: allow Super Admins to manage admin-analytics snapshot
-- ==============================================================================

-- 1. Fix touch_user_activity (resolves 100% silent failures on user presence heartbeat)
CREATE OR REPLACE FUNCTION public.touch_user_activity()
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = public
AS $$
BEGIN
    UPDATE public.profiles
    SET last_active_at = now()
    WHERE id = auth.uid();
END;
$$;

-- 2. Recreate is_admin() and is_super_admin() with STABLE volatility
-- Enables PostgreSQL planner to cache auth evaluation per query, eliminating N-row repeat queries
CREATE OR REPLACE FUNCTION public.is_admin()
RETURNS boolean
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.profiles
    WHERE id = (select auth.uid()) AND role IN ('admin', 'super_admin')
  );
$$;

CREATE OR REPLACE FUNCTION public.is_super_admin()
RETURNS boolean
LANGUAGE sql
STABLE
SECURITY DEFINER
SET search_path = public
AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.profiles
    WHERE id = (select auth.uid()) AND role = 'super_admin'
  );
$$;

-- 3. Upgrade RLS policies to use (select auth.uid()) InitPlan optimization
DROP POLICY IF EXISTS "Users can manage own backup" ON public.user_backups;
CREATE POLICY "Users can manage own backup"
ON public.user_backups
FOR ALL
TO public
USING ((select auth.uid()) = user_id)
WITH CHECK ((select auth.uid()) = user_id);

DROP POLICY IF EXISTS "Users can update own profile" ON public.profiles;
CREATE POLICY "Users can update own profile"
ON public.profiles
FOR UPDATE
TO authenticated
USING ((select auth.uid()) = id)
WITH CHECK ((select auth.uid()) = id);

-- 4. Storage RLS Policy: Allow Super Admins to manage 'admin-analytics/*' snapshots in 'user-backups' bucket
DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_policies 
        WHERE schemaname = 'storage' 
          AND tablename = 'objects' 
          AND policyname = 'Super Admins can manage analytics snapshots'
    ) THEN
        CREATE POLICY "Super Admins can manage analytics snapshots"
        ON storage.objects
        FOR ALL
        TO authenticated
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
