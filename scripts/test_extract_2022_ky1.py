import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky1):
    if "2022" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky1, f)
        break

doc = pymupdf.open(target)

# Let's inspect P27 for Q27
print("=== 2022 ky1 P27-28 ===")
for p in [26, 27]:
    t = doc[p].get_text()
    if "27." in t:
        print(f"--- P{p+1} ---")
        idx = t.find("27.")
        print(t[idx:idx+1500])

# Let's inspect P36-37 for Q32
print("=== 2022 ky1 P36-37 ===")
for p in [35, 36]:
    t = doc[p].get_text()
    if "32." in t:
        print(f"--- P{p+1} ---")
        idx = t.find("32.")
        print(t[idx:idx+1500])

# Let's inspect P45-51 for Q36, 37, 38, 39
print("=== 2022 ky1 P45-51 ===")
for p in range(44, 52):
    t = doc[p].get_text()
    for q in [36, 37, 38, 39]:
        if f"{q}." in t:
            print(f"--- Q{q} on P{p+1} ---")
            idx = t.find(f"{q}.")
            print(t[idx:idx+1200])
            print("="*40)
