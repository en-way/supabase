# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2010-2025新题型真题\【新题型】-英语二 （2010-2024年）.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

out_file = r'scripts/2013_ky2_partb_exam_raw.txt'
with open(out_file, 'w', encoding='utf-8') as out:
    for p in range(6, 10):
        pix = doc[p].get_pixmap(dpi=110)
        res, _ = ocr(pix.tobytes('png'))
        txt = '\n'.join([r[1] for r in res]) if res else ''
        print(f"Part B Page {p+1} extracted ({len(txt)} chars)", flush=True)
        out.write(f"\n\n=== PAGE {p+1} ===\n\n" + txt)

print("Finished dumping Part B pages 7 to 10!", flush=True)
