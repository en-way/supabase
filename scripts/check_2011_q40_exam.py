import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题（2001-2025）"
target = None
for f in os.listdir(pdf_base):
    if "2011" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base, f)
        break

if target:
    doc = pymupdf.open(target)
    for p in range(len(doc)):
        t = doc[p].get_text()
        if "40." in t:
            print(f"=== Exam Paper Page {p+1} ===")
            idx = t.find("40.")
            print(t[idx:idx+600])
else:
    print("Test paper PDF not found.")
