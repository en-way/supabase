# -*- coding: utf-8 -*-
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

investigate_targets = [
    (2017, 'ky1', 39),
    (2017, 'ky1', 40),
    (2006, 'ky1', 20),
    (2008, 'ky1', 20),
    (2020, 'ky1', 23),
    (2020, 'ky1', 25),
    (2020, 'ky1', 28),
    (2018, 'ky1', 24),
    (2018, 'ky1', 27),
    (2018, 'ky1', 30),
    (2018, 'ky1', 34),
    (2018, 'ky1', 40),
    (2021, 'ky1', 24),
    (2002, 'ky1', 31),
    (2002, 'ky1', 32),
    (2002, 'ky1', 38),
    (2022, 'ky2', 8),
    (2022, 'ky2', 9),
    (2022, 'ky2', 12),
    (2022, 'ky2', 19),
    (2022, 'ky2', 20),
    (2022, 'ky2', 32),
    (2022, 'ky2', 38),
    (2022, 'ky2', 40),
    (2012, 'ky1', 33),
    (2012, 'ky1', 35),
    (2010, 'ky1', 27)
]

for f in sorted(glob.glob('public/data/exams/*.json')):
    d = json.load(open(f, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    for q in d.get('questions', []):
        so = q.get('sort_order')
        if (yr, cat, so) in investigate_targets:
            print(f"================ {yr} {cat} Q{so} ================")
            print(f"Stem: {q.get('stem')}")
            print(f"Ans: {q.get('correct_answer')}")
            print(f"Opts: {[o.get('text') for o in q.get('options', [])]}")
            expl = q.get('explanation', '')
            lines = expl.split('\n')
            print("Expl head 5 lines:")
            for l in lines[:5]:
                print("  ", l)
