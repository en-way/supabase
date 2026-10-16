import pypdf
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

pdf_files = {
    2016: "2016黄皮书真题解析（英语一）.pdf",
    2017: "2017黄皮书真题解析（英语一）.pdf",
    2018: "2018黄皮书真题解析（英语一）.pdf",
    2019: "2019黄皮书真题解析（英语一）.pdf",
    2020: "2020黄皮书真题解析（英语一）.pdf",
    2021: "2021黄皮书真题解析（英语一）.pdf",
    2022: "2022黄皮书真题解析（英语一）.pdf",
}

for year, fname in pdf_files.items():
    fp = os.path.join(pdf_dir, fname)
    reader = pypdf.PdfReader(fp)
    print(f"\n==========================================")
    print(f"YEAR {year}: {fname} (pages: {len(reader.pages)})")
    print(f"==========================================")
    
    # Locate pages with Part B (between reading A and translation)
    # Translation usually has 46, 47, 48, 49, 50. Part B has 41, 42, 43, 44, 45.
    matched_pages = []
    for i, page in enumerate(reader.pages):
        txt = page.extract_text() or ""
        # Check if page has discussion of 41-45
        has_41_45 = any(re.search(rf'[\(（\[【]{q}[\)）\]】]|(?:^|\n)\s*{q}\s*[\.、\s]|(?:题|空)\s*{q}', txt) for q in [41, 42, 43, 44, 45])
        # Check if page is before translation (46-50)
        has_trans = "46" in txt and "47" in txt and "48" in txt and "49" in txt and "50" in txt
        if has_41_45 and not has_trans:
            matched_pages.append(i + 1)
            
    print(f"Matched Part B pages: {matched_pages}")
    for pno in matched_pages:
        txt = reader.pages[pno - 1].extract_text()
        print(f"\n--- Page {pno} ---")
        lines = [line.strip() for line in txt.split("\n") if line.strip()]
        for line in lines:
            if any(k in line for k in ["41", "42", "43", "44", "45", "答案", "［A］", "[A]", "［B］", "[B]", "［C］", "[C]", "［D］", "[D]", "［E］", "[E]", "［F］", "[F]", "［G］", "[G]"]):
                print("  ", line[:100])
