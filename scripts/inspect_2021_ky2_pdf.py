import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base):
    if "2021" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base, f)
        break

print(f"Target PDF: {target}")
doc = pymupdf.open(target)
print("Page count:", len(doc))

# Search for Q21, Q23, Q24, Q25 in the PDF
for p in range(len(doc)):
    t = doc[p].get_text()
    if any(k in t for k in ["21. Research", "23. Efforts", "24. We can learn", "25. Scandinavian"]):
        print(f"=== Page {p+1} ===")
        for line in t.split('\n'):
            if any(k in line for k in ["21.", "22.", "23.", "24.", "25.", "精准定位", "命题解密"]):
                print("  ", line.strip()[:100])
