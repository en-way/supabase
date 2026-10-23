# -*- coding: utf-8 -*-
"""
verify_2013_ky1_local.py
Rigorous forensic validation for 2013 ky1 exam local JSON
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Local Verification for 2013 ky1 Exam ===")

json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json'
assert os.path.exists(json_path), f"File not found: {json_path}"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Exam Metadata Check
exam = data.get("exam", {})
title = exam.get("title") or data.get("title")
assert title == "2013年全国硕士研究生入学统一考试英语（一）真题", f"Invalid title: {title}"
year = exam.get("year") or data.get("year")
assert year == 2013, f"Invalid year: {year}"
cat = exam.get("category_id") or data.get("category_id")
assert cat == "ky1", f"Invalid category: {cat}"
total_score = exam.get("total_score") or data.get("total_score")
assert total_score == 60.0, f"Invalid total score: {total_score}"
print("[PASS] 1. Exam metadata verified successfully.")

# 2. Passages Check
passages = data.get("passages", [])
assert len(passages) == 6, f"Expected 6 passages, got {len(passages)}"

expected_paras = [4, 6, 7, 7, 7, 8] # Part B has 7 text paras + 1 options block = 8 blocks
for idx, p in enumerate(passages):
    pid = p.get("id")
    sec = p.get("section_type")
    content = p.get("content", "")
    paras = [para for para in content.split("\n\n") if para.strip()]
    print(f"Passage {idx} ({sec}, id={pid}): {len(content)} chars, {len(paras)} paragraphs")
    assert len(paras) >= expected_paras[idx], f"Passage {idx} has {len(paras)} paras, expected at least {expected_paras[idx]}"
    
    # Forensic anti-pollution assertions
    if idx == 1: # Text 1
        assert "The victims of this revolution, of course, are not limited to designers" in content, "Text 1 Para 3 missing"
        assert "Overdressed is the fashion world's answer" in content, "Text 1 Para 4 missing"
        assert "better clothes is good for both the planet and their wallets" not in content, "Text 1 contains external junk"
    elif idx == 2: # Text 2
        assert "It is suggested in Paragraph 1" not in content, "Text 2 contains stem pollution"
        assert "hoirified" not in content, "Text 2 contains OCR error hoirified"
        assert "Microsoffs" not in content, "Text 2 contains OCR error Microsoffs"
    elif idx == 3: # Text 3
        assert "the past holds the key to the future" in content, "Text 3 missing Para 6"
        assert "This long perspective makes the pessimistic view of our prospects" in content, "Text 3 missing Para 7"
    elif idx == 4: # Text 4
        assert "to holds the key to" not in content, "Text 4 contains Text 3 inverted fragment"
        assert "In Arizona v. United States" in content, "Text 4 Para 2 corrupted"
        assert "Two of the three objecting Justices—" in content, "Text 4 Para 5 missing header"
    elif idx == 5: # Part B
        assert "[A] The idea is to force social scientists" in content, "Part B missing option [A]"
        assert "[B] The solution is to change the mindset" in content, "Part B missing option [B]"
        assert "[41] ____________" in content and "[45] ____________" in content, "Part B gaps missing"

print("[PASS] 2. All 6 Passages verified with forensic anti-pollution integrity.")

# 3. Questions Check
questions = data.get("questions", [])
assert len(questions) == 45, f"Expected 45 questions, got {len(questions)}"

official_answers = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'B',
    6: 'D', 7: 'A', 8: 'A', 9: 'D', 10: 'C',
    11: 'A', 12: 'C', 13: 'B', 14: 'C', 15: 'B',
    16: 'C', 17: 'D', 18: 'D', 19: 'B', 20: 'A',
    21: 'A', 22: 'B', 23: 'D', 24: 'C', 25: 'C',
    26: 'D', 27: 'A', 28: 'C', 29: 'B', 30: 'D',
    31: 'B', 32: 'A', 33: 'D', 34: 'B', 35: 'A',
    36: 'B', 37: 'C', 38: 'A', 39: 'C', 40: 'D',
    41: 'E', 42: 'F', 43: 'D', 44: 'G', 45: 'A'
}

calc_score = 0.0
for q in questions:
    qno = q.get("question_number")
    so = q.get("sort_order")
    assert qno == so, f"Question number {qno} != sort order {so}"
    assert isinstance(qno, int) and 1 <= qno <= 45, f"Invalid question number: {qno}"
    
    ca = q.get("correct_answer")
    ans = q.get("answer")
    assert ca == ans == official_answers[qno], f"Q{qno}: Answer mismatch! Got {ca}/{ans}, expected {official_answers[qno]}"
    
    opts = q.get("options", [])
    assert isinstance(opts, list) and len(opts) in (4, 7), f"Q{qno}: Invalid options length: {len(opts)}"
    opt_keys = [item["key"] for item in opts]
    assert ca in opt_keys, f"Q{qno}: Correct answer {ca} not in option keys {opt_keys}"
    
    pts = q.get("points")
    qt = q.get("q_type")
    if qno <= 20:
        assert pts == 0.5, f"Q{qno}: Cloze question point must be 0.5, got {pts}"
        assert qt == "cloze_item", f"Q{qno}: Expected cloze_item, got {qt}"
    else:
        assert pts == 2.0, f"Q{qno}: Reading question point must be 2.0, got {pts}"
        assert qt == "reading_item", f"Q{qno}: Expected reading_item, got {qt}"
    calc_score += pts
    
    expl = q.get("explanation", "")
    assert len(expl) >= 180, f"Q{qno}: Explanation too short ({len(expl)})"
    assert '\ufffd' not in expl, f"Q{qno}: Explanation contains replacement char"

assert abs(calc_score - 60.0) < 1e-5, f"Calculated total score {calc_score} != 60.0"
print(f"[PASS] 3. All 45 Questions verified: 100% answer match, valid types, points sum to {calc_score}.")

print("=== ALL LOCAL VERIFICATION CHECKS PASSED SUCCESSFULLY (100%) ===")
