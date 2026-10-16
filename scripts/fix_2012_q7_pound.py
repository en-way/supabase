import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('public/data/exams/*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    if d.get('exam', {}).get('year') == 2012 and d.get('exam', {}).get('category_id') == 'ky1':
        for q in d.get('questions', []):
            if q.get('sort_order') == 7:
                expl = q.get('explanation', '')
                if 'o£' in expl:
                    q['explanation'] = expl.replace('o£', 'of')
                    with open(f, 'w', encoding='utf-8') as fp2:
                        json.dump(d, fp2, ensure_ascii=False, indent=2)
                    print("Replaced o£ with of in 2012 Q7 successfully!")
