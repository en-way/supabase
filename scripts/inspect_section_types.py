import sys
sys.path.append('scripts')
import db_ops

rows = db_ops.run_sql("""
    select section_type, count(*) as count
    from passages 
    group by section_type;
""")
print('Section types in passages:')
for r in rows:
    print(' ', r)

titles = db_ops.run_sql("""
    select sort_order, title, count(*) as count
    from passages 
    group by sort_order, title 
    order by sort_order;
""")
print('\nTitles by sort order:')
for t in titles:
    print(' ', t)
