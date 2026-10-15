import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Starting master calibration of exam data...")

# Map of (year, cat, sort_order) -> new_answer
ANSWER_FIXES = {
    # 2001 ky1
    (2001, 'ky1', 4): 'B',
    (2001, 'ky1', 8): 'B',
    (2001, 'ky1', 18): 'C',
    # 2002 ky1
    (2002, 'ky1', 4): 'B',
    (2002, 'ky1', 6): 'A',
    (2002, 'ky1', 12): 'A',
    (2002, 'ky1', 15): 'B',
    (2002, 'ky1', 16): 'D',
    (2002, 'ky1', 19): 'C',
    (2002, 'ky1', 21): 'C',
    (2002, 'ky1', 23): 'D',
    (2002, 'ky1', 33): 'D',
    (2002, 'ky1', 34): 'A',
    (2002, 'ky1', 37): 'C',
    (2002, 'ky1', 40): 'D',
    # 2003 ky1
    (2003, 'ky1', 3): 'C',
    (2003, 'ky1', 4): 'D',
    (2003, 'ky1', 10): 'D',
    (2003, 'ky1', 11): 'A',
    (2003, 'ky1', 12): 'D',
    (2003, 'ky1', 13): 'B',
    (2003, 'ky1', 16): 'D',
    (2003, 'ky1', 23): 'C',
    (2003, 'ky1', 28): 'B',
    (2003, 'ky1', 33): 'C',
    (2003, 'ky1', 36): 'C',
    (2003, 'ky1', 37): 'A',
    (2003, 'ky1', 39): 'D',
    # 2011 ky1
    (2011, 'ky1', 4): 'B',
    # 2013 ky1
    (2013, 'ky1', 21): 'A',
    # 2014 ky1
    (2014, 'ky1', 21): 'A',
    (2014, 'ky1', 22): 'C',
    # 2015 ky1
    (2015, 'ky1', 24): 'A',
    (2015, 'ky1', 28): 'D',
    (2015, 'ky1', 29): 'D',
    (2015, 'ky1', 30): 'D',
    (2015, 'ky1', 39): 'C',
    (2015, 'ky1', 40): 'B',
    # 2016 ky1
    (2016, 'ky1', 23): 'D',
    (2016, 'ky1', 34): 'A',
    (2016, 'ky1', 37): 'B',
    # 2017 ky1
    (2017, 'ky1', 6): 'D',
    (2017, 'ky1', 21): 'A',
    (2017, 'ky1', 23): 'D',
    (2017, 'ky1', 25): 'C',
    # 2020 ky1
    (2020, 'ky1', 11): 'C'
}

# Detailed Question Calibrations (stem, options, explanation)
DETAILED_QUESTION_FIXES = {
    # 2002 ky1 Q4
    (2002, 'ky1', 4): {
        'stem': 'Choose the best option for blank [4] in the passage:',
        'options': [
            {'key': 'A', 'text': '(in the) process (of)', 'value': 'A'},
            {'key': 'B', 'text': '(in the) company (of)', 'value': 'B'},
            {'key': 'C', 'text': '(in the) light (of)', 'value': 'C'},
            {'key': 'D', 'text': '(in the) form (of)', 'value': 'D'}
        ],
        'answer': 'B',
        'explanation': '［A］ (in the) process (of)在... 过程中\n［B］ (in the) company (of)在....陪伴下；与.... 同时出现\n［C］ (in the) light (of)考虑到，鉴于，根据\n［D］ (in the) form (of)以....的形式\n［试题考点］上下文语义+介词短语辨析\n［解题思路］③句以“19世纪报纸成为主要传播媒介的时间”为参照点，用一条线罗列宣传册、书籍、期刊、报纸作为主要传播媒介的发展历程。其中following in the wake of...指“报纸紧跟宣传册和书之后而来”；而空格处连接“期刊”，应体现“期刊与报纸在时间上的先后顺序”,选项中体现时间线索的只有［B］项(in the) company (of),意为“与……同时出现”，至此纸质媒体的发展顺序可整理为：先是宣传册与图书，然后19世纪报纸伴随期刊一同成为印刷时代的主流媒介。\n［错项排除］［A］［C］［D］三项都不能体现期刊与报纸两者在时间上的关系；其中 ,in the process of表示进程，in the light of侧重“考虑问题的根据、视角等”，in the form of表示“形式”。'
    },
    # 2002 ky1 Q6
    (2002, 'ky1', 6): {
        'stem': 'Choose the best option for blank [6] in the passage:',
        'options': [
            {'key': 'A', 'text': '(lead) on', 'value': 'A'},
            {'key': 'B', 'text': '(lead) out', 'value': 'B'},
            {'key': 'C', 'text': 'over', 'value': 'C'},
            {'key': 'D', 'text': '(lead) off', 'value': 'D'}
        ],
        'answer': 'A',
        'explanation': '［A］ (lead) on引导，率领……继续前进\n［B］ (lead) out领舞伴起舞;鼓励、逗引(某人)讲话\n［C］ over不与lead搭配\n［D］ (lead) off起始于；开始\n［试题考点］短语动词搭配+副词词义辨析\n［解题思路］通过对上题的分析，可知④句主题为通信革命进程，空格6、7同样位于此句，均表示进程。其主干部分说明，通信革命在19世纪(during the same time)加速发展。beginning with. . . leading 6 through...部分为现在分词做状语，详细描述通讯革命加速发展的进程态势：始于铁路，然后是电报电话等，此处空格前lead意为“带路、引路、前行”，因此空格处应能体现“继续前进”的态势。介词on含有be continuing to do sth"继续地，向前地"之意，与lead连用，凸显了通信革命一路向前、马不停蹄的发展势头。［A］项正确。\n［错项排除］out与lead搭配意为“领舞伴起舞；鼓励、逗弓|(某人)讲话”，脱离全句主题；over不与lead搭配，其本身作为进程讲含有“结束”的意思，而文中表示的却是“继续往前发展”。［D］项lead off (from) sth意为“起始于(某地)% lead (sth) off则指“开始做某事”，不合文意。'
    },
    # 2001 ky1 Q8
    (2001, 'ky1', 8): {
        'stem': 'Choose the best option for blank [8] in the passage:',
        'options': [
            {'key': 'A', 'text': 'present', 'value': 'A'},
            {'key': 'B', 'text': 'offer', 'value': 'B'},
            {'key': 'C', 'text': 'manifest', 'value': 'C'},
            {'key': 'D', 'text': 'indicate', 'value': 'D'}
        ],
        'answer': 'B',
        'explanation': '［A］ present提交，提出\n［B］ offer主动提出，提供，给予\n［C］ manifest表明，清楚显示（尤指情感、态度或品质）\n［D］ indicate显示，暗示\n［试题考点］动词词义辨析\n［解题思路］空格所在的定语从句修饰a committee report,指出"该报告认为自我监管没有... 足够的监控”。而大法官对此表示赞同。did not offer sufficient control意为“没提供足够的监控”，符合上下文语义。故［B］正确。\n［错项排除］manifest和indicate的含义为“显示，呈现，指示”，与“足够的监控”搭配，显然不符合文意。present—般指"（正式地）呈递"，不与control搭配。'
    },
    # 2003 ky1 Q33
    (2003, 'ky1', 33): {
        'stem': 'It can be inferred from Paragraph 3 that',
        'options': [
            {'key': 'A', 'text': 'shippers will be charged less without a rival railroad', 'value': 'A'},
            {'key': 'B', 'text': 'there will soon be only one railroad company nationwide', 'value': 'B'},
            {'key': 'C', 'text': 'overcharged shippers are unlikely to appeal for rate relief', 'value': 'C'},
            {'key': 'D', 'text': 'a government board ensures fair play in railway business', 'value': 'D'}
        ],
        'answer': 'C',
        'explanation': '［精准定位］第三段末句提到，申诉过程既耗财又耗时，并且只有在极端情况下才有效，从而暗示多数托运商不太可能因为收费高而申诉。所以［C］正确。\n［命题解密］正确项［C］是第三段③句的同义改写,overcharged shippers对应文中Shippers who... charged；are unlikely to appeal for the rate relief 对应文中 but the process... work only in truly extreme cases。\n［A］颠倒②句比较关系：将（be） charged 20 to 30 percent more（托运商将会被提高收费）改为be charged less（托运商将会被降低收费）。［B］将①句“多数托运商仅由一家铁路公司服务”改为“全国将只有一家铁路公司”。［D］对③句前半句“若托运商觉得被索价过高，可上诉到联邦政府的地面运输委员会”断章取义、得岀貌似正确的结论“政府部门可保证铁路行业的公平竞争”，却忽略了随后部分（but...）转而否定了这一可能。'
    },
    # 2011 ky1 Q5
    (2011, 'ky1', 5): {
        'stem': 'Choose the best option for blank [5] in the passage:',
        'options': [
            {'key': 'A', 'text': 'measurable', 'value': 'A'},
            {'key': 'B', 'text': 'manageable', 'value': 'B'},
            {'key': 'C', 'text': 'affordable', 'value': 'C'},
            {'key': 'D', 'text': 'renewable', 'value': 'D'}
        ],
        'answer': 'A',
        'explanation': '5. ［A］ measurable 显著的 ［B］ manageable 可处理的 ［C］ affordable负担得起的 ［D］ renewable可再生的\n［考点提炼］句内语义+形容词辨析。正确率：70%\n［解题思路］上文表明，笑很可能对身体健康影响甚微，只能引起身体机能短期变化；本句通过方式状语the way walking or jogging does将"大笑"和"散步或慢跑"作比较，以unlikely说明"前者不如后者对身体的积极影响大”，选项中和benefits连用表现“成效大”的只有［A］。\n［错项排除］其余三项都只能表示“（因有某技能、素质而）能够……的”，侧重说明“能力”。［B］强调“在尺寸、数量以及难度水平上应付得过来”。［C］强调“买得起、担负得起的”。［D］利用其“延长”这层释义干扰，认为“大笑没法和散步一样产生持续效果”，但该释义涉及主体对象为“协议、官方文件等”，强调“有效期可延长的”。'
    },
    # 2011 ky1 Q18
    (2011, 'ky1', 18): {
        'stem': 'Choose the best option for blank [18] in the passage:',
        'options': [
            {'key': 'A', 'text': 'adapted', 'value': 'A'},
            {'key': 'B', 'text': 'catered', 'value': 'B'},
            {'key': 'C', 'text': 'turned', 'value': 'C'},
            {'key': 'D', 'text': 'reacted', 'value': 'D'}
        ],
        'answer': 'D',
        'explanation': '18. ［A］ adapted 适应 ［B］ catered 迎合 ［C］ turned 求助于；改用 ［D］ reacted 回应\n［考点提炼］上下文语义+动词辨析。正确率：70%\n［解题思路］空格所在句为实验结果，由下文所得实验结论“表情可以影响情绪”以及“笑这一行为也能够改善情绪”可知，做微笑表情的人能够表现出更为激烈的情绪，只有［D］能体现这层含义。\n［错项排除］［A］指“为了融入新情形调整、改变行为和态度等”，要适应的对象一般是“新环境/情况/变化等”，而文中宾语为funny cartoons,不存在“需要对之适应”一说。［B］表示“满足某种需求或欲望”，而“牙咬钢笔的参与者迎合卡通书的需求”不合逻辑。［C］一方面表示“求助于……”，另一方面强调“开始使用新东西，尤指作为解决问题的方式”，而文中“幽默画册”仅仅是实验者用于考查参与者情绪的引子，而“……更热切地求助于/开始使用卡通画册”重心落在了“画册”上，与实验目的“了解身体反应VS情绪的关系”相去甚远。'
    },
    # 2011 ky1 Q19
    (2011, 'ky1', 19): {
        'stem': 'Choose the best option for blank [19] in the passage:',
        'options': [
            {'key': 'A', 'text': 'suggesting', 'value': 'A'},
            {'key': 'B', 'text': 'requiring', 'value': 'B'},
            {'key': 'C', 'text': 'mentioning', 'value': 'C'},
            {'key': 'D', 'text': 'supposing', 'value': 'D'}
        ],
        'answer': 'A',
        'explanation': '19. ［A］ suggesting 表明 ［B］ requiring 需要 ［C］ mentioning 提到 ［D］ supposing 假设\n［考点提炼］句内语义。正确率：90%\n［解题思路］空格句部分在全句中充当状语，前文为“具体实验”，实验结果指出：假笑者比皱眉者对滑稽画册的反应更为强烈，也即：笑这一身体动作能够影响情绪（更能感知到幽默），因此空格部分是对前文实验结果的进一步结论，符合要求的只有［A］。\n［错项排除］［B］用于引出“某事实现的条件”，而文中前半部分为“两种参与者的不同反应”这一客观情况，空格后为“具体结论”，“情况需要/要求结论”逻辑不通；其次从语法角度看.require接that从句时需使用虚拟语气。［C］表“提及，谈到”，而“实验结果提及实验结论”显然不是实验研究所应有的逻辑。［D］—方面用于“引出观点”，其逻辑主语为“人”，而文中逻辑主语为“实验结果”；另一方面用于“假定某可能情况，从而考虑该情况下的结果”，而文中that从句为实验结论，而非“假设情况”。'
    },
    # 2012 ky1 Q12
    (2012, 'ky1', 12): {
        'stem': 'Choose the best option for blank [12] in the passage:',
        'options': [
            {'key': 'A', 'text': 'serve', 'value': 'A'},
            {'key': 'B', 'text': 'satisfy', 'value': 'B'},
            {'key': 'C', 'text': 'upset', 'value': 'C'},
            {'key': 'D', 'text': 'replace', 'value': 'D'}
        ],
        'answer': 'C',
        'explanation': '12. ［A］ serve 服务 ［B］ satisfy 满足 ［C］ upset 使苦恼；打败 ［D］ replace 代替，取代\n［考点提炼］句内语义+熟词僻意。正确率：23%\n［解题思路］段首句“宪法制定者们的设想是法律拥有独立于政治的权威”，也就是说,受终身制保护的情况下，法官无需惧怕或迎合当权者，可以自由行使司法权；符合文意的只有［C］,此处用其僻意“打败实力被认为远超自己的对手”，文中表示“法官可以毫无顾虑地惩治违法的当权者”。\n［错项排除］［A］强调“履行义务”；［B］表示“使满足”；两项均体现“为当权者的利益服务”，与文意相反。［D］表示“取代”，但法官与当权者（分别为“司法”和“行政”）隶属于不同系统，前者无法取代后者。'
    },
    # 2013 ky1 Q21
    (2013, 'ky1', 21): {
        'stem': 'Priestly criticizes her assistant for her',
        'options': [
            {'key': 'A', 'text': 'insensitivity to fashion', 'value': 'A'},
            {'key': 'B', 'text': 'obsession with high fashion', 'value': 'B'},
            {'key': 'C', 'text': 'poor bargaining skill', 'value': 'C'},
            {'key': 'D', 'text': 'lack of imagination', 'value': 'D'}
        ],
        'answer': 'A',
        'explanation': '［精准定位］第一段①句指出Priestly在斥责助手，原因是助手认为高端时尚与己无关。②句Priestly解释时尚如何自上而下，并指出助理毛衫颜色过时。可见助理受斥原因是对时尚不敏感，［A］正确。\n［命题解密］题干+ ［A］同义改写第一段①句:criticize. . . for与scolds. . . for同义；imagining that high fashion doesn\'t affect her 与 her insensitivity to fashion 近义。\n［B］将①句助理受斥原因“认为高端时尚与己无关(imagining... doesn\'t affect her)”改为完全相反的"痴迷于高端时尚(obsession with)”。［C］对②句bargain望文生义：该词在文中用于说明助理毛衫出处“清货区(bargain bin)”,和“议价能力(bargaining skill)”毫无关系。［D］对①句 imagining. . . doesn\'t...断章取义：该内容指“助理认为时尚与己无关”，无关“想象力的匮乏(lack of imagination)”。'
    },
    # 2016 ky1 Q2
    (2016, 'ky1', 2): {
        'stem': 'Choose the best option for blank [2] in the passage:',
        'options': [
            {'key': 'A', 'text': 'adapt to', 'value': 'A'},
            {'key': 'B', 'text': 'provide for', 'value': 'B'},
            {'key': 'C', 'text': 'compete with', 'value': 'C'},
            {'key': 'D', 'text': 'decide on', 'value': 'D'}
        ],
        'answer': 'D',
        'explanation': '2. ［A］ adapt to 适应 ［B］ provide for 供养，抚养 ［C］ compete with 与... 竞争 ［D］ decide on 决定；选定\n［考点提炼］句内语义+动词词组语义辨析。\n［解题思路］空格所在的③句实为由并列连词or连接的两个分句，or后面的句子从男方父母的角度(the young man\'s parents)指出父母替孩子选择配偶(may make the choice of a spouse) ,or 前面的句子则从男方本人角度(A young man)指出男方自主(on his own)选择配偶，因此不难推知______ a likely spouse 与 make the choice of a spouse 近义，空格处应表达"选择"的语义，［D］意为 to choose sth from a number of possibilities,符合文意。'
    },
    # 2016 ky1 Q5
    (2016, 'ky1', 5): {
        'stem': 'Choose the best option for blank [5] in the passage:',
        'options': [
            {'key': 'A', 'text': 'Although', 'value': 'A'},
            {'key': 'B', 'text': 'Lest', 'value': 'B'},
            {'key': 'C', 'text': 'After', 'value': 'C'},
            {'key': 'D', 'text': 'Unless', 'value': 'D'}
        ],
        'answer': 'C',
        'explanation': '5. ［A］ Although尽管；不过 ［B］ Lest以免；唯恐 ［C］ After在……之后 ［D］ Unless除非\n［考点提炼］上下文逻辑。\n［解题思路］空格后指出，______配偶已经被选定，双方家庭相互调查，由空格句语义以及动词时态的过渡has been selected-investigates可知，前后两种行为是程序性的先后关系：配偶选定之后，双方家庭开始相互调查家庭背景，［C］ After符合这一顺承逻辑。\n［错项排除］［A］通常表让步，还可对前述内容做出评价，表语义的轻微转折，但语义重点仍落于主句；此处“配偶已经选定”与“双方开始调查家庭背景”为顺承逻辑，而非让步或转折逻辑；［B］或表目的，引出竭力避免或不希望发生的情况；［D］表条件，“选定配偶”是“双方家庭开始调查家庭背景”的前提，“以免/除非配偶已经被选定，双方家庭开始调查家庭背景”均不合逻辑。'
    },
    # 2017 ky1 Text 2 (Q26-Q30)
    (2017, 'ky1', 26): {
        'stem': "Queen Liliuokalani's remark in Paragraph 1 indicates",
        'options': [
            {'key': 'A', 'text': 'her conservative view on the historical role of astronomy', 'value': 'A'},
            {'key': 'B', 'text': 'the importance of astronomy in ancient Hawaiian society', 'value': 'B'},
            {'key': 'C', 'text': 'the regrettable decline of astronomy in ancient times', 'value': 'C'},
            {'key': 'D', 'text': "her appreciation of star watchers' feats in her time", 'value': 'D'}
        ],
        'answer': 'B',
        'explanation': '［精准定位］①句直引利留卡拉尼女王之言“古代夏威夷人都是天文学家”，②句随后解释“古代夏威夷社会观星师极受尊敬”。借由两句间“观星师与天文学家、天文学与天文学家、受尊敬与受重视”的语义关联可推断，女王之言实质表明了天文学家在古代夏威夷社会中的重要性，［B］正确。\n［命题解密］正确项［B］是对①②句的合理推断，其中the importance对应the most esteemed。\n［A］conservative利用惯性思维制造干扰，与①②句传达的女王对“古代天文学家备受重视，即天文学在古代有重要作用”毫无保留的肯定态度相悖。［C］将③④句暗含之今日情形“夏威夷天文学地位衰落（decline）偷换为女王之言所表古代情形。［D］利用②句Star watchers the most esteemed过度推导出“观星师因技艺高超、功勋卓著受到女王的赞赏”，且in her time（女王所处时代）与①句引言中ancient, were等词表明的信息“在女王生活时代之前的古代时期”明显相悖。'
    },
    (2017, 'ky1', 27): {
        'stem': 'Mauna Kea is deemed as an ideal astronomical site due to',
        'options': [
            {'key': 'A', 'text': 'its geographical features', 'value': 'A'},
            {'key': 'B', 'text': 'its protective surroundings', 'value': 'B'},
            {'key': 'C', 'text': 'its religious implications', 'value': 'C'},
            {'key': 'D', 'text': 'its existing infrastructure', 'value': 'D'}
        ],
        'answer': 'A',
        'explanation': '［精准定位］根据Mauna Kea定位至第二段。①句直陈莫纳克亚山为全球天文学研究重地，②句进而说明原因：气候干燥、没有光污染、高出空气对流层且空气稀薄；由此可知，莫纳克亚山是因其自身优越的地理环境成为绝佳天文观测台址，［A］正确。\n［命题解密］正确项［A］是对②句其地理环境优势的概括归纳。\n［B］利用②句“空气稀薄、位于对流层之上”制造干扰，认为其具有“保护性周边环境”，但莫纳克亚山周边为无边海洋，并未有起保护作用的周边环境，且②句所述条件为该山本身特性，并非“周围事物赋予其的保护特征”。［C］利用③句Sacred Mount和has deep religious meaning干扰，但这是夏威夷原住民视其为圣地、反对修建TMT的原因，并非天文学界选择其为天文台址的原因。［D］将②句“十几座巨型望远镜已立于该山”偷换为“现有的完备基础设施”。'
    },
    (2017, 'ky1', 28): {
        'stem': 'The construction of the TMT is opposed by some locals partly because',
        'options': [
            {'key': 'A', 'text': 'it may risk ruining their intellectual life', 'value': 'A'},
            {'key': 'B', 'text': 'it reminds them of a humiliating history', 'value': 'B'},
            {'key': 'C', 'text': 'their culture will lose a chance of revival', 'value': 'C'},
            {'key': 'D', 'text': 'they fear losing control of Mauna Kea', 'value': 'D'}
        ],
        'answer': 'B',
        'explanation': '［精准定位］第三段①句以“抗议者认为在莫纳克亚山顶修建望远镜不仅亵渎圣山、而且也是对夏威夷主权的侵犯”引出反对原因。②③句进而说明抗议者眼中“侵犯夏威夷主权”具体含义：强迫夏威夷放弃其主权并被美国吞并，给其带来屈辱历史，而建立TMT不仅会加剧历史苦痛、而且勾起痛苦回忆；由这些信息可知，建立TMT勾起当地人屈辱历史的回忆是其反对修建TMT的原因之一，［B］正确。\n［命题解密］正确项［B］是对第三段②③句内容的合理概括，其中a humiliating history对应③句a painful history of ... annexation。\n［A］将第三段①句“夏威夷原住民正在为追求自身文化、历史以及知性生活的复兴而斗争”曲解为“TMT的修建会毁掉其知性生活”。［C］颠倒第三段①句逻辑，文中指出原住民为了复兴自身文化而反对修建TMT，并非修建TMT使其文化丧失复兴机会。［D］过度推断，当地人反对修建TMT旨在保护圣山和唤醒夏威夷主权意识，并不存在“惧怕失去莫纳克亚山控制权”这一担忧。'
    },
    (2017, 'ky1', 29): {
        'stem': "It can be inferred from Paragraph 5 that progress in today's astronomy",
        'options': [
            {'key': 'A', 'text': 'is fulfilling the dreams of ancient Hawaiians', 'value': 'A'},
            {'key': 'B', 'text': 'helps spread Hawaiian culture across the world', 'value': 'B'},
            {'key': 'C', 'text': 'may uncover the origin of Hawaiian culture', 'value': 'C'},
            {'key': 'D', 'text': "will eventually soften Hawaiians' hostility", 'value': 'D'}
        ],
        'answer': 'A',
        'explanation': '［精准定位］第五段①句以“科学也有其文化历史”指出天文学和夏威夷文化具有相通之处，②③④句具体说明相通之处：探索人（天文学家&古代夏威夷人）好奇心相同、都在试图解答相同人类本源问题（我们是谁？从哪里来？到哪里去？）、文化使命一致（了解自己以及祖先的真正家园）；末句进而借引言指明今日天文学对古代夏威夷文化的继承发展：古代夏威夷人敢于在太平洋上开拓探索，当代天文学家正继承这一精神开拓星空；由这些信息可知，今日天文学的发展正在实现古代夏威夷人的梦想，［A］正确。\n［命题解密］正确项［A］是对第五段⑤句引言中“两代人都在开拓探索（voyage）”深层内涵的合理引申推断。\n［B］过度推导，天文学探索的是“人类重大起源问题”，并非致力于“传播夏威夷文化”。［C］将③句“追寻人类共同家园、探求人类本源问题”偷换为“探求夏威夷文化起源”。［D］主观臆断，文中末两段着力阐述天文学与夏威夷文化的相通之处，但并未提及“这是否会缓和当地人敌意”。'
    },
    (2017, 'ky1', 30): {
        'stem': "The author's attitude toward choosing Mauna Kea as the TMT site is one of",
        'options': [
            {'key': 'A', 'text': 'severe criticism', 'value': 'A'},
            {'key': 'B', 'text': 'passive acceptance', 'value': 'B'},
            {'key': 'C', 'text': 'slight hesitancy', 'value': 'C'},
            {'key': 'D', 'text': 'full approval', 'value': 'D'}
        ],
        'answer': 'D',
        'explanation': '［精准定位］第一段以Sadly引出天文学TMT项目进展不顺，体现作者的同情遗憾之意；第五段③④句指出抗议者忽视了“天文学家和夏威夷文化都在探索相同重大问题”这一现实，体现作者支持天文探索事业的立场：天文学与夏威夷文化本源相通，并不存在难以化解的矛盾，天文事业的进步有助于解答夏威夷文化所探索的问题;末段④句指出完全有理由欢迎任何人来莫纳克亚山探索星空，明确作者态度：完全支持天文学家。［D］正确。\n［命题解密］正确项［D］是对文中 Sadly、ignore the reality、There is no reason why everyone cannot be welcomed on Mauna Kea等信息所传递出的作者对TMT选址于莫纳克亚山态度的正确解读。'
    },
    # 2017 ky1 Q35
    (2017, 'ky1', 35): {
        'stem': 'Which of the following is the best title for the text ?',
        'options': [
            {'key': 'A', 'text': 'High GDP But Inadequate Well-being, a UK Lesson', 'value': 'A'},
            {'key': 'B', 'text': 'GDP Figures, a Window on Global Economic Health', 'value': 'B'},
            {'key': 'C', 'text': 'Robert F. Kennedy, a Terminator of GDP', 'value': 'C'},
            {'key': 'D', 'text': "Brexit, the UK's Gateway to Well-being", 'value': 'D'}
        ],
        'answer': 'A',
        'explanation': '［精准定位］文章首两段质疑GDP的观点，并聚焦“英国脱欧事件”予以强调；第三至五段则以近期研究发现“英国及其他主要经济体未能将高GDP转化为民生福祉”暗示高GDP并不等同于国民幸福；第六、七段则明确指出“GDP无法衡量环境质量、教育成果等关乎民生的重要因素，因此政策制定者不能一味忧心GDP,而应努力提升社会福利”。可见，全文以“英国脱欧”为反例，指出高GDP并非等同于幸福感，不足以衡量国家发展，［A］正确。\n［命题解密］正确项［A］既锁定了文章核心论点“GDP在衡量民生方面存在局限性（High GDP But Inadequate Well-being）",又明确了文章切入点：“以英国为反例，给各国以警醒（a UK lesson）”。\n［B］将文章观点“GDP不足以衡量国家经济活动”篡改为与之完全相反的“GDP是全球经济健康之窗”。［C］肯尼迪只是GDP的批判者，并非终结者，无力概括全篇。［D］将文中信息“英国人选择脱欧在一定程度上是不满幸福感的持续下降”篡改夸大为“脱欧是英国实现幸福之路”。'
    },
    # 2020 ky1 Text 3 (Q31-Q35)
    (2020, 'ky1', 31): {
        'stem': 'The author believes that the bills sponsored by Lewis and Haddad will',
        'options': [
            {'key': 'A', 'text': 'help little to reduce gender bias', 'value': 'A'},
            {'key': 'B', 'text': 'pose a threat to the state government', 'value': 'B'},
            {'key': 'C', 'text': 'raise women\'s position in politics', 'value': 'C'},
            {'key': 'D', 'text': 'greatly broaden career options', 'value': 'D'}
        ],
        'answer': 'A',
        'explanation': '［精准定位］首段提到进步人士通常支持旨在促进平等的法案，随后第二段首句指出两位议员在马萨诸塞州发起的议案（提议所有州委员会和顾问委员会中女性人数至少占50%）便属于此类法案，但紧接着在②句明确作者态度：但此类硬性规定几乎无助于促进真正的平等。由此可见，作者认为该法案对促进性别平等收效甚微，［A］正确。\n［命题解密］正确项［A］是对第二段②句 do little to promote genuine equality 的同义改写，其中 help little to reduce 对应 do little to promote，gender bias 与 equality 构成反义转述。\n［B］pose a threat无中生有，第二段提及各州委员会，但并未提及法案对州政府构成威胁。［C］与第二段②句“法案无助于促进平等”相悖。［D］broaden career options偏离文章讨论重点，法案针对的是“委员会任命”，并非普通大众的职业选择。'
    },
    (2020, 'ky1', 32): {
        'stem': 'Which of the following is true of the California measure?',
        'options': [
            {'key': 'A', 'text': 'It has irritated private business owners.', 'value': 'A'},
            {'key': 'B', 'text': 'It is welcomed by the Supreme Court.', 'value': 'B'},
            {'key': 'C', 'text': 'It may go against the Constitution.', 'value': 'C'},
            {'key': 'D', 'text': 'It will settle the prior controversies.', 'value': 'D'}
        ],
        'answer': 'C',
        'explanation': '［精准定位］第四段①句指出加州已通过一项具有法律约束力的类似法案，随后②句指出该法案可能招致的严重后果：极可能被判违宪。由此可见，加州法案很可能违反宪法，［C］正确。\n［命题解密］正确项［C］中 may go against the Constitution 是对第四段②句 is likely to be struck down on constitutional grounds 的同义改写。\n［A］利用第四段①句 publicly held corporations 干扰，但文中并未提及私企老板的愤怒情绪。［B］与第四段②句“可能被最高法院裁定违宪而废止”的走向完全相反。［D］settle the prior controversies捏造事实，法案反而引发了新的合宪性争议。'
    },
    (2020, 'ky1', 33): {
        'stem': 'The author mentions the study by Catalyst to illustrate',
        'options': [
            {'key': 'A', 'text': 'the harm from arbitrary board decision', 'value': 'A'},
            {'key': 'B', 'text': 'the importance of constitutional guarantees', 'value': 'B'},
            {'key': 'C', 'text': 'the pressure on women in global corporations', 'value': 'C'},
            {'key': 'D', 'text': 'the needlessness of government interventions', 'value': 'D'}
        ],
        'answer': 'D',
        'explanation': '［精准定位］第五段首句先指出政府强制措施根本没必要，随后②③句援引非营利研究机构Catalyst的调查发现（即便没有政府干预，财富500强企业中女性董事比例也已实现显著上升）作为论据；由此可见，作者引用该机构的调查旨在说明：无需政府干涉，企业董事会女性比例也在自发上升，政府干预实属多余，［D］正确。\n［命题解密］正确项［D］是对第五段①句 Government intervention is not needed 以及②③句数据的准确概括，needlessness 对应 not needed。\n［A］arbitrary board decision脱离上下文逻辑，该研究讨论的是董事会女性比例自然增长，无关任意决策的危害。［B］属于第四段话题，第五段已转向探讨干预的必要性。［C］pressure on women偏离调查核心内容。'
    },
    (2020, 'ky1', 34): {
        'stem': 'Norway\'s adoption of a nationwide corporate gender quota has led to',
        'options': [
            {'key': 'A', 'text': 'the underestimation of elite women\'s role', 'value': 'A'},
            {'key': 'B', 'text': 'the objection to female participation on boards', 'value': 'B'},
            {'key': 'C', 'text': 'the entry of unqualified candidates into the board', 'value': 'C'},
            {'key': 'D', 'text': 'the growing tension between labour and management', 'value': 'D'}
        ],
        'answer': 'C',
        'explanation': '［精准定位］第七段引出挪威全国性企业性别配额的案例，随后第八段指出研究发现：由于硬性配额要求企业必须在短时间内任命大量女性董事，导致大批缺乏管理经验、资历不足的女性进入董事会，对企业业绩造成不利影响。由此可见，挪威配额制直接导致不合格人选进入了董事会，［C］正确。\n［命题解密］正确项［C］是对第八段 less-experienced women were appointed to boards 的归纳总结，unqualified candidates 对应 less-experienced candidates。\n［A］与事实相反，政策过度拔高了少数精英女性的职位。［B］objection to female participation曲解文意，各界反对的是硬性配额机制本身，而非女性参评。［D］labour and management劳资紧张关系属于杜撰内容。'
    },
    (2020, 'ky1', 35): {
        'stem': 'Which of the following can be inferred from the text?',
        'options': [
            {'key': 'A', 'text': 'Women\'s need in employment should be considered.', 'value': 'A'},
            {'key': 'B', 'text': 'Feasibility should be a prime concern in policymaking.', 'value': 'B'},
            {'key': 'C', 'text': 'Everyone should try hard to promote social justice.', 'value': 'C'},
            {'key': 'D', 'text': 'Major social issues should be the focus of legislation.', 'value': 'D'}
        ],
        'answer': 'B',
        'explanation': '［精准定位］文章开篇三段提出观点：多样性指令等政策对促进公平无济于事，反而会强化特权。第四至九段指出此类政策的不可行：可能被判违宪；不但没有必要，甚至很可能带来多种不良后果。末段重申此类政策的无效性。可见，本文重在指出此类政策不可行，建议政策制定者考量其可行性，［B］正确。\n［命题解密］正确项为全文主旨的换角度表述:此类政策无可行性=政策制定者在制定政策时应首要考量其可行性（Feasibility should be a prime concern in policymaking）。\n［A］偏离文章关注对象：文中关注的是"董事会性别配额制政策"，并非"普通女性就业需求"。［C］偏离话题：本文讨论的是"政策有效性"，并非“大众应如何推进社会正义”。［D］与作者立场相反，作者认为硬性立法往往得不偿失。'
    }
}

exams_dir = 'public/data/exams'
total_questions_updated = 0
total_files_touched = 0

for filepath in sorted(glob.glob(os.path.join(exams_dir, '*.json'))):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    exam = data.get('exam', {})
    yr = exam.get('year')
    cat = exam.get('category_id')
    
    file_modified = False
    
    # 1. Total score / pass score sanity calibration
    if yr and yr < 2005 and cat == 'ky1':
        if exam.get('total_score') != 50:
            exam['total_score'] = 50
            file_modified = True
        if exam.get('pass_score') != 30:
            exam['pass_score'] = 30
            file_modified = True
            
    for q in data.get('questions', []):
        so = q.get('sort_order')
        key = (yr, cat, so)
        
        # Check detailed fixes
        if key in DETAILED_QUESTION_FIXES:
            fix = DETAILED_QUESTION_FIXES[key]
            if 'stem' in fix and q.get('stem') != fix['stem']:
                q['stem'] = fix['stem']
                file_modified = True
            if 'options' in fix:
                q['options'] = fix['options']
                file_modified = True
            if 'answer' in fix:
                q['answer'] = fix['answer']
                q['correct_answer'] = fix['answer']
                file_modified = True
            if 'explanation' in fix:
                q['explanation'] = fix['explanation']
                file_modified = True
            total_questions_updated += 1
            print(f"[{yr} {cat} Q{so}] Detailed calibration applied (Stem, Options, Answer={fix.get('answer')})")
            
        # Check answer fixes
        elif key in ANSWER_FIXES:
            new_ans = ANSWER_FIXES[key]
            old_ans = q.get('answer')
            if old_ans != new_ans or q.get('correct_answer') != new_ans:
                q['answer'] = new_ans
                q['correct_answer'] = new_ans
                file_modified = True
                total_questions_updated += 1
                print(f"[{yr} {cat} Q{so}] Answer calibrated: {old_ans} -> {new_ans}")
                
        # Always enforce answer == correct_answer integrity
        if q.get('answer') != q.get('correct_answer'):
            q['correct_answer'] = q.get('answer')
            file_modified = True
            
    if file_modified:
        total_files_touched += 1
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n Master Forensic Calibration Completed!")
print(f"Total files touched: {total_files_touched}")
print(f"Total questions calibrated: {total_questions_updated}")
