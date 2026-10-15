import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__)))
import db_ops

sql = """
SELECT
  (SELECT count(*) FROM pg_stat_activity WHERE state = 'active') AS active_connections,
  (SELECT count(*) FROM pg_stat_activity) AS total_connections,
  (SELECT round(sum(heap_blks_hit) / NULLIF(sum(heap_blks_hit + heap_blks_read), 0) * 100, 2)
   FROM pg_statio_user_tables) AS cache_hit_ratio_pct,
  pg_size_pretty(pg_database_size(current_database())) AS db_size,
  (SELECT pg_size_pretty(pg_total_relation_size('public.questions'))) AS questions_size,
  (SELECT pg_size_pretty(pg_total_relation_size('public.passages'))) AS passages_size,
  (SELECT pg_size_pretty(pg_total_relation_size('public.exams'))) AS exams_size;
"""

res = db_ops.run_sql(sql)
print("=== Current DB State ===")
for k, v in res[0].items():
    print(f"  {k}: {v}")

sql2 = """
SELECT name, setting, unit FROM pg_settings
WHERE name IN ('max_connections', 'shared_buffers', 'work_mem', 'effective_cache_size');
"""
rows = db_ops.run_sql(sql2)
print("\n=== PostgreSQL Settings ===")
for r in rows:
    print(f"  {r['name']}: {r['setting']} {r['unit'] or ''}")

sql3 = """
SELECT 
    schemaname,
    relname AS tablename,
    n_live_tup,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||relname)) AS total_size,
    seq_scan,
    idx_scan
FROM pg_stat_user_tables
ORDER BY n_live_tup DESC;
"""
rows = db_ops.run_sql(sql3)
print("\n=== Table Stats ===")
for r in rows:
    print(f"  {r['tablename']}: {r['n_live_tup']} rows, {r['total_size']}, seq_scan={r['seq_scan']}, idx_scan={r['idx_scan']}")
