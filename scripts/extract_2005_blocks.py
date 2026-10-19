import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2005年考研英语真题解析.pdf'
doc = fitz.open(pdf_path)

# Let's inspect pages where Q21-Q40 are located: pages 9 to 47
target_qs = list(range(21, 41))

for p in range(8, 48):
    blocks = doc[p].get_text("blocks")
    # sort blocks vertically then horizontally, or check each block
    for b in blocks:
        text = b[4]
        for q in target_qs:
            if text.strip().startswith(f"{q}.") or text.strip().startswith(f"{q} ."):
                print(f"=== Page {p+1} Question {q} ===")
                print(text)
                print("-" * 30)
            elif f"[{chr(65)}]" in text or "[A]" in text:
                # check if this block has options
                if any(x in text for x in ["[A]", "[B]", "[C]", "[D]", "[ A ]", "[BJ"]):
                    pass
