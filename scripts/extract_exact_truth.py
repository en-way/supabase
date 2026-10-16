# -*- coding: utf-8 -*-
"""
extract_exact_truth.py
Extract precise truth from Huang Pi Shu PDFs.
"""

import pymupdf
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2019 English 1 Text 1 & Text 2
pdf_2019_1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2019黄皮书真题解析（英语一）.pdf"
doc = pymupdf.open(pdf_2019_1)

print("=== 2019 ky1 Text 1 End & Text 2 Beginning ===")
for p in range(12, 22):
    t = doc[p].get_text()
    if 'Short-termism' in t or 'Grade inflation' in t:
        print(f"--- Page {p+1} ---")
        print(t[:1500])

print("\n=== 2019 ky1 Text 4 End ===")
for p in range(30, 40):
    t = doc[p].get_text()
    if 'Neil Saunders' in t or 'Small Business & Entrepreneurship' in t:
        print(f"--- Page {p+1} ---")
        print(t[:1500])

# 2. 2022 English 2 Text 3
pdf_2022_2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2022年真题解析及复习思路.pdf"
doc2 = pymupdf.open(pdf_2022_2)

print("\n=== 2022 ky2 Text 3 End ===")
for p in range(len(doc2)):
    t = doc2[p].get_text()
    if 'dark patterns' in t.lower() and ('researcher' in t.lower() or 'standards' in t.lower()):
        print(f"--- Page {p+1} ---")
        print(t[:1500])

# 3. 2008 English 1 Text 3
pdf_2008_1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2008年考研英语真题解析.pdf"
doc3 = pymupdf.open(pdf_2008_1)

print("\n=== 2008 ky1 Text 3 End ===")
for p in range(len(doc3)):
    t = doc3[p].get_text()
    if 'Gordon' in t and 'confident' in t:
        print(f"--- Page {p+1} ---")
        print(t[:1500])
