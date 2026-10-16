import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def dump_page_lines(fname, pno, filter_terms=None):
    import os
    doc = fitz.open(os.path.join(pdf_dir, fname))
    txt = doc[pno-1].get_text()
    print(f"\n=== {fname} Page {pno} ===")
    for l in txt.split("\n"):
        if filter_terms is None or any(t in l for t in filter_terms):
            print("  ", l.strip())

# 2008 Q4 (Page 2) & Q11 (Page 4)
dump_page_lines("2008年考研英语真题解析.pdf", 2)
dump_page_lines("2008年考研英语真题解析.pdf", 4)

# 2009 Q4, Q8, Q12 (Pages 2, 3, 4, 5)
dump_page_lines("2009年考研英语真题解析.pdf", 2)
dump_page_lines("2009年考研英语真题解析.pdf", 3)
dump_page_lines("2009年考研英语真题解析.pdf", 4)
dump_page_lines("2009年考研英语真题解析.pdf", 5)

# 2012 Q7 (Page 3, 4)
dump_page_lines("2012黄皮书真题解析（英语一）.pdf", 3)
dump_page_lines("2012黄皮书真题解析（英语一）.pdf", 4)

# 2013 Q40 (around Page 44, 45, 46)
dump_page_lines("2013黄皮书真题解析（英语一）.pdf", 43)
dump_page_lines("2013黄皮书真题解析（英语一）.pdf", 44)
dump_page_lines("2013黄皮书真题解析（英语一）.pdf", 45)
