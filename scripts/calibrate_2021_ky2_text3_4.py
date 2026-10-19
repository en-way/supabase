import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

JSON_PATH = 'public/data/exams/4ebd819e-c832-5890-9048-ba16040a5607.json'

data = json.load(open(JSON_PATH, encoding='utf-8'))

# 1. Update Passages
p4_text = """When Microsoft bought task management app Wunderlist and mobile calendar Sunrise in 2015, it picked two newcomers that were attracting considerable buzz in Silicon Valley. Microsoft's own Office dominates the market for "productivity" software, but the start-ups represented a new wave of technology designed from the ground up for the smartphone world.

Both apps, however, were later scrapped, after Microsoft said it had used their best features in its own products. Their teams of engineers stayed on, making them two of the many "acqui-hires" that the biggest companies have used to feed their great hunger for tech talent.

To Microsoft's critics, the fates of Wunderlist and Sunrise are examples of a remorseless drive by Big Tech to chew up any innovative companies that lie in their path. "They bought the seedlings and closed them down," complained Paul Arnold, a partner at San Francisco-based Switch Ventures, putting an end to businesses that might one day turn into competitors. Microsoft declined to comment.

Like other start-up investors, Mr. Arnold's own business often depends on selling start-ups to larger tech companies, though he admits to mixed feelings about the result: "I think these things are good for me, if I put my selfish hat on. But are they good for the American economy? I don't know."

The US Federal Trade Commission says it wants to find the answer to that question. This week, it asked the five most valuable US tech companies for information about their many small acquisitions over the past decade. Although only a research project at this stage, the request has raised the prospect of regulators wading into early-stage tech markets that until now have been beyond their reach.

Given their combined market value of more than $5.5 trillion, rifling through such small deals — many of them much less prominent than Wunderlist and Sunrise — might seem beside the point. Between them, the five biggest tech companies have spent an average of only $3.4 billion a year on sub-$1 billion acquisitions over the past five years — a drop in the ocean compared with their massive financial reserves, and the more than $130 billion of venture capital that was invested in the US last year.

However, critics say the big companies use such deals to buy their most threatening potential competitors before their businesses have a chance to gain momentum, in some cases as part of a "buy and kill" tactic to simply close them down."""

p5_text = """We're fairly good at judging people based on first impressions, thin slices of experience ranging from a glimpse of a photo to five-minute interaction, and deliberation can be not only extraneous but intrusive. In one study of the ability she called "thin slicing," the late psychologist Nalini Ambady asked participants to watch silent 10-second video clips of professors and to rate the instructor's overall effectiveness. Their ratings correlated strongly with students' end-of-semester ratings. Another set of participants had to count backward from 1,000 by nines as they watched the clips, occupying their conscious working memory. Their ratings were just as accurate, demonstrating the intuitive nature of the social processing.

Critically, another group was asked to spend a minute writing down reasons for their judgment, before giving the rating. Accuracy dropped dramatically. Ambady suspected that deliberation focused them on vivid but misleading cues, such as certain gestures or utterances, rather than letting the complex interplay of subtle signals form a holistic impression. She found similar interference when participants watched 15-second clips of pairs of people and judged whether they were strangers, friends, or dating partners.

Other research shows we're better at detecting deception from thin slices when we rely on intuition instead of reflection. "It's as if you're driving stick shift," says Judith Hall, a psychologist at Northeastern University, "and if you start thinking about it too much, you can't remember what you're doing. But if you go on automatic pilot, you're fine. Much of our social life is like that."

Thinking too much can also harm our ability to form preferences. College students' ratings of strawberry jams and college courses aligned better with experts' opinions when the students weren't asked to analyze their rationale. And people made car-buying decisions that were both objectively better and more personally satisfying when asked to focus on their feelings rather than on details, but only if the decision was complex — when they had a lot of information to process.

Intuition's special powers are unleashed only in certain circumstances. In one study, participants completed a battery of eight tasks, including four that tapped reflective thinking (discerning rules, comprehending vocabulary) and four that tapped intuition and creativity (generating new products or figures of speech). Then they rated the degree to which they had used intuition ("gut feelings," "hunches," "my heart"). Use of their gut hurt their performance on the first four tasks, as expected, and helped them on the rest. Sometimes the heart is smarter than the head."""

for p in data['passages']:
    if p['id'] == 'fbd49496-cbd6-5676-ad1d-29e41cd6aad3':
        p['content'] = p4_text
        print("Updated Passage 4 (Text 3)")
    elif p['id'] == 'c45660d2-1cee-5a4f-8852-8203bf51b493':
        p['content'] = p5_text
        print("Updated Passage 5 (Text 4)")

# 2. Update Questions Q31 to Q40
q_updates = {
    31: {
        "stem": "What is true about Wunderlist and Sunrise after their acquisitions?",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "Their engineers were retained.", "value": "A"},
            {"key": "B", "text": "Their market values declined.", "value": "B"},
            {"key": "C", "text": "Their tech features improved.", "value": "C"},
            {"key": "D", "text": "Their products were re-priced.", "value": "D"}
        ],
        "explanation": """［精准定位］由after their acquisitions定位至第二段首句中later。该段指出Wunderlist与Sunrise被收购后的情况：软件被下架（①句），工程师被留用（②句），故[A]正确。

［命题解密］[A] Their engineers were retained 同义改写第二段②句 Their... engineers stayed on。
[B]源于第六段①句their... market value，但此处谈论的是“五大科技巨头的市场价值巨大”而非“Wunderlist与Sunrise的市场价值下滑”。[C]张冠李戴：由第二段①句“微软将它们的最佳性能融入自身产品”，可知科技性能得到提升的对象为微软自家产品而非被收购的两款应用。[D]利用首段①句“微软收购两款软件”与常识“换东家后会重新定价”捏造，但“重新定价”所含的信息“仍在市场上销售”与第二段①句所含的信息“被下架”相悖。

［技巧总结］四个选项的指向性很明确、辨识度也很高，对于此类事实细节题按照“回文定位法”最为合适。根据题干Wunderlist and Sunrise after their acquisitions直接定位至第二段，该段两句成段，第一句指向“软件的命运（下架）”，第二句指向“软件工程师的命运（留用）”，与之相匹配的唯有[A]，其余各选项要么捏造，要么偷换概念。"""
    },
    32: {
        "stem": "Microsoft's critics believe that the big tech companies tend to ________.",
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": "exaggerate their product quality", "value": "A"},
            {"key": "B", "text": "eliminate their potential competitors", "value": "B"},
            {"key": "C", "text": "treat new tech talent unfairly", "value": "C"},
            {"key": "D", "text": "ignore public opinions", "value": "D"}
        ],
        "explanation": """［精准定位］由题干Microsoft's critics与big tech companies直接定位至第三段。该段①句点明批评者的总观点：科技巨头会蚕食挡道的创新公司。②句具体阐释①句：他们（科技巨头）将那些有朝一日可能会成长为竞争对手的企业扼杀于摇篮。可见［B］正确。

［命题解密］［B］eliminate their potential competitors同义概述了第三段②句的putting an end to businesses that might one day turn into competitors，阐明了①句中chew up any innovative companies that lie in their path的内涵。
［A］对第二段①句said... best features in its own products断章取义，将文意“表示自家产品借鉴了被购软件的最佳性能”曲解为“夸耀自家产品最佳，夸大产品质量”，且将微软个体的行为泛化为所有大型科技公司的行为。［C］歪曲第二段②句中大型科技公司对科技人才的态度：将原文的“求贤若渴（their great hunger for tech talent）”反向窜改为“不公正对待人才（treat... unfairly）”。［D］将第三段末句declined to comment所暗藏的“礼貌拒绝置评（decline：refuse politely to do sth）”窜改为“忽略（ignore: pay no attention to sth）”。此外，［A］［C］［D］均为作者陈述的事实，并非题干所问的“批评者的观点”。

［技巧总结］本题考查人物观点，解答关键是锁定人物观点表达句。首先根据Microsoft's critics直接锁定第三段①句，该句中a remorseless drive by Big Tech to chew up any innovative companies that lie in their path明确表达科技巨头的倾向性行为（蚕食将阻碍其发展的任何创新公司），与之相匹配的唯有［B］。"""
    },
    33: {
        "stem": "Paul Arnold is concerned that small acquisitions might ________.",
        "correct_answer": "C",
        "options": [
            {"key": "A", "text": "weaken big tech companies", "value": "A"},
            {"key": "B", "text": "worsen market competition", "value": "B"},
            {"key": "C", "text": "harm the national economy", "value": "C"},
            {"key": "D", "text": "discourage start-up investors", "value": "D"}
        ],
        "explanation": """［精准定位］首先由题干中Paul Arnold定位至第三、四段，再由试题命制顺序（上题已针对第三段设题）可进一步定位至第四段。该段首先指出，对于“科技巨头收购初创企业”，阿诺德内心五味杂陈。随后点明其担忧的原因：这种小额收购可能会危害美国经济。可见，［C］正确。

［命题解密］题干+［C］是对第四段③句疑问句式But are they good for the American economy?的正确解读，harm体现了阿诺德的质疑态度：这类收购可能不利于美国经济。
［A］［B］均与第三段②句阿诺德的观点“科技巨头在初创企业发展为竞争者之前将其消灭”的言外之意相悖：这些小额收购不是削弱而是巩固大型科技公司现有的地位；不是加剧市场竞争，而是阻碍新竞争对手产生、保持市场竞争的现状。［D］与第四段②句阿诺德的观点“这些小额收购有利于我（阿诺德代表初创企业投资者）”所体现的积极意义相悖。

［技巧总结］本题依然考查人物观点，但解答关键更在于利用人物站位排除部分干扰项，然后再借助其核心观点句锁定正确选项。首先，文中Paul Arnold作为微软批评者的代表人物出现，对微软所代表的做法“科技巨头在初创企业成长为竞争对手前将其收购（巩固科技巨头的垄断地位，杜绝新的市场竞争产生）”持反对态度，应首先排除［A］［B］。接着，根据题干中concerned所传递出的“疑虑，担忧”锁定到第四段中情感表达词mixed feelings以及疑问句式are they good for the American economy?所传递出的“对美国经济的担忧”，从而锁定正确答案为［C］。"""
    },
    34: {
        "stem": "The US Federal Trade Commission intends to ________.",
        "correct_answer": "C",
        "options": [
            {"key": "A", "text": "limit Big Tech's expansion", "value": "A"},
            {"key": "B", "text": "encourage research collaboration", "value": "B"},
            {"key": "C", "text": "examine small acquisitions", "value": "C"},
            {"key": "D", "text": "supervise start-ups' operation", "value": "D"}
        ],
        "explanation": """［精准定位］根据题干关键词Federal Trade Commission定位至第五段。该段①②句指出，FTC为了找到“科技巨头收购初创企业是否对美国经济不利”的答案，要求“五大科技公司提供其过去十年所进行的所有小额收购的相关信息”。可见，FTC意欲审查科技巨头小额收购行为，以防对美国经济不利，［C］正确。

［命题解密］［C］是对②句中asked... for information about their many small acquisitions的同义转述。
［A］由②③句中“要求提供”和“插手干预”等信息过度推导得来，文中无据可依。［B］对③句only a research project（只是一个研究项目）断章取义，但句中实际指向“FTC目前尚处研究调查阶段，尚未上升到政策措施等高度”，并未提及“政府要鼓励合作式研究”。［D］将③句“干预早期科技市场”错误理解为监管初创企业，句中实际指向“监督科技巨头对初创企业的收购”。

［技巧总结］本题考查FTC的行为目的，可搜寻文内有关目的的表达词，找到答案信息，即根据第五段①句中wants to可锁定其后find the answer to that question，而追溯前文发现that question指向上段末句are they good for the American economy（they指向these things/selling start-ups to larger tech companies，进而可知small acquisitions），进而可知FTC意在调查“小额收购对美国经济的影响”，与之相匹配的唯有［C］，且由目标句（①句）后的解释说明句（②句）“FTC开始要求五大科技巨头提供其过去十年来的小额收购信息”可进一步佐证。"""
    },
    35: {
        "stem": "For the five biggest tech companies, their small acquisitions have ________.",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "brought little financial pressure", "value": "A"},
            {"key": "B", "text": "raised few management challenges", "value": "B"},
            {"key": "C", "text": "set an example for future deals", "value": "C"},
            {"key": "D", "text": "generated considerable profits", "value": "D"}
        ],
        "explanation": """［精准定位］根据题目关键词the five biggest tech companies可定位至第六段②句。该句表明，五大公司加起来每年用于小额收购的资金仅有34亿美元，同它们的金融储备相比，这笔钱无异于沧海一粟。再加上具体数字（3.4 billion vs 130 billion）的对比可知，五大公司财力雄厚，这些小额收购并未对公司财政造成多少压力，故［A］正确。

［命题解密］［A］是对第六段②句中only $3.4 billion a year, a drop in the ocean compared with their massive financial reserves的合理推断。
［B］由常识“公司并购之后带来的人员增长将会是一个管理问题”捏造，但文中并未提到任何“管理问题”。［C］由第三段②句中examples, in their path望文生义，但该句实质指向“微软收购Wunderlist/Sunrise是科技巨头收购初创企业的众多案例中的两例”而非“为这类收购树立了榜样”。［D］则将五大公司的巨额利润归功于他们所进行的小额收购，而文中并没有出现相应的因果联系。

［技巧总结］本题考查“小型收购对科技巨头”的影响，实质于长难句处设题，意在考查学生明确复杂关系、了解特殊修辞、理解长难句的能力，解答关键在分解长难句主体，明确其语义要点。第六段②句主体信息实为the five biggest tech companies（主语）have spent an average of only $3.4 billion a year（谓语部分）— a drop in the ocean compared with their massive financial reserves...（同位语）。根据其中的情感表达词only、a drop in the ocean、massive不难锁定正确项为［A］。"""
    },
    36: {
        "stem": "Nalini Ambady's study deals with ________.",
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": "the power of people's memory", "value": "A"},
            {"key": "B", "text": "the reliability of first impressions", "value": "B"},
            {"key": "C", "text": "instructor-student interaction", "value": "C"},
            {"key": "D", "text": "people's ability to influence others", "value": "D"}
        ],
        "explanation": """［精准定位］由题干中的Nalini Ambady's study定位至第一、二段安巴迪的“行为薄片撷取”能力研究。第一段①句指出人们擅长通过第一印象即thin slices of experience评判他人，②句顺而指出安巴迪就thin slicing这一能力进行了研究，说明安巴迪的研究与人们的第一印象有关。再结合第一段③⑤句、第二段②句所指出的“安巴迪将参与者和学生对教师的评分进行对比，评估参与者对教师的第一印象的准确性”，可知安巴迪的研究涉及“第一印象的可靠性”，故［B］正确。

［命题解密］正确项［B］是对第一、二段中安巴迪的研究内容的正确概述，其中first impressions对应主题词first impressions、thin slices of experience，reliability是对correlated strongly、just as accurate、Accuracy dropped dramatically的高度概括。
［A］将第一段④句中对参与者的干扰occupying their conscious working memory断章取义为安巴迪的研究涉及人们的记忆，但原文并未提及记忆的力量。［C］对第一段②③句中的关键信息professors, instructor, students强加关联，捏造出安巴迪的研究涉及“教师与学生的互动”。［D］将第二段①②句中“参与者被要求写下评分理由，导致他们的评分准确性大幅下降”这一研究发现错误解读为“研究人员影响了参与者的判断”，而原文的真实含义是“写出评分理由”这一思考行为降低了评分的准确性。

［技巧总结］本题考察对细节信息进行整合概括的能力，解题时需要厘清段内、段际逻辑关系。
1. 从段内逻辑来看，第一段①句指出第一印象即“经验薄片（thin slices of experience）”，②句直接说明安巴迪的研究关乎“行为薄片撷取（thin slicing）”，从两者的重合内容thin slice可推断安巴迪的研究关乎“第一印象”。另外，第一段②③句和④⑤句呈现相似的句间关系：先说明参与者在不同条件下根据第一印象对教师评分，后描述该评分的准确性。这也说明安巴迪的研究重点是“第一印象的准确性”，由此锁定答案［B］。
2. 从段际逻辑来看，第一、二段都涉及安巴迪的研究，但两段之间构成对比关系：第一段的前两组参与者情况表明，当参与者根据第一印象评分时，评分结果往往非常准确；而第二段的第三组参与者（①②句）和另一项研究（④句）表明，过多思考反而会干扰我们判断的准确性。将两段逻辑串联可知，这两段的两项研究都在论证首段首句：我们很擅长运用第一印象来评判他人，此时深思不仅没有必要，而且会造成干扰。由此，进一步锁定答案［B］。［A］［C］［D］均运用各项研究对参与者的不同要求捏造干扰，可排除。"""
    },
    37: {
        "stem": "In Ambady's study, rating accuracy dropped when participants ________.",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "focused on specific details", "value": "A"},
            {"key": "B", "text": "gave the rating in limited time", "value": "B"},
            {"key": "C", "text": "watched shorter video clips", "value": "C"},
            {"key": "D", "text": "discussed with one another", "value": "D"}
        ],
        "explanation": """［精准定位］根据题干关键词Ambady's study和rating accuracy dropped定位至第二段②句。梳理上下文逻辑可知，①句指出导致评分准确率下降的直接原因是“参与者需写下评分原因”，③句中安巴迪推测出现这一结果是因为“deliberation focused them on vivid but misleading cues（深思使他们将精力集中于那些生动但具有误导性的信号）”，其中focused them on vivid but misleading cues表明参与者将注意力放在了具体细节上，对应［A］选项中focused on specific details，因此［A］正确。

［命题解密］正确项［A］是对第二段③句安巴迪对实验结果的解读deliberation focused them on vivid... cues的同义改写。
［B］将第二段①句中的spend a minute writing down their reasons误当作对评分时间的限制，实际上这是对参与者写下评分理由的时间限制，且该限制也并非评分准确性下降的原因。［C］根据第一段②句中的10-second video clips和第二段④句中的15-second clips臆断出视频的时长影响了评分的准确性，实际上视频的时长并非研究重点。［D］由第一段④句的Another set和第二段①句的another group错误推断出one another，在此基础上捏造出“参与者需相互讨论，给出评分”，原文并未涉及相关描述。

［技巧总结］因果细节题主要考查对上下文因果逻辑的把握，需要正确梳理句间逻辑。如本题，第二段①句描述评分条件：参与者需要写出评分理由；②句描述评分结果：此时评分准确性下降；③句介绍安巴迪分析的原因：参与者为写出理由而进行了深思（deliberation），深思时只关注生动的细节信息，忽略了整体印象。浏览选项后可锁定［A］选项为对评分下降原因的正确描述，其他三个选项均属主观臆断，可排除。"""
    },
    38: {
        "stem": "Judith Hall mentions driving to show that ________.",
        "correct_answer": "A",
        "options": [
            {"key": "A", "text": "reflection can be distracting", "value": "A"},
            {"key": "B", "text": "memory may be selective", "value": "B"},
            {"key": "C", "text": "social skills must be cultivated", "value": "C"},
            {"key": "D", "text": "deception is difficult to detect", "value": "D"}
        ],
        "explanation": """［精准定位］由题干中的人名Judith Hall与关键词driving定位至第三段②③句。朱迪斯•霍尔称，若一个人开着手动挡车，如果他反复思考如何挂挡，就会导致他忘记本来是要做什么。如果他只是不假思索地按照习惯操作，就会开得很顺利。两种情形的对比表明，依靠直觉往往比较顺利，而深思熟虑可能反而会导致注意力分散，从而影响判断。另外，朱迪斯•霍尔的观点以It's as if...开始，表明该观点是为支撑上文观点服务的，因此我们也可以借助首句内容解题。首句指出，当我们依靠直觉而非深思时，更能从“行为薄片”中觉察到欺骗；言外之意即直觉比深思更可靠。［A］符合题意。

［命题解密］正确项［A］是对朱迪斯•霍尔比较手动挡汽车驾驶员的两种心态之目的的正确解读。
［B］对②句you can't remember what you're doing断章取义。该句意在说明“深入思考会将注意力导向其他事物，忘记原本所要做的事”，而非“记忆具有选择性”。［C］由末句碎片信息“社交生活”捏造而来，本文并未论及获得社交技能的途径。［D］由首句中we're better at detecting deception逆向推导而来，但该句意在指出依靠直觉作出的判断比依靠深思更准确。

［技巧总结］人物观点+写作目的题。解答此类题时，除直接从人物观点本身推断出答案外，亦可借助论据（人物观点）与论点（作者观点）的关系进行判断：若论据是为支撑论点，此时两者意思相近；若提出论据的目的在于树靶驳斥，则两者意思相反。就本题而言，要判断作者引用朱迪斯•霍尔之观点的目的在于批驳还是引证，须先了解第三段与前两段的逻辑关系。首先，由于第三段首句中没有表转折的词，可初步推断本段与前两段为顺承关系。仔细分析也可得知，前两段作者通过引述研究的结果证明“处理社交类信息时依靠直觉做出的判断更准确，深思反而会对判断造成干扰（interference）”，而进入第三段，作者先在首句中通过引述其他研究发现再次证明“社会生活中直觉判断比深思更准确”，随后又在②③④句中引述朱迪斯•霍尔“驾驶手动挡汽车”的类比进一步阐释该观点。由此可知，朱迪斯•霍尔的言论是作为支撑性论据受到引用，其论点与首句作者观点相似。因此，朱迪斯•霍尔提及驾驶是为了表明（处理社交信息时）深思熟虑反会让人分心。"""
    },
    39: {
        "stem": "When you are making complex decisions, it is advisable to ________.",
        "correct_answer": "D",
        "options": [
            {"key": "A", "text": "collect enough data", "value": "A"},
            {"key": "B", "text": "list your preferences", "value": "B"},
            {"key": "C", "text": "seek expert advice", "value": "C"},
            {"key": "D", "text": "follow your feelings", "value": "D"}
        ],
        "explanation": """［精准定位］根据题干关键词complex decisions定位到第四段末句。该句指出，当人们被要求关注感觉而非细节时，他们做出的购车决定既合理又令自己满意，但只有在这一决定很复杂的情况下方才如此。由此可知，在做复杂决定时，明智的做法是“遵从你的感觉”，故［D］正确。同时排除［A］。

［命题解密］题干+正确项［D］是对第四段末句的正确解读。
［B］项由首句过度推断而来：如果说“考虑得太多会损害我们形成偏好的能力”，那么“（事先）列出偏好”就可以帮助我们做决定。但此种理解误解了首句的语义重心：作者想强调的并非偏好的形成，而是想得太多对形成偏好/做决定这一能力的损害。［C］由②句碎片信息experts' opinions捏造而来。该句实指在不需要深思时，人们对事物的评估与专家意见更一致，也即“（在某些情况下）直觉判断更准确”。

［技巧总结］事实细节题。解答此类题目的关键在于精准定位。对于那些关键词未落在定位句范围内的选项，多数情况下可被认定为干扰项。就本题而言，根据题目关键词complex decisions可定位至第四段末句。细察本句，可发现题干When you are making complex decisions同义改写only if the decision was complex，由此可知题干主句it is advisable to +正确项应复现if条件句的主句people made... details。而又因为［D］follow your feelings同义复现focus on their feelings，“明智的（advisable）”概括关注感觉的结果，即“人们做出的购车决定既合理又令自己满意（people made... satisfying）”，因此［D］正确。题干+［A］所反映之意为“关注细节是明智的”，与作者意思恰恰相反。而［B］项preferences、［C］项expert advice分别源自①②句，不在本题考查的信息范围内，因此排除。"""
    },
    40: {
        "stem": "What can we learn from the last paragraph?",
        "correct_answer": "B",
        "options": [
            {"key": "A", "text": "Generating new products takes time.", "value": "A"},
            {"key": "B", "text": "Intuition may affect reflective tasks.", "value": "B"},
            {"key": "C", "text": "Vocabulary comprehension needs creativity.", "value": "C"},
            {"key": "D", "text": "Objective thinking may boost intuitiveness.", "value": "D"}
        ],
        "explanation": """［精准定位］末段首句指出，直觉的特殊能力只有在特定情形下才能发挥出来。②③④句引用研究发现进一步说明：在一项研究中，参与者要完成四项运用深度思索能力、四项运用直觉与创造力的任务，并为其使用直觉的程度打分。结果发现，使用直觉损害了他们在前四项任务中的表现，而对后四项任务则有所帮助。由此可知，直觉会降低思考性工作的成效，故［B］正确。

［命题解密］正确项［B］是对末段引述的研究发现（④句）的合理解读。
［A］利用②句碎片信息generating new products捏造而来，文中并未涉及创造新产品所消耗时间的多少。［C］张冠李戴。②句明确指出，理解词汇需要运用的是深度思索能力，而创造新产品或修辞格需要的才是创造力。［D］利用第四段③句objectively捏造而来，文中并未论及提升直觉力的方法。

［技巧总结］段落推理题。末段主体部分关注一项研究，结合各选项内容可知本题考查对研究结果的推理和引申。解题时需先确定引入该研究的语境，再在此基础上对研究结果进行解读。具体而言，由于首句指出“直觉的特殊能力只有在特定情形下才能发挥出来”，因此可确定下述研究应就论证“在何种情形下直觉的能力才能发挥出来”而展开。再细看研究本身可知，直觉在需要运用直觉与创造力的任务中发挥了积极作用，而对需要运用深度思索能力的任务的完成产生了负面影响。由此可知［B］正确。另外，本题的提问方式（根据某段可以得知什么？）也很有特点，这种问题实际上考查的是段落主旨或者在主旨基础上的合理推断。以本段为例，本段首句为段落主旨，指出直觉的特殊能力只有在特定情境下才会发挥出来。言外之意，直觉也不是“万能灵药”，有的情况并不适合运用直觉行事。［B］选项符合这一逻辑推理。"""
    }
}

for q in data['questions']:
    so = q['sort_order']
    if so in q_updates:
        u = q_updates[so]
        q['stem'] = u['stem']
        q['correct_answer'] = u['correct_answer']
        q['answer'] = u['correct_answer']
        q['options'] = u['options']
        q['explanation'] = u['explanation']
        print(f"Updated Question Q{so}: Ans={q['correct_answer']}, Stem={q['stem'][:30]}...")

with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully calibrated 2021 ky2 Text 3 & Text 4 in local JSON!")
