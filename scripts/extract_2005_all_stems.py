import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2005年考研英语真题解析.pdf')

for q in range(21, 36):
    print(f"=== Q{q} ===")
    for p in range(5, 37):
        t = doc[p].get_text()
        lines = t.splitlines()
        for i, l in enumerate(lines):
            if l.strip().startswith(f"{q}.") or l.strip().startswith(f"{q} ."):
                # print next 10 lines
                for s in lines[i:i+10]:
                    print("  ", s)
                break
