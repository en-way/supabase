import json
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def calibrate_2019():
    path = 'public/data/exams/5bcba462-0a1e-59b2-9fcb-c171d242db3b.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for q in data['questions']:
        qnum = q.get('sort_order')
        if qnum == 31:
            q['explanation'] = (
                "［精准定位］由题干关键词Mary Shelley's novel Frankenstein虽可直接定位至首段，但由is mentioned because it即可推断此题考查写作目的，"
                "故应结合文章话题及下文内容予以解答。首段以科幻小说《弗兰肯斯坦》出版200周年开篇，称赞著作者极有远见，在书中预言了未来（200年后的今天）"
                "技术将带来的诸多道德问题，浏览下文发现只有篇末复现作品相关词Frankenstein，而AI、ethical/ethics却贯穿全篇。由此推知，文章关注点并非《弗兰肯斯坦》本身，"
                "该小说只是作为开篇引子用以引出本文核心话题“与AI相关的伦理道德问题”，也即，文章提及《弗兰肯斯坦》是因为书中预言了 200年后的今天新技术（AI）所引发的道德伦理问题，［C］正确。\n\n"
                "［命题解密］正确项［C］恰当解读了小说重大意义foreshadow many ethical questions to be raised by technologies yet to come 与下文复现关键词 AI, ethical/ethics, issues/questions 之间“引子-正题”关联。\n\n"
                "［A］中fascinate源自第三段②句，但原文意在说明“人类痴迷于某种'机器人'概念”，选项内容“全球AI科学家痴迷于《弗兰肯斯坦》”文中并未提及。\n"
                "［B］由开篇句所涉信息“《弗兰肯斯坦》出版200周年”过度推出“该小说200年来一直受欢迎”，但下文并未论及小说的受欢迎度，故选项偏离文章话题，并非小说被提及的原因。\n"
                "［D］中ethical controversies源自首段末句中ethical questions，但选项将引发伦理问题的主体由“新技术”偷换为“小说《弗兰肯斯坦》”。\n\n"
                "［技巧总结］本题就开篇引子（事例、故事、名人名言等）设置写作目的题。解题思路为：一、首先明确引子的作用：激发读者兴趣，为引入正题服务；二、大体锁定全文主述话题词：速览下文抓取与引子内容有关联的高频复现词；三、分析选项：“能体现引子本身所涉内容”且“能和下文内容顺接（或反映全文主述话题）”的选项是正确项，“与引子所涉内容相悖/无关”或“无法与下文内容建立有效关联（偏离全文主述话题）”的通常是干扰项。如本题，［A］、［B］实际均囿于小说本身，而未与全文多次反复出现的AI、ethical/ethics、questions/issues/problems相关联，故均予以排除。"
            )
            modified = True
        elif qnum == 32:
            q['explanation'] = (
                "［精准定位］由题干关键词David Eagleman可直接定位至第四段。该段通过直接引用、间接引用两种方式指出伊格曼观点：人类思维方式（文中又指“意识”）极其复杂、难于理解，更甭提复制（思维方式/意识）。换言之，人类目前对意识的认识还十分有限、尚且无法复制意识。［D］正确。\n\n"
                "［命题解密］题干+正确项是对第四段①句的同义改写：题干中consciousness对应how people think，［D］项同义改写 far too complex to be understood, let alone reproduced。\n\n"
                "［A］利用第四段②句中explaining what... and how...设障，却忽略其前否定表达there are no good theories，从而将原文no theories explaining...“没有理论能够解释意识、更甭提去制造复制意识的机器（即'人工智能'）”曲解为helps explain“有助解释人工智能”。\n"
                "［B］中robot making虽与第四段段末build a machine同义，但原文意在指出我们目前对意识的认识“阻碍（how you could ever）”，而非“误导（misleading）”机器人的制造。\n"
                "［C］虽复现第三段末popular sci-fi TV series，但原文并未提及“我们目前对意识的认识”与热门科幻剧的关系，而且该处也并非伊格曼的观点。\n\n"
                "［技巧总结］人物观点题的解题关键是把握人物观点表达中的情感色彩表达词以及特定特殊句式。如本题，定位段中far too complex to be understood（强调否定意义的too... to...“太……而不能……”结构）、let alone reproduced（常用在含否定意味的句子后表示进一步否定的let alone“更不要谈”结构）、no good theories explaining（绝对表达 no“没有”）、how you could ever...（反问表达“你怎么可能……？”）等均透露出David Eagleman对人类理解意识以及机器复制意识（即人工智能）的否定态度，借此可确定相关题目的基调定是“负向（局限、不能）”，而非“正向（有助、启示）”，对比选项，唯有［D］项符合这一主基调。"
            )
            modified = True
        elif qnum == 33:
            q['explanation'] = (
                "［精准定位］根据题干关键词the ethical issues brought by autonomous vehicles定位至第五段。该段①句概述指出AI相关伦理问题业已出现，②至⑥句进而以自动驾驶汽车引发的伦理问题予以说明。②句首先指出自动驾驶汽车的投入使用带来了棘手的伦理问题，③至⑥句以“AI（自动驾驶汽车）与人类驾驶员的差距”解释其棘手的伦理问题：人类驾驶员的决策过程十分短暂且极其复杂（③④句）；而目前的AI技术不太成熟：AI眼力远不及人类，且编程上也很难穷举所有驾驶情景（⑤⑥句）。由此可知，我们目前仍无法解决自动驾驶汽车带来的伦理问题，［B］正确。\n\n"
                "［命题解密］正确项［B］是对第五段②句 thorny ethical questions、⑤句 not nearly as sophisticated、⑥句 a difficult programming problem 的综合概括和推断。\n\n"
                "［A］是对末句中a difficult programming problem“一个有难度的编程问题”的近乎绝对/全盘否定化。\n"
                "［C］、［D］涉及大众对伦理问题解决办法的“关注”、“好奇”，但文中并不涉及大众的关注和好奇。\n\n"
                "［技巧总结］本题考查事实细节，解题时应先确定解题范围，再注意对比选项与原文。题干autonomous vehicles在第五段②句中复现，由该句中表示例证的for example可确定解题范围为该段②至⑥句；四个选项涉及“能否解决（hardly... found, beyond... capacity）”与“大众反响（public concern, much curiosity）”两大方向，②至⑥句分析现状“自动驾驶汽车带来的伦理问题相当棘手：目前的AI与人类驾驶员相比仍有很大缺陷（split-second, complex, not nearly as sophisticated, difficult programming problem）”，并不涉及大众看法，先排除［C］、［D］；剩余两项中，［A］过度推导，几乎全盘否定了解决问题的可能，过于绝对，［B］客观描述问题解决的现状，为正确项。"
            )
            modified = True
        elif qnum == 34:
            q['stem'] = "The author's attitude toward Google's pledges is one of ________."
            q['options'] = [
                {"key": "A", "text": "affirmation", "value": "A"},
                {"key": "B", "text": "skepticism", "value": "B"},
                {"key": "C", "text": "contempt", "value": "C"},
                {"key": "D", "text": "respect", "value": "D"}
            ]
            q['correct_answer'] = "A"
            q['answer'] = "A"
            q['explanation'] = (
                "［精准定位］由题干关键词Google's pledges初步定位至第七段，但由The author's attitude可知本题考查作者态度，故应注意上下文相关内容。"
                "第七段具体介绍了谷歌有关AI的相关承诺，第八段①句作者随即做出点评：虽然谷歌的声明含混笼统，但它代表了一个起点。"
                "由此可知，作者认为谷歌声明虽有瑕疵，但总体值得肯定，［A］正确。\n\n"
                "［命题解密］正确项［A］是对第八段①句 While the statement is vague, it represents one starting point中“让步-转折”逻辑所含作者态度的正确解读。\n\n"
                "［B］skepticism为负向态度词，由第八段首句vague臆断而来，却忽视句中语义重心（While预示主句为语义重点）represents one starting point所传递的肯定语义色彩。\n"
                "［C］contempt（意为 the feeling that sb/sth is without value and deserves no respect at all“蔑视；轻蔑；鄙视”）是极端负向情感词，明显与第八段represents one starting point所传递的肯定态度相悖。\n"
                "［D］respect（语用色彩为 used for showing that you admire or strongly approve of someone or something“对……的赞赏或强烈支持”）虽是正向情感词，但程度过重，忽略其前让步从句中vague所传递的否定语义色彩。\n\n"
                "［技巧总结］本题考查作者态度，解题关键在于找准并理解体现作者态度的词（组）或表达。题干Google's pledges为作者评价对象，可据此初步定位具体介绍谷歌承诺的第七段，作者态度有可能出现在该段前后：第六段介绍各国政府的举措，排除；第八段①句中作者先让步（While）指出谷歌声明的缺点“含混笼统”，随后肯定其优点“是一个起点”，由此可知作者对谷歌承诺总体持肯定态度。浏览四个选项，先排除带有明显负面色彩的［B］、［C］；剩余两项中虽均为正面评价，但只有［A］与作者客观肯定的态度相符，［D］有夸大赞誉之嫌。"
            )
            modified = True
        elif qnum == 35:
            q['stem'] = "Which of the following would be the best title for the text?"
            opts = q.get('options')
            if isinstance(opts, list):
                for o in opts:
                    if o.get('key') == 'A':
                        o['text'] = "AI's Future: In the Hands of Tech Giants"
            elif isinstance(opts, dict):
                opts['A'] = "AI's Future: In the Hands of Tech Giants"
            q['explanation'] = (
                "［精准定位］文章先以玛丽•雪莱巨著《弗兰肯斯坦》为引，提出全文话题：技术引发的伦理道德问题；尔后铺垫当前AI技术的发展现状：尚且难以复制人类意识；"
                "随后指出当前AI技术已然引发伦理问题，并对各国政府、企业的相关具体措施予以了肯定；最后总结强调AI必须反映人类最高价值观才能真正造福人类（言外之意：人类必须将自身价值观灌输给AI）。"
                "综上可知，本文传达的主旨是：虽然目前的AI无法复制复杂的人类意识（不具备复杂的道德意识），但为了应对日益凸显的AI伦理问题，人类必须将自身道德观念灌输给AI，让其具备“道德意识”，"
                "［C］为最恰当的标题，其中conscience意为the part of your mind that tells you whether your actions are right or wrong“良心，良知（心智的一部分）”。\n\n"
                "［命题解密］正确项［C］是对文中两大意群（一、当前AI尚不能复制极为复杂的人类意识［包括道德伦理意识］；二、当前AI已然引发诸多关键性伦理问题，要解决这些伦理问题唯有赋予AI以最高人类价值观）的高度概括。\n\n"
                "［A］中Tech Giants对应第六、七段提及的mega-corporations、Google，无法概括全文，且文中并未明确指出AI的未来掌握在科技巨擘手中。\n"
                "［B］以开篇引子《弗兰肯斯坦》为标题，但它并非文章论述焦点。\n"
                "［D］近义复现末段out-of-control monster，但选项只提及“问题（AI有可能失控）”，而未触及文章后半部分的语义重点“针对问题给出的建议/出路（要让AI反映人类价值观）”。\n\n"
                "［技巧总结］本题考查文章标题，要求考生总体把握文章，梳理全文脉络时需着重把握文中两个关键词consciousness与values的语义逻辑关系“人类意识包含多个方面，价值观念/道德意识是其中一方面”，"
                "由此才能深层理解本文中的让步转折行文逻辑：AI虽无法复制包括道德意识在内的人类意识（第二至四段），但为了应对日益凸显的AI伦理问题人类必须将其道德意识灌输给AI（第五至末段）；"
                "［C］既抓住全文的核心话题，也高度概括了第二至末段的让步转折行文脉络。［A］、［B］、［D］或仅涵盖文章部分信息或偏离论述焦点，均予以排除。"
            )
            modified = True

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Calibrated 2019 ky1 successfully!")

def calibrate_2016():
    path = 'public/data/exams/666cdb4e-7fd3-53c2-8c91-a12fa3160c09.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for q in data['questions']:
        qnum = q.get('sort_order')
        if qnum == 26:
            q['explanation'] = (
                "［精准定位］第一段③句明确指出：英国人很重视乡村，认为“乡村”与王室、莎士比亚、NHS 一样，令他们引以为傲，但是这种民意得到的政治支持却非常有限。"
                "换言之，英国民众对乡村的观点没有在政治中得到很好的体现。［A］正确。\n\n"
                "［命题解密］正确项［A］是对第一段③句has limited political support的合理解读。\n\n"
                "［B］利用③句royal family、support等词捏造出“受到王室的全面支持”，但文中并未介绍王室的态度。"
                "［C］利用③句Shakespeare捏造关联，但文中用其旨在体现“人们对countryside的重视：将其与Shakespeare相提并论”，并未介绍英国民众乡村观的起始时间。"
                "［D］利用③句NHS捏造关联，由makes them proudest捏造出“带给NHS许多好处”，但同样文中提到NHS旨在突出人们对乡村的重视（将其与NHS等并列，视为“国之四宝”），二者并无直接关联。\n\n"
                "［技巧总结］本题直接考点为第一段③句（长难句），实际全面考查对第一段信息的分析能力。正确解答此类试题需要考生：1）会读题，抓住各选项关键信息，锁定答题范围；2）细读文，借助语法知识理清句子结构，由逻辑关联词确定各语义成分功能，明确句子语义重点以及各提及对象之间关系。\n"
                "具体来看，首先读题：根据四个选项关键词politics、royal family、Shakespearean age、NHS可锁定本题答题范围在③句。随后梳理理清句子结构：While构成句内转折，语义重点在后：转折之前Britons rate the countryside alongside... as...（人们认为乡村与 一样，都是 ）为题干所述内容（即民众对乡村的看法），其中the countryside与the royal family、Shakespeare、NHS为并列平行结构，四者之间并无直接语义逻辑关联；this（指代前半句）has limited political support为语义重点。最后于语义重点中比对选项：唯有［A］体现作者强调内容，故正确；［B］、［C］、［D］均以并列平行结构the royal family、Shakespeare、NHS强生关联，故错误。"
            )
            modified = True
        elif qnum == 27:
            q['stem'] = "According to Paragraph 2, the achievements of the National Trust are now being ________."
            q['explanation'] = (
                "［精准定位］第二段④句指出：现在他们（即英国当局）不仅不再建设乡村，甚至逐年用混凝土（即城市建设）吞噬乡村（土地）。"
                "这很明显与①②句所述国民托管组织宗旨（永葆自然美之地）背道而驰，损坏了③句所述该组织所取得的成果（使得国家公园和绿化带得以创建）。故［D］正确。\n\n"
                "［命题解密］正确项［D］是对④句中第二分句的同义概括，其中gradually对应every year, destroyed对应consumes。\n\n"
                "［A］因④句They don't make countryside any more and... consumes more of it 而来，但句中They 实指英国当局，而非组织本身，组织所取得的成就是“被破坏，逐渐消失”而非“被蒙上阴影，黯然失色”。"
                "［B］根据⑤句constant guardianship（持续保护）制造出properly protected（恰当保护），却将文意“作者建议乡村需要持续保护”篡改为“作者描述组织目前的成果维护情况”。"
                "［C］源自④句concrete一词，但此处该词为名词“混凝土”（混凝土吞噬了该组织的成果），并非动词“巩固，加强”（该组织的成果正被加强）。\n\n"
                "［技巧总结］本题就涉及今昔变化以及多个提及对象的段落（第二段）命制事实概括题。解答此类题时需要考生：1）根据原文时态或时间标记词（no more, not any more, no longer）等理解事实细节、概括得出今昔变化；2）借助作者评论性话语把握整体趋势。\n"
                "如本题，首先了解事实细节：根据A century ago可推知国民托管组织的创建初衷“旨在永葆自然美之地”，根据later可推知该组织的成就“使得诸多国家公园和绿化带得以创建”，根据一般现在时态及every year可推知英国住建当局不再建设乡村，相反每年混凝土还吞噬乡村。随后概括今昔对比得出：国民托管组织的成果正逐年被破坏。最后结合末句作者评注（呼吁）“乡村需要持续保护”，可确定［D］为答案。"
            )
            modified = True
        elif qnum == 28:
            q['stem'] = "Which of the following can be inferred from Paragraph 3?"
            q['explanation'] = (
                "［精准定位］根据第三段⑥⑦句可知，Ukip是下一届选举中唯一支持乡村保护的政党，且⑥句中“嗅到了机会”暗示UKip将从中获利，即为其下一届选举获得民众支持。由此可见，［C］属于合理推测，故正确。\n\n"
                "［命题解密］正确项［C］是对第三段⑥⑦句的合理推断，其中may gain照应chance。\n\n"
                "［A］将第三段④句councils oppose development（当地议会反对开发）错误说成Labour... opposing development（工党反对开发），而实际上工党反对当地议会、支持开发。"
                "［B］错误推导②句：“保守党会放弃'计划外'建筑”与原文“保守党批准在当地居民可能反对的地方进行'计划外'建设”方向相反。"
                "［D］干扰源自⑤句silent一词，但该词指自由民主党在“保护乡村”问题上保持沉默，并非指该党正失去政治影响力。\n\n"
                "［技巧总结］本段就涉及多方观点及多个事实的第三段命制事实细节题。解答此类题型时需结合“定位法”与“排除法”：1）先根据各选项关键词定位至原文；2）然后将选项内容与原文逐一进行细致对比，比对中需深挖原文信息；3）错误项一般是添加信息或篡改原文内容，正确项有可能是原文信息的言外之意。\n"
                "具体来看，首先根据选项关键词Labour、The Conservatives、Ukip、The Liberal Democrats分别定位至文中④句、②句、⑥⑦句和⑤句。接着仔细比对发现：［A］opposing development与④句gives rural development priority over conservation意义相反，且under attack属于添加信息；［B］may abandon与②句authorizing不符，且无从推知；［C］may gain大致同⑥句chance（机会）之意，且⑥⑦句确实指出Ukip支持保护乡村（sided with those pleading for...），其保护乡村运动使得其他党胆战心惊，由此可推测该党可能因其支持民众乡村保护而在下一届选举中受益，故初步断定其正确；［D］losing political influence从⑤句中难以推断，证实［C］正确。"
            )
            modified = True
        elif qnum == 29:
            q['stem'] = "The author holds that George Osborne's preference ________."
            q['explanation'] = (
                "［精准定位］第五段⑥⑦句指出：乡村得到了发展且将一直发展下去，边界及特点被尊重的乡村发展得最好；⑧⑨句批判奥斯本偏好“支持在乡村新建而不是在城市翻新或改造，支持在城郊修建购物中心而非在城中建商业街”：没有破坏城市保护区，却破坏了乡村保护区。可见［A］正确。\n\n"
                "［命题解密］题干+正确项［A］是第五段奥斯本倾向favours... against...及作者对其点评a biased one, ruin rural ones 的合理推断。\n\n"
                "［B］将第五段①句隐含的“强调解决住房危机必要性”的主体由“游说团体(lobby)”偷换成“奥斯本(Osborne)”。"
                "［C］将第五段③句“奥斯本在游说团体的压力下支持在乡村建新房子(Under lobby pressure, George Osborne...)”理解为与之相反的“奥斯本对抗游说团体的立场坚定(firm stand against lobby pressure)”。"
                "［D］将第五段③④句 favours rural new-build against urban..., favours out-of-town shopping sites against high streets所传递的“奥斯本不重视乡村保护，对乡村地区持偏见”反向曲解为“奥斯本对城市地区有强烈偏见(a strong prejudice against urban areas)”。\n\n"
                "［技巧总结］解答本题的关键是借助三个取舍表达(③句favours... against；④句favours... against；⑤句not a... but a...)，一个反问质疑(⑧⑨句do not ruin... Why ruin...?)、以及诸多形容词副词(biased, always等)理解③至⑨句所述奥斯本做法及作者对其态度。具体来看，可借助③④句取舍结构明确奥斯本做法；借助⑤句取舍、⑧⑨句反问、以及形容词副词，理解作者对奥斯本倾向(不去破坏城市保护区，却去破坏乡村保护区)的批驳，从而确定［A］正确，其他三项均与原文相悖，可排除。\n"
                "附捷径1：细读选项发现［A］、［D］实为对立选项，答案有可能在其中之一，而［D］很明显与文意不符，故［A］正确。附捷径2：文章主要讲述乡村保护未得到政府足够重视，题干中Osborne实际代表政府，选项中唯有［A］跟countryside搭边，且指出了 Osborne对乡村的忽视，故正确。"
            )
            modified = True
        elif qnum == 30:
            q['stem'] = "In the last paragraph, the author shows his appreciation of ________."
            q['explanation'] = (
                "［精准定位］第六段③句指岀半个世纪的城乡规划使得拥挤度位居欧洲第二的英国拥有令人艳羡的乡村协调性以及低密度城市居住条件，很明显作者对英国城乡规划表示欣赏。［C］正确。\n\n"
                "［命题解密］题干 + 正确项［C］是对第六段③句 town and country planning has enabled... enviable rural coherence... low-density urban living 的合理推断。\n\n"
                "［A］利用②句所述“英国是欧洲最拥挤的国家(Britain is Europe's most crowded country)”制造出“英国人口规模(the size of population)”的干扰，但原文中作者并未对英国人口大小表示欣赏。"
                "［B］“英国令人羡慕的城市生活方式(the enviable urban lifestyle in Britain)”干扰来自③句“令人羡慕的乡村协调性(an enviable rural coherence)”，但作者谈到乡村协调性是为了表达城乡规划的成功。"
                "［D］“当今英国政治生活(the political life in today's Britain)”干扰来自⑤句“政治光谱上的左派和右派(the left and right of the political spectrum)”，但作者意指团结政治力量保护乡村，而非表达对政治生活的欣赏。\n\n"
                "［技巧总结］作者于末段针对全文所述问题提出建议并表明态度，且提及正反两个事例，命题人于此设置态度细节题旨在考查对事实信息的分辨以及对全文主旨的把握。解题关键在于：1)理解作者的建议(should be..., not...)、呼吁(rather than... should...)；2)理解文中两个事例(Britain VS Southern Portugal, Spain or Ireland)的正反关系；3)体味形容词副词(enviable, still permitting...)等传达的作者态度；4)意识到作者所赞同的必定与文章论述主题挂钩或相近，而不是生疏的细枝末节。\n"
                "具体来看，文章一直围绕乡村开发还是保护、城乡规划的问题而展开，［C］ the town-and-country planning in Britain最接近主题；且末段③④句提到了英国的城乡规划带来了令人羡慕的乡村和谐和低密度城市生活(enviable rural coherence, low-density urban living)，体现出作者的赏识，故［C］正确。"
            )
            modified = True

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Calibrated 2016 ky1 successfully!")

def calibrate_2018():
    path = 'public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for q in data['questions']:
        qnum = q.get('sort_order')
        expl = q.get('explanation', '')
        if qnum == 21:
            sec_idx = expl.find('［命题解密］')
            rest = expl[sec_idx:] if sec_idx != -1 else ""
            q['explanation'] = (
                "［精准定位］第二段②句指出，美国的工作中约一半处于被自动化的高风险，中产阶级尤其不堪负担。"
                "④句进一步指出，许多中产职业已经引起、或很快会引起机器人的兴趣。可见，受自动化威胁最大的是中产阶级工人，［D］正确。\n\n" + rest
            )
            modified = True
        elif qnum == 22:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 23:
            sec_idx = expl.find('［命题解密］')
            rest = expl[sec_idx:] if sec_idx != -1 else ""
            q['explanation'] = (
                "［精准定位］第四段①句指出，自动化时代应该反思教育。②句则指出，从小学到大学的所有课程都应该少强调事实记忆，多强调创新及复杂沟通能力。可见［A］正确。\n\n" + rest
            )
            modified = True
        elif qnum == 24:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 25:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 26:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 27:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 28:
            sec_idx = expl.find('［命题解密］')
            rest = expl[sec_idx:] if sec_idx != -1 else ""
            q['explanation'] = (
                "［精准定位］第三段②③④句介绍奈特基金会的调查结果，其中②句指出年轻人利用分布式信任来验证新闻，"
                "③句进而做出解释：他们交叉核对新闻来源、倾向于多角度分析的新闻资讯、尤其是对各种观点兼收并蓄的新闻资讯。由此可见，［B］正确。\n\n" + rest
            )
            modified = True
        elif qnum == 29:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 30:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 33:
            opts = q.get('options')
            if isinstance(opts, list):
                for o in opts:
                    if o.get('key') == 'C':
                        o['text'] = "making profits from patients' data is illegal"
            elif isinstance(opts, dict):
                opts['C'] = "making profits from patients' data is illegal"
            q['explanation'] = (
                "［精准定位］第二段末句指出作者对⑥句Ms Denham裁定依据（判NHS违法因为它才是数据拥有者，而DeepMind只是处理数据而已）的看法：不得要领（misses the point）：“让数据拥有价值的，是处理和集成它们，而不是掌控它们”，［D］正确。\n\n"
                "［命题解密］［D］是第二段末句 it is processing and aggregation... that gives the data value 的同义改写。\n\n"
                "［A］将第二段③句保护隐私的措施 all necessary permissions... and all unnecessary data...误当成作者观点，但⑤句中作者已明确指出“在此案中，隐私甚至不是最重要的（not even the most important）”。\n"
                "［B］从⑥句“NHS掌控数据，而DeepMind只处理数据”捏造出“NHS泄露数据，而DeepMind贩卖数据，前者比后者更恶劣”，与文意相去甚远。\n"
                "［C］是由第二段第⑥句“NHS掌控患者数据”杂糅第三段首句“问题是谁该从分析数据中获利（who should benefit from...）”而成，但作者在文中并未“指出谁/某事违法（illegal）”，他想表达的是“具有垄断性质的科技巨头从分析患者数据中获利，而不受监管限制（裁定只判NHS侵犯病人隐私权）”这一情况并不合理。\n\n"
                "［技巧总结］涉及多方观点/做法的段落常成为命题人关注的焦点。若就作者观点设题，则一般要求考生通过抓取语气词、关联词，尤其是表示转折、常常引出作者观点的but、yet、however等词来把握作者站位；要警惕命题人扭曲或直接利用他人观点命制干扰项。就本题而言，细读⑤句和⑦句转折词But后内容，从 not the only...，not even the most important 以及 misses the point 基本可判定作者对于 Denham裁定依据的不认同态度，从而排除［A］，而［C］illegal并非作者所能认定，最后根据⑦句作者的反对理由排除［B］，锁定正确答案［D］。"
            )
            modified = True
        elif qnum == 34:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 39:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 40:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Calibrated 2018 ky1 successfully!")

def calibrate_2020():
    path = 'public/data/exams/f56943c1-0ba8-58fe-b7d3-061352345067.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for q in data['questions']:
        qnum = q.get('sort_order')
        expl = q.get('explanation', '')
        if qnum == 21:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 22:
            sec_idx = expl.find('［命题解密］')
            rest = expl[sec_idx:] if sec_idx != -1 else ""
            q['explanation'] = (
                "［精准定位］本段①句指出，一些人认为该提议是英国失去申请“欧洲文化之都”资格后的自我安慰；"
                "②句指出英国正陷入无休止的自我庆祝之中。［B］项是对质疑者态度的合理概括。\n\n" + rest
            )
            modified = True
        elif qnum == 23:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 24:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 25:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 26:
            sec_idx = expl.find('［命题解密］')
            rest = expl[sec_idx:] if sec_idx != -1 else ""
            q['explanation'] = (
                "［精准定位］首段首句提出科学出版业一本万利（a licence to print money），②③句分别指出，科学文献的供稿与审稿皆为无偿进行，即科学出版业在“内容获取”方面投入的成本为零。可见［D］正确。\n\n" + rest
            )
            modified = True
        elif qnum == 27:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                clean_part = expl[pos_idx:]
                # ensure no text of IV paragraph poured in
                cut_p4 = clean_part.find('IV ❶ The most drastic')
                if cut_p4 != -1:
                    clean_part = clean_part[:cut_p4].strip()
                q['explanation'] = clean_part
                modified = True
        elif qnum == 28:
            q['explanation'] = (
                "［精准定位］第四段①句thoroughly illegal（完全不合法）初步暗示作者对Sci-Hub的质疑态度；"
                "②句评述Sci-Hub的成功带来的启示：科学出版业合法的生态体系在其用户中已失去合理/正统性（the legal ecosystem has lost legitimacy），"
                "该合法体系必须彻底改变（must be transformed），以重获权威/合理性。由此可见，作者通过非法（无版权保障的）网站的大获成功反向凸显当前科学出版业态的弊病之重，"
                "改革之迫切（如不进行自我改革，事态可能会进一步恶化，催生更多危及各方合法权利的非法事物），可见作者对Sci-Hub等非法网站的成功其实是感到担忧的，［C］正确。\n\n"
                "［命题解密］本题为作者观点态度题，考查作者对免费文献下载网站Sci-Hub的态度。\n\n"
                "［A］、［D］分别传达“问题终获解决”、“有了信心、希望”之意，均为正面态度，与文中thoroughly illegal, lost legitimacy与must be transformed所传递的作者情感“必须对'正统'加以改革，以避免'违法'愈演愈烈”相矛盾。"
                "［B］体现“不理解”之意，但事实上作者对Sci-hub的兴起原因以及兴起的启示都相当明了。\n\n"
                "［技巧总结］当作者的观点态度没有明确给出时，要根据作者选用词汇及表达的情感色彩判断其观点态度。第四段①句thoroughly illegal流露作者对Sci-Hub的批评态度，"
                "②句三个“合法性”相关的描述 legally accessed、the legal ecosystem与has lost legitimacy连用，再次通过“合法体系的正统性必须得到维护”来强调Sci-Hub的非法性，"
                "进一步明确作者对Sci-Hub的不满态度，must be transformed以断然的语气强调真正的解决办法——彻底改革现有科学出版体系（不能任由非法网站继续发展），"
                "同时也与文末作者所述结论“打破行业垄断态势，让权力重获平衡”相符。"
            )
            modified = True
        elif qnum == 29:
            pos_idx = expl.find('［精准定位］')
            if pos_idx > 0:
                q['explanation'] = expl[pos_idx:]
                modified = True
        elif qnum == 30:
            sec_idx = expl.find('［命题解密］')
            rest = expl[sec_idx:] if sec_idx != -1 else ""
            q['explanation'] = (
                "［精准定位］末段①句指出，（众多科学家）付出免费劳动，而赚取巨额利润的却是控制行业的少数大公司，由此可知，科学出版业中，少数（大公司）以多数（科学家的免费劳动）为食，从而发展壮大。［D］正确。\n\n" + rest
            )
            modified = True

    if modified:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Calibrated 2020 ky1 successfully!")

if __name__ == '__main__':
    calibrate_2019()
    calibrate_2016()
    calibrate_2018()
    calibrate_2020()
