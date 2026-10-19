import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2021 ky1 Text 4 (Q36-40)
p2021 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2021黄皮书真题解析（英语一）.pdf'
doc2021 = fitz.open(p2021)
print("=== 2021 ky1 Text 4 ===")
for p in range(len(doc2021)):
    t = doc2021[p].get_text()
    if '36.' in t and 'broadband' in t:
        print(f"2021 Page {p+1} (Q36):")
        print(t[:1500])
        print("="*40)
    if '40.' in t and 'Congress' in t:
        print(f"2021 Page {p+1} (Q40):")
        print(t[:1500])
        print("="*40)

# 2. 2020 ky1 Text 4 (Q36-40)
p2020 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2020黄皮书真题解析（英语一）.pdf'
doc2020 = fitz.open(p2020)
print("\n=== 2020 ky1 Text 4 ===")
for p in range(len(doc2020)):
    t = doc2020[p].get_text()
    if '38.' in t and ('multilateral' in t or 'unilateral' in t):
        print(f"2020 Page {p+1} (Q38):")
        print(t[:1500])
        print("="*40)
    if '40.' in t and ('Digital Tax' in t or 'digital' in t):
        print(f"2020 Page {p+1} (Q40):")
        print(t[:1500])
        print("="*40)

# 3. 2022 ky2 Text 4 (Q36-40)
p2022 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2010-2025）\2022年考研英语（二）真题解析.pdf'
doc2022 = fitz.open(p2022)
print("\n=== 2022 ky2 Text 4 ===")
for p in range(len(doc2022)):
    t = doc2022[p].get_text()
    if '36.' in t and 'ethics' in t:
        print(f"2022 Page {p+1} (Q36):")
        print(t[:1500])
        print("="*40)
    if '38.' in t and 'Schwitzgebel' in t:
        print(f"2022 Page {p+1} (Q38):")
        print(t[:1500])
        print("="*40)

# 4. 2007 ky1 Text 3 (Q34-35)
p2007 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2007年真题解析及复习思路.pdf'
doc2007 = fitz.open(p2007)
print("\n=== 2007 ky1 Text 3 (Q34-35) ===")
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
