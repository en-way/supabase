# -*- coding: utf-8 -*-
import fitz
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2020年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print(f"Total pages: {len(doc)}", flush=True)

with open("scripts/2020_ky2_structure.txt", "w", encoding="utf-8") as out:
    for p in range(len(doc)):
        pix = doc[p].get_pixmap(dpi=100)
        res, _ = ocr(pix.tobytes('png'))
        if not res:
            continue
        text = '\n'.join([r[1] for r in res])
        
        headers = []
        for line in text.splitlines():
            line_str = line.strip()
            if any(k in line_str for k in ["Section", "Part", "Text", "真题精解", "总体分析", "答案速查", "试题精解", "完形填空", "英语知识运用", "阅读理解", "新题型", "英语（二）", "复习思路"]):
                headers.append(line_str)
        summary = f"Page {p+1}: {' | '.join(headers[:4])}"
        out.write(summary + "\n")
        print(summary, flush=True)

print("Scan complete.", flush=True)
