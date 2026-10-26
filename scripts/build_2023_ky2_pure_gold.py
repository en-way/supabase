import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

JSON_PATH = 'public/data/exams/0a5fc663-29a1-504d-981d-49763767e394.json'

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    d = json.load(f)

# 1. Standardize Exam
d['title'] = '2023年全国硕士研究生招生考试英语（二）真题'
d['total_score'] = 60.0
d['pass_score'] = 36.0

exam = d.get('exam', {})
exam['id'] = '0a5fc663-29a1-504d-981d-49763767e394'
exam['title'] = '2023年全国硕士研究生招生考试英语（二）真题'
exam['duration_minutes'] = 180
exam['total_score'] = 60.0
exam['pass_score'] = 36.0
exam['approval_status'] = 'approved'
exam['is_published'] = True
exam['category_id'] = 'ky2'
exam['year'] = 2023
exam['passages'] = [{'count': 6}]
exam['questions'] = [{'count': 45}]
d['exam'] = exam

# 2. Standardize Passages
passages = d.get('passages', [])
assert len(passages) == 6, f"Expected 6 passages, found {len(passages)}"

# Passage 6: remove the 2 direction paragraphs, keep title + [I]-[XII]
p6 = passages[5]
p6_paras = [p.strip() for p in p6['content'].split('\n\n') if p.strip()]
if len(p6_paras) == 15:
    print("Trimming 2 direction paragraphs from Passage 6...")
    p6_paras = p6_paras[2:]
    p6['content'] = '\n\n'.join(p6_paras)

paras_clean = [p for p in p6['content'].split('\n\n') if p.strip()]
assert len(paras_clean) == 13, f"Expected 13 paras in P6, found {len(paras_clean)}"

for idx, p in enumerate(passages, 1):
    p['sort_order'] = idx
    p['exam_id'] = '0a5fc663-29a1-504d-981d-49763767e394'
    p['category_id'] = 'ky2'
    p['passage_type'] = None

passage_ids = [p['id'] for p in passages]

# 3. Standardize Questions
questions = d.get('questions', [])
assert len(questions) == 45, f"Expected 45 questions, found {len(questions)}"

official_answers = [
    'B', 'C', 'A', 'D', 'D', 'D', 'A', 'B', 'B', 'C',
    'C', 'D', 'C', 'A', 'A', 'B', 'D', 'B', 'C', 'A',
    'A', 'B', 'B', 'C', 'D',
    'D', 'A', 'C', 'B', 'D',
    'C', 'C', 'A', 'A', 'B',
    'A', 'C', 'D', 'B', 'A',
    'D', 'F', 'B', 'A', 'G'
]

for i, q in enumerate(questions, 1):
    q['question_number'] = i
    q['sort_order'] = i
    q['exam_id'] = '0a5fc663-29a1-504d-981d-49763767e394'
    q['category_id'] = 'ky2'
    
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

print("Successfully rebuilt 2023 ky2 pure gold json!")
