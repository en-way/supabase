import fitz
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def find_q_in_pdf(fname, yr, qno):
    fp = os.path.join(pdf_dir_ky1, fname)
    doc = fitz.open(fp)
    print(f"\n=================== SEARCHING {yr} Q{qno} in {fname} ===================")
    for pno in range(len(doc)):
        txt = doc[pno].get_text()
        # Find occurrences of qno
        matches = [m.start() for m in re.finditer(rf'(?:^|\n)\s*{qno}\s*[.．、]', txt)]
        if not matches:
            # try finding [A] or similar
            matches = [m.start() for m in re.finditer(rf'{qno}题', txt)]
        for m in matches:
            snippet = txt[max(0, m - 50):min(len(txt), m + 300)]
            print(f"--- Page {pno+1} ---")
            for line in snippet.split('\n')[:15]:
                print("  ", line.strip())

find_q_in_pdf("2013黄皮书真题解析（英语一）.pdf", 2013, 40)
find_q_in_pdf("2012黄皮书真题解析（英语一）.pdf", 2012, 7)
find_q_in_pdf("2009年考研英语真题解析.pdf", 2009, 4)
find_q_in_pdf("2009年考研英语真题解析.pdf", 2009, 8)
find_q_in_pdf("2009年考研英语真题解析.pdf", 2009, 12)
find_q_in_pdf("2008年考研英语真题解析.pdf", 2008, 4)
find_q_in_pdf("2008年考研英语真题解析.pdf", 2008, 8)
find_q_in_pdf("2008年考研英语真题解析.pdf", 2008, 11)
find_q_in_pdf("2007年考研英语真题解析.pdf", 2007, 7)
