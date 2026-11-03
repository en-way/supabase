# -*- coding: utf-8 -*-
import fitz
from rapidocr_onnxruntime import RapidOCR

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2014年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

# Pages with text overview and语篇分析 for Text 1, 2, 3, 4, Part B
reading_pages = [
    (15, 16, "Text 1"),
    (22, 23, "Text 2"),
    (29, 30, "Text 3"),
    (37, 38, "Text 4"),
    (45, 46, 47, "Part B")
]

with open("scripts/ky2_reading_passages_raw.txt", "w", encoding="utf-8") as out:
    for item in reading_pages:
        title = item[-1]
        pages = item[:-1]
        out.write(f"\n{'='*40} {title} {'='*40}\n")
        print(f"Extracting {title} (Pages {pages})...", flush=True)
        for p in pages:
            pix = doc[p-1].get_pixmap(dpi=120)
            res, _ = ocr(pix.tobytes('png'))
            if not res: continue
            text = '\n'.join([r[1] for r in res])
            out.write(f"\n--- Page {p} ---\n")
            out.write(text + "\n")

print("Saved reading passages raw text.")
