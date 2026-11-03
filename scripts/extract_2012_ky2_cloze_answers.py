# -*- coding: utf-8 -*-
import fitz
import sys
import re
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2012年真题解析及复习思路.pdf')
ocr = RapidOCR()

print("Extracting Cloze Q1-Q20 answers directly from HuangPiShu (pages 1 to 12)...", flush=True)

# In each page 1-12, let's OCR and search for "【答案" or "答案"
for p in range(0, 13):
    page = doc[p]
    # render page at 80 DPI
    pix = page.get_pixmap(dpi=80)
    res, _ = ocr(pix.tobytes('png'))
    if not res:
        continue
    txt = '\n'.join([r[1] for r in res])
    lines = txt.splitlines()
    for l in lines:
        if '【答案' in l or '答案】' in l or re.search(r'\[答案\]|[【\[]答\s*案', l):
            print(f"Page {p+1}: {l}", flush=True)
        elif re.search(r'^\s*([1-9]|1[0-9]|20)\s*[\.、]\s*本题考查', l):
            print(f"Page {p+1} Header: {l}", flush=True)
