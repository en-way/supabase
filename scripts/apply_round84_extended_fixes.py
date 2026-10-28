# -*- coding: utf-8 -*-
"""
apply_round84_extended_fixes.py
Applies the second-pass calibrations identified during ultra-deep forensic re-check:
1. 2014 ky1 Q16 options: strip (keep) ... (of/with)
2. 2012 ky1 Q6 options: strip (to)
3. 2012 ky1 Q7 options: strip (to)
4. 2020 ky1 Q20 option D: strip (with)
5. 2024 ky1 Q41-Q45 stems: harmonize to 'Match [Name] with [his/her] argument:'
"""

import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

EXAMS_DIR = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def load_json(exam_id):
    path = os.path.join(EXAMS_DIR, f"{exam_id}.json")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f), path

def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def run():
    print("=== Applying Round 84 Extended Polish Fixes ===")

    # 1. 2014 ky1 (240cc48a-439b-5d27-8464-f7dc53e060dc)
    d, p = load_json("240cc48a-439b-5d27-8464-f7dc53e060dc")
    for q in d['questions']:
        if q.get('sort_order') == 16:
            q['options'] = [
                {'key': 'A', 'value': 'A', 'text': 'order', 'content': 'order'},
                {'key': 'B', 'value': 'B', 'text': 'track', 'content': 'track'},
                {'key': 'C', 'value': 'C', 'text': 'pace', 'content': 'pace'},
                {'key': 'D', 'value': 'D', 'text': 'hold', 'content': 'hold'}
            ]
            print("  -> 2014 ky1 Q16 options cleaned.")
            break
    save_json(p, d)

    # 2. 2012 ky1 (baa66182-74ec-5a78-b2d2-077ffdcad9dc)
    d, p = load_json("baa66182-74ec-5a78-b2d2-077ffdcad9dc")
    for q in d['questions']:
        so = q.get('sort_order')
        if so == 6:
            q['options'] = [
                {'key': 'A', 'value': 'A', 'text': 'resistant', 'content': 'resistant'},
                {'key': 'B', 'value': 'B', 'text': 'subject', 'content': 'subject'},
                {'key': 'C', 'value': 'C', 'text': 'immune', 'content': 'immune'},
                {'key': 'D', 'value': 'D', 'text': 'prone', 'content': 'prone'}
            ]
            print("  -> 2012 ky1 Q6 options cleaned.")
        elif so == 7:
            q['options'] = [
                {'key': 'A', 'value': 'A', 'text': 'resorts', 'content': 'resorts'},
                {'key': 'B', 'value': 'B', 'text': 'sticks', 'content': 'sticks'},
                {'key': 'C', 'value': 'C', 'text': 'leads', 'content': 'leads'},
                {'key': 'D', 'value': 'D', 'text': 'applies', 'content': 'applies'}
            ]
            print("  -> 2012 ky1 Q7 options cleaned.")
    save_json(p, d)

    # 3. 2020 ky1 (f56943c1-0ba8-58fe-b7d3-061352345067)
    d, p = load_json("f56943c1-0ba8-58fe-b7d3-061352345067")
    for q in d['questions']:
        if q.get('sort_order') == 20:
            for opt in q['options']:
                if opt['key'] == 'D':
                    opt['text'] = 'end up'
                    opt['content'] = 'end up'
                    print("  -> 2020 ky1 Q20 option D cleaned.")
            break
    save_json(p, d)

    # 4. 2024 ky1 (f303f3fb-abfe-477f-a2e5-8dcd1ba78ef0)
    d, p = load_json("f303f3fb-abfe-477f-a2e5-8dcd1ba78ef0")
    stem_map = {
        41: 'Match Hannah with her argument:',
        42: 'Match Buck with his argument:',
        43: 'Match Sara with her argument:',
        44: 'Match Victor with his argument:',
        45: 'Match Julia with her argument:'
    }
    for q in d['questions']:
        so = q.get('sort_order')
        if so in stem_map:
            q['stem'] = stem_map[so]
            print(f"  -> 2024 ky1 Q{so} stem standardized.")
    save_json(p, d)

    print("=== Extended Polish Complete! ===")

if __name__ == '__main__':
    run()
