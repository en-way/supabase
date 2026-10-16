import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky1):
    if "2009" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky1, f)
        break

doc = pymupdf.open(target)
for p in range(47, 53):
    t = doc[p].get_text()
    for l in t.split('\n'):
        if any(l.strip().startswith(f"{q}.") for q in [41, 42, 43, 44, 45]):
            print(f"P{p+1}: {l.strip()}")
        if "答案" in l or "精准定位" in l:
            print(f"P{p+1} --> {l.strip()[:60]}")
