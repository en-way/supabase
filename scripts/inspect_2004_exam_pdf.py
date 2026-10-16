import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题（2001-2025）"
target_file = None
for f in os.listdir(pdf_dir):
    if "2004" in f and f.endswith(".pdf"):
        target_file = os.path.join(pdf_dir, f)
        break

print(f"Found target: {target_file}")
if target_file:
    doc = pymupdf.open(target_file)
    print(f"Page count: {len(doc)}")
    for i in range(min(3, len(doc))):
        print(f"=== PAGE {i+1} ===")
        print(doc[i].get_text()[:800])
