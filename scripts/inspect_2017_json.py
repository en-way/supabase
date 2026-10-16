# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if d['exam']['year'] == 2017 and d['exam']['category_id'] == 'ky1':
        print(f"File: {f}")
        for q in d['questions']:
            so = q['sort_order']
            if so in [39, 40]:
                print(f"=== Q{so} ===")
                print(f"Stem: {q['stem']}")
                print(f"Ans: {q['correct_answer']}")
                print(f"Options: {q['options']}")
                print("Explanation:")
                print(q['explanation'])
                print("-" * 50)
