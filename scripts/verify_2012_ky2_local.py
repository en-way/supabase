# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

JSON_PATH = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\2d124f8f-f9af-5b94-9cc9-0087a76ee289.json'

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    d = json.load(f)

title = d.get('title') or d.get('exam', {}).get('title')
print(f"Title: {title}")
assert title == '2012年全国硕士研究生入学统一考试英语（二）真题', f"Title mismatch: {title}"

passages = d.get('passages', [])
print(f"Passages count: {len(passages)}")
assert len(passages) == 6, f"Expected 6 passages, got {len(passages)}"

expected_types = ['cloze', 'reading', 'reading', 'reading', 'reading', 'reading_part_b']
for i, p in enumerate(passages):
    exp_t = expected_types[i]
    act_t = p.get('type')
    assert act_t == exp_t, f"Passage {i} type mismatch: expected {exp_t}, got {act_t}"
    p_num = p.get('passage_number')
    assert p_num is not None, f"Passage {i} passage_number is None"
    c = p.get('content', '')
    paras = c.split('\n\n')
    words = len(c.split())
    print(f"Passage {i} ({p.get('title')}): type={act_t}, p_num={p_num}, paras={len(paras)}, words={words}")
    # Verify no bad concat
    assert 'Thehomeworkrulesshould' not in c, f"Bad concat in passage {i}"
    assert 'across-the-boardrule' not in c, f"Bad concat in passage {i}"
    assert 'shouldbe' not in c, f"Bad concat in passage {i}"
    assert 'e of the or invent them' not in c, f"Truncation artifact in passage {i}"
    assert 'G. [1]. Joe' not in c, f"G. [1]. Joe artifact in passage {i}"

# Check questions
questions = d.get('questions', [])
print(f"Questions count: {len(questions)}")
assert len(questions) == 45, f"Expected 45 questions, got {len(questions)}"

total_pts = 0.0
for i, q in enumerate(questions):
    so = q.get('sort_order')
    qn = q.get('question_number')
    assert so == i + 1, f"Question {i+1} sort_order mismatch: {so}"
    assert qn == i + 1, f"Question {i+1} question_number mismatch: {qn}"
    
    pts = float(q.get('points', 0))
    total_pts += pts
    q_type = q.get('q_type')
    ans = q.get('correct_answer')
    ans_alt = q.get('answer')
    assert ans == ans_alt, f"Q{so} ans ({ans}) != ans_alt ({ans_alt})"
    
    expl = q.get('explanation', '')
    assert len(expl) > 50, f"Q{so} explanation too short: {len(expl)}"
    
    opts = q.get('options', [])
    if so <= 20:
        assert pts == 0.5, f"Q{so} points should be 0.5, got {pts}"
        assert q_type == 'cloze_item', f"Q{so} q_type should be cloze_item, got {q_type}"
        assert len(opts) == 4, f"Q{so} should have 4 options, got {len(opts)}"
    elif so <= 40:
        assert pts == 2.0, f"Q{so} points should be 2.0, got {pts}"
        assert q_type == 'reading_item', f"Q{so} q_type should be reading_item, got {q_type}"
        assert len(opts) == 4, f"Q{so} should have 4 options, got {len(opts)}"
    else:
        assert pts == 2.0, f"Q{so} points should be 2.0, got {pts}"
        assert q_type == 'reading_item', f"Q{so} q_type should be reading_item, got {q_type}"
        assert len(opts) == 7, f"Q{so} should have 7 options, got {len(opts)}"

assert total_pts == 60.0, f"Total points expected 60.0, got {total_pts}"
print(f"Total score: {total_pts} (Perfect!)")
print("All 2012 ky2 local verification checks PASSED 100%!")
