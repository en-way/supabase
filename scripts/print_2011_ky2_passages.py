# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\53a52573-0afc-51a4-86b6-b2f321cbe6a8.json', encoding='utf-8') as f:
    d = json.load(f)

for i, p in enumerate(d.get('passages', [])):
    c = p.get('content', '')
    t = p.get('title', '')
    print(f"\n=== Passage {i}: {t} ===")
    print(f"Type: {p.get('type')}, passage_type: {p.get('passage_type')}, Words: {len(c.split())}, Chars: {len(c)}")
    print(f"Start: {repr(c[:140])}")
    print(f"End:   {repr(c[-140:])}")
