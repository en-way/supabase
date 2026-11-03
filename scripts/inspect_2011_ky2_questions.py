# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\53a52573-0afc-51a4-86b6-b2f321cbe6a8.json', encoding='utf-8') as f:
    d = json.load(f)

questions = d.get('questions', [])
print(f"Total questions: {len(questions)}")

for i, q in enumerate(questions):
    so = q.get('sort_order')
    pts = q.get('points')
    ans = q.get('correct_answer') or q.get('answer')
    opts = [o.get('text') for o in q.get('options', [])]
    stem = q.get('stem', '')
    exp = q.get('explanation', '')
    print(f"Q{so:02d}: ans={ans}, pts={pts}, opts_cnt={len(opts)}, exp_len={len(exp)}, stem={repr(stem[:60])}")
