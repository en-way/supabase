# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if d['exam']['year'] == 2008 and d['exam']['category_id'] == 'ky1':
        for q in d['questions']:
            so = q['sort_order']
            if so in [18, 19, 20]:
                print(f"2008 Q{so} opts: {[o.get('text') for o in q.get('options', [])]}")
                print(f"2008 Q{so} expl: {q.get('explanation', '')[:100]}")
