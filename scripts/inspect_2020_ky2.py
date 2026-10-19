import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

p2020_ky2 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2020年真题解析及复习思路.pdf'
doc = fitz.open(p2020_ky2)
print("=== 2020 ky2 Text 1 (Q21-25) ===")
for p in range(len(doc)):
    t = doc[p].get_text()
    if '21.' in t and 'rats' in t:
        print(f"2020 ky2 Page {p+1} (Q21):")
        print(t[:1500])
        print("="*40)
    if '26.' in t and 'CEO' in t:
        print(f"2020 ky2 Page {p+1} (Q26):")
        print(t[:1500])
        print("="*40)
