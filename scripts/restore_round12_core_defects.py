import json
import os
import sys
import hashlib
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 12 Core Defects Restoration ===")

# 1. 2004 ky1 Cloze & Passage
path_2004 = "public/data/exams/47036de0-e57d-5ccb-9bc8-b3f86d4e6457.json"
with open(path_2004, "r", encoding="utf-8") as f:
    data_2004 = json.load(f)

true_passage_2004 = """Many theories concerning the causes of juvenile delinquency focus either on the individual or on society as the major influence. Theories [1] on the individual suggest that children engage in criminal behavior [2] they were not sufficiently penalized for previous misdeeds or that they have learned criminal behavior through [3] with others. Theories focusing on the role of society suggest that children commit crimes in [4] to their failure to rise above their socioeconomic status, [5] as a rejection of middle-class values.

Most theories of juvenile delinquency have focused on children from disadvantaged families, [6] the fact that children from wealthy homes also commit crimes. The latter may commit crimes [7] lack of adequate parental control. All theories, however, are tentative and are [8] to criticism.

Changes in the social structure may indirectly [9] juvenile crime rates. For example, changes in the economy that [10] to fewer job opportunities for youth and rising unemployment [11] make gainful employment increasingly difficult to obtain. The resulting discontent may in [12] lead more youths into criminal behavior.

Families have also [13] changes these years. More families consist of one-parent households or two working parents; [14], children are likely to have less supervision at home [15] was common in the traditional family [16]. This lack of parental supervision is thought to be an influence on juvenile crime rates. Other [17] causes of offensive acts include frustration or failure in school, the increased [18] of drugs and alcohol, and the growing [19] of child abuse and child neglect. All these conditions tend to increase the probability of a child committing a criminal act, [20] a direct cause-and-effect relationship has not yet been established."""

data_2004["passages"][0]["content"] = true_passage_2004

# Load 2004 clean explanations
with open("scripts/expl_2004.json", "r", encoding="utf-8") as f:
    expl_2004 = json.load(f)

official_2004_q = [
    (1, "C", [("A", "acting"), ("B", "relying"), ("C", "centering"), ("D", "commenting")]),
    (2, "D", [("A", "before"), ("B", "unless"), ("C", "until"), ("D", "because")]),
    (3, "A", [("A", "interaction"), ("B", "assimilation"), ("C", "cooperation"), ("D", "consultation")]),
    (4, "D", [("A", "in return"), ("B", "in reply"), ("C", "in reference"), ("D", "in response")]),
    (5, "A", [("A", "or"), ("B", "but rather"), ("C", "but"), ("D", "or else")]),
    (6, "B", [("A", "considering"), ("B", "ignoring"), ("C", "highlighting"), ("D", "discarding")]),
    (7, "C", [("A", "on"), ("B", "in"), ("C", "for"), ("D", "with")]),
    (8, "D", [("A", "immune"), ("B", "resistant"), ("C", "sensitive"), ("D", "subject")]),
    (9, "A", [("A", "affect"), ("B", "reduce"), ("C", "check"), ("D", "reflect")]),
    (10, "B", [("A", "point"), ("B", "lead"), ("C", "come"), ("D", "amount")]),
    (11, "A", [("A", "in general"), ("B", "on average"), ("C", "by contrast"), ("D", "at length")]),
    (12, "C", [("A", "in case"), ("B", "in short"), ("C", "in turn"), ("D", "in essence")]),
    (13, "D", [("A", "survived"), ("B", "noticed"), ("C", "undertaken"), ("D", "experienced")]),
    (14, "B", [("A", "contrarily"), ("B", "consequently"), ("C", "similarly"), ("D", "simultaneously")]),
    (15, "A", [("A", "than"), ("B", "that"), ("C", "which"), ("D", "as")]),
    (16, "B", [("A", "system"), ("B", "structure"), ("C", "concept"), ("D", "heritage")]),
    (17, "B", [("A", "assessable"), ("B", "identifiable"), ("C", "negligible"), ("D", "incredible")]),
    (18, "D", [("A", "expense"), ("B", "restriction"), ("C", "allocation"), ("D", "availability")]),
    (19, "A", [("A", "incidence"), ("B", "awareness"), ("C", "exposure"), ("D", "popularity")]),
    (20, "C", [("A", "provided"), ("B", "since"), ("C", "although"), ("D", "supposing")]),
]

q_map_2004 = {item[0]: item for item in official_2004_q}

for q in data_2004["questions"]:
    so = q.get("sort_order")
    if so in q_map_2004:
        _, ans, raw_opts = q_map_2004[so]
        q["stem"] = f"Choose the best option for blank [{so}] in the passage:"
        q["options"] = [{"key": k, "text": t, "value": k} for k, t in raw_opts]
        q["correct_answer"] = ans
        q["answer"] = ans
        q["explanation"] = expl_2004.get(str(so), "")
        q["points"] = 0.5

with open(path_2004, "w", encoding="utf-8") as f:
    json.dump(data_2004, f, ensure_ascii=False, indent=2)
print("-> Restored 2004 ky1 cloze passage and 20 questions successfully!")

# 2. 2010 ky1 Q26
path_2010 = "public/data/exams/e5abf09b-e94d-5994-b944-7c5711cd4e4d.json"
with open(path_2010, "r", encoding="utf-8") as f:
    data_2010 = json.load(f)

expl_2010_q26 = """26. Business-method patents have recently aroused concern because of ________.
[A] their limited value to businesses
[B] their connection with asset allocation
[C] the possible restriction on their granting
[D] the controversy over their authorization

【考点提炼】事实细节题。
【精准定位】根据题干have recently aroused concern定位至第二段①②句（Now, ... has ... abuzz），此两句明确指出知识产权律师议论纷纷的原因是：最高专利法庭将广泛复审商业方法专利，并已准备好削减此类专利数量。可见商业方法专利最近引发争议是因为它们的授予很有可能要受到限制，[C]正确。
【命题解密】题干+正确项[C]符合第二段①②句暗含的因果逻辑：最高专利法庭准备限制商业方法专利的授予引起该类专利引发关注。the possible restriction同义改写①句appears ... scale back。
【干扰项设置】[A]从“首段暗含的作者对商业方法专利授予过多的不认同态度（what are called...）”和“第二段权威当局拟对这类专利进行限制”中捕风捉影，但“反对其过滥”不等于“所有的商业方法专利价值有限”；其次首段表明企业争相申请这类专利，可见它们“对企业来说相当重要”。[B]由首段③句中asset allocation而来，但该句仅为“过去10年来无数商业方法专利被授予”的一个例子，不涉及“新近商业方法专利何以引争议”。[D]将第二段①句中时间“自10年前”偷换成“最近”，将多年以来存在的争议说成是“新近引发关注”。"""

for q in data_2010["questions"]:
    if q.get("sort_order") == 26:
        q["stem"] = "Business-method patents have recently aroused concern because of ________."
        q["options"] = [
            {"key": "A", "text": "their limited value to businesses", "value": "A"},
            {"key": "B", "text": "their connection with asset allocation", "value": "B"},
            {"key": "C", "text": "the possible restriction on their granting", "value": "C"},
            {"key": "D", "text": "the controversy over their authorization", "value": "D"},
        ]
        q["correct_answer"] = "C"
        q["answer"] = "C"
        q["explanation"] = expl_2010_q26

with open(path_2010, "w", encoding="utf-8") as f:
    json.dump(data_2010, f, ensure_ascii=False, indent=2)
print("-> Corrected 2010 ky1 Q26 options, answer (C), and explanation successfully!")

# 3. 2012 ky1 Q40
path_2012 = "public/data/exams/baa66182-74ec-5a78-b2d2-077ffdcad9dc.json"
with open(path_2012, "r", encoding="utf-8") as f:
    data_2012 = json.load(f)

expl_2012_q40 = """40. John Donahue's attitude towards the public-sector system is one of ________.
[A] disapproval
[B] appreciation
[C] tolerance
[D] indifference

【考点提炼】观点态度题。
【精准定位】末段介绍John Donahue观点：政府公共部门文化标准适合那些寻求安稳的人却不利于那些追求事业有成的人，这一缺乏激励的体制是美国面临的严重问题。可见他对当前公共部门体制持不满、担忧态度，[A]符合文意。
【命题解密】正确项[A] disapproval是对专家观点（①③句）suit those who want to stay put but is bad for high achievers ... be a much bigger problem for America 的概括。
【干扰项设置】[B] appreciation（欣赏）与原文批评态度相反；[C] tolerance（容忍）和[D] indifference（漠不关心）均不符合原文强烈的批评性态度。"""

for q in data_2012["questions"]:
    if q.get("sort_order") == 40:
        q["stem"] = "John Donahue's attitude towards the public-sector system is one of ________."
        q["options"] = [
            {"key": "A", "text": "disapproval", "value": "A"},
            {"key": "B", "text": "appreciation", "value": "B"},
            {"key": "C", "text": "tolerance", "value": "C"},
            {"key": "D", "text": "indifference", "value": "D"},
        ]
        q["correct_answer"] = "A"
        q["answer"] = "A"
        q["explanation"] = expl_2012_q40

with open(path_2012, "w", encoding="utf-8") as f:
    json.dump(data_2012, f, ensure_ascii=False, indent=2)
print("-> Corrected 2012 ky1 Q40 options and explanation successfully!")

# 4. Correct 3 Official Answers: 2016 Q1 (A), 2017 Q14 (B), 2013 Q2 (B)
path_2016 = "public/data/exams/666cdb4e-7fd3-53c2-8c91-a12fa3160c09.json"
with open(path_2016, "r", encoding="utf-8") as f:
    data_2016 = json.load(f)
for q in data_2016["questions"]:
    if q.get("sort_order") == 1:
        q["correct_answer"] = "A"
        q["answer"] = "A"
with open(path_2016, "w", encoding="utf-8") as f:
    json.dump(data_2016, f, ensure_ascii=False, indent=2)
print("-> Corrected 2016 ky1 Q1 answer to A (as well as)!")

path_2017 = "public/data/exams/4fd42872-4822-5786-8d16-0317051bf03d.json"
with open(path_2017, "r", encoding="utf-8") as f:
    data_2017 = json.load(f)
for q in data_2017["questions"]:
    if q.get("sort_order") == 14:
        q["correct_answer"] = "B"
        q["answer"] = "B"
with open(path_2017, "w", encoding="utf-8") as f:
    json.dump(data_2017, f, ensure_ascii=False, indent=2)
print("-> Corrected 2017 ky1 Q14 answer to B (associated)!")

path_2013 = "public/data/exams/6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json"
with open(path_2013, "r", encoding="utf-8") as f:
    data_2013 = json.load(f)
for q in data_2013["questions"]:
    if q.get("sort_order") == 2:
        q["correct_answer"] = "B"
        q["answer"] = "B"
    if q.get("sort_order") == 10:
        q["explanation"] = """10. [A] found 找到；碰到
[B] studied 研究
[C] chosen 选择；选中
[D] identified 确认；认出；发现

【考点提炼】句内语义。正确率：73%
【解题思路】空格部分 ______ randomly for... 修饰 the few others，指“在同一天中被随机挑选中参加面试的其他几位申请者”。回顾介绍大学录取过程中的面试安排，由关键词 randomly 可推知，“其他几位申请者”与“某位申请者”在同一天参加面试是随机的，应该是随机选择的结果，[C]正确。
【错项排除】[A]表示“找到，发现一直在寻找的事物”，[D]表示“确认身份、属性、特点”或“发现某物或其本质”时，均有明确的目的性，与 randomly 所体现的随机性相悖；found 还可表示“（意外或偶然地）碰到（to discover sb/sth unexpectedly or by chance）”，虽包含偶然性，但申请者显然不是被“偶然碰到或发现”的，而是经历了“提交申请-被挑选-安排面试时间-参加面试”的过程；“被随机研究”与“大学录取中的面试安排”这一主题无关，排除[B]。"""
with open(path_2013, "w", encoding="utf-8") as f:
    json.dump(data_2013, f, ensure_ascii=False, indent=2)
print("-> Corrected 2013 ky1 Q2 answer to B (external) and restored Q10 explanation!")

# 5. Restore 2020 Q7, 2001 Q5, 2008 Q12 explanations
path_2020 = "public/data/exams/f56943c1-0ba8-58fe-b7d3-061352345067.json"
with open(path_2020, "r", encoding="utf-8") as f:
    data_2020 = json.load(f)
for q in data_2020["questions"]:
    if q.get("sort_order") == 7:
        q["explanation"] = """7. [A] forget 忘记；忽略
[B] regret 后悔；遗憾
[C] finish 完成；结束
[D] avoid 避免；躲避

【考点提炼】上下文语义+动词辨析。
【解题思路】This means that...（这也就是说……）提示本句继上句“官方警告”引出相应的逻辑结论（即官方认定的可取做法）。而根据已有信息“人们应该______将土豆烤脆，拒绝薄皮披萨……”不难判断“脆土豆片和薄脆皮披萨一样，均为需抵制的高温烹制食品”，选项中只有[D] avoid 与 reject 语义一致，avoid doing sth 意为“（刻意）避免做某事”。
【错项排除】其他三项虽然均可接 doing sth，分别表示“忘记做过某事”、“后悔做了某事”以及“完成了某事”，但均不合文意。"""
with open(path_2020, "w", encoding="utf-8") as f:
    json.dump(data_2020, f, ensure_ascii=False, indent=2)
print("-> Restored 2020 ky1 Q7 explanation!")

path_2001 = "public/data/exams/2c892204-071f-5943-86be-d49bca93fe71.json"
with open(path_2001, "r", encoding="utf-8") as f:
    data_2001 = json.load(f)
for q in data_2001["questions"]:
    if q.get("sort_order") == 5:
        q["explanation"] = """5. [A] publicity （媒体的）关注，宣传，公诸于众
[B] penalty 处罚，罚款
[C] popularity 受欢迎，普遍，流行
[D] peculiarity 特性，怪癖

【试题考点】逻辑语义搭配。
【解题思路】首段提及政府欲禁止媒体买断目击者提供的案件消息，本段说明大法官欲采取具体行动实施该禁令，即引入“规定媒体购买目击者信息违法”的草案，即“反对公开案件信息”，此处符合“严格控制案件公开程度”的只有 publicity“（报纸、电视等媒体对某人或某物的）关注，报道”。give publicity to sth 为常用搭配，指“将某事宣扬、公布于世”。故[A]为正确答案。
【错项排除】其他项都与 publicity 词形相近，但三项语义均不符合上下文逻辑。"""
with open(path_2001, "w", encoding="utf-8") as f:
    json.dump(data_2001, f, ensure_ascii=False, indent=2)
print("-> Restored 2001 ky1 Q5 explanation!")

path_2008 = "public/data/exams/d80926ab-1841-5d1f-a999-56773986c46d.json"
with open(path_2008, "r", encoding="utf-8") as f:
    data_2008 = json.load(f)
for q in data_2008["questions"]:
    if q.get("sort_order") == 12:
        q["explanation"] = """12. [A] missions 重要任务；使命；天职
[B] fortunes 时运；运气；财富
[C] interests 兴趣；利益
[D] careers 事业；成就

【考点提炼】名词辨析+熟词僻意。正确率：36%
【解题思路】由13题选项均为及物动词判断，as引导非限定性定语从句（即正如他们中的精英的……所表明的那样；其中as指代前文and have contributed...），对主句内容“这一族群对西方知识文化生活贡献巨大”进行补充说明，故从句内容只能涉及“精英们做出贡献的证据、体现”；而已知as从句中主语为“the careers of their elites（族群中精英的事业成就）”，因此判断空格处只能表示“（这些精英们的）成就、成功”，[D]符合文意，该词此处取其僻意：（事业的）成功，成就。
【错项排除】[A]的两层含义“客观（硬性的）任务”和“主观（认定的）使命”均不涉及内容是否得以完成或实现，无法体现贡献巨大。[B]可以表示“物质财富”，但“有钱”不等同于“贡献大”；也可以表示“个人、家庭、国家等的发展变化趋势、际遇”，或“影响人生的机会、运气”，两者同属偶然性因素，不足以证明“贡献颇大”。[C]可表示“个人兴趣或爱好”、“利益或好处”，但“感兴趣不等于擅长”，“有利益不等于贡献大”，排除。"""
with open(path_2008, "w", encoding="utf-8") as f:
    json.dump(data_2008, f, ensure_ascii=False, indent=2)
print("-> Restored 2008 ky1 Q12 explanation!")

# 6. Update version.json
with open("public/data/version.json", "r", encoding="utf-8") as f:
    v = json.load(f)

v_hash = hashlib.md5(f"round12-{datetime.now(timezone.utc).isoformat()}".encode('utf-8')).hexdigest()[:12]
v["version"] = f"2026.10.16.r12.{v_hash}"
v["updated_at"] = datetime.now(timezone.utc).isoformat()
v["calibration_round"] = 12

with open("public/data/version.json", "w", encoding="utf-8") as f:
    json.dump(v, f, ensure_ascii=False, indent=2)
print(f"-> Updated version.json: version={v['version']}")

print("=== Round 12 Restoration Complete! ===")
