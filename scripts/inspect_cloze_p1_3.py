import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("<<<PAGE_")
for p in pages[1:4]:
    pnum = p.split(">>>")[0]
    pcontent = p.split(">>>", 1)[1]
    print(f"=== PAGE {pnum} ===")
    print(pcontent[:2000])
