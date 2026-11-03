# -*- coding: utf-8 -*-
import json
import glob
import sys

sys.path.append(r'd:\A16pro\Aing\antigravity\supabase\scripts')
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("Probing 2012 ky2 DB & Local state...")
res = db_ops.run_sql("select id, year, category_id, title, total_score from exams where year = 2012 and category_id = 'ky2';")
print("2012 ky2 DB exam:", res)

for jf in glob.glob(r'public/data/exams/*.json'):
    try:
        with open(jf, encoding='utf-8') as f:
            d = json.load(f)
            e = d.get('exam', {})
            if (e.get('year') == 2012 or d.get('year') == 2012) and (e.get('category_id') == 'ky2' or d.get('category_id') == 'ky2'):
                print("2012 ky2 local file:", jf)
                print("Title:", d.get('title') or e.get('title'))
                print("Passages count:", len(d.get('passages', [])))
                print("Questions count:", len(d.get('questions', [])))
                for idx, p in enumerate(d.get('passages', [])):
                    c = p.get('content', '')
                    print(f"P{idx}: type={p.get('type')}, words={len(c.split())}, start={repr(c[:60])}")
                for q_idx in [0, 20, 25, 30, 35, 40]:
                    if q_idx < len(d.get('questions', [])):
                        q = d['questions'][q_idx]
                        print(f"Q{q_idx+1}: stem={repr(q.get('stem')[:50])}, ans={q.get('correct_answer')}, pts={q.get('points')}")
                break
    except Exception:
        continue
