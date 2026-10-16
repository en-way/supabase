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

targets = [21, 22, 23, 24, 26, 27, 28, 29]
for p in range(9, 28):
    t = doc[p].get_text()
    for q in targets:
        if f"{q}." in t and any(k in t for k in ["【精准定位】", "［精准定位］", "【命题解密】", "［命题解密］"]):
            print(f"=== 2022 ky2 Q{q} on Page {p+1} ===")
            idx = t.find(f"{q}.")
            print(t[idx:idx+1200])
            print("="*40)
