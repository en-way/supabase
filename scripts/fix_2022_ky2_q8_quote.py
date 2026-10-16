import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('public/data/exams/*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    if d.get('exam', {}).get('year') == 2022 and d.get('exam', {}).get('category_id') == 'ky2':
        for q in d.get('questions', []):
            if q.get('sort_order') == 8:
                expl = q.get('explanation', '')
                if 'attention44突' in expl:
                    q['explanation'] = expl.replace('attention44突', 'attention”突')
                    with open(f, 'w', encoding='utf-8') as fp2:
                        json.dump(d, fp2, ensure_ascii=False, indent=2)
                    print("Fixed 44 quote in 2022 ky2 Q8!")
