# -*- coding: utf-8 -*-
"""
sync_round39_batch.py
Fast, single-transaction batch synchronization of Round 39 calibrated questions from local JSON to Supabase.
"""

import sys
import glob
import json
import os

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 39) ===")

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
            q_updates.append({
                "id": dq["id"],
                "year": year,
                "cat": cat,
                "sort_order": so,
                "stem": jq.get("stem"),
                "options": json.dumps(jq.get("options", []), ensure_ascii=False),
                "correct_answer": jq.get("correct_answer"),
                "explanation": jq.get("explanation"),
                "diffs": f"ans={ans_diff}, stem={stem_diff}, opts={opts_diff}, expl={expl_diff}"
            })

print(f"Total question updates needed: {len(q_updates)}")
for u in q_updates:
    print(f"  - {u['year']} {u['cat']} Q{u['sort_order']} (ID: {u['id']}): {u['diffs']}")

if not q_updates:
    print("Database is already 100% in sync with local JSON files!")
    sys.exit(0)

# 3. Construct single batch SQL query
sql_parts = ["BEGIN;"]
for u in q_updates:
    stmt = f"""
    UPDATE questions
    SET stem = {sql_escape(u['stem'])},
        options = {sql_escape(u['options'])}::jsonb,
        correct_answer = {sql_escape(u['correct_answer'])},
        explanation = {sql_escape(u['explanation'])}
    WHERE id = '{u['id']}';
    """
    sql_parts.append(stmt.strip())

sql_parts.append("COMMIT;")
batch_sql = "\n".join(sql_parts)

print("\nExecuting batch transaction in Supabase...")
res = db_ops.run_sql(batch_sql)
print("Batch SQL execution complete!")

# 4. Verify DB Parity
print("\nVerifying parity after sync...")
import subprocess
ret = subprocess.run([sys.executable, "scripts/verify_db_parity.py"], capture_output=True, text=True, encoding="utf-8")
print(ret.stdout)
if ret.stderr:
    print("STDERR:", ret.stderr)

if ret.returncode == 0 and "0 differences" in ret.stdout:
    print("SUCCESS: Supabase and local JSON are in 100% Golden Parity!")
else:
    print("WARNING: Parity check returned non-zero or diffs exist.")
