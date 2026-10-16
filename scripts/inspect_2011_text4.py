import pymupdf
import json
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
# Search for Q39 and Q40
for p in range(len(doc)):
    t = doc[p].get_text()
    if "39." in t or "40." in t:
        print(f"=== Page {p+1} ===")
        for l in t.split('\n'):
            if any(l.strip().startswith(f"{i}.") for i in [36, 37, 38, 39, 40]):
                print(l.strip())
