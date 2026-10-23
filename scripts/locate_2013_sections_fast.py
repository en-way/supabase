# -*- coding: utf-8 -*-
import fitz
import sys
import numpy as np
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2013年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Scanning top headers of all {len(doc)} pages...", flush=True)

for p in range(len(doc)):
    rect = doc[p].rect
    # Crop top 20% of the page
    crop_rect = fitz.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + rect.height * 0.22)
    pix = doc[p].get_pixmap(clip=crop_rect, dpi=90)
    img_bytes = pix.tobytes('png')
    res, _ = ocr(img_bytes)
    txt = ' | '.join([r[1] for r in res]) if res else ''
    print(f"P{p+1}: {txt[:100]}", flush=True)
