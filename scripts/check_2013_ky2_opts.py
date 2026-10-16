import json

with open(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for q in d['questions']:
    if q.get('sort_order') in range(41, 46):
        print(f"Q{q['sort_order']}: ans={q.get('correct_answer')}")
        for o in q.get('options', []):
            print(f"   [{o.get('key')}]: {o.get('text')}")
        break
