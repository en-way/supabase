# -*- coding: utf-8 -*-
import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = 'public/data/exams'
for fpath in sorted(glob.glob(os.path.join(exams_dir, '*.json'))):
    d = json.load(open(fpath, encoding='utf-8'))
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    if yr == 2019 and cat == 'ky1':
        for p in d['passages']:
            if p['sort_order'] == 2:
                print(f"=== 2019 ky1 Text 1 Full Content ===")
                print(p['content'])
