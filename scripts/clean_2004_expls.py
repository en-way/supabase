import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

cloze_section = text.split("<<<PAGE_15>>>")[0]

for q in range(1, 21):
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*(.*?)(?=(?:\n\s*{q+1}\.\s*|<<<PAGE_15>>>|\Z))', cloze_section, re.DOTALL)
    if m:
        content = m.group(1).strip()
        # Clean up cipher artifacts in explanations
        # eAo -> [A], eBo -> [B], eCo -> [C], eDo -> [D]
        content = re.sub(r'e([A-D])o', r'[\1]', content)
        content = re.sub(r'e([A-D])', r'[\1]', content)
        content = content.replace('M精准定位s', '【精准定位】').replace('M精准定位', '【精准定位】')
        content = content.replace('M空格设置s', '【空格设置】').replace('M空格设置', '【空格设置】')
        content = content.replace('M干扰设置s', '【干扰项设置】').replace('M干扰项设置', '【干扰项设置】')
        content = content.replace('M干扰项设置s', '【干扰项设置】')
        content = content.replace('本题考核的知识点是c', '【考点提炼】').replace('本题考核的知识点是c', '【考点提炼】')
        lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('<<<PAGE')]
        print(f"=== 2004 Q{q} ({len(lines)} lines) ===")
        print('\n'.join(lines[:6]))
