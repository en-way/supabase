# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")
pdf_path = None
for p in base_dir.rglob("*.pdf"):
    if "2017" in p.name and "英语一真题解析" in str(p.parent):
        pdf_path = p
        break

print(f"Found: {pdf_path}")
doc = fitz.open(str(pdf_path))
print(f"Total pages: {len(doc)}")

for i in range(len(doc)):
    t = doc[i].get_text()
    if any(k in t for k in ["sarcastic", "tolerant", "skeptical", "supportive"]) and "40." in t:
        print(f"\n=== Page {i+1} ===")
        print(t)
    elif "39." in t and ("guarantee fair play" in t or "transparency" in t):
        print(f"\n=== Page {i+1} ===")
        print(t[:1500])
