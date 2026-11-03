# -*- coding: utf-8 -*-
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\A16pro\Aing\antigravity\supabase\scripts\2020_ky1_dump.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Replace fonts anomalies
text = re.sub(r'---\s*PAGE\s*\d+\s*---', '', text)
text = re.sub(r'(?:^|\n)\s*&\s*\[A\]', '\n8. [A]', text)
text = re.sub(r'(?:^|\n)\s*11\.\s*EA\]', '\n11. [A]', text)
text = re.sub(r'(?:^|\n)\s*1&\s*［A］', '\n18. ［A］', text)
text = re.sub(r'21\s*・\s*Cooper and her colleagues argue that a 41 town of\s*culture" award could\s*・',
              '21. Cooper and her colleagues argue that a "town of culture" award could _______.', text)
text = re.sub(r'2&\s*How does', '28. How does', text)
text = re.sub(r'36\.\s*The French Senate has passed a hill to\s*・',
              '36. The French Senate has passed a bill to _______.', text)

# Test Q21 to Q40
reading_blocks = {}
for q in range(21, 41):
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*([A-Z].*?)(?=(?:^|\n)\s*(?:{q+1}\.|\bText\s+\d|\bPart\s+B|•词汇注释|三、语篇分析|•语篇分析|$))', text, re.DOTALL)
    if m:
        block = m.group(0).strip()
        reading_blocks[q] = block
        # Find explanation start: [精准定位] or [命题解密] or ［精准定位］ or ［命题解密］
        expl_idx = -1
        for kw in ['［精准定位］', '[精准定位]', '［命题解密］', '[命题解密]']:
            pos = block.find(kw)
            if pos != -1 and (expl_idx == -1 or pos < expl_idx):
                expl_idx = pos
        expl = block[expl_idx:].strip() if expl_idx != -1 else ""
        print(f"Reading Q{q}: block_len={len(block)}, expl_len={len(expl)}")
    else:
        print(f"Reading Q{q}: NOT FOUND")

# Test Part B Q41-Q45
partb_blocks = {}
for q in range(41, 46):
    m = re.search(rf'{q}\.\s*［答案］([A-G])\s*［精解］(.*?)(?=(?:\d+\.\s*［答案］|$))', text, re.DOTALL)
    if m:
        ans = m.group(1)
        expl = m.group(2).strip()
        partb_blocks[q] = (ans, expl)
        print(f"Part B Q{q}: ans={ans}, expl_len={len(expl)}")
    else:
        print(f"Part B Q{q}: NOT FOUND")
