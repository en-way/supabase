# -*- coding: utf-8 -*-
"""
sync_round46_batch.py
Fast, single-transaction batch synchronization of Round 46 (2002 ky1) calibrated questions and passages from local JSON to Supabase.
"""

import sys
import glob
import json
import os
import subprocess

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 46 - 2002 ky1) ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Fetch DB questions
db_questions = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, 
           q.stem, q.options, q.correct_answer, q.explanation
    from questions q
    join exams e on q.exam_id = e.id
    where e.year = 2002 and e.category_id = 'ky1'
""")
db_q_map = {(q["year"], q["category_id"], q["sort_order"]): q for q in db_questions}

# 2. Fetch DB passages
db_passages = db_ops.run_sql("""
    select id, title, content from passages
    where id in (
        '8b7dec36-0057-5b3e-8d45-b736f5b913e2',
        'c82eb2c3-d5f7-58fa-981e-0806ff32c124',
        'e105b25c-a6ec-502d-b204-11a9c304d4fe',
        '53474821-9120-5962-acc2-5c36455d7aeb',
        'f0cbd337-0bdf-58e8-8723-cf2c30aa0d62'
    )
""")
db_p_map = {p["id"]: p for p in db_passages}

# 3. Read local 2002 json
json_path = 'public/data/exams/e1b9d134-9546-55ab-9a60-c7e5b04046a3.json'
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

sql_statements = ["BEGIN;"]
updates_count = 0

# Check passages
for p in exam_data.get('passages', []):
    pid = p.get('id')
    db_p = db_p_map.get(pid)
    local_content = p.get('content', '')
    if not db_p or db_p.get('content') != local_content:
        sql = f"UPDATE passages SET content = {sql_escape(local_content)} WHERE id = '{pid}';"
        sql_statements.append(sql)
        updates_count += 1
        print(f"Passage to update: {pid} (len: {len(local_content)})")

# Check questions
for q in exam_data.get('questions', []):
    so = q.get('sort_order')
    db_q = db_q_map.get((2002, 'ky1', so))
    if not db_q:
        print(f"Warning: Question 2002 ky1 Q{so} not found in DB!")
        continue
    
    qid = db_q['id']
    local_stem = q.get('stem', '')
    local_ans = q.get('correct_answer') or q.get('answer', '')
    local_exp = q.get('explanation', '')
    local_opts = json.dumps(q.get('options', []), ensure_ascii=False)
    db_opts = json.dumps(db_q.get('options', []), ensure_ascii=False) if isinstance(db_q.get('options'), (list, dict)) else str(db_q.get('options'))

    needs_update = False
    if db_q.get('stem') != local_stem:
        needs_update = True
    if db_q.get('correct_answer') != local_ans:
        needs_update = True
    if db_q.get('explanation') != local_exp:
        needs_update = True
    if db_opts != local_opts:
        needs_update = True
        
    if needs_update:
        sql = f"""UPDATE questions SET 
            stem = {sql_escape(local_stem)},
            correct_answer = {sql_escape(local_ans)},
            explanation = {sql_escape(local_exp)},
            options = {sql_escape(local_opts)}::jsonb
            WHERE id = '{qid}';"""
        sql_statements.append(sql)
        updates_count += 1
        print(f"Question to update: Q{so:02d} (ans: {db_q.get('correct_answer')} -> {local_ans})")

sql_statements.append("COMMIT;")

print(f"\nTotal updates to execute: {updates_count}")

if updates_count > 0:
    full_sql = "\n".join(sql_statements)
    res = db_ops.run_sql(full_sql)
    print("Batch DB Update successfully committed!")
else:
    print("DB is already 100% in parity with local JSON.")
