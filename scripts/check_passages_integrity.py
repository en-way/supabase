import json
import glob
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

print("=== Checking Passage Integrity Across All 41 Exams ===")

for f in sorted(glob.glob('public/data/exams/*.json')):
    with open(f, 'r', encoding='utf-8') as jf:
        d = json.load(jf)
    yr = d['exam']['year']
    cat = d['exam']['category_id']
    passages = d.get('passages', [])
    questions = d.get('questions', [])
    stems = [q.get('stem', '').strip() for q in questions if len(q.get('stem', '').strip()) > 15]

    for p in passages:
        c = p.get('content', '').strip()
        so = p.get('sort_order')
        t = p.get('title')

        # Check if stem is in beginning
        for st in stems:
            if st in c[:200] and 'Directions' not in t and so != 1:
                print(f"[STEM IN PASSAGE] {yr} {cat} P{so} ({t}): stem = {st[:50]}")

        # Check abrupt ending
        if c and c[-1] not in ('.', '!', '?', '"', "'", ']', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print(f"[ABRUPT END] {yr} {cat} P{so} ({t}): ends with {repr(c[-40:])}")

        # Check word count or length
        if len(c) < 350 and so != 6:
            print(f"[SHORT PASSAGE] {yr} {cat} P{so} ({t}): len = {len(c)}")

print("=== Integrity Check Complete ===")
