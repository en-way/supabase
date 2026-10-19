import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Inspect 2006 ky1 Q36
p2006 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2006年考研英语真题解析.pdf'
doc2006 = fitz.open(p2006)
print("=== 2006 ky1 Q36 ===")
for p in range(len(doc2006)):
    t = doc2006[p].get_text()
    if '36.' in t and ('Wordsworth' in t or 'Baudelaire' in t):
        print(f"2006 Page {p+1}:")
        print(t[:1500])
        print("="*40)

# 2. Inspect 2005 ky1 Q26 and surrounding questions (Q24 - Q34)
p2005 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2005年考研英语真题解析.pdf'
doc2005 = fitz.open(p2005)
print("=== 2005 ky1 Q24 - Q28 ===")
for p in range(len(doc2005)):
    t = doc2005[p].get_text()
    if '26.' in t and 'smoking' in t:
        print(f"2005 Page {p+1}:")
        print(t[:1500])
        print("="*40)

