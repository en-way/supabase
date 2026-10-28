# -*- coding: utf-8 -*-
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 86 Calibration: Section Type & Title Canonicalization ===")

# 1. Update 2001 ky1 and 2012 ky1 section_types
files_to_fix_section_type = [
    '2c892204-071f-5943-86be-d49bca93fe71.json', # 2001 ky1
    'baa66182-74ec-5a78-b2d2-077ffdcad9dc.json', # 2012 ky1
]

for fname in files_to_fix_section_type:
    for ddir in ['public/data/exams', 'out/data/exams']:
        fpath = os.path.join(ddir, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for idx, p in enumerate(data['passages']):
            if idx == 0:
                p['section_type'] = 'cloze'
            else:
                p['section_type'] = 'reading'
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Fixed section_types in {fpath}")

# 2. Canonicalize 2011 ky1 and 2011 ky2 passage titles
files_to_fix_titles = [
    '111d6c78-81a1-53dc-a039-dad4c94ebd35.json', # 2011 ky1
    '53a52573-0afc-51a4-86b6-b2f321cbe6a8.json', # 2011 ky2
]

title_map = {
    2: 'Section II: Reading Comprehension Part A - Text 1',
    3: 'Section II: Reading Comprehension Part A - Text 2',
    4: 'Section II: Reading Comprehension Part A - Text 3',
    5: 'Section II: Reading Comprehension Part A - Text 4',
}

for fname in files_to_fix_titles:
    for ddir in ['public/data/exams', 'out/data/exams']:
        fpath = os.path.join(ddir, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for p in data['passages']:
            so = p.get('sort_order')
            if so in title_map:
                p['title'] = title_map[so]
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Standardized passage titles in {fpath}")

print("Local JSON files updated successfully!")
