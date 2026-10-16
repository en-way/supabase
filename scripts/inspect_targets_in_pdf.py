import fitz
import sys
import re
import os
import json
import glob

sys.stdout.reconfigure(encoding='utf-8')

BASE_KY1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

targets = [
    (2004, 8, "2004年考研英语真题解析.pdf", "8."),
    (2011, 3, "2011黄皮书真题解析（英语一）.pdf", "3."),
    (2011, 7, "2011黄皮书真题解析（英语一）.pdf", "7."),
    (2011, 11, "2011黄皮书真题解析（英语一）.pdf", "11."),
    (2011, 40, "2011黄皮书真题解析（英语一）.pdf", "40."),
    (2013, 2, "2013黄皮书真题解析（英语一）.pdf", "2."),
    (2013, 10, "2013黄皮书真题解析（英语一）.pdf", "10."),
    (2003, 25, "2003年真题解析及复习思路.pdf", "25."),
    (2009, 11, "2009年考研英语真题解析.pdf", "11."),
    (2012, 40, "2012黄皮书真题解析（英语一）.pdf", "40."),
    (2008, 12, "2008年考研英语真题解析.pdf", "12.")
]

for yr, qnum, fname, pat in targets:
    fp = os.path.join(BASE_KY1, fname)
    doc = fitz.open(fp)
    print(f"\n==================== {yr} ky1 Q{qnum} in {fname} ====================")
    
    # Get DB current state
    for ep in glob.glob("public/data/exams/*.json"):
        with open(ep, "r", encoding="utf-8") as f:
            d = json.load(f)
        if d.get("exam", {}).get("category_id") == "ky1" and d.get("exam", {}).get("year") == yr:
            for q in d.get("questions", []):
                if q.get("sort_order") == qnum:
                    print(f"DB correct_answer: {q.get('correct_answer')}")
                    print(f"DB options: {[(o['key'], o['text']) for o in q.get('options', [])]}")
                    print(f"DB stem: {q.get('stem')}")
                    print(f"DB explanation snippet: {(q.get('explanation') or '')[:120]}")
                    break
    
    # Search in PDF
    for p in range(len(doc)):
        t = doc[p].get_text()
        # Look for question marker
        m = re.search(rf'(?:^|\n)\s*{qnum}\s*[\.、]\s*', t)
        if m:
            print(f"--- Found on Page {p+1} in PDF ---")
            idx = m.start()
            print(t[idx:idx+400])
            break
