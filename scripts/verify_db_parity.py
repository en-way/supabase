import sys
import glob
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Verifying Supabase DB vs Local JSON Parity ===")

db_questions = db_ops.run_sql('select count(*) as c from questions')
db_passages = db_ops.run_sql('select count(*) as c from passages')
print(f"DB total questions: {db_questions[0]['c']}, passages: {db_passages[0]['c']}")

db_q = db_ops.run_sql('''
    select e.year, e.category_id, q.sort_order, q.correct_answer, q.explanation
    from questions q
    join exams e on q.exam_id = e.id
''')
db_q_map = {(r['year'], r['category_id'], r['sort_order']): r for r in db_q}

diff_count = 0
for f in sorted(glob.glob(r'public/data/exams/*.json')):
    data = json.load(open(f, encoding='utf-8'))
    yr = data['exam']['year']
    cat = data['exam']['category_id']
    for q in data['questions']:
        so = q['sort_order']
        db_item = db_q_map.get((yr, cat, so))
        if not db_item:
            print(f"Missing in DB: {yr} {cat} Q{so}")
            diff_count += 1
            continue
        if (q.get('explanation') or '').strip() != (db_item.get('explanation') or '').strip():
            print(f"Expl diff: {yr} {cat} Q{so}")
            diff_count += 1
        if q.get('correct_answer') != db_item.get('correct_answer'):
            print(f"Ans diff: {yr} {cat} Q{so}")
            diff_count += 1

print(f"Total DB vs JSON diffs: {diff_count}")
if diff_count == 0:
    print("SUCCESS: 100% Full Golden Parity Achieved! 0 differences!")
