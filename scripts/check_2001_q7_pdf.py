import pymupdf
import pathlib
import sys

sys.stdout.reconfigure(encoding='utf-8')

root = pathlib.Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）")

# Find 2001 ky1 pdf
p2001 = None
for p in root.rglob("*.pdf"):
    if "2001" in p.name and ("英语一" in p.parent.name or "2001-2025" in p.parent.name or "2001" in p.name):
        print(f"Candidate: {p}")
        if "2001" in p.name:
            p2001 = p

# Let's open the 2001 PDF in 英语一
for p in root.rglob("*2001*.pdf"):
    print("Found:", p)
    doc = pymupdf.open(p)
    for idx, page in enumerate(doc):
        text = page.get_text()
        if 'agreed' in text or 'sided' in text or 'Lord Irvine' in text:
            print(f"\n--- Page {idx+1} in {p.name} ---")
            lines = [l.strip() for l in text.splitlines() if l.strip()]
            for i, line in enumerate(lines):
                if any(k in line for k in ['agreed', 'sided', 'shared', 'complied', '7.']):
                    s = max(0, i-3)
                    e = min(len(lines), i+5)
                    print('\n'.join(lines[s:e]))
                    print('='*30)
