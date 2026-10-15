import os
import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）"

target_file = None
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if "2022" in f and ("英语（一）" in f or "英语(一)" in f or "英语一" in f) and f.endswith(".pdf"):
            target_file = os.path.join(root, f)
            break

print("Target PDF:", target_file)

reader = pypdf.PdfReader(target_file)
print("Page count:", len(reader.pages))

# Search for the quick answer table (答案速查)
found_quick_table = False
for i, page in enumerate(reader.pages):
    txt = page.extract_text()
    if "答案速查" in txt or "真题答案" in txt or "参考答案" in txt:
        print(f"\n--- Page {i+1} Answer Key ---")
        print(txt[:1500])
        found_quick_table = True

# Also search for Q26-Q30, Q40, Q41-Q45 in question text and explanations
for p_idx in [30, 31, 32, 50, 51, 52, 53, 54, 55, 56]:
    txt = reader.pages[p_idx].extract_text()
    print(f"\n==================== Page {p_idx+1} ====================")
    for line in txt.split("\n"):
        if any(marker in line for marker in ["29.", "40.", "41.", "42.", "43.", "44.", "45.", "答案", "定位", "推测", "速查"]):
            print("  ", line)
