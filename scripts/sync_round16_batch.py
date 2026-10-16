import sys
import glob
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Fast Batch DB Sync ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

db_questions = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, 
           q.stem, q.options, q.correct_answer, q.explanation, q.points, q.passage_id
    from questions q
    join exams e on q.exam_id = e.id
""")
db_q_map = {(q["year"], q["category_id"], q["sort_order"]): q for q in db_questions}

json_questions = {}
for f in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    data = json.load(open(f, encoding="utf-8"))
    yr = data["exam"]["year"]
    cat = data["exam"]["category_id"]
    for q in data["questions"]:
        json_questions[(yr, cat, q["sort_order"])] = q

updates = []
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
        updates.append(f"""
        UPDATE public.questions
        SET stem = {sql_escape(jq['stem'])},
            options = {sql_escape(opts_json)}::jsonb,
            correct_answer = {sql_escape(jq['correct_answer'])},
            explanation = {sql_escape(jq['explanation'])}
        WHERE id = '{dq['id']}';
        """)

print(f"Total questions to update in batch: {len(updates)}")
if updates:
    batch_sql = "BEGIN;\n" + "\n".join(updates) + "\nCOMMIT;"
    print("Executing batch transaction...")
    db_ops.run_sql(batch_sql)
    print("Batch transaction committed successfully!")
else:
    print("No updates needed!")
