import json

p = 'public/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json'
d = json.load(open(p, encoding='utf-8'))
for q in d['questions']:
    if q['sort_order'] == 22:
        q['stem'] = 'The statement "it is all too monkey" (Last line, Paragraph 1) implies that ________.'
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('Updated 2005 ky1 Q22 stem with blank.')
