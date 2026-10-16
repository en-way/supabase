# -*- coding: utf-8 -*-
import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2010年真题解析及复习思路.pdf"
doc = pymupdf.open(pdf_path)

print("=== 2010 ky2 Part B in PDF ===")
for p in range(len(doc)):
    t = doc[p].get_text()
    if 'Utah' in t or 'Kroo' in t:
        print(f"--- Page {p+1} ---")
        lines = t.splitlines()
        for idx, l in enumerate(lines):
            if 'Utah' in l or 'Kroo' in l or 'assemble' in l or 'change' in l:
                print("\n".join(lines[max(0, idx-3):min(len(lines), idx+6)]))
                print("-" * 30)
