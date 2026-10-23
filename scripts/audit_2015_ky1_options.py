# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json

with open(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\865e5af8-24a4-58e1-bc9e-640f32d8e946.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== CLOZE OPTIONS (Q1-Q20) ===")
for i in range(20):
    q = d['questions'][i]
    ans = q.get('answer')
    opts_str = ' | '.join(['[' + o['key'] + '] ' + o['text'] for o in q['options']])
    print(f"Q{i+1:02d} (ans={ans}): {opts_str}")

print("\n=== READING OPTIONS (Q21-Q40) ===")
for i in range(20, 40):
    q = d['questions'][i]
    ans = q.get('answer')
    opts_str = ' | '.join(['[' + o['key'] + '] ' + o['text'] for o in q['options']])
    print(f"Q{i+1:02d} (ans={ans}): {opts_str}")
