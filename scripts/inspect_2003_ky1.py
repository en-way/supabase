# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if d['exam']['year'] == 2003 and d['exam']['category_id'] == 'ky1':
        print(f"File: {f}")
        for q in d['questions']:
            so = q['sort_order']
            if so in [1, 2, 3, 21, 26, 31, 36]:
                print(f"Q{so}: {q['stem']}")
                print(f"  Ans: {q['correct_answer']}")
                print(f"  Opts: {[o.get('text') for o in q.get('options', [])]}")
