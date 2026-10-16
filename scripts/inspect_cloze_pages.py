import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open("scratch_2004_decoded.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect the first 15 pages in scratch_2004_decoded.txt
pages = text.split("<<<PAGE_")
for p in pages[1:10]:
    page_num = p.split(">>>")[0]
    content = p.split(">>>", 1)[1]
    print(f"=== PAGE {page_num} ===")
    print(content[:800])
