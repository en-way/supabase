# -*- coding: utf-8 -*-
"""
Round 37 Calibration Script (Self-contained)
Target:
1. 2013 ky1 Text 1 (Q21-Q25) in 6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json
2. 2007 ky1 Text 1 (Q21-Q25) in e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

text_2013_q21 = """［精准定位］第一段①句指出Priestly在斥责助手，原因是助手认为高端时尚与己无关。②句Priestly解释时尚如何自上而下，并指出助理毛衫颜色过时。可见助理受斥原因是对时尚不敏感，［A］正确。
［命题解密］题干+［A］同义改写第一段①句：criticize... for与scolds... for同义；imagining that high fashion doesn't affect her与her insensitivity to fashion近义。
［B］将①句助理受斥原因“认为高端时尚与己无关（imagining... doesn't affect her）”改为完全相反的“痴迷于高端时尚（obsession with）”。［C］对②句bargain望文生义：该词在文中用于说明助理毛衫出处“清货区（bargain bin）”，和“议价能力（bargaining skill）”毫无关系。［D］对①句imagining... doesn't...断章取义：该内容指“助理认为时尚与己无关”，无关“想象力的匮乏（lack of imagination）”。
［技巧总结］本题考查“人物观点+因果事实”，题目定位容易、但准确理解定位信息难（表述较抽象，且含专有名词）。解题关键在于借助下文（继续阐释同一事件）仔细推敲文字确切含义，切忌望文生义。
具体来看，第一段以Priestly... scolds...、Priestly explains...衔接，共同说明Priestly观点。解题时首先可根据criticize... for与scolds... for的同义关系直接定位到①句imagining that high fashion doesn't affect her，但需借助②句解释才可确定［A］为其真正含义（fashion虽和high fashion看似不同，所指实则相同），是正确项。［B］与直接定位信息完全相反，［C］对②句bargain（bin）望文生义（与段落内容无关），二者均较易排除。［D］与直接定位信息imagining... doesn't...看似对应，有较强干扰性，但根据②句解释可知偏离文意。"""

text_2013_q22 = """［精准定位］第二段④句指出，大众品牌鼓励消费者“将衣服看做一次性产品、隔不了几周便要更新一次衣橱”。可见克莱恩认为大众品牌在力劝消费者频繁购衣，［B］正确。
［命题解密］题干+正确项［B］概括改写第二段④句：urge... to对应encourage... to；shop for their garments more frequently明确see clothes as disposable... renew their wardrobe every few weeks。
［A］源自第二段③句less wasted，但该句指大众品牌“库存浪费更少”，并非“鼓励消费者减少/对抗浪费”。［C］对第二段④句don't advertise断章取义：它并非指“大众品牌鼓励消费者不受广告影响”，而是说明“大众品牌不公开宣扬，而是暗中诱导消费者”。［D］利用第二段①句feverish world形成干扰。但该句指“克莱恩谴责疯狂的快时尚世界”，并非“克莱恩指出大众品牌在力劝消费者抵制疯狂的时尚界”。
［技巧总结］本题就长难句命制“事实概括+人物观点”题，要求考生就长难句中信息进行概括提炼，明确人物观点。解题时可采用思路：首先分析长难句，锁定正确项确切来源，并概括其主要内容，初步得出正确项；最后把握段落框架，得知人物整体观点，完全确定正确项（正确项与人物整体观点一致；错误项则往往存在矛盾）。
具体来看，首先根据题干mass-market labels urge consumers to定位到第二段④句These labels encourage style-conscious consumers to，并锁定正确项准确来源为see... meant to... and to renew...。随后概括具体内容“将衣服视为用完即弃，只用来穿一两水，没几周便更新一次衣橱”，初步确定选［B］。最后参考克莱恩整体观点“强烈谴责大众品牌推动的快时尚”（主要体现于第二段①、⑤句），可最终确定与之一致的［B］，同时排除与之矛盾的［A］、［C］、［D］。"""

text_2013_q23 = """［精准定位］由考查词所在句（第二段①句）可知，该词体现Cline就“快时尚”的总体态度。由下文（第二、三段）可知，Cline认为快时尚鼓动消费者频繁购衣，绑架了时尚周期，造成了多方危害。可见，Cline对快时尚持“谴责”态度，［D］为所考词正确含义。
［命题解密］正确项［D］accusation体现了第二段①句feverish一词的否定色彩，以及随后encourage consumers to see clothes as disposable... hijacked fashion cycles... rely on low-wage overseas labor... strain natural resources... use massive amounts of harmful chemicals传递的批判态度。
［A］弱化Cline对快时尚的“不认同”，总体偏“接受态度”，但文中丝毫未提及Cline对快时尚的肯定。［B］利用第一段①句doesn't affect her捏造干扰“Cline对快时尚漠不关心（indifference）”，但实际上该内容和Cline观点无关。［C］利用第二段①句feverish形成干扰，但该词为贬义（Cline认为快时尚非常疯狂），并非褒义（Cline对快时尚充满热情）。
［技巧总结］“词义题”虽然总体上都意在考查根据上下文推断词义的能力，但具体方向有所不同：有的侧重考查“文中同向/反向关系”，解题重点在于识别同义/近义/反义表达；有的考查“文中指代关系”，解题重点在于厘清多个主体之间错综复杂的关系；有的侧重考查“总分解释关系”（往往就概括性词汇命题），解题重点在于对详释部分进行概括。
本题重在最后一个考查角度，但也结合第一个角度：所考词是对Cline就“快时尚”态度的高度概括，解题之道重在概括后文内容（第二、三段），但同时也可借助“同向关系”（feverish与考查词indictment均体现Cline对快时尚的态度）。"""

text_2013_q24 = """［精准定位］末段③句指出，虚荣深植人心，人们只有在无力支付不可持续购物时，才会开始可持续性购物。可见，“定价”对于购物是否可持续/环境友好至关重要，［C］正确。
［命题解密］正确项［C］是基于全文内容对末段③句的顺势推导，environment-friendly purchasing同义替换原文shopping sustainably；pricing明确when they can't afford not to所指；is vital to明确will only start... when体现的二者关系。
［A］在末段关键词idealism和vanity间强加关联。文中只是指出“人性虚荣”，并未比较“理想主义者”相对整体人群的虚荣性。［B］对末段①句反向干扰，该句指出快时尚业已经关注可持续性（have made efforts to curb...）。［D］暗示“虚荣心”、与原文vanity is constant貌似契合，且unaffordable与原文can't afford对应，因此具有很大干扰性。但实际上末句是指出“人们只有在无力支付时，才会放弃过度购衣”，而不是“人们对买不起的昂贵服装更感兴趣”。
［技巧总结］本文就文章末段命制推理引申题，但该段文意经转折，最终提出作者观点，且涉及抽象概括的表述（idealism, vanity is constant等），双重否定兼省略句（③句），虚拟倒装结构（be it in food or in energy），故较难把握。解题时需要沉于文字，结合上下文仔细推敲文字的言外之意以及各句之间的逻辑联系。在最后面对两项难以抉择时，应以文章主题为纲做出取舍。
具体来看：首先定位对比，可排除与文意相悖的［B］、以及强加关联的［A］，剩下［C］［D］都与vanity is constant（虚荣深植人心）相吻合、且都能与末句相连，较难取舍。这时联系文章主题可知，本文讨论的并非“普通人买不起的昂贵服饰”而是“对环境造成极大损害的廉价时尚服饰”，故舍［D］选［C］。"""

text_2013_q25 = """［精准定位］文章第一至三段引出并介绍克莱恩该书作对大众品牌驱动快时尚的强烈批判。第四至六段介绍书中提出的快时尚应对方式——消费者停止购买，并指出这只是一种理想主义。可见，本文聚焦于克莱恩对快时尚的批判，［C］是文章恰当标题。
［命题解密］［C］criticism of the fast-fashion industry是克莱恩作品的主旨，是本文作者评论的对象。
［A］将文中表述see clothes as disposable... renew their wardrobe every few weeks... buy 20 billion garments a year... vanity is a constant兀自将其串成一副“奢侈生活”的图像，但实际上脱离文章主线：“快时尚”并不等于“奢侈的生活方式”。［B］错把引子部分的关键词high fashion当做全文主旨，而全文的着眼点在与之相悖的fast fashion。［D］偏离文章关注对象：文章关注的是“推动快时尚的大众市场品牌（mass market labels）”，并非“大众市场的秘密（mass market secrets）”。
［技巧总结］文章主旨题的正确选项不仅要体现“文章讨论对象”，还要契合“文章情感基调”。正确项［C］中fast fashion是遍布全篇的关键词，体现文章关注对象；criticism概括feverish、indictment、victims、impact on labor and environment，体现对快时尚的批判态度。［A］中“奢侈的生活方式（extravagant lifestyle）”，［B］中a high-fashion myth（高级时尚），［D］中大众市场（mass-market secret）均非全文关注对象。"""

text_2007_q21 = """［精准定位］文章前两段言及足球运动员生日现象并猜想其原因，后三段则以艾利克森研究为例探究出色表现的决定性因素，可见文章试图从足球领域的出色表现延伸至记忆力等其他更多领域的出色表现，说明其背后原因。因此开篇现象意在引出对“究竟是什么造就出色表现”的探讨，［C］正确。
［命题解密］正确项［C］中introduce the topic综合概括了本文“以现象引话题”的开篇方式，expert performance对应文中话题词汇elite（soccer players）、expert performers、high achievers。
［A］由第三段③④⑤句中反复出现的training而来，但文章旨在借助“反复训练能极大提升记忆能力”说明“后天培养的重要性”，从而否定“优秀表现源于先天”的观点，而非强调“专业训练本身的重要性”。
［B］由①②句中2006's World Cup tournament、elite soccer players、the World Cup而来，但该内容除前两段外下文未有涉及，显然文章旨在引领读者关注“球员生日怪象”而非“球星本人”。［D］利用首段句末even more pronounced设置干扰，但偷换了比较的对象：文中意在强调球员生日集中现象“颇为显著（不止世界杯，更大范围来看更是如此）”，而非“对球队的表现进行比较”。
［技巧总结］本题考查考生对开篇方式/开篇结构的把握。相对于开门见山论述话题的“直接式”开篇，“引入式开篇”（引子内容可为具体事例/现象、实验结论或哲理故事）更容易成为命题人的着眼点。此类题中，引入话题的现象/事例等本身往往并非关注点，而是扮演“引子”角色，引出正向或反向的观点或现象。解答此类题型时：①需要关注现象背后的内容/观点；②通览全篇，联系文章主旨大意判断。
如本题，首先，关注现象背后的内容/观点：文章首段提出“球员生日”这一具体现象后，第二段对这一现象的几种解释均暗藏先天条件、既定因素的作用，由此暗示一种观点：“出色源于先天遗传”，初步断定“球员生日现象”可能是文章讨论话题的引子。其次，通览全篇，联系文章主旨：后三段不再继续讨论现象，而是借某人物研究实验探讨出色表现的决定性因素，并由尾句主旨句（are nearly always made, not born），最终确定文章讨论对象乃“出色表现”，文首现象仅为引出这一话题服务，敲定［C］正确。"""

text_2007_q22 = """［精准定位］被考查词上文指出“狂热的球迷父母容易在春天受孕”，所在部分解释“此时（springtime）”，正是“一年中足球……的巅峰”，由此可知，soccer-mad与soccer mania应为同义复现，选项中craze最为接近mad（非常喜欢、痴迷）之意，所以［B］正确。
［命题解密］正确项［B］craze对应mad，从基本含义、感情色彩与感情强烈程度三个方面均实现了与mania的对等替换。
［A］将文中“mad（疯狂）”扭曲为“fun（乐趣）”，感情强烈程度大大减弱。［C］强调一种“近乎病态的情绪失控、不可理喻的极端行为”，多含贬义色彩，而文中单纯想表现“对足球狂热、痴迷”的心情，未触及“异常激动而举止失常”这层含义。［D］将原文“mad（疯狂）”弱化为“excitement（兴奋、激动）”，减弱了感情强烈程度。
［技巧总结］本题考查学生根据句内逻辑关系确定语义关系（反义、同义、上下义等）的能力。被考查词mania所在部分与其前部分由逗号隔开，初步判断两部分为解释说明关系（逗号通常起着解释说明作用），随后注意到前后两个时间表达：at the annual peak of...紧接in springtime，显然是为解释前者服务，由此可断定soccer-mania与其前soccer-mad为同义关系，最终锁定答案为［B］。"""

text_2007_q23 = """［精准定位］第四段②③句明确指出艾利克森的研究结论（即个人观点）：后天的信息编码能力完全能压倒先天因素，决定记忆能力的高低，而刻意练习又是提高有目的信息编码能力的最佳方法。也就是说，好的记忆力在于对信息进行有目的的处理，［A］正确。
［命题解密］正确项［A］是对第四段②③句内容的合理概括和改写。其中depends on对应swamped by所蕴含的强大力量（即信息编码能力的“决定性”作用）；meaningful processing of information对应②句how well... encodes the information以及③句encode information meaningfully。
［B］将段中①句“记忆行为是认知活动而非直觉（more of a cognitive exercise than an intuitive one）”反向曲解为“好记忆源于直觉而非认知”。［C］将①句中“记忆力本身非基因所决定”反向曲解为“由基因决定”，并添加无关信息“心理因素”。［D］断章取义，利用⑤句concentrating一词臆断“好记性需要注意力高度集中”，但文中concentrating as much on... as on...意不在强调“注意力本身”，而是强调“要对技巧和结果投以同样的重视”。
［技巧总结］本题形似考查人物观点，实质考查事实细节。解答此题的重点在利用句群内隐含的语义逻辑关系去揣摩“难以理解的关键句”，并借助语义逻辑关联“跳出细节，挑出重点”；并将选项和原文对比，排除与原文逻辑不符的选项。
如本题，段中①句以not genetically determined否定“先天遗传因素”之后，进一步以more of... than...结构取前（a cognitive exercise）舍后（an intuitive one），对比选项后即可排除［B］、［C］；②句借助are swamped by...结构（swamp虽为生僻词，却可通过该句内以whatever标记的“先让步后转折”的语义逻辑关联窥见其大致语义）将重点信息引至how well... “encodes” the information，由此推出“信息编码”对“记忆”的重要性，初步选定［A］为正确项。进而再以③句encode information meaningfully与选项［A］的近义可以最终敲定该选项的正确性。［D］看似符合④⑤句... more than... Rather所示的“舍前取后”逻辑，但仔细对比却发现偷换原文细节概念；应注意，考查核心观点或段落主旨时，借助段中琐碎细节信息设置的选项往往作为干扰项出现，相比之下，正确项则通常具有归纳概括性。"""

text_2007_q24 = """［精准定位］第五段④句以另一种方式重述了③句艾利克森及其同事的最终研究结论：表现出色的人几乎都是后天培养而非先天遗传的。［D］正确。
［命题解密］正确项［D］是对文章主旨句（末句）的同义改写。其中high achievers和owe success mostly to nurture分别对应expert performers和are nearly always made。注：nurture一词意为“培养，教育”，偏重后天因素，与偏重先天的nature构成一对经典矛盾。
［A］强调“天赋”的重要性，恰与全文“强调后天努力而否定天赋”的主基调相反。［B］干扰来自②句biographical details，但此处意在强调“研究的科学严谨性（收集研究对象生平资料为研究工作之一）”，而非探讨“生平资料信息包含解释出色表现的原因”。［C］将③句天赋“被过高估计”反向曲解为“被忽略”。
［技巧总结］本题同上题，形似考查人物观点，实质考查研究的最终结论（实为全篇内容的提炼升华）。解答此题的关键在：1、找出研究结论句，正确答案往往是对研究结论的同义替换；2、结合上下文更多线索锁定正确答案。
如本题，③④句呈现研究结论，首先应格外关注冒号后内容：“talent is highly overrated、expert performers are nearly always made”为同一语义正反两面不同方式的表述，阐明文章主旨“出色者乃后天造就，而非天赋使然”，初步锁定［D］；其次，根据上文（第四段）艾利克森有关记忆力的研究结论“记忆力通过后天刻意练习可以得到提升”可进一步推知“后天培养对出色表现的重要作用”，由此最终敲定［D］正确。"""

text_2007_q25 = """［精准定位］文章开篇由“优秀球员生日现象”引入，引发“优秀是否源于天生”这一疑问；后以艾利克森一系列研究说明“记忆能力并非基因决定，而是刻意练习下的认知活动”，末段则以其更多研究突破单纯“对记忆能力的阐释”，明确指出“天赋”被高估，各领域的优秀表现几乎都是通过后天的努力练习造就的，故［C］正确。
［命题解密］正确项［C］是对文章主旨句（文末句）的概括，其中practice、perfect分别对应made（后天培养）、expert performers（出色表现者）。
［A］从②句They gather all the data they can, not just... but also...推断出“研究者们怀揣坚定信念投身研究，最终得出正确结论”，但文中旨在强调“后天练习 vs 先天基因”两者对于优秀表现的影响，而不在于说明“成功源于执着的信念（faith）”。［B］喻义“因果报应”，能体现“足够努力便会收获成功”，但侧重点在于“产出和投入一致，后者决定前者”，偏离本文批驳立意“优秀无关天赋，而是源自后天勤奋”。［D］强调“先天因素”，干扰源自第二段②句“父母遗传因素对孕育优秀球员的影响”，但后文对这种先天因素予以了否定。
［技巧总结］本文以现象开篇，引出话题并树靶；继而依据研究打靶并提出新观点。命题人借谚语考查学生概括全文主旨的能力。此题需要从文章主旨句（往往出现于首尾段、与开篇方式紧密相关）入手，抓住文章脉络进行解答。"""

# 1. Calibrate 2013 ky1
file_2013 = 'public/data/exams/6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json'
with open(file_2013, 'r', encoding='utf-8') as f:
    d13 = json.load(f)

calibrated_count_13 = 0
for q in d13['questions']:
    so = q.get('sort_order')
    if so == 21:
        q['stem'] = 'Priestly criticizes her assistant for her ________.'
        q['explanation'] = text_2013_q21
        calibrated_count_13 += 1
    elif so == 22:
        q['stem'] = 'According to Cline, mass-market labels urge consumers to ________.'
        q['explanation'] = text_2013_q22
        calibrated_count_13 += 1
    elif so == 23:
        q['stem'] = 'The word "indictment" (Line 3, Para. 2) is closest in meaning to ________.'
        q['explanation'] = text_2013_q23
        calibrated_count_13 += 1
    elif so == 24:
        q['stem'] = 'Which of the following can be inferred from the last paragraph?'
        q['explanation'] = text_2013_q24
        calibrated_count_13 += 1
    elif so == 25:
        q['stem'] = 'What is the subject of the text?'
        q['explanation'] = text_2013_q25
        calibrated_count_13 += 1

with open(file_2013, 'w', encoding='utf-8') as f:
    json.dump(d13, f, ensure_ascii=False, indent=2)

print(f"2013 ky1 calibration completed: {calibrated_count_13} questions calibrated.")

# 2. Calibrate 2007 ky1
file_2007 = 'public/data/exams/e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json'
with open(file_2007, 'r', encoding='utf-8') as f:
    d07 = json.load(f)

calibrated_count_07 = 0
for q in d07['questions']:
    so = q.get('sort_order')
    if so == 21:
        q['stem'] = 'The birthday phenomenon found among soccer players is mentioned to ________.'
        q['options'] = [
            {'key': 'A', 'text': 'stress the importance of professional training', 'value': 'A'},
            {'key': 'B', 'text': 'spotlight the soccer superstars in the World Cup', 'value': 'B'},
            {'key': 'C', 'text': 'introduce the topic of what makes expert performance', 'value': 'C'},
            {'key': 'D', 'text': 'explain why some soccer teams play better than others', 'value': 'D'}
        ]
        q['explanation'] = text_2007_q21
        calibrated_count_07 += 1
    elif so == 22:
        q['stem'] = 'The word “mania” (Line 4, Paragraph 2) most probably means ________.'
        q['options'] = [
            {'key': 'A', 'text': 'fun', 'value': 'A'},
            {'key': 'B', 'text': 'craze', 'value': 'B'},
            {'key': 'C', 'text': 'hysteria', 'value': 'C'},
            {'key': 'D', 'text': 'excitement', 'value': 'D'}
        ]
        q['explanation'] = text_2007_q22
        calibrated_count_07 += 1
    elif so == 23:
        q['stem'] = 'According to Ericsson, good memory ________.'
        q['options'] = [
            {'key': 'A', 'text': 'depends on meaningful processing of information', 'value': 'A'},
            {'key': 'B', 'text': 'results from intuitive rather than cognitive exercises', 'value': 'B'},
            {'key': 'C', 'text': 'is determined by genetic rather than psychological factors', 'value': 'C'},
            {'key': 'D', 'text': 'requires immediate feedback and a high degree of concentration', 'value': 'D'}
        ]
        q['explanation'] = text_2007_q23
        calibrated_count_07 += 1
    elif so == 24:
        q['stem'] = 'Ericsson and his colleagues believe that ________.'
        q['options'] = [
            {'key': 'A', 'text': 'talent is a dominating factor for professional success', 'value': 'A'},
            {'key': 'B', 'text': 'biographical data provide the key to excellent performance', 'value': 'B'},
            {'key': 'C', 'text': 'the role of talent tends to be overlooked', 'value': 'C'},
            {'key': 'D', 'text': 'high achievers owe their success mostly to nurture', 'value': 'D'}
        ]
        q['explanation'] = text_2007_q24
        calibrated_count_07 += 1
    elif so == 25:
        q['stem'] = 'Which of the following proverbs is closest to the message the text tries to convey?'
        q['options'] = [
            {'key': 'A', 'text': '“Faith will move mountains.”', 'value': 'A'},
            {'key': 'B', 'text': '“One reaps what one sows.”', 'value': 'B'},
            {'key': 'C', 'text': '“Practice makes perfect.”', 'value': 'C'},
            {'key': 'D', 'text': '“Like father, like son.”', 'value': 'D'}
        ]
        q['explanation'] = text_2007_q25
        calibrated_count_07 += 1

with open(file_2007, 'w', encoding='utf-8') as f:
    json.dump(d07, f, ensure_ascii=False, indent=2)

print(f"2007 ky1 calibration completed: {calibrated_count_07} questions calibrated.")
