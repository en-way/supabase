import pypdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"

pdf_files = {
    2016: "2016黄皮书真题解析（英语一）.pdf",
    2017: "2017黄皮书真题解析（英语一）.pdf",
    2018: "2018黄皮书真题解析（英语一）.pdf",
    2019: "2019黄皮书真题解析（英语一）.pdf",
    2020: "2020黄皮书真题解析（英语一）.pdf",
}

for year, fname in pdf_files.items():
    fp = os.path.join(pdf_dir, fname)
    reader = pypdf.PdfReader(fp)
    print(f"\n==========================================")
    print(f"YEAR {year}: {fname} (pages: {len(reader.pages)})")
    # Scan pages 40 to 65
    for p_idx in range(35, min(65, len(reader.pages))):
        txt = reader.pages[p_idx].extract_text() or ""
        # Check if there is 41
        if any(marker in txt for marker in ["41.", "41题", "41 答案", "41.答案", "【41】", "[41]", "(41)", "41-45"]):
            print(f"Year {year} Page {p_idx+1} matched:")
            for line in txt.split("\n"):
                if any(m in line for m in ["41", "42", "43", "44", "45", "答案", "排序", "试题精解", "真题精解", "【解析】", "[A]", "[B]", "[C]", "[D]", "[E]", "[F]", "[G]", "［A］", "［B］", "［C］", "［D］", "［E］", "［F］", "［G］"]):
                    print("  ", line.strip()[:100])
