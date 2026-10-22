# -*- coding: utf-8 -*-
"""
sync_round51_batch.py
Fast, single-transaction batch synchronization of Round 51 (2009 ky1) calibrated questions and passages from local JSON to Supabase.
"""

import sys
import json
import os

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 51 - 2009 ky1) ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Read local 2009 json
json_path = 'public/data/exams/9369aa41-c91e-548c-bf99-1ad46a07ac25.json'
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

exam_id = exam_data['exam']['id']

# 2. Fetch DB questions
db_questions = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, 
           q.stem, q.options, q.correct_answer, q.explanation
    from questions q
    join exams e on q.exam_id = e.id
    where e.year = 2009 and e.category_id = 'ky1'
""")
db_q_map = {(q["year"], q["category_id"], q["sort_order"]): q for q in db_questions}
print(f"Fetched {len(db_questions)} DB questions for 2009 ky1.")

# 3. Fetch DB passages
passage_ids = [p['id'] for p in exam_data.get('passages', [])]
p_id_list_str = ", ".join(f"'{pid}'" for pid in passage_ids)
db_passages = db_ops.run_sql(f"""
    select id, title, content, section_type from passages
    where id in ({p_id_list_str})
""")
db_p_map = {p["id"]: p for p in db_passages}
print(f"Fetched {len(db_passages)} DB passages for 2009 ky1.")

sql_statements = ["BEGIN;"]
updates_count = 0

# Check exam title
local_title = exam_data['exam']['title']
sql_statements.append(f"UPDATE exams SET title = {sql_escape(local_title)} WHERE id = '{exam_id}';")
updates_count += 1
print(f"Exam title update queued: {local_title}")

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
    db_q = db_q_map.get((2009, 'ky1', so))
    if not db_q:
        print(f"Warning: Question 2009 ky1 Q{so} not found in DB!")
        continue
    
    qid = db_q['id']
    local_stem = q.get('stem') or q.get('prompt')
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
        sql = f"""UPDATE questions SET 
            stem = {sql_escape(local_stem)},
            correct_answer = {sql_escape(local_ans)},
            options = {sql_escape(local_opts)}::jsonb,
            explanation = {sql_escape(local_expl)}
            WHERE id = '{qid}';"""
        sql_statements.append(sql)
        updates_count += 1
        print(f"Queue question update: Q{so} (id: {qid})")

sql_statements.append("COMMIT;")

print(f"\nTotal updates to execute: {updates_count}")

if updates_count > 0:
    batch_sql = "\n".join(sql_statements)
    print("Executing batch SQL transaction...")
    res = db_ops.run_sql(batch_sql)
    print(f"Batch SQL execution result: {res}")
    print("Sync completed successfully!")
else:
    print("No updates needed. Everything is in sync.")
