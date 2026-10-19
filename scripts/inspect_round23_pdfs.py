import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Inspect 2006 ky1 Q22, Q25, Q32
p2006 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2006年考研英语真题解析.pdf'
doc2006 = fitz.open(p2006)
print("=== 2006 ky1 Q22, Q25, Q32 ===")
for p in range(len(doc2006)):
    t = doc2006[p].get_text()
    if '22. According to' in t or '22.According to' in t:
        print(f"2006 Page {p+1} (Q22):")
        print(t[:1200])
        print("="*40)
    if '25. In the author' in t or '25.In the author' in t or "25. ln the author" in t:
        print(f"2006 Page {p+1} (Q25):")
        print(t[:1000])
        print("="*40)
    if '32. We can infer' in t or '32.We can infer' in t:
        print(f"2006 Page {p+1} (Q32):")
        print(t[:1200])
        print("="*40)

# 2. Inspect 2008 ky1 Q35
p2008 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2008年考研英语真题解析.pdf'
doc2008 = fitz.open(p2008)
print("\n=== 2008 ky1 Q35 ===")
for p in range(len(doc2008)):
    t = doc2008[p].get_text()
    if '35. The text intends' in t or '35.The text intends' in t:
        print(f"2008 Page {p+1} (Q35):")
        print(t[:1200])
        print("="*40)

# 3. Inspect 2001 ky1 Q28
p2001 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2001年真题解析及复习思路.pdf'
doc2001 = fitz.open(p2001)
print("\n=== 2001 ky1 Q28 ===")
for p in range(len(doc2001)):
    t = doc2001[p].get_text()
    if '28. It seems that now' in t or '28.It seems that now' in t or ('28.' in t and 'country\'s economy depends' in t):
        print(f"2001 Page {p+1} (Q28):")
        print(t[:1200])
        print("="*40)
