# -*- coding: utf-8 -*-
"""
sync_round93_batch.py
Fast batch synchronization of Round 93 purified explanations and questions from local JSON to Supabase.
"""

import sys
import json
import os
import glob

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 93 Purified Explanations) ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Fetch all DB questions
print("Fetching current questions from Supabase...")
db_q = db_ops.run_sql('''
    select q.id, e.year, e.category_id, q.sort_order, q.explanation
    from questions q
    join exams e on q.exam_id = e.id
''')
db_q_map = {(r['year'], r['category_id'], r['sort_order']): r for r in db_q}
print(f"Loaded {len(db_q)} questions from DB.")

# 2. Check diffs against local JSONs
files = sorted(glob.glob(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json'))
updates = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    yr = data['exam']['year']
    cat = data['exam']['category_id']
    for q in data['questions']:
        so = q['sort_order']
        db_item = db_q_map.get((yr, cat, so))
        if not db_item:
            continue
        local_expl = (q.get('explanation') or '').strip()
        db_expl = (db_item.get('explanation') or '').strip()
        if local_expl != db_expl:
            updates.append({
                'id': db_item['id'],
                'year': yr,
                'category_id': cat,
                'sort_order': so,
                'explanation': q.get('explanation') or ''
            })

print(f"Total questions needing explanation update in DB: {len(updates)}")

if not updates:
    print("Zero updates needed. Database is already in 100% parity.")
    sys.exit(0)

# 3. Apply updates in batches
batch_size = 50
for i in range(0, len(updates), batch_size):
    batch = updates[i:i + batch_size]
    sql_statements = []
    for item in batch:
        qid = item['id']
        expl_sql = sql_escape(item['explanation'])
        sql_statements.append(f"UPDATE questions SET explanation = {expl_sql} WHERE id = '{qid}';")
    batch_sql = "\n".join(sql_statements)
    db_ops.run_sql(batch_sql)
    print(f"Synced batch {i + 1} to {min(i + batch_size, len(updates))}...")

print(f"Successfully synced all {len(updates)} purified questions to Supabase DB!")
