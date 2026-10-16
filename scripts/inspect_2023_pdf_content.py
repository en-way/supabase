import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_pdf(yr, cat):
    base = pdf_base_ky1 if cat == 'ky1' else pdf_base_ky2
    for f in os.listdir(base):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(base, f))
    return None

doc23_1 = get_pdf(2023, 'ky1')
print("=== 2023 ky1 PDF Page 1-5 sample ===")
for p in range(5):
    print(f"--- Page {p+1} ---")
    print(doc23_1[p].get_text()[:600])

print("\n=== 2023 ky1 PDF Reading Q21 search ===")
for p in range(len(doc23_1)):
    t = doc23_1[p].get_text()
    if "21." in t and any(k in t for k in ["精准定位", "命题解密", "试题精解", "锁定", "答案"]):
        print(f"--- Page {p+1} contains Q21 ---")
        print(t[:1200])
        break
