import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def print_first_lines(fname, pno, count=25):
    import os
    doc = fitz.open(os.path.join(pdf_dir, fname))
    lines = doc[pno-1].get_text().split('\n')
    print(f"=== {fname} Page {pno} (first {count} lines) ===")
    for l in lines[:count]:
        print("  ", l.strip())

print_first_lines("2009年考研英语真题解析.pdf", 5)
print_first_lines("2008年考研英语真题解析.pdf", 4)
print_first_lines("2008年考研英语真题解析.pdf", 5)
