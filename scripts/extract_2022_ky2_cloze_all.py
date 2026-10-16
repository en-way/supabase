# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")
pdf_path = [p for p in base_dir.rglob("*.pdf") if "2022" in p.name and "英语二" in str(p)][0]
doc = fitz.open(str(pdf_path))
print(f"2022 ky2 PDF: {pdf_path.name}, pages: {len(doc)}")

for i in range(10):
    t = doc[i].get_text()
    if "Section I Use of English" in t or "一、总体分析" in t or "二、试题精解" in t or any(f"{q}." in t for q in range(1, 21)):
        print(f"=== Page {i+1} ===")
        print(t)
