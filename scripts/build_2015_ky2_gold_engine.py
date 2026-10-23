# -*- coding: utf-8 -*-
"""
Round 63: 2015 ky2 Gold Engine
Performs forensic reconstruction of 2015 English (Two) exam:
- Exam metadata normalization (title, total_score, pass_score)
- Passages 0-5 gold reconstruction (clean structure, restored sentences, no OCR footnotes, no directions in text)
- Questions 1-45 gold reconstruction (question_number 1..45, points 0.5/2.0, q_type, options, answers, cleaned explanations)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
import re

EXAM_PATH = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\17ca33c3-66f2-5ae0-a1ba-847f507dd6e4.json"

with open(EXAM_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. Update Exam Metadata
exam = data["exam"]
exam["title"] = "2015年全国硕士研究生招生考试英语（二）真题"
exam["total_score"] = 60.0
exam["pass_score"] = 36.0

# 2. Reconstruct Passages
passages = data["passages"]

p0_content = """In our contemporary culture, the prospect of communicating with — or even looking at — a stranger is virtually unbearable. Everyone around us seems to agree by the way they cling to their phones, even without a [1] on a subway.

It's a sad reality — our desire to avoid interacting with other human beings — because there's [2] to be gained from talking to the stranger standing by you. But you wouldn't know it, [3] into your phone. This universal protection sends the [4] "Please don't approach me."

What is it that makes us feel we need to hide [5] our screens? One answer is fear, according to Jon Wortmann, executive mental coach. We fear rejection, or that our innocent social advances will be [6] as "creep." We fear we'll be [7]. We fear we'll be disruptive. Strangers are inherently [8] to us, so we are more likely to feel [9] when communicating with them compared with our friends and acquaintances. To avoid this anxiety, we [10] to our phones. "Phones become our security blanket," Wortmann says. "They are our happy glasses that protect us from what we perceive is going to be more [11]."

But once we rip off the bandaid, tuck our smartphones in our pockets and look up, it doesn't [12] so bad. In one 2011 experiment, behavioral scientists Nicholas Epley and Juliana Schroeder asked commuters to do the unthinkable: Start a [13]. They had Chicago train commuters talk to their fellow [14]. "When Dr. Epley and Ms. Schroeder asked other people in the same train station to [15] how they would feel after talking to a stranger, the commuters thought their [16] would be more pleasant if they sat on their own," the New York Times summarizes. Though the participants didn't expect a positive experience, after they [17] with the experiment, "not a single person reported having been snubbed." [18], these commutes were reportedly more enjoyable compared with those without communication, which makes absolute sense, [19] human beings thrive off of social connections. It's that [20]: Talking to strangers can make you feel connected."""

p1_content = """A new study suggests that contrary to most surveys, people are actually more stressed at home than at work. Researchers measured people's cortisol, which is a stress marker, while they were at work and while they were at home and found it higher at what is supposed to be a place of refuge.

Further contradicting conventional wisdom, we found that women as well as men have lower levels of stress at work than at home, writes one of the researchers, Sarah Damaske. In fact women even say they feel better at work, she notes. It is men, not women, who report being happier at home than at work. Another surprise is that the findings hold true for both those with children and without, but more so for nonparents. This is why people who work outside the home have higher happiness levels and lower stress levels than those who do not work outside the home.

What explains this difference? For working women, it's not because, as some people believe, the roles of women and men have changed. Working women still experience the blurring of their roles as breadwinners and housewives. But Damaske suggests that work provides a sense of accomplishment and a social support network that home doesn't.

But it's not just a gender thing. At work, people pretty much know what they're supposed to be doing: working, making money, doing the tasks they have to do in order to draw an income. The bargain is very pure: Employee puts in hours of physical or mental labor and employee draws out life-sustaining moola.

On the home front, however, people have no such clarity. Rare is the household in which the division of labor is so clinically and methodically laid out. There are a lot of tasks to be done, there are inadequate rewards for most of them. Your home colleagues - your family - have no clear rewards for their labor; they need to be talked into it, or if they're teenagers, threatened with complete removal of all electronic devices. Plus, they're your family. You cannot fire your family. You never really get to go home from home.

So it's not surprising that people are more stressed at home. Not only are the tasks apparently infinite, the co-workers are much harder to motivate."""

p2_content = """For years, studies have found that first-generation college students - those who do not have a parent with a college degree - lag other students on a range of education achievement factors. Their grades are lower and their dropout rates are higher. But since such students are most likely to advance economically if they succeed in higher education, colleges and universities have pushed for decades to recruit more of them. This has created "a paradox" in that recruiting first-generation students, but then watching many of them fail, means that higher education has "continued to reproduce and widen, rather than close" an achievement gap based on social class, according to the depressing beginning of a paper forthcoming in the journal Psychological Science.

But the article is actually quite optimistic, as it outlines a potential solution to this problem, suggesting that an approach (which involves a one-hour, next-to-no-cost program) can close 63 percent of the achievement gap (measured by such factors as grades) between first-generation and other students.

The authors of the paper are from different universities, and their findings are based on a study involving 147 students (who completed the project) at an unnamed private university. First generation was defined as not having a parent with a four-year college degree. Most of the first-generation students (59.1 percent) were recipients of Pell Grants, a federal grant for undergraduates with financial need, while this was true only for 8.6 percent of the students with at least one parent with a four-year degree.

Their thesis - that a relatively modest intervention could have a big impact - was based on the view that first-generation students may be most lacking not in potential but in practical knowledge about how to deal with the issues that face most college students. They cite past research by several authors to show that this is the gap that must be narrowed to close the achievement gap.

Many first-generation students "struggle to navigate the middle-class culture of higher education, learn the 'rules of the game,' and take advantage of college resources," they write. And this becomes more of a problem when colleges don't talk about the class advantages and disadvantages of different groups of students. "Because US colleges and universities seldom acknowledge how social class can affect students' educational experiences, many first-generation students lack insight about why they are struggling and do not understand how students 'like them' can improve.\""""

p3_content = """Even in traditional offices, the lingua franca of corporate America has gotten much more emotional and much more right-brained than it was 20 years ago, says Harvard Business School historian Nancy Koehn. She started spinning off examples. "If you and I parachuted back to Fortune 500 companies in 1990, we would see much less frequent use of terms like journey, mission, passion. There were goals, there were strategies, there were objectives, but we didn't talk about energy; we didn't talk about passion."

Koehn pointed out that this new era of corporate vocabulary is very "team"-oriented - and that is not by coincidence. "Let's not forget sports - in male-dominated corporate America, it's still a big deal. It's not explicitly conscious; it's the idea that I'm a coach, and you're my team, and we're in this together. There are lots and lots of CEOs in very different companies, but most think of themselves as coaches and this is their team and they want to win."

These terms are also intended to infuse work with meaning - and, as Rakesh Khurana, another professor, points out, increase allegiance to the firm. "You have the importation of terminology that historically used to be associated with non-profit organizations and religious organizations: terms like vision, values, passion, and purpose," said Khurana.

This new focus on personal fulfillment can help keep employees motivated amid increasingly loud debates over work-life balance. The "mommy wars" of the 1990s are still going on today, prompting arguments about why women still can't have it all and books like Sheryl Sandberg's Lean In, whose title has become a buzzword in its own right. Terms like unplug, offline, life-hack, bandwidth, and capacity are all about setting boundaries between the office and the home. But if your work is your "passion," you'll be more likely to devote yourself to it, even if that means going home for dinner and then working long after the kids are in bed.

But this seems to be the irony of office speak: Everyone makes fun of it, but managers love it, companies depend on it, and regular people willingly absorb it. As a linguist once said, "You can get people to think it's nonsense at the same time that you buy into it." In a workplace that's fundamentally indifferent to your life and its meaning, office speak can help you figure out how you relate to your work - and how your work defines who you are."""

p4_content = """Many people talked of the 288,000 new jobs the Labor Department reported for June, along with the drop in the unemployment rate to 6.1 percent, as good news. And they were right. For now it appears the economy is creating jobs at a decent pace. We still have a long way to go to get back to full employment, but at least we are now finally moving forward at a faster pace.

However, there is another important part of the jobs picture that was largely overlooked. There was a big jump in the number of people who report voluntarily working part-time. This figure is now 830,000 (4.4 percent) above its year ago level.

Before explaining the connection to the Obamacare, it is worth making an important distinction. Many people who work part-time jobs actually want full-time jobs. They take part-time work because this is all they can get. An increase in involuntary part-time work is evidence of weakness in the labor market and it means that many people will be having a very hard time making ends meet. There was an increase in involuntary part-time in June, but the general direction has been down. Involuntary part-time employment is still far higher than before the recession, but it is down by 640,000 (7.9 percent) from its year ago level.

We know the difference between voluntary and involuntary part-time employment because people tell us. The survey used by the Labor Department asks people if they worked less than 35 hours in the past week. The survey then asks whether they worked less than 35 hours in that week because they wanted to work less than full time or because they had no choice. They are only classified as voluntary part-time workers if they tell the survey taker they chose to work less than 35 hours a week.

The issue of voluntary part-time relates to Obamacare because one of the main purposes was to allow people to get insurance outside of employment. For many people, especially those with serious health conditions or family members with serious health conditions, before Obamacare the only way to get insurance was through a job that provided health insurance.

However, Obamacare has allowed more than 12 million people to either get insurance through Medicaid or the exchanges. These are people who may previously have felt the need to get a full-time job that provided insurance in order to cover themselves and their families. With Obamacare there is no longer a link between employment and insurance."""

p5_content = """Some Old Truths to Help You Overcome Tough Times

Unfortunately, life is not a bed of roses. We are going through life facing sad experiences. Moreover, we are grieving various kinds of loss: a friendship, a romantic relationship or a house. Hard times may hold you down at what usually seems like the most inopportune time, but you should remember that they won't last forever.

When our time of mourning is over, we press forward, stronger with a greater understanding and respect for life. Furthermore, these losses make us mature and eventually move us toward future opportunities for growth and happiness. I want to share these old truths I've learned along the way.

[41] ____________________
Fear is both useful and harmful. This normal human reaction is used to protect us by signaling danger and preparing us to deal with it. Unfortunately, people create inner barriers with a help of exaggerating fears. My favorite actor Will Smith once said, "Fear is not real. It is a product of thoughts you create. Do not misunderstand me. Danger is very real. But fear is a choice." I do completely agree that fears are just the product of our luxuriant imagination.

[42] ____________________
If you are surrounded by problems and cannot stop thinking about the past, try to focus on the present moment. Many of us are weighed down by the past or anxious about the future. You may feel guilt over your past, but you are poisoning the present with the things and circumstances you cannot change. Value the present moment and remember how fortunate you are to be alive. Enjoy the beauty of the world around and keep the eyes open to see the possibilities before you. Happiness is not a point of future and not a moment from the past, but a mindset that can be designed into the present.

[43] ____________________
Sometimes it is easy to feel bad because you are going through tough times. You can be easily caught up by life problems that you forget to pause and appreciate the things you have. Only strong people prefer to smile and value their life instead of crying and complaining about something.

[44] ____________________
No matter how isolated you might feel and how serious the situation is, you should always remember that you are not alone. Try to keep in mind that almost everyone respects and wants to help you if you are trying to make a good change in your life, especially your dearest and nearest people. You may have a circle of friends who provide constant good humor, help and companionship. If you have no friends or relatives, try to participate in several online communities, full of people who are always willing to share advice and encouragement.

[45] ____________________
Today many people find it difficult to trust their own opinion and seek balance by gaining objectivity from external sources. This way you devalue your opinion and show that you are incapable of managing your own life. When you are struggling to achieve something important you should believe in yourself and be sure that your decision is the best. You live in your skin, think your own thoughts, have your own values and make your own choices."""

passages[0]["content"] = p0_content
passages[1]["content"] = p1_content
passages[2]["content"] = p2_content
passages[3]["content"] = p3_content
passages[4]["content"] = p4_content
passages[5]["content"] = p5_content

for p in passages:
    if p.get("sequence_number") is None:
        p["sequence_number"] = p["sort_order"]

# 3. Gold Question Reconstructions
questions = data["questions"]

# Golden Data Specs
gold_specs = {
    1: {
        "stem": "Choose the best option for blank [1] in the passage:",
        "opts": [("A", "signal"), ("B", "permit"), ("C", "ticket"), ("D", "record")],
        "ans": "A",
        "expl": "［考点提炼］名词语义辨析与生活常识关联。\n［精准定位］空格位于第一段第二句状语中：they cling to their phones, even without a [1] on a subway。\n［命题解密］首句指出人们对与陌生人交流的恐惧；第二句列举地铁中乘客盯住手机不放的典型生活场景。即使在没有“手机信号”的情况下依然低头紧抱手机，最能体现对人际社交的回避。故 A 项 signal（信号）符合语境。\n［错项排除］B项 permit（许可证）、C项 ticket（车票）和 D项 record（记录）均无法与手机在地铁中的使用场景形成逻辑衔接。"
    },
    2: {
        "stem": "Choose the best option for blank [2] in the passage:",
        "opts": [("A", "nothing"), ("B", "little"), ("C", "another"), ("D", "much")],
        "ans": "D",
        "expl": "［考点提炼］不定代词语义辨析与因果逻辑。\n［精准定位］第二段第一句：there's [2] to be gained from talking to the stranger standing by you。\n［命题解密］该句阐述之所以“回避与他人互动是可悲的现实（sad reality）”，是因为与身边的陌生人攀谈其实可以带来“很多（much）”益处。前后构成因果逻辑，只有表示收获良多的 D 项 much 符合文意。\n［错项排除］A项 nothing（毫无收获）与 B项 little（几乎没有）与后文交谈获益的正面意义截然相悖；C项 another（另一个）缺乏指代对象。"
    },
    3: {
        "stem": "Choose the best option for blank [3] in the passage:",
        "opts": [("A", "beaten"), ("B", "plugged"), ("C", "guided"), ("D", "brought")],
        "ans": "B",
        "expl": "［考点提炼］动词短语固定搭配与上下文语义。\n［精准定位］第二段第二句：But you wouldn't know it, [3] into your phone。\n［命题解密］plug into 原指插上插头通电，引申为“全神贯注沉浸于、埋头于”。此处形容现代人耳朵插着耳机、全副身心扎进手机屏幕的生动写照。故 B 项 plugged 为唯一正确搭配。\n［错项排除］A项 beaten（被击打）、C项 guided（被引导）与 D项 brought（被带来）均无法与 into your phone 搭配构成“沉迷于手机”之意。"
    },
    4: {
        "stem": "Choose the best option for blank [4] in the passage:",
        "opts": [("A", "message"), ("B", "code"), ("C", "notice"), ("D", "sign")],
        "ans": "A",
        "expl": "［考点提炼］名词语义辨析与后置同位语引申。\n［精准定位］第二段第三句：This universal protection sends the [4] \"Please don't approach me.\"\n［命题解密］后文引号内的句子“请不要靠近我”是该保护机制向外界传递的明确“信号/信息（message）”。send the message 为常用表达，意为传递出某种讯息。故 A 项 message 正确。\n［错项排除］B项 code（密码/准则）、C项 notice（通知/告示）与 D项 sign（标志/手势）均不能准确表达这种由行为流露出的心理沟通信息。"
    },
    5: {
        "stem": "Choose the best option for blank [5] in the passage:",
        "opts": [("A", "under"), ("B", "beyond"), ("C", "behind"), ("D", "from")],
        "ans": "C",
        "expl": "［考点提炼］介词搭配与比喻隐喻。\n［精准定位］第三段第一句：What is it that makes us feel we need to hide [5] our screens?\n［命题解密］hide behind 为固定搭配，意为“躲藏在……背后”。人们把手机屏幕当作挡箭牌和护身符躲在后面以逃避现实人际交往，故 C 项 behind 正确。\n［错项排除］A项 under（在……下方）、B项 beyond（超出……之外）与 D项 from（来自）均不符合躲在屏幕后寻求心理庇护的隐喻逻辑。"
    },
    6: {
        "stem": "Choose the best option for blank [6] in the passage:",
        "opts": [("A", "misapplied"), ("B", "misinterpreted"), ("C", "misadjusted"), ("D", "mismatched")],
        "ans": "B",
        "expl": "［考点提炼］动词语义辨析与被动语态。\n［精准定位］第三段第三句：We fear rejection, or that our innocent social advances will be [6] as \"creep.\"\n［命题解密］作者分析社交恐惧的根源：担心我们善意的社交搭讪被对方“误解/曲解（misinterpreted）”为心怀不轨的怪人（creep）。故 B 项 misinterpreted 准确传达此意。\n［错项排除］A项 misapplied（被误用）、C项 misadjusted（失调）与 D项 mismatched（不匹配）皆与社交互动中意图被曲解的语境不符。"
    },
    7: {
        "stem": "Choose the best option for blank [7] in the passage:",
        "opts": [("A", "judged"), ("B", "fired"), ("C", "replaced"), ("D", "delayed")],
        "ans": "A",
        "expl": "［考点提炼］动词被动语义辨析与社交心理。\n［精准定位］第三段第四句：We fear we'll be [7]. We fear we'll be disruptive.\n［命题解密］本段连续以 We fear... 排比句式剖析心理阴影：人们害怕被拒绝、被评价被评头论足（judged）、害怕造成打扰。judged 意为“被评判/被指指点点”，切合社交焦虑的核心特征，故 A 项正确。\n［错项排除］B项 fired（被解雇）、C项 replaced（被取代）与 D项 delayed（被延误）均属于职场或行程词汇，脱离了大众陌生人交流的心理范畴。"
    },
    8: {
        "stem": "Choose the best option for blank [8] in the passage:",
        "opts": [("A", "unreasonable"), ("B", "ungrateful"), ("C", "unconventional"), ("D", "unfamiliar")],
        "ans": "D",
        "expl": "［考点提炼］形容词语义辨析与词汇复现。\n［精准定位］第三段第六句：Strangers are inherently [8] to us, so we are more likely to feel...\n［命题解密］strangers（陌生人）天然具有的特质就是“陌生的、不熟悉的（unfamiliar）”，这正是人们对其产生心理防备的生物学根源。故 D 项 unfamiliar 符合同根逻辑。\n［错项排除］A项 unreasonable（不合理的）、B项 ungrateful（忘恩负义的）与 C项 unconventional（非传统的）皆非陌生人的固有本质属性。"
    },
    9: {
        "stem": "Choose the best option for blank [9] in the passage:",
        "opts": [("A", "comfortable"), ("B", "confident"), ("C", "anxious"), ("D", "angry")],
        "ans": "C",
        "expl": "［考点提炼］形容词语义辨析与后文照应。\n［精准定位］第三段第六至七句：so we are more likely to feel [9]... To avoid this anxiety, we...\n［命题解密］第七句紧接着提到 To avoid this anxiety（为了消除这种焦虑），直接明示第六句空格处正是表示焦虑心理的形容词 anxious。故 C 项正确。\n［错项排除］A项 comfortable（舒适的）与 B项 confident（自信的）为正面情绪，与语境相反；D项 angry（愤怒的）不符合陌生人初次接触时的常态心理。"
    },
    10: {
        "stem": "Choose the best option for blank [10] in the passage:",
        "opts": [("A", "attend"), ("B", "turn"), ("C", "take"), ("D", "point")],
        "ans": "B",
        "expl": "［考点提炼］动词短语固定搭配与心理转移。\n［精准定位］第三段第七句：To avoid this anxiety, we [10] to our phones.\n［命题解密］turn to sb./sth. 意为“求助于、转向”。为了逃避与陌生人相处的焦虑，人们转而向手机寻求心理慰藉。故 B 项 turn 构成完美搭配。\n［错项排除］A项 attend to（照料/处理）、C项 take to（喜欢上/养成习惯）与 D项 point to（指向）均不表示逃避困难时寻求替代寄托。"
    },
    11: {
        "stem": "Choose the best option for blank [11] in the passage:",
        "opts": [("A", "dangerous"), ("B", "mysterious"), ("C", "violent"), ("D", "boring")],
        "ans": "A",
        "expl": "［考点提炼］形容词语义辨析与前文比喻照应。\n［精准定位］第三段末句：protect us from what we perceive is going to be more [11].\n［命题解密］前文将手机比喻为 security blanket（安全毯），安全毯的作用是保护我们免受潜在“危险/危害（dangerous）”的侵袭，对应社交恐惧中人们对外部不可控威胁的主观臆想。故 A 项 dangerous 正确。\n［错项排除］B项 mysterious（神秘的）、C项 violent（暴力的）与 D项 boring（无聊的）均偏离了安全防护的比喻重心。"
    },
    12: {
        "stem": "Choose the best option for blank [12] in the passage:",
        "opts": [("A", "bend"), ("B", "resist"), ("C", "hurt"), ("D", "decay")],
        "ans": "C",
        "expl": "［考点提炼］动词语义辨析与固定习语。\n［精准定位］第四段第一句：tuck our smartphones in our pockets and look up, it doesn't [12] so bad.\n［命题解密］作者用撕掉创可贴的比喻指出：一旦我们收起手机抬起头与陌生人眼神接触，其实“感觉并没有那么糟糕/没那么痛（doesn't hurt so bad）”。hurt 此处表示心理上的受挫或不适感。故 C 项 hurt 正确。\n［错项排除］A项 bend（弯曲）、B项 resist（抵抗）与 D项 decay（腐烂）均不能用于描绘人际交流带来的感受体验。"
    },
    13: {
        "stem": "Choose the best option for blank [13] in the passage:",
        "opts": [("A", "lecture"), ("B", "debate"), ("C", "conversation"), ("D", "negotiation")],
        "ans": "C",
        "expl": "［考点提炼］名词语义辨析与后文同义词复现。\n［精准定位］第四段第二至三句：Start a [13]. They had Chicago train commuters talk to their fellow...\n［命题解密］后文明确解释实验内容是让乘客与周围同行的人交谈（talk to），后文多次出现 talking to a stranger, communication。因此 start a conversation（开始交谈/攀谈）为标准表达，故 C 项正确。\n［错项排除］A项 lecture（讲座）、B项 debate（辩论）与 D项 negotiation（谈判）皆为正式严肃的特殊沟通形式，非通勤车厢中自发的日常攀谈。"
    },
    14: {
        "stem": "Choose the best option for blank [14] in the passage:",
        "opts": [("A", "trainees"), ("B", "employees"), ("C", "researchers"), ("D", "passengers")],
        "ans": "D",
        "expl": "［考点提炼］名词语义辨析与场景常识。\n［精准定位］第四段第三句：They had Chicago train commuters talk to their fellow [14].\n［命题解密］train commuters 指火车通勤乘客，与其同行的人显然是同车“乘客（passengers）”。fellow passengers 意为同行乘客，故 D 项正确。\n［错项排除］A项 trainees（实习生）、B项 employees（雇员）与 C项 researchers（研究员）与车厢公共交通环境不符。"
    },
    15: {
        "stem": "Choose the best option for blank [15] in the passage:",
        "opts": [("A", "reveal"), ("B", "choose"), ("C", "predict"), ("D", "design")],
        "ans": "C",
        "expl": "［考点提炼］动词语义辨析与实验对比逻辑。\n［精准定位］第四段第四句：asked other people in the same train station to [15] how they would feel after talking to a stranger...\n［命题解密］实验人员让未参与交谈的站台路人“预测/设想（predict）”如果和陌生人搭讪会是什么感觉。路人预测自己单独坐着会更舒适，而实际参与实验的人体验却很愉快。这种前后反差体现 predict 的科学对比设计。故 C 项 predict 正确。\n［错项排除］A项 reveal（揭示/透露）、B项 choose（选择）与 D项 design（设计）均非让受试者预判未来心理感受的准确词汇。"
    },
    16: {
        "stem": "Choose the best option for blank [16] in the passage:",
        "opts": [("A", "voyage"), ("B", "flight"), ("C", "walk"), ("D", "ride")],
        "ans": "D",
        "expl": "［考点提炼］名词语义辨析与交通场景。\n［精准定位］第四段第四句：the commuters thought their [16] would be more pleasant if they sat on their own...\n［命题解密］乘坐火车、汽车等交通工具的通勤路程通常称作 ride（车程/乘坐）。后文也提到 these commutes were reportedly more enjoyable。故 D 项 ride 准确贴切。\n［错项排除］A项 voyage（长途航海旅行）、B项 flight（飞机航班）与 C项 walk（步行）均与坐火车（train commuters）的场景相悖。"
    },
    17: {
        "stem": "Choose the best option for blank [17] in the passage:",
        "opts": [("A", "went through"), ("B", "did away"), ("C", "caught up"), ("D", "put up")],
        "ans": "A",
        "expl": "［考点提炼］动词短语搭配与语义理解。\n［精准定位］第四段第五句：after they [17] with the experiment, \"not a single person reported having been snubbed.\"\n［命题解密］go through with sth. 为固定习语，意为“把……做到底，贯彻/执行完成（某艰难或预设的计划）”。受试者顶住顾虑切实完成实验后，发现无人被冷落冷遇。故 A 项 went through 正确。\n［错项排除］B项 do away with（废除/消灭）、C项 catch up with（追赶上）与 D项 put up with（容忍/忍受）均无法表达执行完成实验之意。"
    },
    18: {
        "stem": "Choose the best option for blank [18] in the passage:",
        "opts": [("A", "In turn"), ("B", "In fact"), ("C", "In particular"), ("D", "In consequence")],
        "ans": "B",
        "expl": "［考点提炼］逻辑副词短语与语篇推进。\n［精准定位］第四段第六句：[18], these commutes were reportedly more enjoyable compared with those without communication...\n［命题解密］前一句指出受试者没有一人被冷落，本句进一步递进揭示惊喜的事实真相：事实上（In fact），比起一路沉默，这些进行了交流的通勤过程反而更加愉快。故 B 项 In fact 承前启后表达递进与事实陈述，最为精确。\n［错项排除］A项 In turn（轮流/反过来）、C项 In particular（特别/尤其）与 D项 In consequence（结果）在此处均缺乏严密的逻辑支撑。"
    },
    19: {
        "stem": "Choose the best option for blank [19] in the passage:",
        "opts": [("A", "unless"), ("B", "whereas"), ("C", "if"), ("D", "since")],
        "ans": "D",
        "expl": "［考点提炼］连词辨析与因果论证。\n［精准定位］第四段第六句：which makes absolute sense, [19] human beings thrive off of social connections.\n［命题解密］前半句表示交谈带来快乐是完全讲得通的（makes absolute sense），后半句给出理论依据：因为（since）人类本就是依靠社会连接而繁衍兴旺的。since 引导原因状语从句，逻辑严谨。故 D 项 since 正确。\n［错项排除］A项 unless（除非）、B项 whereas（然而/反之）与 C项 if（如果）均不能引导具有客观必然性的因果解释从句。"
    },
    20: {
        "stem": "Choose the best option for blank [20] in the passage:",
        "opts": [("A", "funny"), ("B", "simple"), ("C", "logical"), ("D", "rare")],
        "ans": "B",
        "expl": "［考点提炼］形容词语义辨析与主旨收束。\n［精准定位］第四段末句：It's that [20]: Talking to strangers can make you feel connected.\n［命题解密］It's that simple 为英语常见收束表达，意为“道理就这么简单：与陌生人交谈能让你产生人际连结感”。作者用极其精炼有力的短句总结全文，呼吁大家打破冷漠屏障。故 B 项 simple 准确。\n［错项排除］A项 funny（滑稽好笑的）、C项 logical（符合逻辑的）与 D项 rare（罕见的）均破坏了该总结性短语的地道凝练语感。"
    },
    21: {
        "stem": "According to Paragraph 1, most previous surveys found that home",
        "opts": [
            ("A", "offered greater relaxation than the workplace"),
            ("B", "was an ideal place for stress measurement"),
            ("C", "generated more stress than the workplace"),
            ("D", "was an unrealistic place for relaxation")
        ],
        "ans": "A",
        "expl": "［考点提炼］事实细节题与反向逻辑推理。\n［精准定位］第一段首句：A new study suggests that contrary to most surveys, people are actually more stressed at home than at work.\n［命题解密］新研究表明，与“大多数调查（most surveys）”相反，人们在家里实际上比在工作中压力更大。由此可推知：以往的大多数调查普遍认为“家庭比工作场所更能让人放松（offered greater relaxation than the workplace）”，新研究恰恰颠覆了这一传统调查共识。故 A 项正确。\n［错项排除］C项为新研究的发现，而非过去 surveys 的结论；B项与 D项在第一段并未提及，且 D 项误解了 what is supposed to be a place of refuge 的深层含义。"
    },
    22: {
        "stem": "According to Damaske, who are likely to be the happiest at home?",
        "opts": [
            ("A", "Working mothers."),
            ("B", "Childless husbands."),
            ("C", "Working fathers."),
            ("D", "Childless wives.")
        ],
        "ans": "B",
        "expl": "［考点提炼］事实细节题与信息多重交叉定位。\n［精准定位］第二段第三至四句：It is men, not women, who report being happier at home than at work. Another surprise is that the findings hold true for both those with children and without, but more so for nonparents.\n［命题解密］作者指出在家庭中感到比在工作中更快乐的是男性（men, not women）；且这一结论在没有孩子的人群中更为显著（more so for nonparents）。将男性（husbands）与无子女（childless）两者信息叠加，即为 Childless husbands。故 B 项正确。\n［错项排除］A项 Working mothers 和 D项 Childless wives 均为女性，与文中 men, not women 直接冲突；C项 Working fathers 未体现 nonparents 的核心限制。"
    },
    23: {
        "stem": "The blurring of working women's roles refers to the fact that",
        "opts": [
            ("A", "they are both breadwinners and housewives"),
            ("B", "their home is also a place for kicking back"),
            ("C", "there is often much housework left behind"),
            ("D", "it is difficult for them to leave their office")
        ],
        "ans": "A",
        "expl": "［考点提炼］细节理解题与同位语互释。\n［精准定位］第三段第二句：Working women still experience the blurring of their roles as breadwinners and housewives.\n［命题解密］句中 as breadwinners and housewives 直接作为同位语明确阐释了 roles 的具体内涵：职业女性面临的角色模糊，正是指她们既要承担养家糊口的赚钱责任（breadwinners），又要承担照料家庭的主妇责任（housewives）。故 A 项精准概括。\n［错项排除］B项（家是放松的地方）、C项（家务遗留）与 D项（难以离开办公室）均非文中 roles 的对应解释。"
    },
    24: {
        "stem": "The word \"moola\" (Line 4, Para. 4) most probably means",
        "opts": [
            ("A", "skills"),
            ("B", "energy"),
            ("C", "earnings"),
            ("D", "nutrition")
        ],
        "ans": "C",
        "expl": "［考点提炼］词义猜测题与句内平行对照。\n［精准定位］第四段第二至三句：...doing the tasks they have to do in order to draw an income. The bargain is very pure: Employee puts in hours of physical or mental labor and employee draws out life-sustaining moola.\n［命题解密］第四段描述职场契约的清晰性：投入劳动换取收入（draw an income）。下句结构完全对仗：puts in labor（付出劳动）与 draws out life-sustaining moola（获取维持生计的薪酬）。由此可知 moola 即代指 income（收入、金钱、earnings）。故 C 项 earnings 正确。\n［错项排除］A项 skills（技能）、B项 energy（精力）与 D项 nutrition（营养）均无法与 draws out... 和 income 构成语义对应。"
    },
    25: {
        "stem": "The home front differs from the workplace in that",
        "opts": [
            ("A", "family labor is often adequately rewarded"),
            ("B", "home is hardly a cozier working environment"),
            ("C", "household tasks are generally more motivating"),
            ("D", "division of labor at home is seldom clear-cut")
        ],
        "ans": "D",
        "expl": "［考点提炼］对比细节题与同义转换。\n［精准定位］第五段第一至二句：On the home front, however, people have no such clarity. Rare is the household in which the division of labor is so clinically and methodically laid out.\n［命题解密］第四段先阐明职场分工清晰纯粹，第五段转折（however）对比家庭生活：在家庭大后方，分工如此条理分明的情况实属罕见（Rare is the household in which the division of labor is so clinically and methodically laid out）。Rare（罕见）与 D 项 seldom clear-cut（很少界线分明）完美对应。故 D 项正确。\n［错项排除］A项与文中 there are inadequate rewards for most of them 截然相悖；B项为无端主观臆断；C项与后文 co-workers are much harder to motivate 相矛盾。"
    },
    26: {
        "stem": "Recruiting more first-generation students has",
        "opts": [
            ("A", "reduced their dropout rates"),
            ("B", "narrowed the achievement gap"),
            ("C", "missed its original purpose"),
            ("D", "depressed college students")
        ],
        "ans": "C",
        "expl": "［考点提炼］细节推理题与悖论反差解析。\n［精准定位］第一段第三至四句：...colleges and universities have pushed for decades to recruit more of them. This has created \"a paradox\" in that recruiting first-generation students, but then watching many of them fail, means that higher education has \"continued to reproduce and widen, rather than close\" an achievement gap...\n［命题解密］高校大力招收第一代大学生的初衷原本是促进社会公平，但由于缺乏后续支持，眼睁睁看着他们学业失败，反而扩大而非缩小了阶层成就差距。这种悖论表明扩招政策“未能实现其最初的目的（missed its original purpose）”。故 C 项正确。\n［错项排除］A项与文中 Their grades are lower and their dropout rates are higher 相反；B项与 widen, rather than close 完全相反；D项 depressed 转移了论文作者的态度（a depressing beginning）。"
    },
    27: {
        "stem": "The authors of the research article are optimistic because",
        "opts": [
            ("A", "their findings appeal to students"),
            ("B", "the recruiting rate has increased"),
            ("C", "the problem is solvable"),
            ("D", "their approach is costless")
        ],
        "ans": "C",
        "expl": "［考点提炼］因果细节题与段落主旨归纳。\n［精准定位］第二段：But the article is actually quite optimistic, as it outlines a potential solution to this problem, suggesting that an approach... can close 63 percent of the achievement gap...\n［命题解密］第二段明确指出作者感到乐观的原因在于：文章提出了解决该问题的一种潜在方案（outlines a potential solution to this problem），且该干预手段能缩小 63% 的成就差距。由此可知，作者乐观是因为“该难题是可以解决的（the problem is solvable）”。故 C 项正确。\n［错项排除］A项（研究吸引学生）无中生有；B项（录取率提高）非乐观原因；D项将文中 next-to-no-cost（几乎零成本）绝对化为 costless（完全无成本），属于张冠李戴干扰项。"
    },
    28: {
        "stem": "The study suggests that most first-generation students",
        "opts": [
            ("A", "are from single-parent families"),
            ("B", "study at private universities"),
            ("C", "are in need of financial support"),
            ("D", "have failed their college")
        ],
        "ans": "C",
        "expl": "［考点提炼］事实细节题与背景知识推导。\n［精准定位］第三段第三句：Most of the first-generation students (59.1 percent) were recipients of Pell Grants, a federal grant for undergraduates with financial need...\n［命题解密］文中数据显示，59.1%（绝大多数）的第一代大学生都是联邦佩尔助学金的资助对象，而该助学金专门设立给有经济困难的本科生（for undergraduates with financial need）。因此，绝大多数第一代大学生“需要经济资助（are in need of financial support）”。故 C 项正确。\n［错项排除］A项由 not having a parent with a four-year college degree 偷换概念为单亲家庭；B项把样本来源某一私立大学夸大为该群体普遍就读私立大学；D项混淆了部分退学与全体失败。"
    },
    29: {
        "stem": "The authors of the paper believe that first-generation students",
        "opts": [
            ("A", "may lack opportunities to apply for research projects"),
            ("B", "are inexperienced in handling their issues at college"),
            ("C", "can have a potential influence on other students"),
            ("D", "are actually indifferent to the achievement gap")
        ],
        "ans": "B",
        "expl": "［考点提炼］观点态度细节题与同义转述。\n［精准定位］第四段第一句：Their thesis... was based on the view that first-generation students may be most lacking not in potential but in practical knowledge about how to deal with the issues that face most college students.\n［命题解密］研究人员认为，第一代大学生最缺乏的不是学术潜力，而是应对高校学生常见问题的实用知识（lacking in practical knowledge about how to deal with the issues）。lacking practical knowledge 恰恰等同于 B 项 are inexperienced in handling their issues at college。故 B 项正确。\n［错项排除］A项中的 research projects 属于断章取义拼接；C项窜改了 potential 的词性和含义；D项（对差距漠不关心）违背常理和文意。"
    },
    30: {
        "stem": "We may infer from the last paragraph that",
        "opts": [
            ("A", "universities often reject the culture of the middle-class"),
            ("B", "students are usually to blame for their lack of resources"),
            ("C", "social class greatly helps enrich educational experiences"),
            ("D", "colleges are partly responsible for the problem in question")
        ],
        "ans": "D",
        "expl": "［考点提炼］推理引申题与因果归因。\n［精准定位］第五段第二至三句：And this becomes more of a problem when colleges don't talk about the class advantages and disadvantages... \"Because US colleges and universities seldom acknowledge how social class can affect students' educational experiences...\"\n［命题解密］最后一段指出，高校对不同群体的阶层优劣势避而不谈，很少承认社会阶层对教育体验的影响，导致第一代学生无法认清自身困境根源。这说明高校对于第一代大学生的学业适应困境“负有部分责任（colleges are partly responsible for the problem in question）”。故 D 项正确。\n［错项排除］A项与第一段高校本身充斥中产阶级文化相悖；B项将责任推给学生，与作者批评高校漠视立场相反；C项正反颠倒，社会阶层差距带来的是困境而非丰富体验。"
    },
    31: {
        "stem": "According to Nancy Koehn, office language has become",
        "opts": [
            ("A", "less strategic"),
            ("B", "less energetic"),
            ("C", "more objective"),
            ("D", "more emotional")
        ],
        "ans": "D",
        "expl": "［考点提炼］细节事实题与直接定位。\n［精准定位］第一段第一句：Even in traditional offices, the lingua franca of corporate America has gotten much more emotional and much more right-brained than it was 20 years ago, says Harvard Business School historian Nancy Koehn.\n［命题解密］哈佛商学院历史学家南希·克恩明确指出，如今美国企业的办公通用语变得更加情感化（has gotten much more emotional）。故 D 项 more emotional 完全忠实于原文直接信息，正确答案为 D。\n［错项排除］A项 less strategic、B项 less energetic 和 C项 more objective 均取自下文所列举的昔日词汇与新词对比（There were goals, strategies... but we didn't talk about energy...），并非办公室语言整体演变趋势的准确概括。"
    },
    32: {
        "stem": "\"Team\"-oriented corporate vocabulary is closely related to",
        "opts": [
            ("A", "sports culture"),
            ("B", "gender difference"),
            ("C", "historical incidents"),
            ("D", "athletic executives")
        ],
        "ans": "A",
        "expl": "［考点提炼］细节理解题与原因深层剖析。\n［精准定位］第二段第一至二句：Koehn pointed out that this new era of corporate vocabulary is very \"team\"-oriented - and that is not by coincidence. \"Let's not forget sports - in male-dominated corporate America, it's still a big deal...\"\n［命题解密］克恩指出新时代企业词汇偏向“团队”绝非巧合，根源在于美国企业界深受男性喜爱的“体育文化（sports culture）”影响，CEO把自己视作教练（coach），把员工视作球队（team）。故 A 项 sports culture 正确。\n［错项排除］B项（性别差异）虽提到 male-dominated，但它只是体育文化在企业盛行的社会背景，而非词汇直接渊源；C项（历史事件）和 D项（健美型高管）纯属无中生有误导。"
    },
    33: {
        "stem": "Khurana believes that the importation of terminology aims to",
        "opts": [
            ("A", "revive historical terms"),
            ("B", "promote company image"),
            ("C", "foster corporate cooperation"),
            ("D", "strengthen employee loyalty")
        ],
        "ans": "D",
        "expl": "［考点提炼］人物观点题与词汇同义替换。\n［精准定位］第三段第一句：These terms are also intended to infuse work with meaning - and, as Rakesh Khurana, another professor, points out, increase allegiance to the firm.\n［命题解密］库拉纳教授指出，企业从非营利组织和宗教组织引入这些新词汇，目的在于赋予工作意义，并“提高对公司的忠诚度（increase allegiance to the firm）”。allegiance 即 loyalty，故 D 项 strengthen employee loyalty 准确同义改写。\n［错项排除］A项（复兴历史术语）曲解了 historically used to be associated with 的出处说明；B项（宣传公司形象）和 C项（促进企业合作）脱离了句中 allegiance to the firm 的核心指向。"
    },
    34: {
        "stem": "It can be inferred that Lean In",
        "opts": [
            ("A", "voices for working women"),
            ("B", "appeals to passionate workaholics"),
            ("C", "triggers debates among mommies"),
            ("D", "praises motivated employees")
        ],
        "ans": "A",
        "expl": "［考点提炼］推理引申题与语境例证功能。\n［精准定位］第四段第二句：The \"mommy wars\" of the 1990s are still going on today, prompting arguments about why women still can't have it all and books like Sheryl Sandberg's Lean In...\n［命题解密］文中在讨论关于“女性为何依然不能兼顾事业与家庭”的争论中，列举了谢丽尔·桑德伯格的畅销书《向前一步》（Lean In），该书呼吁女性勇于争取职场领导权、平衡家庭与事业。由此可推知其核心功能是“为职场女性发声（voices for working women）”。故 A 项正确。\n［错项排除］B项（吸引工作狂）和 D项（赞美有动力的员工）偏离了该书关照女性角色的主旨；C项倒置因果，该书是 mommy wars 持续发酵催生的产物，而非争论的源头。"
    },
    35: {
        "stem": "Which of the following statements is true about office speak?",
        "opts": [
            ("A", "Linguists believe it to be nonsense."),
            ("B", "Regular people mock it but accept it."),
            ("C", "Companies find it to be fundamental."),
            ("D", "Managers admire it but avoid it.")
        ],
        "ans": "B",
        "expl": "［考点提炼］事实细节综合判断题与句意匹配。\n［精准定位］第五段第一句：Everyone makes fun of it, but managers love it, companies depend on it, and regular people willingly absorb it.\n［命题解密］作者总结指出职场行话的讽刺之处：每个人都在取笑调侃它（makes fun of it / mock it），但普通员工却又自愿接受吸收它（regular people willingly absorb it / accept it）。B 项正是对此句前后转折反差的精准归纳。\n［错项排除］A项断章取义，文中是借语言学家之言说明人前认为荒谬人后全盘接受的双重心理；C项把 indifferent to life 杂糅为行话是 fundamental 的；D项 managers love it 与 avoid 相悖。"
    },
    36: {
        "stem": "Which part of the jobs picture was neglected?",
        "opts": [
            ("A", "The prospect of a thriving job market."),
            ("B", "The increase of voluntary part-time jobs."),
            ("C", "The possibility of full employment."),
            ("D", "The acceleration of job creation.")
        ],
        "ans": "B",
        "expl": "［考点提炼］事实细节题与同义词复现定位。\n［精准定位］第二段：However, there is another important part of the jobs picture that was largely overlooked. There was a big jump in the number of people who report voluntarily working part-time.\n［命题解密］第二段首句中的 overlooked（被忽视）完全对应题干中的 neglected。紧接着指出被忽视的内容是：自愿兼职人数的大幅激增（a big jump in the number of people who report voluntarily working part-time）。故 B 项 The increase of voluntary part-time jobs 正确。\n［错项排除］A项（就业市场繁荣前景）、C项（充分就业可能性）与 D项（创造就业加速）均为第一段中已经广为人知、大肆讨论的好消息，非被忽视的部分。"
    },
    37: {
        "stem": "Many people work part-time because they",
        "opts": [
            ("A", "prefer part-time jobs to full-time jobs"),
            ("B", "feel that is enough to make ends meet"),
            ("C", "cannot get their hands on full-time jobs"),
            ("D", "want more leisure time for family")
        ],
        "ans": "C",
        "expl": "［考点提炼］因果事实细节题与口语习语转换。\n［精准定位］第三段第一至三句：Many people who work part-time jobs actually want full-time jobs. They take part-time work because this is all they can get.\n［命题解密］第三段指出，许多从事兼职的人实际上渴望全职工作，他们之所以做兼职是因为“这是他们唯一能找到的工作（this is all they can get）”。C 项 cannot get their hands on full-time jobs（无法染指/找不到全职工作）是对原文的完美同义转换。故 C 项正确。\n［错项排除］A项与 actually want full-time jobs 相反；B项与后文 having a very hard time making ends meet（维持生计极其艰难）相反；D项（想要更多家庭闲暇）属于自愿兼职者特征，非非自愿兼职原因。"
    },
    38: {
        "stem": "Involuntary part-time employment in the US",
        "opts": [
            ("A", "shows a general tendency of decline"),
            ("B", "is harder to acquire than one year ago"),
            ("C", "satisfies the real need of the jobless"),
            ("D", "has stabilized at a historical low")
        ],
        "ans": "A",
        "expl": "［考点提炼］事实细节题与趋势特征归纳。\n［精准定位］第三段第五句：There was an increase in involuntary part-time in June, but the general direction has been down.\n［命题解密］作者明确指出，尽管6月份非自愿兼职人数有所微升，但“总体发展方向一直是下降的（the general direction has been down）”。A 项 shows a general tendency of decline 正是对 the general direction has been down 的规范同义概括。故 A 项正确。\n［错项排除］B项断章取义，人数下降是由于经济好转找到全职，非兼职更难获得；C项与被迫兼职者的实际困境冲突；D项与 still far higher than before the recession 相悖。"
    },
    39: {
        "stem": "It can be learned that with Obamacare,",
        "opts": [
            ("A", "it is no longer easy for part-timers to get insurance"),
            ("B", "full-time employment is still essential for insurance"),
            ("C", "companies are forced to hire more part-time workers"),
            ("D", "employment is no longer a precondition to get insurance")
        ],
        "ans": "D",
        "expl": "［考点提炼］细节推理题与因果核心破题。\n［精准定位］第六段末句及第五段首句：The issue of voluntary part-time relates to Obamacare because one of the main purposes was to allow people to get insurance outside of employment... With Obamacare there is no longer a link between employment and insurance.\n［命题解密］文中强调奥巴马医改的核心目的和重大变革在于“打破了就业与医疗保险之间的必然联系（no longer a link between employment and insurance）”，使人们无需就业也能通过医疗补助或交易平台获得保险。即“就业不再是获得医保的先决条件（employment is no longer a precondition to get insurance）”。故 D 项正确。\n［错项排除］A项（兼职者更难获得医保）与事实相反；B项（全职工作仍必不可少）与医改破除绑定的事实直接抵触；C项在原文中并未提及强制雇佣兼职。"
    },
    40: {
        "stem": "The text mainly discusses",
        "opts": [
            ("A", "employment in the US"),
            ("B", "part-timer classification"),
            ("C", "the impact of Obamacare on jobs"),
            ("D", "the rise of gig economy")
        ],
        "ans": "A",
        "expl": "［考点提炼］主旨大意题与全文宏观统领。\n［精准定位］全文脉络与各段首句宏观归纳。\n［命题解密］文章开篇从美国劳工部6月新增就业与失业率下降切入，接着分析被忽视的自愿兼职增长，继而辨析自愿与非自愿兼职的经济内涵，最后探讨奥巴马医改对就业与医保脱钩的深远影响。全文始终紧扣“美国就业状况（employment in the US）”这一核心大主题展开。故 A 项宏观准确。\n［错项排除］B项（兼职分类）仅为第四段局部的技术定义说明；C项（奥巴马医改对就业影响）是以偏概全的局部论据；D项（零工经济崛起）脱离了正文讨论的传统就业市场调研框架。"
    },
    41: {
        "stem": "Choose the most suitable subheading from A-G for section [41]:",
        "opts": [
            ("A", "You are not alone"),
            ("B", "Experience helps you grow"),
            ("C", "Pave your own unique path"),
            ("D", "Most of your fears are unreal"),
            ("E", "Think about the present moment"),
            ("F", "Don't fear responsibility for your life"),
            ("G", "There are many things to be grateful for")
        ],
        "ans": "D",
        "expl": "［考点提炼］新题型小标题匹配题。\n［精准定位］Section [41] 原文首末句：Fear is both useful and harmful... My favorite actor Will Smith once said, \"Fear is not real... Danger is very real. But fear is a choice.\" I do completely agree that fears are just the product of our luxuriant imagination.\n［命题解密］该段开篇讨论恐惧（Fear），随后借威尔·史密斯名言指出“恐惧并非真实存在，而是思想的产物（Fear is not real）”，结尾强调恐惧只是丰富想象力的虚构产物。核心论点即“大部分恐惧都是不真实的”，与 D 项 Most of your fears are unreal 完美契合。故选 D。"
    },
    42: {
        "stem": "Choose the most suitable subheading from A-G for section [42]:",
        "opts": [
            ("A", "You are not alone"),
            ("B", "Experience helps you grow"),
            ("C", "Pave your own unique path"),
            ("D", "Most of your fears are unreal"),
            ("E", "Think about the present moment"),
            ("F", "Don't fear responsibility for your life"),
            ("G", "There are many things to be grateful for")
        ],
        "ans": "E",
        "expl": "［考点提炼］新题型小标题匹配题。\n［精准定位］Section [42] 原文首末句：If you are surrounded by problems and cannot stop thinking about the past, try to focus on the present moment... Value the present moment and remember how fortunate you are to be alive... a mindset that can be designed into the present.\n［命题解密］该段反复强调 focus on the present moment, Value the present moment, designed into the present。劝告读者不要被过去或未来所累，而应着眼当下、活在当下。与 E 项 Think about the present moment 原词高度呼应。故选 E。"
    },
    43: {
        "stem": "Choose the most suitable subheading from A-G for section [43]:",
        "opts": [
            ("A", "You are not alone"),
            ("B", "Experience helps you grow"),
            ("C", "Pave your own unique path"),
            ("D", "Most of your fears are unreal"),
            ("E", "Think about the present moment"),
            ("F", "Don't fear responsibility for your life"),
            ("G", "There are many things to be grateful for")
        ],
        "ans": "G",
        "expl": "［考点提炼］新题型小标题匹配题。\n［精准定位］Section [43] 原文：You can be easily caught up by life problems that you forget to pause and appreciate the things you have. Only strong people prefer to smile and value their life instead of crying and complaining...\n［命题解密］该段呼吁身处逆境时不要只顾哭泣抱怨，要停下来懂得欣赏珍惜自己已拥有的东西（appreciate the things you have / value their life）。appreciate the things you have 正是心怀感恩（grateful）的核心要义，对应 G 项 There are many things to be grateful for。故选 G。"
    },
    44: {
        "stem": "Choose the most suitable subheading from A-G for section [44]:",
        "opts": [
            ("A", "You are not alone"),
            ("B", "Experience helps you grow"),
            ("C", "Pave your own unique path"),
            ("D", "Most of your fears are unreal"),
            ("E", "Think about the present moment"),
            ("F", "Don't fear responsibility for your life"),
            ("G", "There are many things to be grateful for")
        ],
        "ans": "A",
        "expl": "［考点提炼］新题型小标题匹配题。\n［精准定位］Section [44] 原文首句：No matter how isolated you might feel and how serious the situation is, you should always remember that you are not alone.\n［命题解密］段落首句直截了当给出核心观点：无论感到多么孤立无援，都必须时刻记住你绝非孤身一人（remember that you are not alone）。后文围绕朋友、亲人以及网络社区的支持展开论述。A 项 You are not alone 为原文原词，完全吻合。故选 A。"
    },
    45: {
        "stem": "Choose the most suitable subheading from A-G for section [45]:",
        "opts": [
            ("A", "You are not alone"),
            ("B", "Experience helps you grow"),
            ("C", "Pave your own unique path"),
            ("D", "Most of your fears are unreal"),
            ("E", "Think about the present moment"),
            ("F", "Don't fear responsibility for your life"),
            ("G", "There are many things to be grateful for")
        ],
        "ans": "C",
        "expl": "［考点提炼］新题型小标题匹配题。\n［精准定位］Section [45] 原文末句：When you are struggling to achieve something important you should believe in yourself and be sure that your decision is the best. You live in your skin, think your own thoughts, have your own values and make your own choices.\n［命题解密］该段批判盲目依赖外部意见、贬低自我见解的做法，极力倡导要相信自己，过自己的生活，有自己的思想和价值观，做出自己的抉择。排比句 live in your skin, think your own thoughts, make your own choices 深刻阐明要走属于自己的独特之路，与 C 项 Pave your own unique path（铺就属于自己的独特道路）意旨完全相同。故选 C。"
    }
}

# Update all 45 questions
for i, q in enumerate(questions, 1):
    spec = gold_specs[i]
    q["question_number"] = i
    q["sort_order"] = i
    pts = 0.5 if i <= 20 else 2.0
    q["points"] = pts
    q["score"] = pts
    q_t = "cloze_item" if i <= 20 else "reading_item"
    q["q_type"] = q_t
    q["question_type"] = q_t
    q["stem"] = spec["stem"]
    q["correct_answer"] = spec["ans"]
    q["answer"] = spec["ans"]
    q["explanation"] = spec["expl"]
    q["options"] = [{"key": k, "text": v, "value": k} for k, v in spec["opts"]]

# Save file
with open(EXAM_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("SUCCESS: 2015 ky2 Gold Engine successfully executed and written to JSON!")
