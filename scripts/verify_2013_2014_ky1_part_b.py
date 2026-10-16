import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

def check_pdf(fname, search_terms):
    import os
    fp = os.path.join(pdf_dir, fname)
    doc = fitz.open(fp)
    print(f"\n==========================================")
    print(f"SEARCHING {fname} (pages: {len(doc)})")
    print(f"==========================================")
    for pno in range(len(doc)):
        txt = doc[pno].get_text()
        if any(t in txt for t in search_terms):
            print(f"--- Page {pno+1} ---")
            for line in txt.split("\n"):
                if any(w in line for w in ["41", "42", "43", "44", "45", "答案", "［A］", "［B］", "［C］", "［D］", "［E］", "［F］", "［G］", "[A]", "[B]", "[C]", "[D]", "[E]", "[F]", "[G]", "排序"]):
                    print("  ", line.strip()[:100])

print("Checking 2013 ky1 Part B:")
check_pdf("2013黄皮书真题解析（英语一）.pdf", ["Part B", "41.", "41题", "41题答案", "41题 答案"])

print("\nChecking 2014 ky1 Part B:")
check_pdf("2014黄皮书真题解析（英语一）.pdf", ["Part B", "41.", "41题", "41题答案", "41题 答案"])
