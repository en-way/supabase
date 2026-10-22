import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_id = "e5abf09b-e94d-5994-b944-7c5711cd4e4d"
json_path = f"public/data/exams/{exam_id}.json"

print("=== Starting 2010 ky1 Gold Calibration ===")

with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

with open('scripts/extracted_2010_all_gold.json', 'r', encoding='utf-8') as f:
    extracted_exps = json.load(f)

# 1. Update Title in both root and exam object
official_title = "2010年全国硕士研究生入学统一考试英语（一）真题"
exam_data['title'] = official_title
if 'exam' in exam_data:
    exam_data['exam']['title'] = official_title
print(f"Exam title set to: {official_title}")

# 2. Update Passages
passage_specs = [
    {
        "type": "cloze",
        "passage_number": 1,
        "title": "Section I: Use of English"
    },
    {
        "type": "reading",
        "passage_number": 1,
        "title": "Section II: Reading Comprehension Part A - Text 1"
    },
    {
        "type": "reading",
        "passage_number": 2,
        "title": "Section II: Reading Comprehension Part A - Text 2"
    },
    {
        "type": "reading",
        "passage_number": 3,
        "title": "Section II: Reading Comprehension Part A - Text 3"
    },
    {
        "type": "reading",
        "passage_number": 4,
        "title": "Section II: Reading Comprehension Part A - Text 4"
    },
    {
        "type": "reading_part_b",
        "passage_number": 5,
        "title": "Section II: Reading Comprehension Part B"
    }
]

passages = exam_data.get('passages', [])
for i, spec in enumerate(passage_specs):
    if i < len(passages):
        passages[i]['type'] = spec['type']
        passages[i]['passage_number'] = spec['passage_number']
        passages[i]['title'] = spec['title']
        print(f"Passage {i} calibrated: type={spec['type']}, num={spec['passage_number']}, title={spec['title']}")

# 3. Update Questions
questions = exam_data.get('questions', [])
total_points = 0.0

for idx, q in enumerate(questions):
    qnum = idx + 1
    q['question_number'] = qnum
    q['sort_order'] = qnum
    
    # Points & Type
    if qnum <= 20:
        q['type'] = "cloze_item"
        q['q_type'] = "cloze_item"
        q['points'] = 0.5
    else:
        q['type'] = "reading_item"
        q['q_type'] = "reading_item"
        q['points'] = 2.0
    
    total_points += q['points']
    
    # Clean options punctuation
    if qnum == 30:
        for opt in q.get('options', []):
            if opt.get('key') == 'C' and opt.get('text', '').endswith('patents'):
                opt['text'] = opt['text'] + '.'
    elif qnum == 35:
        for opt in q.get('options', []):
            if opt.get('key') == 'C' and opt.get('text', '').endswith('influenced'):
                opt['text'] = opt['text'] + '.'
                
    # Inject pure gold explanation
    gold_exp = extracted_exps.get(str(qnum))
    if gold_exp:
        q['explanation'] = gold_exp
    else:
        print(f"Warning: No gold explanation for Q{qnum}")

print(f"Total points calculated: {total_points} (Target: 60.0)")
assert total_points == 60.0, f"Error: Total points is {total_points}, expected 60.0"

# Save calibrated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("Saved calibrated JSON successfully!")
