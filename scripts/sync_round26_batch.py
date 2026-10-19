# -*- coding: utf-8 -*-
"""
sync_round26_batch.py
Fast, single-transaction batch synchronization of Round 26 questions from local JSON to Supabase.
"""

import sys
import glob
import json
import os

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 26) ===")

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

# 2. Collect JSON questions
json_questions = {}
for f in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    data = json.load(open(f, encoding="utf-8"))
    yr = data["exam"]["year"]
    cat = data["exam"]["category_id"]
    for q in data["questions"]:
        json_questions[(yr, cat, q["sort_order"])] = q

# 3. Compare questions
q_updates = []
for key, jq in json_questions.items():
    if key not in db_q_map:
        continue
    dq = db_q_map[key]
    ans_diff = jq.get("correct_answer") != dq.get("correct_answer")
    stem_diff = (jq.get("stem") or "").strip() != (dq.get("stem") or "").strip()
    
    # compare options
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

print(f"Found {len(q_updates)} questions needing DB update in Round 26:")
for k, qid, jq, ad, sd, od, ed in q_updates:
    diffs = []
    if ad: diffs.append("ans")
    if sd: diffs.append("stem")
    if od: diffs.append("opts")
    if ed: diffs.append("expl")
    print(f"  - {k[0]} {k[1]} Q{k[2]} (id={qid}): diffs={','.join(diffs)}")

if not q_updates:
    print("Database is already 100% in sync with local JSON files!")
    sys.exit(0)

# 4. Generate batch SQL inside a single transaction
statements = ["BEGIN;"]
for k, qid, jq, ad, sd, od, ed in q_updates:
    stem_val = sql_escape(jq.get("stem"))
    ans_val = sql_escape(jq.get("correct_answer"))
    expl_val = sql_escape(jq.get("explanation"))
    opts_json_str = json.dumps(jq.get("options", []), ensure_ascii=False)
    opts_val = sql_escape(opts_json_str)
    
    sql = f"""
    UPDATE questions 
    SET stem = {stem_val},
        correct_answer = {ans_val},
        options = {opts_val}::jsonb,
        explanation = {expl_val}
    WHERE id = '{qid}';
    """
    statements.append(sql.strip())

statements.append("COMMIT;")

full_sql = "\n".join(statements)

print("\nExecuting atomic batch transaction on Supabase...")
res = db_ops.run_sql(full_sql)
print(f"Transaction result: {res}")
print(f"Successfully synced {len(q_updates)} questions to Supabase DB in a single transaction!")
