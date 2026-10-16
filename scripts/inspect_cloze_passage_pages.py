import sys

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

pages = text.split("<<<PAGE_")
target_pages = [1, 6, 8, 10, 11]

for pnum in target_pages:
    pcontent = pages[pnum].split(">>>", 1)[1]
    print(f"==================== PAGE {pnum} ====================")
    lines = pcontent.split('\n')
    print('\n'.join(lines[:45]))
