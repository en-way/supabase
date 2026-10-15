-- ==============================================================================
-- Migration: 20260919000002_fix_profiles_rls.sql
-- Fix infinite recursion in public.profiles RLS policy
-- ==============================================================================

-- 1. Helper function with SECURITY DEFINER to avoid RLS recursion
CREATE OR REPLACE FUNCTION public.is_admin()
RETURNS BOOLEAN AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.profiles
    WHERE id = auth.uid() AND role = 'admin'
  );
$$ LANGUAGE sql SECURITY DEFINER SET search_path = public;

-- 2. Drop the recursive policy
DROP POLICY IF EXISTS "Admins can view and manage all profiles" ON public.profiles;
DROP POLICY IF EXISTS "Users can view and update own profile" ON public.profiles;
DROP POLICY IF EXISTS "Authenticated can read profiles" ON public.profiles;
DROP POLICY IF EXISTS "Users can update own profile" ON public.profiles;
DROP POLICY IF EXISTS "Admins can manage any profile" ON public.profiles;

-- 3. Clean, non-recursive policies:
-- All authenticated users can read profiles
CREATE POLICY "Authenticated can read profiles" ON public.profiles 
    FOR SELECT TO authenticated USING (true);

-- Regular users can update their own profile (nickname, avatar, etc.)
CREATE POLICY "Users can update own profile" ON public.profiles 
    FOR UPDATE TO authenticated 
    USING (auth.uid() = id) 
    WITH CHECK (auth.uid() = id);

-- Admins can manage all profiles using the security definer function
CREATE POLICY "Admins can manage any profile" ON public.profiles 
    FOR ALL TO authenticated 
    USING (public.is_admin());

-- Update exams, passages, questions policies to use is_admin() as well
DROP POLICY IF EXISTS "Admins can manage exams" ON public.exams;
CREATE POLICY "Admins can manage exams" ON public.exams 
    FOR ALL TO authenticated USING (public.is_admin());

DROP POLICY IF EXISTS "Admins can manage passages" ON public.passages;
CREATE POLICY "Admins can manage passages" ON public.passages 
    FOR ALL TO authenticated USING (public.is_admin());

DROP POLICY IF EXISTS "Admins can manage questions" ON public.questions;
CREATE POLICY "Admins can manage questions" ON public.questions 
    FOR ALL TO authenticated USING (public.is_admin());
