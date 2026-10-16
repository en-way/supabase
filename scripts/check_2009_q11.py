import pymupdf
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base):
    if "2009" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base, f)
        break

doc = pymupdf.open(target)
# Q11 on pages 1-6
for p in range(len(doc)):
    t = doc[p].get_text()
    if "11." in t and "costs" in t:
        print(f"=== Page {p+1} ===")
        idx = t.find("11.")
        print(t[idx:idx+800])
        break
