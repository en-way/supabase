import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

content = open('scratch_2004_decoded.txt', encoding='utf-8').read()
pages = content.split('<<<PAGE_')

print("=== Finding Reading Passages & Questions in 2004 ===")

for p in pages:
    if not p.strip(): continue
    p_num = int(p.split('>>>')[0])
    text = p.split('>>>')[1]
    
    # Check for passage start
    if any(k in text for k in ['Text 1', 'Text 2', 'Text 3', 'Text 4', 'Part A', 'Reading Comprehension']):
        for line in text.split('\n'):
            if any(k in line for k in ['Text', 'Reading', 'Part A']):
                print(f"P{p_num}: {line.strip()[:60]}")
    
    # Check for question numbers
    q_matches = re.findall(r'\n(2[1-9]|3\d|40)\.\s*([A-Za-z\u4e00-\u9fff]+)', text)
    if q_matches:
        print(f"P{p_num} Questions: {q_matches}")
