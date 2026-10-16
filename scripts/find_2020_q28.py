# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2020黄皮书真题解析（英语一）.pdf")
doc = fitz.open(str(p))
print(f"2020 PDF pages: {len(doc)}")

for i in range(len(doc)):
    t = doc[i].get_text()
    if any(k in t for k in ["Sci-Hub", "Elbakyan", "open-access"]) and ("28." in t or "28" in t):
        print(f"=== Page {i+1} ===")
        lines = t.split("\n")
        for idx, l in enumerate(lines):
            if "28." in l or "Sci-Hub" in l or "Elbakyan" in l:
                print("\n".join(lines[max(0, idx-2):min(len(lines), idx+15)]))
                break
