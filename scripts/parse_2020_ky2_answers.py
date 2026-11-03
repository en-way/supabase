# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/2020_ky2_full_book.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect each question block
answers = {}

# Cloze 1-20
# In cloze, each question 1-20 has [考点提炼] or [解题思路] where the correct option is stated, e.g. [D]正确 or [B]符合文意
for q in range(1, 21):
    # Pattern around q. [A]...
    m = re.search(rf'(?:^|\n){q}\.[\s\S]*?(?=(?:^|\n){q+1}\.|\n=== Page|\Z)', text)
    if m:
        block = m.group(0)
        # Search for [A-D] followed by 正确 / 符合 / 契合
        ans_m = re.findall(r'\[([A-D])\](?:正确|为正确|为本题正确|符合|契合|符合文意)', block)
        if ans_m:
            answers[q] = ans_m[-1]
        else:
            answers[q] = None
    else:
        answers[q] = None

# Reading 21-40
for q in range(21, 41):
    m = re.search(rf'(?:^|\n){q}\.[\s\S]*?(?=(?:^|\n){q+1}\.|\n=== Page|\Z)', text)
    if m:
        block = m.group(0)
        ans_m = re.findall(r'\[([A-D])\](?:正确|为正确|为本题正确|最贴合|符合|契合)', block)
        if ans_m:
            answers[q] = ans_m[-1]
        else:
            answers[q] = None
    else:
        answers[q] = None

# Part B 41-45
for q in range(41, 46):
    m = re.search(rf'(?:^|\n){q}\.[\s\S]*?(?=(?:^|\n){q+1}\.|\n=== Page|\Z)', text)
    if m:
        block = m.group(0)
        ans_m = re.findall(r'(?:\[答案\]|【答案】|［答案］)\s*([A-G])', block)
        if ans_m:
            answers[q] = ans_m[0]
        else:
            ans_m2 = re.findall(r'\[([A-G])\](?:正确|为正确|符合|契合)', block)
            if ans_m2:
                answers[q] = ans_m2[-1]
            else:
                answers[q] = None
    else:
        answers[q] = None

print("=== Extracted Answers ===")
for q in range(1, 46):
    print(f"Q{q:02d}: {answers.get(q)}")
