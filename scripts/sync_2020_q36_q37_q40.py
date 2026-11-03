import sys
import json
import time

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Fetching 2020 KY2 questions from Supabase...")
db_q = db_ops.run_sql('''
    select q.id, q.sort_order, q.explanation
    from questions q
    join exams e on q.exam_id = e.id
    where e.year = 2020 and e.category_id = 'ky2'
''')
db_map = {r['sort_order']: r for r in db_q}

p = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json"
with open(p, "r", encoding="utf-8") as f:
    d = json.load(f)

for q in d["questions"]:
    so = q["sort_order"]
    if so in [36, 37, 40]:
        expl = q["explanation"]
        qid = db_map[so]["id"]
        expl_sql = "'" + expl.replace("'", "''") + "'"
        db_ops.run_sql(f"UPDATE questions SET explanation = {expl_sql} WHERE id = '{qid}';")
        print(f"Updated 2020 KY2 Q{so} in DB.")
        time.sleep(0.5)

print("Done updating 2020 KY2 questions in DB!")
