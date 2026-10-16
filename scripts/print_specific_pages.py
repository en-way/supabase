import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def get_text_pages(yr, p_start, p_end):
    for f in os.listdir(pdf_base_ky1):
        if str(yr) in f and f.endswith(".pdf"):
            doc = pymupdf.open(os.path.join(pdf_base_ky1, f))
            return "\n".join([f"=== Page {p+1} ===\n" + doc[p].get_text() for p in range(p_start-1, min(p_end, len(doc)))])
    return ""

print("--- 2017 ky1 Pages 45-47 ---")
print(get_text_pages(2017, 45, 47)[:3000])

print("--- 2016 ky1 Pages 57-58 ---")
print(get_text_pages(2016, 57, 58)[:3000])
