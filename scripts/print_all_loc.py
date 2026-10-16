import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

cloze_text = text.split("<<<PAGE_15>>>")[0]

for q in range(1, 21):
    next_q = q + 1 if q < 20 else 21
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*(.*?)(?=(?:\n\s*{next_q}\.\s*|<<<PAGE_15>>>|\Z))', cloze_text, re.DOTALL)
    if m:
        block = m.group(1)
        # extract lines after 精准定位 until 空格设置
        m_loc = re.search(r'精准定位.*?(?=空格设置|干扰设置|$)', block, re.DOTALL)
        loc_text = m_loc.group(0).strip() if m_loc else "NOT FOUND"
        print(f"=== Q{q} ===")
        print(loc_text.replace('\n', ' ')[:250])
