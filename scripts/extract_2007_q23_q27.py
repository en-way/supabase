import re

with open('scripts/full_text_2007.txt', 'r', encoding='utf-8') as f:
    t2007 = f.read()

for q in [23, 27]:
    print(f"\n================ 2007 Q{q} ================")
    matches = re.findall(rf'{q}\.\s+.*?(?=(?:\n\d+\.|\n===|\Z))', t2007, re.DOTALL)
    for m in matches[:3]:
        print(m[:800])
        print('-'*50)
