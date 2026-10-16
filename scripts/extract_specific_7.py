import glob
import fitz
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语一真题解析（2001-2025）'

targets = [
    (2006, 5), (2006, 20),
    (2008, 1), (2008, 5), (2008, 19), (2008, 20),
    (2009, 19)
]

for y, q in targets:
    fpath = glob.glob(f'{pdf_dir}/*{y}*.pdf')[0]
    doc = fitz.open(fpath)
    print(f"=== {y} Q{q} ===")
    found = False
    for p in range(min(10, len(doc))):
        t = doc[p].get_text()
        # Look for "{q}." or "{q} "
        m = re.search(rf'(?:^|\n)\s*(?:&|{q})\.\s*.*?(?:考点|思路)', t, re.DOTALL)
        if m:
            start = m.start()
            print(f"Found on Page {p+1}:")
            print(t[start:start+600])
            found = True
            break
    if not found:
        print(f"Not matched by regex on {y} Q{q}")
