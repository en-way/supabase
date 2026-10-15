import sys
import os
import glob
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 4 DB Sync (Passages & Questions) ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Sync Passages
print("\n[1/2] Checking Passages in DB vs JSON...")
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
    for p in data["passages"]:
        json_passages[(yr, cat, p["sort_order"])] = p

p_updates = []
for key, jp in json_passages.items():
    if key not in db_p_map:
        continue
    dp = db_p_map[key]
    if (jp.get("content") or "").strip() != (dp.get("content") or "").strip():
        p_updates.append({
            "id": dp["id"],
            "key": key,
            "content": jp.get("content")
        })

print(f"Total passages requiring update in DB: {len(p_updates)}")
for pu in p_updates:
    print(f"  -> Passage update: {pu['key'][0]} {pu['key'][1]} sort_order={pu['key'][2]}")

if p_updates:
    statements = []
    for pu in p_updates:
        sql = f"UPDATE public.passages SET content = {sql_escape(pu['content'])} WHERE id = '{pu['id']}';"
        statements.append(sql)
    batch_sql = "BEGIN;\n" + "\n".join(statements) + "\nCOMMIT;"
    db_ops.run_sql(batch_sql)
    print("Passages updated successfully in DB.")

# 2. Sync Questions
print("\n[2/2] Checking Questions in DB vs JSON...")
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
            "diffs": [
                k for k, v in [
                    ("ans", ans_diff), ("stem", stem_diff), 
                    ("opts", opts_diff), ("expl", expl_diff), 
                    ("pts", pts_diff), ("pid", pid_diff)
                ] if v
            ]
        })

print(f"Total questions requiring sync to DB: {len(q_updates)}")
for qu in q_updates:
    print(f"  -> Question diff: {qu['key'][0]} {qu['key'][1]} Q{qu['key'][2]}: {qu['diffs']}")

batch_size = 25
total_batches = (len(q_updates) + batch_size - 1) // batch_size

for b in range(total_batches):
    chunk = q_updates[b * batch_size : (b + 1) * batch_size]
    statements = []
    for u in chunk:
        opt_json = json.dumps(u["options"], ensure_ascii=False)
        pid_val = f"'{u['passage_id']}'" if u["passage_id"] else "NULL"
        sql = f"""
            UPDATE public.questions 
            SET 
                correct_answer = {sql_escape(u['correct_answer'])},
                stem = {sql_escape(u['stem'])},
                options = {sql_escape(opt_json)}::jsonb,
                explanation = {sql_escape(u['explanation'])},
                points = {u['points']},
                passage_id = {pid_val}
            WHERE id = '{u['id']}';
        """
        statements.append(sql.strip())
    
    batch_sql = "BEGIN;\n" + "\n".join(statements) + "\nCOMMIT;"
    db_ops.run_sql(batch_sql)
    print(f"Synced questions batch {b+1} / {total_batches} ({len(chunk)} questions)")

print("\n=== Supabase DB Round 4 Synchronization Completed Successfully! ===")
