# -*- coding: utf-8 -*-
"""
Round 38 Calibration Script (Self-contained)
Target:
2011 ky1 Reading Comprehension (Q21-Q40) in 111d6c78-81a1-53dc-a039-dad4c94ebd35.json
- Fix eaten stems (Q24, Q25, Q28, Q29, Q31, Q36, Q37, Q38, Q39)
- Fix corrupted / swapped options (Q27, Q28)
- Remove stacked bilingual stems & options in explanation heads
- Cut leaked text / bleedings in tail
- Restore complete HuangPiShu [精准定位], [命题解密], 错项排除 & [技巧总结]
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# ----------------- Text 1 (Q21-Q25) -----------------
text_2011_q21 = """［精准定位］第一段①句指出，纽约爱乐乐团聘请Gilbert作为其下任音乐总监的任命决定引发古典音乐界热议，②句紧接着指出其反响为古典音乐界在很大程度上是赞同该任命的，③句更是以音乐评论家Tommasini的欢呼来例证古典音乐界的赞同态度。可见［C］正确。
［命题解密］正确项［C］received acclaim是对②句favorable, to say the least以及③句Hooray! At last!的概括。
［A］利用③句critic的同根词criticism设置干扰，但文中critic是“评论家”之意，且其所言Hooray! At last!表明他对任命的态度为“支持”而非“批判”。
［B］第二段内容“人们认为Gilbert声名不够显著”确实暗含音乐界对任命的怀疑之音（suspicion），但第一段体现的总体态度是“支持赞赏”。
［D］干扰源自第二段①句the appointment came as such a surprise，但将其含义“强调人们虽支持任命，但还是感到意外”改为“对任命感到好奇/不明其中原因”。
［技巧总结］本题就“事件反响”命题，也可视为“文中人物（音乐界）观点态度题”。解答此题须注意：一、抓取各选项关键差异，简化待处理信息；二、总体把握文中内容、抓住反响/态度主线，切忌舍本逐末或对个别词汇断章取义；三、分清观点所属，切勿将作者观点当作文中人物观点。
具体看本题，先分析选项发现四个动词可忽略，区分点在于四个表示态度的名词criticism, suspicion, acclaim, curiosity。随后阅读原文并进行提炼概括，发现古典音乐界对任命总体为赞赏态度（虽然感到吃惊，但并不影响其总体态度）。此外，若把后文的“作者观点”当作“古典音乐界观点”，很可能会误选suspicion，故一定避免此类错误。"""

text_2011_q22 = """［精准定位］第一段③句是Tommasini对任命Gilbert的反应，第二段②句是对Gilbert本人的评价，Tommasini在该句称Gilbert为“谦逊的、没有令人生畏派头的指挥”。可见［B］正确。
［命题解密］正确项［B］是对第二段②句an unpretentious musician with no air of the formidable conductor about him的概括。
［A］对第二段①句反向干扰，将Gilbert“相对不为人知”改为“非常有影响力/知名”。［C］对第二段②句反向干扰，将Tommasini认为Gilbert“没有令人敬畏的派头”改为“令人尊敬的”。［D］既偷换第三段①句观点所有者又违背其本身内容，将“作者不知道Gilbert是否是一位伟大/有天赋的指挥”改为“Tommasini认为Gilbert是一位有天赋的指挥”。
［技巧总结］本题考查“文中人物”就“事件人物某一具体方面的”看法。要求考生全面理解文中人物话语/观点，并进行区分归类，找到题目所问信息；然后进行归纳概括并加以推理。注意干扰项典型设置方式：利用否定句式反向干扰（将否定当作肯定）、将“其他人物观点或文章作者观点”当作“题干所考人物观点”。
具体看本题，首先可圈定前两段中关于Tommasini的所有内容（第一段③句，第二段②句），随后对信息进行区分：第一段③句是Tommasini就Gilbert任命的看法；第二段②句才是就Gilbert本人的看法，是解题的直接线索。但问题在于unpretentious、formidable较生僻，难以直接得知Tommasini观点。故转而借助Even一词理解到，②句是对①句“音乐界对任命感到吃惊，因为吉尔伯特相对不为人所知”的典型例证，［B］与文意一致。"""

text_2011_q23 = """［精准定位］第四段首先指出音乐会忠实听众认为录音无法取代现场演奏，作者对此评价为“没有抓住核心问题”。随后具体说明：音乐录音相对现场演奏更具优势，这些优势已经给古典音乐乐团带来危机。可见，作者认为音乐会忠实听众高估了现场演奏的价值，［D］正确。
［命题解密］正确项［D］是对第四段missing the point在文中具体含义的正确理解，是对②③④句主要内容的概括。
［A］利用②句the time, attention, and money设置干扰词expenses，但“时间、关注和金钱”是各方竞争争夺的对象，而非指“现场演奏的成本”。［B］［C］利用②句not only... but also...设置干扰，但这罗列的是“古典音乐现场演奏的多个竞争对手”，而非是说明“现场演出”或“演奏录音”形式多样。且reject和exaggerate无从得知。
［技巧总结］本题就第四段内容考查“作者对文中人物观点的看法”，需整体把握段落信息。作者提及他人观点的目的分为两种：一、通过批驳对方观点表明自己观点，二、援引对方观点支持自己观点。解题时需要根据句子特征以及逻辑关系词划分段落结构，识别解题的主要线索和次要线索。
如解答本题时，首先可根据首句missing the point的高度概括性（及随后各句的细节性）以及段中主要逻辑词thus（语用功能为“概括前文，述出结果”）判断段落论证结构（①句提出主旨，②③④句具体论证），从而将主要关注点放在首句，并根据missing the point语义判断作者对音乐会忠实听众的看法持“驳斥”态度，即：作者认为“音乐录音可以取代现场演奏”，确定答案为［D］。"""

text_2011_q24 = """［精准定位］第四段③句指出音乐录音的优势：价格低廉、随处可得、艺术品质大多较高，可自主选择“消费”时间和地点，④句将上述优点概括为这类录音的普遍可得性（widespread availability）。故［B］正确。
［命题解密］正确项［B］义同④句widespread availability，概括了③句cheap, available everywhere... can be "consumed" at a time and place of the listener's choosing。
［A］与第四段③句“音乐录音的艺术品质往往比当今的现场演奏高很多”完全相悖。［C］篡改扭曲第四段③句“音乐录音比当今很多现场演奏的品质高”。［D］对第四段②句great classical musicians of the 20th century断章取义，文中提到“20世纪伟大古典音乐家的演奏录音”，并不能说明演奏录音“只涵盖了这一部分作品”。
［技巧总结］本题考查考生分析长难句、把握具体信息的能力，需要得出其中正确关系（注：第三段内容和这一长难句信息紧密相关，对于解题有很大帮助）。
具体来看，正确项［B］概括直接考点③句比较结论，且符合第三段信息（间接考点）。而错误项［A］颠倒比较结果，［C］扭曲具体信息，［D］缩小比较对象范围。若借助上题（考查对本段的宏观把握能力）确认“作者认为音乐录音并非不如现场演奏”，则会大大降低解答本题的难度并提高正确选择的可能。"""

text_2011_q25 = """［精准定位］根据题干revitalizing定位到第五段。该段②句指出Gilbert在新音乐方面的能力受到音乐界的广泛认可，但③句随即以疑问句进行质疑，④句进而指出这一措施的局限性：仅仅扩充乐团的演奏曲目是远远不够的。可见作者对吉尔伯特能否振兴乐团持怀疑态度，［A］正确。
［命题解密］正确项［A］是对③句质疑及④句will not be enough指出的“局限性”的准确解读。
［B］源于开篇“Hooray! At last!”，但这是Tommasini的观点，是作者不认同的观点。［C］源于末段capable of turning the Philharmonic into "a markedly different, more vibrant organization"，但是这是评论家Alex Ross观点，也是作者不赞同的观点。［D］对末段③句错误解读，将“疑问质疑”理解为“表达困惑”。
［技巧总结］本题考查作者态度，表面是就文章末段设题，但实际考查的是对文章整体的把握。解答这类题目需要从文章结构、段间（句间）关系、词汇褒贬色彩多角度整体把握文章内容。切忌断章取义（只抓文中只言片语便确定选项）、张冠李戴（将他人的观点当作作者观点）。
具体看本题，单看第五段，该段以“提出可能措施—质疑该措施”表达了对“靠吉尔伯特振兴纽约爱乐乐团”的质疑，再看全篇，文章整体为“树靶（第一、二段）——批驳（第三、四、五段）”，表面批驳“古典音乐界对任命的看法”，实则在质疑吉尔伯特在振兴纽约爱乐乐团中的作用，故选［A］。"""

# ----------------- Text 2 (Q26-Q30) -----------------
text_2011_q26 = """［精准定位］首段前三句对麦基离职的说辞进行评价：令人吃惊的坦率直接、与人们（此处尤指高管）通常做法不同的是，麦基直截了当表明自己辞职的理由，且将该理由公之于众，可见麦基辞职时的态度为坦率的，［B］正确。
［命题解密］正确项［B］是对文中straight up、Rather than cloaking... came right out and say、broadcasting等词所展现的“直白、直截了当”的高度概括。
［A］和［C］分别从③句broadcasting his ambition以及was very much my decision主观臆断出麦基“傲慢”和“以自我为中心”，但文中此处意不在批评麦基为人，而在于强调其“行事方式（离职）相当坦率”。［D］从①句surprisingly和②句came right out and said主观推出麦基离职是“冲动”使然，而文中②句to pursue...明确表明其职业目标：管理一家公司。
［技巧总结］针对某特殊事例的开篇，命题人有时设计写作目的题，考查对文章宏观把握（近年来这类题相对较少）；有时考查事件细节，如“事件或现象发生的原因（背景）”、“人物具体行为、态度、观点”，看似与主题关联不大，但切记开篇事例实际扮演“引子”角色，用于引出全文主题，细节奠定全文基调。
如本题，解题时首先要“本本主义”：紧抓段中情感态度词来甄别选项，切忌通过个别词汇衍生主观意志；随后再“高屋建瓴”，文章读完后，返回来考虑选项体现的情感基调是否与全文主题基调一致。［A］［C］［D］均“贬义”，而全文无意批判高管行事作风，而是强调“高管辞职、裸辞不像过去被认为是不光彩，如今正成为一种被认可的趋势”，这与“麦基离职时直言相告，不再讳莫如深”所体现的情感基调吻合。"""

text_2011_q27 = """［精准定位］第二段主要分析了高管裸辞的原因：麦基裸辞为了实现“管理一家公司”的职业目标，雅芳公司和美国运通公司二号高管为追求CEO职位而辞职，还有一些高管因继任计划未获董事会首肯而希望换份工作进一步发展。归纳便是：高管裸辞主要由于想要“追求新的职业目标”，［D］正确。
［命题解密］正确项［D］是对第一段②句to pursue my goal of running a company、第二段④句looking for a CEO post的高度概括。
［A］从⑥句a turbulent business environment和④句looking for a CEO post等片段信息中臆断出“高管的经济收入因糟糕的商业环境而下滑，希望通过寻求CEO职位来改善”，但段中未提及他们是因为追求财富而辞职。［B］将①句to reflect on what kind of company he wanted to run偷换为“思考个人生活”。［C］对⑤句in response to shareholder pressure断章取义，文中此处指“董事会囿于股东压力，因而审查高管继任计划，致使一些高管无法获得首肯通过，从而选择辞职”，而非“高管因为与董事会关系紧张而辞职”。
［技巧总结］因果细节是最常考的事实细节。这类题目的题干中通常会出现因果关系词，最常用的是the reason, because of, because, in that, as a result of, be responsible for, due to, owing to, thanks to，本题使用了非显性的因果关系词be spurred by。
第二段借助with the explanation that...、who don't get the nod also may wish to...这类隐形因果表达明确了高管辞职的原因。此外还可以通过本段重点信息③句得知麦基高调裸辞并非个例，再结合首段②句said he was leaving "to pursue my goal of running a company",可推知［D］正确。"""

text_2011_q28 = """［精准定位］被考词所在句上文（①句）点出段落要点：为寻找更好职位而辞掉高级职位，这不符合惯例；所在句（②句）解释道：多年来，高管和猎头们都遵循这样的规则：最有吸引力的CEO是那些……；下文（③句）引证招聘者之言说明：每一次人才搜寻工作，董事会都会要他从在任CEO中物色。纵观选项，唯有［C］“寻找”符合上下文所透露的语义：人才搜寻。
［命题解密］正确项［C］同义替换段内look for, search, look at,与headhunters（猎头）语域相近。
［A］偷换了②③两句语境，③句can't think of... where a board has not instructed me to...文意重点在于“猎头挖人之举符合董事会授意”，不在于说“优秀的CEO都是被认可的”。［B］在②句the ones who must be poached和the most attractive CEO之间机械地划上等号，衍生出“被留心、关注的”之意。［D］反向曲解文中search, look at, headhunt等所传达的“被猎取，被搜寻”这一语义。
［技巧总结］poach是超纲词，也是第四段的主题关键词。阅读中，生词是可猜测的。每篇文章中都存在上下文线索和语言的冗余，最常见的有：句子逻辑、词语的搭配、解释、同位语、举例、近义反义词复现。
理解poach需要到上下文中寻找线索。首先，从句间语义逻辑入手。①②句是对比关系。①句为非传统做法：高管主动辞职去寻求更高职位；②句为传统做法：（优秀）CEO人选必须是被poached的。②③句是解释关系。③句进一步解释②句的传统招聘规则：董事会授意猎头公司从其他公司现任CEO中物色人选。综上可知，传统规则是CEO被猎头从其他公司挖过来。其次，从词语搭配判断。与poach构成动宾关系的是CEO candidates，③句中与CEO搭配的是search和look at，只有［C］符合搭配要求。"""

text_2011_q29 = """［精准定位］末段③句指出高端职场传统规则：不挪窝更保险，原地不动最安全；换而言之，过去高级职员们常常坚守其职。［A］为正确选项。
［命题解密］正确项［A］是③句第一个分句的同义改写，used to对应The traditional rule, cling to their posts对应stay where you are。
［B］把③句stay where you are等同于loyalty，从文中“过去的固守原地不动其实伤害更大，裸辞兴起”错误得出“忠诚已经过时”的结论，但“待在原处（一直不跳槽）”未必就“忠诚”。［C］从①句the old disgrace is fading for top performers反推出“高级职员历来非常关注名声”，但选项为一般现在时，不符合文中“过去会认为裸辞后的待业状态有失身份，而现在已改变”的语义逻辑。［D］把③句The traditional rule was it's safer to stay where you are偷换成泛化的“坚守传统规则更安全”（注意选项中traditional rules为复数形式，泛指一切传统规则）；其次从文中来看，传统规则已被颠覆，暗示其“不再安全”。
［技巧总结］段落推断题要求考生体味段中的“言外之意”。解答此类题首先要建立在理解字面含义的基础上，推测作者未明说但又意欲表达的含义。要尽可能与作者达成“共识”。
如本题，②句说金融危机使（高级职员们）暂时失业或辞去糟糕工作变得更可接受了；换言之，高级职员过去往往不能接受裸辞，宁肯固守岗位；同时，③句说传统的职场规则是待在原来的岗位上更安全，但是这项规则已经被彻底颠覆了；也即，以前高管们都倾向于固守岗位，但现在不再如此，［A］正确。"""

text_2011_q30 = """［精准定位］本文采用例证法、引证法，就新现象“金融危机过后美国高端职场顶级经理人纷纷裸辞”展开原因及意义分析。全文主题词为jump without a net/quitting/top managers/CEOs，［C］符合文章中心主旨。
［命题解密］［C］Top Managers Jump without a Net（高管裸辞）全面契合文章主旨。
［A］“首席执行官们：路在何方？”与［B］“首席执行官们：一路高升？”均属于宽泛而偏离主线的设问，未能体现“裸辞（without a net）”这一核心动态。［D］“顶尖人才的唯一出路”中The Only Way Out过于绝对，偏离文意。
［技巧总结］主旨标题题旨在考查文章主旨，其解答技巧重在寻找文章主题句或主题词。主题句通常出现在三个地方：文章首段首句、文章开头转折处和文章开头现象结束处。且主题句通常是一个概括总结性的结论或者判断。纵观各段落主题句可知，全文一直都是在讲高管的裸辞，［C］正确。"""

# ----------------- Text 3 (Q31-Q35) -----------------
text_2011_q31 = """［精准定位］根据题干关键词“earned” media定位到首段④句。该句指出，热衷某一产品的消费者自愿将其推荐给朋友时，便创建了“赢得（口碑）”媒介。可见［D］符合文意。
［命题解密］题干+正确项［D］构成对第一段④句关于“赢得媒介”部分（前半句）的同义改写：enthusiastic about recommending对应willingly promoting；favorite products对应passionate about a product。
［A］对④句passionate... registered with its Web site断章取义，将关于两种媒介的信息“热情的消费者很可能会生成‘口碑’媒介（'earned' media）；企业给网站注册用户发送提醒以利用‘自有’媒介（'owned' media）”糅杂到一起并堆砌于一种媒介、得出与文意无关的选项“消费者热衷在某些网站购物时会形成赢得媒介”。［B］将④句sending e-mail alerts about products由“企业生成自有媒介的手段（a company may leverage “owned” media）”改为“消费者生成赢得媒介的方式（Consumers may create "earned" media）”。［C］将④句passionate... willingly promoting it to friends篡改为与之存在巨大含义偏差的eager to help their friends promote quality products。
［技巧总结］涉及“新概念、新事物”以及“复杂关系”的长难句很容易成为命题人的着眼点，对于这种题目要：一、精读所考句，辨认其间涉及关系；二、结合“寻找正确项”和“排除干扰项”两个角度：正确项为对原文的同义改写或概括引申；干扰项通常为偷梁换柱、糅杂信息、扭曲信息等。
如本题，题干就“赢得媒介（earned media）的生成”设题。对应原文（首段④句）则涉及两个新概念（“赢得媒介”和“自有媒介”）以及围绕两个新概念的两组关系（赢得媒介/消费者/产品/朋友；自有媒介/公司/email/其网站注册的消费者）。明确这种关系后对比各项，发现［D］与原文信息一致，而［A］将属于两个概念的信息糅杂，［B］偷梁换柱，［C］则扭曲信息生成与原文外形相似、含义相远的信息，［D］正确。"""

text_2011_q32 = """［精准定位］根据题干关键词sold media定位到第二段。该段③④句指出，出售媒介衍生自“自有媒介”，其生成条件是：自有媒介拥有巨大的用户访问量来吸引其他营销商付费投放广告。可见［C］符合文意。
［命题解密］正确项［C］strong user traffic是对第二段④句whose traffic is so strong that...所述“出售媒介”特征的概括，体现了其核心内容traffic... strong。
［A］将④句that environment所指主观理解为“安全的商业环境”，但文中并未提及出售媒介的“安全性”。［B］将⑥句所述BabyCenter个例“推广竞争性产品（competitive products）”当做出售媒介的共性，并将其改为具有巨大含义偏差的“以随机竞争为特点”。［D］将⑦句Besides generating income... makes... gives... and may help...功能“说明BabyCenter这一出售媒介的优势”理解为“说明出售媒介整体特征——组织方式灵活”。
［技巧总结］本题考查文章重点关注新事物“出售媒介”的总体特征。答题时需：一、读题干，意识到features、is characterized by是典型的考查“某物总体特征”的设问方式；二、定位原文，从原文寻找“概括性内容”，切勿将“个例特点”当“整体特征”；三、辨别选项，概括原文、体现关键点的选项是正确项。具体看本题，第二段⑥句for instance对前文论点举例说明，［C］强劲的用户流量准确概括了其核心特征，为正确项。"""

text_2011_q33 = """［精准定位］根据题干关键词earned media定位到第三段。该段指出：同样的重大技术变革在给营销商带来更多传播渠道的同时，也增加了其风险——充满激情的消费者会发表不利于企业的观点；这种劫持媒介是赢得（口碑）媒介的反面。紧接着作者用社交网络用户举例说明：网络用户可以通过劫持原本媒介向最初创建这些网络的企业（即：企业原本是将其作为“赢得/口碑媒介”）施压。可见，赢得（口碑）媒介有可能被用作“劫持”媒介，用以制造负面效应，［B］正确。
［命题解密］正确项［B］是第三段②③句隐含深意“劫持媒介和赢得（口碑）媒介的对立衍生关系”的体现，其中be used to produce negative effects对应the opposite of，并明确businesses that originally created them深层内涵。
［A］将①②句中passionate consumers will... voice their opinions... more damaging ways... make negative allegations所表明的信息“狂热消费者可能（利用赢得媒介）与企业产生冲突”改为“狂热消费者会与赢得媒介产生冲突”。［C］将②句campaign理解为“竞争、竞赛”之意、并进一步主观得出联系“赢得媒介加剧竞争”，而实际上这里campaign意为“宣传活动”。［D］将②句negative所指“消费者对产品等发表负面评论”偷换为“消费者对赢得媒介发表负面评论”，且文中并未表明一切负面评论都是赢得媒介应受的，deserve all夸大其词。
［技巧总结］本题考查考生“洞察细节+把握前后逻辑关系”的能力，题干就第三段暗示的“赢得媒介（earned media）”信息设题，但该段主要关注“劫持媒介（hijacked media）”，需要借助多条线索，明确二者关系：1）第三段②句直接说明劫持媒介和赢得媒介为“对立转换关系”；2）第三段①句、③句和首段Consumers passionate about a product may create "earned" media by willingly promoting it to friends呼应，表明“劫持媒介”和“赢得媒介”关键人物均在于“充满激情的消费者”，不同在于“这些消费者发表的信息有益于还是不利于营销者”。综合两条线索可确定［B］正确。"""

text_2011_q34 = """［精准定位］第四段①②句指出，面对劫持媒介造成的威胁，公司的回应必须尽可能迅速而周到、且公司就此已经在短时间内取得巨大进步。③句列举丰田汽车公司的例子对前两句观点予以佐证。由此可见，丰田汽车公司在文中是“有效回应劫持媒介以降低损失”的事例，［A］正确。
［命题解密］正确项［A］是第四段②句（例证观点句）的同义改写。
［B］将①句中劫持媒介的发起者“消费者”篡改为“丰田汽车公司”。［C］将③句engage with consumers directly所表明信息“丰田公司在社交媒体上与声讨自己的消费者直接进行交流”曲解为“与支持自己的消费者进行合作”。［D］对③句a relatively quick and well-orchestrated social-media response campaign断章取义，理解为“丰田公司借助劫持媒介有效发起……活动”，而实际上丰田公司是“被迫努力应对劫持媒介所造成危机的‘受害者’”。
［技巧总结］本题直接考查理解例证、区分论点论据的能力，但由于例证观点句中有正话反说、固定短语等，故实际也间接考查结合上下文理解特殊表达具体含义的能力。解答此题需注意：一、举例一定是为说明论点（意群、段落、甚或是文章主旨）。二、遇到难以理解的论点句需根据前后句逻辑及文章主旨进行推理；三、若短时间内无法得知论点句确切含义，可转而采用“确定正确项”和“排除干扰项”相结合的方式解题。
具体看本题，首先根据逻辑提示词for example将第四段一分为二：①②句为论点，③句事例为论据；再根据In such a case, the company's response may...进一步将②句确定为主要观点句，正确项应该是对②句的改写。但随后发现②句中may not be sufficiently quick or thoughtful不易理解，这时可借助事例主要信息alleviated some of the damage, quick and well-orchestrated, campaign, efforts推知丰田公司基本上做到了成功应对危机，判断［A］正确、［D］错误，借助具体信息对比排除偷梁换柱的［B］、添加无关信息supportive的［C］。"""

text_2011_q35 = """［精准定位］通览全文，第一段指出，现代市场营销已经超越传统的单一的付费媒介，成为各种媒介合力作用的结果。第二段重点展现“出售媒介”给营销商带来的机遇。第三、四段则说明劫持媒介带给营销商的风险并说明公司应如何应对。可见，本文主要围绕“营销新媒介”展开论述，［A］体现全文论述对象。
［命题解密］［A］是对文章主旨句（第一段⑤句）的概括和改写，对应原文中alternative forms of media, a broad range of factors beyond conventional media，且体现了充斥全篇的各种media字样。
［B］根据第三段②句the opposite of设置干扰，文中该词强调的是劫持媒介和赢得（口碑）媒介的“对立衍生关系”而非“相互冲突关系”，且该选项以偏概全：文中并非仅限于讨论这两种媒介的关系。［C］将占据本文较大篇幅（第三、四段）的媒介之一“劫持媒介”当做本文唯一关注对象，依然犯了以偏概全的错误；且dominance无从推知。［D］将第一、二段提及较多的“自有媒介”当做文章关注对象，但第三、四段基本未再提及该内容，故同样以偏概全；且文中并未指出自有媒介非常流行——popularity无从推知。
［技巧总结］本题是典型的文章主旨题考查方式，解答此类题应：1）通览全文，通过归纳各段主旨大意来理清文章论证结构、并抓取各段反复出现的关键词，得出全文核心论述对象；2）正确项必须恰当地涵盖文章核心主线，且体现充斥全篇的media字样，［A］正确。"""

# ----------------- Text 4 (Q36-Q40) -----------------
text_2011_q36 = """［精准定位］第一段②句指出，Senior建议我们应把幸福视为一种过去完成时的状态，③句进而指出，今天看似沉重繁琐的育儿负担在日后却会成为极大的满足与欣喜的源泉。可见Senior认为育儿能够带来日后回味时的快乐，［C］正确。
［命题解密］正确项［C］是对②③句中consider being happy as a past-tense condition... later be sources of intense gratification and delight的高度概括。
［A］将②句用于说明育儿会带来“日后的快乐（a past-tense condition）”曲解为“稍纵即逝的/短暂的快乐”。［B］将②句Senior摒弃的观点“将育儿视为即时即地的快乐（enjoyment in progress近义替换moment-to-moment joy）”视为其认同的观点。［D］将③句later be sources of intense gratification and delight（育儿会带来日后的巨大快乐［但过程本身非常折磨］）错误理解为“育儿会带来持久的回报”。
［技巧总结］本题针对涉及“多组取舍关系”以及“抽象表达（a past-tense condition等）”的第一段命制“人物观点题”。这要求：一、借助观点引出词（suggest, write, say等）及取舍标志（Rather than, instead, instead of等）对信息分类，区分人物所持观点及其摒弃观点；二、联系上下文明确抽象表达的具体含义；三、意识到“将人物摒弃观点当做赞同观点”及“对抽象表达断章取义”是最典型的干扰方式。
具体到本题，借助观点引出词suggestion/suggests/writes及取舍标记Rather than/instead of可明确划分Jennifer Senior所持有观点（①句suggestion that引领内容；②句Senior suggests及we should引领部分；③句内容）及其摒弃的做法（②句Rather than及instead of引领内容），［C］是对其持有观点的概括，［B］将其摒弃观点当做持有观点，［A］、［D］对其中抽象表达断章取义，故［C］正确。"""

text_2011_q37 = """［精准定位］第二段指出，报刊每周都会专题报道明星妈妈怀孕、育儿故事。联系上段“没有什么比‘育儿绝非完全是成就自我、丰富生活的体验’这一提议更能引发人们讨论”可知媒体如此热衷报道这类新闻的原因：生育是公众高度关注的话题。第三段首句也证实道：当今社会执着地颂扬生育。故［D］正确。
［命题解密］正确项［D］是对第二段内容的概括引申，也是对第三段首句的同义改写：the public对应society；having children is highly valued对应so persistently celebrates procreation。
［A］将第二段所述事实“每周报刊杂志上都会有对明星妈妈的特别报道（news, features）”改为与之存在含义偏差的“明星妈妈是（各报刊杂志）永恒的八卦对象（source for gossip）”。［B］single mothers with babies源自第二段②句newly single-mom，但deserve greater attention却是无法推知的内容（文中并未将“单身妈妈”与其他女性/妈妈对比）。［C］news about pregnant celebrities源自第二段②句the usual "Jennifer Aniston is pregnant" news，但文中只提及这类报道很常见，而并未提及这类报道的“娱乐性（entertaining）”。
［技巧总结］本题考查对段落细节的理解和概括推理能力。解答这类题型时应注意：一、对段落主要信息进行概括推理，不能孤立地理解某一具体信息；二、概括推理的标尺是该段的论述结构、上下文（尤其是段落首尾句）乃至全文主题，而非常识性信息或主观印象；三、将选项信息与原文对比，排除那些“部分正确+部分错误”的选项。
具体看本题，段落以递进结构展示了杂志对“明星妈妈幸福育儿形象”的高频度、全方位报道，且上段已表明本文论述主题“育儿幸福观”，下段首句则明确指出这是一个高度颂扬生育的社会，可见［D］是结合上下文对第二段内容做出的概括推理，为正确项。"""

text_2011_q38 = """［精准定位］第三段②③句指出：不快乐的无子女者不断被外界信息所烦扰：孩子是世界上唯一最重要的，无子女者的不快乐一定源于没有孩子的空缺。可见，无子女者不断受到外界指责，［A］正确。
［命题解密］正确项［A］是对第三段②③句信息...（not） fair... are bothered with the message that...结合上下文做出的概括推理。
［B］从第二段内容“媒体特别关注明星育儿、怀孕的消息”主观反推出“无子女者被媒体忽视”，但这与第三段③句“无子女者不断受到外界信息/媒体的烦扰”相悖。
［C］是第三段③句that children are the single most important thing in the world暗含的“社会大众”观点“不生育子女是逃避社会责任”，但它实为受批判的观点。
［D］是第三段③句obviously their（childless folks'）misery must be...暗含的“社会大众”观点“无孩者生活并不圆满、很难对生活感到满足”，但它实为受批判的观点。
［技巧总结］本题是就涉及“对比、类比、比喻”等论证手法、包含“外界做法/态度”及“本段/本文作者批驳态度”的段落命制的对本文观点推理引申题，难度相当大。解答此题需要：一、结合上文作者态度把握段落主旨方向；二、整体看全段理解对比、类比、比喻的功用和内涵；三、借助语态（被动VS主动）区分“文章本身观点”和“社会大众观点”；四、深层挖掘词语中暗含的情感色彩。
具体看本题：根据题干可知题目问的是第三段所传达的“本文观点”；结合本文前两段概括本段主旨为：作者认为当下社会一味崇尚生育的做法有失公允；借助被动语态（are... provoked... are bothered...）可知本段末句所述为“社会外界做法/态度”而非“文章本身表明的观点”；整体看首句的类比“将后悔生儿育女视为赞同残杀小猫”和末句的比喻“无子女者的痛苦必定是……孩子大小的窟窿带来的直接后果”可得出外界对无子女者的道德绑架和武断指责；进一步深挖发现，the single most important thing in the world, must be, direct result所含有的情感色彩已明显传递外界对不生育子女者的批判；而rarely are provoked...和are bothered with...的对比，分别反向、正向传递了批评的“经常、无处不在”，从而确定［A］正确。"""

text_2011_q39 = """［精准定位］第四段①句指出，名人杂志中呈现出来的为人父母形象当然非常不现实，尤其是布洛克这样的单亲妈妈。紧接着②③句以单亲父母育儿的实际艰辛反衬名人杂志宣传的“独自养娃小菜一碟”严重脱离现实。可见，名人杂志传达的信息具有误导性，［D］正确。
［命题解密］正确项［D］misleading是对①句hugely unrealistic（极度不现实）的同义替换。
［A］将文中名人杂志宣扬育儿“轻松（a piece of cake）”误解为“令人宽慰（soothing）”。［B］将②③句“说明名人杂志宣扬信息和现实育儿情形并不一致”误解为“说明名人杂志模棱两可，可以做出不同的解读”。［C］将②③句所述“现实情形”和“名人杂志信息”之间的“不一致、相悖关系”曲解为“补充、补偿关系”。
［技巧总结］本题考查段落核心论点与作者评价态度。抓住段落首句中心句中的态度评价词（hugely unrealistic）即可迅速破题，并同义替换为misleading。"""

text_2011_q40 = """［精准定位］末段最后两句指出，名人杂志上那些光鲜亮丽的明星母亲形象给公众传递了一种虚假的信号，使得人们误以为为人父母是一种轻松无压力的美妙体验，从而深刻影响了公众对待生儿育女的态度。可见，明星母亲影响了我们对育儿的态度，［B］正确。
［命题解密］正确项［B］Celebrity moms have influenced our attitude towards child rearing是对末段核心主旨的精确提炼。
［A］与末段事实相反，明星母亲正是借助生儿育女大肆增添自身光彩。［C］无中生有，文中并未提及生孩子加剧了对生活的不满。［D］利用文中stress-free, happiness-enhancing parenthood捏造干扰，文中并未提及我们忽略了育儿的快乐。
［技巧总结］尾段推断题通常考查全文最终结论或文章主旨的升华。解答此类题应紧扣尾段观点，抓住核心动词与宾语之间的逻辑对应关系，排除无中生有和反向曲解选项。"""

# Run calibration
exam_path = 'public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json'
with open(exam_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

calibrated_count = 0

for q in exam_data['questions']:
    so = q.get('sort_order')
    if so == 21:
        q['stem'] = "We learn from Para. 1 that Gilbert's appointment has ________."
        q['explanation'] = text_2011_q21
        calibrated_count += 1
    elif so == 22:
        q['stem'] = "Tommasini regards Gilbert as an artist who is ________."
        q['explanation'] = text_2011_q22
        calibrated_count += 1
    elif so == 23:
        q['stem'] = "The author believes that the devoted concertgoers ________."
        q['explanation'] = text_2011_q23
        calibrated_count += 1
    elif so == 24:
        q['stem'] = "According to the text, which of the following is true of recordings?"
        q['explanation'] = text_2011_q24
        calibrated_count += 1
    elif so == 25:
        q['stem'] = "Regarding Gilbert's role in revitalizing the Philharmonic, the author feels ________."
        q['explanation'] = text_2011_q25
        calibrated_count += 1
    elif so == 26:
        q['stem'] = "When McGee announced his departure, his manner can best be described as being ________."
        q['explanation'] = text_2011_q26
        calibrated_count += 1
    elif so == 27:
        q['stem'] = "According to Paragraph 2, senior executives' quitting may be spurred by ________."
        q['options'] = [
            {'key': 'A', 'text': 'their expectation of better financial status', 'value': 'A'},
            {'key': 'B', 'text': 'their need to reflect on their private life', 'value': 'B'},
            {'key': 'C', 'text': 'their strained relations with the boards', 'value': 'C'},
            {'key': 'D', 'text': 'their pursuit of new career goals', 'value': 'D'}
        ]
        q['explanation'] = text_2011_q27
        calibrated_count += 1
    elif so == 28:
        q['stem'] = 'The word "poached" (Line 3, Paragraph 4) most probably means ________.'
        q['options'] = [
            {'key': 'A', 'text': 'approved of', 'value': 'A'},
            {'key': 'B', 'text': 'attended to', 'value': 'B'},
            {'key': 'C', 'text': 'hunted for', 'value': 'C'},
            {'key': 'D', 'text': 'guarded against', 'value': 'D'}
        ]
        q['explanation'] = text_2011_q28
        calibrated_count += 1
    elif so == 29:
        q['stem'] = "It can be inferred from the last paragraph that ________."
        q['explanation'] = text_2011_q29
        calibrated_count += 1
    elif so == 30:
        q['stem'] = "Which of the following is the best title for the text?"
        q['explanation'] = text_2011_q30
        calibrated_count += 1
    elif so == 31:
        q['stem'] = 'Consumers may create "earned" media when they are ________.'
        q['explanation'] = text_2011_q31
        calibrated_count += 1
    elif so == 32:
        q['stem'] = "According to Paragraph 2, sold media feature ________."
        q['explanation'] = text_2011_q32
        calibrated_count += 1
    elif so == 33:
        q['stem'] = "The author indicates in Paragraph 3 that earned media ________."
        q['explanation'] = text_2011_q33
        calibrated_count += 1
    elif so == 34:
        q['stem'] = "Toyota Motor's experience is cited as an example of ________."
        q['explanation'] = text_2011_q34
        calibrated_count += 1
    elif so == 35:
        q['stem'] = "Which of the following is the text mainly about?"
        q['explanation'] = text_2011_q35
        calibrated_count += 1
    elif so == 36:
        q['stem'] = "Jennifer Senior suggests in her article that raising a child can bring ________."
        q['explanation'] = text_2011_q36
        calibrated_count += 1
    elif so == 37:
        q['stem'] = "We learn from Paragraph 2 that ________."
        q['explanation'] = text_2011_q37
        calibrated_count += 1
    elif so == 38:
        q['stem'] = "It is suggested in Paragraph 3 that childless folks ________."
        q['explanation'] = text_2011_q38
        calibrated_count += 1
    elif so == 39:
        q['stem'] = "According to Paragraph 4, the message conveyed by celebrity magazines is ________."
        q['explanation'] = text_2011_q39
        calibrated_count += 1
    elif so == 40:
        q['stem'] = "Which of the following can be inferred from the last paragraph?"
        q['explanation'] = text_2011_q40
        calibrated_count += 1

with open(exam_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"2011 ky1 Reading calibration completed: {calibrated_count} questions calibrated.")
