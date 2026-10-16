import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base):
    if "2011" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base, f)
        break

doc = pymupdf.open(target)

# Q3 is on page 2
print("=== 2011 Q3 ===")
t2 = doc[1].get_text()
idx3 = t2.find("3.\n")
idx4 = t2.find("4.\n")
print(t2[idx3:idx4].strip())

# Q11 is on page 4
print("\n=== 2011 Q11 ===")
t4 = doc[3].get_text()
idx11 = t4.find("11.")
idx12 = t4.find("12.")
print(t4[idx11:idx12].strip())

# Q39 is on page 40-41
print("\n=== 2011 Q39 ===")
t40 = doc[39].get_text()
idx39 = t40.find("39.")
print(t40[idx39:idx39+1500].strip())

# Q40 is on page 43
print("\n=== 2011 Q40 ===")
t43 = doc[42].get_text()
idx40 = t43.find("40.")
print(t43[:idx40+1500].strip())
