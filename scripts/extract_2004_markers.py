import fitz
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2004年考研英语真题解析.pdf")

print("=== 2004 Cloze Questions in HuangPiShu ===")
# Collect all questions from explanations on pages 2 to 11
for p in range(2, 11):
    t = doc[p].get_text()
    lines = t.split('\n')
    for i, l in enumerate(lines):
        if '本题考核的知识点' in l or '本题考查' in l:
            # Look backwards for options
            opts_lines = lines[max(0, i-6):i]
            print(f"--- Page {p+1} ---")
            print('\n'.join(opts_lines))
            print(l)
