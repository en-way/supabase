import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

p2007 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2007年考研英语真题解析.pdf'
doc2007 = fitz.open(p2007)
print("=== 2007 ky1 Text 3 (Q34-35) ===")
for p in range(len(doc2007)):
    t = doc2007[p].get_text()
    if '34.' in t and 'inferred from the last paragraph' in t:
        print(f"2007 Page {p+1} (Q34):")
        print(t[:1500])
        print("="*40)
    if '35.' in t and 'best title for this text' in t:
        print(f"2007 Page {p+1} (Q35):")
        print(t[:1500])
        print("="*40)
