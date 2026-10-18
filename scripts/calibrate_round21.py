import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Calibrate 2001 ky1 Q7
file_2001 = 'public/data/exams/2c892204-071f-5943-86be-d49bca93fe71.json'
with open(file_2001, 'r', encoding='utf-8') as f:
    d2001 = json.load(f)

for q in d2001['questions']:
    if q['sort_order'] == 7:
        print("Calibrating 2001 ky1 Q7...")
        q['correct_answer'] = 'D'
        q['answer'] = 'D'

with open(file_2001, 'w', encoding='utf-8') as f:
    json.dump(d2001, f, ensure_ascii=False, indent=2)
print("Saved 2001 ky1.")

# 2. Calibrate 2003 ky1 Q24, Q25
file_2003 = 'public/data/exams/91ff038a-e3f9-5b6d-82c5-1328735be1d1.json'
with open(file_2003, 'r', encoding='utf-8') as f:
    d2003 = json.load(f)

for q in d2003['questions']:
    if q['sort_order'] == 24:
        print("Calibrating 2003 ky1 Q24 options...")
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "Straitford guarantees the truthfulness of its information"
            elif opt['key'] == 'C':
                opt['text'] = "Straitford's business is characterized by unpredictability"
    elif q['sort_order'] == 25:
        print("Calibrating 2003 ky1 Q25 explanation...")
        q['explanation'] = (
            "［精准定位］根据题干关键词proud of定位到全文末句：斯特雷福特公司对其独立的声音感到自豪。"
            "由上文可知，斯特雷福特公司具有“局外人”的地位，不必附和官方，［B］正确。\n\n"
            "［命题解密］题干和正确项构成了对末段④⑤句的概括。nonconformist image对应文中don't sound "
            "like the usual Washington back-and-forthing 和 independent voice。\n\n"
            "［错项排除］［A］official status与③句\"Straitford将其‘局外人的地位’（outsider status）视为自己成功的关键\"相悖。"
            "［C］、［D］错把“次要原因”当做“主要原因”：①②句虽暗示Straitford公司人员精简高效、且有些军事背景，但这并非其成功的关键所在；"
            "随后内容才以 see... as the key to its success 亮出其成功的关键。\n\n"
            "［技巧总结］从题目所涉原文内容来看，第五段意在明确Straitford公司成功的关键，③句指出“局外人地位”才是其成功关键。"
            "从选项设置来看，四个选项均为文中提及或暗示的信息，取舍颇有难度。解答这类“无论从文章来看还是从选项来看都颇有迷惑性”题目的关键在于："
            "牢牢抓住命题人留下的关键线索，并以此反推；反推过程中排除偷梁换柱（将B的特征当做考查主体A的特征）、文不对题（将关于“A的次要信息”当做题目所要求的“A的主要信息”）。\n"
            "如本题，据题干中most proud of可理解到“正确项必须是Straitford公司的特征且必须是其最引以为豪的方面（其他主体的特征排除，是Straitford特征但并非其最自豪之处的也须排除）”，"
            "定位到文章末句（take pride in its independent voice），将问题转化为反推 its independent voice 所指。［A］是“政府机构”特征而非“Straitford”特征，直接排除；"
            "其他三个选项中，［C］、［D］虽为①②句表明的Straitford特征，但无论是从“代词近指”还是“语义的对应”来看，都不大可能是its independent voice所指，"
            "而［B］nonconformist image 恰能对应 outsider status，成为 its independent voice 所指，故排除［C］、［D］，选取［B］。"
        )

with open(file_2003, 'w', encoding='utf-8') as f:
    json.dump(d2003, f, ensure_ascii=False, indent=2)
print("Saved 2003 ky1.")

# 3. Calibrate 2015 ky1 Q28, Q34, Q36, Q37, Q38
file_2015 = 'public/data/exams/865e5af8-24a4-58e1-bc9e-640f32d8e946.json'
with open(file_2015, 'r', encoding='utf-8') as f:
    d2015 = json.load(f)

for q in d2015['questions']:
    if q['sort_order'] == 28:
        print("Calibrating 2015 ky1 Q28...")
        q['explanation'] = (
            "［精准定位］第四段③句明确指出：查看一个人的手机就犹如进入他或她的家（entering his or her home），可见［D］正确。\n\n"
            "［命题解密］正确项［D］是对第四段③句entering his or her home（进入他或她家中）的同义改写。\n\n"
            "［错项排除］［A］错将第四段①句加州观点（作者反驳的观点）“查看手机内容犹如查看钱包（similar to going through a suspect's purse）”当做作者观点。"
            "［B］源自第四段④句medical history。［C］源自该句comprehensive records of recent correspondence，但两选项严重以偏概全：只是搜查手机危及的（诸多方面）中的一方面，并非“搜查手机内容”的整体类比对象。\n\n"
            "［技巧总结］本题就“文中类比信息”考查“作者观点”。解题时需：准确辨别信息，勿将他人观点当做作者看法；整体理解作者观点，切记以偏概全。具体来看：首先根据题干可找到文中两处对应信息（第四段①句和②③句），随后发现①句为加州观点（California's lame argument），②③句才是作者观点，故舍弃与①句对应的［A］。随后对比发现，［B］［C］均以偏概全，可排除；［D］契合作者整体类比，故正确。"
        )
    elif q['sort_order'] == 34:
        print("Calibrating 2015 ky1 Q34...")
        q['explanation'] = (
            "［精准定位］第六段③句表明David Vaux对《科学》新举措的看法：把一些论文交给统计学家（审查）的想法“有一定价值，但缺点在于，要先通过评审编委会来决定哪些论文需要细查”，言外之意即，编委会自身缺乏有效监管，这一想法还需要进一步完善，［C］正确。\n\n"
            "［命题解密］［C］是对人物引语中 has some merit, but a weakness is that 的合理引申和概括。room for further improvement 是对原文 weakness 的委婉表述。\n\n"
            "［错项排除］［A］利用②句中Researchers should improve their standards设置干扰，但联系①句可知“（研究者）提高水准”指的是“提高数据分析技能，减少统计错误”，而非“增加工作量”；"
            "［B］与②句engaging reviewers who are statistically literate矛盾，此处恰恰是“重视”审稿人（尤其精通统计的）的作用，而非“削弱”。"
            "［D］过度放大文中a weakness而忽略has some merit。\n\n"
            "［技巧总结］本题与上题解题思路类似，解题关键在准确定位（由题干定位至末句）并识别出正确项 has room for further improvement 是对句中 has some merit, but a weakness is that 的合理引申和概括。"
        )
    elif q['sort_order'] == 36:
        print("Calibrating 2015 ky1 Q36 (Rectifying answer to A)...")
        q['correct_answer'] = 'A'
        q['answer'] = 'A'
        q['explanation'] = (
            "［精准定位］第一段①句直接引述Elisabeth说辞：我们如此多公共机构中都缺失诚实正直精神，这很令人担忧；②句说明她认为的原因：“利润和市场应该是社会中唯一的分选机制”是一种共识，即当前分选机制以“利”为中心；第二段继续引述，阐释“以利为中心”的后果：会威胁资本主义与自由，会让机构迷途堕落，可见，Elisabeth担忧“一味重利的分选机制的影响”，［A］正确。\n\n"
            "［命题解密］题干+正确项［A］是对前两段的概括：题干中upset对应原文unsettling，表明Elisabeth的担忧态度；the consequences of the current \"sorting mechanism\" 对应第二段①②句 could become one of the most dangerous goals... was wounding..., would lose its way...，是担忧的具体内容。\n\n"
            "［错项排除］［B］将第二段②句 wounding companies... lose its way... illegal telephone hacking 结合第一段关键词profit形成干扰，但原文逻辑为“道德缺失→行为不当”，而非“行为不当→经济损失”。"
            "［C］将第二段①句“政府机构道德缺失（the absence of...）”改为“政府在道德问题上无能”，把“政府”由“问题主体”篡改为“问题治理者”。"
            "［D］将原文正直诚实的“缺失（dearth）”偷换为“滥用、使用不当（misuse）”。\n\n"
            "［技巧总结］选项为较长的名词结构时，考虑先把信息“化整为零”，排除与文意完全不搭的内容并大致判断答案；然后再结合次要信息分析选项设置思路，确保推断无误。本题选项重心分别为：［A］当前分选机制的后果/影响、［B］企业的经济损失、［C］政府的低效、不称职、［D］正直的误用/滥用。“企业”、“政府”在第二段首句同时提及，两者同属our institutions，共性是“内部都缺失道德（within）”，完全不涉及“财政、经济”以及“政府执行力”问题；“正直”贯穿两段始终，但“使用不当”和文中“缺失”大相径庭。而三项次要信息“因不道德行为、在道德问题上、在机构内部”均与文中要义有所挂钩，造成干扰。［A］中“分选机制”看似“太窄、不着调”，但核心词“影响、后果”辅以限定语“当前的”，使其内涵厚重，实际指代宏观的“社会/经济活动的方式、机制”。"
        )
    elif q['sort_order'] == 37:
        print("Calibrating 2015 ky1 Q37...")
        q['explanation'] = (
            "［精准定位］第三段首句表明两位主编的判决情况，②至⑤句接着指出：参与窃听的记者多达5500人；其余的还在候审，案件事实仍在展开。可见，仍有许多犯案记者将受到法律制裁，［B］符合文意。\n\n"
            "［命题解密］［B］是对第三段④⑤句Others await trial（其他人尚待审判）、This long story still unfolds（这一长串事件仍在展开）以及首句the wider issue of dearth of integrity still stands的明确解读。\n\n"
            "［错项排除］［A］与③句信息“案件核心人物Glenn Mulcaire承认电话窃听已达到工业规模（as was acknowledged by...）”矛盾。"
            "［C］与①句信息“Andy Coulson被判合谋电话窃听罪名成立（finding guilty...）”完全相悖。"
            "［D］利用现实情形“某些情况下（如破案时），可允许进行电话窃听”干扰，但脱离文意。\n\n"
            "［技巧总结］段落推断题的解答应以“段落/群、或文章主旨”为总指导。第三段继前两段“揭示负面现象”后引入具体案件，可知事例为现象服务，意在说明“现象严峻，亟待改变”，纵观选项，［C］和［D］属于“为窃听开脱”的内容，有违总体导向，［B］表明涉案群体庞大，能突显现象，［A］虽聚焦案件核心人物，但全文仅此一处提及，且“认不认罪”属于个人主观行为，与全文探讨的现象/主旨没有实质性关联。"
        )
    elif q['sort_order'] == 38:
        print("Calibrating 2015 ky1 Q38...")
        q['explanation'] = (
            "［精准定位］第四段首句指出，不光窃听事实，审判中的辩词也体现道德缺失问题。②③句继而以Rebekah的辩词为例说明（one of... revelations）：（身为主编却）对编辑室中发生的事毫不了解，也不闻不问，甚至从不询问新闻内容来源。可见作者认为她无视道德，试图以不知情来推卸责任，［A］正确。\n\n"
            "［命题解密］［A］概括了排比强调结构 how little she knew... how little she thought... she never inquired以及astonishing一词所反映的作者的质疑态度。\n\n"
            "［错项排除］［B］把反复出现的how little...主观解读为“只关注鸡毛蒜皮，忽略/规避重点问题”，而末句successful表明其辩词成功为其赢得无罪判决，自然不会“无关紧要”。"
            "［C］根据②③句暗示的“其辩词有意推卸责任、极力强调自己不知情从而无罪”干扰，但该内容无法与“狡猾性格”绝对挂钩（无视律师角色、人性弱点等），且不是作者在段中想表达的重点。"
            "［D］从上段首句conspiring to...（Andy合谋进行电话窃听）衍生出“Rebekah在酝酿阴谋”，在文中并无信息支撑。\n\n"
            "［技巧总结］The author believes/holds/implies...本质上属于“态度题”，对应的原文一定有非常明显的体现作者立场的情感词或特殊表达。文中astonishing（惊讶得难以置信）结合“道德缺失”的论述背景，先行暗示作者对其辩词的负面态度，且很坚决，选项中［B］只体现“主次不分”，不涉及“大是大非”；其余三项都契合“负面态度”，但［D］无从得知，［C］关注点在其“（有别于他人的）个人性格（personality）”，而文中讨论的是“人们当前普遍的行为倾向”。只有［A］与how little... how little... never...以及in her newsroom体现的“不可思议、岂有此理”之意吻合。"
        )

with open(file_2015, 'w', encoding='utf-8') as f:
    json.dump(d2015, f, ensure_ascii=False, indent=2)
print("Saved 2015 ky1.")

# 4. Calibrate 2018 ky1 Q31, Q32, Q35, Q36, Q37, Q38
file_2018 = 'public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json'
with open(file_2018, 'r', encoding='utf-8') as f:
    d2018 = json.load(f)

for q in d2018['questions']:
    if q['sort_order'] == 31:
        print("Calibrating 2018 ky1 Q31...")
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "It failed to pay due attention to patients' rights."
        q['explanation'] = (
            "［精准定位］根据题干 agreement 定位至首段末句中 which 定语从句部分：NHS下属的皇家自由信托医院把数据交由 DeepMind 负责是基于一项不明确的协议，协议远没有对患者权利及其隐私权期望进行考虑，可见［B］符合文义。\n\n"
            "［命题解密］正确项［B］同义替换原文 took far too little account of the patients' rights。\n\n"
            "［错项排除］［A］将③句“会使权力更加集中于科技巨头(further concentration of power in the tech giants)”曲解为“导致科技巨头之间的冲突(conflicts among tech giants)”。"
            "［C］将末句“协议远未考虑患者的隐私权期望(the patients'... and their expectations)”张冠李戴成“协议未达到 DeepMind 的期待(the latter's expectations)”。"
            "［D］误解首句信息 the dangers of the deal between...(协议带来的威胁)，并把末句信息“委员会专员裁定……违法(verdict against)”、“协议不明确、忽视患者权益”相关联，主观推出“协议危及双方”，但“被判违法”≠“陷入危险”，其次只有 NHS 一方被判违法。\n\n"
            "［技巧总结］本题聚焦 agreement, 考查相关信息正误，可知该词意义重大，因此除“定位并比对信息”之外，还应刻意思考它在文中“为何重要、起什么作用”，命题人常会基于此设置正确项。如本题，可首先定位至④句，It is against that background that... 强调句式暗示前三句实为背景铺垫，本句事件才是段落核心信息，即“裁定NHS违法”(verdict against)；而 agreement 位于 which 定语从句中，两个修饰成分 vague 以及 which took far little... 负面指向明显，可知“agreement有问题、无视患者权益”是事件的导火索，选项中只有[B]直接聚焦事件（说明了裁定的原因），其余均与裁定无关。"
        )
    elif q['sort_order'] == 32:
        print("Calibrating 2018 ky1 Q32...")
        q['explanation'] = (
            "［精准定位］第二段②③句指出 NHS 信托对 Denham 裁定的回应：已纠正了其错误行为；其与 DeepMind 的协议会受到仔细审查以确保所有要使用的内容都取得患者允许，所有不必要的数据则加以清除，可见［C］正确。\n\n"
            "［命题解密］［C］意同②句 has mended its ways, 并概括了③句 Further arrangements... will be carefully scrutinised to ensure that all... all... 所体现的具体补救措施。\n\n"
            "［错项排除］［A］受到①句 almost (apologized) 干扰，但一方面该句主语为 DeepMind 而非题干中的 NHS, 另一方面“差不多道歉了”不能简单等同于“空头承诺”。"
            "［B］将②句 mended its ways 错误理解为“拒不服从判决”。"
            "［D］源于第二段①句 apologized, 但这是 DeepMind 做法，其次“诚恳道歉”≠“采取了补救措施”。\n\n"
            "［技巧总结］对于涉及到“事件、争议N方做法/观点”的题目，首先要明确题目考查对象，然后理清相关方各自的做法/观点，再对比选项进行排除，混淆各方的做法/观点是常见的干扰。本题中，由第二段前两句提炼出的做法分别是“DeepMind几乎已经道歉”、“NHS信托纠正了其行为方式”，故很容易先排除张冠李戴的［D］，初步推知［C］正确；进而由③句提到的具体改进做法，排除反向干扰的［A］、［B］，最终确定［C］为答案。"
        )
    elif q['sort_order'] == 35:
        print("Calibrating 2018 ky1 Q35...")
        q['explanation'] = (
            "［精准定位］由题干关键词 AI 所对应的 software, big data 等词定位至末段⑤至⑧句。⑥句指出“我们尚处于技术革命的初期，任何现在看似微不足道的决定都可能对未来产生巨大影响”，言下之意即“当前就‘高科技用于医疗’问题所做的任何决定都应周全考虑、谨慎行事”，可见［B］符合文义。\n\n"
            "［命题解密］［B］是对末段⑥句 small choices now may turn out to have gigantic consequences 的概括。\n\n"
            "［错项排除］［A］把第⑤句中 big data may be... as a big pharma has done 误读为一种不确定态度（ambiguous），但此处意在说明作者对未来情况的推测“大数据以后预计会像大型制药公司那样（垄断行事）”。"
            "［C］把文末作者“赞赏案情报告（a welcome start）”偷换为作者“赞赏AI应用在医疗领域”，作者虽然承认这种应用是一大进步，但全文意在表现应用背后的问题所在。文末也只是“支持监管部门对问题的重视和介入”，作者实际不认同裁定本身的效力，而是期待相关措施能更加谨慎，完善到位。"
            "［D］源于⑦句带负面色彩的 long struggle（漫长的斗争）、avoid a future of digital feudalism（避免未来变成数据封建专制），但作者的矛头是“科技公司垄断”，而非题干中的“AI应用在医疗领域”；其次 contemptuous 一词侧重于“傲慢瞧不上”，作者在文中并未表现出此态度。\n\n"
            "［技巧总结］作者态度题实际影射全文主旨。此类题目可借助“文章论述结构”以及“作者论述角度”两个方面解题。从论证结构来看，第一至三段作者以“树靶—批驳”结构，明确批评了 Ms Denham 的裁定不妥、未切中要害，并在末段指出“科技巨头（垄断）才是需要担忧的对象”，站位相当明确，据此可排除［A］、［C］；而从论述角度看，作者在质疑科技巨头垄断之余却于首段、末段几度指出“AI技术用于医疗研究富有潜力、有望挽救患者生命”，可见其并非一味批判，据此可排除完全否定的［D］，确定答案为［B］，即作者意欲“警示人们及早防范新事物的负面影响”。"
        )
    elif q['sort_order'] == 36:
        print("Calibrating 2018 ky1 Q36...")
        q['explanation'] = (
            "［精准定位］首段①②③句指出 USPS 处于严重财政赤字状态，④⑤句说明根本原因：技术变革使得对其核心产品需求降低，而其监管体系又致其无法灵活管理、适应新现实。可见“管理僵化”为内因，［B］正确。\n\n"
            "［命题解密］正确项［B］是对首段末句 a regulatory structure that denies management the flexibility... 的概括改写。\n\n"
            "［错项排除］［A］将首段②句“USPS持续收支不平衡(expenses have exceeded revenue)”篡改为“预算不平衡(unbalanced budget)”，且这是 USPS 财政问题“本身”，而非“成因”。"
            "［C］由首段⑤句的“技术变革”主观推出“USPS耗费大量财力升级技术”，而文中实际情形是“USPS未能灵活调整业务以适应新现实/技术变革”。"
            "［D］将首段③句 unfunded 断章取义为“银行终止对USPS的资金支持”，而这实际上指“USPS背负无资金准备负债”，文中并未提及“银行支持”。\n\n"
            "［技巧总结］本题是就长难句命制的因果细节题。可采取的解题思路：首先借助因果标记词(reasons、fundamentally等)锁定答案来源(长难句)；随后从语法结构、语义逻辑等角度分析长难句、初步得出答案；最后梳理逻辑、看是否形成顺滑的因果关系。\n"
            "具体来看：首先明确题目考查“USPS财政问题的部分原因”（选项只要符合原因之一便正确），定位至 There are many reasons... 之后的⑤句。随后分析该长难句：整体以 the USPS is in a historic squeeze between A and B 结构说明 USPS 两难境地：技术变革对其核心业务造成巨大冲击(decrease...)，监管体系造成管理僵化(denies... the flexibility)，［B］体现后者，故正确。最后梳理逻辑：“管理僵化”令其无法适应“技术冲击新现实”，故陷入“财政问题”（确定［B］无误）。［C］与此相悖，［A］、［D］与此无直接关联，可排除。"
        )
    elif q['sort_order'] == 37:
        print("Calibrating 2018 ky1 Q37...")
        q['explanation'] = (
            "［精准定位］第二段指出，由于各利益集团向国会施压、要求保护现状，近年来立法改革频频失败，导致邮政局无力偿还债务、唯有推迟现代化。可见［A］正确。\n\n"
            "［命题解密］正确项［A］是对第二段因果链的合理概括。\n\n"
            "［错项排除］［B］将第二段信息 Congress、the Postal Service unable to pay its bills 杂糅，主观推断出“国会援助资金不足”，但文章并未提及“国会资金援助”。"
            "［C］将首段⑤句 decreased demand for its... product 以及第二段②句 whatever else happens to the Postal Service 关联，主观得出“邮政服务需求减少导致USPS未能进行现代化”，但这只是在退步说明“无论邮政服务境况如何（利益集团都要求保护与其利益相关的现状）”，并未触及第二段所示真正原因。"
            "［D］与第二段因果逻辑“邮政工会向国会施压→立法改革失败”中传递的“邮政工会极具影响力”之意完全相悖。\n\n"
            "［技巧总结］本题就“涉及多个主体之间复杂关系的段落”命制因果事实题。解题关键在于借助状语功能、逻辑关联词、指代关系等，理解各主体之间关系，明确因果关系网。注：“与文中事实相反”以及“虽为文中事实、但和主干不存在因果关系”的选项均排除。\n"
            "具体来看，解题关键在于借助 This is why（this指代①句）、leaving（引导结果状语）、A exert pressure on B（A向B施压等）描绘多个主体“利益集团、国会、USPS等”之间关系，明确其间因果关系，得出［A］正确。［D］与文中事实相反，［C］虽为文中事实但并非原因、［B］则捏造信息 funding，均排除。"
        )
    elif q['sort_order'] == 38:
        print("Calibrating 2018 ky1 Q38...")
        q['explanation'] = (
            "［精准定位］第三段②③句指出新法规提出的缓解 USPS 财政困难的两种方式：每封信邮资费率上涨 1 美分；将退休人员转入联邦医疗保险。④句指出，后一举措将大幅抵消预付退休人员医保造成的财政负担，化解 USPS 及其工会长久以来的抱怨。可见［A］正确。\n\n"
            "［命题解密］正确项［A］ removing its burden of retiree health care 同义改写第三段③句 shifting postal retirees into Medicare（④句 the latter step 所指）。\n\n"
            "［错项排除］［B］源自②句立法举措的积极意义“所节省资金可用于负担新运输工具”，但这与 USPS 及其工会的抱怨消解无因果关联。"
            "［C］源自③句法案的前一举措（former step），且将“提高邮资费率”篡改为“采用新的邮资费率增长机制”。"
            "［D］与立法举措“提高邮资费率”的可预期后果“邮件用户减少”显然矛盾。\n\n"
            "［技巧总结］命题人于涉及“多重指代关系、多个提及对象”的内容设置“结果—方式（可视为因果关系）题”，旨在考查考生梳理文中关系的能力。解题时应：借助逻辑关联词初步理清句内/句间逻辑，厘清“词汇替换”和“代词所指”，明确文中对应关系；识别“强加因果”或“偷换因果”的陷阱。\n"
            "具体来看，先由题干关键词 long-standing complaint by the USPS and its unions 定位至第三段末句，thus 明确主句内容为原因，初步锁定［A］。再上溯探寻 The latter step 所指即 shifting postal retirees into Medicare，可完全确定［A］正确。［B］虽为文中提及内容，但与题干所问没有因果关联。［C］、［D］不仅与题干所问没有因果关联，且违背原文事实细节。"
        )

with open(file_2018, 'w', encoding='utf-8') as f:
    json.dump(d2018, f, ensure_ascii=False, indent=2)
print("Saved 2018 ky1.")

print("\nAll Round 21 calibrations applied successfully!")
