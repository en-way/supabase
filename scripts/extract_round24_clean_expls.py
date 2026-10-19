import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2021 ky1 Text 4
p2021 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2021黄皮书真题解析（英语一）.pdf'
doc2021 = fitz.open(p2021)
print("=== 2021 ky1 Text 4 Explanations ===")
for p in range(38, 44):
    print(f"--- Page {p+1} ---")
    print(doc2021[p].get_text())

# 2. 2020 ky1 Text 4
p2020 = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2020黄皮书真题解析（英语一）.pdf'
doc2020 = fitz.open(p2020)
print("\n=== 2020 ky1 Text 4 Explanations ===")
for p in range(36, 43):
    print(f"--- Page {p+1} ---")
    print(doc2020[p].get_text())

