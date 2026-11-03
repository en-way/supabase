# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2020年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

sections = {
    "Cloze Questions (Q1-20)": list(range(4, 10)),
    "Text 1 Questions (Q21-25)": list(range(12, 19)),
    "Text 2 Questions (Q26-30)": list(range(21, 28)),
    "Text 3 Questions (Q31-35)": list(range(30, 38)),
    "Text 4 Questions (Q36-40)": list(range(40, 47)),
    "Part B Questions (Q41-45)": list(range(48, 54)),
}

with open("scripts/2020_ky2_questions_raw.txt", "w", encoding="utf-8") as out:
    for name, pages in sections.items():
        out.write(f"\n==================== {name} ====================\n")
        print(f"Extracting {name} (pages {pages})...", flush=True)
        for p in pages:
            pix = doc[p-1].get_pixmap(dpi=150)
            res, _ = ocr(pix.tobytes('png'))
            if res:
                out.write(f"\n--- Page {p} ---\n")
                text = '\n'.join([r[1] for r in res])
                out.write(text + "\n")

print("Questions extraction complete.", flush=True)
