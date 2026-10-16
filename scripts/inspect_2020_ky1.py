# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if d['exam']['year'] == 2020 and d['exam']['category_id'] == 'ky1':
        for p in d['passages']:
            if p['sort_order'] == 3:
                print("2020 ky1 Passage 3 title:", p['title'])
                print("Content head:", p['content'][:200])
        for q in d['questions']:
            if 26 <= q['sort_order'] <= 30:
                print(f"Q{q['sort_order']}: {q['stem']}")
