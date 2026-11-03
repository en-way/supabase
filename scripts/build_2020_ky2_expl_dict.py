# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/2020_ky2_full_book.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect explanations for each question
expl_dict = {}

# Cloze 1-20
for q in range(1, 21):
    m = re.search(rf'(?:^|\n){q}\.\s*\[A\][\s\S]*?(?=(?:^|\n)\d{{1,2}}\.\s*\[A\]|\n=== Page|\Z)', text)
    if m:
        block = m.group(0)
        # Find explanation part after options
        lines = block.splitlines()
        expl_lines = []
        capture = False
        for l in lines:
            if any(k in l for k in ['[考点提炼]', '［考点提炼］', '[解题思路]', '［解题思路］']):
                capture = True
            if capture:
                expl_lines.append(l)
        expl_dict[q] = '\n'.join(expl_lines).strip()
    else:
        expl_dict[q] = ""

print(f"Cloze expls captured: {len([q for q in range(1, 21) if expl_dict[q]])}/20")
for q in range(1, 5):
    print(f"Q{q} expl length: {len(expl_dict[q])}, snippet: {repr(expl_dict[q][:60])}")
