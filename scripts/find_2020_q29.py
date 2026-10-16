import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky1):
    if "2020" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky1, f)
        break

doc = pymupdf.open(target)
for p in range(len(doc)):
    t = doc[p].get_text()
    if "29." in t:
        print(f"=== Page {p+1} contains '29.' ===")
        lines = [l for l in t.split('\n') if l.strip()]
        for idx, l in enumerate(lines):
            if "29." in l or "29．" in l:
                print("\n".join(lines[max(0, idx-2):min(len(lines), idx+15)]))
