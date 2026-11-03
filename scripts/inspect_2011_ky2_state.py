# -*- coding: utf-8 -*-
import json
import sys
import glob

sys.path.append(r'd:\A16pro\Aing\antigravity\supabase\scripts')
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("==================== Inspecting 2011 ky2 State ====================")

# 1. DB search
res = db_ops.run_sql("select id, year, category_id, title, total_score from exams where year = 2011 and category_id = 'ky2';")
print("DB exam record:", res)

exam_id = res[0]['id'] if res else None

# 2. Local JSON search
json_files = glob.glob(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json')
ky2_2011_file = None
for jf in json_files:
    try:
        with open(jf, encoding='utf-8') as f:
            d = json.load(f)
            e = d.get('exam', {})
            if (e.get('year') == 2011 or d.get('year') == 2011) and (e.get('category_id') == 'ky2' or d.get('category_id') == 'ky2'):
                ky2_2011_file = jf
                break
    except Exception:
        continue

print("Local JSON file:", ky2_2011_file)

if ky2_2011_file:
    with open(ky2_2011_file, encoding='utf-8') as f:
        d = json.load(f)
    print("Local Title:", d.get('title') or d.get('exam', {}).get('title'))
    print("Passages count:", len(d.get('passages', [])))
    print("Questions count:", len(d.get('questions', [])))
    for i, p in enumerate(d.get('passages', [])):
        c = p.get('content', '')
        print(f"P{i} ({p.get('title')}): type={p.get('type')}, words={len(c.split())}, start={repr(c[:60])}")
    for i in [0, 20, 25, 30, 35, 40]:
        if i < len(d.get('questions', [])):
            q = d['questions'][i]
            print(f"Q{i+1}: stem={repr(q.get('stem')[:50])}, ans={q.get('correct_answer')}, pts={q.get('points')}")
