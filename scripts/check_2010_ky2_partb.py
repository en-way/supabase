import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('public/data/exams/*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    if d.get('exam', {}).get('year') == 2010 and d.get('exam', {}).get('category_id') == 'ky2':
        for q in d.get('questions', []):
            so = q.get('sort_order', 0)
            if 41 <= so <= 45:
                print(f"Q{so}: ans={q.get('correct_answer')}, stem={repr(q.get('stem')[:60])}")
                print(f"  opts: {q.get('options')}")
