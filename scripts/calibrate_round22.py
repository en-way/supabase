import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 22 Calibration ===")

# 1. 2008 ky1 Text 4 (Q36-40)
f2008 = [f for f in glob.glob('public/data/exams/*.json') if '2008' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
with open(f2008, 'r', encoding='utf-8') as f:
    d2008 = json.load(f)

for q in d2008['questions']:
    so = q['sort_order']
    if so == 36:
        print("Calibrating 2008 ky1 Q36...")
        q['stem'] = "George Washington's dental surgery is mentioned to"
        q['options'] = [
            {"key": "A", "text": "show the primitive medical practice in the past"},
            {"key": "B", "text": "demonstrate the cruelty of slavery in his days"},
            {"key": "C", "text": "stress the role of slaves in the U.S. history"},
            {"key": "D", "text": "reveal some unknown aspect of his life"}
        ]
        q['correct_answer'] = 'D'
        q['answer'] = 'D'
        q['explanation'] = (
            "［精准定位］由题干关键词 George Washington's dental surgery 定位至首段。该段指出华盛顿从奴隶口中拔了九颗牙移植到自己口中。"
            "第二段首句则指出：这与人们通过历史书所熟知的华盛顿砍樱桃树的形象大不相同。反推可知，作者第一段事例意在让读者看到华盛顿不为人知的一面，［D］正确。\n\n"
            "［命题解密］正确项［D］体现了“第一段事例”和“第二段首句”之间形成的对比。选项 some unknown aspect 恰和第二段首句 most people remember 相对。\n\n"
            "［错项排除］［A］利用第一段②句关于牙齿手术的实施细节，以及考生背景知识“18世纪牙齿移植技术尚不发达”形成干扰，但和上下文无法顺接。"
            "［B］利用第一段②句所述事实“华盛顿命人从奴隶口中拔出牙齿移入自己口中”及背景信息“奴隶制相当残忍”设置干扰，但偏离事例关注对象（主角）“华盛顿”。"
            "［C］改变讨论范围，故事最多只能说明奴隶对于华盛顿、开国元勋一代人的作用，而选项却将其扩大至在美国历史上的作用。\n\n"
            "［技巧总结］本题就首段事例设置写作目的题，解题关键在第二段首句。解题思路为："
            "1）若文章首段整段单纯讲述事例，则写作目的应往下文寻找。"
            "2）理清“方向”：作者是正向引入（从点扩大到面）还是反向引入（从特例到相反的总体现象）；且要注意把握“度”：既不能拘泥于事例本身细节，又不能主观拔高事例意义。"
            "3）避免干扰的关键在于：不能脱离语境，依赖自身背景知识对事例细节进行主观臆测。具体到本题，文章首段并未就牙齿手术直接给出作者观点，而是讲述了一个事例；"
            "随后第二段首句承接指出“这与大多数人记忆中历史书上的华盛顿大不相同”，作者对比意图极为明显，即说明“这一面是不为人所知的”，锁定［D］。"
            "［A］、［B］、［C］均脱离了“华盛顿事例不为人知”这一核心意图，故排除。"
        )
    elif so == 37:
        print("Calibrating 2008 ky1 Q37...")
        q['stem'] = "We may infer from the second paragraph that"
        q['options'] = [
            {"key": "A", "text": "DNA technology has been widely applied to history research"},
            {"key": "B", "text": "in its early days the U.S. was confronted with delicate situations"},
            {"key": "C", "text": "historians deliberately made up some stories of Jefferson's life"},
            {"key": "D", "text": "political compromises are easily found throughout the U.S. history"}
        ]
        q['correct_answer'] = 'B'
        q['answer'] = 'B'
        q['explanation'] = (
            "［精准定位］第二段⑤句指出，历史学家的著作揭示了美国建国初期的脆弱性。根据上下文可知，这里“脆弱性”指的是早期美国特殊的、微妙的环境，"
            "它导致了建国者的道德妥协（明知奴隶制错误，却很少有人试图推翻它）。因此［B］正确。\n\n"
            "［命题解密］正确项［B］是对第二段⑤句 the fragile nature of the country's infancy 的改写，delicate（needing to be dealt with carefully or sensitively in order to avoid problems or failure“微妙的，需要谨慎处理的”）对应 fragile；in its early days the U.S. 对应 the country's infancy。\n\n"
            "［错项排除］［A］将②③句信息“DNA技术激发了历史学家对奴隶制在开国元勋们生活中所扮演角色的关注”夸大为“DNA技术被广泛用于历史研究”。"
            "［C］将③句信息“历史学家借助DNA证据几乎可以确证杰斐逊与其奴隶的故事”改为与之完全相反的“历史学家故意编造杰斐逊的生活故事”。"
            "［D］将⑤句信息“美国早期领袖做出了道德妥协”夸大为“政治妥协在整个美国历史上随处可见”。\n\n"
            "［技巧总结］第二段涉及历史学家对开国元勋研究角度的转变及具体的研究发现等，本题就此考查考生“对具体细节进行推理引申”的能力。解答此类题目首先要“抓大”（比对上下文语境，提取本段关键词，归纳段落主旨），然后“揪小”（在段落主旨宏观脉络下，理解文章细节、对比选项）；错误项一般就段中“细节”颠倒是非或夸大其词。"
            "如本题，提取段落关键词 begun to focus on... examined history from the bottom up... moral compromises... knew slavery was wrong... did little to fight it 可知，本段意在指出历史学家通过研究角度的转变取得的新发现：开国元勋对待奴隶制态度矛盾复杂（做出道德妥协；意识到奴隶制的错误性，却没有以实际行动来极力反对它），下文就此态度展开原因分析。"
            "［B］从大方向上符合这一段落主线（开国元勋之所以这样做，很大原因在于当时微妙的环境），且从细节上选项关键词 delicate 是对原文关键词 fragile 的同义表达，in its early days the U.S. 正确表述文中关注范围 the country's infancy，故正确。［A］、［D］夸大其词、［C］颠倒是非，且三个选项均无法与段落主旨相关联，故排除。"
        )
    elif so == 38:
        print("Calibrating 2008 ky1 Q38...")
        q['stem'] = "What do we learn about Thomas Jefferson?"
        q['options'] = [
            {"key": "A", "text": "His political view changed his attitude towards slavery."},
            {"key": "B", "text": "His status as a father made him free the child slaves."},
            {"key": "C", "text": "His attitude towards slavery was complex."},
            {"key": "D", "text": "His affair with a slave stained his prestige."}
        ]
        q['correct_answer'] = 'C'
        q['answer'] = 'C'
        q['explanation'] = (
            "［精准定位］第三段②句指出杰斐逊私下表达过对奴隶制的反感，但又知道奴隶制非常重要；第五段指出在任期间他扩大了奴隶制的范围；"
            "第六段则指出他解放了奴隶赫明斯的孩子。可见他对奴隶制的态度是复杂的，［C］正确。\n\n"
            "［命题解密］正确项［C］是对散落全篇的 knew slavery was wrong and yet most did little to fight it... Jefferson privately expressed distaste for slavery, they also understood that... extended slavery... freed Hemings's children 等内容的高度概括。\n\n"
            "［错项排除］［A］将第五段①句 the statesmen's political lives depended on slavery 中涉及关系“（政治家们/杰斐逊等）的政治生涯取决于奴隶制”歪曲成与之存在巨大含义偏差的“他的政治观点改变（影响）了他对奴隶制的态度”。"
            "［B］将第六段①句中杰斐逊给予自由的对象“赫明斯的子女”放大为“儿童奴隶”。"
            "［D］对第二段③句 Thomas Jefferson had fathered at least one child with his slave Sally Hemings 进行过度推导，文中并未指出这玷污了杰斐逊的声誉。\n\n"
            "［技巧总结］本题综合考查“关于杰斐逊的事实细节”，虽段落跨度较大，但究其根本仍在借文中典型事例人物考查文章主旨。此类题的解答方法有二："
            "1）将原文所有关于杰斐逊的信息一网打尽，然后结合全文主旨，归纳出人物的行为特点、情感态度及前后变化，最后与选项对比，做出正确选择；"
            "2）先概括各选项主要信息，有目的地回文中找相关类似信息。对此类借典型事例人物考查文章主旨的题，正确项一般不仅是文章信息的同义表达，还须从大局出发，不拘泥于细节；错误项通常会对文章的细枝末节偷梁换柱、过度引申或故意歪曲。"
            "如本题，可将第二、三、五、六段关于杰斐逊对奴隶制的态度行为及阶段性变化逐一罗列（杰斐逊为开国元勋之一，因此文中提及开国元勋部分也需留意），经对比发现：［C］是对相关信息的高度概括，为正确项；［A］歪曲文中关系，［B］夸大其词，［D］过度引申，故均排除。"
        )
    elif so == 39:
        print("Calibrating 2008 ky1 Q39...")
        q['explanation'] = (
            "［精准定位］第五段首句指出，政治家的政治生涯取决于奴隶制；紧接着以杰斐逊事例证明：杰斐逊在1800年总统选举中的险胜即得益于五分之三方案。"
            "由此可知，以杰斐逊为代表的一些开国元勋在政治上得益于奴隶制，［A］正确。\n\n"
            "［命题解密］正确项［A］是对第五段首句的同义改写，Some Founding Fathers 对应 the statesmen, benefit politically from slavery 对应 political lives depended on slavery 以及 The three-fifths formula handed Jefferson his narrow victory。\n\n"
            "［错项排除］［B］对第四段③句 counted a slave as three fifths of a man for purposes of congressional representation 设置干扰，但原文提及该条款是为说明出于国会代表权（congressional representation）考虑，在计算人口时将奴隶的人口乘以五分之三，并未提及奴隶选举权问题。该选项是利用“奴隶没有选举权”这一常识设置干扰。"
            "［C］对第四段②句的比喻 Owning slaves was “like having a large bank account”（喻意“奴隶对奴隶主具有巨大价值”）断章取义。"
            "［D］将第四段③句 the “peculiar institution”等同于 a peculiar institution：将“奴隶制”称为“特别制度（peculiar institution）”的是“南方各州”，而不是“本文作者”（句中定冠词 the 和引号表明：作者并不认同这一称谓）。\n\n"
            "［技巧总结］本题题干无法推知所考范围。对此，可先提炼选项关键词，然后大致定位搜索范围，并将原文和选项进行推理对比。需注意：一，理清句间关系（尤其是例证关系），完整把握句群信息；二，不能对比喻表达断章取义，而是应该结合上下文得知其具体含义；三，注意文中特殊标点的语用功能，如引号经常表示引用、反语或讽刺，其表示的不一定是作者认同的观点，甚至可能是作者排斥的看法。"
            "如本题，首先根据题干关键信息 savings accounts/peculiar institution/benefit politically from slavery 与原文 a large bank account/the “peculiar institution”/political lives depended on slavery 的相似性可以定位到第四、五段。完成定位后进行对比推理发现，［A］把握了第五段①②句间的例证关系，完整体现该部分内容，故正确。"
        )
    elif so == 40:
        print("Calibrating 2008 ky1 Q40...")
        q['explanation'] = (
            "［精准定位］根据题干关键词 Washington's decision to free slaves 定位到第六段②句。该句指出华盛顿在目睹了独立战争中黑人士兵的勇敢后，开始相信人人生而平等，最终决定解放其奴隶。可见，让他最终下决心释放奴隶的是他在独立战争中的经历，［B］为正确选项。\n\n"
            "［命题解密］题干+正确项［B］构成对末段②句 ...had begun to... after observing the bravery of the black soldiers during the Revolutionary War, ...grant his slaves their freedom 所暗含因果关系的明确。\n\n"
            "［错项排除］［A］对第二段⑤句反向干扰，将开国元勋（包括华盛顿）“在奴隶制问题上做出了道德妥协/采取了不够道德的做法（moral compromises）”改为相反的“华盛顿出于道德考虑释放了奴隶（moral considerations）”。"
            "［C］曲解第四段②句 Owning slaves was “like having a large bank account”之中含有的逻辑关系，将“奴隶具有巨大的经济价值，所以奴隶主不愿解放奴隶”改为与之相悖的“华盛顿（奴隶主）之所以释放奴隶是因为其经济状况”。"
            "［D］利用第五段①句 political lives 断章取义，但原文指出政治家的“政治生涯得益于奴隶制”，与华盛顿解放奴隶的行为无关。\n\n"
            "［技巧总结］本文就“文中多处提及的人物行为”设置因果细节题，答案所在句为关系复杂的长难句、且并未使用直接因果关系词。本题考查考生对文中隐含因果关系的把握。解答此类题目时需：一，定位需准确：一定要抓住题干关键词、知道题目问的是该人物的哪一具体行为；二，挖掘需深入：定位原文后，需深入挖掘原文中隐含的因果关系，要意识到因果关系不仅体现在逻辑副词、连词上（therefore, consequently, because），还可能体现在动词上（drive, prompt等），甚至是时间关系上（如作者强调的先后动作）；三，干扰排除需有理有据：查看选项是否与原文对应内容相悖，是否与本题所问逻辑不通。"
            "如本题，先根据题干关键词明确：本题考查“华盛顿释放奴隶”的原因，定位至第六段②句；随后发现该句所强调的时间先后中（had begun to... after...）暗含因果关系，［B］选项符合这一关系，故正确。而［A］、［C］、［D］不仅与题目所问华盛顿行为没有直接关系，且与题干无法建立通顺的逻辑关系，故排除。"
        )

with open(f2008, 'w', encoding='utf-8') as f:
    json.dump(d2008, f, ensure_ascii=False, indent=2)
print("Saved 2008 ky1.")

# 2. 2009 ky1 Text 2 (Q29-30)
f2009 = [f for f in glob.glob('public/data/exams/*.json') if '2009' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
with open(f2009, 'r', encoding='utf-8') as f:
    d2009 = json.load(f)

for q in d2009['questions']:
    so = q['sort_order']
    if so == 29:
        print("Calibrating 2009 ky1 Q29...")
        q['stem'] = "In the last paragraph, a problem commercial genetic testing faces is"
        q['explanation'] = (
            "［精准定位］末段②句指出，商业基因检测公司使用的数据库并未系统地收集数据，而是将多个研究项目的信息混杂在一起。［A］为正确选项。\n\n"
            "［命题解密］正确项［A］disorganized data collection 是第六段②句 don't rely on data collected systematically but rather lump together information 的同义替换。\n\n"
            "［错项排除］［B］将③句 have a lot of data from some regions and not others“数据地区来源不均衡”曲解为“数据重复（overlapping）”。"
            "［C］取段中 sample, compared, a lot of data 碎片化信息捏造出“样本比对过多（excessive sample comparison）”。"
            "［D］将④句“基因检测计算机程序申请专利且不接受外界评估（the computer programs... may be patented and not subject to... outside evaluation）”偷换为“缺乏专利评估（lack of patent evaluation）”。\n\n"
            "［技巧总结］本题形似考查综合性事实细节，实对段中既体现段落主旨又集词汇、语法难点于一身的段难句②句设题。解题时重在借助逻辑连接词、近义/同义复现、特殊句式结构等找到全段语义重心，并根据特殊句式或逻辑连接词推断难点词汇之意。具体思路：借助关联词 In addition 可将段落分为前后两部分；再借近义/同义复现 reference collections、Databases、DNA database 推知前部分落脚点在“数据库”，由此可基本确定数据库为主要批判点（重心即考点），从而锁定均关乎数据库的［A］disorganized（源自②句 don't rely on data collected systematically but rather lump together information from different research projects）、［B］overlapping（源于③句 have a lot of data from some regions and not others）；最后借助取舍结构 not A but rather B（不是A而是B）、from A and not B（来自A而不是B）可知两句语义重心在“信息收集不系统（也即 lump together 之意）、地域分布不均”问题上，只有［A］符合要求。"
        )
    elif so == 30:
        print("Calibrating 2009 ky1 Q30...")
        q['stem'] = "An appropriate title for the text is most likely to be"
        q['explanation'] = (
            "［精准定位］文首两段引出DNA检测；中间两段介绍DNA检测的用途及条件；末两段分析指出DNA检测的问题。［B］最切合文章。\n\n"
            "［命题解密］正确项［B］是对全篇全部内容的覆盖，又明确了文章论述的对象。\n\n"
            "［错项排除］［A］中 Fors 源自第三段 Among the most popular、the latest rage among passionate genealogists（最流行的有……、最近在狂热系谱学家中……）等内容而来，令学生可能产生作者在论述“DNA检测的优点”的错觉，而那只是对DNA检测的客观介绍，并非意指其“好的方面”。"
            "［C］将第二段“available without prescriptions、over the-counter（无需处方即可获得）”视为“DNA Testing Outside the Lab（实验室外的DNA检测）”，而商业基因检测并非就是实验室外的基因检测。"
            "［D］根据第五段 skeptical、false precision（怀疑的、伪精确性）等内容而来，但文意旨在“揭示DNA检测只能揭示一两位祖先信息，精确性有待提高”，而选项中 Lies（谎言）贬义色彩过重，而且该选项没有涵盖前四段对DNA testing的介绍。\n\n"
            "［技巧总结］命题点通常依全篇布局均匀分布，因此纵观其他四道题题干以窥视全篇主旨内容不失为解答文章主旨题（标题题）的捷径。具体思路为：纵观其他四题，前两题针对首四段，考查PTK（DNA检测一种）的特点、用途（availability、pricing, used to）；第三、四题针对末两段，考查DNA检测的弊端（fails, problem）；就此可见，文章对DNA检测的特点、用途及问题都做了诠释，［B］能涵盖这些信息。"
        )

with open(f2009, 'w', encoding='utf-8') as f:
    json.dump(d2009, f, ensure_ascii=False, indent=2)
print("Saved 2009 ky1.")

# 3. 2010 ky1 Part B (Q45)
f2010 = [f for f in glob.glob('public/data/exams/*.json') if '2010' in json.load(open(f, encoding='utf-8'))['exam']['title'] and json.load(open(f, encoding='utf-8'))['exam']['category_id'] == 'ky1'][0]
with open(f2010, 'r', encoding='utf-8') as f:
    d2010 = json.load(f)

for q in d2010['questions']:
    if q['sort_order'] == 45:
        print("Calibrating 2010 ky1 Q45...")
        expl = q['explanation']
        cut_idx = expl.find("（三） 借助路标词")
        if cut_idx != -1:
            q['explanation'] = expl[:cut_idx].strip()
            print("Successfully trimmed leaked Q42 from 2010 ky1 Q45.")

with open(f2010, 'w', encoding='utf-8') as f:
    json.dump(d2010, f, ensure_ascii=False, indent=2)
print("Saved 2010 ky1.")

print("\nRound 22 Calibrations applied successfully!")
