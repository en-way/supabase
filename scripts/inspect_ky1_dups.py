import fitz
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

pdf_map = {
    2006: "2006年考研英语真题解析.pdf",
    2007: "2007年考研英语真题解析.pdf",
    2008: "2008年考研英语真题解析.pdf",
    2009: "2009年考研英语真题解析.pdf",
    2010: "2010黄皮书真题解析（英语一）.pdf",
    2011: "2011黄皮书真题解析（英语一）.pdf",
    2012: "2012黄皮书真题解析（英语一）.pdf",
    2013: "2013黄皮书真题解析（英语一）.pdf",
    2014: "2014黄皮书真题解析（英语一）.pdf",
    2015: "2015黄皮书真题解析（英语一）.pdf",
    2016: "2016黄皮书真题解析（英语一）.pdf",
    2017: "2017黄皮书真题解析（英语一）.pdf",
    2020: "2020黄皮书真题解析（英语一）.pdf",
    2021: "2021黄皮书真题解析（英语一）.pdf",
    2022: "2022黄皮书真题解析（英语一）.pdf",
}

# The target questions to inspect in ky1:
targets = [
    (2021, 3), (2021, 15),
    (2020, 7),
    (2017, 7), (2017, 11),
    (2016, 30),
    (2015, 13),
    (2014, 3), (2014, 17),
    (2013, 10), (2013, 14), (2013, 40),
    (2012, 7),
    (2011, 11),
    (2010, 40),
    (2009, 4), (2009, 8), (2009, 12),
    (2008, 4), (2008, 8), (2008, 11),
    (2007, 7),
    (2006, 4), (2006, 40),
    (2022, 30), (2022, 34)
]

print(f"Inspecting {len(targets)} duplicate questions in ky1 Yellow Books...")

for yr, qno in targets:
    fname = pdf_map.get(yr)
    if not fname:
        continue
    fp = os.path.join(pdf_dir_ky1, fname)
    doc = fitz.open(fp)
    
    # Search for lines like "3. [答案]" or "3.［答案］" or "3. \n[A]" or "3. [A]"
    found = []
    for pno in range(len(doc)):
        txt = doc[pno].get_text()
        # Look for question number pattern
        pattern = rf"(?:^|\n)\s*{qno}\.\s*(?:［?答案］?|\[A\]|［A］|[A-Z])"
        if re.search(pattern, txt) or f"\n{qno}." in txt or f"{qno}题" in txt:
            found.append(pno)
            
    print(f"\n=================== {yr} ky1 Q{qno} (Matched pages: {[p+1 for p in found[:3]]}) ===================")
    for pno in found[:2]:
        txt = doc[pno].get_text()
        lines = txt.split("\n")
        # Find where qno appears
        for i, l in enumerate(lines):
            if re.match(rf"^\s*{qno}\.", l.strip()):
                print(f"--- Page {pno+1} around line {i}: ---")
                start = max(0, i - 1)
                end = min(len(lines), i + 15)
                for j in range(start, end):
                    print(f"  {lines[j].strip()}")
                break
