# -*- coding: utf-8 -*-
import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2012年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Total pages in 2012 ky2 PDF: {len(doc)}")

# Let's inspect pages 1 to 5 to find table of contents or headers
for p in range(min(5, len(doc))):
    pix = doc[p].get_pixmap(dpi=120)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    res, _ = ocr(img)
    lines = [item[1] for item in res] if res else []
    print(f"--- Page {p+1} ({len(lines)} lines) ---")
    for l in lines[:5]:
        print(" ", l)
