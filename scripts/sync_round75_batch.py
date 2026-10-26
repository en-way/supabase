# -*- coding: utf-8 -*-
"""
sync_round75_batch.py
Fast, single-transaction batch synchronization of Round 75 (2021 ky2) calibrated questions and passages from local JSON to Supabase.
"""

import sys
import json
import os

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 75 - 2021 ky2) ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Read local 2021 ky2 json
json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\4ebd819e-c832-5890-9048-ba16040a5607.json'
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

exam_id = exam_data.get('id') or exam_data.get('exam', {}).get('id') or "4ebd819e-c832-5890-9048-ba16040a5607"

# 2. Fetch DB questions
db_questions = db_ops.run_sql(f"""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, 
           q.stem, q.options, q.correct_answer, q.explanation, q.points, q.q_type, q.passage_id
    from questions q
    join exams e on q.exam_id = e.id
    where e.id = '{exam_id}'
""")
db_q_map = {q["sort_order"]: q for q in db_questions}
print(f"Fetched {len(db_questions)} DB questions for 2021 ky2.")

# 3. Fetch DB passages
passage_ids = [p['id'] for p in exam_data.get('passages', [])]
p_id_list_str = ", ".join(f"'{pid}'" for pid in passage_ids)
db_passages = db_ops.run_sql(f"""
    select id, title, content, section_type, sort_order from passages
    where id in ({p_id_list_str})
""")
db_p_map = {p["id"]: p for p in db_passages}
print(f"Fetched {len(db_passages)} DB passages for 2021 ky2.")

sql_statements = ["BEGIN;"]
updates_count = 0

# Check exam title & total_score & pass_score
local_title = exam_data.get('title') or exam_data.get('exam', {}).get('title')
sql_statements.append(f"UPDATE exams SET title = {sql_escape(local_title)}, total_score = 60.0, pass_score = 36.0, duration_minutes = 180, approval_status = 'approved', is_published = true WHERE id = '{exam_id}';")
updates_count += 1
print(f"Exam metadata update queued: {local_title}")

# Check passages
for p in exam_data.get('passages', []):
    pid = p.get('id')
    db_p = db_p_map.get(pid)
    local_content = p.get('content') or p.get('text', '')
    local_title_p = p.get('title', '')
    if not local_title_p and db_p:
        local_title_p = db_p.get('title', '')
    local_type = p.get('passage_type') or p.get('type') or p.get('section_type', '')
    db_section_type = 'cloze' if ('Use of English' in local_title_p or local_type == 'use_of_english') else 'reading'
    
    sql_statements.append(f"""
        UPDATE passages 
        SET title = {sql_escape(local_title_p)},
            content = {sql_escape(local_content)},
            section_type = {sql_escape(db_section_type)},
            sort_order = {p.get('sort_order', 1)}
        WHERE id = '{pid}';
    """)
    updates_count += 1
    print(f"Passage update queued: {pid} ({local_title_p})")

# Check questions
for q in exam_data.get('questions', []):
    sort_order = q.get('sort_order')
    db_q = db_q_map.get(sort_order)
    qid = q.get('id')
    
    local_points = 0.5 if sort_order <= 20 else 2.0
    local_q_type = 'cloze_item' if sort_order <= 20 else 'reading_item'
    local_answer = q.get('correct_answer') or q.get('answer', '')
    local_stem = q.get('stem', '')
    local_expl = q.get('explanation', '')
    local_opts = json.dumps(q.get('options', []), ensure_ascii=False)
    local_passage_id = q.get('passage_id')
    
    sql_statements.append(f"""
        UPDATE questions 
        SET points = {local_points},
            q_type = {sql_escape(local_q_type)},
            correct_answer = {sql_escape(local_answer)},
            stem = {sql_escape(local_stem)},
            explanation = {sql_escape(local_expl)},
            options = {sql_escape(local_opts)}::jsonb,
            sort_order = {sort_order},
            passage_id = {sql_escape(local_passage_id)}
        WHERE id = '{qid}';
    """)
    updates_count += 1

sql_statements.append("COMMIT;")

full_sql = "\n".join(sql_statements)
print(f"Executing atomic transaction batch ({updates_count} updates)...")
res = db_ops.run_sql(full_sql)
print("Batch transaction result:", res)
print("=== DB Sync Finished Successfully ===")
