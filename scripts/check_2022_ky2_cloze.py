# -*- coding: utf-8 -*-
import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

for f in glob.glob('public/data/exams/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    if d['exam']['year'] == 2022 and d['exam']['category_id'] == 'ky2':
        for q in d['questions']:
            so = q['sort_order']
            if 1 <= so <= 20:
                opts = [f"[{o['key']}] {o['text']}" for o in q.get('options', [])]
                expl_head = q.get('explanation', '').split('\n')[0]
                print(f"Q{so:02d}: Ans={q.get('correct_answer')} | Opts={opts[:2]} | ExplHead={expl_head[:60]}")
