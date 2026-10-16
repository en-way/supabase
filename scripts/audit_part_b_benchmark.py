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
    
    # 1. Look for quick answer table
    found_table = False
    for p_idx, page in enumerate(reader.pages):
        txt = page.extract_text()
        if "答案速查" in txt or "真题答案" in txt or "Part B" in txt:
            # check if it has 41. or 41-45 answers
            m = re.findall(r'4[1-5]\s*[\.．、\s]\s*([A-G])', txt)
            if len(m) >= 3:
                print(f"Found answers on page {p_idx+1}: {m}")
                found_table = True
    
    # 2. Look for Part B text / explanation pages
    part_b_pages = []
    for p_idx, page in enumerate(reader.pages):
        txt = page.extract_text()
        if ("Part B" in txt or "新题型" in txt or "阅读理解B" in txt or "阅读理解 B" in txt) and any(f"{q}" in txt for q in [41, 42, 43, 44, 45]):
            part_b_pages.append(p_idx+1)
    print(f"Part B pages: {part_b_pages}")
