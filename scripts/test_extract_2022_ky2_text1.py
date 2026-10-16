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

for q, p in [(21, 10), (22, 12), (23, 13), (24, 15)]:
    t = doc[p].get_text()
    print(f"=== 2022 ky2 Q{q} on Page {p+1} ===")
    idx = t.find(f"{q}.")
    print(t[idx:idx+1400])
    print("="*40)
