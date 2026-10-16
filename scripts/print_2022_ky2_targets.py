# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")
pdf_path = None
for p in base_dir.rglob("*.pdf"):
    if "2022" in p.name and "英语二" in str(p):
        pdf_path = p
        break

doc = fitz.open(str(pdf_path))
print(f"2022 ky2 PDF: {pdf_path.name}, pages: {len(doc)}")

targets = [32, 38, 40]
for i in range(len(doc)):
    t = doc[i].get_text()
    for q in targets:
        if f"{q}." in t and ("精解" in t or "正确率" in t or "【考点" in t or "［精准定位］" in t or "【命题解密】" in t or "［命题解密］" in t):
            print(f"=== Page {i+1} for Q{q} ===")
            lines = t.split("\n")
            for idx, l in enumerate(lines):
                if f"{q}." in l and not "Page" in l:
                    print("\n".join(lines[idx:idx+15]))
                    print("-" * 40)
                    break
