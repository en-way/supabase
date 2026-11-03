import json

path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\17ca33c3-66f2-5ae0-a1ba-847f507dd6e4.json'
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

for i in [0, 1, 20, 21, 30, 31, 40, 41]:
    q = d['questions'][i]
    print(f"--- Q{i+1} ---")
    print("num:", q.get('question_number'))
    print("ans:", q.get('answer'))
    print("type:", q.get('question_type'))
    print("score:", q.get('score'))
    print("stem:", q.get('stem'))
    print("options:", type(q.get('options')), q.get('options'))
    print("analysis len:", len(q.get('analysis', '') or ''))
