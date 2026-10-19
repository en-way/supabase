import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2005年考研英语真题解析.pdf'
doc = fitz.open(pdf_path)

# Let's inspect pages where Q21-Q40 are located: pages 6 to 47
target_qs = list(range(21, 41))

for q in target_qs:
    print(f"\n==================== QUESTION {q} ====================")
    found = False
    for p in range(5, 48):
        text = doc[p].get_text()
        lines = text.splitlines()
        for i, l in enumerate(lines):
            ls = l.strip()
            # match "21. " or "21 ."
            if ls.startswith(f"{q}.") or ls.startswith(f"{q} .") or ls.startswith(f"{q}．"):
                print(f"Page {p+1}:")
                # print the next 20 lines
                sub = lines[i:min(len(lines), i+25)]
                for s in sub:
                    print("  ", s)
                found = True
                break
        if found:
            break
