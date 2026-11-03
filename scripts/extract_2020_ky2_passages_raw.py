# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2020年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

sections = {
    "Cloze": [1, 2, 3],
    "Text 1": [11, 12],
    "Text 2": [19, 20],
    "Text 3": [28, 29],
    "Text 4": [38, 39, 40],
    "Part B": [46, 47, 48]
}

with open("scripts/2020_ky2_passages_raw.txt", "w", encoding="utf-8") as out:
    for name, pages in sections.items():
        out.write(f"\n==================== {name} ====================\n")
        print(f"Extracting {name} (pages {pages})...")
        for p in pages:
            pix = doc[p-1].get_pixmap(dpi=150)
            res, _ = ocr(pix.tobytes('png'))
            if res:
                out.write(f"\n--- Page {p} ---\n")
                text = '\n'.join([r[1] for r in res])
                out.write(text + "\n")

print("Passage extraction complete.")
