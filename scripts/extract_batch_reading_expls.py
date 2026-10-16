import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_pdf(yr, cat):
    base = pdf_base_ky1 if cat == 'ky1' else pdf_base_ky2
    for f in os.listdir(base):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(base, f))
    return None

def extract_target(yr, cat, p_start, p_end, q_label):
    doc = get_pdf(yr, cat)
    print(f"\n==================== {yr} {cat} {q_label} (Pages {p_start}-{p_end}) ====================")
    text = ""
    for p in range(p_start - 1, min(p_end, len(doc))):
        text += f"\n--- Page {p+1} ---\n" + doc[p].get_text()
    return text

# 1. 2017 ky1 Q38 (Pages 44-46)
t_2017_q38 = extract_target(2017, 'ky1', 44, 46, "Q38")
print(t_2017_q38[:1200])

# 2. 2016 ky1 Q44, Q45 (Page 57-58)
t_2016_q44_45 = extract_target(2016, 'ky1', 56, 58, "Q44-45")
print(t_2016_q44_45[:1200])

# 3. 2021 ky2 Q21, Q23, Q24, Q25 (Pages 11-18)
t_2021_ky2 = extract_target(2021, 'ky2', 11, 17, "Q21-25")
print(t_2021_ky2[:1200])
