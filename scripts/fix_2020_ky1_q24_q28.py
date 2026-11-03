import json

path = 'public/data/exams/f56943c1-0ba8-58fe-b7d3-061352345067.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data['questions']:
    so = q.get('sort_order') or q.get('question_number')
    if so == 24:
        if 'A u town of culture could be' in q['explanation']:
            idx = q['explanation'].find('IV')
            if idx != -1:
                q['explanation'] = q['explanation'][:idx].strip()
            else:
                idx = q['explanation'].find('A u town of culture could be')
                q['explanation'] = q['explanation'][:idx].strip()
            print("Fixed Q24 explanation tail.")
    if so == 28:
        if q['explanation'].endswith('让权力重获平衡”。'):
            q['explanation'] = q['explanation'][:-1] + '相符。'
            print("Fixed Q28 explanation ending.")

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated json successfully!")
