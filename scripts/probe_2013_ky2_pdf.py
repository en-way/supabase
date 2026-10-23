import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2013年真题解析及复习思路.pdf'

reader = pypdf.PdfReader(pdf_path)
for i in range(min(15, len(reader.pages))):
    text = reader.pages[i].extract_text() or ''
    first_line = text.split('\n')[0] if text else '[EMPTY]'
    print(f"Page {i+1}: len={len(text)}, first_line={first_line[:80]}")
