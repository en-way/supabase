import json
import os
import glob
import re
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Round 4 Deep Calibration: Part B Text, Options, and Broken Explanations...")

# Build a map of (year, category_id) -> filepath
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
# 1. Part B Passages & Options Fixes
# ==============================================================================

# A. 2022 ky2 Part B
fpath, d_2022_ky2 = get_exam(2022, "ky2")
p_2022_ky2_text = """Directions: Read the following text and answer the questions by choosing the most suitable subheading from the list A-G for each of the numbered paragraphs (41-45). There are two extra subheadings which you do not need to use. Mark your answers on the ANSWER SHEET. (10 points)

[A] Make It a Habit.
[B] Don't Go It Alone.
[C] Start Low, Go Slow.
[D] Talk With Your Doctor.
[E] Listen to Your Body.
[F] Go Through the Motions.
[G] Round Out Your Routine.

How to Get Active Again

Getting back into exercise can be a challenge in the best of times, but with gyms and in-person exercise classes off-limits to many people these days, it can be tricky to know where to start. And it's important to get the right dose of activity. "Too much too soon either results in injury or burnout," says Mary Yoke, PhD, a faculty member in the kinesiology department at Indiana University in Bloomington. The following simple strategies will help you return to exercise safely after a break.

[41] ____________________
Don't try to go back to what you were doing before your break. If you were walking 3 miles a day, playing 18 holes of golf three times a week, or lifting 10-pound dumbbells for three sets of 10 reps, reduce activity to half a mile every other day, or nine holes of golf once a week with short walks on other days, or use 5-pound dumbbells for one set of 10 reps. Increase time, distance, and intensity gradually. "This isn't something you can do overnight," says Keri L. Denay, MD, lead author of a recent American College of Sports Medicine advisory that encourages Americans to not overlook the benefits of activity during the pandemic. But you will reap benefits such as less anxiety and improved sleep right away.

[42] ____________________
If you're breathing too hard to talk in complete sentences, back off. If you feel good, go a little longer or faster. Feeling wiped out after a session? Go easier next time. And stay alert to serious symptoms, such as chest pain or pressure, severe shortness of breath or dizziness, or faintness, and seek medical attention immediately.

[43] ____________________
Consistency is the key to getting stronger and building endurance and stamina. Ten minutes of activity per day is a good start, says Marcus Jackovitz, DPT, a physical therapist at the University of Miami Hospital. All the experts we spoke with highly recommend walking because it's the easiest, most accessible form of exercise. Although it can be a workout on its own, if your goal is to get back to Zumba classes, tennis, cycling, or any other activity, walking is also a great first step.

[44] ____________________
Even if you can't yet do a favorite activity, you can practice the moves. With or without a club or racket, swing like you're hitting the ball. Paddle like you're in a kayak or canoe. Mimic your favorite swimming strokes. The action will remind you of the joy the activity brought you and prime your muscles for when you can get back to it, Jackovitz says.

[45] ____________________
Exercising with others "can keep you accountable and make it more fun, so you're more likely to do it again," Jackovitz says. You can do activities such as golf and tennis or take a walk with others and still be socially distant. But when you can't connect in person, consider using technology. Chat on the phone with a friend while you walk around your neighborhood. FaceTime with a relative as you strength train or stretch at home. You can also join a livestream or on-demand exercise class."""

d_2022_ky2["passages"][5]["content"] = p_2022_ky2_text
options_2022_ky2 = [
    {"key": "A", "text": "Make It a Habit", "value": "A"},
    {"key": "B", "text": "Don't Go It Alone", "value": "B"},
    {"key": "C", "text": "Start Low, Go Slow", "value": "C"},
    {"key": "D", "text": "Talk With Your Doctor", "value": "D"},
    {"key": "E", "text": "Listen to Your Body", "value": "E"},
    {"key": "F", "text": "Go Through the Motions", "value": "F"},
    {"key": "G", "text": "Round Out Your Routine", "value": "G"},
]
for q in d_2022_ky2["questions"]:
    so = q["sort_order"]
    if 41 <= so <= 45:
        q["options"] = list(options_2022_ky2)
        if so == 45:
            q["explanation"] = q["explanation"].replace("\n\n52", "").strip()
save_exam(fpath, d_2022_ky2)
print("Updated 2022 ky2 Part B passage & Q41-Q45 options.")

# B. 2021 ky2 Part B
fpath, d_2021_ky2 = get_exam(2021, "ky2")
p4_text = d_2021_ky2["passages"][4]["content"]
if p4_text.startswith("e're"):
    d_2021_ky2["passages"][4]["content"] = "W" + p4_text

p_2021_ky2_text = """Directions: Read the following text and match each of the numbered sections (Questions 41-45) with the most suitable heading from the list A-G. Mark your answers on the ANSWER SHEET. (10 points)

[A] Stay calm.
[B] Stay humble.
[C] Decide whether to wait.
[D] Be realistic about the risks.
[E] Don't make judgements.
[F] Identify a shared goal.
[G] Ask permission to disagree.

How to disagree with someone more powerful than you

Your boss proposes a new initiative you think won't work. Your senior colleague outlines a project timeline you believe is unrealistic. What do you say when you disagree with someone who has more power than you do? How do you decide whether it's worth speaking up? And if you do, what exactly should you say? Here's how to disagree with someone more powerful than you.

[41] ____________________
You may decide it's best to hold off on voicing your opinion. Maybe you haven't finished thinking the problem through, or you want to get a clearer sense of what the group thinks. If you think other people are going to disagree, too, you might want to gather your army first. People can contribute experience or information to your thinking — all the things that would make the disagreement stronger or more valid. It's also a good idea to delay the conversation if you are in a meeting or other public space. Discussing the issue in private will make the powerful person feel less threatened.

[42] ____________________
Before you share your thoughts, think about what the powerful person cares about — it may be the credibility of their team or getting a project done on time. You're more likely to be heard if you can connect your disagreement to a higher purpose. When you do speak up, don't assume the link will be clear. You'll want to state it overtly, contextualizing your statements so that you're seen not as a disagreeable subordinate but as a colleague who's trying to advance a common objective. The discussion will then become more like a chess game than a boxing match.

[43] ____________________
This step may sound overly deferential, but it's a smart way to give the powerful person psychological safety and control. You can say something like, "I know we seem to be moving toward a first-quarter commitment here. I have reasons to think that won't work. I'd like to lay out my reasoning. Would that be OK?" This gives the person a choice, allowing him to verbally opt in. And, assuming he says yes, it will make you feel more confident about voicing your disagreement.

[44] ____________________
You might feel your heart racing or your face turning red, but do whatever you can to remain neutral in both your words and actions. When your body language communicates reluctance or anxiety, it undercuts the message. It sends a mixed message, and your counterpart gets to choose what signals to read. Deep breaths can help, as can speaking more slowly and deliberately. When we feel panicky, we tend to talk louder and faster. Simply slowing the pace and talking in an even tone helps the other person cool down and does the same for you. It also makes you seem confident, even if you aren't.

[45] ____________________
Emphasize that you're only offering your opinion, not gospel truth. It may be a well-informed, well-researched opinion, but it's still an opinion, so talk tentatively and slightly understate your confidence. Instead of saying: "If we set an end-of-quarter deadline, we will never make it," say, "This is just my opinion, but I don't see how we will make that deadline." Having asserted your opinion (as a position, not as a fact), demonstrate equal curiosity about other views. Remind the person that this is your point of view, and then invite critique. Be open to hearing other opinions."""

d_2021_ky2["passages"][5]["content"] = p_2021_ky2_text
options_2021_ky2 = [
    {"key": "A", "text": "Stay calm", "value": "A"},
    {"key": "B", "text": "Stay humble", "value": "B"},
    {"key": "C", "text": "Decide whether to wait", "value": "C"},
    {"key": "D", "text": "Be realistic about the risks", "value": "D"},
    {"key": "E", "text": "Don't make judgements", "value": "E"},
    {"key": "F", "text": "Identify a shared goal", "value": "F"},
    {"key": "G", "text": "Ask permission to disagree", "value": "G"},
]
for q in d_2021_ky2["questions"]:
    so = q["sort_order"]
    if 41 <= so <= 45:
        q["options"] = list(options_2021_ky2)
    elif so == 22:
        q["explanation"] = """22. AT&T is cited to show ________.
22. 文中引用美国电话电报公司是为了说明 ________。
[A] an alternative to the fire-and-hire strategy
［A］“先裁后聘”策略的替代方案
[B] an immediate need for government support
［B］当前亟需政府支持
[C] the importance of staff appraisal standards
［C］工作人员考核标准的重要性
[D] the characteristics of reskilling programs
［D］再培训方案的特点

［精准定位］第二段②句指出，面对技能需求问题，大多数公司的做法是解雇技能过时的员工，用掌握紧缺技能的人取而代之，即“先裁后聘”策略。③句转而指出，情况并非总是如此，并以④句AT&T的做法为例予以说明：AT&T选择了大规模的技能再培训方案而非“先裁后聘”策略，为反其道而行之提供了一个完美范例。故引用AT&T旨在说明再培训方案能够很好地替代“先裁后聘”策略，［A］正确。
［命题解密］正确项［A］是对④句 decided to do a massive reskilling program rather than go with a fire-and-hire strategy 的准确概括。
［B］利用⑥句the focus usually turns to government to handle干扰，但“让政府出手”是“宏观经济层面”的解决方案，而“AT&T的反常规做法”是“公司层面”的解决方案，两者角度不同。［C］由④句对AT&T的评价a gold standard（完美范例/黄金标准）和②句大多数公司的做法let go of workers whose skills are no longer in demand（解雇技能过时的员工）杂糅捏造而来，文中并未讨论“员工的考核标准”。［D］中reskilling programs虽提到了④句AT&T的方案，但characteristics偏离文意，作者引用AT&T意在说明“再培训”方案可以替代常规的“先裁后聘”策略，而非介绍前者的具体特点。
［技巧总结］本题为写作目的题，解题关键在于区分论点和论据，并理解举例的目的是为了支撑观点。具体看本题：第二段②句先指出大多数公司在面对技能不匹配问题时倾向于先裁后聘，随后③句转而提出“这种做法并非必然”的论点，接着④句引用AT&T予以例证：AT&T没有采用常规的“先裁后聘”策略，而是对员工进行了大规模的技能再培训。该例子旨在论证③句，也即与传统“先裁后聘”策略不同的其他方案，故［A］正确。"""
save_exam(fpath, d_2021_ky2)
print("Updated 2021 ky2 Part B passage, options & Q22 explanation.")

# C. 2010 ky1 Part B
fpath, d_2010_ky1 = get_exam(2010, "ky1")
p5 = d_2010_ky1["passages"][5]["content"]
p5 = p5.replace("were on the wrong planet. Part B\n\n", "")
p5 = p5.replace("were on the wrong planet. Part B \n\n", "")
p5 = p5.replace("were on the wrong planet. Part B\n", "")
p5 = p5.replace("[A] OThe", "[A] The")
p5 = p5.replace("[B] ORetail", "[B] Retail")
d_2010_ky1["passages"][5]["content"] = p5.strip()
save_exam(fpath, d_2010_ky1)
print("Cleaned 2010 ky1 Part B passage.")

# D. 2011 ky1 Part B
fpath, d_2011_ky1 = get_exam(2011, "ky1")
p5 = d_2011_ky1["passages"][5]["content"]
p5 = re.sub(r'^[、\s\.\.\.a-zA-Z\s]+But most find it difficult\.\.\.\s*', '', p5)
p5 = p5.replace("[C] OEqually", "[C] Equally")
d_2011_ky1["passages"][5]["content"] = p5.strip()
save_exam(fpath, d_2011_ky1)
print("Cleaned 2011 ky1 Part B passage.")

# E. 2012 ky1 Part B
fpath, d_2012_ky1 = get_exam(2012, "ky1")
p5 = d_2012_ky1["passages"][5]["content"]
if p5.startswith("Part B I "):
    p5 = p5[len("Part B I "):]
p5 = p5.replace("wonder at those marvels O You are the lucky inheritor'1", "wonder at those marvels. You are the lucky inheritor")
d_2012_ky1["passages"][5]["content"] = p5.strip()
save_exam(fpath, d_2012_ky1)
print("Cleaned 2012 ky1 Part B passage.")

# F. 2013 ky1 Part B
fpath, d_2013_ky1 = get_exam(2013, "ky1")
p5 = d_2013_ky1["passages"][5]["content"]
if p5.startswith("7 Part B I "):
    p5 = p5[len("7 Part B I "):]
d_2013_ky1["passages"][5]["content"] = p5.strip()
save_exam(fpath, d_2013_ky1)
print("Cleaned 2013 ky1 Part B passage.")

# G. 2014 ky1 Part B
fpath, d_2014_ky1 = get_exam(2014, "ky1")
p5 = d_2014_ky1["passages"][5]["content"]
if p5.startswith("Part B  "):
    p5 = p5[len("Part B  "):]
d_2014_ky1["passages"][5]["content"] = p5.strip()
save_exam(fpath, d_2014_ky1)
print("Cleaned 2014 ky1 Part B passage.")

# H. 2022 ky1 Part B
fpath, d_2022_ky1 = get_exam(2022, "ky1")
p5 = d_2022_ky1["passages"][5]["content"]
if p5.startswith("B D Part B "):
    p5 = p5[len("B D Part B "):]
d_2022_ky1["passages"][5]["content"] = p5.strip()
save_exam(fpath, d_2022_ky1)
print("Cleaned 2022 ky1 Part B passage.")

# I. 2005 ky1 Part B
fpath, d_2005_ky1 = get_exam(2005, "ky1")
p5 = d_2005_ky1["passages"][5]["content"]
p5 = re.sub(r'^N\s+O\s+What to do\?', 'What to do?', p5)
p5 = p5.replace('healt h care', 'health care')
p5 = p5.replace('crea tio o f a', 'creation of a')
p5 = p5.replace('p rov incha ving its', 'province having its')
p5 = p5.replace('VI O But', 'But')
d_2005_ky1["passages"][5]["content"] = p5.strip()
save_exam(fpath, d_2005_ky1)
print("Cleaned 2005 ky1 Part B passage.")

# J. 2013 ky2 Part B (Currency symbols)
fpath, d_2013_ky2 = get_exam(2013, "ky2")
p5 = d_2013_ky2["passages"][5]["content"]
for f_curr, pound_curr in [("f 60", "£60"), ("f 40", "£40"), ("f 130,000", "£130,000"), ("f 1", "£1"), ("f 21", "£21"), ("f 16", "£16"), ("f 12", "£12")]:
    p5 = p5.replace(f_curr, pound_curr)
d_2013_ky2["passages"][5]["content"] = p5
save_exam(fpath, d_2013_ky2)
print("Cleaned 2013 ky2 Part B currency symbols (£).")

# K. 2016 ky2 Part B (Title spacing)
fpath, d_2016_ky2 = get_exam(2016, "ky2")
p5 = d_2016_ky2["passages"][5]["content"]
p5 = p5.replace("ActYour ShoeSize, NotYour Age", "Act Your Shoe Size, Not Your Age")
d_2016_ky2["passages"][5]["content"] = p5
save_exam(fpath, d_2016_ky2)
print("Cleaned 2016 ky2 Part B title spacing.")


# ==============================================================================
# 2. Broken / Truncated Explanations Restoration
# ==============================================================================

# A. 2001 ky1 Q25
fpath, d_2001_ky1 = get_exam(2001, "ky1")
for q in d_2001_ky1["questions"]:
    if q["sort_order"] == 25:
        q["explanation"] = """25. Digital divide is something ________.
25. 数字鸿沟是一种 ________ 事物。
[A] getting worse because of the Internet
［A］因互联网而恶化的
[B] the rich countries are responsible for
［B］应由富裕国家负责的
[C] the world must guard against
［C］全世界应该警惕的
[D] considered positive today
［D］如今被认为积极的

［精准定位］第一段③句提到，20年前“我”就曾谈到这种迫在眉睫的危险（looming danger），这里的 looming danger指前文提到的digital divide，即世界上信息资源丰富地区和信息资源贫乏地区之间的鸿沟。既然是世界范围的危险，当然要警惕，因此［C］正确。
［命题解密］正确项［C］是第一段③句的引申，guard against对应句中this looming danger。
［A］将网络由“对抗数字鸿沟的积极力量”改为“加大数字鸿沟的消极因素”；［B］利用第一段①句 the rich捏造干扰，但文中用其指“信息丰富”，而非“富裕国家”，且文中没有提及数字鸿沟该由谁负责；［D］将第一段④句“现在出现了对抗数字鸿沟（这一危险的）的积极因素”改为“数字鸿沟具有积极作用”。
［技巧总结］“改变不同主体之间关联”以及“部分原文信息-部分捏造信息”是事实综合题中常见干扰方式。如本题：错误项以文中词汇the internet、the rich、positive加大干扰；正确项［C］虽单纯从字面来看似在文中无所依，但其含义完全顺应作者观点，是对作者观点的合理引申。"""
save_exam(fpath, d_2001_ky1)
print("Restored 2001 ky1 Q25 explanation.")

# B. 2011 ky1 Q30
fpath, d_2011_ky1 = get_exam(2011, "ky1")
for q in d_2011_ky1["questions"]:
    if q["sort_order"] == 30:
        q["explanation"] = """30. Which of the following is the best title for the text?
30. 以下哪一项是本文最好的标题？
[A] CEOs: Where to Go?
［A］首席执行官们：路在何方？
[B] CEOs: All the Way Up?
［B］首席执行官们：一路高升？
[C] Top Managers Jump without a Net
［C］高级经理们在没有新工作的情况下辞职
[D] The Only Way Out for Top Performers
［D］高级职员们唯一的出路

［精准定位］首段介绍具体事例：美国银行总裁高调裸辞；第二、三段借分析高管裸辞的内外在原因说明这一现象的普遍性；第四至六段总评该现象：曾经是少有现象，如今更可接受、更加普遍。可见，全文都围绕着“高管裸辞”展开论述，并且“高管”和“裸辞”这两个主题关键词在文中反复出现，故［C］正确。
［命题解密］正确项［C］是全文主题的高度概括。
［A］、［B］首先将中心词由top managers偷换成CEOs，而CEOs是大多数高管裸辞的职业追求目标；其次以疑问形式传递的不确定口吻替换了文中作者明确的态度：高管裸辞已成趋势。［D］从末段③句的 been fundamentally inverted 以及④句 who've been hurt the worst are... stayed too long 编制出 The Only Way这一绝对性表达，但“传统规则、观念的彻底颠覆（裸辞不再是不可接受的行为）”不能等同于“高管们只有裸辞一条路可走”；再者本文为“现象分析”类型（描述、评价“高管裸辞”现象），而非“问题解决”类型（谈及“出路、解决办法”）。
［技巧总结］标题题旨在考查文章主旨，因而其解答技巧重在寻找文章主题句或主题词。主题句通常出现在三个地方：文章首段首句、文章开头转折处和文章开头现象结束处。且主题句通常是一个概括总结性的结论或者判断。纵观各段落主题句可知，全文一直都是在讲高管的裸辞，［C］正确。"""
save_exam(fpath, d_2011_ky1)
print("Restored 2011 ky1 Q30 explanation.")

# C. 2014 ky1 Q38
fpath, d_2014_ky1 = get_exam(2014, "ky1")
for q in d_2014_ky1["questions"]:
    if q["sort_order"] == 38:
        q["explanation"] = """38. According to Paragraph 3, the report suggests ________.
38. 根据第三段，报告建议 ________。
[A] an exclusive study of American history
［A］专注美国历史研究
[B] a greater emphasis on theoretical subjects
［B］更加重视理论科目
[C] the application of emerging technologies
［C］应用新兴技术
[D] funding for the study of foreign languages
［D］资助外语研究

［精准定位］第三段②句指出：报告鼓励使用新数字技术。可见［C］正确。
［命题解密］正确项［C］是对段中②句 encourages the use of new digital technologies 的同义改写。
［A］利用②句“美国历史”设置陷阱，却将插入说明“尤其要（particularly）”偷换为“专注于（exclusive）”；［B］利用③句“精心设计连贯课程”设置陷阱，而该句并没有说“更注重理论科目”，相反强调“学者们要将学识运用到实际以迎接挑战”，即“注重理论联系实际”；［D］杂糅③句“加大对教师的资助”及④句“加大外语研究力度”而成，却将资助对象由“教师”偷换为“外语研究”。
［技巧总结］本题为名副其实的细节题，解答关键也为细节题的典型思路“将选项回文定位并一一比对以判断对错”：先根据各选项核心关键词（[A] American history、[B] subjects、[C] emerging technologies、[D] foreign languages）分别定位②句、③句、②句、④句；再仔细比对原文发现[A] exclusive篡改particularly之意、[B] theoretical无从对应、[D] funding对象实为 teachers而非 study of foreign languages，唯有[C] application 对应 use、emerging 对应 digital，故正确。"""
save_exam(fpath, d_2014_ky1)
print("Restored 2014 ky1 Q38 explanation.")

# D. 2008 ky1 Q10 & Q16
fpath, d_2008_ky1 = get_exam(2008, "ky1")
for q in d_2008_ky1["questions"]:
    if q["sort_order"] == 10:
        q["explanation"] = """10. [A] normal 正常的，平常的
[B] common 常见的，共同的
[C] mean 平均的
[D] total 总的，全部的
［考点提炼］熟词僻意＋形容词辨析。正确率：14%
［解题思路］空格所在部分说明这一族群在智商测试中表现突出（do well）：得分比 100 的值高出 12 至 15 分。前文提及，这一族群比其他族群智商更高，即他们在智商测试中的得分应该高于其他族群的得分，故必然高于测试的平均值，［C］后接名词，可表示“平均的”，用法等同于 average，故正确。
［错项排除］normal value 指“标准值，正常值”，介词 of 后可以接“正常值的主体”；其次该短语表示一个区间的范围，而非某确定数值，故排除［A］。common value 指“共同价值观”，偏离上下文语境，排除［B］。total value 指“总价、总值”，而 above the total value of... 显然违背逻辑：既然是“总数值”，自然不能“高于它”，排除［D］。"""
    elif q["sort_order"] == 16:
        q["explanation"] = """16. [A] assessing 评价，评定；估价
[B] supervising 监督，指导
[C] administering 管理，治理
[D] valuing 尊重，重视
［考点提炼］熟词僻意。正确率：34%
［解题思路］句中 such as... 引出对 social effects 的举例说明，即“高智商形成的社会因素”。结合选项动词，再由已知信息“重视教育的传统”以及段首句“他们对西方知识文化的贡献巨大”可以推知，该族群在教育方面投入很大，故这一传统应该是“重视教育”，［D］正确。
［错项排除］［A］、［B］与［C］均从管理者的角度介绍某种单一因素，文中对象为“某一特定族群”，既未强调其地位，也未说明其身份，且对教育单纯的“评估、监管、管理”并不能与“贡献巨大”发生直接关联，排除这三项。"""
save_exam(fpath, d_2008_ky1)
print("Restored 2008 ky1 Q10 & Q16 explanations.")

# E. 2009 ky1 Q3, Q11, Q15
fpath, d_2009_ky1 = get_exam(2009, "ky1")
for q in d_2009_ky1["questions"]:
    if q["sort_order"] == 3:
        q["explanation"] = """3. [A] thinner 更薄的；更细的；更稀的
[B] stabler 更稳定的，更稳固的
[C] lighter 更明亮的；更轻的
[D] dimmer 更暗淡的；更愚笨的
［考点提炼］上下文语义。正确率：73%
［解题思路］由 This suggests 可推知空格句“____ 的灯泡寿命越长”是由上文实验结果“越聪明的果蝇寿命越短”得出的推论，两句之间为反向呼应的关系；而由后半句 ...not being too bright（不是特别明亮）可以判断本句涉及对“暗灯泡 vs 亮灯泡”的对比，故空格处只能为 dimmer，即“越暗的灯泡寿命越长”，dim 既表示“暗的”，还含有“愚笨的”这层喻意，恰与上句“聪明的（smarter）”反向对应，［D］正确。
［错项排除］［A］只涉及灯泡的粗细造型，而灯泡的寿命主要取决于灯丝。［B］利用常识“性能稳定的灯泡寿命长”干扰，但与上文结论“聪明的果蝇寿命短”无关。［C］与文中大逻辑相反。"""
    elif q["sort_order"] == 11:
        q["explanation"] = """11. [A] features 特征，特色
[B] influences 影响
[C] costs 代价，付出
[D] rewards 报酬，奖赏
［考点提炼］上下文语义。正确率：56%
［解题思路］空格句指出，研究含蓄地提出了一个问题：我们独有的智力到底会有怎样的 ____。上文第二段首句已明确指出“智力是代价高昂的选择（a high-priced option）”，并且后文第三段继续探讨智力消耗更多能量和给养的弊端，故此处空格词必然对应“代价（costs）”，［C］正确。
［错项排除］［A］“特征”偏离文意，文章并非在泛泛列举智力的特点；［B］“影响”过于宽泛，无法呼应前文 high-priced option 所体现的代价；［D］“报酬”与全文探讨智力负面代价的主题逻辑相反。"""
    elif q["sort_order"] == 15:
        q["explanation"] = """15. [A] if 如果
[B] unless 除非
[C] as 当……时
[D] lest 免得，以免
［考点提炼］上下文语义＋虚拟语气。正确率：75%
［解题思路］空格句意为：我们认为，____ 动物掌管实验室，它们会测定我们的……。首先“动物掌管实验室”并非真实情况，从时态 ran... would test 可知此句为虚拟语气，表达对不可能情况的假设，只有 if 符合要求，同时与前句假设“动物如果有机会，将会对人类做什么实验”相呼应，［A］正确。
［错项排除］［B］用于引出某事不会发生的唯一条件；［C］引导时间状语从句，不与虚拟语气配合表假设；［D］表“以免、免得”，不符合虚拟条件句的语义。"""
save_exam(fpath, d_2009_ky1)
print("Restored 2009 ky1 Q3, Q11, Q15 explanations.")

# F. 2005 ky1 Q12, Q19
fpath, d_2005_ky1 = get_exam(2005, "ky1")
for q in d_2005_ky1["questions"]:
    if q["sort_order"] == 12:
        q["explanation"] = """12. [A] limited (to) 局限于
[B] committed (to) 致力于
[C] dedicated (to) 献身于
[D] exposed (to) 接触到，体验到
［考点提炼］动词短语。正确率：55%
［解题思路］when (people are) ____ to it often enough 限定人对气味由不敏感而变敏感的条件（其中 it 指代上文的 a certain smell）：使人……这种气味足够频繁。选项都涉及“置于这种气味当中”，但空格词应能体现“闻”这一动作，即常常闻这一气味，会变得敏感。符合要求的只能是［D］，exposed 与 to 搭配，含“使接触、使熟悉”之意，文中 exposed to it often enough 表示“闻得足够多、足够熟悉”。
［错项排除］［A］“局限于”偏离语境；［B］与［C］主语通常是人主动“致力于、献身于某事业”，不能与被动语态中人接触气味搭配。"""
    elif q["sort_order"] == 19:
        q["explanation"] = """19. [A] available (for) 可得到的，可用的
[B] reliable 可信赖的，可靠的
[C] identifiable 可识别的
[D] (be) suitable (for) 适合的
［考点提炼］形容词辨析。正确率：46%
［解题思路］④句回应①句，进一步表明大脑认定的气味感受器的最佳工作方式。smell receptors 与 signals 是“工具 vs 对象”的关系，相当于“鼻子 vs 气味”的关系，只有 available (for) 能表达这种关系，即“气味接收器随时可用于接收不熟悉和紧急信号（鼻子随时能闻到相应气味）”，［A］正确。
［错项排除］［B］强调某人或某物值得信赖；［D］强调适合于某目的，后接 signals 不符合语义搭配；［C］弄反了主客体关系，“气味对感受器可识别”合理，“感受器对气味可识别”违背常识。"""
save_exam(fpath, d_2005_ky1)
print("Restored 2005 ky1 Q12, Q19 explanations.")

# G. 2006 ky1 Q6, Q11
fpath, d_2006_ky1 = get_exam(2006, "ky1")
for q in d_2006_ky1["questions"]:
    if q["sort_order"] == 6:
        q["explanation"] = """6. [A] cover 覆盖；行走，占据
[B] change 变化
[C] range 变化，变动
[D] differ 看法不一致，不同
［考点提炼］动词辨析。正确率：58%
［解题思路］空格句含义为：（对无家可归者的）估算数字在 60 万到 300 万之间。空格处动词应可以接 anywhere from... to... 结构，表示“从 60 万到 300 万”的变化范围，［C］ range 可以与 from... to... 连用，表示“（在一定范围内）变化，变动”，符合文意。
［错项排除］［A］ cover 后接数字时指“行走一段距离”或“占一片面积”，但宾语为固定数值而非数值范围；［B］接 from A to B 时表示“从 A 变成 B”，强调质变而非范围变动；［D］ differ 表示不同，estimates differ 后面接介词短语 on the homeless population，不接范围数值。"""
    elif q["sort_order"] == 11:
        q["explanation"] = """11. [A] Hence 因此
[B] But 但是
[C] Even 甚至，连，即使
[D] Only 只有；不过（连词）
［考点提炼］句内逻辑关系。正确率：52%
［解题思路］空格上文①句指出，找到能够帮助日益增多的无家可归者的方法变得日益困难；空格句继而指出，即使无家可归者设法找到提供三餐与住宿的地方，仍然有很多人每天大部分时间流落街头。主句中关键词 still 暗示从句和主句间为让步转折逻辑，Even when 意为“即使当……时”，契合让步语境，［C］正确。
［错项排除］［A］表因果；［B］为并列连词，不能置于 when 从句前引导让步状语；［D］ Only when 引导充分必要条件，与主句 still 矛盾。"""
save_exam(fpath, d_2006_ky1)
print("Restored 2006 ky1 Q6, Q11 explanations.")

# H. 2007 ky1 Q12
fpath, d_2007_ky1 = get_exam(2007, "ky1")
for q in d_2007_ky1["questions"]:
    if q["sort_order"] == 12:
        q["explanation"] = """12. [A] Since 既然
[B] If 如果
[C] Unless 除非
[D] While 然而
［考点提炼］句内逻辑关系。正确率：60%
［解题思路］空格词表示两个分句之间的逻辑关系。前半句指出，多数领导者力求继续维持天主教作为国家官方宗教；后半句指出，一些领导人试图结束这一排他局面；其中，most leaders 与 some (leaders)、sought to maintain 与 sought to end、Catholicism 与 other faiths 分别形成鲜明对比，凸显分歧，只有［D］符合这一逻辑，while 用于“对比两项内容”，展示领导层间就宗教问题的分歧，与段首主旨句契合。
［错项排除］［A］既可表时间，也可表因果，均不符合两派领导人意见分歧的对比语境；［B］表假设条件；［C］引导反面条件“除非”。"""
save_exam(fpath, d_2007_ky1)
print("Restored 2007 ky1 Q12 explanation.")

# I. 2013 ky1 Q19
fpath, d_2013_ky1 = get_exam(2013, "ky1")
for q in d_2013_ky1["questions"]:
    if q["sort_order"] == 19:
        q["explanation"] = """19. ［A］ achieve实现，达到 
［B］ undo使无效，取消，废除
［C］ maintain 保持，维持 
［D］ disregard 忽视，无视
［考点提炼］上下文语义。正确率：25%
［解题思路］根据上文，后一位申请者的分数被无端降低了 0.075。本句转折，指出 0.075 虽然听起来微乎其微，但却需要多出 30 分的 GMAT 成绩来抵消其影响。面试分数降低，GMAT 分数提高，这是两相抵消的过程。［B］ undo 指“消除、抵消其不良影响”，符合文意。
［错项排除］［A］侧重“成功完成某事或取得好的结果”；［C］侧重“维持现状、保持水平”；但“达到、维持面试分数降低这一影响”均与文意相悖；［D］表示“不理会，忽视”，但仅仅“忽视面试分数降低的影响”并不需要 GMAT 成绩高出 30 分，故排除。"""
save_exam(fpath, d_2013_ky1)
print("Restored 2013 ky1 Q19 explanation.")

# J. 2015 ky1 Q12
fpath, d_2015_ky1 = get_exam(2015, "ky1")
for q in d_2015_ky1["questions"]:
    if q["sort_order"] == 12:
        q["explanation"] = """12. ［A］ drive驾驶；驱使；促进 
［B］ observe观察；注意到
［C］ confuse使困惑；混淆 
［D］ limit限制
［考点提炼］句内语义+动词辨析。
［解题思路］空格句中 that 指代 many mechanisms，空格词考查“许多机制”与“我们（选择基因相似的朋友）”之间的关系。③句提出：或许是嗅觉基因使我们凑到相似的环境中去，but 转而引出“事情可能不会这么简单（暗示有其他原因）”。因此，④句是对③句中 there is more to it 的进一步解释：我们之所以会选择基因相似的人做朋友，还可能存在许多机制的协同作用，空格词应当与③句中 draw（吸引）具有相同的功能和作用，即“吸引，驱使我们去选择朋友”，［A］ drive 正确。
［错项排除］［B］表示“观察”，强调用眼睛看，主语 many mechanisms 不能实施该动作；［C］表示“使困惑”；［D］表示“限制，制约”，此两项均偏向负面，不符合解释选择朋友机制的语境。"""
save_exam(fpath, d_2015_ky1)
print("Restored 2015 ky1 Q12 explanation.")

# K. 2018 ky1 Q18, Q19
fpath, d_2018_ky1 = get_exam(2018, "ky1")
for q in d_2018_ky1["questions"]:
    if q["sort_order"] == 18:
        q["explanation"] = """18. [A] forced 勉强的；被迫的
[B] willing 乐意的；心甘情愿的
[C] hesitant 犹豫的；不情愿的
[D] entitled 有权做……的，有资格的
［考点提炼］句内语义+形容词辨析。
［解题思路］空格后 demonstrating that they trusted his leadership 表明这些没有被欺骗过的孩子信任测试员的指挥，既然如此，他们肯定“乐意配合测试员的下一步行动”，［B］ willing 符合文意。
［错项排除］［A］ forced 表示“违背个人意愿、被迫做某事”；［C］ hesitant 表示“迟疑不决的”，两项均与“信任测试员指挥”相悖；［D］ entitled 表示“被赋予法律/正式权利或资格”，文中实验为游戏性质，与权利无关。"""
    elif q["sort_order"] == 19:
        q["explanation"] = """19. [A] In contrast 相比之下 
[B] As a result 作为结果；因此
[C] On the whole 总体而言 
[D] For instance 例如
［考点提炼］上下文语义逻辑+介词短语辨析。
［解题思路］上文“大部分没有被欺骗过的孩子乐意配合测试员”与空格句“30个孩子中只有5个参与了后续活动”存在明显语义对比（the majority vs only five），也与“两组孩子分别面对可信 vs 不可信行为，反应截然不同”的实验预期相符，［A］ In contrast 用于引出与前述内容完全不同的对照情形，符合文意。
［错项排除］［B］ As a result 引出结果；［C］ On the whole 用于引出总体概括；［D］ For instance 用于引出事例；空格后为两组受试儿童的对比数据，故排除其他三项。"""
save_exam(fpath, d_2018_ky1)
print("Restored 2018 ky1 Q18, Q19 explanations.")

# L. 2020 ky1 Q16
fpath, d_2020_ky1 = get_exam(2020, "ky1")
for q in d_2020_ky1["questions"]:
    if q["sort_order"] == 16:
        q["explanation"] = """16. ［A］ made 做；构成 
［B］ served 端上（菜、饮料）；为……服务
［C］ saved 拯救；节省；保存 
［D］ used 使用
［考点提炼］上下文语义+动词辨析。
［解题思路］空格所在句直译为：在周日，一块煮牛肉和一些清蒸蔬菜总可以被端上桌，没有约克郡布丁或葡萄酒。结合上文中提到的食品标准局的健康建议和②句反诘（这样的生活还值得过吗？）可知，这里是在说“周日人们并非不能只吃清淡的煮牛肉和清蒸蔬菜”，但如此一来生活就失去了乐趣，serve up 为固定动词短语，意为“（为某人）端上、提供（饭菜）”，故［B］为正确选项。
［错项排除］make up 意为“组成，构成”，脱离餐饮语境；save up 宾语通常为钱财，指攒钱；use up 意为“用光，耗尽”，均不符合文意。"""
save_exam(fpath, d_2020_ky1)
print("Restored 2020 ky1 Q16 explanation.")

# M. 2021 ky1 Q2, Q14
fpath, d_2021_ky1 = get_exam(2021, "ky1")
for q in d_2021_ky1["questions"]:
    if q["sort_order"] == 2:
        q["explanation"] = """2. [A] alternatively 要不，或者 
[B] formally 正式地；形式上
[C] accidentally 意外地；偶然地 
[D] generally 通常；普遍地，一般地
［考点提炼］上下文语义+副词辨析。
［解题思路］由上题分析可知，②句是在说明流体智力随年龄变化的规律，具有普遍性、一般性。且由③句核心信息“（但）科学家发现大脑某些变化可能并非不可避免”也可反推“流体智力随变老而衰退”只是一般情形。［D］ generally 常用于“引出在大多数情况下成立的现象、规律”，符合文意。
［错项排除］［A］ alternatively 用于引出另一种替代方案；［B］ formally 强调“正式性、严肃性”，不用于形容生理自然变化；［C］ accidentally 表示偶然发生的少数情况，与普遍规律相悖。"""
    elif q["sort_order"] == 14:
        q["explanation"] = """14. [A] alter 改变；修改
[B] spread 传播；伸展
[C] remove 移动；去除
[D] explain 说明；解释 
［考点提炼］上下文语义。
［解题思路］空格句指出，希望未来的研究可以 ____ 这些差异。“这些差异”指前一句所述“女性身上的这种联系或许（may be）与免疫力变化相关，男性身上的这种联系似乎（appear to）与免疫系统无关”。其中 may be, appear to 均带有明显的推测语气，暗含还需进一步研究确认。空格句中 It is hoped that future studies could 针对后续研究方向传达出期盼，空格词应表示“深入研究并解释差异”，以实现“当前局限—后续研究”的呼应，［D］ explain 符合文意。
［错项排除］［A］ alter 与［C］ remove 均指向“消除差异”，暗示差异为不利因素；［B］ spread 指向“扩大差异”；而文中仅客观呈现性别差异，并未评价好坏，排除其他三项。"""
save_exam(fpath, d_2021_ky1)
print("Restored 2021 ky1 Q2, Q14 explanations.")

# N. 2003 ky1 Q1, Q9
fpath, d_2003_ky1 = get_exam(2003, "ky1")
for q in d_2003_ky1["questions"]:
    if q["sort_order"] == 1:
        q["explanation"] = """1. [A] (give) thought (to) 想过，思考
[B] (give sb a/some) idea (of) 使了解……的情况
[C] (give) opinion (to sb/on sth) 向某人提出意见
[D] (give) advice (to sb/on sth) 提建议
［试题考点］平行句子结构+固定搭配
［解题思路］①②句针对“青少年成长过程中身心都处于变化”这一现象，提示教师不应忽视这一事实，语义重点在于“教师应对此给予重视”。①句指出教师“应意识到这类变化（need to be aware of...）”，②句 they also need to... 表明其与①句的并列关系，语义重点仍在于“教师对这些变化的认识”上，同时更进一步。填入 thought 一词，与 be aware of 含义相近并更进一步，give thought to... 指“认真考虑某事”，符合作者认为教师“应关注、研究变化进而帮助学生应对变化”的总体态度，［A］项正确。
［错项排除］空格词语与 give... to 构成短语。idea 通常与介词 of 而不与 to 连用；另外，give sb an idea of sth 意为“让某人了解某事”，而文中建议对象为教师，不存在“教师让其他人了解青少年变化”这一问题，故排除［B］项。opinion 和 advice 用法相似，虽可与 give 及 to 搭配，但介词 to 后应接“人”，即 give opinion/advice to sb，而文中介词 to 之后为“how...从句”，用以说明教师应关注的内容，故排除该两项。"""
    elif q["sort_order"] == 9:
        q["explanation"] = """9. [A] displaying 展示，陈列 
[B] describing 描写，描述，描绘
[C] creating 创造，创建 
[D] exchanging 交换，交流
［试题考点］上下文语义+动宾搭配
［解题思路］空格所在短语与前文 publishing newsletters... 和后文 sponsoring book discussion clubs 并列，都是“多赢活动”的具体例子。因此空格动词应能与 students' artwork 构成搭配，并且体现出“多赢”的特点。displaying students' artwork 意为“展出学生们的艺术作品”，让更多学生的作品得到展示与认可，属于典型的多赢活动，故［A］项正确。
［错项排除］describing students' artwork 意为“描述学生作品”，显然无法作为一项组织性的活动；creating students' artwork 搭配不当，学校组织者不能“替学生创作作品”；exchanging students' artwork 强调学生之间“交换作品”，未能突出让更多学生获得他人赞赏和认可的激励目的。"""
save_exam(fpath, d_2003_ky1)
print("Restored 2003 ky1 Q1, Q9 explanations.")

print("\n--- All local JSON calibrations completed successfully. ---")
