import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("<<<PAGE_")
p11 = pages[11].split(">>>", 1)[1]
p12 = pages[12].split(">>>", 1)[1]

for p in [p11, p12]:
    for l in p.split('\n'):
        if '语篇分析' in l or '第四段' in l or '第五段' in l:
            print(l)
