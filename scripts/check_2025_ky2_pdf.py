import pymupdf
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2025英语二真题解析及复习思路.pdf'
doc = pymupdf.open(pdf_path)
print(f'Total pages in 2025 ky2 PDF: {len(doc)}')

for pno in range(min(5, len(doc))):
    text = doc[pno].get_text()
    print(f'Page {pno+1}: text len = {len(text)}')
