import json
import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# List of targets to inspect in detail:
# 1. 2017 ky1 Q38
# 2. 2016 ky1 Q44, Q45
# 3. 2022 ky1 Q27, Q32, Q36, Q37, Q38, Q39
# 4. 2021 ky2 Q21, Q23, Q24, Q25
# 5. 2022 ky2 Q21, Q22, Q23
# 6. 2009 ky1 Q43, Q44
# 7. 2002 ky1 Q30
# 8. 2010 ky1 Q25

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_pdf_doc(yr, cat):
    base = pdf_base_ky1 if cat == 'ky1' else pdf_base_ky2
    for f in os.listdir(base):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(base, f))
    return None

targets = [
    (2017, 'ky1', 38),
    (2016, 'ky1', 44),
    (2016, 'ky1', 45),
    (2022, 'ky1', 27),
    (2022, 'ky1', 32),
    (2022, 'ky1', 36),
    (2022, 'ky1', 37),
    (2022, 'ky1', 38),
    (2022, 'ky1', 39),
    (2021, 'ky2', 21),
    (2021, 'ky2', 23),
    (2021, 'ky2', 24),
    (2021, 'ky2', 25),
    (2022, 'ky2', 21),
    (2022, 'ky2', 22),
    (2022, 'ky2', 23),
    (2009, 'ky1', 43),
    (2009, 'ky1', 44),
    (2002, 'ky1', 30),
    (2010, 'ky1', 25),
]

print(f"Total targets: {len(targets)}")

for yr, cat, so in targets:
    doc = get_pdf_doc(yr, cat)
    if not doc:
        print(f"[{yr} {cat} Q{so}] PDF not found!")
        continue
    # Search for question number in PDF
    found_pages = []
    for p in range(len(doc)):
        t = doc[p].get_text()
        if f"{so}." in t or f"第{so}题" in t or f"[{so}]" in t or f"【{so}】" in t:
            if any(k in t for k in ["精准定位", "命题解密", "试题精解", "考点提炼", "解题思路", "【答案】"]):
                found_pages.append(p + 1)
    print(f"[{yr} {cat} Q{so}] found in PDF pages: {found_pages}")
