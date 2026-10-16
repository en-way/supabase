import sys
import os
import glob
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 7 DB Sync (Questions, Passages, Explanations) ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Sync Passages
print("\nChecking Passages in DB vs JSON...")
db_passages = db_ops.run_sql("""
    select p.id, p.exam_id, e.year, e.category_id, p.sort_order, p.content
    from passages p
    join exams e on p.exam_id = e.id
""")
db_p_map = {(p["year"], p["category_id"], p["sort_order"]): p for p in db_passages}

json_passages = {}
for f in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    data = json.load(open(f, encoding="utf-8"))
    yr = data["exam"]["year"]
    cat = data["exam"]["category_id"]
    for p in data.get("passages", []):
        json_passages[(yr, cat, p["sort_order"])] = p

p_updates = []
for key, jp in json_passages.items():
    if key not in db_p_map:
        continue
    dp = db_p_map[key]
    if jp.get("content") != dp.get("content"):
        p_updates.append({
            "id": dp["id"],
            "key": key,
            "content": jp.get("content")
        })

print(f"Total passages requiring update in DB: {len(p_updates)}")
for pu in p_updates:
    print(f"  -> Passage update: {pu['key'][0]} {pu['key'][1]} Passage {pu['key'][2]}")
    sql = f"""
    UPDATE public.passages
    SET content = {sql_escape(pu['content'])}
    WHERE id = '{pu['id']}';
    """
    db_ops.run_sql(sql)
print("Passages updated successfully in DB.")

# 2. Sync Questions
print("\nChecking Questions in DB vs JSON...")
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

q_updates = []
for key, jq in json_questions.items():
    if key not in db_q_map:
        continue
    dq = db_q_map[key]
    
    ans_diff = jq.get("correct_answer") != dq.get("correct_answer")
    stem_diff = jq.get("stem") != dq.get("stem")
    opts_diff = json.dumps(jq.get("options"), sort_keys=True) != json.dumps(dq.get("options"), sort_keys=True)
    expl_diff = jq.get("explanation") != dq.get("explanation")
    pts_diff = jq.get("points") != float(dq.get("points"))
    pid_diff = jq.get("passage_id") != dq.get("passage_id")
    
    if ans_diff or stem_diff or opts_diff or expl_diff or pts_diff or pid_diff:
        q_updates.append({
            "id": dq["id"],
            "key": key,
            "correct_answer": jq.get("correct_answer"),
            "stem": jq.get("stem"),
            "options": jq.get("options"),
            "explanation": jq.get("explanation"),
            "points": jq.get("points"),
            "passage_id": jq.get("passage_id"),
            "diffs": {
                "ans": ans_diff,
                "stem": stem_diff,
                "opts": opts_diff,
                "expl": expl_diff,
                "pts": pts_diff,
                "pid": pid_diff
            }
        })

print(f"Total questions requiring update in DB: {len(q_updates)}")
for qu in q_updates[:30]:
    print(f"  -> Question update: {qu['key'][0]} {qu['key'][1]} Q{qu['key'][2]} diffs={qu['diffs']}")
if len(q_updates) > 30:
    print(f"  ... and {len(q_updates) - 30} more")

if q_updates:
    statements = []
    for qu in q_updates:
        opts_json_str = json.dumps(qu["options"], ensure_ascii=False)
        pid_sql = f"'{qu['passage_id']}'" if qu["passage_id"] else "NULL"
        sql = f"""
        UPDATE public.questions
        SET correct_answer = {sql_escape(qu['correct_answer'])},
            stem = {sql_escape(qu['stem'])},
            options = {sql_escape(opts_json_str)}::jsonb,
            explanation = {sql_escape(qu['explanation'])},
            points = {qu['points']},
            passage_id = {pid_sql}
        WHERE id = '{qu['id']}';
        """
        statements.append(sql)
    batch_sql = "BEGIN;\n" + "\n".join(statements) + "\nCOMMIT;"
    db_ops.run_sql(batch_sql)
    print("Questions updated successfully in DB.")

# 3. Final Parity Verification
print("\n=== Verifying DB vs JSON Consistency ===")
final_p_count = db_ops.run_sql("select count(*) as count from passages;")[0]["count"]
final_q_count = db_ops.run_sql("select count(*) as count from questions;")[0]["count"]
print(f"Passages count in DB: {final_p_count} (Expected: 243)")
print(f"Questions count in DB: {final_q_count} (Expected: 1825)")
assert int(final_p_count) == 243, f"Passage count mismatch: {final_p_count}"
assert int(final_q_count) == 1825, f"Question count mismatch: {final_q_count}"

# Check that 0 diffs remain
remaining_q_diffs = 0
db_q_fresh = { (q["year"], q["category_id"], q["sort_order"]): q for q in db_ops.run_sql("""
    select q.id, e.year, e.category_id, q.sort_order, q.correct_answer, q.stem, q.options, q.explanation
    from questions q join exams e on q.exam_id = e.id
""")}
for key, jq in json_questions.items():
    dq = db_q_fresh[key]
    if jq.get("correct_answer") != dq.get("correct_answer") or \
       jq.get("stem") != dq.get("stem") or \
       json.dumps(jq.get("options"), sort_keys=True) != json.dumps(dq.get("options"), sort_keys=True) or \
       jq.get("explanation") != dq.get("explanation"):
        remaining_q_diffs += 1

print(f"Remaining Question Diffs between DB and JSON: {remaining_q_diffs} (Expected: 0)")
assert remaining_q_diffs == 0, f"Found {remaining_q_diffs} question discrepancies!"

print("\n🎉 Round 7 DB Sync Completed with 100% Parity!")
