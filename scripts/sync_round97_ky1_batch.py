# -*- coding: utf-8 -*-
"""
sync_round97_ky1_batch.py
Sync all 111 calibrated English 1 explanations to Supabase DB in batches of 10 with retries.
"""

import sys
import json
import glob
import time

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

print("=== Step 1: Loading all KY1 questions from DB ===")
db_rows = db_ops.run_sql("""
    select q.id, q.exam_id, e.year, e.category_id, q.sort_order, q.explanation
    from questions q
    join exams e on q.exam_id = e.id
    where e.category_id = 'ky1'
""")
print(f"Loaded {len(db_rows)} KY1 questions from DB.")

db_map = {}
for r in db_rows:
    yr = r['year']
    so = r['sort_order']
    db_map[(yr, so)] = r

print("=== Step 2: Comparing with Local JSON files ===")
updates_needed = []

for fpath in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    d = json.load(open(fpath, encoding='utf-8'))
    title = d.get('title', '')
    cat = d.get('category_id') or d.get('exam', {}).get('category_id')
    if cat != 'ky1' and '英语（一）' not in title and '英语一' not in title:
        continue
    
    yr = d.get('year') or d.get('exam', {}).get('year')
    for q in d.get('questions', []):
        qn = q.get('question_number')
        local_expl = q.get('explanation', '')
        
        db_q = db_map.get((yr, qn))
        if not db_q:
            continue
            
        db_expl = db_q.get('explanation') or ''
        if db_expl.strip() != local_expl.strip():
            updates_needed.append({
                'id': db_q['id'],
                'year': yr,
                'qn': qn,
                'explanation': local_expl
            })

print(f"Total questions needing explanation updates: {len(updates_needed)}")

print("=== Step 3: Executing Updates in Batches of 10 ===")
batch_size = 10
total_batches = (len(updates_needed) + batch_size - 1) // batch_size

for b_idx in range(total_batches):
    batch = updates_needed[b_idx * batch_size : (b_idx + 1) * batch_size]
    sql_stmts = ["BEGIN;"]
    for item in batch:
        escaped_expl = sql_escape(item['explanation'])
        sql_stmts.append(f"UPDATE questions SET explanation = {escaped_expl} WHERE id = '{item['id']}';")
    sql_stmts.append("COMMIT;")
    full_sql = "\n".join(sql_stmts)
    
    # Retry loop
    success = False
    for attempt in range(1, 4):
        try:
            db_ops.run_sql(full_sql)
            success = True
            break
        except Exception as e:
            print(f"Batch {b_idx + 1}/{total_batches} attempt {attempt} failed: {e}")
            time.sleep(2 * attempt)
            
    if not success:
        print(f"FATAL: Batch {b_idx + 1} failed after 3 attempts.")
        sys.exit(1)
        
    qs_str = ", ".join(f"{it['year']} Q{it['qn']}" for it in batch)
    print(f"Batch {b_idx + 1}/{total_batches} synced successfully ({len(batch)} items): {qs_str}")
    time.sleep(0.5)

print("=== All updates completed successfully! ===")
