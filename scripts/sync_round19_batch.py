# -*- coding: utf-8 -*-
"""
sync_round19_batch.py
Fast, single-transaction batch synchronization of both questions and passages from local JSON to Supabase.
"""

import sys
import glob
import json
import os

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 19) ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Fetch DB questions & passages
db_questions = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, 
           q.stem, q.options, q.correct_answer, q.explanation, q.points, q.passage_id
    from questions q
    join exams e on q.exam_id = e.id
""")
db_q_map = {(q["year"], q["category_id"], q["sort_order"]): q for q in db_questions}

db_passages = db_ops.run_sql("""
    select p.id, p.exam_id, e.year, e.category_id, p.sort_order, p.title, p.content
    from passages p
    join exams e on p.exam_id = e.id
""")
db_p_map = {(p["year"], p["category_id"], p["sort_order"]): p for p in db_passages}

# 2. Collect JSON items
json_questions = {}
json_passages = {}
for f in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    data = json.load(open(f, encoding="utf-8"))
    yr = data["exam"]["year"]
    cat = data["exam"]["category_id"]
    for q in data["questions"]:
        json_questions[(yr, cat, q["sort_order"])] = q
    for p in data["passages"]:
        json_passages[(yr, cat, p["sort_order"])] = p

# 3. Compare questions
q_updates = []
for key, jq in json_questions.items():
    if key not in db_q_map:
        continue
    dq = db_q_map[key]
    ans_diff = jq.get("correct_answer") != dq.get("correct_answer")
    stem_diff = jq.get("stem") != dq.get("stem")
    opts_diff = json.dumps(jq.get("options"), sort_keys=True) != json.dumps(dq.get("options"), sort_keys=True)
    expl_diff = (jq.get("explanation") or "").strip() != (dq.get("explanation") or "").strip()
    
    if ans_diff or stem_diff or opts_diff or expl_diff:
        opts_json = json.dumps(jq["options"], ensure_ascii=False)
        q_updates.append(f"""
        UPDATE public.questions
        SET stem = {sql_escape(jq['stem'])},
            options = {sql_escape(opts_json)}::jsonb,
            correct_answer = {sql_escape(jq['correct_answer'])},
            explanation = {sql_escape(jq['explanation'])}
        WHERE id = '{dq['id']}';
        """)

# 4. Compare passages
p_updates = []
for key, jp in json_passages.items():
    if key not in db_p_map:
        continue
    dp = db_p_map[key]
    content_diff = (jp.get("content") or "").strip() != (dp.get("content") or "").strip()
    title_diff = (jp.get("title") or "").strip() != (dp.get("title") or "").strip()
    
    if content_diff or title_diff:
        p_updates.append(f"""
        UPDATE public.passages
        SET title = {sql_escape(jp['title'])},
            content = {sql_escape(jp['content'])}
        WHERE id = '{dp['id']}';
        """)

print(f"Total questions to update in batch: {len(q_updates)}")
print(f"Total passages to update in batch: {len(p_updates)}")

all_updates = q_updates + p_updates
if all_updates:
    batch_sql = "BEGIN;\n" + "\n".join(all_updates) + "\nCOMMIT;"
    print("Executing batch transaction...")
    res = db_ops.run_sql(batch_sql)
    print("Batch transaction committed successfully!")
else:
    print("No updates needed, DB already in 100% parity!")
