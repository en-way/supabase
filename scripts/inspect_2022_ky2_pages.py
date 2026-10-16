import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky2):
    if "2022" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky2, f)
        break

doc = pymupdf.open(target)
print("=== 2022 ky2 Pages 10-16 ===")
for p in range(9, 16):
    t = doc[p].get_text()
    for l in t.split('\n'):
        if any(l.strip().startswith(f"{q}.") for q in [21, 22, 23, 24, 25]):
            print(f"P{p+1}: {l.strip()}")
        if "精准定位" in l or "命题解密" in l:
            print(f"P{p+1} --> {l.strip()[:60]}")
