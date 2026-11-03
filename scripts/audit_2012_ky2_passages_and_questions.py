# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
p = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\2d124f8f-f9af-5b94-9cc9-0087a76ee289.json'
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)

print("=== Passages ===")
for i, ps in enumerate(d.get('passages', [])):
    print(f"\n--- Passage {i} ({ps.get('title')}) ---")
    lines = ps.get('content', '').splitlines()
    for l in lines[:5]:
        print("  ", l)
    if len(lines) > 5:
        print("   ...")
        for l in lines[-3:]:
            print("  ", l)

print("\n=== Questions 1-45 Answers & Stems ===")
for i, q in enumerate(d.get('questions', [])):
    opts = {o.get('key'): o.get('text') for o in q.get('options', [])}
    print(f"Q{i+1:02d}: Ans={q.get('correct_answer')}, Stem={repr(q.get('stem'))}")
    if i in [0, 1, 2, 20, 25, 30, 35, 40]:
        for k in sorted(opts.keys()):
            print(f"    [{k}] {opts[k]}")
