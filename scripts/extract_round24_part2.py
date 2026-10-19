import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 3. 2022 ky2 Text 4 (Q36-40)
p2022 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）\2022年真题解析及复习思路.pdf'
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
