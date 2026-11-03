# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\2d124f8f-f9af-5b94-9cc9-0087a76ee289.json'
with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Title:", d.get('title') or d.get('exam', {}).get('title'))
print("Year:", d.get('year') or d.get('exam', {}).get('year'))
print("Category:", d.get('category_id') or d.get('exam', {}).get('category_id'))
print("Passages count:", len(d.get('passages', [])))
print("Questions count:", len(d.get('questions', [])))

print("\n--- Passages Detail ---")
for i, p in enumerate(d.get('passages', [])):
    c = p.get('content', '')
    paras = c.split('\n\n')
    words = len(c.split())
    print(f"P{i} (id={p.get('id')}): title={repr(p.get('title'))}, type={p.get('type')}, num={p.get('passage_number')}, paras={len(paras)}, words={words}")
    print(f"    first 80 chars: {repr(c[:80])}")
    print(f"    last 60 chars: {repr(c[-60:])}")

print("\n--- Questions Summary ---")
qs = d.get('questions', [])
for i, q in enumerate(qs):
    so = q.get('sort_order') or q.get('question_number')
    stem = q.get('stem') or ''
    ans = q.get('correct_answer')
    pts = q.get('points')
    opts = [f"[{o.get('key')}]: {o.get('text')}" for o in q.get('options', [])]
    expl_len = len(q.get('explanation') or '')
    print(f"Q{i+1:02d} (so={so}, id={q.get('id')}): ans={ans}, pts={pts}, opts_count={len(opts)}, expl_len={expl_len}")
    print(f"    stem: {repr(stem[:70])}")
    if i in [0, 20, 25, 30, 35, 40]:
        print(f"    sample opts: {opts[:2]}")
