# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

exam = data['exam']
print("Exam Title:", exam.get('title'))
assert exam.get('title') == "2013年全国硕士研究生入学统一考试英语（二）真题"
assert float(exam.get('total_score')) == 60.0

passages = data['passages']
print("Passages count:", len(passages))
assert len(passages) == 6

expected_para_counts = [4, 6, 5, 6, 7, 6]
for idx, p in enumerate(passages):
    paras = [para.strip() for para in p['text'].split('\n\n') if para.strip()]
    print(f"Passage {idx} ({p['section_type']}, {p['title']}): {len(paras)} paras, {len(p['text'].split())} words")
    assert len(paras) == expected_para_counts[idx], f"Passage {idx} paras {len(paras)} != {expected_para_counts[idx]}"

questions = data['questions']
print("Questions count:", len(questions))
assert len(questions) == 45

total_pts = 0
for idx, q in enumerate(questions):
    assert q['question_number'] == idx + 1
    assert q['sort_order'] == idx + 1
    assert q['question_type'] == 'multiple_choice'
    assert q['answer'] == q['correct_answer']
    total_pts += q['points']
    opts = q['options']
    assert isinstance(opts, dict)
    if idx < 40:
        assert set(opts.keys()) == {'A', 'B', 'C', 'D'}
        for k, v in opts.items():
            assert v != k and len(v) > 0
    else:
        assert set(opts.keys()) == {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
        for k, v in opts.items():
            assert v != k and len(v) > 0
    expl = q['explanation']
    assert len(expl) > 60
    assert '【精准定位】' in expl or '【命题解密】' in expl

print(f"Total points calculated: {total_pts}")
assert total_pts == 60.0

print("ALL LOCAL 2013 KY2 TESTS PASSED PERFECTLY!")
