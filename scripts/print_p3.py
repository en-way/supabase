import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("<<<PAGE_")
p7_lines = pages[7].split(">>>", 1)[1].split('\n')
for i in range(15, 35):
    print(f"{i}: {p7_lines[i]}")
