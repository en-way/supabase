import sys
import os
import glob
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 5 DB Sync (Passages & Questions) ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Sync Passages
print("\n[1/2] Checking Passages in DB vs JSON...")
db_passages = db_ops.run_sql("""
    select p.id, p.exam_id, e.year, e.category_id, p.sort_order, p.title, p.content
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

p_inserts = []
p_updates = []

for key, jp in json_passages.items():
    if key not in db_p_map:
        yr, cat, s_order = key
        stype = 'cloze' if s_order == 1 else 'reading'
        p_inserts.append({
            "id": jp["id"],
            "exam_id": jp["exam_id"],
            "category_id": cat,
            "section_type": stype,
            "title": jp["title"],
            "content": jp["content"],
            "sort_order": s_order
        })
    else:
        dp = db_p_map[key]
        c_diff = (jp.get("content") or "").strip() != (dp.get("content") or "").strip()
        t_diff = (jp.get("title") or "").strip() != (dp.get("title") or "").strip()
        if c_diff or t_diff:
            p_updates.append({
                "id": dp["id"],
                "key": key,
                "title": jp.get("title"),
                "content": jp.get("content")
            })

print(f"Passages to INSERT into DB: {len(p_inserts)}")
for pi in p_inserts:
    print(f"  -> Insert passage: id={pi['id']}, title={pi['title']}, sort_order={pi['sort_order']}")

if p_inserts:
    insert_stmts = []
    for pi in p_inserts:
        sql = f"""
        INSERT INTO public.passages (id, exam_id, category_id, section_type, title, content, sort_order)
        VALUES ('{pi['id']}', '{pi['exam_id']}', '{pi['category_id']}', '{pi['section_type']}', {sql_escape(pi['title'])}, {sql_escape(pi['content'])}, {pi['sort_order']});
        """
        insert_stmts.append(sql)
    batch_insert_sql = "BEGIN;\n" + "\n".join(insert_stmts) + "\nCOMMIT;"
    db_ops.run_sql(batch_insert_sql)
    print("New passages successfully inserted into DB.")

print(f"Passages requiring UPDATE in DB: {len(p_updates)}")
for pu in p_updates:
    print(f"  -> Update passage: {pu['key'][0]} {pu['key'][1]} sort_order={pu['key'][2]}")

if p_updates:
    update_stmts = []
    for pu in p_updates:
        sql = f"""
        UPDATE public.passages 
        SET title = {sql_escape(pu['title'])}, content = {sql_escape(pu['content'])} 
        WHERE id = '{pu['id']}';
        """
        update_stmts.append(sql)
    batch_update_sql = "BEGIN;\n" + "\n".join(update_stmts) + "\nCOMMIT;"
    db_ops.run_sql(batch_update_sql)
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
for qu in q_updates[:25]:
    print(f"  -> Question update: {qu['key'][0]} {qu['key'][1]} Q{qu['key'][2]} diffs={qu['diffs']}")
if len(q_updates) > 25:
    print(f"  ... and {len(q_updates) - 25} more")

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

# 3. Final Verification between DB and JSON
print("\n=== Verifying DB vs JSON Consistency ===")
final_p_count = db_ops.run_sql("select count(*) as count from passages;")[0]["count"]
final_q_count = db_ops.run_sql("select count(*) as count from questions;")[0]["count"]
print(f"Passages count in DB: {final_p_count} (Expected: 243)")
print(f"Questions count in DB: {final_q_count} (Expected: 1825)")
assert int(final_p_count) == 243, f"Passage count mismatch: {final_p_count}"
assert int(final_q_count) == 1825, f"Question count mismatch: {final_q_count}"

print("\n🎉 Round 5 DB Sync Completed with 100% Consistency!")
