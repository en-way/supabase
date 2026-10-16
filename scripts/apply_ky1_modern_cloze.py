#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_ky1_modern_cloze.py
将 2016-2022 年考研英语一 26 道缺陷完型试题（含 2022 全量 20 题、2017 Q14/Q17/Q18、2016 Q1/Q19、2018 Q10）
注入 public/data/exams/*.json。
"""

import os
import sys
import glob
import json

sys.stdout.reconfigure(encoding='utf-8')

RESTORED_PATH = os.path.join(os.path.dirname(__file__), 'ky1_modern_cloze_restored.json')
EXAMS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'exams'))

def main():
    with open(RESTORED_PATH, 'r', encoding='utf-8') as f:
        restored = json.load(f)

    exam_files = glob.glob(os.path.join(EXAMS_DIR, '*.json'))
    total_updated = 0

    for ep in exam_files:
        with open(ep, 'r', encoding='utf-8') as f:
            d = json.load(f)
        
        exam = d.get('exam', {})
        cat = exam.get('category_id')
        yr = str(exam.get('year'))

        if cat == 'ky1' and yr in restored:
            yr_updates = restored[yr]
            modified = False
            for q in d.get('questions', []):
                so = str(q.get('sort_order'))
                if so in yr_updates:
                    old_len = len(q.get('explanation') or '')
                    new_exp = yr_updates[so]
                    q['explanation'] = new_exp
                    modified = True
                    total_updated += 1
                    print(f"[{yr} ky1 Q{so:2s}] Explanation upgraded: {old_len} chars -> {len(new_exp)} chars")
            
            if modified:
                with open(ep, 'w', encoding='utf-8') as f:
                    json.dump(d, f, ensure_ascii=False, indent=2)
                print(f"Saved updated exam: {yr} ky1 ({ep})")

    print(f"\nSuccessfully applied upgrades to {total_updated} questions across English I modern years!")

if __name__ == '__main__':
    main()
