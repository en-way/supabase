# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = Path(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2018黄皮书真题解析（英语一）.pdf")
doc = fitz.open(str(p))

targets = [24, 27, 30, 34, 40]
for i in range(len(doc)):
    t = doc[i].get_text()
    for q in targets:
        if f"{q}." in t and ("精解" in t or "正确率" in t or "【考点" in t or "［精准定位］" in t or "【命题解密】" in t):
            print(f"=== Page {i+1} for Q{q} ===")
            lines = t.split("\n")
            for idx, l in enumerate(lines):
                if f"{q}." in l and not "Page" in l:
                    print("\n".join(lines[idx:idx+15]))
                    print("-" * 40)
                    break
