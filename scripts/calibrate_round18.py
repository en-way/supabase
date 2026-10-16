# -*- coding: utf-8 -*-
"""
calibrate_round18.py
Round 18 Calibration Script:
1. 2011 ky1 Q21, Q22, Q23, Q32, Q33, Q35 authentic options, correct answers and complete stems
2. 2014 ky1 Q31, Q32, Q33, Q39, Q40 authentic options, correct answers and explanations
3. 2001 ky1 Q32 and Q40 authentic options, correct answers and complete stems
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Calibrate 2011 ky1 (111d6c78-81a1-53dc-a039-dad4c94ebd35.json)
f_2011 = 'public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json'
d_2011 = json.load(open(f_2011, encoding='utf-8'))
for q in d_2011['questions']:
    so = q['sort_order']
    if so == 21:
        q['stem'] = "We learn from Para. 1 that Gilbert's appointment has ________."
        q['options'] = [
            {"key": "A", "text": "incurred criticism", "value": "A"},
            {"key": "B", "text": "raised suspicion", "value": "B"},
            {"key": "C", "text": "received acclaim", "value": "C"},
            {"key": "D", "text": "aroused curiosity", "value": "D"}
        ]
        q['correct_answer'] = "C"
        q['answer'] = "C"
        print("Calibrated 2011 ky1 Q21")
    elif so == 22:
        q['stem'] = "Tommasini regards Gilbert as an artist who is ________."
        q['options'] = [
            {"key": "A", "text": "influential", "value": "A"},
            {"key": "B", "text": "modest", "value": "B"},
            {"key": "C", "text": "respectable", "value": "C"},
            {"key": "D", "text": "talented", "value": "D"}
        ]
        q['correct_answer'] = "B"
        q['answer'] = "B"
        print("Calibrated 2011 ky1 Q22")
    elif so == 23:
        q['stem'] = "The author believes that the devoted concertgoers ________."
        q['options'] = [
            {"key": "A", "text": "ignore the expenses of live performances", "value": "A"},
            {"key": "B", "text": "reject most kinds of recorded performances", "value": "B"},
            {"key": "C", "text": "exaggerate the variety of live performances", "value": "C"},
            {"key": "D", "text": "overestimate the value of live performances", "value": "D"}
        ]
        q['correct_answer'] = "D"
        q['answer'] = "D"
        print("Calibrated 2011 ky1 Q23")
    elif so == 32:
        q['stem'] = "According to Paragraph 2, sold media feature ________."
        q['options'] = [
            {"key": "A", "text": "a safe business environment", "value": "A"},
            {"key": "B", "text": "random competition", "value": "B"},
            {"key": "C", "text": "strong user traffic", "value": "C"},
            {"key": "D", "text": "flexibility in organization", "value": "D"}
        ]
        q['correct_answer'] = "C"
        q['answer'] = "C"
        print("Calibrated 2011 ky1 Q32")
    elif so == 33:
        q['stem'] = "The author indicates in Paragraph 3 that earned media ________."
        q['options'] = [
            {"key": "A", "text": "invite constant conflicts with passionate consumers", "value": "A"},
            {"key": "B", "text": "can be used to produce negative effects in marketing", "value": "B"},
            {"key": "C", "text": "may be responsible for fiercer competition", "value": "C"},
            {"key": "D", "text": "deserve all the negative comments about them", "value": "D"}
        ]
        q['correct_answer'] = "B"
        q['answer'] = "B"
        print("Calibrated 2011 ky1 Q33")
    elif so == 35:
        q['stem'] = "Which of the following is the text mainly about?"
        q['options'] = [
            {"key": "A", "text": "Alternatives to conventional paid media.", "value": "A"},
            {"key": "B", "text": "Conflict between hijacked and earned media.", "value": "B"},
            {"key": "C", "text": "Dominance of hijacked media.", "value": "C"},
            {"key": "D", "text": "Popularity of owned media.", "value": "D"}
        ]
        q['correct_answer'] = "A"
        q['answer'] = "A"
        print("Calibrated 2011 ky1 Q35")

json.dump(d_2011, open(f_2011, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 2. Calibrate 2014 ky1 (240cc48a-439b-5d27-8464-f7dc53e060dc.json)
f_2014 = 'public/data/exams/240cc48a-439b-5d27-8464-f7dc53e060dc.json'
d_2014 = json.load(open(f_2014, encoding='utf-8'))
for q in d_2014['questions']:
    so = q['sort_order']
    if so == 31:
        q['stem'] = "The Fundamental Physics Prize is seen as ________."
        q['options'] = [
            {"key": "A", "text": "a symbol of the entrepreneurs' wealth", "value": "A"},
            {"key": "B", "text": "a handsome reward for researchers", "value": "B"},
            {"key": "C", "text": "a possible replacement of the Nobel Prizes", "value": "C"},
            {"key": "D", "text": "an example of bankers' investments", "value": "D"}
        ]
        q['correct_answer'] = "B"
        q['answer'] = "B"
        print("Calibrated 2014 ky1 Q31")
    elif so == 32:
        q['stem'] = "The critics think that the new awards will most benefit ________."
        q['options'] = [
            {"key": "A", "text": "the profit-oriented scientists", "value": "A"},
            {"key": "B", "text": "the achievement-based system", "value": "B"},
            {"key": "C", "text": "the founders of the new awards", "value": "C"},
            {"key": "D", "text": "peer-review-led research", "value": "D"}
        ]
        q['correct_answer'] = "C"
        q['answer'] = "C"
        print("Calibrated 2014 ky1 Q32")
    elif so == 33:
        q['stem'] = "The discovery of the Higgs boson is a typical case which involves ________."
        q['options'] = [
            {"key": "A", "text": "legitimate concerns over the new prizes", "value": "A"},
            {"key": "B", "text": "controversies over the recipients' status", "value": "B"},
            {"key": "C", "text": "the joint effort of modern researchers", "value": "C"},
            {"key": "D", "text": "the demonstration of research findings", "value": "D"}
        ]
        q['correct_answer'] = "C"
        q['answer'] = "C"
        print("Calibrated 2014 ky1 Q33")
    elif so == 39:
        q['stem'] = "The author implies in Paragraph 5 that professors are ________."
        q['options'] = [
            {"key": "A", "text": "supportive of free markets", "value": "A"},
            {"key": "B", "text": "conservative about public policy", "value": "B"},
            {"key": "C", "text": "biased against classical liberal ideas", "value": "C"},
            {"key": "D", "text": "cautious about intellectual investigation", "value": "D"}
        ]
        q['correct_answer'] = "C"
        q['answer'] = "C"
        q['explanation'] = """39. The author implies in Paragraph 5 that professors are ________.
39.作者在第五段中暗示教授们________。
[A] supportive of free markets ［A］支持自由市场
[B] conservative about public policy ［B］在公共政策上立场保守
[C] biased against classical liberal ideas ［C］对古典人文思想持有偏见
[D] cautious about intellectual investigation ［D］对学术研究持谨慎态度

【精准定位】第五段指出教授们认为古典人文思想属于非常规、非正当合理的学术研究范围，而作者对人文思想是持积极肯定态度。由此可知，作者实质暗示教授们对古典人文思想持有偏见，［C］正确。
【命题解密】正确项［C］中 biased 是对段中 portraying conservative or classical liberal ideas—such as free markets and self-reliance—as falling outside the boundaries of routine, and sometimes legitimate, intellectual investigation所蕴藏作者观点的最合理推断。
【干扰项排除】［A］与“教授们对古典人文思想（包括自由市场）的偏见态度”相悖；［B］与“教授们支持进步的公共政策”相悖；［D］将“教授们认为古典人文思想不属于学术研究范畴”曲解为“他们对学术研究持谨慎态度”。"""
        print("Calibrated 2014 ky1 Q39 (options and explanation)")
    elif so == 40:
        q['stem'] = "Which of the following would be the best title for the text?"
        q['options'] = [
            {"key": "A", "text": "Ways to Grasp \"The Heart of the Matter\"", "value": "A"},
            {"key": "B", "text": "Illiberal Education and \"The Heart of the Matter\"", "value": "B"},
            {"key": "C", "text": "The AAAS's Contribution to Liberal Education", "value": "C"},
            {"key": "D", "text": "Progressive Policy vs. Liberal Education", "value": "D"}
        ]
        q['correct_answer'] = "B"
        q['answer'] = "B"
        q['explanation'] = """40. Which of the following would be the best title for the text?
40.下列哪项最适合做本文的标题？
[A] Ways to Grasp "The Heart of the Matter" ［A］理解《问题的核心》的方法。
[B] Illiberal Education and "The Heart of the Matter" ［B］非人文教育与《问题的核心》。
[C] The AAAS's Contribution to Liberal Education ［C］美国人文与科学院对人文教育的贡献。
[D] Progressive Policy vs. Liberal Education ［D］进步政策VS人文教育。

【精准定位】文首段点题:《问题的核心》虽值得赞赏，却未触及当前美国人文教育危机的本质，其结果最终可能是弊大于利；第二段退而补充《问题的核心》的出台背景；第三至五段详细阐述主题:《问题的核心》所设目标总体而言值得欣赏，但它从未触及“人文教育非人文的本质”这一问题核心；文末段重申主题:《问题的核心》未能深刻全面分析“人文教育非人文”这一挑战性难题，其结果很可能阻碍人文教育改革。由此可见，［B］最能概括文意。
【命题解密】正确项［B］是对文章主旨的最佳概括。
【干扰项排除】［A］纯属无中生有，文章重点评述《问题的核心》的缺点，并未介绍如何理解《问题的核心》；［C］利用文首句“美国人文与科学院证实人文教育的重要性”设置干扰，虽有一定正确成分，却并非文意重点；［D］利用第五段“教授重进步政策、轻/弃人文教育”设置陷阱，虽有一定正确成分，却并非文意重点。"""
        print("Calibrated 2014 ky1 Q40 (options and explanation)")

json.dump(d_2014, open(f_2014, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 3. Calibrate 2001 ky1 (2c892204-071f-5943-86be-d49bca93fe71.json)
f_2001 = 'public/data/exams/2c892204-071f-5943-86be-d49bca93fe71.json'
d_2001 = json.load(open(f_2001, encoding='utf-8'))
for q in d_2001['questions']:
    so = q['sort_order']
    if so == 32:
        q['stem'] = "Despite its efforts, the newspaper industry still cannot satisfy the readers owing to its ________."
        q['options'] = [
            {"key": "A", "text": "failure to realize its real problem", "value": "A"},
            {"key": "B", "text": "tendency to hire annoying reporters", "value": "B"},
            {"key": "C", "text": "likeliness to do inaccurate reporting", "value": "C"},
            {"key": "D", "text": "prejudice in matters of race and gender", "value": "D"}
        ]
        q['correct_answer'] = "A"
        q['answer'] = "A"
        print("Calibrated 2001 ky1 Q32")
    elif so == 40:
        q['stem'] = "According to the passage, downshifting emerged in the US as a result of ________."
        q['options'] = [
            {"key": "A", "text": "the quick pace of modern life", "value": "A"},
            {"key": "B", "text": "man's adventurous spirit", "value": "B"},
            {"key": "C", "text": "man's search for mythical experiences", "value": "C"},
            {"key": "D", "text": "the economic situation", "value": "D"}
        ]
        q['correct_answer'] = "D"
        q['answer'] = "D"
        print("Calibrated 2001 ky1 Q40")

json.dump(d_2001, open(f_2001, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("\n=== All Round 18 Calibrations Successfully Applied to Local JSON! ===")
