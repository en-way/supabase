# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_id = "207d2963-734a-52bd-9fa3-6c341efb5974"
json_path = f"public/data/exams/{exam_id}.json"

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

print(f"Title: {d.get('title')}")
assert d.get('title') == "2010年全国硕士研究生入学统一考试英语（二）真题", "Title mismatch"

passages = d.get('passages', [])
assert len(passages) == 6, f"Expected 6 passages, got {len(passages)}"

expected_answers = [
    # Cloze 1-20
    'D', 'C', 'B', 'A', 'A', 'B', 'D', 'C', 'B', 'A',
    'C', 'D', 'D', 'A', 'C', 'B', 'D', 'C', 'A', 'B',
    # Reading 21-40
    'D', 'A', 'B', 'C', 'C', 'A', 'C', 'B', 'D', 'C',
    'A', 'A', 'D', 'C', 'B', 'D', 'A', 'C', 'B', 'D',
    # Part B 41-45
    'F', 'T', 'F', 'T', 'F'
]

questions = d.get('questions', [])
assert len(questions) == 45, f"Expected 45 questions, got {len(questions)}"

total_score = 0.0
for i, q in enumerate(questions):
    qnum = q.get('question_number')
    assert qnum == i + 1, f"Q{i+1} has wrong question_number: {qnum}"
    ans = q.get('correct_answer')
    exp_ans = expected_answers[i]
    assert ans == exp_ans, f"Q{qnum} expected {exp_ans}, got {ans}"
    score = q.get('score')
    if qnum <= 20:
        assert score == 0.5, f"Q{qnum} expected score 0.5, got {score}"
    else:
        assert score == 2.0, f"Q{qnum} expected score 2.0, got {score}"
    total_score += score
    exp = q.get('explanation', '')
    assert len(exp) > 50, f"Q{qnum} explanation too short: {len(exp)}"
    assert '［' in exp or '[' in exp, f"Q{qnum} lacks standard tag"

print(f"Total calculated score: {total_score} (Expected: 60.0)")
assert total_score == 60.0, "Total score mismatch"
print("All 45 questions and 6 passages verified successfully!")
