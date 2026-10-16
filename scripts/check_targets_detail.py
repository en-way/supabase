import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in sorted(glob.glob('public/data/exams/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    if yr == 2009 and cat == 'ky1':
        for q in d['questions']:
            if q['sort_order'] in [43, 44]:
                print(f"2009 ky1 Q{q['sort_order']}: len={len(q.get('explanation',''))}")
                print(q.get('explanation'))
                print("-" * 50)
    if yr == 2016 and cat == 'ky1':
        for q in d['questions']:
            if q['sort_order'] in [44, 45]:
                print(f"2016 ky1 Q{q['sort_order']}: len={len(q.get('explanation',''))}")
                print(q.get('explanation'))
                print("-" * 50)
    if yr == 2021 and cat == 'ky2':
        for q in d['questions']:
            if q['sort_order'] in [21, 23, 24, 25]:
                print(f"2021 ky2 Q{q['sort_order']}: len={len(q.get('explanation',''))}")
                print(q.get('explanation'))
                print("-" * 50)
    if yr == 2022 and cat == 'ky1':
        for q in d['questions']:
            if q['sort_order'] in [27, 32, 36, 37, 38, 39]:
                print(f"2022 ky1 Q{q['sort_order']}: len={len(q.get('explanation',''))}")
                print(q.get('explanation'))
                print("-" * 50)
    if yr == 2022 and cat == 'ky2':
        for q in d['questions']:
            if q['sort_order'] in [21, 22, 23]:
                print(f"2022 ky2 Q{q['sort_order']}: len={len(q.get('explanation',''))}")
                print(q.get('explanation'))
                print("-" * 50)
