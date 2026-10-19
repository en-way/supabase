import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Scanning all ky1 exams for short explanations (<250 chars) ===")

ky1_files = sorted([f for f in glob.glob('public/data/exams/*.json')])

short_items = []
for f in ky1_files:
    d = json.load(open(f, encoding='utf-8'))
    if d['exam']['category_id'] == 'ky1':
        yr = d['exam']['year']
        for q in d['questions']:
            so = q['sort_order']
            expl = q.get('explanation', '')
            if so in range(21, 41) and len(expl) < 250:
                short_items.append((yr, so, len(expl), expl[:50]))

print(f"Total short reading explanations in ky1: {len(short_items)}")
for item in short_items:
    print(f"  - {item[0]} ky1 Q{item[1]}: len={item[2]} -> {repr(item[3])}")
