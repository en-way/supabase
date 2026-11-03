# -*- coding: utf-8 -*-
import fitz
import re
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2013年真题解析及复习思路.pdf')
ocr = RapidOCR()

# Pages for bilingual texts:
# Text 1: 18, 19, 21, 22, 23
# Text 2: 26, 28, 30, 31, 32
# Text 3: 36, 38, 39, 41, 42, 43
# Text 4: 45, 46, 48, 49, 51, 52

# Let's inspect the paragraph headers in bilingual sections (I ①, II ①, III ①, etc.)
def inspect_bilingual(pages, label):
    print(f"\n=== {label} ===")
    for p in pages:
        pix = doc[p].get_pixmap(dpi=90)
        res, _ = ocr(pix.tobytes('png'))
        txt = '\n'.join([r[1] for r in res]) if res else ''
        lines = txt.splitlines()
        for l in lines:
            m = re.search(r'([I|V|X]+)\s*[①O0]', l)
            if m:
                print(f"P{p+1}: {l.strip()[:80]}")

inspect_bilingual([17, 18, 20, 21, 22, 23], 'Text 1')
inspect_bilingual([25, 27, 29, 30, 31, 32], 'Text 2')
inspect_bilingual([35, 37, 38, 40, 41, 42], 'Text 3')
inspect_bilingual([44, 45, 47, 48, 50, 51], 'Text 4')
