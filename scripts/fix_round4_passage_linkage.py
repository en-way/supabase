import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Round 4: Fixing Question-to-Passage Linkage for 2011 ky2 and 2013 ky2...")

fixes = [
    {
        'file': 'public/data/exams/53a52573-0afc-51a4-86b6-b2f321cbe6a8.json',
        'year': 2011,
        'cat': 'ky2',
    },
    {
        'file': 'public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json',
        'year': 2013,
        'cat': 'ky2',
    }
]

db_updates = []

for item in fixes:
    fpath = item['file']
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    passages = data['passages']
    p3_id = passages[3]['id'] # Text 3
    p4_id = passages[4]['id'] # Text 4
    
    modified = False
    for q in data['questions']:
        so = q['sort_order']
        if 31 <= so <= 35:
            if q['passage_id'] != p3_id:
                print(f"[{item['year']} ky2 Q{so}] Remapped to Text 3 ({p3_id})")
                q['passage_id'] = p3_id
                modified = True
                db_updates.append((q['id'], p3_id, so, item['year']))
        elif 36 <= so <= 40:
            if q['passage_id'] != p4_id:
                print(f"[{item['year']} ky2 Q{so}] Remapped to Text 4 ({p4_id})")
                q['passage_id'] = p4_id
                modified = True
                db_updates.append((q['id'], p4_id, so, item['year']))
                
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nLocal JSON files updated. Now updating {len(db_updates)} questions in Supabase DB...")

if db_updates:
    statements = []
    for qid, pid, so, yr in db_updates:
        sql = f"UPDATE public.questions SET passage_id = '{pid}' WHERE id = '{qid}';"
        statements.append(sql)
    
    batch_sql = "BEGIN;\n" + "\n".join(statements) + "\nCOMMIT;"
    db_ops.run_sql(batch_sql)
    print("Supabase DB successfully updated with correct passage linkages!")

print("\n--- Passage Linkage Calibration Complete ---")
