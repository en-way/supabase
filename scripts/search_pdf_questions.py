import fitz
import sys
import re
import os

sys.stdout.reconfigure(encoding='utf-8')

BASE_KY1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def search_in_pdf(pdf_name, q_str, max_pages=15):
    fp = os.path.join(BASE_KY1, pdf_name)
    doc = fitz.open(fp)
    print(f"\n==================== {pdf_name} : {q_str} ====================")
    for p in range(min(max_pages, len(doc))):
        t = doc[p].get_text()
        if q_str in t:
            idx = t.find(q_str)
            print(f"--- Page {p+1} ---")
            print(t[max(0, idx-50):min(len(t), idx+400)])
            return

# 1. 2016 Q1
search_in_pdf("2016黄皮书真题解析（英语一）.pdf", "1. [A")

# 2. 2017 Q14
search_in_pdf("2017黄皮书真题解析（英语一）.pdf", "14. [A")

# 3. 2020 Q7
search_in_pdf("2020黄皮书真题解析（英语一）.pdf", "7. [A", max_pages=12)
search_in_pdf("2020黄皮书真题解析（英语一）.pdf", "7. ［A", max_pages=12)

# 4. 2010 Q26
search_in_pdf("2010黄皮书真题解析（英语一）.pdf", "26.", max_pages=35)

# 5. 2001 Q5
search_in_pdf("2001年真题解析及复习思路.pdf", "5.", max_pages=15)
