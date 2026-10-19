# -*- coding: utf-8 -*-
"""
sync_round38_batch.py
Fast, single-transaction batch synchronization of Round 38 calibrated questions from local JSON to Supabase.
"""

import sys
import glob
import json
import os

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync (Round 38) ===")

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
                "so": so,
                "stem": jq.get("stem"),
                "options": jq.get("options"),
                "correct_answer": jq.get("correct_answer"),
                "explanation": jq.get("explanation"),
                "reasons": [
                    k for k, v in [
                        ("answer", ans_diff), 
                        ("stem", stem_diff), 
                        ("options", opts_diff), 
                        ("explanation", expl_diff)
                    ] if v
                ]
            })

print(f"Found {len(q_updates)} questions needing update in DB.")

if not q_updates:
    print("DB is already 100% in sync with local JSON!")
    sys.exit(0)

# Build single batch SQL
sql_statements = ["BEGIN;"]
for item in q_updates:
    print(f"  -> Queuing update for {item['year']} {item['cat']} Q{item['so']} (reasons: {', '.join(item['reasons'])})")
    opts_json = json.dumps(item["options"], ensure_ascii=False)
    sql_statements.append(f"""
        UPDATE questions
        SET stem = {sql_escape(item['stem'])},
            options = {sql_escape(opts_json)}::jsonb,
            correct_answer = {sql_escape(item['correct_answer'])},
            explanation = {sql_escape(item['explanation'])}
        WHERE id = '{item['id']}';
    """)

sql_statements.append("COMMIT;")
batch_sql = "\n".join(sql_statements)

print("Executing batch transaction against Supabase...")
res = db_ops.run_sql(batch_sql)
print("Batch update completed successfully!")
print(f"Total synchronized questions: {len(q_updates)}")
