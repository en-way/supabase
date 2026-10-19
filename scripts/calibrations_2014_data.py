import json
import re

# Comprehensive 2014 ky1 Reading Comprehension (Q21-Q40) Calibration Data
# Sourced directly from 2014黄皮书真题解析（英语一）.pdf

calibrations_2014 = {
    21: {
        "stem": "George Osborne's scheme was intended to ________.",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "encourage jobseekers' active engagement in job seeking", "value": "encourage jobseekers' active engagement in job seeking"},
            {"key": "B", "text": "provide the unemployed with easier access to benefits", "value": "provide the unemployed with easier access to benefits"},
            {"key": "C", "text": "guarantee jobseekers' legitimate right to benefits", "value": "guarantee jobseekers' legitimate right to benefits"},
            {"key": "D", "text": "motivate the unemployed to report voluntarily", "value": "motivate the unemployed to report voluntarily"}
        ],
        "explanation": """［精准定位］首段①句指出计划目的：使生活更好，并降低依赖。②句说明计划内容：失业者须带简历到求职中心、注册网上求职、并开始寻找工作，才有资格领取失业金；且之后须每周报到一次。结合两句可知，计划旨在鼓励失业者积极寻找工作、而不是依赖失业金，［A］正确。
［命题解密］正确项［A］结合②句计划内容，明确①句 In order to "change lives for the better" and reduce "dependency" 所述目的。
［错项排除］［B］对①句 change lives for the better 断章取义，由②句可知：获得救济是“更难”、而非“更易”。［C］对②句 Only if... will they be eligible for benefit... 反向干扰：该计划是在“限制”、而不是“保障”失业者领取救济金的权利。［D］用②句 they should report 干扰，但这属于计划细节、不能体现整体目的，且文中是“强行规定（they should）”、而非“鼓励自愿（motivate... voluntarily）”。
［技巧总结］本题考查“新政目的”，且直接定位信息为抽象概述，解题时需结合新政的具体规定、针对情形等加以理解把握，切忌断章取义。具体来看，答题时根据题干 was intended to 可直接锁定①句 In order to，并确定 change lives for the better and reduce dependency 为正确项来源。但由于该表述抽象概括，所以应结合②句“规定详述”加以理解，确定［A］正确。排除对直接定位信息断章取义的［B］，错误理解特殊句式（倒装条件句）的［C］，以及将“细节内容”当“整体目的”、且扭曲文意的［D］。"""
    },
    22: {
        "stem": 'The phrase "to sign on" (Line 2, Para. 2) most probably means ________.',
        "correct_answer": "C",
        "options": [
            {"key": "A", "text": "to check on the availability of jobs at the jobcentre", "value": "to check on the availability of jobs at the jobcentre"},
            {"key": "B", "text": "to accept the government's restrictions on the allowance", "value": "to accept the government's restrictions on the allowance"},
            {"key": "C", "text": "to register for an allowance from the government", "value": "to register for an allowance from the government"},
            {"key": "D", "text": "to attend a governmental job-training program", "value": "to attend a governmental job-training program"}
        ],
        "explanation": """［精准定位］由所考词所在句“失业最初几天应该用于找工作，而不是指望 sign on”可知：sign on 是“找工作”的对立面。再结合上句“求职者需要经过七天的等待期才能申请津贴”及下句“之所以这样做，是要帮助人们远离救济”，可确定 sign on 指“登记领取政府津贴”，［C］正确。
［命题解密］正确项［C］体现了 sign on 和 looking for work、stay off benefits、get into work faster 之间的对立，以及与 the jobseeker's allowance 的同向。
［错项排除］［A］为第一段②句 they should report weekly 暗示信息，但这和“找工作”为同向关系、而非对立关系。［B］ the government's restrictions on the allowance 与第二段②句同义，但“接受这种限制（accept...）”无法和“找工作”构成对立。［D］ a governmental job-training program 源自第二段④句 help those on benefits get into work faster，但选项无法和 the jobseeker's allowance 建立联系。
［技巧总结］本题就“涉及复杂关系的内容（第二段）”命制词义推断题，解题关键是通过多条线索（因果、转折标记，取舍结构、语义逻辑等）找到上下文中的同义/近义/上下义关系。具体看本题：一，借助 should be spent..., not... 可判断：looking to sign on 和 looking for work 为对立关系。二，借助②③句 seven-day 和 Those first few days 的同指关系可判断：looking to sign on 和 the jobseeker's allowance 直接相关。三，借助③④句间紧密逻辑可知 stay off benefits / get into work faster 和 looking for work 同向，和 looking to sign on 反向。综合三条线索可知［C］正确。"""
    },
    23: {
        "stem": "What prompted the chancellor to develop his scheme?",
        "correct_answer": "D",
        "options": [
            {"key": "A", "text": "A desire to secure a better life for all.", "value": "A desire to secure a better life for all."},
            {"key": "B", "text": "An eagerness to protect the unemployed.", "value": "An eagerness to protect the unemployed."},
            {"key": "C", "text": "An urge to be generous to the claimants.", "value": "An urge to be generous to the claimants."},
            {"key": "D", "text": "A passion to ensure fairness for taxpayers.", "value": "A passion to ensure fairness for taxpayers."}
        ],
        "explanation": """［精准定位］根据题干设问直接定位至第二段⑧句（What motivated him...）。该句指出，激励奥斯本制定其计划的是对“基本公平”的热情：保护纳税者，控制开支，确保只有最应资助的申请者才能领到补贴。可见，［D］符合文意。
［命题解密］正确项是对第二段⑧句的概括：passion 近义替换 zeal，ensure fairness for taxpayers 概括 "fundamental fairness" — protecting the taxpayer...。
［错项排除］［A］源自第二段⑦句 the socially concerned chancellor, trying to change lives for the better...，但这是表象（体现于 On first hearing），并非真正动机。［B］源自第二段④句 help people stay off benefits and help those on benefits get into work faster，但这是奥斯本自己的说辞，并非其真正动因。［C］对第二段⑧句 only the most deserving claimants received their benefits 反向干扰：新政明显是对失业金申请者“更小气”，而不是“更大方”。
［技巧总结］本题考查奥斯本实施新政的“真正动机”。解题关键在于：将文中信息分类、识别“表象”和“真相”。具体来看，解题关键在于将第二段信息分类：①②③④句介绍新政规定及奥斯本口中的“目的”（he claimed）——⑤⑥句作者发起质疑（Help? Really?）——⑦句作者说明表象（On first hearing）——⑧句说明真正动机（What motivated him, we were to understand, was...）。随后可排除来自于“奥斯本说辞”及“表象”的干扰项，留下来自“真正动机”的［C］、［D］。最后将两选项与⑧句仔细比对，排除与文意相反的［C］，确定与文意相符的［D］。"""
    },
    24: {
        "stem": "According to Paragraph 3, being unemployed makes one feel ________.",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "uneasy", "value": "uneasy"},
            {"key": "B", "text": "insulted", "value": "insulted"},
            {"key": "C", "text": "enraged", "value": "enraged"},
            {"key": "D", "text": "guilty", "value": "guilty"}
        ],
        "explanation": """［精准定位］第三段集中论述了失业带给人们的打击：经济窘迫，心理尴尬，感到不被需要，失去原有的目标感及有序感，无比渴望早日找到工作。可见，失业令人内心恐慌不安，［A］正确。
［命题解密］正确项［A］ uneasy 体现了第三段关键词汇 hurting... financially terrifying, psychologically embarrassing... not wanted... 表达的心理感受。
［错项排除］［B］ insulted 相关信息为 hurting，但根据①句冒号后及②句对其解释，可知失业带来的是心理窘迫难堪而非受辱。［C］ enraged 相关信息为 you know that support is minimal and extraordinarily hard to get，但从中无法得出失业者“愤怒”。［D］ guilty 无中生有，失业并非道德过错，文中未提及失业者感到内疚。
［技巧总结］解答情感态度细节题时，应从全段多处细节事实中提取核心情感基调，避免受个别极端情绪词（如 enraged、insulted）误导。整段描述失业造成的经济恐慌（financially terrifying）与被社会排斥感（excluded from work environment），uneasy（不安、忐忑）最准确中肯地概括了这种心理状态。"""
    },
    25: {
        "stem": "To which of the following would the author most probably agree?",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "Unemployment benefits should not be made conditional.", "value": "Unemployment benefits should not be made conditional."},
            {"key": "B", "text": "The British welfare system indulges jobseekers' laziness.", "value": "The British welfare system indulges jobseekers' laziness."},
            {"key": "C", "text": "The jobseekers' allowance has met their actual needs.", "value": "The jobseekers' allowance has met their actual needs."},
            {"key": "D", "text": "Osborne's reforms will reduce the risk of unemployment.", "value": "Osborne's reforms will reduce the risk of unemployment."}
        ],
        "explanation": """［精准定位］第四段③④⑤句指出，奥斯本计划完全偏离了英国福利制度“无条件帮助人们度过危机”的建制初衷。福利制度本质上是一种社会保险，公民缴税正是为了在遭遇不测时获得确定无条件的保障。作者强烈反对给失业救济预设苛刻前提条件，［A］正确。
［命题解密］［A］合理推导了第四段主旨观点：作者借②句虚拟语气（It is as though...）及③④⑤句正反对比，论证失业救济金不应附加苛刻条件，与［A］完全吻合。
［错项排除］［B］源自第一段③句 state only too ready to indulge 及第二段⑦句 subsidises laziness，但这是奥斯本的理念（作者所批驳的看法）。［C］与第四段⑤句 no insurance... the least generous（救济金数目甚微，无法为失业者提供充分保障）相悖。［D］将第四段③句 you can insure yourself against the risk of unemployment 偷换为奥斯本改革能够降低失业风险，与作者批判态度相反。
［技巧总结］推断作者观点态度题时，需准确区分“作者引述的反方/当事人立场”与“作者本人的批判立场”。作者通篇对奥斯本的新政持讽刺批判态度，认定失业救济应是社会兜底契约，不应设置惩罚性前置门槛。"""
    },
    26: {
        "stem": "A lot of students take up law as their profession due to ________.",
        "correct_answer": "D",
        "options": [
            {"key": "A", "text": "the growing demand from clients", "value": "the growing demand from clients"},
            {"key": "B", "text": "the increasing pressure of inflation", "value": "the increasing pressure of inflation"},
            {"key": "C", "text": "the prospect of working in big firms", "value": "the prospect of working in big firms"},
            {"key": "D", "text": "the attraction of financial rewards", "value": "the attraction of financial rewards"}
        ],
        "explanation": """［精准定位］根据第二段②句“顶尖律师可挣得摩天大楼般高的钱，吸引众多学生涌入法学院（skyscrapers of cash... continue to lure in hordes of applicants）”可知，金钱回报是吸引学生从事法律行业的核心诱因，［D］正确。
［命题解密］题干 + 正确项［D］是对第二段②句 skyscrapers of cash... lure in... 的同义改写，the attraction of financial rewards 对应 lure in 与 cash。
［错项排除］［A］ the growing demand from clients 与第二段①句 clients... cut their legal budgets（委托人纷纷削减法律预算）相反。［B］ the increasing pressure of inflation 全文未提及通胀压力。［C］ the prospect of working in big firms 将大律所的高额收入偷换为去大律所工作本身。
［技巧总结］因果细节题直接锁定原文因果提示词（lure in 诱惑/吸引），将修辞化表达（skyscrapers of cash）转化为正规概括表达（financial rewards），即可迅速锁定答案。"""
    },
    27: {
        "stem": "Which of the following adds to the costs of legal education in most American states?",
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": "Higher tuition fees for undergraduate studies.", "value": "Higher tuition fees for undergraduate studies."},
            {"key": "B", "text": "Receiving training by professional associations.", "value": "Receiving training by professional associations."},
            {"key": "C", "text": "Admissions approval from the bar association.", "value": "Admissions approval from the bar association."},
            {"key": "D", "text": "Pursuing a bachelor's degree in another major.", "value": "Pursuing a bachelor's degree in another major."}
        ],
        "explanation": """［精准定位］第三段③句介绍当前法律教育体制：先要攻读四年非法律专业学士学位，后才可进入法学院攻读三年法律学位，最后还得花重金通过律师资格考试；且法学院必须经由美国律师协会（ABA）认可认证。这一漫长昂贵的行业培训体系推高了整体成本，［B］正确。
［命题解密］正确项［B］对应第三段③句中 a four-year undergraduate degree in some unrelated subject... a three-year law degree at an American Bar Association-approved school 整个行业协会强制规训体制，Receiving training by professional associations 准确概括了必须在经专业协会认证机构受训的要求。
［错项排除］［A］本科学费高昂并非导致法律教育费用居高不下的主要制度根源，文意重在指出必须先读四年无关本科这一制度缺陷。［C］将考试准备费用歪曲为准入许可审批。［D］攻读其他专业学士学位只是受制于强制教育路径的结果，而非制度推高费用的核心机制。
［技巧总结］本题考查深层制度因果关联。文章指出美国绝大多数州僵化的行业协会垄断了从学院准入到执业考试的全流程，强制推行冗长多余的专业培训体制，从而直接导致法律教育费用居高不下。"""
    },
    28: {
        "stem": "Hindrance to the reform of the legal system originates from ________.",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "the rigid bodies governing the profession", "value": "the rigid bodies governing the profession"},
            {"key": "B", "text": "lawyers' and clients' strong resistance", "value": "lawyers' and clients' strong resistance"},
            {"key": "C", "text": "the stern exam for would-be lawyers", "value": "the stern exam for would-be lawyers"},
            {"key": "D", "text": "non-professionals' sharp criticism", "value": "non-professionals' sharp criticism"}
        ],
        "explanation": """［精准定位］第四段②句明确指出：切实可行的改革计划早已具备，但各州行业管理机构过于保守不愿推行（Sensible ideas... are around. But the state-level bodies that govern the profession are too conservative to implement them）。可见，保守僵化的行业管理机构阻碍了改革，［A］正确。
［命题解密］正确项［A］是对第四段②句的同义改写，其中 rigid 对应 too conservative，bodies governing the profession 原词对应 bodies that govern the profession。
［错项排除］［B］ lawyers' and clients' strong resistance 与文意相反，第四段①句指出改革对律师和客户都有益（help both lawyers and their customers），双方并不反对。［C］ the stern exam 是法学院毕业生的障碍，并非阻碍制度改革的根源。［D］非专业人士批评是推动改革的呼声，而非阻碍改革的阻力。
［技巧总结］细节事实题通过抓准主语施动者定位。题干 Hindrance（阻碍）同义对应原文 too conservative to implement them（过于保守而不愿推行），其执行主体正是 the state-level bodies that govern the profession。"""
    },
    29: {
        "stem": 'The guild-like ownership structure is considered "restrictive" partly because it ________.',
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": "prevents lawyers from gaining due profits", "value": "prevents lawyers from gaining due profits"},
            {"key": "B", "text": "bans outsiders' involvement in the profession", "value": "bans outsiders' involvement in the profession"},
            {"key": "C", "text": "aggravates the ethical situation in the trade", "value": "aggravates the ethical situation in the trade"},
            {"key": "D", "text": "keeps lawyers from holding law-firm shares", "value": "keeps lawyers from holding law-firm shares"}
        ],
        "explanation": """［精准定位］第五段②句解释①句所述概念“限制性所有权结构”：除了哥伦比亚特区，非律师身份的人不允许拥有律师事务所的股份（non-lawyers may not own any share of a law firm）；④句也强调其本质是排除外部非专业人士准入（keeping outsiders out）。可见，限制性所有权排斥了外部人员参与，［B］正确。
［命题解密］正确项［B］是对第五段②句 non-lawyers may not own any share of a law firm 以及④句 keeping outsiders out 的同义改写，bans outsiders' involvement 准确对应排斥外部资本与管理者。
［错项排除］［A］ prevents lawyers from gaining due profits 与原文相反，大律所合伙人收益极其丰厚。［C］将律所借口维护职业道德（ethical argument）曲解为使道德恶化。［D］将限制“非律师（non-lawyers）”持股偷换为限制“律师（lawyers）”持股。
［技巧总结］考查段落核心概念的内涵界定。第五段采用“总（提出限制性所有权概念）—分（具体说明除特区外严禁非律师参股合伙）”结构，抓住 non-lawyers / outsiders 即可一击命中［B］。"""
    },
    30: {
        "stem": "In this text, the author mainly discusses ________.",
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": "the factors that help make a successful lawyer in America", "value": "the factors that help make a successful lawyer in America"},
            {"key": "B", "text": "a problem in America's legal profession and solutions to it", "value": "a problem in America's legal profession and solutions to it"},
            {"key": "C", "text": "the role of undergraduate studies in America's legal education", "value": "the role of undergraduate studies in America's legal education"},
            {"key": "D", "text": "flawed ownership of America's law firms and its causes", "value": "flawed ownership of America's law firms and its causes"}
        ],
        "explanation": """［精准定位］首两段提出话题“美国法律服务费用高昂”；第三段剖析教育体制与债务成因，第四段提出改革培训与准入的对策；第五段剖析行会式所有权垄断问题，末段提出开放所有权、引入外部竞争的对策。全文通过两个完整回合的“剖析问题—提出解决对策”展开论述，文章中心正是美国法律行业的问题与解决出路，［B］正确。
［命题解密］正确项［B］是对全文主旨脉络最精准有力的宏观概括，既涵盖法律服务昂贵低效之问题（a problem），又涵盖放开管制、引入竞争之对策（solutions to it）。
［错项排除］［A］由第三段教育路径捏造出成功律师的要素，偏离主旨。［C］将本科教育在法律培养中的环节这一局部支撑细节夸大为全篇主旨。［D］律所所有权结构仅为第五六段讨论的第二项具体问题，以偏概全。
［技巧总结］主旨大意题解题关键在宏观结构梳理。文章逻辑清晰：提出问题（首段高昂收费）→ 深入原因分析与对策一（教育改革）→ 深入原因分析与对策二（律所所有权改革）→ 呼吁美国效仿英国改革。问题与对策（problem and solutions）完美契合全文框架。"""
    },
    31: {
        "stem": "The Fundamental Physics Prize is seen as ________.",
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": "a symbol of the entrepreneurs' wealth", "value": "a symbol of the entrepreneurs' wealth"},
            {"key": "B", "text": "a handsome reward for researchers", "value": "a handsome reward for researchers"},
            {"key": "C", "text": "a possible replacement of the Nobel Prizes", "value": "a possible replacement of the Nobel Prizes"},
            {"key": "D", "text": "an example of bankers' investments", "value": "an example of bankers' investments"}
        ],
        "explanation": """［精准定位］首句开门见山指出 300 万美元的基础物理学奖（Fundamental Physics Prize, FPP）是个极具吸引力的尝试；②③句接着说明一系列类似的奖金丰厚奖项（lucrative awards for researchers）已加入诺贝尔奖之列，旨在奖励杰出科研工作者。可见，该奖项是对研究人员的丰厚奖赏，［B］正确。
［命题解密］［B］中 a handsome reward for researchers 是对原文 US $3-million、lucrative awards for researchers 的直接同义替换。
［错项排除］［A］利用首段④句 funded from the fat bank accounts of Internet entrepreneurs 设伏，但这只是奖项资金来源，并非该奖项被赋予的社会认知属性。［C］过度推论，文中指出新奖与诺贝尔奖并存（join the Nobels），而非替代诺贝尔奖。［D］将银行账户（bank accounts）偷换为银行家的投资行为。
［技巧总结］首道细节题考查核心概念的定性。作者首段正面肯定新奖项设立的实质价值，抓住 lucrative awards for researchers（面向科研人员的丰厚奖项），与 handsome reward 构成标准近义替换。"""
    },
    32: {
        "stem": "The critics think that the new awards will most benefit ________.",
        "correct_answer": "C",
        "options": [
            {"key": "A", "text": "the profit-oriented scientists", "value": "the profit-oriented scientists"},
            {"key": "B", "text": "the achievement-based system", "value": "the achievement-based system"},
            {"key": "C", "text": "the founders of the new awards", "value": "the founders of the new awards"},
            {"key": "D", "text": "peer-review-led research", "value": "peer-review-led research"}
        ],
        "explanation": """［精准定位］根据 The critics 定位至第二段前两句引入批评人士视角。④句尖锐指出：（批评者认为）设立巨奖实际上是背后设立者自我包装宣传的营销手段（The critics say... an exercise in self-promotion for those behind them）。因此在批评者看来，最大的受益者正是出资设奖的创始人们，［C］正确。
［命题解密］题干 + ［C］是对第二段④句 an exercise in self-promotion for those behind them 的合理推导，those behind them 即指设立奖项的创始人（the founders）。
［错项排除］［A］将批评者担忧奖项吸引心术不正者（skew the priorities）曲解为逐利科学家是最大获益者。［B］与第二段⑤句 time-honoured peer-review-led research 混合设置反向干扰。［D］同行评审研究体制恰恰是批评者担心会被新奖项侵蚀破坏的对象。
［技巧总结］观点推断题必须严格界定题目所问的主体立场（The critics think）。锁定原文 an exercise in self-promotion（自我推销的一场秀），其施动对象 those behind them 即对应 founders。"""
    },
    33: {
        "stem": "The discovery of the Higgs boson is a typical case which involves ________.",
        "correct_answer": "C",
        "options": [
            {"key": "A", "text": "legitimate concerns over the new prizes", "value": "legitimate concerns over the new prizes"},
            {"key": "B", "text": "controversies over the recipients' status", "value": "controversies over the recipients' status"},
            {"key": "C", "text": "the joint effort of modern researchers", "value": "the joint effort of modern researchers"},
            {"key": "D", "text": "the demonstration of research findings", "value": "the demonstration of research findings"}
        ],
        "explanation": """［精准定位］第四段③句前半句指出，传统授奖对人数不超过三人的硬性限制早已与现代科研通力合作的性质严重脱节（the Nobel Foundation's limit... has long been outgrown by the collaborative nature of modern research）；紧接着后半句以希格斯玻色子的发现为例说明：这一发现是由数千位物理学家共同协作完成的。可见该案例体现了现代科研工作者的共同努力，［C］正确。
［命题解密］［C］是对第四段③句的合理推断，the joint effort of modern researchers 精准对应文中 collaborative nature of modern research 以及数千科学家的共同攻关。
［错项排除］［A］源自①句 there are legitimate concerns，但希格斯玻色子是用来举例证明科学协作性与旧评奖规则的冲突，而非新奖担忧。［B］将人数限制偷换为获奖者身份争议。［D］脱离段落论证核心。
［技巧总结］例证题的核心是“例子为观点服务”。希格斯玻色子发现案例紧跟在 the collaborative nature of modern research 之后，充当论据，论点即为科学研究已是集体智慧协作的产物，直接匹配［C］。"""
    },
    34: {
        "stem": "According to Paragraph 4, which of the following is true of the Nobels?",
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": "History has never cast doubt on them.", "value": "History has never cast doubt on them."},
            {"key": "B", "text": "Their endurance has done justice to them.", "value": "Their endurance has done justice to them."},
            {"key": "C", "text": "They are the most representative honor.", "value": "They are the most representative honor."},
            {"key": "D", "text": "Their legitimacy has long been in dispute.", "value": "Their legitimacy has long been in dispute."}
        ],
        "explanation": """［精准定位］第四段④句指出，诺贝尔奖当年同样是由富裕的私人出资设立；⑤句紧接着指出：诺贝尔奖历经一个多世纪历史沉淀与时间考验，才确立了举世公认的合法性与尊崇声望（the Nobels have great prestige and history has given them legitimacy）。正是经受住了岁月的洗礼赋予了诺贝尔奖真正的崇高地位，［B］正确。
［命题解密］［B］是对第四段④⑤句内容的合理概括，endurance 对应历经岁月，has done justice to them 对应 history has given them legitimacy 彰显出其应得的声望价值。
［错项排除］［A］与原文不符：第四段论及新旧奖项均面临评奖机制局限性的质疑。［C］过度引申，文中仅称 have great prestige，并未断言为“最”具代表性荣誉。［D］将早年私人设立与评奖局限性曲解为合理性长期处于争议中，与末句肯定其合法性矛盾。
［技巧总结］事实细节题把握长难句的修辞与论证重心。作者强调历史沉淀（history has given them legitimacy）使得诺奖经受住时间检验，endurance 巧妙概括这一内涵。"""
    },
    35: {
        "stem": "The author believes that the new awards are ________.",
        "correct_answer": "D",
        "options": [
            {"key": "A", "text": "unworthy of public attention", "value": "unworthy of public attention"},
            {"key": "B", "text": "subject to undesirable changes", "value": "subject to undesirable changes"},
            {"key": "C", "text": "harmful to the culture of research", "value": "harmful to the culture of research"},
            {"key": "D", "text": "acceptable despite the criticism", "value": "acceptable despite the criticism"}
        ],
        "explanation": """［精准定位］首段①句 ...is indeed an interesting experiment 即奠定作者对新奖项“总体肯定”的基调；第二段虽列举批评者的担忧，但末段最终亮明作者核心立场：大方接纳此类新奖项是明智之举（It is wise to be grateful to the new awards...）；④句让步指出批评固然合理，但捐资人以自己的财富奖赏科研无可厚非，应予以包容接纳，［D］正确。
［命题解密］［D］是对作者综合态度的最合理概括。末段④句前半部分 It is fair to criticize 让步表明对外界批评的理解，对应选项 despite the criticism；后半部分以 but 转折提出捐资助研无可厚非，末句进一步肯定接纳新奖项，对应选项 acceptable。
［错项排除］［A］与作者首段及末段积极肯定态度直接矛盾。［B］源于第五段④句 it is the prize-givers' money to do with as they wish，但作者意在说明出资人有权支配资金，而非暗示奖项存在不良突变。［C］是第二段批评人士的消极担忧，并非作者立场。
［技巧总结］作为篇末作者态度题，解答需统揽全文论述脉络：作者虽承认批评人士指出的缺陷与铜臭隐忧（fair to criticize），但通篇主流立足于现实建设性视角，倡导积极肯定与感恩新奖项对科学界的注资扶持，因此“批评声中仍值得肯定（acceptable despite the criticism）”最精准体现了作者的辩证包容态度。"""
    },
    36: {
        "stem": "According to Paragraph 1, what is the author's attitude toward the AAAS's report?",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "Critical.", "value": "Critical."},
            {"key": "B", "text": "Appreciative.", "value": "Appreciative."},
            {"key": "C", "text": "Contemptuous.", "value": "Contemptuous."},
            {"key": "D", "text": "Tolerant.", "value": "Tolerant."}
        ],
        "explanation": """［精准定位］首段采取欲抑先扬手法：①句先肯定报告强调人文社科重要性的积极初衷（deserves praise for affirming the importance...）；②句转折词 however 引出核心论点：令人遗憾的是，该报告未能指出人文教育所面临危机的实质，结果可能是弊大于利（cause more harm than good）。可见，作者对其根本态度是批判性的，［A］正确。
［命题解密］正确项［A］是对开篇欲抑先扬、重心落于转折之后的批判性立场（cause more harm than good）的精准概括。
［错项排除］［B］ Appreciative 仅为①句表面赞扬的让步铺垫，并非作者最终定性。［C］ Contemptuous（轻蔑的）情感过度极端苛刻。［D］ Tolerant（宽容的）与文中明确直言其弊大于利、阻碍改革的鲜明批判立场不符。
［技巧总结］段落观点态度题需紧扣转折逻辑词。开篇赞扬（deserves praise）随即被 however（然而）与 cause more harm than good（弊大于利）强势反转，作者立意重在“抑”而非“扬”，态度确属 Critical。"""
    },
    37: {
        "stem": "Influential figures in the Congress required that the AAAS report on how to ________.",
        "correct_answer": "D",
        "options": [
            {"key": "A", "text": "define the government's role in education", "value": "define the government's role in education"},
            {"key": "B", "text": "safeguard individuals' rights to education", "value": "safeguard individuals' rights to education"},
            {"key": "C", "text": "retain people's interest in liberal education", "value": "retain people's interest in liberal education"},
            {"key": "D", "text": "keep a leading position in liberal education", "value": "keep a leading position in liberal education"}
        ],
        "explanation": """［精准定位］第二段首句明确指出：国会重要人物要求 AAAS 拟定报告，界定各级政府及相关机构可采取的举措，以维持美国在人文与社科教育研究领域的卓越领先地位（to maintain national excellence in humanities and social scientific scholarship and education）。可见国会的核心要求是保持领先地位，［D］正确。
［命题解密］题干 + 正确项［D］是对第二段首句 to maintain national excellence in humanities and social scientific... education 的同义改写，keep a leading position 对应 maintain national excellence。
［错项排除］［A］、［B］、［C］利用首句中 actions taken by governments、educators、individual benefactors 等碎片词设伏，但国会要求的是界定“可以采取的行动”以维持领先，绝非要求界定“政府在教育中的角色”或“维护受教育权利”或“保持公众兴趣”。
［技巧总结］细节题直接根据题干核心词 Congress 和 required 定位至第二段首句。由 how to 明确考查行动旨归，快速定位末尾不定式目的状语 to maintain national excellence...，选项［D］直接完美对应。"""
    },
    38: {
        "stem": "According to Paragraph 3, the report suggests ________.",
        "correct_answer": "C",
        "options": [
            {"key": "A", "text": "an exclusive study of American history", "value": "an exclusive study of American history"},
            {"key": "B", "text": "a greater emphasis on theoretical subjects", "value": "a greater emphasis on theoretical subjects"},
            {"key": "C", "text": "the application of emerging technologies", "value": "the application of emerging technologies"},
            {"key": "D", "text": "funding for the study of foreign languages", "value": "funding for the study of foreign languages"}
        ],
        "explanation": """［精准定位］第三段②句详细梳理了报告提出的几项具体建议：支持全面扫盲、强调历史和政府体制学习，以及鼓励使用新的数字技术（and encourages the use of new digital technologies）。可见，应用新兴数字技术正是报告明确倡导的措施，［C］正确。
［命题解密］正确项［C］是对段中②句 encourages the use of new digital technologies 的标准同义改写，the application of emerging technologies 对应 the use of new digital technologies。
［错项排除］［A］利用②句 American history 设陷，但原文表述为 particularly（尤其是），而非 exclusive（排他的/唯独的）。［B］ theoretical subjects 全文未提及。［D］利用③句 investment in research 及④句 foreign languages 拼凑干扰，原文资助重点是教师培训而非孤立的外语学科研究。
［技巧总结］细节正误题需逐一比对选项修饰限制词。［A］将“特别强调（particularly）”篡改为“专属排他（exclusive）”，［C］通过词义泛化（use → application, new digital → emerging）实现同义替换，最为精准规范。"""
    },
    39: {
        "stem": "The author implies in Paragraph 5 that professors are ________.",
        "correct_answer": "C",
        "options": [
            {"key": "A", "text": "supportive of free markets", "value": "supportive of free markets"},
            {"key": "B", "text": "conservative about public policy", "value": "conservative about public policy"},
            {"key": "C", "text": "biased against classical liberal ideas", "value": "biased against classical liberal ideas"},
            {"key": "D", "text": "cautious about intellectual investigation", "value": "cautious about intellectual investigation"}
        ],
        "explanation": """［精准定位］第五段指出：现如今教授们惯常将进步主义的历史阐释和公共政策作为唯一适宜的研究课题，而将传统或古典自由人文思想（如自由市场和自力更生）描绘为超出常规、甚至超出正当合理的学术研究范畴（while portraying conservative or classical liberal ideas... as falling outside the boundaries of routine, and sometimes legitimate, intellectual investigation）。这实质揭示了教授们对古典自由人文思想抱有极深的偏见与排斥，［C］正确。
［命题解密］正确项［C］中 biased against 是对段中 portraying conservative or classical liberal ideas... as falling outside the boundaries of routine, and sometimes legitimate, intellectual investigation 批判态度的合理概括。
［错项排除］［A］与文意相悖，教授们将自由市场排斥在正当学术研究之外。［B］与原文相悖，教授们推崇的是进步主义公共政策（progressive public policy），而非保守主义。［D］曲解文意，教授们并非对学术研究谨慎，而是对特定人文思潮进行意识形态化打压。
［技巧总结］推断题需解读句群修辞与对比结构。该段核心句式为 treat A as B while portraying X as Y，对比体现教授对“革新政策（A）”的追捧与对“古典自由思想（X）”的污名化排斥，biased against 准确揭示其实质偏见。"""
    },
    40: {
        "stem": "Which of the following would be the best title for the text?",
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": 'Ways to Grasp "The Heart of the Matter"', "value": 'Ways to Grasp "The Heart of the Matter"'},
            {"key": "B", "text": 'Illiberal Education and "The Heart of the Matter"', "value": 'Illiberal Education and "The Heart of the Matter"'},
            {"key": "C", "text": "The AAAS's Contribution to Liberal Education", "value": "The AAAS's Contribution to Liberal Education"},
            {"key": "D", "text": "Progressive Policy vs. Liberal Education", "value": "Progressive Policy vs. Liberal Education"}
        ],
        "explanation": """［精准定位］文首段点题：《问题的核心》虽值得赞赏，却未触及当前美国人文教育危机的本质（failure to address the true nature of the crisis）；第二段补充出台背景；第三至五段展开论述报告的致命缺陷：缺乏人文精神的非人文素质教育才是危机根源，而报告对此只字不提；文末段重申主题：报告遮蔽了问题的深度与广度，很可能阻碍人文教育改革。由此可见，全文核心是剖析非人文教育与《问题的核心》报告的关系，［B］最能概括文意。
［命题解密］正确项［B］是对文章主旨的最佳概括，精准融合文章评论对象 The Heart of the Matter 与批判主线 Illiberal Education。
［错项排除］［A］无中生有，文章重点在于批评报告缺陷，而非介绍如何理解该报告。［C］将首句让步肯定放大为文章核心，偏离全篇批判主基调。［D］仅涉及第五段论证局部，无法统摄全文。
［技巧总结］标题归纳题首尾呼应与双核心词法则。文章开篇与结尾均聚焦《问题的核心》（The Heart of the Matter）报告未能解决“非人文教育（Illiberal Education）”的实质危机，两者的矛盾冲突构成了整篇评论的核心框架，［B］最为贴切传神。"""
    }
}
