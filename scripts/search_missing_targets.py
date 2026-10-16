import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def find_in_pdf(yr, keyword):
    for f in os.listdir(pdf_base_ky1):
        if str(yr) in f and f.endswith(".pdf"):
            doc = pymupdf.open(os.path.join(pdf_base_ky1, f))
            print(f"=== Searching {yr} for '{keyword}' ({len(doc)} pages) ===")
            for p in range(len(doc)):
                t = doc[p].get_text()
                if keyword in t:
                    print(f"Found on page {p+1}:")
                    idx = t.find(keyword)
                    print(t[max(0, idx-80):idx+400])
                    print("-" * 40)
                    return

find_in_pdf(2017, "public officials")
find_in_pdf(2009, "文化传播")
find_in_pdf(2002, "abnormalities")
