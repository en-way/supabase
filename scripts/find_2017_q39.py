# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")
found_pdfs = []
for p in base_dir.rglob("*.pdf"):
    if "2017" in p.name:
        found_pdfs.append(p)

print(f"Found {len(found_pdfs)} PDFs matching 2017:")
for p in found_pdfs:
    print(f"  {p}")

for p in found_pdfs:
    doc = fitz.open(str(p))
    for i in range(len(doc)):
        t = doc[i].get_text()
        if "39." in t and "Well-enforced" in t:
            print(f"\nMatch in {p.name} P{i+1}:")
            lines = t.split("\n")
            for idx, l in enumerate(lines):
                if "39." in l or "Well-enforced" in l:
                    print("\n".join(lines[max(0, idx-2):min(len(lines), idx+15)]))
                    break
