import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

cloze_text = text.split("<<<PAGE_15>>>")[0]

for q in range(1, 21):
    next_q = q + 1 if q < 20 else 21
    pattern = rf'(?:^|\n)\s*{q}\.\s*(.*?)(?=(?:\n\s*{next_q}\.\s*|<<<PAGE_15>>>|\Z))'
    m = re.search(pattern, cloze_text, re.DOTALL)
    if m:
        block = m.group(1)
        # Search for answer patterns: e.g., "所以eAoor正确", "所以选eDo", "所以eCocenteringtonh正确", "为正确选项"
        # Let's search for mentions of [A], [B], [C], [D] near 正确 or 选 or 为正确选项
        ans_match = re.findall(r'(?:选|所以|只有|项为)\s*e([A-D])|e([A-D])[a-zA-Z\s\(\)]*(?:正确|为正确选项)', block)
        print(f"Q{q}: matches: {ans_match}")
