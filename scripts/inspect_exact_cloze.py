import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def show_around(fname, pno, start_line_str):
    import os
    doc = fitz.open(os.path.join(pdf_dir, fname))
    lines = doc[pno-1].get_text().split('\n')
    for i, l in enumerate(lines):
        if l.strip().startswith(start_line_str):
            print(f"=== {fname} Page {pno} (line {i}) ===")
            for j in range(max(0, i-1), min(len(lines), i+15)):
                print("  ", lines[j].strip())

print("2009 Q4:")
show_around("2009年考研英语真题解析.pdf", 2, "4.")
show_around("2009年考研英语真题解析.pdf", 1, "4.")

print("\n2009 Q12:")
show_around("2009年考研英语真题解析.pdf", 4, "12.")
show_around("2009年考研英语真题解析.pdf", 5, "12.")

print("\n2008 Q4:")
show_around("2008年考研英语真题解析.pdf", 2, "4.")

print("\n2008 Q11:")
show_around("2008年考研英语真题解析.pdf", 4, "11.")

print("\n2012 Q7:")
show_around("2012黄皮书真题解析（英语一）.pdf", 3, "7.")
show_around("2012黄皮书真题解析（英语一）.pdf", 4, "7.")
