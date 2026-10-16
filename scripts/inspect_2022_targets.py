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

# Check 2022 ky1
doc22_1 = get_doc(2022, 'ky1')
print("=================== 2022 ky1 ===================")
targets_22_1 = [27, 32, 36, 37, 38, 39]
for p in range(20, 55):
    t = doc22_1[p].get_text()
    for q in targets_22_1:
        if f"{q}." in t and any(k in t for k in ["【精准定位】", "［精准定位］", "【命题解密】", "［命题解密］", "【答案】", "［答案］"]):
            print(f"--- 2022 ky1 Q{q} on Page {p+1} ---")
            lines = [l for l in t.split('\n') if l.strip()]
            for idx, l in enumerate(lines):
                if f"{q}." in l:
                    print("\n".join(lines[max(0, idx):min(len(lines), idx+35)]))
                    print("-" * 40)

# Check 2022 ky2
doc22_2 = get_doc(2022, 'ky2')
print("=================== 2022 ky2 ===================")
targets_22_2 = [21, 22, 23, 24, 26, 27, 28, 29]
for p in range(9, 30):
    t = doc22_2[p].get_text()
    for q in targets_22_2:
        if f"{q}." in t and any(k in t for k in ["【精准定位】", "［精准定位］", "【命题解密】", "［命题解密］", "【答案】", "［答案］"]):
            print(f"--- 2022 ky2 Q{q} on Page {p+1} ---")
            lines = [l for l in t.split('\n') if l.strip()]
            for idx, l in enumerate(lines):
                if f"{q}." in l:
                    print("\n".join(lines[max(0, idx):min(len(lines), idx+35)]))
                    print("-" * 40)
