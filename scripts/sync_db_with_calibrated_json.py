import sys
import os
import glob
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

print("Fetching current questions from Supabase DB...")
db_questions = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, 
           q.stem, q.options, q.correct_answer, q.explanation, q.points
    from questions q
    join exams e on q.exam_id = e.id
""")
print(f"Total DB questions loaded: {len(db_questions)}")
db_map = {(q["year"], q["category_id"], q["sort_order"]): q for q in db_questions}

# Load all JSON questions
json_questions = {}
for f in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    data = json.load(open(f, encoding="utf-8"))
    exam = data["exam"]
    yr = exam["year"]
    cat = exam["category_id"]
    for q in data["questions"]:
        json_questions[(yr, cat, q["sort_order"])] = q

print(f"Total JSON questions loaded: {len(json_questions)}")

updates_needed = []
for key, jq in json_questions.items():
    if key not in db_map:
        continue
    dq = db_map[key]
    
    # Check what fields need update
    ans_diff = jq.get("correct_answer") != dq.get("correct_answer")
    stem_diff = jq.get("stem") != dq.get("stem")
    opts_diff = json.dumps(jq.get("options"), sort_keys=True) != json.dumps(dq.get("options"), sort_keys=True)
    expl_diff = jq.get("explanation") != dq.get("explanation")
    pts_diff = jq.get("points") != float(dq.get("points"))
    
    if ans_diff or stem_diff or opts_diff or expl_diff or pts_diff:
        updates_needed.append({
            "id": dq["id"],
            "key": key,
            "correct_answer": jq.get("correct_answer"),
            "stem": jq.get("stem"),
            "options": jq.get("options"),
            "explanation": jq.get("explanation"),
            "points": jq.get("points"),
            "diffs": [
                k for k, v in [
                    ("ans", ans_diff), ("stem", stem_diff), 
                    ("opts", opts_diff), ("expl", expl_diff), ("pts", pts_diff)
                ] if v
            ]
        })

print(f"\nTotal questions requiring sync to DB: {len(updates_needed)}")
for u in updates_needed[:10]:
    print(f"  [{u['key'][0]} {u['key'][1]} Q{u['key'][2]}] diffs: {u['diffs']}")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# Batch update in transactions of 25 questions
batch_size = 25
total_batches = (len(updates_needed) + batch_size - 1) // batch_size

for b in range(total_batches):
    chunk = updates_needed[b * batch_size : (b + 1) * batch_size]
    statements = []
    for u in chunk:
        opt_json = json.dumps(u["options"], ensure_ascii=False)
        sql = f"""
            UPDATE public.questions 
            SET 
                correct_answer = {sql_escape(u['correct_answer'])},
                stem = {sql_escape(u['stem'])},
                options = {sql_escape(opt_json)}::jsonb,
                explanation = {sql_escape(u['explanation'])},
                points = {u['points']}
            WHERE id = '{u['id']}';
        """
        statements.append(sql.strip())
    
    batch_sql = "BEGIN;\n" + "\n".join(statements) + "\nCOMMIT;"
    db_ops.run_sql(batch_sql)
    print(f"Synced batch {b+1} / {total_batches} ({len(chunk)} questions)")

print("\nDatabase synchronization completed successfully!")
