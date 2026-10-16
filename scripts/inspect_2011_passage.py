import pymupdf
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# DB passage
with open("public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json", "r", encoding="utf-8") as f:
    d = json.load(f)

print("=== 2011 DB Passage ===")
print(d['passages'][0]['content'])

# PDF passage (page 1)
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base):
    if "2011" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base, f)
        break

doc = pymupdf.open(target)
print("\n=== 2011 PDF Passage (Page 1) ===")
print(doc[0].get_text()[:1500])
