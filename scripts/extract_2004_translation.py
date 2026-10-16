import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf")

print("=== 2004 Full Translation & Passage ===")
for p in range(0, 3):
    print(f"--- Page {p+1} ---")
    t = doc[p].get_text()
    for line in t.split('\n'):
        if any('\u4e00' <= c <= '\u9fff' for c in line) and not '词汇注释' in line:
            print(line.strip())
