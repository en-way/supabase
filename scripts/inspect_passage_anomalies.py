# -*- coding: utf-8 -*-
import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams = [
    (2014, 'ky1', 4, 'Reading Text 3'),
    (2021, 'ky2', 1, 'Cloze'),
    (2019, 'ky1', 2, 'Reading Text 1'),
    (2019, 'ky1', 5, 'Reading Text 4'),
    (2022, 'ky2', 4, 'Reading Text 3'),
    (2008, 'ky1', 4, 'Reading Text 3'),
]

exams_dir = 'public/data/exams'
for fpath in sorted(glob.glob(os.path.join(exams_dir, '*.json'))):
    d = json.load(open(fpath, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    for e_yr, e_cat, e_so, desc in exams:
        if yr == e_yr and cat == e_cat:
            for p in d['passages']:
                if p['sort_order'] == e_so:
                    c = p['content']
                    print(f"=== {yr} {cat} P{e_so} ({desc}) ===")
                    print(f"Last 250 chars:\n{c[-250:]}\n")
