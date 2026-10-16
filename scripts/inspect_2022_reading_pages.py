import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky1):
    if "2022" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky1, f)
        break

doc = pymupdf.open(target)
pages_to_check = [24, 25, 33, 34, 42, 43, 44, 45, 49, 50]
for p in pages_to_check:
    print(f"=== Page {p+1} ===")
    t = doc[p].get_text()
    for l in t.split('\n'):
        if any(l.strip().startswith(f"{q}.") for q in [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]):
            print(f"  {l.strip()}")
        if "精准定位" in l or "第一步" in l or "试题精解" in l:
            print(f"  --> {l.strip()[:80]}")
