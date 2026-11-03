# -*- coding: utf-8 -*-
import fitz
import re
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2020年真题解析及复习思路.pdf')
ocr = RapidOCR()

with open("scripts/2020_ky2_paragraphs_all.txt", "w", encoding="utf-8") as out:
    for p in range(len(doc)):
        pix = doc[p].get_pixmap(dpi=150)
        res, _ = ocr(pix.tobytes('png'))
        if not res:
            continue
        w, h = pix.width, pix.height
        left_boxes = []
        for box, txt, score in res:
            ys = [pt[1] for pt in box]
            xs = [pt[0] for pt in box]
            min_x, max_x = min(xs), max(xs)
            min_y, max_y = min(ys), max(ys)
            if max_x < w * 0.56: # Left column
                left_boxes.append((min_y, min_x, txt))
        left_boxes.sort(key=lambda x: x[0])
        
        # Check if there is paragraph markers in left boxes
        has_para = any(re.search(r'^[I|V|X]+[①O0❶❷❸❹❺\d]', b[2].strip()) or re.search(r'^[I|V|X]+\s+[①O0❶❷❸❹❺\d]', b[2].strip()) for b in left_boxes)
        if has_para:
            out.write(f"\n==================== Page {p+1} ====================\n")
            for y, x, txt in left_boxes:
                out.write(f"{txt}\n")
            print(f"Found paragraph on Page {p+1}", flush=True)

print("Paragraph scan finished!", flush=True)
