# -*- coding: utf-8 -*-
import fitz, sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2018年真题解析及复习思路.pdf'
doc = fitz.open(pdf_path)

toc = doc.get_toc()
print(f"TOC entries: {len(toc)}")
for item in toc:
    print(item)
