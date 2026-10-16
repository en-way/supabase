import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_doc(yr, cat):
    base = pdf_base_ky1 if cat == 'ky1' else pdf_base_ky2
    for f in os.listdir(base):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(base, f))
    return None

# Check 2016 ky1 Q44 and Q45
doc16 = get_doc(2016, 'ky1')
print("=== 2016 ky1 P57-58 ===")
for p in [56, 57]:
    print(f"--- Page {p+1} ---")
    print(doc16[p].get_text())

# Check 2009 ky1 Q43, Q44
doc09 = get_doc(2009, 'ky1')
print("=== 2009 ky1 P52-53 ===")
for p in [51, 52]:
    print(f"--- Page {p+1} ---")
    print(doc09[p].get_text())

# Check 2020 ky1 Q29
doc20 = get_doc(2020, 'ky1')
print("=== 2020 ky1 search Q29 ===")
for p in range(len(doc20)):
    t = doc20[p].get_text()
    if "29." in t and any(k in t for k in ["【精准定位】", "【命题解密】", "【答案】", "【精解】"]):
        print(f"--- Page {p+1} ---")
        print(t[:1500])
