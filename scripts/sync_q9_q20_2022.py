import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from db_ops import run_sql

with open('public/data/exams/cc4bf627-e456-538f-87e2-4a99ebb613ed.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

statements = ["BEGIN;"]
for q in d['questions']:
    if q['sort_order'] in [9, 20]:
        expl_escaped = q['explanation'].replace("'", "''")
        sql = f"UPDATE questions SET explanation = '{expl_escaped}' WHERE id = '{q['id']}';"
        statements.append(sql)
statements.append("COMMIT;")

batch_sql = "\n".join(statements)
print(f'Syncing {len(statements)-2} questions to Supabase...')
res = run_sql(batch_sql)
print('Done! Result:', res)
