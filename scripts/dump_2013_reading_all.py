# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2001-2025阅读真题\【大间距】-英语二 （2010-2024）.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

out_file = r'scripts/2013_ky2_reading_exam_raw.txt'
with open(out_file, 'w', encoding='utf-8') as out:
    for p in range(52, 69):
        pix = doc[p].get_pixmap(dpi=110)
        res, _ = ocr(pix.tobytes('png'))
        txt = '\n'.join([r[1] for r in res]) if res else ''
        print(f"Page {p+1} extracted ({len(txt)} chars)", flush=True)
        out.write(f"\n\n=== PAGE {p+1} ===\n\n" + txt)

print("Finished dumping 2013 reading pages 53 to 69!", flush=True)
