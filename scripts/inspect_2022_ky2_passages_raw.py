# -*- coding: utf-8 -*-
import sys
import pymupdf
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2022年真题解析及复习思路.pdf"
doc = pymupdf.open(pdf_path)

# Let's inspect page 1 to 7 for Cloze
# Let's find word counts across the PDF: [xxx words]
print("=== Word count mentions in PDF ===")
for p_idx in range(len(doc)):
    text = doc[p_idx].get_text("text")
    m = re.findall(r"\[\d+\s*words?\]", text)
    if m:
        print(f"Page {p_idx+1}: {m}")
