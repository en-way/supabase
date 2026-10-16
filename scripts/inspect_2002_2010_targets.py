import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def print_pdf_pages(yr, p_list):
    for f in os.listdir(pdf_base_ky1):
        if str(yr) in f and f.endswith(".pdf"):
            doc = pymupdf.open(os.path.join(pdf_base_ky1, f))
            print(f"=== {yr} ky1 ===")
            for p in p_list:
                print(f"--- Page {p+1} ---")
                print(doc[p].get_text()[:1500])

print_pdf_pages(2002, [22, 23])
print_pdf_pages(2010, [14, 15])
