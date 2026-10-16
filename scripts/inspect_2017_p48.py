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

doc = fitz.open(str(pdf_path))
print("=== Page 48 ===")
print(doc[47].get_text())
