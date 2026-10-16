import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

data_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

files = {
    2023: 'b5992dc7-d0ac-56ce-8845-aa2c58675802.json',
    2024: 'f303f3fb-abfe-477f-a2e5-8dcd1ba78ef0.json',
    2025: 'c75ee9ef-ec21-5396-b3bf-4e30260d2918.json',
}

for yr, f in files.items():
    fp = os.path.join(data_dir, f)
    with open(fp, 'r', encoding='utf-8') as fp_in:
        d = json.load(fp_in)
    print(f"\n=================== {yr} ky1 ===================")
    for q in d['questions']:
        if q['sort_order'] in range(41, 46):
            exp = q.get('explanation') or ''
            first_lines = exp.strip().split('\n')[:3]
            print(f"Q{q['sort_order']}: ans={q['correct_answer']}")
            print(f"  exp preview: {' | '.join(first_lines)[:120]}")
