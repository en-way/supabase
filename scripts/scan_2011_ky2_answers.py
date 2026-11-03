# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2011年真题解析及复习思路.pdf')
ocr = RapidOCR()

print(f"Total pages: {len(doc)}", flush=True)

# Usually the answer table is in page 1, 2, or last page
for p in [0, 1, 2, 3]:
    pix = doc[p].get_pixmap(dpi=110)
    res, _ = ocr(pix.tobytes('png'))
    txt = '\n'.join([r[1] for r in res]) if res else ''
    print(f"\n=== Page {p+1} ===", flush=True)
    for l in txt.splitlines():
        print(l, flush=True)
