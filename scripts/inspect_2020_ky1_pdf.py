import os
import sys
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2020黄皮书真题解析（英语一）.pdf"
print(f"Authoritative PDF: {pdf_path}")

doc = pymupdf.open(pdf_path)
print(f"Total Pages: {len(doc)}")

non_empty = [i+1 for i, page in enumerate(doc) if len(page.get_text().strip()) > 0]
print(f"Pages with selectable text: {len(non_empty)} / {len(doc)}")
if non_empty:
    print(f"Sample pages with text: {non_empty[:10]}")
    for p_num in non_empty[:3]:
        print(f"--- Page {p_num} preview ---")
        lines = [l.strip() for l in doc[p_num-1].get_text().splitlines() if l.strip()]
        print("\n".join(lines[:6]))
