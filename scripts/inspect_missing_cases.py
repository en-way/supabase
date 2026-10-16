import fitz
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = 'c:/Users/57867/Desktop/WYJ/考研/考研英语历年真题（分题型版）/英语一真题解析（2001-2025）'

missing_cases = [
    (2001, 7), (2003, 11), (2003, 14), (2005, 6), (2005, 10), (2005, 17),
    (2006, 14), (2007, 2), (2007, 4), (2007, 17), (2008, 1), (2008, 11),
    (2009, 3), (2009, 5), (2009, 12), (2009, 18), (2010, 20), (2012, 17),
    (2012, 20), (2013, 19), (2014, 2), (2015, 18)
]

for y, q in missing_cases:
    fpath = glob.glob(f'{pdf_dir}/*{y}*.pdf')[0]
    doc = fitz.open(fpath)
    found = False
    for p in range(min(12, len(doc))):
        t = doc[p].get_text()
        # Look for "{q}." or "{q} "
        m = re.search(rf'(?:^|\n)\s*(?:&|{q})[\.、\s].*?(?:考点|思路)', t, re.DOTALL)
        if m:
            print(f"[{y} Q{q}] Found on Page {p+1}: {repr(m.group(0)[:80])}")
            found = True
            break
    if not found:
        print(f"[{y} Q{q}] NOT found with simple pattern. Searching just '{q}.'...")
        for p in range(min(12, len(doc))):
            t = doc[p].get_text()
            if f'{q}.' in t or f'{q} ' in t:
                # print lines
                for l in t.split('\n'):
                    if l.strip().startswith(f'{q}.') or l.strip().startswith(f'{q} '):
                        print(f"   Page {p+1}: {repr(l.strip()[:60])}")
