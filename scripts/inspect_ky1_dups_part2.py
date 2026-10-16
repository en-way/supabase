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
    2016: "2016黄皮书真题解析（英语一）.pdf",
    2022: "2022黄皮书真题解析（英语一）.pdf",
}

targets = [
    (2016, 30),
    (2022, 30), (2022, 34),
    (2013, 10), (2013, 14), (2013, 40),
    (2012, 7),
    (2011, 11),
    (2010, 40),
    (2009, 4), (2009, 8), (2009, 12),
    (2008, 4), (2008, 8), (2008, 11),
    (2007, 7),
    (2006, 4), (2006, 40),
]

for yr, qno in targets:
    fname = pdf_map.get(yr)
    if not fname:
        continue
    fp = os.path.join(pdf_dir_ky1, fname)
    doc = fitz.open(fp)
    
    print(f"\n=================== {yr} ky1 Q{qno} ===================")
    found_lines = []
    for pno in range(len(doc)):
        txt = doc[pno].get_text()
        lines = txt.split("\n")
        for i, l in enumerate(lines):
            # match line starting with qno. e.g. "30." or "30. [A]" or "30.［答案］"
            if re.match(rf"^\s*{qno}\.\s*(?:\[A\]|［A］|\[考点|［考点|\[答案|［答案|[A-Z]|In|The|According|Which|What|It)", l.strip()):
                print(f"--- Page {pno+1}: ---")
                start = max(0, i - 1)
                end = min(len(lines), i + 20)
                for j in range(start, end):
                    print(f"  {lines[j].strip()}")
                break
