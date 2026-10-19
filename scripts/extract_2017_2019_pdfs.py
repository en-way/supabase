import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Extracting 2017 ky1 Text 2 (Q31-Q35) ===")
doc17 = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2017黄皮书真题解析（英语一）.pdf')

for p in range(len(doc17)):
    t = doc17[p].get_text()
    if any(q in t for q in ['31. Robert F. Kennedy', '32. It can be inferred', '33. Which of the following is true', '34. According to the author,', '35. It can be inferred from the last']):
        print(f"--- 2017 Page {p+1} ---")
        print(t)
        print("="*60)

print("\n=== Extracting 2019 ky1 Text 4 (Q36-Q40) ===")
doc19 = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2019黄皮书真题解析（英语一）.pdf')

for p in range(len(doc19)):
    t = doc19[p].get_text()
    if any(q in t for q in ['36. The Supreme Court', '37. It can be learned from', '38. According to Justice', '39. Who are most likely', '40. In dealing with']):
        print(f"--- 2019 Page {p+1} ---")
        print(t)
        print("="*60)
