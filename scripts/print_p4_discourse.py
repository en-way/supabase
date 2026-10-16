import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("<<<PAGE_")
p11 = pages[11].split(">>>", 1)[1]
p12 = pages[12].split(">>>", 1)[1]

lines = p11.split('\n') + p12.split('\n')
capture = False
for l in lines:
    if '语篇分析' in l:
        capture = True
    elif '真题精解' in l:
        capture = False
    if capture:
        print(l)
