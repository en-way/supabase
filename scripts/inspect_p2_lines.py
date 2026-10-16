import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("<<<PAGE_")
p5 = pages[5].split(">>>", 1)[1]
for i, l in enumerate(p5.split('\n')):
    if any(k in l for k in ['theories', 'delinquency', 'families', 'wealthy', 'criticism', 'tentative']):
        print(f"{i}: {l}")
