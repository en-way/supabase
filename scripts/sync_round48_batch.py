# -*- coding: utf-8 -*-
"""
sync_round48_batch.py
Fast, single-transaction batch synchronization of Round 48 (2006 ky1) calibrated questions and passages from local JSON to Supabase.
"""

import sys
import json
import os

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 48 - 2006 ky1) ===")

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
    where e.year = 2006 and e.category_id = 'ky1'
""")
db_q_map = {(q["year"], q["category_id"], q["sort_order"]): q for q in db_questions}

# 2. Fetch DB passages
db_passages = db_ops.run_sql("""
    select id, title, content, section_type from passages
    where id in (
        'fd77d6d0-6ded-51ba-9d44-013d77ee979c',
        '0bac5a94-e87c-55fb-b24c-8c12f9d18ef6',
        '28dfa39a-3497-58ab-b17a-4b2e1849a872',
        'fe979c03-674c-5223-9d58-f99599d97e78',
        '9e8e8e4e-9255-5653-ab22-be437e84ce83',
        '5f091ca1-0269-547e-b380-e82bc98ba95d'
    )
""")
db_p_map = {p["id"]: p for p in db_passages}

# 3. Read local 2006 json
json_path = 'public/data/exams/c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json'
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

sql_statements = ["BEGIN;"]
updates_count = 0

# Check passages
for p in exam_data.get('passages', []):
    pid = p.get('id')
    db_p = db_p_map.get(pid)
    local_content = p.get('content', '')
    local_type = p.get('type', '')
    db_section_type = 'cloze' if local_type == 'cloze' else 'reading'
    if not db_p or db_p.get('content') != local_content or db_p.get('section_type') != db_section_type:
        sql = f"UPDATE passages SET content = {sql_escape(local_content)}, section_type = {sql_escape(db_section_type)} WHERE id = '{pid}';"
        sql_statements.append(sql)
        updates_count += 1
        print(f"Passage to update: {pid} (len: {len(local_content)}, type: {db_section_type})")

# Check questions
for q in exam_data.get('questions', []):
    so = q.get('sort_order')
    db_q = db_q_map.get((2006, 'ky1', so))
    if not db_q:
        print(f"Warning: Question 2006 ky1 Q{so} not found in DB!")
        continue
    
    qid = db_q['id']
    local_stem = q.get('stem')
    local_ans = q.get('correct_answer') or q.get('answer')
    local_opts = json.dumps(q.get('options', []), ensure_ascii=False)
    local_expl = q.get('explanation')
    
    db_opts_str = json.dumps(db_q['options'], ensure_ascii=False) if isinstance(db_q['options'], (list, dict)) else db_q['options']
    
    needs_update = False
    if db_q.get('stem') != local_stem:
        needs_update = True
    if db_q.get('correct_answer') != local_ans:
        needs_update = True
    if db_opts_str != local_opts:
        needs_update = True
    if db_q.get('explanation') != local_expl:
        needs_update = True
        
    if needs_update:
        sql = f"""UPDATE questions 
SET stem = {sql_escape(local_stem)},
    options = {sql_escape(local_opts)}::jsonb,
    correct_answer = {sql_escape(local_ans)},
    explanation = {sql_escape(local_expl)}
WHERE id = '{qid}';"""
        sql_statements.append(sql)
        updates_count += 1
        print(f"Question to update: Q{so} (ID: {qid})")

sql_statements.append("COMMIT;")

if updates_count > 0:
    print(f"\nTotal items to update: {updates_count}. Executing single atomic transaction...")
    batch_sql = "\n".join(sql_statements)
    result = db_ops.run_sql(batch_sql)
    print("Database sync completed successfully!")
else:
    print("\nAll 2006 items already in 100% parity with DB! Nothing to update.")
