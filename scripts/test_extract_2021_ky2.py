import pymupdf
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"
target = None
for f in os.listdir(pdf_base_ky2):
    if "2021" in f and f.endswith(".pdf"):
        target = os.path.join(pdf_base_ky2, f)
        break

doc = pymupdf.open(target)

# P11: Q21
p11 = doc[10].get_text()
# Find 21. Research by...
idx21 = p11.find("21. Research by the World Economic Forum")
# In p11, find where Roman numeral II begins (next section)
idx_ii = p11.find("U ❶ The question of who should pay for reskilling")
if idx_ii == -1: idx_ii = p11.find("The question of who should pay")
print("2021 ky2 Q21 chunk:")
print(p11[idx21:idx_ii].strip())
print("="*50)

# P14: Q23
p14 = doc[13].get_text()
idx23 = p14.find("23.为解决技能不匹配问题")
# In p14, find where Roman numeral III begins
idx_iii = p14.find("With the pandemic")
if idx_iii == -1: idx_iii = p14.find("皿❶With the pandemic")
print("2021 ky2 Q23 chunk:")
print(p14[idx23:idx_iii].strip())
print("="*50)

# P15: Q24
p15 = doc[14].get_text()
idx24 = p15.find("24. We can learn from Paragraph 3")
# In p15, find page number or next section
idx_end24 = p15.find("IV ❶")
if idx_end24 == -1: idx_end24 = p15.find("15\n")
print("2021 ky2 Q24 chunk:")
print(p15[idx24:idx_end24].strip())
print("="*50)

# P17: Q25
p17 = doc[16].get_text()
idx25 = p17.find("25.北欧航空公司决定")
idx_end25 = p17.find("17\n")
print("2021 ky2 Q25 chunk:")
print(p17[idx25:idx_end25].strip())
print("="*50)
