# -*- coding: utf-8 -*-
"""
Round 69 Gold Data Generator: 2018 ky2
UUID: 8868dd40-75bf-590b-98a4-a516c5e1c161
"""
import json
import os

def build_gold_exam():
    # 1. Load existing JSON to preserve IDs
    json_path = 'public/data/exams/8868dd40-75bf-590b-98a4-a516c5e1c161.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Update exam metadata
    exam = data['exam']
    exam['title'] = '2018年全国硕士研究生招生考试英语（二）真题'
    exam['category_id'] = 'ky2'
    exam['year'] = 2018
    exam['exam_type'] = 'real'
    exam['total_score'] = 60.0
    exam['pass_score'] = 36.0
    exam['duration_minutes'] = 180
    exam['approval_status'] = 'approved'

    # 3. Update passages
    from build_2018_ky2_gold_engine import get_gold_passages
    gold_passages = get_gold_passages()
    for i, p_text in enumerate(gold_passages):
        data['passages'][i]['content'] = p_text

    # 4. Define questions data
    q_data = [
        # Q1-Q20 (Cloze)
        (
            "Choose the best option for blank [1] in the passage:",
            [("A", "ignore"), ("B", "protect"), ("C", "resolve"), ("D", "discuss")],
            "C",
            "［考点提炼］句间因果逻辑＋研究结果一致性。\n"
            "［解题思路］首句设问“人们为何会阅读负面的网络评论并做其他令自己不快的事？”。第二句以 Because 给出原因：研究表明，这是因为人类生来就有“消除不确定性的需求”。第三句进一步阐释：研究表明，人们的认知需求是如此强烈。联系三句可推知，an inherent need to resolve uncertainty（消除不确定性、明确认知情形的需求），恰能解释人们为何“宁愿忍受不快也要去阅读负面评论等”。因此C项 resolve 符合文意。\n"
            "［错项排除］[A] ignore（忽视；不理）与“强烈的认知需求”语义相反；[B] protect（保护；维护）无法回答首句设问；[D] discuss（讨论；商讨）尚未付诸个人实践，与下文“努力求知（know）”存在偏差。"
        ),
        (
            "Choose the best option for blank [2] in the passage:",
            [("A", "seek"), ("B", "refuse"), ("C", "wait"), ("D", "regret")],
            "A",
            "［考点提炼］句内因果逻辑＋句间解释关系。\n"
            "［解题思路］空格所在的宾语从句为 so...that...（如此……以至于……）结构，people will seek to satisfy their curiosity 说明 the need to know is so strong 所导致的结果。新研究显示，人们的认知需求是如此强烈，以至于他们会试图、设法满足自己的好奇心。seek to do sth 既符合句内因果逻辑，又解释上句研究结果。\n"
            "［错项排除］[B] refuse（拒绝）与“认知需求极其强烈”方向相反；[C] wait（等待）偏中性，不足以成为强烈认知需求的结果；[D] regret（后悔；遗憾）同样与强烈认知需求相悖。"
        ),
        (
            "Choose the best option for blank [3] in the passage:",
            [("A", "rise"), ("B", "hurt"), ("C", "last"), ("D", "mislead")],
            "B",
            "［考点提炼］句内语义逻辑＋上下文语义一致。\n"
            "［解题思路］空格所在时间状语从句为 even when it is clear the answer will hurt。让步逻辑词 even（即使；甚至）提示“答案明显会令人不快”，结合开篇的 negative 与 painful，可进一步确认空格词应表示“伤害；使令人不快/痛苦”。因此B项 hurt 契合文意。\n"
            "［错项排除］[A] rise（上升；出现）偏离上下文总体方向；[C] last（持续）搭配不合理且偏离文意；[D] mislead（误导）同样偏离上下文“就算令人不快也要探寻答案”的主旨。"
        ),
        (
            "Choose the best option for blank [4] in the passage:",
            [("A", "expose"), ("B", "alert"), ("C", "tie"), ("D", "treat")],
            "A",
            "［考点提炼］固定短语＋研究内容与结论一致性。\n"
            "［解题思路］空格句指出，行为科学家们对“学生是否愿意为了满足好奇心而让自己遭受令人不快的刺激”进行了测试。expose sb to sth 意为“使某人遭受（不快）”。expose themselves to unpleasant stimuli 既与首段末句形成对应，又符合受试者的身份。\n"
            "［错项排除］[B] alert（提醒；使警惕）与满足好奇心甘愿受苦文意不符；[C] tie（捆绑；束缚）体现长期接触，而刺激是短暂的；[D] treat（款待）通常接正面美好事物，无法与 unpleasant stimuli 搭配。"
        ),
        (
            "Choose the best option for blank [5] in the passage:",
            [("A", "concept"), ("B", "message"), ("C", "review"), ("D", "trial")],
            "D",
            "［考点提炼］句间衔接关系＋近义指代。\n"
            "［解题思路］空格所在短语 For one trial 位于句首作状语，起句间衔接作用。上句总述在一连串四项实验中（In a series of four experiments），下文第三段末句指出随后实验（Subsequent experiments），此处引出其中一项试验的操作，trial（试验；考验）与 experiment 近义，符合上下文。\n"
            "［错项排除］[A] concept（概念）、[B] message（信息；消息）、[C] review（回顾；审查）均与实验具体操作步骤的顺接不符。"
        ),
        (
            "Choose the best option for blank [6] in the passage:",
            [("A", "deliver"), ("B", "remove"), ("C", "weaken"), ("D", "interrupt")],
            "A",
            "［考点提炼］动宾搭配＋上下文语义。\n"
            "［解题思路］空格句指出：Half of the pens would deliver an electric shock when clicked（一半的笔在被按动时会产生/发出电击）。deliver an electric shock 表示“释放/给予电击”，符合实验中令人不快的刺激设置。\n"
            "［错项排除］[B] remove（移走；消除）、[C] weaken（减弱）、[D] interrupt（打断；中断）均预设前提为“原本所有笔均带电，按动后消除或减弱”，完全倒置了电击产生的顺序与实验机制。"
        ),
        (
            "Choose the best option for blank [7] in the passage:",
            [("A", "Unless"), ("B", "When"), ("C", "If"), ("D", "Though")],
            "B",
            "［考点提炼］省略句＋时间条件状语从句。\n"
            "［解题思路］逗号前为省略“主语＋be动词”的状语从句，完整形式为 When left alone in the room（当被单独留在房间不加打扰时）。不知道究竟哪些笔带电的学生受好奇心驱使，不停按笔并因此遭受更多电击。When 引出时间与实验情境，符合心理学实验设计规范。\n"
            "［错项排除］[A] Unless（除非）逻辑反常；[C] If（如果）通常用于条件假设或分组对照，文中此句为同一测试情境下的行为对比；[D] Though（尽管；虽然）让步逻辑与事实不符。"
        ),
        (
            "Choose the best option for blank [8] in the passage:",
            [("A", "change"), ("B", "continue"), ("C", "happen"), ("D", "disappear")],
            "C",
            "［考点提炼］比较成分的语义相对性＋上下文语境。\n"
            "［解题思路］句内形成对比：不知道哪些笔会电击自己的学生（who did not know which ones would shock them）与知道将会发生什么的学生（who knew what would happen）。“知道会发生什么”即知道是否会产生电击，happen 与 shock 形成对应。\n"
            "［错项排除］[A] change（改变）、[B] continue（继续）、[D] disappear（消失）均无法与 which ones would shock them 构成自然的语义对比。"
        ),
        (
            "Choose the best option for blank [9] in the passage:",
            [("A", "owing to"), ("B", "rather than"), ("C", "regardless of"), ("D", "such as")],
            "D",
            "［考点提炼］句内列举举例逻辑。\n"
            "［解题思路］空格句指出随后的实验利用其他刺激（with other stimuli）再现了该效应，空格后紧接着 the sound of fingernails on a chalkboard and photographs of disgusting insects（指甲刮擦黑板的声音和令人作呕的昆虫图片），显然是对“其他刺激”的具体举例。such as 意为“例如；诸如”，用于列举举例。\n"
            "［错项排除］[A] owing to（因为；由于）表原因；[B] rather than（而不是）表排除；[C] regardless of（不管；不顾）表让步，均不符合列举逻辑。"
        ),
        (
            "Choose the best option for blank [10] in the passage:",
            [("A", "disagree"), ("B", "discover"), ("C", "forgive"), ("D", "forget")],
            "B",
            "［考点提炼］短语搭配＋文章主旨。\n"
            "［解题思路］第四段首句援引研究者 Hsee 的观点指出：The drive to discover is deeply rooted in humans（探索的欲望深深扎根于人类的本能之中）。The drive to discover 概括了前文的 an inherent need to resolve uncertainty、the need to know 等核心表述，discover（探索；发现）契合全文主旨。\n"
            "［错项排除］[A] disagree（不同意；反对）、[C] forgive（原谅；宽恕）、[D] forget（遗忘）均脱离文章讨论的“求知与好奇心本能”主旨。"
        ),
        (
            "Choose the best option for blank [11] in the passage:",
            [("A", "food"), ("B", "pay"), ("C", "marriage"), ("D", "schooling")],
            "A",
            "［考点提炼］句内并列关系＋同级类比。\n"
            "［解题思路］空格词与 shelter（住所）通过 or 并列，共同受 the basic drives 修饰，属于人类最基础的生存本能需求。food or shelter（食物与住所）为常见经典并列，用最基本的生理需求类比人类探索欲之强烈。\n"
            "［错项排除］[B] pay（工资）、[C] marriage（婚姻）、[D] schooling（学校教育）均不属于最底层的生理生存基本本能需求。"
        ),
        (
            "Choose the best option for blank [12] in the passage:",
            [("A", "begin with"), ("B", "lead to"), ("C", "rest on"), ("D", "learn from")],
            "B",
            "［考点提炼］动宾搭配＋正面因果关系。\n"
            "［解题思路］破折号内内容为举例说明好奇心是一种有益的本能（a good instinct）：it can lead to new scientific advances（例如它能带来新的科学进步）。lead to 意为“导致；引起；带来”，符合正面积极的因果逻辑。\n"
            "［错项排除］[A] begin with（以……为起点）、[C] rest on（依赖于）、[D] learn from（向……学习）均倒置或错置了好奇心与科学进步之间的逻辑因果关系。"
        ),
        (
            "Choose the best option for blank [13] in the passage:",
            [("A", "diligence"), ("B", "withdrawal"), ("C", "persistence"), ("D", "inquiry")],
            "D",
            "［考点提炼］指代回指＋句内转折。\n"
            "［解题思路］转折词 but 提示上下文语义反转：好奇心通常有益，但有时这种探究却可能适得其反（sometimes such inquiry can backfire）。such inquiry 回指前句的 curiosity，inquiry（探究；探索）与 curiosity 近义复现。\n"
            "［错项排除］[A] diligence（勤勉）、[B] withdrawal（退缩；退出）、[C] persistence（坚持）均不能准确回指好奇求知本能。"
        ),
        (
            "Choose the best option for blank [14] in the passage:",
            [("A", "self-deceptive"), ("B", "self-reliant"), ("C", "self-destructive"), ("D", "self-evident")],
            "C",
            "［考点提炼］上下文语义顺承＋负面后果修饰。\n"
            "［解题思路］空格句指出，好奇心会驱使人们去做 self-destructive things（自我毁灭/自毁之事），这是一种深刻的见解。承接上句的 backfire，指出好奇心可能带来的负面严重后果，self-destructive（自毁的；自我破坏的）精准呼应开篇的痛苦与自残式好奇行为。\n"
            "［错项排除］[A] self-deceptive（自欺欺人的）语义过窄；[B] self-reliant（自力更生的）为褒义词；[D] self-evident（显而易见的；不言而喻的）为中性词，均不符合负面有害语境。"
        ),
        (
            "Choose the best option for blank [15] in the passage:",
            [("A", "trace"), ("B", "define"), ("C", "resist"), ("D", "replace")],
            "C",
            "［考点提炼］段首转折＋应对策略。\n"
            "［解题思路］末段首句以 however 转折上文的好奇心负面危害，开启应对解决之道：Unhealthy curiosity is possible to resist, however（不过，病态的好奇心是有可能被抵制/抑制的）。下文紧接着通过实验证明预测感受能减少不良行为，证实病态好奇心可以被抑制（resist）。\n"
            "［错项排除］[A] trace（追踪；追溯）、[B] define（界定；定义）、[D] replace（取代；替换）均无法承接转折引出“如何避免负面好奇心”的下文。"
        ),
        (
            "Choose the best option for blank [16] in the passage:",
            [("A", "conceal"), ("B", "overlook"), ("C", "predict"), ("D", "design")],
            "C",
            "［考点提炼］动宾搭配＋前后近义复现。\n"
            "［解题思路］空格句指出，在最后一项实验中，被鼓励去 predict how they would feel after viewing an unpleasant picture（预测看到令人不快图片后自己作何感受）的参与者更不可能选择看此类图片。predict 与下句的 imagining ahead of time（提前设想）构成精准同义复现。\n"
            "［错项排除］[A] conceal（隐瞒；掩盖）、[B] overlook（忽视；忽略）、[D] design（设计）均与下文的“提前设想后果”语义相悖。"
        ),
        (
            "Choose the best option for blank [17] in the passage:",
            [("A", "pretend"), ("B", "remember"), ("C", "promise"), ("D", "choose")],
            "D",
            "［考点提炼］动词搭配＋实验行为选择。\n"
            "［解题思路］提前预测了不快感受的参与者 were less likely to choose to see such an image（更不可能选择去看这样的图片）。choose to do sth 意为“选择/决定做某事”，体现受试者自主克制了盲目好奇的冲动。\n"
            "［错项排除］[A] pretend（假装）、[B] remember（记得）、[C] promise（答应；承诺）均偏离实验中受试者在好奇心诱惑面前的自主决策行为。"
        ),
        (
            "Choose the best option for blank [18] in the passage:",
            [("A", "outcome"), ("B", "relief"), ("C", "plan"), ("D", "duty")],
            "A",
            "［考点提炼］上下文近义复现。\n"
            "［解题思路］句中指出 imagining the outcome of following through on one's curiosity ahead of time（事先设想坚持满足自己好奇心的结果）有助于确定这是否值得一试。outcome（结果；后果）呼应上句的 how they would feel after...。\n"
            "［错项排除］[B] relief（解脱；宽慰）、[C] plan（计划）、[D] duty（责任；义务）均不符合设想行为后果的逻辑。"
        ),
        (
            "Choose the best option for blank [19] in the passage:",
            [("A", "where"), ("B", "why"), ("C", "whether"), ("D", "how")],
            "C",
            "［考点提炼］宾语从句引导词＋衡量判断。\n"
            "［解题思路］空格句指出设想后果有助于确定这是否值得一试（help determine whether it is worth the endeavor）。whether 引导宾语从句，表达“是否”，体现对盲目满足好奇心价值的理性反思与衡量。\n"
            "［错项排除］[A] where（在哪里）、[B] why（为什么）、[D] how（如何）均无法表达理性衡量“是否值得”的判断逻辑。"
        ),
        (
            "Choose the best option for blank [20] in the passage:",
            [("A", "limitations"), ("B", "consequences"), ("C", "investments"), ("D", "strategies")],
            "B",
            "［考点提炼］文章主旨总结＋引言复现。\n"
            "［解题思路］研究者 Hsee 总结指出：Thinking about long-term consequences is key to reducing the possible negative effects of curiosity（思考长远后果是减少好奇心潜在负面影响的关键）。consequences（后果；结果）高度复现上文的 outcome 与 how they would feel。\n"
            "［错项排除］[A] limitations（局限性）、[C] investments（投资）、[D] strategies（策略）均不符合通过权衡后果以抑制好奇心负面冲动的语境。"
        ),

        # Q21-Q25 (Reading Text 1)
        (
            "A broken bike chain is mentioned to show students' lack of",
            [
                ("A", "practical ability"),
                ("B", "academic training"),
                ("C", "pioneering spirit"),
                ("D", "mechanical memorization")
            ],
            "A",
            "［考点提炼］写作目的题＋例证功能。\n"
            "［解题思路］第二段第二句指出 Koziatek 所在的高中教学特色是实践性的（learning is not something of books... but practical）。紧接着第三句通过反问指出：学生能够说出第13任总统的名字，却完全不会应对坏掉的自行车链条（be utterly overwhelmed by a broken bike chain）。提及坏掉的自行车链条，正是为了具象化说明传统教育下学生“缺乏实际动手与实践能力”。A项 practical ability 为第二句 practical 的原词复现与正解。\n"
            "［错项排除］[B] academic training（学术培训）与[D] mechanical memorization（机械记忆）是传统教育过分强调的内容，而非学生所缺乏的能力；[C] pioneering spirit（开创精神）属于 Koziatek 所在高中的办学特征，而非学生欠缺的技能。"
        ),
        (
            "There exists the prejudice that vocational education is for kids who",
            [
                ("A", "have a stereotyped mind"),
                ("B", "have no career motivation"),
                ("C", "are not academically successful"),
                ("D", "are financially disadvantaged")
            ],
            "C",
            "［考点提炼］事实细节题＋同义改写。\n"
            "［解题思路］根据题干 prejudice 与 vocational education 定位至第四段第三句：Schools in the family of vocational education have that stereotype... that it's for kids who can't make it academically（职业教育类学校有这种刻板印象……即它是面向那些在学业上无法取得成功的孩子）。C项 are not academically successful 是对 can't make it academically 的标准同义改写。\n"
            "［错项排除］[A] have a stereotyped mind（思维模式化）将学校面临的刻板印象偷换为学生自身固化；[B] have no career motivation（缺乏职业动机）无中生有；[D] are financially disadvantaged（经济贫困）将体力劳动地位低下误解为经济困难。"
        ),
        (
            "We can infer from Paragraph 5 that high school graduates",
            [
                ("A", "used to have big financial concerns"),
                ("B", "used to have more job opportunities"),
                ("C", "are reluctant to work in manufacturing"),
                ("D", "are entitled to more educational privileges")
            ],
            "B",
            "［考点提炼］推理引申题＋今昔对比。\n"
            "［解题思路］根据题干 Paragraph 5 与 high school graduates 定位至第五段第二、三句：Manufacturing is not the economic engine that it once was. The job security that the US economy once offered to high school graduates has largely evaporated（制造业已不再是曾经的经济引擎，美国经济曾提供给高中毕业生的就业保障很大程度上已不复存在）。这表明过去制造业繁荣时，高中毕业生享有更多就业机会和保障。B项 used to have more job opportunities 是对原文反向推导的准确表达。\n"
            "［错项排除］[A] used to have big financial concerns（过去有很大的经济顾虑）时态颠倒；[C] are reluctant to work in manufacturing（不愿进入制造业）违背文意；[D] are entitled to more educational privileges（享有更多教育特权）曲解了原文想让孩子多受教育的愿望。"
        ),
        (
            "The headlong push into bachelor's degrees for all",
            [
                ("A", "helps create a lot of middle-skill jobs"),
                ("B", "may narrow the gap in working-class jobs"),
                ("C", "is expected to yield a better-trained workforce"),
                ("D", "indicates the overvaluing of higher education")
            ],
            "D",
            "［考点提炼］事实细节题＋态度观点推断。\n"
            "［解题思路］根据题干定位至第六段首句：But the headlong push into bachelor's degrees for all - and the subtle devaluing of anything less - misses an important point: That's not the only thing the American economy needs（但盲目向所有人推行学士学位——并暗中贬低其他教育——忽略了重要一点：这并非美国经济的唯一所需）。下文进一步指出54%的工作仍是中等技能工作，说明盲目推行本科教育高估了高等学位的普适必要性，D项 indicates the overvaluing of higher education 精准概括了全段论点。\n"
            "［错项排除］[A] helps create a lot of middle-skill jobs（有助于创造大量中等技能岗位）与原文逻辑相悖，推行本科学位忽视了中等技能需求；[B] may narrow the gap in working-class jobs（可能缩小工人职位缺口）将解决方案与问题混淆；[C] is expected to yield a better-trained workforce（有望产生训练更好的劳动力）与原文仅有44%合格工人的事实相反。"
        ),
        (
            "The author's attitude toward Koziatek's school can be described as",
            [
                ("A", "supportive"),
                ("B", "tolerant"),
                ("C", "disappointed"),
                ("D", "cautious")
            ],
            "A",
            "［考点提炼］作者态度题＋全文行文脉络。\n"
            "［解题思路］通读全文，作者在第二段称赞 Koziatek 的实践是 Mr. Koziatek is part of something pioneering（具有开创性的事业），在第七段指出其学校正致力于填补国家急需的技能缺口（trying to fill that gap），末段更是将其学校评价为一记及时的警钟（wake-up call），防止教育走向一刀切。全篇字里行间充满了对该学校的赞许与支持，因此A项 supportive（支持的）为正确答案。\n"
            "［错项排除］[B] tolerant（容忍的）、[C] disappointed（失望的）、[D] cautious（谨慎的）均无法体现作者高度肯定赞赏的主基调。"
        ),

        # Q26-Q30 (Reading Text 2)
        (
            "The word \"plummeting\" (Para. 2) is closest in meaning to",
            [
                ("A", "rising"),
                ("B", "falling"),
                ("C", "changing"),
                ("D", "stabilizing")
            ],
            "B",
            "［考点提炼］词义猜测题＋上下文语境。\n"
            "［解题思路］根据定位词 Paragraph 2 定位至第二段第二、三句：But increasingly the story is about the plummeting prices of renewables, especially wind and solar. The cost of solar panels has dropped by 80 percent and the cost of wind turbines by close to one-third...。第三句中价格猛降80%和近三分之一（dropped by 80 percent）直接对第二句的 plummeting prices 进行数据阐释，plummeting 意为“暴跌；急剧下降”，与 falling（下降）词义最接近。\n"
            "［错项排除］[A] rising（上涨）、[C] changing（改变）、[D] stabilizing（趋于稳定）均与后句的价格骤跌80%语义不符。"
        ),
        (
            "According to Paragraph 3, the use of renewable energy in America",
            [
                ("A", "is as extensive as in Europe"),
                ("B", "is progressing notably"),
                ("C", "has proved to be impractical"),
                ("D", "faces many challenges")
            ],
            "B",
            "［考点提炼］事实细节题＋同义改写。\n"
            "［解题思路］根据题干 Paragraph 3 与 in America 定位至第三段第三、四句：...the United States is also seeing a remarkable shift. In March - for the first time - wind and solar power accounted for more than 10 percent of the power generated in the US...。文中指出美国正在经历显著的转变（remarkable shift），风能和太阳能发电占比历史性突破10%。B项 is progressing notably（正在显著进步）是对 seeing a remarkable shift 的精准同义置换。\n"
            "［错项排除］[A] is as extensive as in Europe（与欧洲一样广泛）与原文美国正在跟进的描述不符；[C] has proved to be impractical（被证实不切实际）与实际突破10%相悖；[D] faces many challenges（面临诸多挑战）并非第三段强调的核心事实。"
        ),
        (
            "It can be learned that in Iowa,",
            [
                ("A", "wind energy has replaced fossil fuels"),
                ("B", "there is a shortage of clean energy supply"),
                ("C", "tech giants are investing in clean energy"),
                ("D", "wind is a widely used energy source")
            ],
            "D",
            "［考点提炼］事实细节题＋细节事实识别。\n"
            "［解题思路］根据定位词 Iowa 定位至第四段第三句：...where wind turbines dot the fields and provide 36 percent of the state's electricity generation...。句中指出在爱荷华州风力发电机遍布田野（dot the fields），并提供了该州36%的电力供应。这充分说明风能是当地广泛使用的能源。D项 wind is a widely used energy source 正确反映了该事实。\n"
            "［错项排除］[A] wind energy has replaced fossil fuels（风能取代了化石燃料）言过其实，仅占36%；[B] there is a shortage of clean energy supply（清洁能源供应不足）与科技巨头被其充足供应所吸引相反；[C] tech giants are investing in clean energy（科技巨头投资清洁能源）偷换概念，科技巨头是被清洁能源吸引以运营数据中心，而非投资开发清洁能源。"
        ),
        (
            "Which of the following is true about clean energy according to Paragraphs 5 & 6?",
            [
                ("A", "Its application has boosted battery storage."),
                ("B", "It is commonly used in car manufacturing."),
                ("C", "Its continuous supply is becoming a reality."),
                ("D", "Its sustainable exploitation will remain difficult.")
            ],
            "C",
            "［考点提炼］事实细节题＋推理归纳。\n"
            "［解题思路］根据定位词 Paragraphs 5 & 6 定位至第五段：质疑者常提出“无风无阳光时怎么办”的反驳，但电池存储容量的提升正使其全天候供电能力变得更有可能（making their ability to keep power flowing around the clock more likely）。keep power flowing around the clock（全天候/不间断供电）与 continuous supply 对应，more likely 表明其正在成为现实。C项准确反映了两段阐述的趋势。\n"
            "［错项排除］[A] Its application has boosted battery storage（其应用促进了电池存储）因果倒置，是电池存储进步促进了清洁能源应用；[B] It is commonly used in car manufacturing（通常用于汽车制造）与电动车仍属罕见（still a rarity）相悖；[D] Its sustainable exploitation will remain difficult（可持续开发仍将困难）与技术突破的前景相反。"
        ),
        (
            "It can be inferred from the last paragraph that renewable energy",
            [
                ("A", "is not really encouraged by the US government"),
                ("B", "is not competitive enough with regard to its cost"),
                ("C", "will bring the US closer to other countries"),
                ("D", "will accelerate global environmental change")
            ],
            "A",
            "［考点提炼］推理引申题＋末段深层含义推断。\n"
            "［解题思路］根据定位词 the last paragraph 定位至第七段末句：What Washington does - or doesn't do - to promote alternative energy may mean less and less at a time of a global shift in thought（在全人类思想观念发生全球性转变之际，华盛顿政府为推广替代能源所做的事情——或者不做的事情——其影响力可能越来越微不足道）。结合第四段特朗普总统公开贬低风能（dismissed wind power），可推知美国政府并未真正大力鼓励和推动可再生能源发展。因此A项 is not really encouraged by the US government 为正解。\n"
            "［错项排除］[B] is not competitive enough with regard to its cost（成本上不够有竞争力）与第二段成本大跌相反；[C] will bring the US closer to other countries（使美国与其他国家更紧密）缺乏依据；[D] will accelerate global environmental change（加速全球环境变化）曲解了减缓气候变化（slowing climate change）的本意。"
        ),

        # Q31-Q35 (Reading Text 3)
        (
            "According to Paragraph 1, Facebook acquired WhatsApp for its",
            [
                ("A", "digital products"),
                ("B", "quality service"),
                ("C", "physical assets"),
                ("D", "user information")
            ],
            "D",
            "［考点提炼］事实细节题＋核心意图识别。\n"
            "［解题思路］根据定位词 Paragraph 1 与 Facebook acquired WhatsApp 定位至第一段末句：...acquire the WhatsApp messaging service, which doesn't have any physical product at all. What WhatsApp offered Facebook was an intricate and finely detailed web of its users' friendships and social lives。这表明 WhatsApp 没有任何实体产品，它能给 Facebook 带来的正是由用户关系网络构成的详尽用户数据与社交生活信息。D项 user information 为其高度提炼。\n"
            "［错项排除］[A] digital products（数字产品）与[C] physical assets（实体资产）与原文 doesn't have any physical product at all 矛盾；[B] quality service（优质服务）只是表面现象，并非两年前斥资收购的核心资产。"
        ),
        (
            "Linking phone numbers to Facebook identities may",
            [
                ("A", "worsen political disputes"),
                ("B", "mislead the European commission"),
                ("C", "pose a risk to Facebook users"),
                ("D", "mess up customer records")
            ],
            "C",
            "［考点提炼］事实细节题＋后果推断。\n"
            "［解题思路］根据定位词 Linking phone numbers to Facebook identities 定位至第二段：Facebook 违背承诺将手机号与社交身份关联，即使不知道消息内容，了解谁与谁通信也是极其泄密的（enormously revealing），后文以政界丑闻和用户购买记录为例，说明个人隐私面临严重泄露风险。C项 pose a risk to Facebook users（对 Facebook 用户构成风险）准确概括了其潜在危害。\n"
            "［错项排除］[A] worsen political disputes（加剧政治争端）属于举例中的背景修辞，非主干影响；[B] mislead the European commission（误导欧盟委员会）是收购时的违约行为，非绑定账号的直接后果；[D] mess up customer records（弄乱客户记录）违背原文记录变得极具价值的表述。"
        ),
        (
            "According to the author, competition law",
            [
                ("A", "should serve the new market powers"),
                ("B", "may worsen the economic imbalance"),
                ("C", "cannot keep pace with the changing market"),
                ("D", "should not provide just one legal solution")
            ],
            "C",
            "［考点提炼］作者观点题＋同义转换。\n"
            "［解题思路］根据定位词 competition law 定位至第三段第三、四句：For one thing, it is very slow compared to the pace of change within the digital economy. By the time a problem has been addressed and remedied it may have vanished in the marketplace...。作者明确指出反垄断法非常迟缓，根本赶不上数字经济的变化节奏。C项 cannot keep pace with the changing market（跟不上市场的变化步伐）是对 very slow compared to the pace of change 的精准改写。\n"
            "［错项排除］[A] should serve the new market powers（应当服务新的市场力量）违背反垄断法监管市场的宗旨；[B] may worsen the economic imbalance（可能加剧经济失衡）无中生有；[D] should not provide just one legal solution（不应只提供一种法律方案）偏离文意。"
        ),
        (
            "Competition law as presently interpreted can hardly protect Facebook users because",
            [
                ("A", "they are not financially reliable"),
                ("B", "they are not defined as customers"),
                ("C", "the services are generally digital"),
                ("D", "the services are paid for by advertisers")
            ],
            "B",
            "［考点提炼］事实细节题＋因果逻辑。\n"
            "［解题思路］根据题干定位至第三段第六、七句：Competition law as presently interpreted deals with financial disadvantage to consumers and this is not obvious when the users of these services don't pay for them. The users of their services are not their customers. That would be the people who buy advertising from them...。作者指出，现行反垄断法关注的是消费者的经济损失，而普通用户免费使用平台，并非法律定义的“客户”（真正的客户是广告商）。B项 they are not defined as customers 直接对应 The users of their services are not their customers。\n"
            "［错项排除］[A] they are not financially reliable（他们在经济上不可靠）曲解了用户不付费；[C] the services are generally digital（服务普遍是数字化的）不是反垄断法难以保护的根本法律原因；[D] the services are paid for by advertisers（服务由广告商买单）是客观商业模式，但法律保护缺失的核心在于用户未被界定为客户。"
        ),
        (
            "The ants analogy is used to illustrate",
            [
                ("A", "a typical competition pattern among digital giants"),
                ("B", "a win-win business model between digital giants"),
                ("C", "the benefits provided for digital giants' customers"),
                ("D", "the relationship between digital giants and their users")
            ],
            "D",
            "［考点提炼］写作手法题＋比喻类比说明。\n"
            "［解题思路］根据定位词 ants analogy 定位至第四段第二、三句：Just as some ants farm the bugs called aphids for the honeydew they produce... so Google farms us for the data that our digital lives yield. Ants keep predatory insects away... Gmail keeps the spammers out... It doesn't feel like a human or democratic relationship...。作者借蚂蚁饲养蚜虫吸取蜜露并提供保护的共生关系，形象比喻数字巨头通过提供邮件等服务圈养用户以获取数据的控制与剥削关系。D项 the relationship between digital giants and their users 精确揭示了比喻所阐明的对象。\n"
            "［错项排除］[A] a typical competition pattern among digital giants（数字巨头间的竞争模式）与[B] a win-win business model between digital giants（数字巨头间的双赢模式）均将对象错定为巨头之间；[C] the benefits provided for digital giants' customers（为数字巨头客户提供的利益）偏离了巨头与普通数据用户之间的关系本质。"
        ),

        # Q36-Q40 (Reading Text 4)
        (
            "The key to mastering the art of deep work is to",
            [
                ("A", "list your immediate tasks"),
                ("B", "make specific daily plans"),
                ("C", "keep to your focus time"),
                ("D", "seize every minute to work")
            ],
            "C",
            "［考点提炼］事实细节题＋核心要素识别。\n"
            "［解题思路］根据定位词 key to mastering the art of deep work 定位至第二段末句：Whichever approach, the key is to determine your length of focus time and stick to it（无论哪种方法，关键都在于确定专注时间的长短并坚持下去）。stick to 意为“坚持”，与 keep to 同义。C项 keep to your focus time（坚守你的专注时间）是原句的直接对应正解。\n"
            "［错项排除］[A] list your immediate tasks（列出眼前的任务）与[B] make specific daily plans（制定具体每日计划）在后文均被指出存在弊端；[D] seize every minute to work（抓紧每分每秒工作）曲解了新闻工作者式在有空时专注工作的内涵。"
        ),
        (
            "The study in the early 1980s cited by Harford shows that",
            [
                ("A", "daily schedules are indispensable to studying"),
                ("B", "students are hardly motivated by monthly goals"),
                ("C", "detailed plans may not be as fruitful as expected"),
                ("D", "distractions may actually increase efficiency")
            ],
            "C",
            "［考点提炼］事实细节题＋同义转换。\n"
            "［解题思路］根据定位词 study in the early 1980s 与 Harford 定位至第五段首句：While the researchers assumed that the well-structured daily plans would be most effective when it came to the execution of tasks, they were wrong: the detailed daily plans demotivated students。研究表明，原本以为最详尽的每日计划最有效，事实证明却适得其反，详细计划反而打击了学生积极性。C项 detailed plans may not be as fruitful as expected（详尽的计划可能不如预期的那样有成效）准确表达了实验结论。\n"
            "［错项排除］[A] daily schedules are indispensable to studying（每日日程对学习必不可少）与实验结论相反；[B] students are hardly motivated by monthly goals（学生很难受月度目标激励）事实相反，月度目标组表现更好；[D] distractions may actually increase efficiency（干扰可能提高效率）是对不可避免干扰的错误解读。"
        ),
        (
            "According to Newport, idleness is",
            [
                ("A", "an essential factor in accomplishing any work"),
                ("B", "an effective way to save time and energy"),
                ("C", "a major contributor to physical health"),
                ("D", "a desirable mental state for busy people")
            ],
            "A",
            "［考点提炼］作者观点题＋同义转换。\n"
            "［解题思路］根据定位词 Newport 与 idleness 定位至第六段末句引述：[idleness] is, paradoxically, necessary to getting any work done, he argues（闲暇看似矛盾，实则是完成任何工作所必需的）。necessary to getting any work done 意即“完成任何工作所必不可少的”。A项 an essential factor in accomplishing any work（完成任何工作中不可或缺的要素）是对原文的完美同义转换。\n"
            "［错项排除］[B] an effective way to save time and energy（节省时间和精力的有效方式）偏离文意，闲暇旨在恢复精力而非单纯节约时间；[C] a major contributor to physical health（身体健康的主要贡献者）借比喻维生素D进行过度引申；[D] a desirable mental state for busy people（忙碌人群理想的心态）未触及“完成工作所必需”的实质。"
        ),
        (
            "Pillay believes that our brains' shift between being focused and unfocused",
            [
                ("A", "can result in psychological well-being"),
                ("B", "can bring about greater efficiency"),
                ("C", "is aimed at better balance in work"),
                ("D", "is driven by task urgency")
            ],
            "B",
            "［考点提炼］事实细节题＋同义改写。\n"
            "［解题思路］根据定位词 Pillay 与 shift between being focused and unfocused 定位至第七段第二句：When our brains switch between being focused and unfocused on a task, they tend to be more efficient（当我们的大脑在一项任务上于专注与非专注状态之间切换时，往往效率更高）。B项 can bring about greater efficiency（能够带来更高的效率）是对 tend to be more efficient 的直接同义置换。\n"
            "［错项排除］[A] can result in psychological well-being（能够带来心理健康）无中生有；[C] is aimed at better balance in work（旨在更好平衡工作）并非大脑机制的目标；[D] is driven by task urgency（受任务紧迫性驱动）偏离原文。"
        ),
        (
            "This text is mainly about",
            [
                ("A", "the key to eliminating distractions"),
                ("B", "the cause of the lack of focus time"),
                ("C", "ways to relieve the tension of busy life"),
                ("D", "approaches to getting more done in less time")
            ],
            "D",
            "［考点提炼］主旨大意题＋篇章宏观归纳。\n"
            "［解题思路］通读全文，文章开篇提出 Cal Newport 克服盲目忙碌陷阱的“深度工作”理念，第二段阐述掌握深度工作的多种途径（approaches to mastering the art of deep work），第三段提出高效日程规划以在更少时间内完成更多工作（get more done in less time），第四、五段探讨每日任务清单的灵活安排（Another approach to getting more done in less time），第六、七、八段阐明结合适当闲暇与大脑切换以实现高效产出。全文核心贯穿于如何在较少时间内完成更多工作的科学方法与途径。D项 approaches to getting more done in less time（在更少时间内完成更多工作的方法）为文章最佳主旨概括。\n"
            "［错项排除］[A] the key to eliminating distractions（消除干扰的关键）与[B] the cause of the lack of focus time（缺乏专注时间的原因）以及[C] ways to relieve the tension of busy life（缓解忙碌生活紧张感的方法）均仅涉及局部细节或片面解读，无法涵盖整篇探讨工作效能方法的宏观架构。"
        ),

        # Q41-Q45 (Reading Part B)
        (
            "Choose the most suitable subheading for section [41]:",
            [
                ("A", "Just say it"),
                ("B", "Be present"),
                ("C", "Skip the small talk"),
                ("D", "Ask for an opinion"),
                ("E", "Find the \"me too\"s"),
                ("F", "Name, places, things"),
                ("G", "Pay a unique compliment")
            ],
            "A",
            "［考点提炼］新题型小标题匹配。\n"
            "［解题思路］[41]段描述在陌生人面前想说话却卡在喉咙不知如何开口的心理状态，作者给出的建议是：just get it out... So keep it simple: \"Hi\", \"Hey\" or \"Hello\"... put on a big smile and just say \"Hi\"（大胆说出来，保持简单直接说声嗨）。A项 Just say it（想说就说/直接说出口）与段落主旨和原词 just say \"Hi\" 完美匹配。\n"
            "［错项排除］段落核心是克服开不了口的恐惧直接说话，而非泛泛寒暄或讨好夸奖，其他选项无法概括该段。"
        ),
        (
            "Choose the most suitable subheading for section [42]:",
            [
                ("A", "Just say it"),
                ("B", "Be present"),
                ("C", "Skip the small talk"),
                ("D", "Ask for an opinion"),
                ("E", "Find the \"me too\"s"),
                ("F", "Name, places, things"),
                ("G", "Pay a unique compliment")
            ],
            "C",
            "［考点提炼］新题型小标题匹配。\n"
            "［解题思路］[42]段指出人们常陷入枯燥无聊的日常寒暄套话中（got stuck in the rut of \"hi\", \"hello\", \"how are you?\" and \"what's going on?\"），导致谈话无法给人留下深刻印象，因此建议 don't be afraid to ask more personal questions（不要害怕问更个性化、深入的问题）。C项 Skip the small talk（跳过闲聊/略过套路寒暄）精准契合该段核心。\n"
            "［错项排除］[D] Ask for an opinion 虽涉及提问，但原文建议是询问个性化问题以突破表面套话，并非征求对方意见。"
        ),
        (
            "Choose the most suitable subheading for section [43]:",
            [
                ("A", "Just say it"),
                ("B", "Be present"),
                ("C", "Skip the small talk"),
                ("D", "Ask for an opinion"),
                ("E", "Find the \"me too\"s"),
                ("F", "Name, places, things"),
                ("G", "Pay a unique compliment")
            ],
            "E",
            "［考点提炼］新题型小标题匹配。\n"
            "［解题思路］[43]段明确指出初次见面时，要努力寻找双方的共同点（make an effort to find the things which you and that person have in common），并从共同点展开交谈。E项 Find the \"me too\"s（寻找“我也一样”的共鸣点）正是“寻找共同之处”的生动地道表达。\n"
            "［错项排除］其他选项均未涉及双方寻找共同爱好或经历的内容。"
        ),
        (
            "Choose the most suitable subheading for section [44]:",
            [
                ("A", "Just say it"),
                ("B", "Be present"),
                ("C", "Skip the small talk"),
                ("D", "Ask for an opinion"),
                ("E", "Find the \"me too\"s"),
                ("F", "Name, places, things"),
                ("G", "Pay a unique compliment")
            ],
            "B",
            "［考点提炼］新题型小标题匹配。\n"
            "［解题思路］[44]段举出低头看手机、心不在焉听人倾诉的反面事例，进而提出正向建议：just be in that communication wholeheartedly. Make eye contact（全心全意投入交流中，保持目光接触）。B项 Be present（专注当下/全心投入）精准对应 be in that communication wholeheartedly。\n"
            "［错项排除］该段强调的是倾听与交谈时的专注投入态度，与其他选项无关。"
        ),
        (
            "Choose the most suitable subheading for section [45]:",
            [
                ("A", "Just say it"),
                ("B", "Be present"),
                ("C", "Skip the small talk"),
                ("D", "Ask for an opinion"),
                ("E", "Find the \"me too\"s"),
                ("F", "Name, places, things"),
                ("G", "Pay a unique compliment")
            ],
            "F",
            "［考点提炼］新题型小标题匹配。\n"
            "［解题思路］[45]段讲述再次相遇却忘记对方名字的尴尬，并建议：remember the little details of the people you met or you talked with; perhaps the places they have been to, the places they want to go, the things they like, the things they hate...（记住对方的细枝末节：去过或想去的地方、喜欢或讨厌的事物）。F项 Name, places, things（名字、地点、事物）准确归纳了段落所列举的细节记忆范畴。\n"
            "［错项排除］[G] Pay a unique compliment 虽提及给人关注，但段落落脚点在于记住对方去过的地方和喜好事物等具体细节，而非赞美对方。"
        )
    ]

    # Update questions in data
    questions = data['questions']
    assert len(questions) == 45, f"Expected 45 questions, got {len(questions)}"

    for i in range(45):
        q = questions[i]
        stem, opts, ans, expl = q_data[i]
        q_num = i + 1
        q['question_number'] = q_num
        q['sort_order'] = q_num
        if q_num <= 20:
            score = 0.5
            q_type = 'cloze_item'
        else:
            score = 2.0
            q_type = 'reading_item'
        q['score'] = score
        q['points'] = score
        q['question_type'] = q_type
        q['q_type'] = q_type
        q['stem'] = stem
        q['options'] = [{'key': k, 'text': t, 'value': k} for k, t in opts]
        q['answer'] = ans
        q['correct_answer'] = ans
        q['explanation'] = expl

    # Save to JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Successfully built and saved 2018 ky2 gold data to JSON!")

if __name__ == '__main__':
    build_gold_exam()
