# -*- coding: utf-8 -*-
import fitz
import re
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2013年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print("Scanning pages 1 to 58 for question headers and answers...", flush=True)

answers = {}

for p in range(0, 58):
    pix = doc[p].get_pixmap(dpi=100)
    res, _ = ocr(pix.tobytes('png'))
    if not res:
        continue
    txt = '\n'.join([r[1] for r in res])
    
    # Check for patterns like "【答案B】", "[答案] B", "【答案】B", "【答案】 B"
    for m in re.finditer(r'【?答案\s*([A-G])】?', txt):
        # find nearby question number
        start = max(0, m.start() - 200)
        end = min(len(txt), m.end() + 200)
        snippet = txt[start:end]
        print(f"P{p+1}: Ans={m.group(1)} in snippet: {snippet.replace(chr(10), ' ')[:100]}", flush=True)
