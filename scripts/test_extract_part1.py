import pymupdf
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_doc(yr, cat):
    base = pdf_base_ky1 if cat == 'ky1' else pdf_base_ky2
    for f in os.listdir(base):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(base, f))
    return None

results = {}

# 1. 2009 ky1 Q43, Q44
doc09 = get_doc(2009, 'ky1')
p52 = doc09[51].get_text()
p53 = doc09[52].get_text()

# In P52, find 43.
idx_43 = p52.find("43 . 本题考核的知识点是")
idx_44 = p53.find("44 . 本题考核的知识点是")
idx_45 = p53.find("45 . 本题考核的知识点是")

q43_text = p52[idx_43:].strip() + "\n" + p53[:idx_44].strip()
q44_text = p53[idx_44:idx_45].strip()

results["2009_ky1_q43"] = q43_text
results["2009_ky1_q44"] = q44_text

# 2. 2020 ky1 Q29
doc20 = get_doc(2020, 'ky1')
p24 = doc20[23].get_text()
# Find 29. in p24
idx_29 = p24.find("29. It can be learned from Paragraphs 5 and 6 that")
idx_vi = p24.find("VI O In some ways the scientific publishing model")
q29_text = p24[idx_29:idx_vi].strip()
results["2020_ky1_q29"] = q29_text

print("Extracted 2009 Q43, Q44 and 2020 Q29 successfully.")
print("2009 Q43 len:", len(q43_text))
print("2009 Q44 len:", len(q44_text))
print("2020 Q29 len:", len(q29_text))
