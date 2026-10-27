import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
path = 'public/data/exams/9286880b-8738-4d73-8697-e70bdd8257c6.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

exam = data['exam']
exam['title'] = '2024年全国硕士研究生招生考试英语（二）真题'
exam['duration_minutes'] = 180
exam['total_score'] = 60.0
exam['pass_score'] = 36.0
exam['approval_status'] = 'approved'
exam['is_published'] = True

passages = data['passages']

# Passage 1: Cloze
p1 = passages[0]
p1_paras = [p.strip() for p in p1['content'].split('\n\n') if p.strip()]
if p1_paras[0].startswith('Directions:'):
    p1_paras = p1_paras[1:]
p1['content'] = '\n\n'.join(p1_paras)
p1['title'] = 'Section I: Use of English'
p1['section_type'] = 'use_of_english'
p1['passage_type'] = 'cloze'
p1['sort_order'] = 1

# Passage 2: Text 1
p2 = passages[1]
p2['title'] = 'Section II: Reading Comprehension Part A - Text 1'
p2['section_type'] = 'reading'
p2['passage_type'] = None
p2['sort_order'] = 2

# Passage 3: Text 2
p3 = passages[2]
p3['title'] = 'Section II: Reading Comprehension Part A - Text 2'
p3['section_type'] = 'reading'
p3['passage_type'] = None
p3['sort_order'] = 3

# Passage 4: Text 3
p4 = passages[3]
p4['title'] = 'Section II: Reading Comprehension Part A - Text 3'
p4['section_type'] = 'reading'
p4['passage_type'] = None
p4['sort_order'] = 4

# Passage 5: Text 4
p5 = passages[4]
p5['title'] = 'Section II: Reading Comprehension Part A - Text 4'
p5['section_type'] = 'reading'
p5['passage_type'] = None
p5['sort_order'] = 5

# Passage 6: Part B
p6 = passages[5]
p6_paras = [p.strip() for p in p6['content'].split('\n\n') if p.strip()]
# Filter out Directions paragraphs and options [A]-[G]
filtered_paras = []
for para in p6_paras:
    if para.startswith('Directions:') or para.startswith('There are two extra choices'):
        continue
    if para.startswith('[A]') or para.startswith('[B]') or para.startswith('[C]') or para.startswith('[D]') or para.startswith('[E]') or para.startswith('[F]') or para.startswith('[G]'):
        continue
    filtered_paras.append(para)

p6['content'] = '\n\n'.join(filtered_paras)
p6['title'] = 'Section II: Reading Comprehension Part B'
p6['section_type'] = 'reading'
p6['passage_type'] = None
p6['sort_order'] = 6

# Questions
questions = data['questions']
for i, q in enumerate(questions, 1):
    q['sort_order'] = i
    q['question_number'] = i
    pts = 0.5 if i <= 20 else 2.0
    q['points'] = pts
    q['score'] = pts
    q['q_type'] = 'cloze_item' if i <= 20 else 'reading_item'
    q['category_id'] = 'ky2'
    q['exam_id'] = '9286880b-8738-4d73-8697-e70bdd8257c6'
    
    # standardize options
    opts = q.get('options', [])
    new_opts = []
    for o in opts:
        k = o.get('key')
        t = o.get('text') or o.get('content')
        new_opts.append({
            'key': k,
            'value': k,
            'text': t,
            'content': t
        })
    q['options'] = new_opts

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Successfully built 2024 ky2 pure gold JSON!')
print('Passages summary:')
for i, p in enumerate(passages, 1):
    paras = p['content'].split('\n\n')
    words = len(p['content'].split())
    print(f'Passage {i} ({p["title"]}): {len(paras)} paras, {words} words')
    print('  Start:', repr(p['content'][:60]))
    print('  End:  ', repr(p['content'][-60:]))
