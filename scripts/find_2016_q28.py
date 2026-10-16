import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2016黄皮书真题解析（英语一）.pdf")
for pno in [25, 26, 27, 28]:
    print(f"=== Page {pno+1} ===")
    txt = doc[pno].get_text()
    for l in txt.split("\n"):
        if any(w in l for w in ["27", "28", "29", "inferred", "Paragraph 3"]):
            print("  ", l.strip()[:80])
