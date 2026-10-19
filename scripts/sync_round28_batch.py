# -*- coding: utf-8 -*-
"""
sync_round28_batch.py
Fast, single-transaction batch synchronization of Round 28 questions from local JSON to Supabase.
"""

import sys
import glob
import json
import os

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 28) ===")

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
""")
db_q_map = {(q["year"], q["category_id"], q["sort_order"]): q for q in db_questions}

# 2. Scan local JSON files
exam_files = glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")

q_updates = []

for ef in exam_files:
    with open(ef, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    exam_meta = data.get("exam", {})
    year = exam_meta.get("year")
    cat = exam_meta.get("category_id")
    
    for jq in data.get("questions", []):
        so = jq.get("sort_order")
        key = (year, cat, so)
        if key not in db_q_map:
            continue
        
        dq = db_q_map[key]
        
        # Check differences
        ans_diff = (jq.get("correct_answer") or "").strip() != (dq.get("correct_answer") or "").strip()
        stem_diff = (jq.get("stem") or "").strip() != (dq.get("stem") or "").strip()
        
        j_opts = json.dumps(jq.get("options", []), sort_keys=True)
        d_opts = dq.get("options")
        if isinstance(d_opts, str):
            try:
                d_opts = json.loads(d_opts)
            except:
                pass
        d_opts_str = json.dumps(d_opts if isinstance(d_opts, (list, dict)) else [], sort_keys=True)
        opts_diff = j_opts != d_opts_str
        
        expl_diff = (jq.get("explanation") or "").strip() != (dq.get("explanation") or "").strip()
        
        if ans_diff or stem_diff or opts_diff or expl_diff:
            q_updates.append((key, dq["id"], jq, ans_diff, stem_diff, opts_diff, expl_diff))

print(f"Total questions with diffs detected: {len(q_updates)}")
for k, qid, jq, ad, sd, od, ed in q_updates:
    diffs = []
    if ad: diffs.append("ans")
    if sd: diffs.append("stem")
    if od: diffs.append("opts")
    if ed: diffs.append("expl")
    print(f"  Target update: {k[0]} {k[1]} Q{k[2]} (id={qid}): diffs={','.join(diffs)}")

if not q_updates:
    print("No updates needed. Everything in sync.")
    sys.exit(0)

# Build single SQL statement with multiple updates inside a transaction
sql_statements = ["BEGIN;"]
for k, qid, jq, ad, sd, od, ed in q_updates:
    stem_val = sql_escape(jq.get("stem"))
    ans_val = sql_escape(jq.get("correct_answer"))
    opts_val = sql_escape(json.dumps(jq.get("options", []), ensure_ascii=False))
    expl_val = sql_escape(jq.get("explanation"))
    
    sql = f"""
    UPDATE questions
    SET stem = {stem_val},
        options = {opts_val}::jsonb,
        correct_answer = {ans_val},
        explanation = {expl_val}
    WHERE id = '{qid}';
    """
    sql_statements.append(sql)
sql_statements.append("COMMIT;")

full_sql = "\n".join(sql_statements)
print(f"Executing batch update for {len(q_updates)} questions in a single transaction...")

res = db_ops.run_sql(full_sql)
print("Batch update response:", res)
print("=== Batch DB Sync Complete ===")
