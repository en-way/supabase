import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("<<<PAGE_")
p10_lines = pages[10].split(">>>", 1)[1].split('\n')
for i in range(15, 45):
    print(f"{i}: {p10_lines[i]}")
