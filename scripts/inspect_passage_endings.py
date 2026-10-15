import json
import glob
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

targets = [
    (2019, 'ky2', 4),
    (2013, 'ky2', 4),
    (2014, 'ky1', 1),
    (2014, 'ky1', 4),
    (2014, 'ky1', 6),
    (2021, 'ky2', 1),
    (2016, 'ky1', 3),
    (2016, 'ky1', 5),
    (2016, 'ky1', 6),
    (2018, 'ky2', 2),
    (2018, 'ky2', 3),
    (2022, 'ky2', 2),
    (2022, 'ky2', 4),
    (2008, 'ky1', 2),
    (2010, 'ky1', 1),
    (2010, 'ky1', 6),
    (2012, 'ky1', 6),
    (2009, 'ky1', 2),
    (2018, 'ky1', 2),
    (2020, 'ky1', 4),
]

for yr, cat, so in targets:
    fpath = [f for f in glob.glob('public/data/exams/*.json') if json.load(open(f, encoding='utf-8'))['exam']['year'] == yr and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == cat][0]
    d = json.load(open(fpath, encoding='utf-8'))
    p = [x for x in d['passages'] if x['sort_order'] == so][0]
    c = p['content'].strip()
    print(f"=== {yr} {cat} P{so} ({p['title']}) ===")
    print("Start:", repr(c[:80]))
    print("End  :", repr(c[-120:]))
    print()
