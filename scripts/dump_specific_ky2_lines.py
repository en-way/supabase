import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for qn in [23, 24, 25, 26, 30, 32, 34, 36, 37, 38, 40]:
    q = [x for x in d['questions'] if x['question_number'] == qn][0]
    expl = q.get('explanation', '')
    print(f"==================== Q{qn} ====================")
    for line in expl.split('\n'):
        if any(term in line for term in ['anetWiles', 'largeAmerican', 'sCEO', 'ontoA', 'areacting', 'theFederal', 'enZ', 'surveyof', 'enerations']):
            print("  LINE:", line)
