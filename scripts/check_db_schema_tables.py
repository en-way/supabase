import sys
sys.path.append('scripts')
import db_ops

tables = db_ops.run_sql("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public' 
    ORDER BY table_name;
""")
print('Tables in public schema:')
for t in tables:
    print(' ', t['table_name'])
