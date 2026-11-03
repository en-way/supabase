# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import fitz
from rapidocr_onnxruntime import RapidOCR
import numpy as np
from PIL import Image
import io
import re

pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2015年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print("=== Scanning 2015 ky2 Cloze (Pages 1 to 14) ===")
for page_idx in range(14):
    page = doc[page_idx]
    pix = page.get_pixmap(dpi=150)
    img = Image.open(io.BytesIO(pix.tobytes('png')))
    res, _ = ocr(np.array(img))
    if not res:
        continue
    text = "\n".join([line[1] for line in res])
    # Search for question number and options
    for q in range(1, 21):
        if re.search(rf'(?:^|\n)\s*{q}\s*[\.、]\s*本题考查', text) or re.search(rf'【答案】\s*([A-D])', text):
            # print snippet
            lines = text.split("\n")
            for i, l in enumerate(lines):
                if f"{q}.本题考查" in l or f"{q}、本题考查" in l or f"{q}. 本题考查" in l:
                    print(f"P{page_idx+1} Q{q}:")
                    for k in range(max(0, i-3), min(len(lines), i+12)):
                        print("  ", lines[k])
