import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')
pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def find_q_text(fname, p_start, p_end, target_q):
    import os
    doc = fitz.open(os.path.join(pdf_dir, fname))
    for p in range(p_start-1, min(p_end, len(doc))):
        txt = doc[p].get_text()
        for i, line in enumerate(txt.split('\n')):
            if any(line.strip().startswith(f"{q}.") or line.strip().startswith(f"{q}．") or line.strip().startswith(f"{q} ") for q in target_q):
                print(f"=== {fname} Page {p+1} ===")
                lines = txt.split('\n')
                for j in range(max(0, i-1), min(len(lines), i+15)):
                    print("  ", lines[j].strip())

print("2012 Q7:")
find_q_text("2012黄皮书真题解析（英语一）.pdf", 1, 10, [6, 7, 8])

print("\n2008 Q4, Q11:")
find_q_text("2008年考研英语真题解析.pdf", 1, 8, [3, 4, 5, 10, 11, 12])

print("\n2009 Q4, Q8, Q12:")
find_q_text("2009年考研英语真题解析.pdf", 1, 8, [3, 4, 5, 7, 8, 9, 11, 12, 13])
