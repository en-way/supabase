import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base):
    if "2011" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base, f)
        break

doc = pymupdf.open(target)
for p in range(len(doc)):
    t = doc[p].get_text()
    if "hardly" in t or "opposite" in t:
        print(f"Page {p+1}:")
        if "hardly" in t:
            print("  FOUND 'hardly'")
        if "opposite" in t:
            print("  FOUND 'opposite'")
