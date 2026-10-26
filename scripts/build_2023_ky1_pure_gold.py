import json

JSON_PATH = 'public/data/exams/b5992dc7-d0ac-56ce-8845-aa2c58675802.json'

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    d = json.load(f)

# 1. Standardize Exam
d['title'] = '2023年全国硕士研究生招生考试英语（一）真题'
d['total_score'] = 60.0
d['pass_score'] = 36.0

exam = d.get('exam', {})
exam['id'] = 'b5992dc7-d0ac-56ce-8845-aa2c58675802'
exam['title'] = '2023年全国硕士研究生招生考试英语（一）真题'
exam['duration_minutes'] = 180
exam['total_score'] = 60.0
exam['pass_score'] = 36.0
exam['approval_status'] = 'approved'
exam['is_published'] = True
exam['category_id'] = 'ky1'
exam['year'] = 2023
exam['passages'] = [{'count': 6}]
exam['questions'] = [{'count': 45}]
d['exam'] = exam

# 2. Standardize Passages
passages = d.get('passages', [])
assert len(passages) == 6, f"Expected 6 passages, found {len(passages)}"

# Passage 6: remove the 4 direction paragraphs, keep only [A]-[H]
p6 = passages[5]
p6_paras = [p.strip() for p in p6['content'].split('\n\n') if p.strip()]
if len(p6_paras) == 12:
    print("Trimming 4 direction paragraphs from Passage 6...")
    p6_paras = p6_paras[4:]
    p6['content'] = '\n\n'.join(p6_paras)

assert len([p for p in p6['content'].split('\n\n') if p.strip()]) == 8, f"Expected 8 paras in P6, found {len(p6['content'].split('\n\n'))}"

for idx, p in enumerate(passages, 1):
    p['sort_order'] = idx
    p['exam_id'] = 'b5992dc7-d0ac-56ce-8845-aa2c58675802'
    p['category_id'] = 'ky1'
    p['passage_type'] = None

passage_ids = [p['id'] for p in passages]

# 3. Standardize Questions
questions = d.get('questions', [])
assert len(questions) == 45, f"Expected 45 questions, found {len(questions)}"

official_answers = [
    'C', 'A', 'D', 'C', 'C', 'A', 'B', 'B', 'A', 'D',
    'D', 'C', 'C', 'B', 'A', 'B', 'D', 'A', 'D', 'A',
    'C', 'B', 'A', 'C', 'D',
    'A', 'D', 'B', 'C', 'D',
    'A', 'C', 'B', 'A', 'D',
    'B', 'C', 'B', 'B', 'D',
    'B', 'F', 'D', 'C', 'G'
]

for i, q in enumerate(questions, 1):
    q['question_number'] = i
    q['sort_order'] = i
    q['exam_id'] = 'b5992dc7-d0ac-56ce-8845-aa2c58675802'
    q['category_id'] = 'ky1'
    
    if i <= 20:
        q['passage_id'] = passage_ids[0]
        q['q_type'] = 'cloze_item'
        q['points'] = 0.5
        q['score'] = 0.5
    elif i <= 25:
        q['passage_id'] = passage_ids[1]
        q['q_type'] = 'reading_item'
        q['points'] = 2.0
        q['score'] = 2.0
    elif i <= 30:
        q['passage_id'] = passage_ids[2]
        q['q_type'] = 'reading_item'
        q['points'] = 2.0
        q['score'] = 2.0
    elif i <= 35:
        q['passage_id'] = passage_ids[3]
        q['q_type'] = 'reading_item'
        q['points'] = 2.0
        q['score'] = 2.0
    elif i <= 40:
        q['passage_id'] = passage_ids[4]
        q['q_type'] = 'reading_item'
        q['points'] = 2.0
        q['score'] = 2.0
    else:
        q['passage_id'] = passage_ids[5]
        q['q_type'] = 'reading_item'
        q['points'] = 2.0
        q['score'] = 2.0

    exp_ans = official_answers[i-1]
    act_ans = q.get('answer') or q.get('correct_answer')
    assert act_ans == exp_ans, f"Q{i} answer mismatch: expected {exp_ans}, got {act_ans}"
    q['answer'] = exp_ans
    q['correct_answer'] = exp_ans

    # Standardize options
    opts = q.get('options', [])
    new_opts = []
    for opt in opts:
        k = (opt.get('key') or opt.get('value') or '').strip()
        t = (opt.get('text') or opt.get('content') or '').strip()
        new_opts.append({
            'key': k,
            'value': k,
            'text': t,
            'content': t
        })
    q['options'] = new_opts

# Write back to JSON
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Successfully rebuilt 2023 ky1 pure gold json!")
