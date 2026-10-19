import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 24 Calibration Implementation ===")

DATA_DIR = 'public/data/exams'

EXAM_MAP = {
    '2021_ky1': 'e7dfeb60-9e71-5912-8e2c-0828e345b98c.json',
    '2020_ky1': 'f56943c1-0ba8-58fe-b7d3-061352345067.json',
    '2022_ky2': 'cc4bf627-e456-538f-87e2-4a99ebb613ed.json',
    '2007_ky1': 'e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json',
}

def load_exam(key):
    path = os.path.join(DATA_DIR, EXAM_MAP[key])
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f), path

def save_exam(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

updated_questions = []

# ----------------------------------------------------
# 1. 2021 ky1 Text 4 (Q36 - Q40)
# ----------------------------------------------------
d2021, p2021 = load_exam('2021_ky1')
for q in d2021['questions']:
    so = q['sort_order']
    if so == 36:
        print("[Calibrating] 2021 ky1 Q36")
        q['explanation'] = (
            "［精准定位］第一段①句提出一直以来人们的担忧：宽带运营商会通过偏袒关联网站而打压竞争对手，"
            "以此侵害网络中立性。②句具体列举宽带运营商可能会进行的不公正行为：减缓特定网络流量、"
            "阻断特定网络流量、或对特定互联网公司收取提速费用。由此可知，人们一直担心宽带运营商在对待客户时有失公允，［C］正确。\n\n"
            "［命题解密］正确项［C］show partiality in treating clients 是对第一段①句 favor affiliated websites over their rivals "
            "以及②句 slow down or block ... or charge ... 等不公待遇行为的概括。\n\n"
            "［干扰排除］\n"
            "［A］错将宽带运营商对网络流量的管控（控制网络流量）等同于“控制互联网公司”。\n"
            "［B］将②句所述宽带运营商可能会做出的具体行为之一（减缓特定网络流量）绝对化为“减缓其网络流量”。\n"
            "［D］将宽带运营商“凭借自身垄断地位偏袒自家人、打压对手”的不公正行为曲解为“加剧与对手的竞争”。\n\n"
            "［技巧总结］事实细节题考查对具体信息的理解与概括。正确选项往往是对原文具体列举行为的高度抽象概括。"
        )
        updated_questions.append(('2021_ky1', q['id'], 36))

    elif so == 37:
        print("[Calibrating] 2021 ky1 Q37")
        q['explanation'] = (
            "［精准定位］第二段①句提出网络中立性倡导者的诉求（出台网络中立规则保护网络自由与创新）。"
            "②③句则指出，面对这一诉求，监管部门 FCC 却在 2017 年投票通过了一项解除对宽带运营商监管的规定（FCC repealed net neutrality rules），"
            "即 FCC 采取了反监管立场，故［B］正确。\n\n"
            "［命题解密］正确项［B］takes an anti-regulatory stance 是对第二段②③句 the FCC voted to repeal ... deregulatory move 等内容的同义改写。\n\n"
            "［干扰排除］\n"
            "［A］利用第三段①句提到的一项旧有规定设障，但文中明确指出 FCC 是废除而非坚守旧规定。\n"
            "［C］将第二段所述“废除网络中立规定”曲解为“出台了特别决议”。\n"
            "［D］与第五段①句提到“FCC 极力禁止各州设立各自的网络中立法规”相悖。\n\n"
            "［技巧总结］细节事实题需紧扣核心实体动作，关注关键动词（repeal / deregulate）的情感与立场方向。"
        )
        updated_questions.append(('2021_ky1', q['id'], 37))

    elif so == 38:
        print("[Calibrating] 2021 ky1 Q38")
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = 'It engages in anti-competitive practices.'
        q['explanation'] = (
            "［精准定位］第三段①句指出，某些宽带运营商会进行反竞争行为，比如 AT&T 以牺牲 Netflix 和 Apple TV 的利益为代价，"
            "偏袒自家流媒体服务（favoring its own video-streaming service at the expense of rivals like Netflix and Apple TV+）。"
            "由此可知，AT&T 进行了反竞争行为，［B］正确。\n\n"
            "［命题解密］正确项［B］It engages in anti-competitive practices 是对第三段①句 AT&T favoring its own service at the expense of rivals 的高度概括。\n\n"
            "［干扰排除］\n"
            "［A］反向曲解，AT&T 本身就是在进行不公平竞争，而非保护他人免受不公平竞争。\n"
            "［C］与第三段②句所述“FCC 终止了对 AT&T 等运营商行为的多项调查”相悖。\n"
            "［D］无中生有，文中并未提及 AT&T 追求高质量服务。\n\n"
            "［技巧总结］例证事实题中，关注举例所支撑的观点句。AT&T 作为典型案例，直接印证了句首的 anti-competitive practices。"
        )
        updated_questions.append(('2021_ky1', q['id'], 38))

    elif so == 39:
        print("[Calibrating] 2021 ky1 Q39")
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = 'focuses on trivialities'
        q['explanation'] = (
            "［精准定位］第四段②句指出，帕特丽夏·米利特法官在协同意见书中公正地指出“这一裁决结果与现代宽带服务的现实脱节”"
            "（the result is unhinged from the realities of modern broadband service）。由此可知，［D］正确。\n\n"
            "［命题解密］正确项［D］is out of touch with reality 是对句中 unhinged from the realities of modern broadband service 的同义改写。\n\n"
            "［干扰排除］\n"
            "［A］与［B］对法官指出裁决脱离现实的言论断章取义，歪曲为“关注琐事”或“传达模棱两可的信息”。\n"
            "［C］与第四段①句上诉法院援引过往类似裁决的事实相悖，且并非法官米利特的观点。\n\n"
            "［技巧总结］观点态度题需牢牢锁定观点原句中的核心修饰词（unhinged from reality 即脱节于现实）。"
        )
        updated_questions.append(('2021_ky1', q['id'], 39))

    elif so == 40:
        print("[Calibrating] 2021 ky1 Q40")
        for opt in q['options']:
            if opt['key'] == 'C':
                opt['text'] = 'Rules need to be set to diversify online services.'
            elif opt['key'] == 'D':
                opt['text'] = "Broadband providers' rights should be protected."
        q['explanation'] = (
            "［精准定位］本题考查末段段落主旨与作者核心建议。首句总结事件“法律之争没完没了，FCC 反复无常”并概述建议“亟需国会介入”"
            "（cry out for Congress to act）。②句细述具体建议：国会需赋权 FCC 禁止宽带运营商干预网络流量，并制定明确规则保护网络的开放与创新。"
            "可见［A］符合上述核心论点，故正确。\n\n"
            "［命题解密］正确项［A］是对末段 cry out for Congress to act ... to give the commission authority ... to create clear rules protecting openness 的合理概括。\n\n"
            "［干扰排除］\n"
            "［B］偷换监管对象：应受监管的是宽带运营商，而非 FCC。\n"
            "［C］曲解文意：制定法规的目的是保护开放与创新，而非使线上服务多样化。\n"
            "［D］偷换保护对象：应受保护的是网络开放与公共利益，而非宽带运营商的特权。\n\n"
            "［技巧总结］末段主旨与建议题需立足于全文高度，抓住文章最终的落脚点与呼吁行动方。"
        )
        updated_questions.append(('2021_ky1', q['id'], 40))

save_exam(p2021, d2021)

# ----------------------------------------------------
# 2. 2020 ky1 Text 4 (Q37 - Q40)
# ----------------------------------------------------
d2020, p2020 = load_exam('2020_ky1')
for q in d2020['questions']:
    so = q['sort_order']
    if so == 37:
        print("[Calibrating] 2020 ky1 Q37")
        q['explanation'] = (
            "［精准定位］第二段末句指出，美国已对法国数字服务税展开 301 调查，可能导致美国对法国征收报复性关税"
            "（could lead to retaliatory tariffs on French goods）。由此可知，法国征收数字服务税可能会招致反制措施，［A］正确。\n\n"
            "［命题解密］正确项［A］may trigger countermeasures against France 是对第二段末句 could lead to retaliatory tariffs 的合理同义替换。\n\n"
            "［干扰排除］\n"
            "［B］将外部调查与报复关税曲解为“国内外饱受批评”。\n"
            "［C］将法国单边税收举措曲解为“旨在促进多边贸易公平竞争”，与第三段所述单边举措相悖。\n"
            "［D］偷换征税范围：首段明确指出该税只适用于全球数字业务收入超过 7.5 亿欧元的科技巨头，并非所有国际企业。\n\n"
            "［技巧总结］推断细节题需注意情态动词的对应（could lead to 对应选项中的 may trigger）。"
        )
        updated_questions.append(('2020_ky1', q['id'], 37))

    elif so == 38:
        print("[Calibrating] 2020 ky1 Q38")
        q['stem'] = 'The countries adopting the unilateral measures share the opinion that'
        for opt in q['options']:
            if opt['key'] == 'C':
                opt['text'] = "tech multinationals' monopoly should be prevented"
        q['explanation'] = (
            "［精准定位］第四段②句指出，采取单边措施的国家都一致认同：当前的国际税收体制未能跟上变化中的全球经济的发展步伐"
            "（they all share a view that the international tax system has failed to keep up with the changing global economy）。"
            "换言之，现行的国际税收体系需要升级改革，［B］正确。\n\n"
            "［命题解密］正确项［B］the current international tax system needs upgrading 是对定位句 has failed to keep up with the changing global economy 的同义改写。\n\n"
            "［干扰排除］\n"
            "［A］无中生有，文中并未提及必须确保科技巨头的收入再分配。\n"
            "［C］偏离主题，文章讨论的是税收管辖权问题，而非反垄断问题。\n"
            "［D］过度引申，文中并未探讨所有国家是否享有平等的征税权。\n\n"
            "［技巧总结］观点归纳题应抓住观点引导词（share a view that ...）后的宾语从句内容进行直接对应。"
        )
        updated_questions.append(('2020_ky1', q['id'], 38))

    elif so == 39:
        print("[Calibrating] 2020 ky1 Q39")
        q['explanation'] = (
            "［精准定位］第五段②句指出：法国的数字服务税以及美国的反应给国际税收体系的未来走向打上了问号"
            "（raise questions about what the future holds for the international tax system）。"
            "由此可知，OECD 目前正在推进的多边国际解决方案面临着不确定的前景，［C］正确。\n\n"
            "［命题解密］正确项［C］is faced with uncertain prospects 是对②句 raise questions about what the future holds 的同义转述。\n\n"
            "［干扰排除］\n"
            "［A］与第二句指出美国也参与了 OECD 工作的客观事实相悖。\n"
            "［B］将前景不明朗曲解为“需要立即进行重新调整”。\n"
            "［D］将已有 131 个国家参与的事实歪曲为“需要更多国家参与”。\n\n"
            "［技巧总结］考查对未来趋势或机构工作现状评价时，重点关注具有转折和评判色彩的短语（raise questions about what the future holds）。"
        )
        updated_questions.append(('2020_ky1', q['id'], 39))

    elif so == 40:
        print("[Calibrating] 2020 ky1 Q40")
        q['explanation'] = (
            "［精准定位］全文首句指出法国率先通过数字服务税法案；随后的论述指出法国开此先河引发多国效仿及国际税收体系的震荡；"
            "末段总结指出法国拟征的数字税是一个明确警告，若国际解决方案难产，更多国家将跟进效仿。"
            "可见全文紧紧围绕“法国率先开征数字税”展开，［B］为最佳标题。\n\n"
            "［命题解密］正确项［B］France Leads the Charge on Digital Tax（法国带头开征数字税）高度概括了全文主题。"
            "Leads the charge 形象贴切地概括了法国开创先河的举措。\n\n"
            "［干扰排除］\n"
            "［A］以偏概全，法国面临关税威胁只是第二段中提到的潜在局部后果。\n"
            "［C］情感色彩与事实偏颇，法国开征数字税是为了增加财政收入，并非对科技巨头说“不”。\n"
            "［D］偏离核心，法国并非要求在数字经济中占有一席之地，而是要求分享税收红利。\n\n"
            "［技巧总结］主旨标题题需把握文章首尾呼应的线索，正确项既要有核心主体（France），又要有核心事件（Digital Tax）。"
        )
        updated_questions.append(('2020_ky1', q['id'], 40))

save_exam(p2020, d2020)

# ----------------------------------------------------
# 3. 2022 ky2 Text 4 (Q36 - Q40)
# ----------------------------------------------------
d2022, p2022 = load_exam('2022_ky2')
for q in d2022['questions']:
    so = q['sort_order']
    if so == 36:
        print("[Calibrating] 2022 ky2 Q36")
        q['explanation'] = (
            "［精准定位］第一段①句指出，科学家们拿不准道德课是否真的能够改变人们的行为，因为证据不足，"
            "依赖的大多是人为的实验室测试或是不可靠的自陈报告（are unsure if their lessons can actually change people's behavior; evidence either way is weak）。"
            "换言之，科学家们普遍认为道德课的影响难以确定，故［A］正确。\n\n"
            "［命题解密］正确项［A］hard to determine 是对文首句 are unsure 与 evidence either way is weak 的同义概括。\n\n"
            "［干扰排除］\n"
            "［B］曲解文意，文中并未指责道德课的效果被狭隘理解。\n"
            "［C］反向干扰，科学家拿不准其是否有效果，而非其效果难以忽视。\n"
            "［D］无中生有，文中并未谈及对效果的总结质量问题。\n\n"
            "［技巧总结］首句细节题注意对比转折词前的让步与疑问焦点（unsure 对应 hard to determine）。"
        )
        updated_questions.append(('2022_ky2', q['id'], 36))

    elif so == 37:
        print("[Calibrating] 2022 ky2 Q37")
        for opt in q['options']:
            if opt['key'] == 'C':
                opt['text'] = 'It is important to students.'
        q['explanation'] = (
            "［精准定位］第二段②句指出，研究人员之所以选择研究吃肉行为，是因为这是一种普遍且易于量化的行为"
            "（eating meat ... is a real-world behavior that is easy to measure）。由此可知，易于测量是选择其作为研究对象的原因，［B］正确。\n\n"
            "［命题解密］正确项［B］It is a behavior easy to measure 与原文 easy to measure 直接吻合。\n\n"
            "［干扰排除］\n"
            "［A］虽然吃肉很普遍，但研究者看重的是容易客观量化（超市购买记录）。\n"
            "［C］与［D］属于无中生有，文中并未提及这对学生是否重要或是课堂热点辩题。\n\n"
            "［技巧总结］因果事实题直接对照原文中的解释说明从句（a behavior that is easy to measure）。"
        )
        updated_questions.append(('2022_ky2', q['id'], 37))

    elif so == 38:
        print("[Calibrating] 2022 ky2 Q38")
        q['stem'] = "Eric Schwitzgebel's previous findings suggest that ethics professors ________."
        q['explanation'] = (
            "［精准定位］第三段①句指出，研究者此前发现伦理学教授与其他学科教授在诸多现实行为上并无二致"
            "（ethics professors do not differ from other professors on a range of behaviors），"
            "比如投票率、献血、按时还书等。这说明伦理学教授在道德层面上未必比其他人表现得更好，［D］正确。\n\n"
            "［命题解密］正确项［D］are not necessarily ethically better 是对 do not differ from other professors on a range of behaviors 的合理深层引申。\n\n"
            "［干扰排除］\n"
            "［A］与［B］主观臆断伦理学教授对学生的宽容度或自身的社交性格，文中无依据。\n"
            "［C］将句中的投票率细节偷换为对政治问题不敏感。\n\n"
            "［技巧总结］例证推理题需要把握引证所要说明的宏观论点：知识上的道德并不必然转化为行为上的优越。"
        )
        updated_questions.append(('2022_ky2', q['id'], 38))

    elif so == 39:
        print("[Calibrating] 2022 ky2 Q39")
        q['explanation'] = (
            "［精准定位］第四段②③句指出心理学家尼娜·施特罗明格的看法：她希望这种影响是真实的，但无法排除存在未知的混杂变量；"
            "而且即便是真实的，也可能会被另一个轻微的干预所逆转（cannot rule out some unknown confounding variable ... might be reversible）。"
            "这表明她认为这种干预的效果是不确定的，［C］正确。\n\n"
            "［命题解密］正确项［C］uncertain 是对 cannot rule out some unknown confounding variable 以及 might be reversible 的高度抽象提炼。\n\n"
            "［干扰排除］\n"
            "［A］与末句“来得快，去得也快（Easy come, easy go）”完全相悖。\n"
            "［B］与［D］将不确定性偷换为可预测性或不可重复性。\n\n"
            "［技巧总结］人物观点题抓关键情态动词与转折词（cannot rule out, might be reversible 即 uncertain）。"
        )
        updated_questions.append(('2022_ky2', q['id'], 39))

    elif so == 40:
        print("[Calibrating] 2022 ky2 Q40")
        q['explanation'] = (
            "［精准定位］第五段①句指出，施维茨格贝尔推测最大的影响来自社会影响——即同学或助教在讨论中起到的示范作用；"
            "②句接着指出，这一影响可能不仅包含理性说服，还夹杂着情感驱动（not only rational argument but also emotional engagement）。"
            "由此可知，学生行为的改变是多种因素共同作用的结果，［C］正确。\n\n"
            "［命题解密］正确项［C］is a result of multiple factors 是对文中 social influence, rational argument 以及 emotional engagement 等多重维度的概括。\n\n"
            "［干扰排除］\n"
            "［A］无中生有，文中并未讨论心理健康益处。\n"
            "［B］将前面的实验统计事实误用为对成因的猜测。\n"
            "［D］过度解读，行为变化并非单纯自我发展的标志。\n\n"
            "［技巧总结］归纳总结题注意段落中并列递进的要素结构（not only ... but also ... 提示多重因素驱动）。"
        )
        updated_questions.append(('2022_ky2', q['id'], 40))

save_exam(p2022, d2022)

# ----------------------------------------------------
# 4. 2007 ky1 Text 3 (Q34 - Q35)
# ----------------------------------------------------
d2007, p2007 = load_exam('2007_ky1')
for q in d2007['questions']:
    so = q['sort_order']
    if so == 34:
        print("[Calibrating] 2007 ky1 Q34")
        q['explanation'] = (
            "［精准定位］文章末段指出：从中产阶级家庭的角度看，上述现象（美国各中产家庭经济风险增加）是（政府）"
            "在以骇人的增速将金融风险大规模转嫁到他们已不堪重负的肩膀上；经济不良后果已经显现，政治影响也不会太远了"
            "（The financial fallout has begun, and the political fallout may not be far behind）。可见，该段暗示经济问题解决不好会引起政治问题，［C］正确。\n\n"
            "［命题解密］正确项［C］financial problems may bring about political problems 是对末句 The financial fallout has begun, and the political fallout may not be far behind 言外之意的明确提炼。\n\n"
            "［干扰排除］\n"
            "［A］用 financial risks 和 political risks 替换原文 fallout，但文中并未对比两者大小，outweigh 属于无中生有。\n"
            "［B］偷换主体：政治风险的承担者是政府与决策层，而非中产阶级自身。\n"
            "［D］将末段词汇 financial responsibility 与 political fallout 杂糅干扰，indicator 属于主观捏造。\n\n"
            "［技巧总结］结尾句推理题需领会作者的警示用意。末句两个并列分句构成前后因果呼应，直指经济困境将演化为政治风暴。"
        )
        updated_questions.append(('2007_ky1', q['id'], 34))

    elif so == 35:
        print("[Calibrating] 2007 ky1 Q35")
        q['options'] = [
            {'key': 'A', 'text': 'The Middle Class on the Alert', 'value': 'A'},
            {'key': 'B', 'text': 'The Middle Class on the Cliff', 'value': 'B'},
            {'key': 'C', 'text': 'The Middle Class in Conflict', 'value': 'C'},
            {'key': 'D', 'text': 'The Middle Class in Ruins', 'value': 'D'}
        ]
        q['explanation'] = (
            "［精准定位］本文第一段提出“美国中产阶级家庭曾经的稳定性已被彻底改变”。第二、三段分别论述“家庭经济模式的改变”"
            "以及“公共政策的改变”对中产阶级家庭安稳性的冲击。末段收束全文，提出警示“经济问题已经出现，政治问题也就不远了”。"
            "可见，全文讨论的是中产阶级家庭经济风险大增、脆弱不堪一击的现状，［B］是对全文主旨的恰当概括。\n\n"
            "［命题解密］正确项［B］The Middle Class on the Cliff（悬崖边上的中产阶级）是对文章内容的正确概括。"
            "the middle class 是全文反复探讨的焦点对象，on the cliff 是对文中 financially secure has been transformed, family risk has risen as well, absorb much more risk 等困境的绝佳象征。\n\n"
            "［干扰排除］\n"
            "［A］张冠李戴：作者是警告政策制定者应该警惕，而非中产阶级保持警惕。\n"
            "［C］曲解文意：中产阶级内部各群体均面临沉重压力，并非处于彼此矛盾之中（in conflict）。\n"
            "［D］夸大其词：文章论述的是中产阶级家庭经济风险加剧、濒临险境，并不等同于已经彻底毁灭（in ruins）。\n\n"
            "［技巧总结］文章主旨标题题需精准把握作者对所描述对象的“程度”与“方向”。on the cliff 既符合濒临危险的现状，又未过分夸大至完全毁灭。"
        )
        updated_questions.append(('2007_ky1', q['id'], 35))

save_exam(p2007, d2007)

print(f"\nSuccessfully executed Round 24 calibration for {len(updated_questions)} questions locally.")
