# -*- coding: utf-8 -*-
"""
Round 15 Calibration Script:
1. Restore authentic 2005 ky1 Q25 stem, options, correct_answer ('B'), and complete explanation.
2. Truncate and clean 2004 ky1 Q20 explanation.
3. Truncate and clean 2004 ky1 Q40 explanation.
4. Truncate 2007 ky1 Q45 explanation to remove leaked translation and watermark.
5. Clean 2008 ky1 Q43 explanation to remove watermark.
6. Truncate 2008 ky1 Q45 explanation to remove leaked translation.
7. Upgrade 2009 ky1 Q41 explanation to complete yellow book 3-step analysis and remove watermark.
8. Truncate 2012 ky1 Q25 explanation to remove leaked long sentences, vocabulary, translation, and watermarks.
9. Upgrade 2012 ky1 Q41-Q45 explanations to complete authoritative yellow book 3-step analysis.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2005 ky1 Q25
f_2005 = 'public/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json'
d_2005 = json.load(open(f_2005, encoding='utf-8'))
for q in d_2005['questions']:
    if q['sort_order'] == 25:
        q['stem'] = "What can we infer from the last paragraph?"
        q['options'] = [
            {"key": "A", "text": "Monkeys can be trained to develop social emotions.", "value": "A"},
            {"key": "B", "text": "Human indignation evolved from an uncertain source.", "value": "B"},
            {"key": "C", "text": "Animals usually show their feelings openly as humans do.", "value": "C"},
            {"key": "D", "text": "Cooperation among monkeys remains stable only in the wild.", "value": "D"}
        ]
        q['correct_answer'] = "B"
        q['explanation'] = (
            "25. 【考点】推理引申题\n"
            "【精准定位】末段第四、五句指出：义愤感并非人类专利，猴子同样具有这一情感；末句则指出但这种公平感是从卷尾猴和人类身上各自演化而来，还是来源他们共同的祖先，至今仍是有待回答的问题。可见人类义愤感的来源尚不得而知，[B] 推理正确。\n"
            "【命题解密】正确项 [B] 是对末段第四至六句内容的正确推导，其中 human indignation 对应四句 Feelings of righteous indignation 以及第六句 such a sense of fairness；uncertain source 则对应 whether... evolved independently... or whether it stems from the common ancestor... is... an unanswered question 所蕴含的“来源尚未确定”之意。\n"
            "[A] 干扰源自末段首句，但该句只是指出“猴子受到社会情感支配”，并未提及这种社会情感是“被培养得来的（be trained）”。且文章一开始就已指出猴子和人类一样有情感表达，这是猴子的“天性”，故错误。\n"
            "[C] 将文章讨论范围从“猴子”扩大到“动物”。注：第二句虽然出现了 each animal，但根据上下文可知它此处专指“猴子”。\n"
            "[D] 将末段第三句所述猴子合作稳定的基础由“每只猴子都感到自己未被欺骗”改为“处于野外环境”。\n"
            "【技巧总结】本题考查对末段信息的推理引申，是考生常感困惑的题型。其实，正确项与干扰项的区别不在于“推理的程度”，而在于“推理的正误”。解决办法是将“定位法”与“排除法”相结合：一方面严格依照原文，挖掘深层次内容，找到推理正确的选项；另一方面探查选项中存在的致命错误（扩大讨论范围，偷换讨论对象，改变或强加逻辑关系等），排除推理错误的选项。\n"
            "如本题，一方面联系第四至六句信息“人猴均有义愤感”及“二者究竟是各自进化还是来自共同祖先尚待回答”基本确定 [B] 推理正确，另一方面可发现 [A]、[C]、[D] 均存在致命错误：文中指出猴子的公平感是猴子天性，可被训练的是“以币换物行为”而非“社会情感”，[A] 中 can be trained 完全错误；文中讨论的只是“猴子的公平感”，并非是宽泛许多的“动物的情感”，[C] 中 animals... feelings 明显夸大文章讨论范围；文中指出猴子合作稳定的基础是“每只猴子都感到自己未被欺骗”而非“处于野外环境（only in the wild）”，[D] 偷换原有逻辑关系。"
        )
        print("Calibrated 2005 ky1 Q25")

json.dump(d_2005, open(f_2005, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 2. 2004 ky1 Q20 & Q40
f_2004 = 'public/data/exams/47036de0-e57d-5ccb-9bc8-b3f86d4e6457.json'
d_2004 = json.load(open(f_2004, encoding='utf-8'))
for q in d_2004['questions']:
    if q['sort_order'] == 20:
        q['explanation'] = (
            "20. [A] provided 倘若（表条件）\n"
            "[B] since 因为，既然（表因果或让步）\n"
            "[C] although 虽然，尽管（表转折或让步）\n"
            "[D] supposing 如果，假使（表条件）\n"
            "【考点提炼】逻辑关系。正确率：52%\n"
            "【精准定位】末句中空格前后是两个完整的分句，因此空格处填入的词应体现它们之间的逻辑关系。前一句提到，以上所有这些情形，即本句提到的其他可识别的原因，都提高了青少年犯罪的可能性；后一句提到，直接的因果关系还没有确定。“已识别的（identifiable）原因”和“还不确定（not yet been established）的因果关系”之间显然存在转折关系。表转折的连词只有 [C] although。\n"
            "【空格设置】文中考查了句内逻辑以及 although 的用法。例句：I felt he was wrong, although I didn't say so at the time. 我觉得他错了，不过我当时没有说出来。\n"
            "【干扰项设置】其他项都是表示逻辑关系的连词，其中 supposing 与 provided 是分词形式的连词。例句：The factory will pay the bonus provided the job is completed on time. 如果工作及时完成的话，工厂将会发放奖金。Since you are not interested, I won't tell you about it. 既然你不感兴趣，那我就不告诉你了。Supposing it rains, what will you do? 假如下雨，你会怎么办呢？"
        )
        print("Calibrated 2004 ky1 Q20")
    elif q['sort_order'] == 40:
        q['explanation'] = (
            "40. What does the author think of intellect?\n"
            "40. 作者如何看待才智？\n"
            "[A] It is second to intelligence.\n"
            "[A] 它与智力相比是次要的。\n"
            "[B] It evolves from common sense.\n"
            "[B] 它是由常识演变而来的。\n"
            "[C] It is to be pursued.\n"
            "[C] 它应该被追求。\n"
            "[D] It underlies power.\n"
            "[D] 它是权力的基础。\n"
            "【精准定位】文章一开始，作者先提出现象：才智在美国教育中被忽视，进而讨论这种趋势的影响和原因，并借用他人的观点来表明自己的态度。作者引用厄尔·绍利斯、霍夫斯坦特和拉维奇的话语，以及第三段首句“学校原本可以并且也应该（逆转美国人对才智追求的厌恶）”都表明了作者对才智的肯定。综合全文可知，作者从头至尾一直在批判学校和社会忽视或轻视才智的做法，即赞成对才智的追求。因此 [C] 正确。\n"
            "【命题解密】本题考查考生正确把握作者观点的能力。作者从多种角度论证了才智的重要性，正确项 [C] 符合该观点。\n"
            "[A] 用作者批判的观点（第四段末句）做干扰；[B] 和 [D] 利用文中词语（第四段末句中 common sense 和首句中 power）设置干扰，捏造它们与才智之间的关系（evolves from 和 underlies）。"
        )
        print("Calibrated 2004 ky1 Q40")

json.dump(d_2004, open(f_2004, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 3. 2007 ky1 Q45
f_2007 = 'public/data/exams/e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json'
d_2007 = json.load(open(f_2007, encoding='utf-8'))
for q in d_2007['questions']:
    if q['sort_order'] == 45:
        # truncate before '二、全文翻译'
        expl = q['explanation']
        if '二、全文翻译' in expl:
            idx = expl.find('二、全文翻译')
            q['explanation'] = expl[:idx].strip()
            print("Calibrated 2007 ky1 Q45")

json.dump(d_2007, open(f_2007, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 4. 2008 ky1 Q43 & Q45
f_2008 = 'public/data/exams/d80926ab-1841-5d1f-a999-56773986c46d.json'
d_2008 = json.load(open(f_2008, encoding='utf-8'))
for q in d_2008['questions']:
    if q['sort_order'] == 43:
        expl = q['explanation']
        if '掌柜' in expl:
            q['explanation'] = expl.replace('掌柜', '').strip()
            print("Calibrated 2008 ky1 Q43")
    elif q['sort_order'] == 45:
        expl = q['explanation']
        if '二、全文翻译' in expl:
            idx = expl.find('二、全文翻译')
            q['explanation'] = expl[:idx].strip()
            print("Calibrated 2008 ky1 Q45")

json.dump(d_2008, open(f_2008, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 5. 2009 ky1 Q41
f_2009 = 'public/data/exams/9369aa41-c91e-548c-bf99-1ad46a07ac25.json'
d_2009 = json.load(open(f_2009, encoding='utf-8'))
for q in d_2009['questions']:
    if q['sort_order'] == 41:
        q['explanation'] = (
            "41. 本题考核的知识点是：内容一致性。\n"
            "【空格推测】上文介绍 Spencer 的生物和文化进化论，该理论强调“人类社会也在进化”，空格可能对此具体阐述。\n"
            "【答案敲定】由选项分析可知，[C] 为本题备选项。\n"
            "[C] 指出“他”将“适者生存”的进化理念推及人类的种族和社会，与第一段 Spencer 的观点“人类社会也在进化”相契合，人称代词 He 可回指 Spencer；同时，选项主要观点“弱小种族和社会最终被更强大、更先进种族和社会所替代”本身存在问题（涉及人种、种族歧视），作者并非完全赞同，观点引出词 argue 复现，表明作者对斯宾塞观点的态度前后一致，选项中 human / races and societies 是原文 human societies 的近义表达，weaker... be replaced by stronger, more advanced... 同义转述原文 advancing toward perfection，因此 [C] 与上文内容一致，是对上文观点的具体解释，敲定为答案。"
        )
        print("Calibrated 2009 ky1 Q41")

json.dump(d_2009, open(f_2009, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 6. 2012 ky1 Q25 & Q41-Q45
f_2012 = 'public/data/exams/baa66182-74ec-5a78-b2d2-077ffdcad9dc.json'
d_2012 = json.load(open(f_2012, encoding='utf-8'))
for q in d_2012['questions']:
    so = q['sort_order']
    if so == 25:
        expl = q['explanation']
        if '三、长难句分析' in expl:
            idx = expl.find('三、长难句分析')
            q['explanation'] = expl[:idx].strip()
            print("Calibrated 2012 ky1 Q25")
    elif so == 41:
        q['explanation'] = (
            "41. 本题考核的知识点是：代词指代 + 上下文衔接。正确率：50%\n"
            "【空格推测】空格上句围绕 fabulous machine“神奇机器（电脑）”展开，空格下句则转至论述 The networked computer“联网电脑”，故空格应涉及“将电脑联网”的内容才能起到承上启下的作用。\n"
            "【答案敲定】由选项分析可知，[C] 为本题备选项。\n"
            "[C] 项主干为 Not only... but... also... 结构，but 表转折递进，将语义分为两大块：第一块内容“他们发明了这样一台机器”概括空格上句“一批天才、勇士等合力发明了一台神奇机器”，they 可回指 a collection of geniuses..., develop such a device 近义复现 create a fabulous machine；第二块语义介绍“他们将机器（电脑）连接入网”，实现与下文第三段“联网电脑”的衔接，选项在语义上能够承上启下；另外，时间状语 The second half of the 20th century 与选项中 by the turn of the millennium 一前一后，按时间顺序呈递“联网电脑”的发展过程，逻辑合理，故敲定 [C] 为本题答案。"
        )
        print("Calibrated 2012 ky1 Q41")
    elif so == 42:
        q['explanation'] = (
            "42. 本题考核的知识点是：词汇复现 + 上下文衔接。正确率：76%\n"
            "【空格推测】空格下文分析“我称其为'隐秘战争'的原因”，推测空格内容应涉及“隐秘战争”。\n"
            "【答案敲定】由选项分析可知，[D] 为本题备选项。\n"
            "[D] 引出并具体介绍“隐秘战争”的概念，与下文分析“为何如此命名”形成的逻辑合理；同时选项指出“联网电脑触发的隐秘战争影响深远”，意在提醒人们联网电脑存在隐患，要谨慎，与上文“人们要谨慎对待联网电脑”语义一致，This is because 所体现的选项与上文因果逻辑成立，故敲定 [D] 为本题答案。"
        )
        print("Calibrated 2012 ky1 Q42")
    elif so == 43:
        q['explanation'] = (
            "43. 本题考核的知识点是：词汇复现 + 代词指代 + 上下文衔接。正确率：62%\n"
            "【空格推测】上文介绍人类较之动物的独特之处“能够创造额外物质财富和精神体验”，下文则另起一段转折指出“人类仍然拘泥于下载模式”，也即人类并未充分利用其主动创造的特性，推测空格可能涉及“人类特性和下载模式之间的关系”。\n"
            "【答案敲定】由选项分析可知，[A] 为本题备选项。\n"
            "[A] 首句以强调句式指出“额外事物”与“人类本性”之间的明显关系，与上文“人类的独特在于能够创造额外事物”经由语义重合点“额外事物”衔接（指代词 these 实现回指），共同说明“人类有创造的本性”，前后内容可顺滑衔接；选项第二句“人类不能超越下载和消费文化（即不能主动创造）将有失人类本性”反向探讨创造性的重要性，与空格后文“但现在人类仍然拘囿于下载模式”转折自然（虽然创造性很重要，但是人类并没有充分利用创造性）。故敲定 [A] 为本题答案。"
        )
        print("Calibrated 2012 ky1 Q43")
    elif so == 44:
        q['explanation'] = (
            "44. 本题考核的知识点是：词汇复现 + 上下文衔接。正确率：55%\n"
            "【空格推测】上文指出，人类局限在下载模式中，从而形成了一个“创造金字塔”；下文第七段则转移对象介绍电视的特点“信息单向流动”，推测空格可能承上阐释“创造金字塔”的影响、原因等，也可能承上启下，由“创造金字塔”过渡至“电视”。\n"
            "【答案敲定】由选项分析可知，[E][F] 为本题备选项。\n"
            "[E] 提及“电脑”与“电视”，分别对应上文“新文化机器”和下文“电视”，似乎能够承上启下，但选项内容“电脑对电视构成挑战”与上文“创造金字塔”毫不相关，话题出现太过突兀，逻辑词 thus 所体现的选项与上文的因果逻辑更是无从得出，故排除。\n"
            "[F] 承接上文“创造金字塔”分析其形成的原因指出“人类的媒体文化一直被电视所影响，而电视的本质就是'下载'”，即下载模式长期左右人类文化，能够解释上文“人类为何仍困于下载模式之中”，因果逻辑合理；另外选项通过追本溯源引出“电视”这一信息，并指出“电视的下载本质”，下文第七段则具体说明该本质“电视信息具有单向流动性，人们只能被动接收”，衔接顺畅，能起到过渡作用。故 [F] 为本题答案。"
        )
        print("Calibrated 2012 ky1 Q44")
    elif so == 45:
        q['explanation'] = (
            "45. 本题考核的知识点是：词汇复现 + 上下文衔接。正确率：33%\n"
            "【空格推测】空格下文另起一段就“何为有意义的上传”提问，反向推测空格内容涉及“有意义的上传”。\n"
            "【答案敲定】由选项分析可知 [B][E][G] 为本题备选项。\n"
            "[B] 虽复现第八段关键词 stickiness“粘性”，但选项举例“某些网站如何增加粘性”与上文“电视是单向媒介”内容毫不相关，更无例证关系；且选项并未涉及“有意义的上传”，不能与下文衔接，故排除。\n"
            "[E] 复现上文关键词 television，看似由上文“电视的单向性特点”过渡至“电脑对电视构成的挑战”，但 thus 表明与选项衔接的上文应提及“电脑和电视的对立、电脑较之电视的优势”，但现有第七段并无该内容，与选项不能构成因果逻辑；另外，选项并未涉及“有意义的上传”，不能与下文第八段衔接，故排除。\n"
            "[G] 指出“联网电脑鼓励人们选择性下载，更重要的是进行有意义的上传”，递进结构 even more importantly 引出新信息“有意义的上传”，下文进而就新信息设问“何为有意义的上传”，衔接顺畅；同时，选项中出现特指名词 the flow“这种流向”可回指上文 one-way tap flowing“（电视信息）单向流动”，选项内容即为，联网电脑（既能上传也能下载）扭转了电视信息的单向流动模式，衔接顺畅合理。故敲定 [G] 为本题答案。"
        )
        print("Calibrated 2012 ky1 Q45")

json.dump(d_2012, open(f_2012, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("\nAll Round 15 calibrations successfully applied!")
