# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\2001-2025阅读真题\【大间距】-英语二 （2010-2024）.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Total pages in Reading PDF: {len(doc)}", flush=True)

# 2010 is first, ~15 pages per year. 2010: 1-15, 2011: 16-30, 2012: 31-45, 2013: 46-60
# Let's check pages 40 to 65
for p in range(40, 65):
    rect = doc[p].rect
    crop_rect = fitz.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + rect.height * 0.15)
    pix = doc[p].get_pixmap(clip=crop_rect, dpi=80)
    res, _ = ocr(pix.tobytes('png'))
    txt = ' | '.join([r[1] for r in res]) if res else ''
    if '2013' in txt or 'Text' in txt or 'Section' in txt:
        print(f"Page {p+1}: {txt}", flush=True)
