# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2020年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

pages_to_dump = [1, 10, 18, 27, 38, 46, 53]

for p_num in pages_to_dump:
    pix = doc[p_num - 1].get_pixmap(dpi=150)
    res, _ = ocr(pix.tobytes('png'))
    if res:
        text = '\n'.join([r[1] for r in res])
        print(f"=== PAGE {p_num} ===")
        print(text[:1500])
        print("\n" + "="*40 + "\n")
