import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'9\.\s*eAoaffect.*?(?=10\.)', text, re.DOTALL)
if m:
    print(m.group(0))
