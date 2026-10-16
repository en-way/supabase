import fitz
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

# The clean PDF in 英语二真题解析（2001-2025）
pdf_path = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2004年考研英语真题解析.pdf"
doc = fitz.open(pdf_path)

cipher = {
    '!': 'M', '"': 'a', '#': 'n', '$': 'y', '%': 't', '&': 'h', '’': 'e',
    '(': 'o', ')': 'r', '*': 'i', '+': 's', ',': 'c', '-': 'u', '.': 'f',
    '/': 'j', '0': '-', '1': 'v', '2': 'l', '3': 'm', '4': 'd', '5': 'b',
    '6': 'g', '7': 'p', '8': '.', '9': 'T', ':': '1', ';': '2', '<': 'w',
    '=': '3', '>': '4', '?': '5', '@': '+', 'A': 'E', 'B': 'z', 'C': 'O',
    'D': 'Y', 'E': 'k', 'F': 'A', 'G': 'B', 'H': 'C', 'I': 'D', 'J': '9',
    'K': '%', 'L': 'H', 'M': 'S', 'N': '7', 'O': '6', 'P': 'x', 'Q': 'I',
    'R': 'q', 'S': 'W', 'T': '8', 'U': '0', 'V': 'G', 'W': 'F'
}

def decode_text(text):
    out = []
    for c in text:
        if c in cipher:
            out.append(cipher[c])
        else:
            out.append(c)
    return ''.join(out)

# Decode all pages and save to scratch_2004_clean_decoded.txt
all_pages = []
for p in range(len(doc)):
    page_text = doc[p].get_text()
    decoded = decode_text(page_text)
    all_pages.append(f"<<<PAGE_{p+1}>>>\n{decoded}")

full_decoded = '\n'.join(all_pages)
with open("scratch_2004_clean_decoded.txt", "w", encoding="utf-8") as f:
    f.write(full_decoded)

print(f"Successfully decoded {len(doc)} pages! Output written to scratch_2004_clean_decoded.txt (len={len(full_decoded)})")
