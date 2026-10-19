import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2008 PDF Text 4
p2008 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2008年考研英语真题解析.pdf'
doc2008 = fitz.open(p2008)
print("=== 2008 PDF Pages ===")
for i, page in enumerate(doc2008):
    t = page.get_text()
    if 'George Washington' in t or '36.' in t or 'Thomas Jefferson' in t or 'Text 4' in t:
        if any(k in t for k in ['36.', '37.', '38.', '39.', '40.']):
            print(f"2008 Page {i+1}:")
            for line in t.splitlines()[:5]:
                print("  ", line.strip())

# 2. 2009 PDF Text 2 Q29-30
p2009 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2009年考研英语真题解析.pdf'
doc2009 = fitz.open(p2009)
print("\n=== 2009 PDF Pages ===")
for i, page in enumerate(doc2009):
    t = page.get_text()
    if '29.' in t or '30.' in t:
        print(f"2009 Page {i+1}:")
        for line in t.splitlines()[:5]:
            print("  ", line.strip())
