import sys
import glob
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("Fetching DB questions...")
db_questions = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, 
           q.stem, q.options, q.correct_answer, q.explanation, q.points, q.passage_id
    from questions q
    join exams e on q.exam_id = e.id
""")
print(f"Fetched {len(db_questions)} DB questions.")

db_q_map = {(q["year"], q["category_id"], q["sort_order"]): q for q in db_questions}

diffs = []
for f in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    data = json.load(open(f, encoding="utf-8"))
    yr = data["exam"]["year"]
    cat = data["exam"]["category_id"]
    for q in data["questions"]:
        so = q["sort_order"]
        key = (yr, cat, so)
        if key in db_q_map:
            dq = db_q_map[key]
            ans_diff = q.get("correct_answer") != dq.get("correct_answer")
            stem_diff = q.get("stem") != dq.get("stem")
            opts_diff = json.dumps(q.get("options"), sort_keys=True) != json.dumps(dq.get("options"), sort_keys=True)
            expl_diff = (q.get("explanation") or "").strip() != (dq.get("explanation") or "").strip()
            if ans_diff or stem_diff or opts_diff or expl_diff:
                diffs.append((key, dq["id"], ans_diff, stem_diff, opts_diff, expl_diff))

print(f"Total diffs: {len(diffs)}")
for d in diffs:
    print(d)
