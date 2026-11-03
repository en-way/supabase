# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np
from PIL import Image
import io

pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2015年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Total pages: {len(doc)}")
# Check headers of pages 1, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
for page_idx in range(0, len(doc), 3):
    page = doc[page_idx]
    # Crop top 25% of page for speed
    rect = page.rect
    crop_rect = fitz.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + rect.height * 0.25)
    pix = page.get_pixmap(clip=crop_rect, dpi=120)
    img = Image.open(io.BytesIO(pix.tobytes('png')))
    res, _ = ocr(np.array(img))
    header = " ".join([l[1] for l in res[:4]]) if res else "EMPTY"
    print(f"Page {page_idx+1:02d}: {header}")
