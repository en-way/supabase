# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")
pdf_path = [p for p in base_dir.rglob("*.pdf") if "2022" in p.name and "英语二" in str(p)][0]
doc = fitz.open(str(pdf_path))
print(f"2022 ky2 PDF: {pdf_path.name}")

with open("scripts/2022_ky2_cloze_raw.txt", "w", encoding="utf-8") as out:
    for i in range(8):
        out.write(f"\n==================== Page {i+1} ====================\n")
        out.write(doc[i].get_text())

print("Saved 2022 ky2 Cloze pages 1-8 to scripts/2022_ky2_cloze_raw.txt")
