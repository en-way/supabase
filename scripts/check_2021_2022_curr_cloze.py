import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

for y in [2021, 2022]:
    for f in glob.glob('public/data/exams/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        exam = d.get('exam', {})
        if exam.get('category_id') == 'ky2' and exam.get('year') == y:
            print(f'=== {y} ky2 current cloze ===')
            qs = d.get('questions', [])
            cloze_qs = [q for q in qs if 1 <= q.get('sort_order', 0) <= 20]
            print('Count:', len(cloze_qs))
            for q in cloze_qs[:5]:
                so = q['sort_order']
                exp = q.get('explanation', '')
                print(f"  Q{so}: len={len(exp)}, text={repr(exp[:60])}")
