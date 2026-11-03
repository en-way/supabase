import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect camelCase patterns like `[a-z]+[A-Z]`
with open(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json", "r", encoding="utf-8") as f:
    d = json.load(f)

print("--- DETECTING CAMELCASE IN 2020 KY2 ---")
for q in d['questions']:
    qn = q['question_number']
    expl = q.get('explanation', '')
    matches = re.findall(r'[a-z]+[A-Z][a-zA-Z]*', expl)
    if matches:
        # filter out acceptable acronyms or normal words if any
        print(f"Q{qn}: {matches}")
