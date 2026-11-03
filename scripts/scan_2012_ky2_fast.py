# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2012年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Total pages: {len(doc)}", flush=True)

# Check last 3 pages and first 3 pages
pages_to_check = [0, 1, 2, len(doc)-2, len(doc)-1]
for p in pages_to_check:
    pix = doc[p].get_pixmap(dpi=110)
    res, _ = ocr(pix.tobytes('png'))
    txt = '\n'.join([r[1] for r in res]) if res else ''
    print(f"\n=== Page {p+1} ===", flush=True)
    for l in txt.splitlines()[:15]:
        print(l, flush=True)
