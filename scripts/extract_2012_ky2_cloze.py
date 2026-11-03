# -*- coding: utf-8 -*-
import fitz
import re
import sys
from rapidocr_onnxruntime import RapidOCR

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2012年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)
ocr = RapidOCR()

print("Scanning pages 1 to 13 (Cloze Q1-Q20)...", flush=True)

page_texts = {}
for p in range(0, 13):
    pix = doc[p].get_pixmap(dpi=120)
    res, _ = ocr(pix.tobytes('png'))
    txt = '\n'.join([r[1] for r in res]) if res else ''
    page_texts[p+1] = txt
    print(f"Page {p+1} scanned ({len(txt)} chars)", flush=True)

with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\2012_ky2_cloze_raw.txt', 'w', encoding='utf-8') as f:
    for p in range(1, 14):
        f.write(f"\n\n=== PAGE {p} ===\n\n" + page_texts.get(p, ''))

print("Cloze scan completed and written to scripts/2012_ky2_cloze_raw.txt", flush=True)
