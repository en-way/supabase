import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2009 ky1 Q38 rest
p2009 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2009年考研英语真题解析.pdf'
doc2009 = fitz.open(p2009)
print("=== 2009 Page 42 ===")
print(doc2009[41].get_text()[:1000])

# 2. 2012 ky1 Q39
p2012 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2012黄皮书真题解析（英语一）.pdf'
doc2012 = fitz.open(p2012)
print("=== 2012 ky1 Q39 ===")
for p in range(len(doc2012)):
    t = doc2012[p].get_text()
    if '39.' in t and ('Wisconsin' in t or 'unions' in t):
        print(f"2012 Page {p+1} (Q39):")
        print(t[:1500])
        print("="*40)
