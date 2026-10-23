import json

path = 'public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for idx, q in enumerate(data.get('questions', [])):
    if idx < 20:
        q['q_type'] = 'cloze_item'
        q['points'] = 0.5
    else:
        q['q_type'] = 'reading_item'
        q['points'] = 2

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated 1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json with q_type and points.")
