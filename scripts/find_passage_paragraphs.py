import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect pages 1 to 14 where cloze text appears
pages = text.split("<<<PAGE_")
for i in range(1, 15):
    p = pages[i]
    pnum = p.split(">>>")[0]
    pcontent = p.split(">>>", 1)[1]
    # Check if there is an article paragraph at the top of the page
    # In HuangPiShu, each paragraph appears at the beginning of its analysis section
    print(f"--- PAGE {pnum} Header ---")
    lines = [l.strip() for l in pcontent.split('\n') if l.strip()]
    for l in lines[:15]:
        print("  ", l[:100])
