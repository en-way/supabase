# -*- coding: utf-8 -*-
import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2012年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Indexing 2012 ky2 PDF ({len(doc)} pages)...")

# Check pages with step=2 or specific pages to find sections
# Let's inspect every 2nd page's top 1/4 area
results = []
for p in range(0, len(doc)):
    # only OCR top 25% of the page to be super fast!
    rect = doc[p].rect
    crop_rect = fitz.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + rect.height * 0.25)
    pix = doc[p].get_pixmap(clip=crop_rect, dpi=100)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    res, _ = ocr(img)
    lines = [item[1] for item in res] if res else []
    text_sample = " | ".join(lines[:3])
    if any(k in text_sample for k in ['Text', 'Part', 'Section', '阅读', '答案', '第一部分', '第二部分', '第三部分', '第四部分', '总体分析']):
        print(f"Page {p+1}: {text_sample}")
        results.append((p+1, text_sample))

print("Indexing complete. Found key sections:", len(results))
