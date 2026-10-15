import json
import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 6 Deep Calibrations: Stems, Options, Explanations & Semantic Alignment ===")

exam_files = {}
for f in glob.glob("public/data/exams/*.json"):
    with open(f, "r", encoding="utf-8") as jf:
        data = json.load(jf)
        yr = data["exam"]["year"]
        cat = data["exam"]["category_id"]
        exam_files[(yr, cat)] = f

def get_exam(yr, cat):
    fpath = exam_files[(yr, cat)]
    with open(fpath, "r", encoding="utf-8") as f:
        return fpath, json.load(f)

def save_exam(fpath, data):
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ==============================================================================
# 1. 2022 ky1: Q16, Q27, Q28, Q29, Q30, Q40, Q41-Q45 Major Calibration
# ==============================================================================
fpath, d_2022_1 = get_exam(2022, "ky1")

expl_2022_q16 = """16. 本题考查的知识点：段际语义逻辑+引述动词辨析。
第一步：语法结构分析
①定位：空格16位于第一句的引述分句中。②句子结构分析：引述分句的结构为“主语（he） +谓语（16）”，该引述分句实际辖域本段两句内容。he指代上文Taiz，即新研究的第一作者。
第二步：语义逻辑分析
本段两句指出，“想要进化成意识，大脑的复杂性和容纳度都需要达到一定的阈值。”他16，“既然植物没有神经系统，那么它们拥有意识的……为零。”结合上文泰兹的话语（Taiz said）“动植物的信号传递只是表面上的相似”可知，本段是在上文基础上的进一步延伸、补充。
第三步：选项正误分析 【答案D】
[A] recalled 意为“回忆；回想”。该项所辖域的引号内的内容是对过去事件或经历的回忆，而文中为泰兹的观点，故排除。
[B] agreed 意为“同意；赞成”。该项所辖域的引号内的内容表达的是对他人观点的认可，而文中均为泰兹本人的观点(he回指Taiz)，故排除。
[C] questioned 意为“询问；质疑”。该项所辖域的引号内的内容表达的是疑问或质疑，与文章内容不符，故排除。
[D] added 意为“补充说；继续说”。该项所辖域的引号内的内容是对观点或看法的进一步补充说明，契合文中引号内内容的性质，故正确。"""

expl_2022_q28 = """锁定 答案 C
1. 定位：根据题干关键词a good sign可定位至第四段首句(there are signs...)。
2. 分析：第四段首先指出，有迹象表明“大学不是Z世代的唯一出路”这一情形已经出现，随后明确有哪些迹象：1. Z世代已经谋求向千禧前辈学习从事无需本科学历的工作；2.雇主早已认识到相较大学毕业生来说雇用中学毕业生的好处；3.许多雇主还认识到取消某些职位的大学学历要求的诸多好处；其中2、3点表明中学毕业生在一定程度上受到了雇主的青睐，即雇主不再将有无大学学位视为判断员工是否适合雇用的标准。
3. 确定：题干+ C项是对2、3点(文中第四段第②③句)的准确概括:taking a realistic attitude to degree对应have long seen the advantages...和seeing the advantages...的深层内涵。
排除干扰：
A. 1. 定位：根据题干Generation Z可定位至第四段首句(Generation Z...)。2. 排除：该项张冠李戴：将“尽管父母和老师还固守着学位论，Z世代却已在谋求向千禧前辈学习”改为“Z世代在谋求获得像样的学位”。
B. 1. 定位：根据题干school leavers可定位至第四段②句(...school leavers...)。2. 排除：该项利用该句“中学毕业生工作认真敬业”这一碎片信息捏造而来。文章并未提到中学毕业生是否愿意成为技术工人。
D. 1. 定位：根据题干parents可定位至第四段首句(parents...)。2. 排除：该项与首句意思相悖：该句指出父母和老师往往仍固守学位论，而非正在改变对教育的看法。
技巧总结：
对于某些正面解答较为困难的题目，如果各选项的结构极为相似，可从选项入手，采用“关键词定位一关键信息比对”的方式判断正误。如本题，各项均为X are doing/willing to do Y的结构，比对可知C项概括雇主做法，确定为正确项。"""

expl_2022_q29 = """锁定 答案 D
1. 定位：根据题干关键词Paragraph 5,those with one degree可定位至第五段(For those for whom a degree is the desired route...)。
2. 分析：第五段首句先提出建议：认为获取大学学位是理想路线的人应把大学学位当作是许多学位中的第一个。随后进一步阐释：在目前这个通才时代，掌握专门的知识或技能大有裨益；研究生薪资比本科生高40%；当越来越多的人拥有一个学位时，拥有两个便是明智之举。可见，作者认为那些拥有了一个学位(本科学位)的人应继续深造。
3. 确定：题干+ D项是对第五段作者建议的准确概括；其中further their studies in a specific field综合自②句have specific knowledge or skills，③句Postgraduates，④句have two。
排除干扰：
A. 1. 定位：根据题干early decision on...career可定位至首句(this...the first of many)。2. 排除：该项过度引申。首句意在提出“渴望获取大学学位的人拿到本科学位之后应该继续深造”，并未指出“因此应当提前做好职业规划”。
B. 1. 定位：根据题干training programs可定位至②句(have specific knowledge or skills)。2. 排除：断章取义。“拥有专门的知识和技能”此处是指研究生阶段教育，而非“在职能力培训”。
C. 1. 定位：根据题干关键词high-paid postgraduates、team up可定位至③④句。2. 排除：曲解两句关系。two指的是“一个人拥有两个学位”，并非“本科生与研究生合作”。
技巧总结：
考查“作者建议”的题目有时难在识别隐藏于定位句中的建议性表达。本题固定句式(it pays to do sth, it makes sense to do sth)和祈使语气(consider...)均在提出建议，综合得出“继续深造，获取更多学位”，从而确定D项正确。"""

expl_2022_q30 = """锁定 答案 A
1. 定位：根据题干the last two paragraphs可定位至第六、七段。
2. 分析：第六段指出，Z世代在其职业生涯中会从事5种职业、为17个雇主工作，他们需要不断提升职业技能才能保持就业能力。所以教育（不仅仅是学校里学的知识）将是Z世代职业轨迹的核心部分。第七段指出，对于一生所从事的职业和大学所学专业高度相关的老一辈人来说，大学学位是定义其身份的关键因素，然而对于Z世代却并非如此（言外之意：终身学习才能定义Z世代）。
3. 确定：A项是对第六、七段信息的高度概括，其中Lifelong learning总结自第六段constantly up-skilling throughout their career... Education, and not just knowledge gained on campus；define采用第七段define一词。
排除干扰：
B. 1. 定位：根据选项关键词make qualified educators可定位至第六段首句。2. 排除：断章取义，目的是保持就业能力，而非成为合格的教育者。
C. 1. 定位：根据选项可定位至第六段末句。2. 排除：误读，强调终身学习的重要性，并非表示学位对Z世代失去了吸引力。
D. 1. 定位：根据选项limited choice of jobs可定位至第六段②句。2. 排除：与该句“Z世代的职业选择非常丰富”相悖。"""

expl_2022_q40 = """锁定 答案 C
1. 定位：由题干关键词"high-income threshold" in Australia可定位至第八段①句(Australia...high-income threshold)。
2. 分析：第八段①句指出，澳大利亚为应对“不正当解雇悖论”，将超过特定“高收入门槛”的员工排除在“不公平解雇法”的保护范围之外。联系上文“不正当解雇法应用于高薪管理人员会阻碍企业发展”，可反推知，澳大利亚政府的“高收入门槛”有利于保障企业主的权益。
3. 确定：C项is beneficial to business owners契合澳大利亚政府设置"高收入门槛"的目的(deals with the unjustified dismissal paradox)。
排除干扰：
A. 1. 定位：由选项关键词managers' earnings可定位至第八段①句。2. 排除：与第八段①句言外之意“高收入经理的工作与收入无法受到法律保障”相悖。
B. 1. 定位：选项关键词undesired results由第八段中消极语义词unjustified、unfair、unwieldy捏造，排除。
D. 1. 定位：选项论及"低可行性"，可关联至第八段③句中的unwieldy, was voted down，但那是新西兰的法案而非澳大利亚，张冠李戴，排除。"""

for q in d_2022_1["questions"]:
    so = q["sort_order"]
    if so == 16:
        q["explanation"] = expl_2022_q16
    elif so == 27:
        q["stem"] = "The percentage of UK graduates in non-graduate roles reflects ________."
    elif so == 28:
        q["stem"] = "The author considers it a good sign that ________."
        q["explanation"] = expl_2022_q28
    elif so == 29:
        q["stem"] = "It is advised in Paragraph 5 that those with one degree should ________."
        q["correct_answer"] = "D"
        q["explanation"] = expl_2022_q29
    elif so == 30:
        q["stem"] = "What can be concluded about Generation Z from the last two paragraphs?"
        q["correct_answer"] = "A"
        q["explanation"] = expl_2022_q30
    elif so == 40:
        q["stem"] = 'It can be inferred that the "high-income threshold" in Australia ________.'
        q["options"] = [
            {"key": "A", "text": "has secured managers' earnings", "value": "A"},
            {"key": "B", "text": "has produced undesired results", "value": "B"},
            {"key": "C", "text": "is beneficial to business owners", "value": "C"},
            {"key": "D", "text": "is difficult to put into practice", "value": "D"}
        ]
        q["correct_answer"] = "C"
        q["answer"] = "C"
        q["explanation"] = expl_2022_q40
    elif so == 41:
        q["correct_answer"] = "F"
        q["answer"] = "F"
    elif so == 42:
        q["correct_answer"] = "C"
        q["answer"] = "C"
    elif so == 43:
        q["correct_answer"] = "A"
        q["answer"] = "A"
    elif so == 44:
        q["correct_answer"] = "D"
        q["answer"] = "D"
    elif so == 45:
        q["correct_answer"] = "G"
        q["answer"] = "G"

save_exam(fpath, d_2022_1)
print("Updated 2022 ky1: Q16, Q27, Q28, Q29, Q30, Q40, Q41-45 fully calibrated.")

# ==============================================================================
# 2. 2010 ky1: Restore authentic Q8 Cloze Explanation
# ==============================================================================
fpath, d_2010_1 = get_exam(2010, "ky1")
expl_2010_q8 = """8. [A] awareness 意识 [B] expectation 预期 [C] sentiment 观点 [D] illusion 错觉
[考点提炼]名词辨析。正确率：43%
[解题思路]本句中that引导的同位语从句解释空格词。联系上段末句the very act of being experimented upon changed subject's behavior...可知，此处重申"霍桑效应"的概念；四项都涉及"主观思维”，可以推知“被试本身之所以会改变行为，是通过影响其思维实现的”，再结合上文“照明无论如何变，效率都提高”可判定：工人因为知道了自己正在受试，所以行为改变，[A]符合文意。
[错项排除][B]表示“对未来情况的预期”，与文中过去进行时态不匹配；或指对事情的“期望或指望”，而文中“他们正被当作实验对象”是真实情况，而非实验对象的期望。[C]表示“对某事物的观点、意见或感想”，但空格后that从句是对事实的客观阐述。[D]表示“错误的观念”，或表示“幻想的事物”；而文中that从句显然是客观事实。"""

stems_2010_1 = {
    22: "Newspaper reviews in England before World War II were characterized by ________.",
    23: "Which of the following would Shaw and Newman most probably agree on?",
    24: "What can be learned about Cardus according to the last two paragraphs?",
    26: "Business-method patents have recently aroused concern because of ________.",
    29: "We learn from the last two paragraphs that business-method patents ________.",
    35: "What is the essential element in the dynamics of social influence?",
    37: "According to the author, the rule changes of the FASB may result in ________.",
    38: "According to Paragraph 4, McCreevy objects to the IASB's attempt to ________."
}

for q in d_2010_1["questions"]:
    so = q["sort_order"]
    if so == 8:
        q["explanation"] = expl_2010_q8
    if so in stems_2010_1:
        q["stem"] = stems_2010_1[so]

save_exam(fpath, d_2010_1)
print("Updated 2010 ky1: Q8 authentic explanation & Q22, 23, 24, 26, 29, 35, 37, 38 stems restored.")

# ==============================================================================
# 3. 2020 ky1: Stems dropped line restoration
# ==============================================================================
fpath, d_2020_1 = get_exam(2020, "ky1")
stems_2020_1 = {
    22: "According to Paragraph 2, the proposal might be regarded by some as ________.",
    23: "The author suggests that a title holder is successful only if it ________.",
    26: 'Scientific publishing is seen as "a license to print money" partly because ________.',
    27: "According to Paragraphs 2 and 3, scientific publishers like Elsevier have ________.",
    29: "It can be learned from Paragraphs 5 and 6 that open access terms ________.",
    30: "Which of the following characterizes the scientific publishing model?",
    37: "It can be learned from Paragraph 2 that the digital services tax ________."
}
for q in d_2020_1["questions"]:
    so = q["sort_order"]
    if so in stems_2020_1:
        q["stem"] = stems_2020_1[so]
save_exam(fpath, d_2020_1)
print("Updated 2020 ky1: Stems restored.")

# ==============================================================================
# 4. 2019 ky1: Q34 Stem & Watermark Cleanup
# ==============================================================================
fpath, d_2019_1 = get_exam(2019, "ky1")
for q in d_2019_1["questions"]:
    if q["sort_order"] == 34:
        q["stem"] = 'The word "arbiters" (Line 6, Paragraph 4) most probably refers to those ________.'
        q["explanation"] = q["explanation"].replace("28\n【公众号：旗胜考研】免费分享\n\n", "")
save_exam(fpath, d_2019_1)
print("Updated 2019 ky1: Q34 stem restored and watermark cleaned.")

# ==============================================================================
# 5. 2013 ky1: Q22, Q23, Q26 Stems & Typos Restoration
# ==============================================================================
fpath, d_2013_1 = get_exam(2013, "ky1")
for q in d_2013_1["questions"]:
    so = q["sort_order"]
    if so == 22:
        q["stem"] = "According to Cline, mass-market labels urge consumers to ________."
    elif so == 23:
        q["stem"] = 'The word "indictment" (Line 3, Para. 2) is closest in meaning to ________.'
    elif so == 26:
        q["stem"] = 'It is suggested in Paragraph 1 that "behavioural" ads help advertisers to ________.'
save_exam(fpath, d_2013_1)
print("Updated 2013 ky1: Q22, Q23, Q26 stems restored.")

# ==============================================================================
# 6. 2015 ky1: Q32 Stem Restoration
# ==============================================================================
fpath, d_2015_1 = get_exam(2015, "ky1")
for q in d_2015_1["questions"]:
    if q["sort_order"] == 32:
        q["stem"] = 'The phrase "flagged up" (Para. 2) is the closest in meaning to ________.'
save_exam(fpath, d_2015_1)
print("Updated 2015 ky1: Q32 stem restored.")

# ==============================================================================
# 7. 2012 ky1: Q21, Q22, Q24, Q26, Q28, Q31 Stems Restoration
# ==============================================================================
fpath, d_2012_1 = get_exam(2012, "ky1")
stems_2012_1 = {
    21: "According to the first paragraph, peer pressure often emerges as ________.",
    22: "Rosenberg holds that public-health advocates should ________.",
    24: "Paragraph 5 shows that our imitation of behaviors ________.",
    26: 'The phrase "reneging on" (Line 3, Para. 1) is closest in meaning to ________.',
    28: "According to Paragraph 4, Entergy seems to have problems with its ________.",
    31: "According to the first paragraph, the process of discovery is characterized by its ________."
}
for q in d_2012_1["questions"]:
    so = q["sort_order"]
    if so in stems_2012_1:
        q["stem"] = stems_2012_1[so]
save_exam(fpath, d_2012_1)
print("Updated 2012 ky1: Q21, 22, 24, 26, 28, 31 stems restored.")

# ==============================================================================
# 8. 2005 ky1: Q28 Stem Restoration
# ==============================================================================
fpath, d_2005_1 = get_exam(2005, "ky1")
for q in d_2005_1["questions"]:
    if q["sort_order"] == 28:
        q["stem"] = 'What does the author mean by "paralysis by analysis" (Last line, Paragraph 4)?'
save_exam(fpath, d_2005_1)
print("Updated 2005 ky1: Q28 stem restored.")

# ==============================================================================
# 9. 2006 ky1: Q37 Stem Restoration
# ==============================================================================
fpath, d_2006_1 = get_exam(2006, "ky1")
for q in d_2006_1["questions"]:
    if q["sort_order"] == 37:
        q["stem"] = 'The word "bummer" (Line 5, Paragraph 5) most probably means something ________.'
save_exam(fpath, d_2006_1)
print("Updated 2006 ky1: Q37 stem restored.")

# ==============================================================================
# 10. 2007 ky1: Q25 Stem Restoration
# ==============================================================================
fpath, d_2007_1 = get_exam(2007, "ky1")
for q in d_2007_1["questions"]:
    if q["sort_order"] == 25:
        q["stem"] = "Which of the following proverbs is closest to the message the text tries to convey?"
save_exam(fpath, d_2007_1)
print("Updated 2007 ky1: Q25 stem restored.")

# ==============================================================================
# 11. 2009 ky1: Q27, Q39 Stems Restoration
# ==============================================================================
fpath, d_2009_1 = get_exam(2009, "ky1")
for q in d_2009_1["questions"]:
    so = q["sort_order"]
    if so == 27:
        q["stem"] = "PTK is used to ________."
    elif so == 39:
        q["stem"] = "The story of John Dane shows that less well-educated New Englanders were often ________."
save_exam(fpath, d_2009_1)
print("Updated 2009 ky1: Q27, Q39 stems restored.")

# ==============================================================================
# 12. 2021 ky1: Q24, Q28, Q33, Q39 Stems Restoration
# ==============================================================================
fpath, d_2021_1 = get_exam(2021, "ky1")
stems_2021_1 = {
    24: "If unable to calm down passengers, the railways may have to face ________.",
    28: "In his study about Indonesia, Ferraro intends to find out ________.",
    33: "What might have kept the Victorians from smiling for pictures in the 1890s?",
    39: "Judge Patricia Millett argues that the appeals court's decision ________."
}
for q in d_2021_1["questions"]:
    so = q["sort_order"]
    if so in stems_2021_1:
        q["stem"] = stems_2021_1[so]
save_exam(fpath, d_2021_1)
print("Updated 2021 ky1: Q24, 28, 33, 39 stems restored.")

# ==============================================================================
# 13. 2021 ky2: Q22 Stem Restoration
# ==============================================================================
fpath, d_2021_2 = get_exam(2021, "ky2")
for q in d_2021_2["questions"]:
    if q["sort_order"] == 22:
        q["stem"] = "AT&T is cited to show ________."
save_exam(fpath, d_2021_2)
print("Updated 2021 ky2: Q22 stem restored.")

# ==============================================================================
# 14. 2018 ky1: Q23, Q26, Q27, Q34 Stems Restoration
# ==============================================================================
fpath, d_2018_1 = get_exam(2018, "ky1")
stems_2018_1 = {
    23: "Education in the age of automation should put more emphasis on ________.",
    26: "According to Paragraphs 1 and 2, many young Americans cast doubts on ________.",
    27: 'The phrase "beef up" (Line 2, Para. 2) is closest in meaning to ________.',
    34: "According to the last paragraph, the real worry arising from this deal is ________."
}
for q in d_2018_1["questions"]:
    so = q["sort_order"]
    if so in stems_2018_1:
        q["stem"] = stems_2018_1[so]
save_exam(fpath, d_2018_1)
print("Updated 2018 ky1: Q23, 26, 27, 34 stems restored.")

# ==============================================================================
# 15. 2022 ky2: Q23, Q24, Q25, Q27, Q30, Q37, Q38, Q39 Stems Restoration
# ==============================================================================
fpath, d_2022_2 = get_exam(2022, "ky2")
stems_2022_2 = {
    23: "The example of organic eggs is used in Paragraph 4 to suggest ________.",
    24: "It can be learned from the last paragraph that young people ________.",
    25: "John Brunnquell would disagree with Julie Stanton over regenerative products' ________.",
    27: "It can be inferred from Paragraph 3 that Americans tend to think that ________.",
    30: "With regard to retirement, Brent Weiss thinks that many people are ________.",
    37: "Which of the following is a reason for the researchers to study meat eating?",
    38: "Eric Schwitzgebel's previous findings suggest that ethics professors ________.",
    39: "Nina Strohminger thinks that the effect of the intervention is ________."
}
for q in d_2022_2["questions"]:
    so = q["sort_order"]
    if so in stems_2022_2:
        q["stem"] = stems_2022_2[so]
save_exam(fpath, d_2022_2)
print("Updated 2022 ky2: Q23, 24, 25, 27, 30, 37, 38, 39 stems restored.")

# ==============================================================================
# 16. 2002 ky1: Q22, Q24, Q27, Q30, Q32, Q33, Q37, Q38, Q39, Q40 Stems Restoration
# ==============================================================================
fpath, d_2002_1 = get_exam(2002, "ky1")
stems_2002_1 = {
    22: "The joke about doctors implies that, in the eyes of nurses, they are ________.",
    24: "To achieve the desired result, humorous stories should be delivered ________.",
    27: 'The word "gizmos" (line 1, paragraph 2) most probably means ________.',
    30: "The author uses the example of a monkey to argue that robots are ________.",
    32: "It can be inferred from the text that the retail price of petrol will go up dramatically if ________.",
    33: "The estimates in Economic Outlook show that in rich countries ________.",
    37: "Which of the following statements is true according to the text?",
    38: "According to the NAS's report, one of the problems in end-of-life care is ________.",
    39: 'Which of the following best defines the word "aggressive" (line 3, paragraph 7)?',
    40: "George Annas would probably agree that doctors should be punished if they ________."
}
for q in d_2002_1["questions"]:
    so = q["sort_order"]
    if so in stems_2002_1:
        q["stem"] = stems_2002_1[so]
save_exam(fpath, d_2002_1)
print("Updated 2002 ky1: Q22, 24, 27, 30, 32, 33, 37, 38, 39, 40 stems restored.")

# ==============================================================================
# 17. 2003 ky1: Q26, Q27, Q28, Q29, Q35, Q37, Q38, Q39 Stems Restoration
# ==============================================================================
fpath, d_2003_1 = get_exam(2003, "ky1")
stems_2003_1 = {
    26: "The author begins his article with Edmund Burke's words to ________.",
    27: "Misled people tend to think that using an animal in research is ________.",
    28: "The example of the grandmotherly woman is used to show the public's ________.",
    29: "The author believes that, in face of the challenge from animal rights advocates, scientists should ________.",
    35: "According to the text, the cost increase in the rail industry is mainly caused by ________.",
    37: "The author uses the example of cancer patients to show that ________.",
    38: "The author's attitude toward Richard Lamm's remark is one of ________.",
    39: "In contrast to the US, Japan and Sweden are funding their medical care ________."
}
for q in d_2003_1["questions"]:
    so = q["sort_order"]
    if so in stems_2003_1:
        q["stem"] = stems_2003_1[so]
save_exam(fpath, d_2003_1)
print("Updated 2003 ky1: Q26, 27, 28, 29, 35, 37, 38, 39 stems restored.")

print("\n--- All Round 6 Deep Calibrations Successfully Applied to Local JSON Files! ---")
