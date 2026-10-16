import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_pdf(yr, cat):
    base = pdf_base_ky1 if cat == 'ky1' else pdf_base_ky2
    for f in os.listdir(base):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(base, f))
    return None

# 1. 2021 ky2 Q21-25
doc_21_2 = get_pdf(2021, 'ky2')
print("=== 2021 ky2 Q21 ===")
print(doc_21_2[10].get_text()[:1200])

print("=== 2021 ky2 Q23 ===")
print(doc_21_2[13].get_text()[:1200])

print("=== 2021 ky2 Q24 ===")
print(doc_21_2[14].get_text()[:1200])

print("=== 2021 ky2 Q25 ===")
print(doc_21_2[16].get_text()[:1200])
