# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/2020_ky2_full_book.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

# Remove === Page \d+ === markers
clean_text = re.sub(r'=== Page \d+ ===\n?', '', raw)

# Check each question
for q in range(1, 46):
    # Pattern to find start of question q
    # In Cloze: q.[A] or q. [A]
    # In Reading: q. Stem...
    # In Part B: q. [答案] or 41. ...
    if q <= 20:
        pat = rf'(?:^|\n){q}\.\s*\[A\]([\s\S]*?)(?=(?:^|\n){q+1}\.\s*\[A\]|Section II|\Z)'
    elif q <= 40:
        pat = rf'(?:^|\n){q}\.([\s\S]*?)(?=(?:^|\n){q+1}\.|\nText|\nPart B|\Z)'
    else:
        pat = rf'(?:^|\n){q}\.([\s\S]*?)(?=(?:^|\n){q+1}\.|\nSection|\Z)'
    
    m = re.search(pat, clean_text)
    if m:
        block = m.group(0)
        # Find correct answer
        # Look for [A-G] followed by 正确 / 符合 / 契合 or [答案]
        ans = None
        ans_m1 = re.findall(r'(?:\[答案\]|【答案】|［答案］)\s*([A-G])', block)
        if ans_m1:
            ans = ans_m1[0]
        else:
            ans_m2 = re.findall(r'\[([A-G])\](?:正确|为正确|为本题正确|最贴合|符合|契合)', block)
            if ans_m2:
                ans = ans_m2[-1]
            else:
                ans_m3 = re.findall(r'(?:选|为|应选)\s*\[([A-G])\]', block)
                if ans_m3:
                    ans = ans_m3[-1]
        print(f"Q{q:02d}: ans={ans} | len={len(block)} | preview={block[:60].strip()}")
    else:
        print(f"Q{q:02d}: NOT FOUND")
