# -*- coding: utf-8 -*-
from pathlib import Path
import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = Path(r"c:\Users\57867\Desktop\WYJ")

def get_pdf(year, cat):
    cat_dir = "英语一真题解析" if cat == "ky1" else "英语二真题解析"
    for p in base_dir.rglob("*.pdf"):
        if str(year) in p.name and cat_dir in str(p.parent):
            return p
    return None

# 1. Inspect 2020 ky1 Q28
pdf_2020 = get_pdf(2020, "ky1")
if pdf_2020:
    doc = fitz.open(str(pdf_2020))
    print(f"=== 2020 ky1 ({len(doc)} pages) ===")
    for i in range(len(doc)):
        t = doc[i].get_text()
        if "28." in t and "Sci-Hub" in t:
            print(f"--- Page {i+1} ---")
            lines = t.split("\n")
            for idx, l in enumerate(lines):
                if "28." in l or "Sci-Hub" in l:
                    print("\n".join(lines[max(0, idx-2):min(len(lines), idx+18)]))
                    break

# 2. Inspect 2022 ky2 Cloze Q8, Q9, Q12, Q19, Q20
pdf_2022_ky2 = get_pdf(2022, "ky2")
if pdf_2022_ky2:
    doc = fitz.open(str(pdf_2022_ky2))
    print(f"\n=== 2022 ky2 ({len(doc)} pages) ===")
    for i in range(15):
        t = doc[i].get_text()
        if any(f"{q}." in t for q in [8, 9, 12, 19, 20]) and any(k in t for k in ["考点", "精解", "选项", "辨析"]):
            print(f"--- Page {i+1} ---")
            for l in t.split("\n"):
                if any(f"{q}." in l for q in [8, 9, 12, 19, 20]):
                    print(" ", l[:80])
