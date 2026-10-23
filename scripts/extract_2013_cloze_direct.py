# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2010-2025完型真题\【完型真题】-英语二（2010-2024年）.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

for p in [6, 7]:
    pix = doc[p].get_pixmap(dpi=130)
    res, _ = ocr(pix.tobytes('png'))
    txt = '\n'.join([r[1] for r in res]) if res else ''
    print(f"=== PAGE {p+1} ===", flush=True)
    print(txt, flush=True)
