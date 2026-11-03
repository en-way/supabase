import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json", "r", encoding="utf-8") as f:
    d2020 = json.load(f)

for q in d2020['questions']:
    qn = q['question_number']
    expl = q.get('explanation', '')
    for line in expl.split('\n'):
        # Find camelCase or lowercase glued words of length >= 14
        tokens = re.findall(r'[A-Za-z]{14,}', line)
        real_exclusions = {'interdisciplinary', 'hospitalizations', 'antidiscrimination', 'unrepresentative', 'unsubstantiated', 'characteristics', 'correspondingly'}
        tokens = [t for t in tokens if t.lower() not in real_exclusions]
        if tokens:
            print(f"2020 Q{qn}: {tokens} in line: {line[:90]}")
