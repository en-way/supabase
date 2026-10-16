import json

with open(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\666cdb4e-7fd3-53c2-8c91-a12fa3160c09.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for q in d['questions']:
    if q.get('sort_order') in [26, 27, 28, 29, 30]:
        print(f"Q{q['sort_order']}: stem={repr(q['stem'])}, ans={q['correct_answer']}")
        for o in q.get('options', []):
            print(f"   [{o.get('key')}]: {o.get('text')}")
