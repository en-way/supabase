# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")
pdf_path = None
for p in base_dir.rglob("*.pdf"):
    if "2006" in p.name and "英语一真题解析" in str(p.parent):
        pdf_path = p
        break

doc = fitz.open(str(pdf_path))
print(f"2006 PDF: {pdf_path}")
for i in range(len(doc)):
    t = doc[i].get_text()
    if "20." in t and any(k in t for k in ["supervision", "addicted", "resistant"]):
        print(f"=== Page {i+1} ===")
        print(t[:800])
