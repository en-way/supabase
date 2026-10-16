import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky2):
    if "2021" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky2, f)
        break

doc = pymupdf.open(target)
print("=== 2021 ky2 Page 16 ===")
print(doc[15].get_text()[:2000])

print("=== 2021 ky2 Page 17 ===")
print(doc[16].get_text()[:2000])
