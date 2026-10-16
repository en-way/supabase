# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if d['exam']['year'] == 2017 and d['exam']['category_id'] == 'ky1':
        for q in d['questions']:
            so = q['sort_order']
            if so in [36, 37, 38, 39, 40]:
                print(f"=== 2017 ky1 Q{so} ===")
                print(f"Stem: {q['stem']}")
                print(f"Ans: {q['correct_answer']}")
                print("Options:")
                for o in q['options']:
                    print(f"  [{o.get('key')}] {o.get('text')}")
                print("Expl head:")
                print(q.get('explanation', '')[:120])
                print("-" * 50)
