import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

f = [x for x in glob.glob(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json') if json.load(open(x, encoding='utf-8'))['exam']['year'] == 2001 and json.load(open(x, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
d = json.load(open(f, encoding='utf-8'))
for q in d['questions']:
    so = q['sort_order']
    if so in [5, 6, 10]:
        print(f"=== 2001 Q{so} ===")
        print(q['explanation'][:400])
        print("...\n")
