import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def get_doc(yr):
    for f in os.listdir(pdf_base_ky1):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(pdf_base_ky1, f))
    return None

doc16 = get_doc(2016)
print("=== 2016 ky1 Page 57 ===")
print(doc16[56].get_text())
print("=== 2016 ky1 Page 58 ===")
print(doc16[57].get_text())
