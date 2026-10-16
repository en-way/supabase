import pymupdf
import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

pdf_base_ky1 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）"
pdf_base_ky2 = r"c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语二真题解析（2001-2025）"

def get_doc(yr, cat):
    base = pdf_base_ky1 if cat == 'ky1' else pdf_base_ky2
    for f in os.listdir(base):
        if str(yr) in f and f.endswith(".pdf"):
            return pymupdf.open(os.path.join(base, f))
    return None

updates = {}

# Load existing base extractions (2017 Q38, 2016 Q45, 2002 Q30, 2010 Q25)
with open('scripts/round13_base_extracted.json', 'r', encoding='utf-8') as f:
    base_data = json.load(f)

for k, v in base_data.items():
    updates[k] = v

# 1. 2009 ky1 Q43 & Q44
doc09 = get_doc(2009, 'ky1')
p52 = doc09[51].get_text()
p53 = doc09[52].get_text()
idx_43 = p52.find("43 . 本题考核的知识点是")
idx_44 = p53.find("44 . 本题考核的知识点是")
idx_45 = p53.find("45 . 本题考核的知识点是")
q43_text = p52[idx_43:].strip() + "\n" + p53[:idx_44].strip()
q44_text = p53[idx_44:idx_45].strip()
updates["2009_ky1_q43"] = {"explanation": q43_text}
updates["2009_ky1_q44"] = {"explanation": q44_text}

# 2. 2020 ky1 Q29
doc20 = get_doc(2020, 'ky1')
p24 = doc20[23].get_text()
idx_29 = p24.find("29. It can be learned from Paragraphs 5 and 6 that")
idx_vi = p24.find("VI O In some ways the scientific publishing model")
q29_text = p24[idx_29:idx_vi].strip()
updates["2020_ky1_q29"] = {"explanation": q29_text}

# 3. 2021 ky2 Q21, Q23, Q24, Q25
doc21_2 = get_doc(2021, 'ky2')
p11 = doc21_2[10].get_text()
idx21 = p11.find("21. Research by the World Economic Forum")
idx_ii = p11.find("The question of who should pay")
if idx_ii == -1: idx_ii = p11.find("U ❶")
q21_text = p11[idx21:idx_ii].strip()
updates["2021_ky2_q21"] = {"explanation": q21_text}

p14 = doc21_2[13].get_text()
idx23 = p14.find("23. Efforts to resolve the skills mismatch")
if idx23 == -1: idx23 = p14.find("23.为解决技能不匹配问题")
idx_iii = p14.find("With the pandemic")
if idx_iii == -1: idx_iii = p14.find("皿❶")
q23_text = p14[idx23:idx_iii].strip()
updates["2021_ky2_q23"] = {"explanation": q23_text}

p15 = doc21_2[14].get_text()
idx24 = p15.find("24. We can learn from Paragraph 3")
idx_end24 = p15.find("IV ❶")
if idx_end24 == -1: idx_end24 = p15.rfind("15")
q24_text = p15[idx24:idx_end24].strip()
updates["2021_ky2_q24"] = {"explanation": q24_text}

p17 = doc21_2[16].get_text()
idx25 = p17.find("25. Scandinavian Airlines decided to")
if idx25 == -1: idx25 = p17.find("25.北欧航空公司决定")
idx_end25 = p17.rfind("17")
q25_text = p17[idx25:idx_end25].strip()
updates["2021_ky2_q25"] = {"explanation": q25_text}

# 4. 2022 ky1 Q27, Q32, Q36, Q37, Q38, Q39
doc22_1 = get_doc(2022, 'ky1')
# Q27: P28
p28 = doc22_1[27].get_text()
idx27 = p28.find("27・ The percentage of UK graduates")
if idx27 == -1: idx27 = p28.find("27. The percentage of UK graduates")
idx_end27 = p28.find("III ❶")
if idx_end27 == -1: idx_end27 = p28.rfind("28")
q27_text = p28[idx27:idx_end27].strip()
updates["2022_ky1_q27"] = {"explanation": q27_text}

# Q32: P37
p37 = doc22_1[36].get_text()
idx32 = p37.find("32. The reworked version of The Four Seasons")
if idx32 == -1: idx32 = p37.find("32.文中提到《四季》的改编版本")
idx_end32 = p37.find("IV ❶")
if idx_end32 == -1: idx_end32 = p37.rfind("37")
q32_text = p37[idx32:idx_end32].strip()
updates["2022_ky1_q32"] = {"explanation": q32_text}

# Q36: P45
p45 = doc22_1[44].get_text()
idx36 = p45.find("36. The personal grievance provisions")
if idx36 == -1: idx36 = p45.find("36. ERA的个人申诉条款旨在")
idx_end36 = p45.rfind("45")
q36_text = p45[idx36:idx_end36].strip()
updates["2022_ky1_q36"] = {"explanation": q36_text}

# Q37: P46-47
p46 = doc22_1[45].get_text()
p47 = doc22_1[46].get_text()
idx37 = p46.find("37. It can be learned from Paragraph 3")
idx_end37 = p47.find("V ❶")
if idx_end37 == -1: idx_end37 = p47.rfind("47")
q37_text = p46[idx37:].strip() + "\n" + p47[:idx_end37].strip()
updates["2022_ky1_q37"] = {"explanation": q37_text}

# Q38: P48
p48 = doc22_1[47].get_text()
idx38 = p48.find("38. Which of the following measures would")
if idx38 == -1: idx38 = p48.find("3& Which of the following measures would")
if idx38 == -1: idx38 = p48.find("38.新西兰生产力委员会可能会支持")
if idx38 == -1: idx38 = p48.find("3&生产力委员会会支持")
idx_end38 = p48.rfind("48")
q38_text = p48[idx38:idx_end38].strip()
q38_text = q38_text.replace("3& Which", "38. Which").replace("3&生产力", "38.生产力")
updates["2022_ky1_q38"] = {"explanation": q38_text}

# Q39: P50
p50 = doc22_1[49].get_text()
idx39 = p50.find("39. What might be an effect of ERA")
idx_end39 = p50.rfind("50")
q39_text = p50[idx39:idx_end39].strip()
updates["2022_ky1_q39"] = {"explanation": q39_text}

# 5. 2022 ky2 Q21, Q22, Q23, Q24, Q26, Q27, Q28, Q29
doc22_2 = get_doc(2022, 'ky2')
# Q21: P11-12
p11 = doc22_2[10].get_text()
p12 = doc22_2[11].get_text()
idx21 = p11.find("21. The climate-friendly eggs are produced")
if idx21 == -1: idx21 = p11.find("21.气候友好型鸡蛋是")
idx_end21 = p12.find("■❶")
if idx_end21 == -1: idx_end21 = p12.find("I'm excited about our progress")
q21_ky2_22 = p11[idx21:].strip() + "\n" + p12[:idx_end21].strip()
updates["2022_ky2_q21"] = {"explanation": q21_ky2_22}

# Q22: P13
p13 = doc22_2[12].get_text()
idx22 = p13.find("22. Larry Brown is excited about his progress in")
if idx22 == -1: idx22 = p13.find("22.拉里•布朗对他在")
idx_end22 = p13.rfind("13")
q22_ky2_22 = p13[idx22:idx_end22].strip()
updates["2022_ky2_q22"] = {"explanation": q22_ky2_22}

# Q23: P15
p15 = doc22_2[14].get_text()
idx23 = p15.find("23 ・ The example of organic eggs")
if idx23 == -1: idx23 = p15.find("23. The example of organic eggs")
idx_end23 = p15.rfind("15")
q23_ky2_22 = p15[idx23:idx_end23].strip()
updates["2022_ky2_q23"] = {"explanation": q23_ky2_22}

# Q24: P18
p18 = doc22_2[17].get_text()
idx24 = p18.find("24. It can be learned from the last paragraph")
idx_end24 = p18.find("25・ John Brunnquell")
if idx_end24 == -1: idx_end24 = p18.find("25. John Brunnquell")
q24_ky2_22 = p18[idx24:idx_end24].strip()
updates["2022_ky2_q24"] = {"explanation": q24_ky2_22}

# Q26: P21
p21 = doc22_2[20].get_text()
idx26 = p21.find("26. The survey conducted by Harris Poll")
idx_end26 = p21.find("III ❶")
if idx_end26 == -1: idx_end26 = p21.rfind("21")
q26_ky2_22 = p21[idx26:idx_end26].strip()
updates["2022_ky2_q26"] = {"explanation": q26_ky2_22}

# Q27: P23
p23 = doc22_2[22].get_text()
idx27 = p23.find("27. It can be inferred from Paragraph 3")
idx_end27 = p23.find("V ❶")
if idx_end27 == -1: idx_end27 = p23.rfind("23")
q27_ky2_22 = p23[idx27:idx_end27].strip()
updates["2022_ky2_q27"] = {"explanation": q27_ky2_22}

# Q28: P24-25
p24 = doc22_2[23].get_text()
p25 = doc22_2[24].get_text()
idx28 = p24.find("28・ Retirement patterns are changing partly due to")
if idx28 == -1: idx28 = p24.find("28. Retirement patterns are changing partly due to")
if idx28 == -1: idx28 = p24.find("28.退休模式正在发生变化")
idx_end28_p25 = p25.find("VI O Because of longer life spans")
if idx_end28_p25 == -1: idx_end28_p25 = p25.find("VI ❶")
q28_ky2_22 = p24[idx28:].strip() + "\n" + p25[:idx_end28_p25].strip()
updates["2022_ky2_q28"] = {"explanation": q28_ky2_22}

# Q29: P26
p26 = doc22_2[25].get_text()
idx29 = p26.find("29. Many \"unretirees\" are increasing their savings")
if idx29 == -1: idx29 = p26.find("29.许多“不退休者\"通过")
idx_end29 = p26.find("Vtt ❶")
if idx_end29 == -1: idx_end29 = p26.find("Unfortunately")
q29_ky2_22 = p26[idx29:idx_end29].strip()
updates["2022_ky2_q29"] = {"explanation": q29_ky2_22}

with open('scripts/round13_all_calibrated.json', 'w', encoding='utf-8') as f:
    json.dump(updates, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(updates)} calibrated updates in scripts/round13_all_calibrated.json")
for k, v in updates.items():
    print(f"  {k}: {len(v.get('explanation', ''))} chars")
