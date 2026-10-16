import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("<<<PAGE_")

print("=== PAGE 5 bottom to PAGE 6 top ===")
p5 = pages[5].split(">>>", 1)[1]
print(p5[-1200:])
p6 = pages[6].split(">>>", 1)[1]
print(p6[:1200])

print("=== PAGE 7 bottom to PAGE 8 top ===")
p7 = pages[7].split(">>>", 1)[1]
print(p7[-1200:])
p8 = pages[8].split(">>>", 1)[1]
print(p8[:1200])
