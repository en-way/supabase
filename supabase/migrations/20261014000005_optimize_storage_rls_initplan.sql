-- 20261014000005_optimize_storage_rls_initplan.sql
-- 升级 storage.objects 中 user-backups 存储桶的行级安全策略（RLS）
-- 将 (auth.uid())::text 包装为 ((select auth.uid())::text)
-- 满足 PostgreSQL 查询优化器的单次计算 InitPlan 特性，杜绝多对象扫描时重复评估用户鉴权

DROP POLICY IF EXISTS "Users can read own backups from storage" ON storage.objects;
DROP POLICY IF EXISTS "Users can upload own backups to storage" ON storage.objects;
DROP POLICY IF EXISTS "Users can update own backups in storage" ON storage.objects;
DROP POLICY IF EXISTS "Users can delete own backups from storage" ON storage.objects;

-- 1. 下载读取策略
CREATE POLICY "Users can read own backups from storage" ON storage.objects
  FOR SELECT TO authenticated
  USING (
    bucket_id = 'user-backups' 
    AND (storage.foldername(name))[1] = ((select auth.uid())::text)
  );

-- 2. 初始上传策略
CREATE POLICY "Users can upload own backups to storage" ON storage.objects
  FOR INSERT TO authenticated
  WITH CHECK (
    bucket_id = 'user-backups' 
    AND (storage.foldername(name))[1] = ((select auth.uid())::text)
  );

-- 3. 覆盖更新策略
CREATE POLICY "Users can update own backups in storage" ON storage.objects
  FOR UPDATE TO authenticated
  USING (
    bucket_id = 'user-backups' 
    AND (storage.foldername(name))[1] = ((select auth.uid())::text)
  )
  WITH CHECK (
    bucket_id = 'user-backups' 
    AND (storage.foldername(name))[1] = ((select auth.uid())::text)
  );

-- 4. 删除清理策略
CREATE POLICY "Users can delete own backups from storage" ON storage.objects
  FOR DELETE TO authenticated
  USING (
    bucket_id = 'user-backups' 
    AND (storage.foldername(name))[1] = ((select auth.uid())::text)
  );
