# -*- coding: utf-8 -*-
import fitz
import re
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2012年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print("Scanning pages 1 to 56 for question headers and answers...", flush=True)

answers = {}

for p in range(0, 56):
    pix = doc[p].get_pixmap(dpi=120)
    res, _ = ocr(pix.tobytes('png'))
    if not res:
        continue
    text = '\n'.join([r[1] for r in res])
    
    # Find question numbers like: "1.本题考查", "21.", "【答案A】", etc.
    # Let's search for 【答案[A-G]】 or [答案][A-G] or 【答案】[A-G]
    # Also find question number mentions
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # Match pattern like "1.本题考查" or "21. It is implied" or "21."
        q_match = re.search(r'(?:^|[^0-9])([1-9]|[1-4][0-9])\s*[\.、]\s*(?:本题考查|According|It |Which|The |By |In |A |What|To |As )', line)
        ans_match = re.search(r'【?答案\s*([A-G])】?', line)
        if ans_match:
            print(f"Page {p+1}: {line.strip()}", flush=True)
        elif '本题考查' in line:
            print(f"Page {p+1}: {line.strip()}", flush=True)

print("Scan finished.", flush=True)
