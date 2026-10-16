import pymupdf
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def search_q(year, keyword):
    for f in os.listdir(pdf_base):
        if year in f and f.endswith(".pdf"):
            doc = pymupdf.open(os.path.join(pdf_base, f))
            print(f"=== Searching {year} for {keyword} ({len(doc)} pages) ===")
            for p in range(len(doc)):
                t = doc[p].get_text()
                if keyword in t:
                    print(f"Found on page {p+1}:")
                    idx = t.find(keyword)
                    print(t[max(0, idx-100):idx+1200])
                    print("="*40)
                    return

search_q("2010", "Business-method patents")
search_q("2012", "Donahue")
