import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky1):
    if "2017" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky1, f)
        break

doc = pymupdf.open(target)
print("=== 2017 Page 45 ===")
print(doc[44].get_text()[:2500])
