# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json'
with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

exam = d.get('exam', {})
print('Exam title:', repr(exam.get('title')))

questions = d.get('questions', [])
print(f'\n=== Questions count: {len(questions)} ===')

issues = []
for q in questions:
    qno = q.get('question_number')
    so = q.get('sort_order')
    ca = q.get('correct_answer')
    opts = q.get('options')
    expl = q.get('explanation', '')
    stem = q.get('stem', '')
    pts = q.get('points')
    qt = q.get('q_type')
    
    opt_keys = []
    if isinstance(opts, dict):
        opt_keys = list(opts.keys())
    elif isinstance(opts, list):
        opt_keys = [str(x) for x in opts]
        issues.append(f'Q{qno}: options is list, not dict! Content: {opts}')
    else:
        issues.append(f'Q{qno}: options is {type(opts)}')
    
    expl_len = len(expl) if expl else 0
    if expl_len < 100:
        issues.append(f'Q{qno} (sort={so}): expl short ({expl_len})')
    if isinstance(opts, dict) and ca not in opts:
        issues.append(f'Q{qno}: ca {ca} not in opts keys {opt_keys}')
    if not stem:
        issues.append(f'Q{qno}: empty stem')
    
    qno_str = f"Q{qno:02d}" if isinstance(qno, int) else f"Q(None)"
    so_str = f"sort={so:02d}" if isinstance(so, int) else f"sort={so}"
    print(f'{qno_str} ({so_str}, {qt}, {pts}pt): Ans={ca}, OptKeys={opt_keys}, ExplLen={expl_len}, Stem="{stem[:50]}..."')

print(f'\nTotal detected issues: {len(issues)}')
for iss in issues:
    print('  -', iss)
