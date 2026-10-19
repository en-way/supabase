import json
import os

def load_exam(exam_id):
    path = f"public/data/exams/{exam_id}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f), path

def save_exam(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Starting Round 27 Calibration...")

# ==========================================================
# 1. 2019 ky1 (5bcba462-0a1e-59b2-9fcb-c171d242db3b)
# ==========================================================
data_2019, path_2019 = load_exam("5bcba462-0a1e-59b2-9fcb-c171d242db3b")
for q in data_2019["questions"]:
    so = q.get("sort_order")
    if so == 26:
        q["stem"] = "What is commonly regarded as the cause of grade inflation?"
        q["explanation"] = (
            "［精准定位］根据题干关键词grade inflation定位至首段①句，该句指出：“分数膨胀”往往被视作高等教育进入消费者时代的产物，即人们通常认为消费者文化是高等教育“分数膨胀”的诱因，［D］正确。\n\n"
            "［命题解密］题干与正确项［D］同义改写首段①句grade inflation is often considered a product of a consumer era in higher education。\n\n"
            "［A］由首段②句“课程目录出现剧烈变化（course catalogs underwent dramatic changes）”干扰，但该现象为“消费者文化进入高等教育领域”的伴生现象，并非“分数膨胀”的原因。［B］源自首段②句graders were far more unforgiving,但将原文“过去的评分者（老师）并不像现在这样宽容”曲解为“学生对分数漠不关心”。［C］利用常识设置干扰，但原文并未提及。\n\n"
            "［技巧总结］考研英语事实细节题题干通常就文中“某事物/现象的产生原因”进行设问，其主要考查方向有二：一是针对文中的“普遍看法（铺垫性信息）”发问，二是针对文中的“真实原因（意欲重点论述的信息）”发问。本题中，首段①句先提出对于“分数膨胀”的普遍看法（often considered a product of...），②句紧接着借从句以a less examined trend引出“相较之下对较少被人关注的原因”，这也是文中意欲重点论述的原因。再审视题干，发现命题人“避重就轻”，针对“普遍看法（铺垫性信息）”发问，所以解题时需牢牢锁定①句，谨防利用②句逻辑或信息设置的干扰。"
        )
    elif so == 27:
        q["stem"] = "What was the original purpose of grade forgiveness?"
        q["explanation"] = (
            "［精准定位］根据题干关键词the original purpose of grade forgiveness可定位至第三段②句，该句介绍数十年前“成绩宽恕”政策刚开始实行时的情形（When this practice first started decades ago...）：仅针对大一新生，旨在为新生提供一次重修课程的机会，帮他们应对高中到大学的过渡，也即适应大学学习，［A］正确。\n\n"
            "［命题解密］［A］是对第三段②句 to give them a second chance... if they struggled in their transition to college-level courses 的概括。\n\n"
            "利用第三段①句as从句的内容进行干扰，但“维持毕业率”和“（提升保留率，）增加学费收入”均为该政策近年来加速实行的原因，而非其初始目的。［C］借第四段②句“通过重修课程，学生在后续课程中表现得更好，最终取得了更大的成功”干扰，该内容固然是“（高校管理者眼中）政策对学生的好处”，但并非政策初衷。\n\n"
            "［技巧总结］本题考查事实细节，解题关键在于准确定位。题干关键词the original purpose of grade forgiveness 看似直接对应第四段①句 the goal of grade forgiveness,但 College officials tend to emphasize that...表明该句/段为当前大学管理者对政策的看法，与题干中过去时态以及original 一词表明的“政策实行之初”不符，故实际应定位至第三段②句（When this practice first started decades ago...）。四个选项中只有［A］符合题意，其他三项均借该政策当前的执行效果（B、D背离初衷，C则扩大作用对象）干扰。"
        )
    elif so == 28:
        q["stem"] = "According to Paragraph 5, grade forgiveness enables colleges to ________."
        q["explanation"] = (
            "［精准定位］第五段指出“成绩宽恕”满足了大学两方面的需要：1.帮助公立大学获得更多政府拨款；2.提高学生对于学校的满意度。［A］符合第一项内容。\n\n"
            "［命题解密］“题干 + ［A］”同义改写②句 better grades can... mean more money。\n\n"
            "［B］由③句“让学生觉得学费物超所值（即，提高消费者满意度）”过度引申而来，但该句实际指“留住在校学生”，而非“吸引还未入学的学生”。［C］由②句“提高毕业率和保留率”臆测出“成绩宽恕”政策有助于“提升高校教学质量”，但文中没有信息支撑这一结论。［D］借②句干扰，但原文为“州政府拨款的部分依据（毕业率和学生保留率高）”，这一条件并非地方政府本身的需求（governments' needs）。\n\n"
            "［技巧总结］题干中的enables colleges to提示本题考查“大学热衷成绩宽恕政策的背后原因/对大学的好处”。应结合微观与宏观思维解题：微观上定位梳理原文并比对选项，宏观上还应思考文中对这一好处的定位。第五段首句satisfies colleges' own needs将这种好处定位为“（大学的）私利”，②句随即验证——财政拨款。③句则呼应首句的“消费者时代”，说明高校的“取悦”心态。所以整段内容与“高等教育本身（［C］项）、州政府需求（［D］项）”毫无关联，［B］虽符合“高校逐利”的总体导向（有利于增加高校学费收入），但比对后发现为过度引申。"
        )
    elif so == 29:
        q["stem"] = 'What does the phrase "to be aligned" (Line 5, Para. 6) most probably mean?'
        q["explanation"] = (
            "［精准定位］所考词组位于第六段③句，而该句中this回指前文信息，需综合分析：本段①句先揭示学校与学生之间关系的实质——商品/服务提供者VS消费者，②句具体说明这一关系：作为消费者的学生及其家长希望顺利拿到学位，作为商品/服务提供者的学校尽力产出合格或看起来合格（即符合学位授予条件）的学生，可见两者动机是一致的，to be aligned意为“一致的，相同的”，［C］正确。\n\n"
            "［命题解密］［C］是基于学生和学校之间关系（responding to consumers' expectations）以及两者目标（expect a college degree 与 turn out graduates who are as qualified as possible 一致）作出的合理推断。\n\n"
            "全文均未提到学生与学校之间存在任何的对立、矛盾，反而是学校致力于满足学生的需求，为学生提供支持，排除［A］与［D］。［B］利用“学校服务学生的同时，实现自身需求，两者互帮互补、各取所需”干扰，但原文主语为“动机（incentives）”，文中动机均指向“拿到文凭”，而非“互补”。\n\n"
            "［技巧总结］③句this乍看指代不明，此时应回顾全段进行判断，首先明确“总—分”布局（①句概述，②③句具体说明），①句 universities are responding to consumers' expectations、②句 Since students... expect..., it is in the best interest of a school to...均表明学生与大学出发点一致（均追求一纸文凭），故推知to be aligned意为“一致的”。捷径：本题实际考查学生与大学动机/态度的关系，可结合全文或明示或暗示的二者关系（首段 consumer era/customers to be pleased、第三段 students... paying tuition、第五段 students... paying the bill... value for... tuition均表明学生与学校为消费关系）可知，学校致力于取悦学生，排除体现矛盾关系的以及互补关系的［B］。"
        )
    elif so == 30:
        q["stem"] = "The author examines the practice of grade forgiveness by ________."
        q["explanation"] = (
            "［精准定位］本题考查作者写作方式（examines... by...），需结合全文内容进行判断。文章第一至三段先介绍“成绩宽恕”政策的内容及其发展情况，特别指出近年来该政策日益普及的现状，第四至六段揭示政策产生和发展的原因，其中第四、五段先分别指出该政策符合学生和大学的需求，第六段总结原因，揭示学生和大学之间关系的实质是消费关系，“成绩宽恕”政策的加速施行是双方共同利益驱使的结果。可见，作者是借助“分析政策背后的原因和动机”来剖析政策、表明态度的，［B］正确。\n\n"
            "［命题解密］［B］正确概括本文写作方式，主要指向第四、五段具体原因分析以及第六段原因总结。\n\n"
            "［A］利用作者隐含的担忧态度进行臆测，但选项内涵实为对尚未实施的计划、政策等进行可行性评定（feasible意为“切实可行的，行得通的”），而本文论述对象“成绩宽恕”政策早已实行数十年；且“可行性”一词侧重“能不能”，而非“该不该”。第四段涉及政策相关观点，但仅涉及制定者和执行者一方的观点，没有观点交锋，故排除［C］。第四、五段虽涉及政策对学生和大学的影响（助学生顺利毕业就业、提高毕业率和学生保留率），但都是双方想要的短期效果，且与全文“曝光这一动机”的立意不符，排除［D］。\n\n"
            "［技巧总结］本题形式上考查论证方式/结构，但作为最后一道题，也可以视作考查文章主旨，解题时需捋清文章主线。前三段介绍大学“成绩宽恕”政策，并指出其近年来加速普及，第四至六段分析原因，指出该政策的背后推手是“买卖双方（学生和大学）的共同需求”，可见本文主要分析了“成绩宽恕”的原因，希望借此引发公众对高等教育“商品化”的反思，［B］正确。"
        )

save_exam(data_2019, path_2019)
print("Calibrated 2019 ky1 Text 2 (Q26-Q30).")

# ==========================================================
# 2. 2016 ky1 (666cdb4e-7fd3-53c2-8c91-a12fa3160c09)
# ==========================================================
data_2016, path_2016 = load_exam("666cdb4e-7fd3-53c2-8c91-a12fa3160c09")
for q in data_2016["questions"]:
    so = q.get("sort_order")
    if so == 31:
        q["stem"] = "The author views Milton Friedman's statement about CSR with ________."
        q["explanation"] = (
            "［精准定位］首段①句先介绍Friedman观点，②句则转折指出作者看法“即便你接受Friedman的基本观点，事情也可能并非那么绝对”，③句引用最新研究发现具体说明作者观点“CSR能为企业创造货币价值”。可见作者对Friedman观点持怀疑态度，［B］正确。\n\n"
            "［命题解密］正确项［B］是对首段②③句 Even if you accept... things may not be absolutely clear-cut... CSR may create monetary value for companies 中所传达作者态度的合理推断。\n\n"
            "［A］没能正确把握“度”：tolerance虽含有一定的“质疑”，但总体为“接受”态度。［C］对②句accept Friedman's premise断章取义，认为作者赞同Friedman观点，但Even if（就算）暗示“Friedman的观点实则难以令人接受”。［D］将②句things may not be absolutely clear-cut（作者认为Friedman观点过于绝对）曲解为“作者对Friedman观点持不确定态度”。\n\n"
            "［技巧总结］开篇引用人物观点/话语主要有“批驳立意（反向）”和“援引入题（正向）”两个方向。确定方向主要有以下几种办法：1. 句间以及句内逻辑衔接词所提示的论证逻辑；2. 蕴含情感色彩的形容词、副词、甚至动词、名词等所体现的作者态度；3. 两者观点具体信息所指方向。此外还需注意：文中的研究发现（尤其是最新研究发现）往往和作者观点一致；让步假设、虚拟语气等的真实语义和表面含义通常相反。"
        )
    elif so == 32:
        q["stem"] = "According to Paragraph 2, CSR helps a company by ________."
        q["explanation"] = (
            "［精准定位］第二段介绍了 CSR使企业增值的三种方式：一、消费者将CSR看作是企业产品质量高的标志；二、消费者出于间接捐助慈善事业的心理愿意购买产品；三、CSR使消费者及他人对企业更加关注并认可。可见这三种方式共同之处在于“为企业赢得来自消费者的信任”，［C］正确。\n\n"
            "［命题解密］［C］抓住了③④⑤句核心关键人物consumers/customers，并概括提炼出内容背后信息：消费者对注重CSR投入的企业持认同和信任态度。\n\n"
            "［A］malpractices（不法行为）源自第一段末句 when they are prosecuted for corruption，但将 CSR 能使企业“因不法行为受诉时受罚较轻”改为“避免做出不法行为”。［B］夸大了第二段⑤句内容“CSR能为企业赢得更多尊重（earn it greater consideration）”，事实上若企业确实行为不当，CSR未必能保护企业免受指摘，顶多能够缓解而已。［D］利用第二段③句词汇high quality设置干扰，但将原文内容CSR会“使消费者认为企业产品质量高（consumers may take... as... products are of high quality）”篡改为“使企业提高其产品质量”。\n\n"
            "［技巧总结］由题目设问方式According to Paragraph 2, CSR helps a company by可知本题既可是“事实细节题（对应第二段②③④所述CSR为企业增值的三种方式之一）”，又可是“事实概括题（体现三种方式共同特征）”。前一种情况考生只需将选项回文定位，找到与某一句内容一致的选项即可。而后一种情况则难度较大，需要考生对所涉及的内容进行总结提炼，找出其共同指向，具体可采用“提炼法”与“排除法”相结合的策略。首先排除与③句内容明显不符的［D］（偷换行为主体）。其余选项需要综合③④⑤句内容进行筛选：三句均出现 consumers... customers... consumers，且 take... a company's products are of high quality... be willing to buy a company's products... greater consideration 均和企业产品及企业本身所受关注度、信任度相关，可初步推知［C］正确；而［A］与［B］与该部分信息无直接关联，可排除。"
        )
    elif so == 33:
        q["stem"] = 'The expression "more lenient" (Para. 4) is closest in meaning to ________.'
        q["explanation"] = (
            "［精准定位］第四段①句（考查词所在句）指出：研究发现CSR计划最全面的企业往往会获得______的处罚。②句进一步指出，研究排除了“由于企业的政治影响力，而非其CSR立场使它们获得宽大处理”的可能：为政治活动捐款更多的企业受到的罚款并不更低。可见，more lenient大概含义为“较轻的处罚，较低的罚款”，［D］正确。\n\n"
            "［命题解密］［D］ less severe正确解读②句对①句的补充解释逻辑，体现more lenient penalties与lower fines的同义关系。\n\n"
            "［A］从第四段②句ruled out... that it was firm's political influence（排除了企业的政治影响力因素的干扰）推出“处罚较为公正、较不具争议性”，但这里为研究方法，与“被诉企业的受罚情况”无关。［B］将第四段②句 it was firm's political influence, rather than their CSR stand, that accounted for the leniency曲解为“政治处罚比CSR处罚更为有效”，从而设置干扰more effective，但由上文可知，CSR会给企业带来“收益”，而不是“惩罚”。［C］利用第二段末句以及第三段所体现的halo effect（光环效应）的性质“更加扩散、持久”设置干扰more lasting，但所考词修饰的是penalties（惩罚）。\n\n"
            "［技巧总结］本题就“研究发现”中的关键词设置词义推断题。对于此类题目，除了常规的词义推断方法“通过判断句间关系在上下文中寻找所考词汇的同义词、近义词、上下义词或者反义词”之外，还必须要结合“研究目的”、“研究对象”、“研究结论”等来理解，正确项应能在其间形成顺滑一致的逻辑关系。如本题的解答，通过判断第四段①②句间为补充解释关系，得知leniency与lower fines同义，基本确定［D］正确。再结合研究目的（区分CSR的三种效应、验证光环效应的影响）、研究方式（研究美国的行贿诉讼案例）以及第一段便已经明确的研究结论（CSR的光环效应能使企业在被诉时受益），可推知研究发现（考查词所在句内容）：CSR计划最全面的企业在被诉时受罚较轻，确定［D］为答案。而其他三项则无法在其间建立顺滑的逻辑关系，故排除。"
        )
    elif so == 34:
        q["stem"] = "When prosecutors evaluate a case, a company's CSR record ________."
        q["explanation"] = (
            "［精准定位］根据题干直接定位至第五段。该段首句指出，检察官原本应该只是基于案情本身进行评判，但实际上他们确实会受到公司CSR记录的影响，可见［A］符合文义。\n\n"
            "［命题解密］正确项［A］ has an impact 是对原文 they do seem to be influenced by a company's record in CSR的同义改写。\n\n"
            "［B］将检察官“基于案情本身判案，但难免受公司CSR记录的影响(seem to be influenced by)”夸大为“将公司CSR记录视为判案可靠证据(reliable evidence)”。［C］对②句increasing... by about 20% result in fines断章取义，从而将文中完整信息“企业捐赠提高20%/即CSR记录佳，则罚款会降低40%”改为“CSR记录会使得公司受罚可能性增加”。［D］对“检察官判案受企业CSR记录影响”过度推断出“企业CSR记录是检察官调查的一部分(constitutes part of the investigation)”，但由第三段可知，这种影响并非来自“调查”，而是来自“光环效应”。\n\n"
            "［技巧总结］本题就第五段所述的“研究结论”命制事实细节题。对于该类题型，需从两个角度加以考虑：①遵循事实细节题正确项的一般原则“题干+正确项=//~原文某句”；②注意“研究是为了论证文章主旨，研究结论体现的便是文章主旨”，故题干+正确项应与文章主旨高度契合。如本题题干+正确项 ［A］ When prosecutors evaluate a case, a company's CSR record has an impact on their decision 对应①句主要内容 they/prosecutors do seem to be influenced by a company's record in CSR，又体现了文章主旨，企业CSR会在其被诉时创造货币价值。"
        )
    elif so == 35:
        q["stem"] = "Which of the following is true of CSR, according to the last paragraph?"
        q["explanation"] = (
            "［精准定位］末段首句指出，研究未能回答“企业应该在CSR上投入多少”这一问题，也即企业在CSR上具体的必要花费数额尚不得而知，［B］正确。\n\n"
            "［命题解密］正确项［B］是对末段首句their study does not answer the question of how much businesses ought to spend on CSR 的同义改写。\n\n"
            "［A］误认为末段③句get into trouble with the law... costly punishment 是在介绍“CSR 被人们所忽视的负面影响”，而实际上该句是在说明CSR最起码的积极作用。［C］将末段①句信息“研究未能解答企业应该在CSR上投入多少”曲解为“研究高估了企业的CSR支出能力/CSR财政能力”。［D］根据末段②句词汇banking望文生义、捏造出“CSR能为银行业带来很多收益”，而实际上banking on意为“指望”，和“银行业”无关。\n\n"
            "［技巧总结］从原文来看，命题的陷阱在于取舍结构、倒装句、否定句等特殊句式。从选项来看，命题人通常会采用望文生义（文中取某词僻义或特殊用法，选项却用其常见含义）、断章取义（不是整体理解句子信息，而是将个别词汇糅杂到一起形成完整的语句）等方式形成干扰。本题中，根据［A］negative effect、［B］spending on、［C］financial capacity、［D］banking industry 不难分别定位至③句、①句、①句、②句，但需要借助语法知识、语义逻辑、以及文章主题等才能理解到［C］曲解文意、［A］断章取义、［D］望文生义，只有［B］是对①句主要内容的同义表达。"
        )

save_exam(data_2016, path_2016)
print("Calibrated 2016 ky1 Text 3 (Q31-Q35).")

# ==========================================================
# 3. 2013 ky1 (6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5)
# ==========================================================
data_2013, path_2013 = load_exam("6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5")
for q in data_2013["questions"]:
    so = q.get("sort_order")
    if so == 26:
        q["stem"] = 'It is suggested in Paragraph 1 that "behavioural" ads help advertisers to ________.'
        q["explanation"] = (
            "［精准定位］第一段①句指出“过半广告预算被浪费”；②③句进而作解“互联网时代，这部分被浪费的预算可大幅减少，因为企业（即广告商）可根据用户网上所搜、所点及所说向潜在客户发送行为广告”。由此可见，互联网行为广告能够帮助广告商省钱。故［D］正确。\n\n"
            "［命题解密］题干+正确项［D］是对②③句的最有力概括。\n\n"
            "［A］根据第一段③句“投放给最有可能购买的潜在客户（at those most likely to buy）”以及第二段①句“人们很高兴被投放行为广告（people are happy to be... sent behavioural ads）”捏造，但前者旨在说明“行为广告具有针对性（从而有效减轻广告费用）”，后者意在指出“广告商太过武断地认为客户收到行为广告会很开心”；［B］由第二段①句a quarrel... advertisers捏造出a quarrel among advertisers，且错将第一段②句fraction“部分”视为friction“竞争”，而段中并未提及广告商竞争相关信息。\n\n"
            "［技巧总结］细节推理题的解答关键：先借助题干关键词定位，再借助定位信息与上下文关联找寻与之匹配的正确项。如本题，由题干“behavioural” ads定位至③句，而该句仅谈及“广告商可以投放行为广告”而未谈及“投放行为广告能够帮助广告商做什么”，由此需上行追溯其他句以把握句群语义逻辑关联：广告浪费钱（首句）→ 互联网能省广告费（②句）→ 互联网行为广告能瞄准目标客户（③句），不难推断，行为广告能帮广告商省钱。"
        )
    elif so == 27:
        q["stem"] = '"the industry" (Line 4, Para. 3) refers to ________.'
        q["explanation"] = (
            "［精准定位］被考词所在句③句指出：FTC和DAA 一致认为the industry将会对DNT要求迅速做出回应。该段①句指出FTC提议在浏览器上添加DNT选项，可见这个提议的动作执行者是浏览器开发商；②句随后介绍微软IE浏览器、苹果Safari浏览器、谷歌Chrome浏览器先后推出DNT选项。由此可知，本段主要谈及浏览器供应商对于DNT提议的回应问题，因此③句中FTC和DAA所提到的the industry应该也是互联网浏览器开发商，［A］正确。\n\n"
            "［命题解密］段中出现多个角色，就名词the industry可考查考生对多个角色的正确区辨。\n\n"
            "［B］源自③句digital，而文中仅提及Digital Advertising Alliance“数字广告联盟”这个机构，并未提及digital information analysts“数字信息分析师”这个群体；［C］根据常识“利用网络进行广告宣传是电子商务的一种类型”捏造而来，而文中并未提及“电子商务运营者”；［D］由①句“添加DNT有助用户告知广告商他们不愿被追踪”误解出“就DNT要求做出回应是广告商的事”，而由第三段主体内容（尤其②句）“各家浏览器供应商纷纷对于DNT提议做出回应”可知其错误性。\n\n"
            "［技巧总结］名词性指代题的解答步骤有：1. 返回原文，找出被考指代词；2. 向上搜索，找最近的名词、名词性短语或句子（先从最近点开始找，找不到再找次近的，一般答案不会离得太远）；3. 将找到的词、词组或句子的意思代入替换该指代词，看其意思是否通顺；4. 将找到的词、词组或句子与四个选项进行比较，找出最佳答案。"
        )
    elif so == 28:
        q["stem"] = "Bob Liodice holds that setting DNT as a default ________."
        q["explanation"] = (
            "［精准定位］第五段④⑤句指出Bob观点：消费者境况将更糟，因为收到的广告不仅不会变少，相反变得更加没有意义、没有针对性。由此可知，Bob认为将DNT设为默认状态无益于消费者，［C］正确。\n\n"
            "［命题解密］就引言内容设题旨在考查对人物观点的把握。正确项［C］是对第五段④句consumers will be worse off 的改写。\n\n"
            "［A］与第五段⑤句“消费者看到的广告不仅不能变少”相悖；［B］与深层文意“作为广告商利益代表的Bob Liodice，其言看似从消费者利益角度出发指责微软举措欠妥，实则意在维护广告商利益（广告业肯定会受影响）”相悖；［D］由第五段②句“人们坚持使用默认选项乃人之常情”捏造出“将DNT设为默认状态与人性冲突”。\n\n"
            "［技巧总结］人物观点态度题的解答关键在：借助观点标记词/符号、情感色彩表达词等把握人物观点。如本题：借助观点表达词及符号（says+双引号）首先定位至第五段④⑤句；随后根据引言内容中的consumers will be worse off、will not get fewer ads、will get less meaningful, less targeted ads 可锁定［C］。"
        )
    elif so == 29:
        q["stem"] = "Which of the following is true according to Paragraph 6?"
        q["explanation"] = (
            "［精准定位］第六段②③句指出：DNT信号并不意味着企业必须停止追踪；由于不知道消费者真实心理，企业很可能会忽略DNT信号而继续追踪。这表明，DNT可能无法达到预期效果，［B］正确。\n\n"
            "［命题解密］［B］是对第六段③句意图及事实的概括。\n\n"
            "［A］与③句中企业面对DNT信号会“置之不理并继续追踪（ignore a DNT signal and press on anyway）”相悖；［C］将③句中“无法辨认用户是否真讨厌行为广告”曲解为“DNT正在失去消费者青睐”；［D］借②句中“企业没有义务履行DNT（does not oblige）”做偷换兼反向干扰，从而曲解为“广告商有义务提供行为广告”。\n\n"
            "［技巧总结］Which型细节题的解题思路是：根据选项关键词一一回文对应。正确项通常对应段落主题，而干扰项或反向曲解、或偷换概念、或断章取义。如本题：纵观选项，［A］、［D］就广告商而言，可定位至②③句（anyone/some companies/some指代“广告商”），但［A］与③句ignore相悖、［D］将②句oblige对象“DNT”偷换为“行为广告”；［B］、［C］虽说就DNT而言，但全段均围绕DNT开展，故转而借选项内部关键词做定位，［C］借 popularity among consumers 定位至③句 whether someone really objects to behavioural ads （someone 指代 consumers），但选项未见句中 whether“疑问”之意，也偷换了 consumers 的讨厌对象为“行为广告”；最终将正确项落在［B］。"
        )
    elif so == 30:
        q["stem"] = "The author's attitude towards what Brendon Lynch said in his blog is one of ________."
        q["explanation"] = (
            "［精准定位］末段⑤句介绍Lynch观点：消费者应该拥有更多控制权；⑥句随后反问“真有那么简单吗？”可见，作者对Lynch观点持怀疑态度，［D］正确。\n\n"
            "［命题解密］正确项［D］skepticism是对反问句式Could it really be that simple?深层含义的合理推断（句中it即指引号内Lynch的观点）。\n\n"
            "［B］、［C］与作者反诘语气（兼有“顶撞”效果，与人辩论时表达立场上的不同）相悖；［A］干扰在于末段提及“DNT并非微软巨大卖点”，而作者支持DNT，似乎给考生造成错觉“作者因支持DNT，所以放纵微软此举”，而题目考查点为作者对Lynch观点的站位，而非对微软举措的站位，况且该站位也不正确。\n\n"
            "［技巧总结］解答作者对文中人物观点的态度题，关键在：分清作者观点及文中人物观点，搞清人物观点与作者观点的异同，重点观察文中表示态度的词、词组、句子或特殊句式。如本题：借助作者针对Lynch博客之言的反问句式即可推断其不认可态度：肯定反问句表达否定，否定反问句表达肯定，文中为肯定反问句，故表否定之意。"
        )
    elif so == 31:
        q["stem"] = "Our vision of the future used to be inspired by ________."
        q["explanation"] = (
            "［精准定位］第一段②句指出：科学和技术能够解决人类的一切难题，使所有人都过上富有成就感与机遇的生活。这表明，以前人们对未来的想象源自对科技的信念，［B］正确。\n\n"
            "［命题解密］正确项［B］是对第一段②句的主干概括。\n\n"
            "［A］和［D］均根据第一段②句后半句“ leading to lives of fulfilment and opportunity for all”捏造干扰，但将“客观带来充实的生活和机会多多”变为“人的渴望/信念”，并将之偷换成“憧憬的促因”。［C］源于第二段首句“人们对自身面临的威胁有了更加深刻的认识”，但这是“目前人们持悲观态度”的原因，而非“以前人们持乐观态度”的原因。\n\n"
            "［技巧总结］题干并未锁定具体段落，但used to间接提示文中涉及“今昔对比”，应关注“曾经、过去”的情况，因此排除第二段（Now），聚焦第一段（Up until... ago）。inspired by...实际引出“促因”，故本题考查因果细节。首段共两句话，①句说明想象的具体情况，显然非题干所考，只能锁定②句：无明显因果关联词，但would表明全句为“主观相信或期待发生的情况”，选项里只有［B］和［D］符合，但［D］中opportunity位于结果状语里，故真正的源头在前，即全句主语：科学和技术。"
        )
    elif so == 32:
        q["stem"] = 'The IUCN\'s "Red List" suggests that human beings are ________.'
        q["explanation"] = (
            "［精准定位］第三段末句指出\"Red List\"中对智人的界定：被列为“无危物种（Least Concern）”，鉴于其分布广泛，适应性强，数量持续增加，并且不存在导致数量整体下降的重大威胁。这表明，人类暂时没有灭绝的危险，是可延续的物种，［A］正确。\n\n"
            "［命题解密］［A］中sustained 是对very widely distributed, adaptable, currently increasing, no major threats, Least Concern等一系列特点的高度概括。\n\n"
            "［B］由“分布极广、没有主要威胁”过度推出“人类主宰世界”。［C］从“数量持续增加”以及《名录》的环保性质（the Conservation of Nature），加之上段①句出现的“气候变化”中主观推出“人类威胁环境”，偏离《名录》对“人”的客观介绍。［D］张冠李戴：原文是“悲观态度有误（gloominess is misplaced）”，而非全盘否定人类。\n\n"
            "［技巧总结］若题干对文中某特定信息（如某人、某组织、某研究等）进行考查，表明这部分内容与段落或全文主旨直接相关，因此解题时首先考虑它为哪项要义服务。本题考查第三段中④句提及的某名录，Homo sapiens、Red List of... IUCN等信息乍看复杂，但先从题干得出信息：《名录》对“人类”有所说明，因此Homo sapiens应是“人”的术语说法，引号中内容为解题线索；而本段首句But继前两段后亮明作者观点：人类未来无需悲观，故引号中应该要证明“人类前景向好”，［C］、［D］均为否定性内容，而［B］夸大人在星球中的地位，与“《名录》本身立足于自然保护（the Conservation of Nature）”脱节。"
        )
    elif so == 33:
        q["stem"] = "Which of the following is true according to Paragraph 5?"
        q["explanation"] = (
            "［精准定位］第五段首句指出，思考人类长远未来比思考近期未来更容易，随后解释为何近期未来不好预测，可见［D］正确。\n\n"
            "［命题解密］［D］中hard to conceive 是对首句 it may be easier to think about such lengthy timescales than about the more immediate future 的同义改写。\n\n"
            "［A］从②句“对‘预测近期未来’的建议——留待科幻小说家（和未来学家）去探索”主观编造出“科幻小说日益受欢迎”。［B］源于③句对Arc杂志的定性——专门研究近期未来，但“有助确定未来学范畴”属主观添加内容。［C］将原文“当今技术的社会影响异常复杂”改为“技术能够解决社会问题”，夸大了技术的作用。\n\n"
            "［技巧总结］“判断正误题”的题干通常传递的信息有限：或聚焦某内容（... is true of/about sth according to...），或完全没有限定内容，且选项铺得很开，信息点分散遍及全段，造成解题困难。应牢记“段落主旨为王、干扰项常利用段中碎片信息捏造而成”的原则。本题考查第五段信息，段中“技术发展的情况、科幻小说作家、未来学家、专业杂志Arc”等信息看似纷杂，但其实都在解释首句“思考近期未来比遥远未来更难——只能留待专家去探索”，选项［D］符合这一段落主旨，其他三项主体分别是“科幻小说”、“Arc杂志”和“技术”，属于段中细节，但阐述性信息“日益流行”、“有助于未来学研究”和“解决了社会问题”均对文意做了扭曲。"
        )
    elif so == 34:
        q["stem"] = "To ensure the future of mankind, it is crucial to ________."
        q["explanation"] = (
            "［精准定位］第六段②句指出：过去掌握着通向未来的钥匙，我们如今已经了解了地球及人类历史的形成模式，所以能更准确地预测未来；末段进一步明确：我们已拥有足够的知识去防范前人的危机、改善后人的命运，综上可知，未来仰仗对过去的认识及总结，［B］正确。\n\n"
            "［命题解密］题干+ ［B］是对第六段②句the past holds the key to the future的进一步明确，is crucial to 对应②句 holds the key to。\n\n"
            "［A］把末段首句结论“人类前景是怎样的（并不悲观）”曲解为“人类前景取决于什么（对世界的乐观态度）”。［C］利用第六段②句planet一词捏造干扰，但文中并不涉及“勘探地球资源”这一信息。［D］利用②句shaping the history干扰，将作者建议“借鉴历史预测未来”改为“抑制人类重塑历史的野心”。\n\n"
            "［技巧总结］上题就第五段命题，提示本题重点关注第六段内容。②句the future和holds the key to 与题干吻合，故为线索句，该句提出观点：欲知未来，史可为鉴；如果说该内容仅说明“如何预测未来（因此与题干的To ensure the future不能完全贴合）”的话，则末段进一步明确这样做的意义：通过学习历史来防患于未然，让未来（后人所生活的世界）更好更安全。干扰项均偏离第六、七段要义。"
        )
    elif so == 35:
        q["stem"] = "Which of the following would be the best title for the text?"
        q["explanation"] = (
            "［精准定位］前两段指出目前人类对未来极度悲观。第三段直接批驳这一态度，并从三个方面论证人类物种目前并无重大威胁。第四至六段介绍如何理性地思考人类未来。末段总结指出，人类已经掌握了足够的知识来降低威胁，并改善后人的命运，即：人类未来依然光明。可见，作者驳立结合，意在表明观点：人类具有光明未来，［A］正确。\n\n"
            "［命题解密］［A］中 prospects of mankind 对应本文话题 future of humanity，ever-bright 概括了作者对未来的乐观态度。\n\n"
            "［B］根据文中关键词汇Science, Technology和Humanity设置选项，但完全忽视篇章核心“人类未来”，且有些违背作者观点“不能仅凭当下科技发展的状况便对人类未来妄下断言”。［C］由第三段“物种的化石记录（fossil record）”以及“智人（Homo sapiens）”等内容而来，但作者援引这些内容是为了证明“人类并无重大生存威胁”，而非介绍“人类的进化史”。［D］将第二段内容“人类面临诸多威胁、未来难测”（作者反驳的观点）当成作者观点。\n\n"
            "［技巧总结］考研阅读文章大多为议论文，即作者通过摆事实、讲道理、辨是非等方法，来确定某观点正确或错误，树立或否定某种主张，因此标题常具有“导向性或结论性”的特点，本文是典型的驳论文，自身观点较普通议论文更加鲜明，而选项中毫无感情色彩，［D］有色彩，但总体为消极，背离文意。另外还可结合主题词（本文为“人类未来”）对选项进行过滤，可直接排除两项。"
        )

save_exam(data_2013, path_2013)
print("Calibrated 2013 ky1 Text 2 (Q26-Q30) & Text 3 (Q31-Q35).")

# ==========================================================
# 4. 2020 ky1 (f56943c1-0ba8-58fe-b7d3-061352345067)
# ==========================================================
data_2020, path_2020 = load_exam("f56943c1-0ba8-58fe-b7d3-061352345067")
for q in data_2020["questions"]:
    so = q.get("sort_order")
    if so == 36:
        q["stem"] = "The French Senate has passed a bill to ________."
        q["explanation"] = (
            "［精准定位］第1段第1句指出，法国参议院通过了一项数字服务税法案，将对跨国科技巨头征收新的税收，选 C。\n\n"
            "［命题解密］正确项［C］impose a levy、tech multinationals分别同义改写文首句中impose an entirely new tax与multinationals that provide digital services。\n\n"
            "［A］利用②句第一分句中碎片信息Digital services platform杂糅而来，但该部分意在解释数字服务税法案中“数字服务”的含义，并非指向法案内容；［B］利用常识误导学生认为“法国对跨国公司收税”意在“保护本土公司利益”，但由第三段首句in need of revenue可知，法国数字服务税意在“提高本国财政收入”；［D］利用②句中targeting advertising based on user data所传递出的广告影响力“基于用户数据即可精准定投”捏造而来，但它错误属性同［A］，对应的原文指向的是“数字服务”的具体内容，而非法案本身的内容。\n\n"
            "［技巧总结］本题解答难点在于：明确题干中bill指向开篇句中a digital services tax。两者的对等关系可以借助a digital services tax前passed“经表决通过（动议、法律等）”、后impose“推行，采用（规章制度），强势实行”两词判断。然后再据由which从句所展示的a digital services tax具体内容“向提供数字服务的大型跨国公司征收一项全新税种”锁定正确项［C］（粗犷型学习者甚至只借助“tax一词与［C］中levy一词同义”即可做出选择）。"
        )

save_exam(data_2020, path_2020)
print("Calibrated 2020 ky1 Text 4 (Q36).")

print("All Round 27 calibrations completed successfully.")
