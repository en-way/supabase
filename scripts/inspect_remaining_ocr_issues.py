import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DATA_DIR = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def load_exam(cat, yr):
    for f in os.listdir(DATA_DIR):
        if not f.endswith('.json'):
            continue
        fp = os.path.join(DATA_DIR, f)
        with open(fp, 'r', encoding='utf-8') as fp_in:
            d = json.load(fp_in)
        exam = d.get('exam', d)
        if exam.get('category_id') == cat and exam.get('year') == yr:
            return f, d
    return None, None

print("=== 2010 ky1 Q26 & Q33 ===")
_, d10 = load_exam('ky1', 2010)
for q in d10['questions']:
    if q['sort_order'] in [26, 33]:
        exp = q.get('explanation', '')
        if 'th&r' in exp:
            print(f"2010 Q{q['sort_order']} has 'th&r' in expl")
        if 'o£' in exp:
            print(f"2010 Q{q['sort_order']} has 'o£' in expl")

print("\n=== 2020 ky1 Q27 watermark ===")
_, d20 = load_exam('ky1', 2020)
for q in d20['questions']:
    if q['sort_order'] == 27:
        exp = q.get('explanation', '')
        for l in exp.split('\n'):
            if '购买' in l:
                print("Line with '购买':", l)

print("\n=== '44' used as quote mark check ===")
for yr in [2010, 2018, 2020, 2021]:
    _, d = load_exam('ky1', yr)
    for q in d['questions']:
        exp = q.get('explanation', '')
        # search for 44 followed by letter or Chinese
        matches = re.findall(r'.{0,15}44[a-zA-Z\u4e00-\u9fa5].{0,15}', exp)
        if matches:
            for m in matches:
                print(f"{yr} ky1 Q{q['sort_order']}: {m.strip()}")
