# -*- coding: utf-8 -*-
"""
calibrate_round19.py
Round 19 Calibration Script:
1. 2014 ky1 Text 3: Remove '[432 words]', restore complete paragraph 5
2. 2021 ky2 Cloze: Fix missing period and restore clean paragraph 6
3. 2019 ky1 Text 1: Remove leaked Text 2 opening fragment
4. 2019 ky1 Text 2: Restore authentic opening paragraph
5. 2019 ky1 Text 4: Restore missing clause, remove 'f,' and fix quotes
6. 2022 ky2 Text 3: Remove leaked question stems at the end of the passage
7. 2008 ky1 Text 3: Fix OCR typos 'ba 1;ketball', 'mil itary', restore missing text and remove ' [,'
8. 2010 ky2 Part B: Clean stray apostrophe in quote ',"’'
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public', 'data', 'exams'))

# 1. 2014 ky1 (240cc48a-439b-5d27-8464-f7dc53e060dc.json) Text 3 (sort_order = 4)
f_2014 = os.path.join(exams_dir, '240cc48a-439b-5d27-8464-f7dc53e060dc.json')
d_2014 = json.load(open(f_2014, encoding='utf-8'))
for p in d_2014['passages']:
    if p['sort_order'] == 4:
        c = p['content']
        # replace the last paragraph
        old_part = "As much as some scientists may complain about the new awards"
        idx = c.find(old_part)
        if idx != -1:
            clean_last_para = (
                "As much as some scientists may complain about the new awards, two things seem clear. "
                "First, most researchers would accept such a prize if they were offered one. "
                "Second, it is surely a good thing that the money and attention come to science rather than go elsewhere. "
                "It is fair to criticize and question the mechanism — that is the culture of research, after all - "
                "but it is the prize-givers' money to do with as they please. "
                "It is wise to take such gifts with gratitude and grace."
            )
            p['content'] = c[:idx] + clean_last_para
            print("Calibrated 2014 ky1 Text 3 (removed '[432 words]' and restored complete paragraph 5)")
json.dump(d_2014, open(f_2014, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 2. 2021 ky2 (4ebd819e-c832-5890-9048-ba16040a5607.json) Cloze (sort_order = 1)
f_2021_ky2 = os.path.join(exams_dir, '4ebd819e-c832-5890-9048-ba16040a5607.json')
d_2021_ky2 = json.load(open(f_2021_ky2, encoding='utf-8'))
for p in d_2021_ky2['passages']:
    if p['sort_order'] == 1:
        c = p['content']
        if c.endswith("better [20] the objective"):
            p['content'] = c + "."
            print("Calibrated 2021 ky2 Cloze (added missing period at end)")
json.dump(d_2021_ky2, open(f_2021_ky2, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 3 & 4 & 5. 2019 ky1 (5bcba462-0a1e-59b2-9fcb-c171d242db3b.json) Text 1, Text 2, Text 4
f_2019_ky1 = os.path.join(exams_dir, '5bcba462-0a1e-59b2-9fcb-c171d242db3b.json')
d_2019_ky1 = json.load(open(f_2019_ky1, encoding='utf-8'))
for p in d_2019_ky1['passages']:
    so = p['sort_order']
    if so == 2: # Text 1
        c = p['content']
        # remove leaked Text 2 fragment
        leak = "Grade inflation the gradual increase in average GPAs"
        idx = c.find(leak)
        if idx != -1:
            p['content'] = c[:idx].strip()
            print("Calibrated 2019 ky1 Text 1 (removed leaked Text 2 opening fragment)")
    elif so == 3: # Text 2
        c = p['content']
        # restore authentic paragraph 1
        old_corrupt = "Grade inflation the gradual increase in average GPAs (grade-point averages) over the past era in higher education, in which students are treated like policy often buried deep in course catalogs called \" grade"
        authentic_para1 = (
            "Grade inflation—the gradual increase in average GPAs (grade-point averages) over the past few decades—is "
            "often considered a product of a consumer era in higher education, in which students are treated like "
            "customers to be pleased. But another, related force—a policy often buried deep in course catalogs called "
            "\"grade forgiveness\"—is helping raise GPAs."
        )
        if old_corrupt in c:
            p['content'] = c.replace(old_corrupt, authentic_para1)
            print("Calibrated 2019 ky1 Text 2 (restored authentic paragraph 1)")
    elif so == 5: # Text 4
        c = p['content']
        # fix corrupted paragraph 7
        old_corrupt_text4 = "Those retailers laws. O The Small Business & Entrepreneurship Council advocacy group said in a statement, uSmall businesses and internet entrepreneurs are not well served at all by this decision. f,"
        authentic_text4_end = (
            "Those retailers may face headaches complying with various state sales tax laws. "
            "The Small Business & Entrepreneurship Council advocacy group said in a statement, "
            "\"Small businesses and internet entrepreneurs are not well served at all by this decision.\""
        )
        if old_corrupt_text4 in c:
            p['content'] = c.replace(old_corrupt_text4, authentic_text4_end)
            print("Calibrated 2019 ky1 Text 4 (restored missing clause and fixed OCR quotes/junk)")
json.dump(d_2019_ky1, open(f_2019_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 6. 2022 ky2 (cc4bf627-e456-538f-87e2-4a99ebb613ed.json) Text 3 (sort_order = 4)
f_2022_ky2 = os.path.join(exams_dir, 'cc4bf627-e456-538f-87e2-4a99ebb613ed.json')
d_2022_ky2 = json.load(open(f_2022_ky2, encoding='utf-8'))
for p in d_2022_ky2['passages']:
    if p['sort_order'] == 4:
        c = p['content']
        leak = ".. According to the last paragraph"
        idx = c.find(leak)
        if idx != -1:
            p['content'] = c[:idx].strip()
            print("Calibrated 2022 ky2 Text 3 (removed leaked question stems from passage end)")
json.dump(d_2022_ky2, open(f_2022_ky2, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 7. 2008 ky1 (d80926ab-1841-5d1f-a999-56773986c46d.json) Text 3 (sort_order = 4)
f_2008_ky1 = os.path.join(exams_dir, 'd80926ab-1841-5d1f-a999-56773986c46d.json')
d_2008_ky1 = json.load(open(f_2008_ky1, encoding='utf-8'))
for p in d_2008_ky1['passages']:
    if p['sort_order'] == 4:
        c = p['content']
        # replace corrupted paragraph 5
        old_corrupt_08 = "ba 1;ketball, the length of mil itary need to predict human height in the near future to design a piece of equipment, Gordon says that by and large,“you could use today’s data and feel fairly confident. ” [,"
        authentic_para_08 = "basketball, the length of military uniforms has not changed for some time. And if you need to predict human height in the near future to design a piece of equipment, Gordon says that by and large, \"you could use today's data and feel fairly confident.\""
        if old_corrupt_08 in c:
            p['content'] = c.replace(old_corrupt_08, authentic_para_08)
            print("Calibrated 2008 ky1 Text 3 (fixed OCR corruption in paragraph 5 and stripped ' [,')")
json.dump(d_2008_ky1, open(f_2008_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 8. 2010 ky2 (207d2963-734a-52bd-9fa3-6c341efb5974.json) Part B (sort_order = 6)
f_2010_ky2 = os.path.join(exams_dir, '207d2963-734a-52bd-9fa3-6c341efb5974.json')
d_2010_ky2 = json.load(open(f_2010_ky2, encoding='utf-8'))
for p in d_2010_ky2['passages']:
    if p['sort_order'] == 6:
        c = p['content']
        if ',"’' in c:
            p['content'] = c.replace(',"’', ',"')
            print("Calibrated 2010 ky2 Part B (cleaned stray apostrophe in quote)")
json.dump(d_2010_ky2, open(f_2010_ky2, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("\n=== All Round 19 Calibrations Successfully Applied! ===")
