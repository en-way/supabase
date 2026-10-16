import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky2):
    if "2021" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky2, f)
        break

doc = pymupdf.open(target)
for p in range(9, 18):
    t = doc[p].get_text()
    print(f"=== 2021 ky2 Page {p+1} ===")
    lines = [l for l in t.split('\n') if l.strip()]
    for idx, l in enumerate(lines):
        if any(f"{q}." in l or f"{q}．" in l for q in [21, 22, 23, 24, 25]):
            print(f"--- Q marker on P{p+1}: {l} ---")
            print("\n".join(lines[max(0, idx):min(len(lines), idx+30)]))
            print("="*40)
