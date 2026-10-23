# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load old questions to get original UUIDs
with open(r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\baa66182-74ec-5a78-b2d2-077ffdcad9dc.json', encoding='utf-8') as f:
    old_data = json.load(f)

old_qs = old_data.get('questions', [])
exam_id = "baa66182-74ec-5a78-b2d2-077ffdcad9dc"

passage_ids = [
    "482c849e-0293-5209-b118-0cd4c91aadb6", # P0 Cloze
    "dc3497d7-d11a-5683-85b6-cc12f1b7eba3", # P1 Text 1
    "d2419589-e83f-5a1b-b3d0-3a82d1263fc4", # P2 Text 2
    "eed30545-c966-5cf7-96bc-731f2ab56649", # P3 Text 3
    "c6027e7b-c31e-5cc7-82a0-d71ff57c6931", # P4 Text 4
    "06091d69-1e9a-56f8-9520-8ebd89db8bbd"  # P5 Part B
]

# Cloze raw options & answers
cloze_data = [
    {"stem": "The court cannot [1] its legitimacy as guardian of the rule of law...", "opts": [("A", "emphasize"), ("B", "maintain"), ("C", "modify"), ("D", "recognize")], "ans": "B"},
    {"stem": "...guardian of the rule of law [2] justices behave like politicians.", "opts": [("A", "when"), ("B", "lest"), ("C", "before"), ("D", "unless")], "ans": "A"},
    {"stem": "Yet, in several instances, justices acted in ways that [3] the court's reputation...", "opts": [("A", "restored"), ("B", "weakened"), ("C", "established"), ("D", "eliminated")], "ans": "B"},
    {"stem": "...makes it less likely that the court's decisions will be [4] as impartial judgments.", "opts": [("A", "challenged"), ("B", "compromised"), ("C", "suspected"), ("D", "accepted")], "ans": "D"},
    {"stem": "Part of the problem is that the justices are not [5] by an ethics code.", "opts": [("A", "advanced"), ("B", "caught"), ("C", "bound"), ("D", "founded")], "ans": "C"},
    {"stem": "At the very least, the court should make itself [6] to the code of conduct...", "opts": [("A", "resistant (to)"), ("B", "subject (to)"), ("C", "immune (to)"), ("D", "prone (to)")], "ans": "B"},
    {"stem": "...to the code of conduct that [7] to the rest of the federal judiciary.", "opts": [("A", "resorts (to)"), ("B", "sticks (to)"), ("C", "leads (to)"), ("D", "applies (to)")], "ans": "D"},
    {"stem": "This and other similar cases [8] the question of whether there is still a line...", "opts": [("A", "evade"), ("B", "raise"), ("C", "deny"), ("D", "settle")], "ans": "B"},
    {"stem": "...whether there is still a [9] between the court and politics.", "opts": [("A", "line"), ("B", "barrier"), ("C", "similarity"), ("D", "conflict")], "ans": "A"},
    {"stem": "The framers of the Constitution envisioned law [10] having authority apart from politics.", "opts": [("A", "by"), ("B", "as"), ("C", "through"), ("D", "towards")], "ans": "B"},
    {"stem": "They gave justices permanent positions [11] they would be free to...", "opts": [("A", "so"), ("B", "since"), ("C", "provided"), ("D", "though")], "ans": "A"},
    {"stem": "...they would be free to [12] those in power...", "opts": [("A", "serve"), ("B", "satisfy"), ("C", "upset"), ("D", "replace")], "ans": "C"},
    {"stem": "...and have no need to [13] political support.", "opts": [("A", "confirm"), ("B", "express"), ("C", "cultivate"), ("D", "offer")], "ans": "C"},
    {"stem": "It was designed [14] to separate the two.", "opts": [("A", "guarded"), ("B", "followed"), ("C", "studied"), ("D", "tied")], "ans": "D"},
    {"stem": "...results from choices between different [15] of liberty and property.", "opts": [("A", "concepts"), ("B", "theories"), ("C", "divisions"), ("D", "conventions")], "ans": "A"},
    {"stem": "...and allows politics to [16] its judgment, it loses its authority apart from politics.", "opts": [("A", "excludes"), ("B", "questions"), ("C", "shapes"), ("D", "controls")], "ans": "C"},
    {"stem": "...easier for decisions with which people disagree to be [17] as political rather than judicial.", "opts": [("A", "dismissed"), ("B", "released"), ("C", "ranked"), ("D", "distorted")], "ans": "A"},
    {"stem": "The justices must [18] doubts about the court's legitimacy...", "opts": [("A", "suppress"), ("B", "exploit"), ("C", "address"), ("D", "ignore")], "ans": "C"},
    {"stem": "...by making themselves [19] to the code of conduct.", "opts": [("A", "accessible"), ("B", "amiable"), ("C", "agreeable"), ("D", "accountable")], "ans": "D"},
    {"stem": "...seen as separate from politics and, [20], convincing as law.", "opts": [("A", "by all means"), ("B", "at all costs"), ("C", "in a word"), ("D", "as a result")], "ans": "D"},
]

# Reading Q21-Q40 data
reading_data = [
    # Text 1: Q21-Q25
    {
        "stem": "According to the first paragraph, peer pressure often emerges as ________.",
        "opts": [
            ("A", "a supplement to the social cure"),
            ("B", "a stimulus to group dynamics"),
            ("C", "an obstacle to social progress"),
            ("D", "a cause of undesirable behaviors")
        ],
        "ans": "D",
        "expl": (
            "【精准定位】第一段③句明确指出：同侪压力通常会导致不好的结果，如酗酒、吸毒、轻率性行为等（It usually leads to no good — drinking, drugs and casual sex）。因此［D］选项符合文意。\n\n"
            "【命题解密】题干与正确项［D］是对③句的同义改写：usually对应often，leads to对应emerges as a cause of，no good（drinking, drugs and casual sex）对应undesirable behaviors。\n\n"
            "【错项排除】［A］将④句through所传递“同侪压力是社会治疗所借助的力量”曲解为“同侪压力是社会治疗的补充（supplement）”；［B］将④句碎片信息be a positive force与group dynamics杂糅并曲解为“同侪压力刺激群体互动”，而群体互动实为同侪压力的另一种表述；［C］将④句help individuals... and possibly the world反向曲解为“同侪压力是社会进步的障碍（obstacle）”。"
        )
    },
    {
        "stem": "Rosenberg holds that public-health advocates should ________.",
        "opts": [
            ("A", "recruit professional advertisers"),
            ("B", "learn from advertisers' experience"),
            ("C", "stay away from commercial advertisers"),
            ("D", "recognize the limitations of advertisements")
        ],
        "ans": "B",
        "expl": (
            "【精准定位】第三段末句介绍罗森伯格针对公共健康运动倡导者提出的建议：应该向善于运用同侪压力的广告人学习（Rosenberg argues convincingly that public-health advocates ought to take a page from advertisers, so skilled at applying peer pressure），因此［B］选项正确。\n\n"
            "【命题解密】题干与正确项［B］是对第三段④句的同义改写：take a page from sb意为“向某人学习”，同义替换learn from advertisers' experience。\n\n"
            "【错项排除】［A］误将take a page from advertisers（向广告人学习）过度推断为recruit professional advertisers（招募职业广告人以为己用）；［C］、［D］均误将段中用于批判公共健康运动倡导者的信息lameness / fail to mobilize / a seriously flawed understanding强加于广告人，推出“应该远离广告人”或“广告具有局限性”，与文意背道而驰。"
        )
    },
    {
        "stem": "In the author's view, Rosenberg's book fails to ________.",
        "opts": [
            ("A", "adequately probe social and biological factors"),
            ("B", "effectively evade the flaws of the social cure"),
            ("C", "illustrate the functions of state funding"),
            ("D", "produce a long-lasting social effect")
        ],
        "ans": "A",
        "expl": (
            "【精准定位】第四段②句明确指出：《加入俱乐部》一书无关细节过多，却没能充分探究使同侪压力发挥如此强大作用的社会和生物机制（Join the Club is filled with too much irrelevant detail and not enough exploration of the social and biological mechanisms that make peer pressure so powerful）。故［A］正确。\n\n"
            "【命题解密】题干与正确项［A］是对第四段②句的同义改写：Rosenberg's book对应Join the Club，fails to adequately probe对应not enough exploration of。\n\n"
            "【错项排除】［B］利用③句flaw of the social cure与it doesn't work very well捏造出“未能避免社会治疗的缺陷”，而文意实为该书暴露了社会治疗的缺陷；［C］利用④句说明社会治疗不能持久的事例“州政府资金一削减，禁烟运动就失效”中的state funding捏造出“未能说明政府基金的功能”；［D］将③句说明社会治疗未能产生长期效果（it doesn't work very well for very long）曲解为该书未能产生长期社会效应。"
        )
    },
    {
        "stem": "Paragraph 5 shows that our imitation of behaviors ________.",
        "opts": [
            ("A", "is harmful to our networks of friends"),
            ("B", "will mislead behavioral studies"),
            ("C", "occurs without our realizing it"),
            ("D", "can produce negative health habits")
        ],
        "ans": "C",
        "expl": (
            "【精准定位】第五段末句指出：这是同侪压力的一种隐秘形式，我们在不知不觉中模仿我们每天看到的行为（This is a subtle form of peer pressure: we unconsciously imitate the behavior we see every day）。由此可知［C］选项符合文意。\n\n"
            "【命题解密】题干our imitation of behaviors对应原文imitate the behavior we see every day，正确项［C］occurs without our realizing it同义改写原文unconsciously。\n\n"
            "【错项排除】［A］根据②句部分信息negative ones spread through networks of friends过度推断出“对朋友圈有害”，忽视了前半句positive health habits；［B］将①②句碎片信息exert enormous influence与emerging body of research杂糅为“会误导行为研究”；［D］将②句“我们会模仿朋友圈传播的好习惯与坏习惯”因果颠倒为“模仿行为会产生不良健康习惯”。"
        )
    },
    {
        "stem": "The author suggests in the last paragraph that the effect of peer pressure is ________.",
        "opts": [
            ("A", "harmful"),
            ("B", "desirable"),
            ("C", "profound"),
            ("D", "questionable")
        ],
        "ans": "D",
        "expl": (
            "【精准定位】最后一段①句首先提出质疑：专家和官僚们能否成功挑选我们的同伴群体并将其引导至道德方向还远不能确定（Far less certain, however, is how successfully experts and bureaucrats can select...）；②③句通过老师调换捣蛋学生座位的类比说明该策略从未真正奏效（The tactic never really works）；④句指出从外部人为调控的根本问题所在：现实中我们坚持自己选择朋友。由此可见，作者对同侪压力在社会治疗中的效果持怀疑态度，［D］正确。\n\n"
            "【命题解密】正确项［D］questionable是对第六段中far less certain、never really works、the problem with a social cure等表达所体现的作者怀疑态度的精准提炼。\n\n"
            "【错项排除】［A］利用④句the problem捏造出“同侪压力本身是有害的”，而原文旨在说明外部调控存在问题；［B］利用①句virtuous捏造“令人满意的”，与作者全段批驳基调相悖；［C］利用第五段①句exert enormous influence过度引申出“深刻的”，偏离了末段对人为调控效果的质疑主旨。"
        )
    },

    # Text 2: Q26-Q30
    {
        "stem": "The phrase \"reneging on\" (Line 3, Para. 1) is closest in meaning to ________.",
        "opts": [
            ("A", "condemning"),
            ("B", "reaffirming"),
            ("C", "dishonoring"),
            ("D", "securing")
        ],
        "ans": "C",
        "expl": (
            "【精准定位】由第一段首两句可知：协议就是协议，但Entergy公司显然是个例外（A deal is a deal — except, apparently, when Entergy is involved）。该公司宣布它将reneging on一项遵守该州严格核法规的长期承诺，激起了公众合理的愤怒。由此推知，该公司做出了违背承诺的行为，故该短语意为“违背，背信”，［C］dishonoring正确。\n\n"
            "【命题解密】正确项［C］dishonoring（不尊重，不履行，违背）是基于首句A deal is a deal以及provoked justified outrage对reneging on所做的精准同义替换。\n\n"
            "【错项排除】［A］condemning谴责；［B］reaffirming重申；［D］securing获得，确保。均与上下文关于“毁约、背弃承诺”的语境不符。"
        )
    },
    {
        "stem": "By entering into the 2002 agreement, Entergy intended to ________.",
        "opts": [
            ("A", "obtain protection from Vermont regulators"),
            ("B", "seek favor from the federal legislature"),
            ("C", "acquire an extension of its business license"),
            ("D", "get permission to purchase a power plant")
        ],
        "ans": "D",
        "expl": (
            "【精准定位】第三段①句明确指出：这一冲突自2002年起就已表面化，当时该企业收购了佛蒙特扬基核电站，并与州监管机构达成协议（when the corporation bought Vermont Yankee and negotiated an agreement with state regulators to keep the products moving）。Entergy公司签订该协议的目的是为了获得收购该核电站的许可，故［D］正确。\n\n"
            "【命题解密】正确项［D］get permission to purchase a power plant是对第三段①句bought Vermont Yankee and negotiated an agreement with state regulators的合理概括。\n\n"
            "【错项排除】［A］将达成协议曲解为寻求州监管机构的“保护”；［B］将州议会批准曲解为寻求“联邦立法机构的支持”；［C］将2002年购买协议与后来2012年寻求许可证延期混淆，属于张冠李戴。"
        )
    },
    {
        "stem": "According to Paragraph 4, Entergy seems to have problems with its ________.",
        "opts": [
            ("A", "managerial practices"),
            ("B", "technical innovativeness"),
            ("C", "financial goals"),
            ("D", "business vision")
        ],
        "ans": "A",
        "expl": (
            "【精准定位】第四段②句明确指出：接二连三发生的事故，包括2007年冷却塔部分倒塌以及2010年发现地下氚泄漏，引发了对该核电站安全性以及Entergy公司管理水平的严重质疑（raised serious questions about the plant's safety and Entergy's management）。故［A］正确。\n\n"
            "【命题解密】正确项［A］managerial practices是对第四段②句Entergy's management的同义替换。\n\n"
            "【错项排除】［B］将冷却塔倒塌和管道泄漏等安全与管理事故曲解为“技术创新”问题；［C］“财务目标”和［D］“商业远见”在文中均未提及，纯属无中生有的干扰项。"
        )
    },
    {
        "stem": "In the author's view, the Vermont case will test ________.",
        "opts": [
            ("A", "Entergy's capacity to fulfill all its promises"),
            ("B", "the nature of states' patchwork regulations"),
            ("C", "the federal authority over nuclear issues"),
            ("D", "the limits of states' power over nuclear issues")
        ],
        "ans": "D",
        "expl": (
            "【精准定位】第五段②句指出：法律学者认为该案将对各州核监管权限提供一个测试性先例；③④句作者进一步指出：明确各州权限虽会引起对拼凑法规的合理担忧，但Entergy公司的毁约行为使得联邦法院不得不去界定州级核监管权限（the limits of state regulatory power）。故［D］正确。\n\n"
            "【命题解密】正确项［D］the limits of states' power over nuclear issues对应第五段末句the limits of state regulatory power。\n\n"
            "【错项排除】［A］将测试州监管权限偷换为Entergy公司履行承诺的能力；［B］将担忧州补丁法规偷换为检验其“性质”；［C］将州政府在核能问题上的权力界限曲解为联邦权力，主体混淆。"
        )
    },
    {
        "stem": "It can be inferred from the last paragraph that ________.",
        "opts": [
            ("A", "Entergy's business elsewhere might be affected"),
            ("B", "the authority of the NRC will be defied"),
            ("C", "Entergy will withdraw its Plymouth application"),
            ("D", "Vermont's reputation might be damaged")
        ],
        "ans": "A",
        "expl": (
            "【精准定位】最后一段末句明确指出：由于Entergy在整个新英格兰地区销售核电，它很可能会发现，佛蒙特州绝非唯一一个把Entergy承诺的信誉价值牢记在心的州（As Entergy sells its nuclear power across New England, it will likely find that Vermont is not the only state that will keep in mind what promises from Entergy are worth）。这暗示其背信弃义的行为将影响其在其他地区的业务，故［A］正确。\n\n"
            "【命题解密】正确项［A］是对末句“佛蒙特州绝非唯一一个记住其承诺价值的州”的合理推论引申。\n\n"
            "【错项排除】［B］将NRC会记住Entergy的信誉曲解为NRC的权威将被藐视；［C］撤回申请与［D］佛蒙特州名誉受损均与原文事实相反，名誉受损的是Entergy公司而非佛蒙特州。"
        )
    },

    # Text 3: Q31-Q35
    {
        "stem": "According to the first paragraph, the process of discovery is characterized by its ________.",
        "opts": [
            ("A", "uncertainty and complexity"),
            ("B", "misconception and deceptiveness"),
            ("C", "logicality and objectivity"),
            ("D", "systematicness and regularity")
        ],
        "ans": "A",
        "expl": (
            "【精准定位】第一段②句明确指出：在日常科学实践中，科学发现往往遵循一条模糊且复杂的路径（But in the everyday practice of science, discovery frequently follows an ambiguous and complicated route）。因此［A］正确。\n\n"
            "【命题解密】题干the process of discovery与正确项［A］uncertainty and complexity分别同义替换原文discovery follows an ambiguous and complicated route。\n\n"
            "【错项排除】［B］将影响科研过程的主观因素（先验知识、误解自欺）曲解为科学发现过程本身的特征；［C］将理想状态下的特点（objective）偷换为现实状态的特征；［D］系统性与规律性属于常识干扰，背离第一段强调的复杂性与模糊性。"
        )
    },
    {
        "stem": "It can be inferred from Paragraph 2 that credibility process requires ________.",
        "opts": [
            ("A", "strict inspection"),
            ("B", "shared efforts"),
            ("C", "individual wisdom"),
            ("D", "persistent innovation")
        ],
        "ans": "B",
        "expl": (
            "【精准定位】第二段③句指出：科学发现声明转变为成熟发现需要经过集体的审查与认可（takes collective scrutiny and acceptance）；④句进而指出：单个研究者的“我、此时、此地”由此转变为科学界的“任何人、任何时间、任何地点”。由此可推知取信过程需要集体的共同努力，［B］正确。\n\n"
            "【命题解密】正确项［B］shared efforts对应第三句collective scrutiny and acceptance以及第四句community's anyone, anywhere, anytime。\n\n"
            "【错项排除】［A］将集体审查狭隘化为严格的单向检查；［C］强调“个人智慧”，与原文反复强调的集体行动（collective scrutiny/community）截然相反；［D］“持续创新”在文中未体现。"
        )
    },
    {
        "stem": "Paragraph 3 shows that a discovery claim becomes credible after it ________.",
        "opts": [
            ("A", "has attracted the attention of the general public"),
            ("B", "has been examined by the scientific community"),
            ("C", "has received recognition from editors and reviewers"),
            ("D", "has been frequently quoted by peer scientists")
        ],
        "ans": "B",
        "expl": (
            "【精准定位】第三段指出：发现声明在得到证实之前不能被作为事实接受，这通常需要其他研究人员复制结果，声明在科学共同体中历经检验、修正、测试其价值并明确其界限（a discovery claim works its way through the community, the idea is revised, its value tested, and its boundaries defined）。故［B］正确。\n\n"
            "【命题解密】正确项［B］has been examined by the scientific community是对第三段全段所述同行重复实验、修正和检验过程的全面概括。\n\n"
            "【错项排除】［A］吸引公众注意力并非确立可信度的必要条件；［C］将整个科学界同行的检验偷换为期刊编辑和审稿人个别环节；［D］被同行引用在第三段中并未作为可信度成立的判定标准。"
        )
    },
    {
        "stem": "Albert Szent-Gyorgyi would most likely agree that ________.",
        "opts": [
            ("A", "scientific claims will survive challenges"),
            ("B", "discoveries today inspire future research"),
            ("C", "efforts to make discoveries are justified"),
            ("D", "scientific work calls for a critical mind")
        ],
        "ans": "D",
        "expl": (
            "【精准定位】第五段引述Albert Szent-Gyorgyi的名言：“科学发现就是见众之所见，思无人之所思”（Discovery consists of seeing what everybody has seen and thinking what nobody has thought）。这表明科学工作需要不落俗套、独立思考与批判性思维，故［D］正确。\n\n"
            "【命题解密】正确项［D］scientific work calls for a critical mind是对引语thinking what nobody has thought的深度内涵概括。\n\n"
            "【错项排除】［A］、［B］、［C］脱离了Albert Szent-Gyorgyi具体引语关于思维独创性与批判性的核心内涵，属于偏离引语主旨的泛泛之论。"
        )
    },
    {
        "stem": "Which of the following would be the best title of the text?",
        "opts": [
            ("A", "Novelty as an Engine of Scientific Development."),
            ("B", "Collective Scrutiny in Scientific Discovery."),
            ("C", "Evolution of Credibility in Doing Science."),
            ("D", "Challenge to Credibility at the Gate to Science.")
        ],
        "ans": "C",
        "expl": (
            "【精准定位】文章首段指出科学发现充满主观复杂性；第二段引出核心概念“取信过程”（credibility process）；第三段阐述发现声明在学术共同体中经历的修改与检验；第四段剖析取信过程中的两大悖论；末段总结可信度如何在共同体协作中最终确立。全文主线始终围绕“科学研究中可信度的演进与确立”，故［C］正确。\n\n"
            "【命题解密】正确项［C］Evolution of Credibility in Doing Science涵盖了全文的核心主题词credibility与发展过程evolution。\n\n"
            "【错项排除】［A］以偏概全，误将新颖性作为全文主旨；［B］集体审查仅是取信过程中的一个手段，不足以概括全文；［D］中心词落于“挑战”，脱离了阐释科学如何克服主观因素确立客观可信度的行文主轴。"
        )
    },

    # Text 4: Q36-Q40
    {
        "stem": "It can be learned from the first paragraph that ________.",
        "opts": [
            ("A", "Teamsters still have a large body of members"),
            ("B", "Jimmy Hoffa used to work as a civil servant"),
            ("C", "unions have enlarged their public-sector membership"),
            ("D", "the government has improved its relationship with unionists")
        ],
        "ans": "C",
        "expl": (
            "【精准定位】第一段指出：1960年美国政府工作人员中只有十分之一加入工会，而如今达到36%；2009年公共部门工会会员人数超过了私营部门；英国一半以上的公共部门人员也加入了工会。这表明工会极大地扩大了其在公共部门的会员人数，故［C］正确。\n\n"
            "【命题解密】正确项［C］是对第一段数据对比（10%到36%，公共部门超过私营部门）的概括性同义替换。\n\n"
            "【错项排除】［A］文中仅提及Teamsters在1960年全盛时期的情况，无法推知现在的会员状况；［B］对首句虚拟语气断章取义，Jimmy Hoffa并非公务员；［D］“政府改善了与工会成员的关系”与文意无关。"
        )
    },
    {
        "stem": "Which of the following is true of Paragraph 2?",
        "opts": [
            ("A", "Public-sector unions are prudent in taking actions."),
            ("B", "Education is required for public-sector union membership."),
            ("C", "Labor Party has long been fighting against public-sector unions."),
            ("D", "Public-sector unions seldom get in trouble for their actions.")
        ],
        "ans": "D",
        "expl": (
            "【精准定位】第二段②句指出公共部门工会壮大的第一个原因：他们可以举行罢工使全国运转瘫痪而无须承担太多后果（they can shut things down without suffering much in the way of consequences）。由此可知，他们很少因为自己的行动而陷入麻烦，故［D］正确。\n\n"
            "【命题解密】正确项［D］seldom get in trouble for their actions同义改写原文without suffering much in the way of consequences。\n\n"
            "【错项排除】［A］称其行动谨慎，与可以随时罢工瘫痪运转相反；［B］将四分之一拥有大学学位曲解为工会会员资格有教育硬性要求；［C］将工党与工会渊源久远且领袖得益于工会选票曲解为工党长期与工会斗争，完全颠倒黑白。"
        )
    },
    {
        "stem": "It can be learned from Paragraph 4 that the income in the state sector is ________.",
        "opts": [
            ("A", "illegally secured"),
            ("B", "indirectly augmented"),
            ("C", "excessively increased"),
            ("D", "fairly adjusted")
        ],
        "ans": "B",
        "expl": (
            "【精准定位】第四段③句指出：政治家们反复采取变相延期给付的方式制定公共部门薪酬协议，保持工资涨幅微弱，但增加假期、尤其是原本就已经非常优厚的养老金（keeping the pay increases modest but adding to holidays and especially pensions that are already generous）。这表明公共部门的收入通过隐蔽、间接的方式得到了增加，故［B］正确。\n\n"
            "【命题解密】题干与正确项［B］indirectly augmented是对原文backloaded pay deals以及增加假期与养老金福利的精准概括。\n\n"
            "【错项排除】［A］政治家与工会达成的协议并非“非法获得”；［C］工资涨幅保持modest（低微），并非过度增加；［D］这种变相给付加重了纳税人负担并拖累财政，并非“公平调整”。"
        )
    },
    {
        "stem": "The example of the unions in Wisconsin shows that unions ________.",
        "opts": [
            ("A", "often run against the current political system"),
            ("B", "can change people's political attitudes"),
            ("C", "may be a barrier to public-sector reforms"),
            ("D", "are dominant in the government")
        ],
        "ans": "C",
        "expl": (
            "【精准定位】第六段承接第五段首句主旨展开：公共部门改革遭到了强烈反对（Reform has been vigorously opposed）；随后在第六段举出威斯康辛州的工会集结数以千计的支持者反对强硬改革派州长Scott Walker的典型事例。作者借此例说明工会成为了公共部门改革的巨大阻碍，故［C］正确。\n\n"
            "【命题解密】正确项［C］may be a barrier to public-sector reforms是第五段主旨句Reform has been vigorously opposed的同义转述，准确指明了事例论证的目的。\n\n"
            "【错项排除】［A］工会反对的是试图削减其特权的改革者，以维护现存体制，而非反对政治体制本身；［B］“改变人们的政治态度”与［D］“在政府中占据主导”均偏离了用以说明阻碍改革的事例核心。"
        )
    },
    {
        "stem": "John Donahue's attitude towards the public-sector system is one of ________.",
        "opts": [
            ("A", "disapproval"),
            ("B", "appreciation"),
            ("C", "tolerance"),
            ("D", "indifference")
        ],
        "ans": "A",
        "expl": (
            "【精准定位】末段引述哈佛大学肯尼迪学院John Donahue的观点：西方行政体制的文化规范适合那些追求安稳的人，但对优秀人才不利（suit those who want to stay put but is bad for high achievers）；一个不能奖励优秀人才的公共部门体制对美国来说可能是个大得多的问题。由此可见其对现行体制持强烈的批评否定态度，故［A］正确。\n\n"
            "【命题解密】正确项［A］disapproval（不赞同，反对）精准概括了专家言论中的is bad for high achievers以及a much bigger problem。\n\n"
            "【错项排除】［B］appreciation欣赏；［C］tolerance容忍；［D］indifference漠不关心。均与专家鲜明的批判态度不符。"
        )
    }
]

# Part B Q41-Q45 data
pb_options = [
    ("A", "Of course, it is precisely these superfluous things that define human culture and ultimately what it is to be human. Downloading and consuming culture requires great skills, but failing to move beyond downloading is to strip oneself of a defining constituent of humanity."),
    ("B", "Applications like tumblr. com, which allow users to combine pictures, words and other media in creative ways and then share them, have the potential to add stickiness by amusing, entertaining and enlightening others."),
    ("C", "Not only did they develop such a device but by the turn of the millennium they had also managed to embed it in a worldwide system accessed by billions of people every day."),
    ("D", "This is because the networked computer has sparked a secret war between downloading and uploading — between passive consumption and active creation — whose outcome will shape our collective future in ways we can only begin to imagine."),
    ("E", "The challenge the computer mounts to television thus bears little similarity to one format being replaced by another in the manner of record players being replaced by CD players."),
    ("F", "One reason for the persistence of this pyramid of production is that for the past half-century, much of the world's media culture has been defined by a single medium — television — and television is defined by downloading."),
    ("G", "The networked computer offers the first chance in 50 years to reverse that flow, to encourage thoughtful downloading and, even more importantly, meaningful uploading.")
]

pb_data = [
    {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (41):",
        "ans": "C",
        "expl": (
            "【考点透析】本题考查代词指代、同义复现与上下文时空逻辑承接。\n\n"
            "【空格推测】空格上文第二段讲述20世纪后半叶众多先驱合力发明个人电脑（create a fabulous machine）；下文第三段提及联网电脑已连接入网。推测空格内容承接电脑的发明并过渡至全球互联系统。\n\n"
            "【答案敲定】［C］项中的Not only did they develop such a device承接上文a fabulous machine，they回指上文a collection of geniuses, warriors, entrepreneurs and visionaries；后半句embed it in a worldwide system accessed by billions of people则顺理成章启下引入互联网，时间状语by the turn of the millennium与上文20th century时序紧密吻合。故［C］正确。"
        )
    },
    {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (42):",
        "ans": "D",
        "expl": (
            "【考点透析】本题考查因果逻辑衔接与篇章核心概念引入。\n\n"
            "【空格推测】空格上文指出电脑的真正意义仍在逐步显现（the true significance of the computer is still emerging）；推测空格内容解释其真正意义为何仍在显现。\n\n"
            "【答案敲定】［D］项以This is because开启因果解释，指出联网电脑引发了下载与上传、被动消费与主动创造之间的“隐秘战争”，其结果将塑造我们的未来，与上文“真正意义仍在显现”因果关系严密契合。故［D］正确。"
        )
    },
    {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (43):",
        "ans": "A",
        "expl": (
            "【考点透析】本题考查指示代词回指与语义反向承接。\n\n"
            "【空格推测】第五段讲述人类与动物的区别在于创造文化并与他人分享；推测空格内容承接这一人类独有的创造性特质并做进一步阐发。\n\n"
            "【答案敲定】［A］项首句以强调句指出正是这些额外事物定义了人类文化和人性（these superfluous things that define human culture and ultimately what it is to be human），these superfluous things准确回指上文人类创造的音乐、绘画、书籍等精神财富；第二句指出如果不能超越下载模式就等于剥夺了人性的核心构成，过渡自然顺畅。故［A］正确。"
        )
    },
    {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (44):",
        "ans": "F",
        "expl": (
            "【考点透析】本题考查词汇复现与段际因果过渡。\n\n"
            "【空格推测】第六段指出大部分人依然受困于下载模式，存在着一个顶层极少人上传、底层绝大多数人消费的“生产金字塔”（a pyramid of production remains）；推测空格内容解释该金字塔长期存在的原因。\n\n"
            "【答案敲定】［F］项首句直接以One reason for the persistence of this pyramid of production回应上文生产金字塔的成因，指出半个世纪以来世界媒体文化一直由电视主导，而电视的本质就是下载，因果衔接完美，并自然引出下文第七段对电视特性的论述。故［F］正确。"
        )
    },
    {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (45):",
        "ans": "G",
        "expl": (
            "【考点透析】本题考查词汇回指、逻辑对比与设问启下。\n\n"
            "【空格推测】第七段指出电视是一个单向龙头，信息单向流出（one-way tap: you open the valve and information flows out）；第八段紧接着设问“何为有意义的上传？”。推测空格内容扭转这种单向流动并引出“有意义的上传”。\n\n"
            "【答案敲定】［G］项指出联网电脑提供了50年来第一次逆转这种流向的机会（reverse that flow回指上文information flows out），更重要的是鼓励“有意义的上传”（meaningful uploading），精准引出第八段首句对meaningful uploading的设问与定义。故［G］正确。"
        )
    }
]

questions = []

# Build Q1-Q20 (Cloze)
for i in range(20):
    cd = cloze_data[i]
    old_q = old_qs[i] if i < len(old_qs) else {}
    q_id = old_q.get('id', f"q_{i+1}")
    opts = [{"key": k, "text": t, "value": k} for k, t in cd["opts"]]
    # Build clean explanation from old explanation if available
    old_expl = old_q.get('explanation') or ""
    clean_expl = old_expl.strip() if len(old_expl.strip()) > 50 else f"本题考查完型填空上下文逻辑与词义辨析，正确答案为［{cd['ans']}］。"
    questions.append({
        "id": q_id,
        "exam_id": exam_id,
        "question_number": i + 1,
        "passage_id": passage_ids[0],
        "stem": f"Choose the best option for blank [{i+1}] in the passage:",
        "options": opts,
        "correct_answer": cd["ans"],
        "points": 0.5,
        "explanation": clean_expl
    })

# Build Q21-Q40 (Reading)
for i in range(20):
    rd = reading_data[i]
    q_num = 21 + i
    old_idx = 20 + i
    old_q = old_qs[old_idx] if old_idx < len(old_qs) else {}
    q_id = old_q.get('id', f"q_{q_num}")
    p_idx = 1 + (i // 5) # 0-4 -> 1, 5-9 -> 2, 10-14 -> 3, 15-19 -> 4
    opts = [{"key": k, "text": t, "value": k} for k, t in rd["opts"]]
    questions.append({
        "id": q_id,
        "exam_id": exam_id,
        "question_number": q_num,
        "passage_id": passage_ids[p_idx],
        "stem": rd["stem"],
        "options": opts,
        "correct_answer": rd["ans"],
        "points": 2.0,
        "explanation": rd["expl"]
    })

# Build Q41-Q45 (Part B)
pb_opts_formatted = [{"key": k, "text": t, "value": k} for k, t in pb_options]
for i in range(5):
    pd = pb_data[i]
    q_num = 41 + i
    old_idx = 40 + i
    old_q = old_qs[old_idx] if old_idx < len(old_qs) else {}
    q_id = old_q.get('id', f"q_{q_num}")
    questions.append({
        "id": q_id,
        "exam_id": exam_id,
        "question_number": q_num,
        "passage_id": passage_ids[5],
        "stem": pd["stem"],
        "options": pb_opts_formatted,
        "correct_answer": pd["ans"],
        "points": 2.0,
        "explanation": pd["expl"]
    })

print(f"Generated {len(questions)} questions.")

with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\2012_ky1_questions_gold.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved to scripts/2012_ky1_questions_gold.json")
