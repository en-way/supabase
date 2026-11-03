# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2001-2025阅读真题\【大间距】-英语二 （2010-2024）.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

with open("scripts/2020_ky2_clean_reading.txt", "w", encoding="utf-8") as out:
    for p in range(164, 181): # 0-indexed 164 is Page 165
        print(f"OCR Page {p+1}...", flush=True)
        pix = doc[p].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes('png'))
        if res:
            out.write(f"\n==================== Page {p+1} ====================\n")
            for box, txt, score in res:
                out.write(f"{txt}\n")

print("Clean reading extracted successfully!", flush=True)
