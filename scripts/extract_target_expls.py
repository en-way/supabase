import pymupdf
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def find_pdf(year_str):
    for f in os.listdir(pdf_base):
        if year_str in f and f.endswith(".pdf"):
            return os.path.join(pdf_base, f)
    return None

targets = [
    ("2010", 26, r'(?:26\.|\[26\]|第\s*26\s*题)'),
    ("2012", 40, r'(?:40\.|\[40\]|第\s*40\s*题)'),
    ("2020", 7,  r'(?:7\.|\[7\]|第\s*7\s*题)'),
    ("2001", 5,  r'(?:5\.|\[5\]|第\s*5\s*题)'),
    ("2008", 12, r'(?:12\.|\[12\]|第\s*12\s*题)'),
    ("2013", 10, r'(?:10\.|\[10\]|第\s*10\s*题)'),
]

for year, qnum, pat in targets:
    pdf_path = find_pdf(year)
    print(f"\n==================== {year} Q{qnum} ====================")
    if not pdf_path:
        print(f"PDF not found for {year}")
        continue
    doc = pymupdf.open(pdf_path)
    found = False
    for p in range(len(doc)):
        text = doc[p].get_text()
        # look for question number pattern
        matches = [m.start() for m in re.finditer(rf'(?:^|\n)\s*{qnum}\.\s*', text)]
        for m_start in matches:
            chunk = text[m_start:m_start+1500]
            # check if it looks like the explanation for this question
            if any(k in chunk for k in ['【答案】', '[答案]', '【解题思路】', '［解题思路］', '【试题考点】', '［考点提炼］', '【精准定位】', '考核的知识点']):
                print(f"Found on page {p+1}:")
                print(chunk[:800])
                print("-" * 50)
                found = True
                break
        if found:
            break
