# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\53a52573-0afc-51a4-86b6-b2f321cbe6a8.json', encoding='utf-8') as f:
    d = json.load(f)

for i, p in enumerate(d.get('passages', [])):
    c = p.get('content', '')
    title = p.get('title', '')
    long_words = re.findall(r'[a-zA-Z]{15,}', c)
    print(f"\n=== Passage {i}: {title} ===")
    if long_words:
        print(f"  Long words (>=15 chars, count={len(long_words)}): {long_words}")
    else:
        print("  Clean: no words >= 15 chars.")
