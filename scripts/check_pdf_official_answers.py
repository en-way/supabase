import fitz
import sys
import re
import os

sys.stdout.reconfigure(encoding='utf-8')

BASE_KY1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

pdf_map = {
    2001: "2001年真题解析及复习思路.pdf",
    2003: "2003年真题解析及复习思路.pdf",
    2004: "2004年考研英语真题解析.pdf",
    2008: "2008年考研英语真题解析.pdf",
    2009: "2009年考研英语真题解析.pdf",
    2010: "2010黄皮书真题解析（英语一）.pdf",
    2011: "2011黄皮书真题解析（英语一）.pdf",
    2012: "2012黄皮书真题解析（英语一）.pdf",
    2013: "2013黄皮书真题解析（英语一）.pdf",
    2016: "2016黄皮书真题解析（英语一）.pdf",
    2017: "2017黄皮书真题解析（英语一）.pdf",
    2020: "2020黄皮书真题解析（英语一）.pdf"
}

for yr, fname in pdf_map.items():
    fp = os.path.join(BASE_KY1, fname)
    if not os.path.exists(fp):
        print(f"Not found: {fp}")
        continue
    doc = fitz.open(fp)
    print(f"=== {yr} ky1 ({fname}) ===")
    
    # Check for "答案速查" or "试题答案"
    found = False
    for p in range(len(doc)-5, len(doc)):
        t = doc[p].get_text()
        if any(k in t for k in ["答案速查", "试题答案", "参考答案", "1～5", "1-5", "1~5"]):
            lines = [l.strip() for l in t.split("\n") if l.strip()]
            for l in lines:
                if any(k in l for k in ["1～5", "1-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", "1~5"]):
                    print(f"  P{p+1}: {l}")
                    found = True
    if not found:
        # Search all pages
        for p in range(len(doc)):
            t = doc[p].get_text()
            if "答案速查" in t:
                lines = [l.strip() for l in t.split("\n") if l.strip()]
                for l in lines:
                    if any(k in l for k in ["1～5", "1-5", "6-10", "11-15", "16-20", "21-25", "26-30", "31-35", "36-40", "41-45", "1~5"]):
                        print(f"  P{p+1}: {l}")
                        found = True
                break
    if not found:
        print("  (Answer table not found on end pages)")
