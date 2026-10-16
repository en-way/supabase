import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Cloze is on pages 1 to 15
cloze_section = text.split("<<<PAGE_15>>>")[0]

# Search for question patterns like \n1. [A] or \n1. 或 18 
# In our cipher: 1. is 1. (since :8 decoded to 1.)
matches = list(re.finditer(r'(?:^|\n)\s*(\d{1,2})\.\s*([A-D]|A|B|C|D|\[A\]|本题考核)', cloze_section))
print(f"Found matches: {len(matches)}")

for q in range(1, 21):
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*.*?(?=(?:\n\s*{q+1}\.\s*|<<<PAGE_15>>>|\Z))', cloze_section, re.DOTALL)
    if m:
        block = m.group(0).strip()
        lines = [l.strip() for l in block.split('\n') if l.strip()]
        header = lines[0] if lines else ''
        opts_line = lines[1] if len(lines) > 1 else ''
        kdtl = [l for l in lines if '本题考核' in l or '本题考查' in l]
        ans = [l for l in lines if '因此选' in l or '正确答案' in l or '为正确' in l or '正确选项' in l]
        print(f"Q{q:2d}: {header[:40]} | {opts_line[:50]} | ans: {ans[:1]}")
    else:
        print(f"Q{q:2d}: NOT FOUND")
