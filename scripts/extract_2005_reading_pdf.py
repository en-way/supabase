import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2005年考研英语真题解析.pdf'
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")

for p in range(len(doc)):
    text = doc[p].get_text()
    for q in range(21, 41):
        if f"{q}." in text or f"{q} ." in text:
            # check if it's the question stem
            lines = text.splitlines()
            for i, line in enumerate(lines):
                if line.strip().startswith(f"{q}.") or line.strip().startswith(f"{q} ."):
                    print(f"--- 2005 Page {p+1} Q{q} ---")
                    # print next 25 lines
                    print("\n".join(lines[max(0, i-2):min(len(lines), i+30)]))
                    print("="*40)
                    break
