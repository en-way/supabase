# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")
pdf_path = None
for p in base_dir.rglob("*.pdf"):
    if "2010" in p.name and "英语一真题解析" in str(p.parent):
        pdf_path = p
        break

doc = fitz.open(str(pdf_path))
print(f"2010 PDF: {pdf_path.name}, pages: {len(doc)}")

for i in range(len(doc)):
    t = doc[i].get_text()
    if "27." in t and "Bilski" in t:
        print(f"=== Page {i+1} for Q27 ===")
        lines = t.split("\n")
        for idx, l in enumerate(lines):
            if "27." in l and not "Page" in l:
                print("\n".join(lines[idx:idx+15]))
                print("-" * 40)
                break
