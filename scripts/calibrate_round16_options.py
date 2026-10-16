# -*- coding: utf-8 -*-
"""
calibrate_round16_options.py
Round 16 Calibration Script:
Restore official yellow book options, correct answers, stems and explanations for:
1. 2017 ky1 Q39 & Q40
2. 2006 ky1 Q20
3. 2008 ky1 Q20
4. 2020 ky1 Q23, Q25, Q28
5. 2018 ky1 Q24, Q27, Q30, Q34, Q40
6. 2002 ky1 Q31, Q32, Q38
7. 2010 ky1 Q27
8. 2021 ky1 Q24
9. 2022 ky2 Q32, Q38, Q40 and Cloze (Q1-Q20 explanations)
10. 2012 ky1 Q33, Q35
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2017 ky1 Q39 & Q40
f_2017_ky1 = 'public/data/exams/4fd42872-4822-5786-8d16-0317051bf03d.json'
d_2017_ky1 = json.load(open(f_2017_ky1, encoding='utf-8'))
for q in d_2017_ky1['questions']:
    so = q['sort_order']
    if so == 39:
        q['stem'] = "Well-enforced laws in government transparency are needed to ________."
        q['options'] = [
            {"key": "A", "text": "awaken the conscience of officials", "value": "A"},
            {"key": "B", "text": "guarantee fair play in official access", "value": "B"},
            {"key": "C", "text": "allow for certain kinds of lobbying", "value": "C"},
            {"key": "D", "text": "inspire hopes in average people", "value": "D"}
        ]
        q['correct_answer'] = "B"
        expl = q.get('explanation', '')
        if "VH ❶ Favoritism" in expl:
            idx = expl.find("VH ❶ Favoritism")
            q['explanation'] = expl[:idx].strip()
        print("Calibrated 2017 ky1 Q39")
    elif so == 40:
        q['stem'] = "The author's attitude toward the court's ruling is ________."
        q['options'] = [
            {"key": "A", "text": "sarcastic", "value": "A"},
            {"key": "B", "text": "tolerant", "value": "B"},
            {"key": "C", "text": "skeptical", "value": "C"},
            {"key": "D", "text": "supportive", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2017 ky1 Q40")
json.dump(d_2017_ky1, open(f_2017_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 2. 2006 ky1 Q20
f_2006_ky1 = 'public/data/exams/c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json'
d_2006_ky1 = json.load(open(f_2006_ky1, encoding='utf-8'))
for q in d_2006_ky1['questions']:
    if q['sort_order'] == 20:
        q['options'] = [
            {"key": "A", "text": "supervision", "value": "A"},
            {"key": "B", "text": "manipulation", "value": "B"},
            {"key": "C", "text": "regulation", "value": "C"},
            {"key": "D", "text": "coordination", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2006 ky1 Q20")
json.dump(d_2006_ky1, open(f_2006_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 3. 2008 ky1 Q20
f_2008_ky1 = 'public/data/exams/d80926ab-1841-5d1f-a999-56773986c46d.json'
d_2008_ky1 = json.load(open(f_2008_ky1, encoding='utf-8'))
for q in d_2008_ky1['questions']:
    if q['sort_order'] == 20:
        q['options'] = [
            {"key": "A", "text": "paradoxical", "value": "A"},
            {"key": "B", "text": "incompatible", "value": "B"},
            {"key": "C", "text": "inevitable", "value": "C"},
            {"key": "D", "text": "continuous", "value": "D"}
        ]
        q['correct_answer'] = "A"
        print("Calibrated 2008 ky1 Q20")
json.dump(d_2008_ky1, open(f_2008_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 4. 2020 ky1 Q23, Q25, Q28
f_2020_ky1 = 'public/data/exams/f56943c1-0ba8-58fe-b7d3-061352345067.json'
d_2020_ky1 = json.load(open(f_2020_ky1, encoding='utf-8'))
for q in d_2020_ky1['questions']:
    so = q['sort_order']
    if so == 23:
        q['stem'] = "The author suggests that a title holder is successful only if it ________."
        q['options'] = [
            {"key": "A", "text": "endeavours to maintain its image", "value": "A"},
            {"key": "B", "text": "meets the aspiration of its people", "value": "B"},
            {"key": "C", "text": "brings its local arts to prominence", "value": "C"},
            {"key": "D", "text": "commits to its long-term growth", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2020 ky1 Q23")
    elif so == 25:
        q['stem'] = "What is the author's attitude towards the proposal?"
        q['options'] = [
            {"key": "A", "text": "Skeptical", "value": "A"},
            {"key": "B", "text": "Objective", "value": "B"},
            {"key": "C", "text": "Favourable", "value": "C"},
            {"key": "D", "text": "Critical", "value": "D"}
        ]
        q['correct_answer'] = "C"
        print("Calibrated 2020 ky1 Q25")
    elif so == 28:
        q['stem'] = "How does the author feel about the success of Sci-Hub?"
        q['options'] = [
            {"key": "A", "text": "Relieved.", "value": "A"},
            {"key": "B", "text": "Puzzled.", "value": "B"},
            {"key": "C", "text": "Concerned.", "value": "C"},
            {"key": "D", "text": "Encouraged.", "value": "D"}
        ]
        q['correct_answer'] = "C"
        print("Calibrated 2020 ky1 Q28")
json.dump(d_2020_ky1, open(f_2020_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 5. 2018 ky1 Q24, Q27, Q30, Q34, Q40
f_2018_ky1 = 'public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json'
d_2018_ky1 = json.load(open(f_2018_ky1, encoding='utf-8'))
for q in d_2018_ky1['questions']:
    so = q['sort_order']
    if so == 24:
        q['stem'] = "The author suggests that tax policies be aimed at ________."
        q['options'] = [
            {"key": "A", "text": "encouraging the development of automation", "value": "A"},
            {"key": "B", "text": "increasing the return on capital investment", "value": "B"},
            {"key": "C", "text": "easing the hostility between rich and poor", "value": "C"},
            {"key": "D", "text": "preventing the income gap from widening", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2018 ky1 Q24")
    elif so == 27:
        q['stem'] = 'The phrase "beef up" (Line 2, Para. 2) is closest in meaning to ________.'
        q['options'] = [
            {"key": "A", "text": "sharpen", "value": "A"},
            {"key": "B", "text": "define", "value": "B"},
            {"key": "C", "text": "boast", "value": "C"},
            {"key": "D", "text": "share", "value": "D"}
        ]
        q['correct_answer'] = "A"
        print("Calibrated 2018 ky1 Q27")
    elif so == 30:
        q['stem'] = "Which of the following would be the best title for the text?"
        q['options'] = [
            {"key": "A", "text": "A Rise in Critical Skills for Sharing News Online", "value": "A"},
            {"key": "B", "text": "A Counteraction Against the Over-tweeting Trend", "value": "B"},
            {"key": "C", "text": "The Accumulation of Mutual Trust on Social Media", "value": "C"},
            {"key": "D", "text": "The Platforms for Projection of Personal Interests", "value": "D"}
        ]
        q['correct_answer'] = "A"
        print("Calibrated 2018 ky1 Q30")
    elif so == 34:
        q['stem'] = "According to the last paragraph, the real worry arising from this deal is ________."
        q['options'] = [
            {"key": "A", "text": "the vicious rivalry among big pharmas", "value": "A"},
            {"key": "B", "text": "the ineffective enforcement of privacy law", "value": "B"},
            {"key": "C", "text": "the uncontrolled use of new software", "value": "C"},
            {"key": "D", "text": "the monopoly of big data by tech giants", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2018 ky1 Q34")
    elif so == 40:
        q['stem'] = "Which of the following would be the best title for the text?"
        q['options'] = [
            {"key": "A", "text": "The USPS Starts to Miss Its Good Old Days", "value": "A"},
            {"key": "B", "text": "The Postal Service: Keep Away from My Cheese", "value": "B"},
            {"key": "C", "text": "The USPS: Chronic Illness Requires a Quick Cure", "value": "C"},
            {"key": "D", "text": "The Postal Service Needs More Than a Band-Aid", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2018 ky1 Q40")
json.dump(d_2018_ky1, open(f_2018_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 6. 2002 ky1 Q31, Q32, Q38
f_2002_ky1 = 'public/data/exams/e1b9d134-9546-55ab-9a60-c7e5b04046a3.json'
d_2002_ky1 = json.load(open(f_2002_ky1, encoding='utf-8'))
for q in d_2002_ky1['questions']:
    so = q['sort_order']
    if so == 31:
        q['stem'] = "The main reason for the latest rise of oil price is ________."
        q['options'] = [
            {"key": "A", "text": "global inflation", "value": "A"},
            {"key": "B", "text": "reduction in supply", "value": "B"},
            {"key": "C", "text": "fast growth in economy", "value": "C"},
            {"key": "D", "text": "Iraq's suspension of exports", "value": "D"}
        ]
        q['correct_answer'] = "B"
        print("Calibrated 2002 ky1 Q31")
    elif so == 32:
        q['stem'] = "It can be inferred from the text that the retail price of petrol will go up dramatically if ________."
        q['options'] = [
            {"key": "A", "text": "price of crude rises", "value": "A"},
            {"key": "B", "text": "commodity prices rise", "value": "B"},
            {"key": "C", "text": "consumption rises", "value": "C"},
            {"key": "D", "text": "oil taxes rise", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2002 ky1 Q32")
    elif so == 38:
        q['stem'] = "According to the NAS's report, one of the problems in end-of-life care is ________."
        q['options'] = [
            {"key": "A", "text": "prolonged medical procedures", "value": "A"},
            {"key": "B", "text": "inadequate treatment of pain", "value": "B"},
            {"key": "C", "text": "systematic drug abuse", "value": "C"},
            {"key": "D", "text": "insufficient hospital care", "value": "D"}
        ]
        q['correct_answer'] = "B"
        print("Calibrated 2002 ky1 Q38")
json.dump(d_2002_ky1, open(f_2002_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 7. 2010 ky1 Q27
f_2010_ky1 = 'public/data/exams/e5abf09b-e94d-5994-b944-7c5711cd4e4d.json'
d_2010_ky1 = json.load(open(f_2010_ky1, encoding='utf-8'))
for q in d_2010_ky1['questions']:
    if q['sort_order'] == 27:
        q['stem'] = "Which of the following is true of the Bilski case?"
        q['options'] = [
            {"key": "A", "text": "Its ruling complies with the court decisions.", "value": "A"},
            {"key": "B", "text": "It involves a very big business transaction.", "value": "B"},
            {"key": "C", "text": "It has been dismissed by the Federal Circuit.", "value": "C"},
            {"key": "D", "text": "It may change the legal practices in the U.S.", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2010 ky1 Q27")
json.dump(d_2010_ky1, open(f_2010_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 8. 2021 ky1 Q24
f_2021_ky1 = 'public/data/exams/e7dfeb60-9e71-5912-8e2c-0828e345b98c.json'
d_2021_ky1 = json.load(open(f_2021_ky1, encoding='utf-8'))
for q in d_2021_ky1['questions']:
    if q['sort_order'] == 24:
        q['stem'] = "If unable to calm down passengers, the railways may have to face ________."
        q['options'] = [
            {"key": "A", "text": "the loss of investment", "value": "A"},
            {"key": "B", "text": "the collapse of operations", "value": "B"},
            {"key": "C", "text": "a reduction of revenue", "value": "C"},
            {"key": "D", "text": "a change of ownership", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2021 ky1 Q24")
json.dump(d_2021_ky1, open(f_2021_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 9. 2012 ky1 Q33, Q35
f_2012_ky1 = 'public/data/exams/baa66182-74ec-5a78-b2d2-077ffdcad9dc.json'
d_2012_ky1 = json.load(open(f_2012_ky1, encoding='utf-8'))
for q in d_2012_ky1['questions']:
    so = q['sort_order']
    if so == 33:
        q['stem'] = "Paragraph 3 shows that a discovery claim becomes credible after it ________."
        q['options'] = [
            {"key": "A", "text": "has attracted the attention of the general public", "value": "A"},
            {"key": "B", "text": "has been examined by the scientific community", "value": "B"},
            {"key": "C", "text": "has received recognition from editors and reviewers", "value": "C"},
            {"key": "D", "text": "has been frequently quoted by peer scientists", "value": "D"}
        ]
        q['correct_answer'] = "B"
        print("Calibrated 2012 ky1 Q33")
    elif so == 35:
        q['stem'] = "Which of the following would be the best title of the text?"
        q['options'] = [
            {"key": "A", "text": "Novelty as an Engine of Scientific Development.", "value": "A"},
            {"key": "B", "text": "Collective Scrutiny in Scientific Discovery.", "value": "B"},
            {"key": "C", "text": "Evolution of Credibility in Doing Science.", "value": "C"},
            {"key": "D", "text": "Challenge to Credibility at the Gate to Science.", "value": "D"}
        ]
        q['correct_answer'] = "C"
        print("Calibrated 2012 ky1 Q35")
json.dump(d_2012_ky1, open(f_2012_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 10. 2022 ky2 Q32, Q38, Q40 & Cloze Q1-Q20
# First import parsed cloze explanations from parse_2022_ky2_cloze
from parse_2022_ky2_cloze import questions_text as cloze_2022_expls

f_2022_ky2 = 'public/data/exams/cc4bf627-e456-538f-87e2-4a99ebb613ed.json'
d_2022_ky2 = json.load(open(f_2022_ky2, encoding='utf-8'))
for q in d_2022_ky2['questions']:
    so = q['sort_order']
    if 1 <= so <= 20:
        if so in cloze_2022_expls:
            q['explanation'] = cloze_2022_expls[so]
            print(f"Injected authentic explanation for 2022 ky2 Q{so:02d}")
    elif so == 32:
        q['stem'] = "The 2019 study on dark patterns is mentioned to show ________."
        q['options'] = [
            {"key": "A", "text": "their major flaws", "value": "A"},
            {"key": "B", "text": "their complex designs", "value": "B"},
            {"key": "C", "text": "their severe damage", "value": "C"},
            {"key": "D", "text": "their strong presence", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2022 ky2 Q32")
    elif so == 38:
        q['stem'] = "Eric Schwitzgebel's previous findings suggest that ethics professors ________."
        q['options'] = [
            {"key": "A", "text": "are seldom critical of their students", "value": "A"},
            {"key": "B", "text": "are less sociable than other professors", "value": "B"},
            {"key": "C", "text": "are not sensitive to political issues", "value": "C"},
            {"key": "D", "text": "are not necessarily ethically better", "value": "D"}
        ]
        q['correct_answer'] = "D"
        print("Calibrated 2022 ky2 Q38")
    elif so == 40:
        q['stem'] = "Eric Schwitzgebel suspects that the students' change in behavior ________."
        q['options'] = [
            {"key": "A", "text": "can bring psychological benefits", "value": "A"},
            {"key": "B", "text": "can be analyzed statistically", "value": "B"},
            {"key": "C", "text": "is a result of multiple factors", "value": "C"},
            {"key": "D", "text": "is a sign of self-development", "value": "D"}
        ]
        q['correct_answer'] = "C"
        print("Calibrated 2022 ky2 Q40")
json.dump(d_2022_ky2, open(f_2022_ky2, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 11. 2003 ky1 Q2 and Q9
f_2003_ky1 = 'public/data/exams/91ff038a-e3f9-5b6d-82c5-1328735be1d1.json'
d_2003_ky1 = json.load(open(f_2003_ky1, encoding='utf-8'))
for q in d_2003_ky1['questions']:
    so = q['sort_order']
    if so == 2:
        q['options'] = [
            {"key": "A", "text": "strengthen", "value": "A"},
            {"key": "B", "text": "accommodate", "value": "B"},
            {"key": "C", "text": "stimulate", "value": "C"},
            {"key": "D", "text": "enhance", "value": "D"}
        ]
        q['correct_answer'] = "B"
        print("Calibrated 2003 ky1 Q2")
    elif so == 9:
        q['options'] = [
            {"key": "A", "text": "displaying", "value": "A"},
            {"key": "B", "text": "describing", "value": "B"},
            {"key": "C", "text": "creating", "value": "C"},
            {"key": "D", "text": "exchanging", "value": "D"}
        ]
        q['correct_answer'] = "A"
        print("Calibrated 2003 ky1 Q9")
json.dump(d_2003_ky1, open(f_2003_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("\n=== All Round 16 Calibrations Successfully Applied! ===")
