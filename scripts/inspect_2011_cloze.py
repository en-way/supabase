import json
import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Inspect 2011 ky1 in DB
with open("public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json", "r", encoding="utf-8") as f:
    d = json.load(f)

print("=== 2011 ky1 Cloze in DB ===")
for q in d.get("questions", [])[:20]:
    so = q.get("sort_order")
    print(f"Q{so}: ans={q.get('correct_answer')}, opts={[o['text'] for o in q.get('options', [])]}")

print("\n=== 2011 ky1 in HuangPiShu PDF ===")
pdf_base = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
for f in os.listdir(pdf_base):
    if "2011" in f and f.endswith(".pdf"):
        doc = pymupdf.open(os.path.join(pdf_base, f))
        for p in range(1, 8):
            t = doc[p].get_text()
            lines = t.split('\n')
            for l in lines:
                if any(l.strip().startswith(f"{i}.") for i in range(1, 21)):
                    print(f"P{p+1}: {l.strip()[:80]}")
