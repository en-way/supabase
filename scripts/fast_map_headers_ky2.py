# -*- coding: utf-8 -*-
import fitz, io, sys
from PIL import Image
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2018年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Mapping all 72 pages using header crop (top 18%)...", flush=True)

page_map = []
for pno in range(len(doc)):
    page = doc[pno]
    rect = fitz.Rect(0, 0, page.rect.width, page.rect.height * 0.18)
    pix = page.get_pixmap(clip=rect, dpi=100)
    img = Image.open(io.BytesIO(pix.tobytes("png")))
    res, _ = ocr(img)
    header_text = " ".join([item[1] for item in res]) if res else ""
    page_map.append((pno + 1, header_text))
    if any(k in header_text for k in ['Text', 'Section', 'Part', '完形', '阅读', '翻译', '写作', '试题', '解析']):
        print(f"P.{pno+1:2d}: {header_text}", flush=True)
    elif pno % 10 == 0:
        print(f"P.{pno+1:2d}: (header: {header_text[:40]})", flush=True)

print("Done mapping!", flush=True)
