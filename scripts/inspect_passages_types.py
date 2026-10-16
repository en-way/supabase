import sys
sys.path.append('scripts')
import db_ops

cols = db_ops.run_sql("""
    SELECT column_name, data_type 
    FROM information_schema.columns 
    WHERE table_name = 'passages'
    ORDER BY ordinal_position;
""")
print('Passages columns:')
for c in cols:
    print(' ', c['column_name'], c['data_type'])

sample = db_ops.run_sql("""
    SELECT id, exam_id, title, sort_order, length(content) as content_len
    FROM passages 
    ORDER BY sort_order
    LIMIT 12;
""")
print('\nSample passages:')
for s in sample:
    print(' ', s)
