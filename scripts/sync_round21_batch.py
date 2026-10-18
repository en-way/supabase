# -*- coding: utf-8 -*-
"""
sync_round21_batch.py
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

print("=== Starting Fast Batch DB Sync (Round 21) ===")

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
    exp_diff = jq.get("explanation") != dq.get("explanation")
    
    # compare options
    j_opts = json.dumps(jq.get("options", []), sort_keys=True)
    d_opts_val = dq.get("options", [])
    if isinstance(d_opts_val, str):
        try:
            d_opts_val = json.loads(d_opts_val)
        except:
            pass
    d_opts = json.dumps(d_opts_val, sort_keys=True)
    opt_diff = j_opts != d_opts

    if ans_diff or stem_diff or exp_diff or opt_diff:
        q_updates.append((dq["id"], key, jq, ans_diff, stem_diff, exp_diff, opt_diff))

print(f"Total Questions to update in DB: {len(q_updates)}")
for uid, key, jq, ad, sd, ed, od in q_updates:
    diffs = []
    if ad: diffs.append("answer")
    if sd: diffs.append("stem")
    if ed: diffs.append("explanation")
    if od: diffs.append("options")
    print(f"  - {key[0]} {key[1]} Q{key[2]}: diff in {', '.join(diffs)}")

# 4. Compare passages
p_updates = []
for key, jp in json_passages.items():
    if key not in db_p_map:
        continue
    dp = db_p_map[key]
    cnt_diff = jp.get("content") != dp.get("content")
    title_diff = jp.get("title") != dp.get("title")
    if cnt_diff or title_diff:
        p_updates.append((dp["id"], key, jp, cnt_diff, title_diff))

print(f"Total Passages to update in DB: {len(p_updates)}")
for uid, key, jp, cd, td in p_updates:
    diffs = []
    if cd: diffs.append("content")
    if td: diffs.append("title")
    print(f"  - {key[0]} {key[1]} P{key[2]}: diff in {', '.join(diffs)}")

if not q_updates and not p_updates:
    print("Everything is already in 100% sync! No updates needed.")
    sys.exit(0)

# 5. Build batch SQL transaction
sql_statements = ["BEGIN;"]

for uid, key, jq, _, _, _, _ in q_updates:
    opts_json = json.dumps(jq.get("options", []), ensure_ascii=False)
    sql_statements.append(f"""
        UPDATE questions SET 
            stem = {sql_escape(jq.get('stem'))},
            options = {sql_escape(opts_json)}::jsonb,
            correct_answer = {sql_escape(jq.get('correct_answer'))},
            explanation = {sql_escape(jq.get('explanation'))}
        WHERE id = {sql_escape(uid)};
    """)

for uid, key, jp, _, _ in p_updates:
    sql_statements.append(f"""
        UPDATE passages SET 
            title = {sql_escape(jp.get('title'))},
            content = {sql_escape(jp.get('content'))}
        WHERE id = {sql_escape(uid)};
    """)

sql_statements.append("COMMIT;")

full_sql = "\n".join(sql_statements)
print(f"Executing batch transaction ({len(sql_statements)-2} statements)...")
res = db_ops.run_sql(full_sql)
print("Batch update result:", res)

print("\nVerifying DB vs JSON sync parity now...")
import verify_db_parity
