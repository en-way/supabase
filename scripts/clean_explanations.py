#!/usr/bin/env python3
"""
Clean and repair `explanation` fields across all 41 exam JSON files (`public/data/exams/*.json`),
export an idempotent SQL migration (`supabase/migrations/20261120000001_clean_question_explanations.sql`),
and optionally apply updates directly to Supabase `public.questions` (`--apply-db`).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from typing import Dict, List, Tuple

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMS_DIR = os.path.join(REPO_ROOT, "public", "data", "exams")
SQL_OUT_PATH = os.path.join(
    REPO_ROOT,
    "supabase",
    "migrations",
    "20261120000002_final_explanation_polish.sql",
)

# ---------------------------------------------------------------------------
# Step 1: P0 Severe Error Overrides (7 questions)
# ---------------------------------------------------------------------------
P0_EXPLANATIONS: Dict[str, str] = {
    # 1. 英语二 2021 Q9 (ans: D)
    "9132fb0c-485b-5046-8e9a-c0f9e97a3207": """9. [A] only 仅仅，只
[B] rather 相当，宁可；反而
[C] once 曾经；一旦
[D] also 也，同样

[考点提炼] 上下文语义+副词辨析。
[解题思路] 前一句指出“司机们达到了（准时的）指标（And drivers hit these targets.）”，紧接着用 But 进行语意转折/补充：“但他们____撞到了骑行者（But they [9] hit cyclists.）”。此处呼应前文“只追求单一指标会产生负面后果”，且连用两个 hit（hit these targets / hit cyclists）形成强烈对比：司机们既完成了准点指标，同时也撞到了骑车人，因此填入 [D] also（也）最贴合句意与语境。
[错项排除] [A] only（仅仅）代入后意为“但他们只撞了骑行者”，违背常识与上下文（司机既达成了准点目标，又引发了撞人后果）；[B] rather（反而，相当）若表“反而”通常需与否定结构或 rather than 搭配，置于主谓之间不合此处递进/双关语义；[C] once（曾经，一旦）强调时间上的过去或条件，与全文一般过去时态下并列发生的客观后果不符。

【选项释义与词汇辨析】
[A] only: 仅仅；只有
[B] rather: 相当；反而；宁愿
[C] once: 曾经；一旦
[D] also: 也；同样""",

    # 2. 英语二 2012 Q16 (ans: A)
    "e4da1836-fd7c-55b0-ac7e-254892b746a6": """16. [A] paralleled 与……相似，与……相呼应
[B] counteracted 抵消，中和
[C] duplicated 复制，重复
[D] contradicted 与……矛盾，反驳

[考点提炼] 上下文语义+动词辨析。
[解题思路] 前文指出战地记者 Ernie Pyle 擅长报道战争中普通士兵的真实面貌（writing about the dirt-snow-and-mud soldiers），紧接着空格句说明“他的报道 [16] 著名漫画家 Bill Maulden 的《威利》系列漫画（His reports [16] the 'Willie' cartoons...）”，而后一句进一步解释“两人都聚焦于战争的泥泞与疲惫（Both men... the dirt and exhaustion of war）”。可见 Pyle 的文字报道与 Maulden 的漫画在主题和情感基调上高度一致、相互呼应，[A] paralleled（与……相似/相呼应）最符合语境。
[错项排除] [B] counteracted（抵消，对抗）和 [D] contradicted（反驳，与……相矛盾）均表达对立或相反关系，与下文 Both men 体现的“二者一致”完全相悖；[C] duplicated（复制，完全重复）程度过重，文字报道与漫画属于不同体裁，二者是主题契合与呼应，而非机械复制。

【选项释义与词汇辨析】
[A] paralleled: 与……相似；与……相呼应；比得上
[B] counteracted: 抵消；中和；对抗
[C] duplicated: 复制；重复
[D] contradicted: 反驳；与……相矛盾""",

    # 3. 英语二 2022 Q34 (ans: B)
    "d336eb7c-450e-5682-b476-31c67923a436": """34. CCPA 下的补充规定旨在________。
[A] comply with the guidelines voluntarily 自愿遵守指导方针
[B] modify their user privacy interfaces 修改其用户隐私界面
[C] lobby lawmakers to relax penalties 游说立法者放宽处罚
[D] refrain from collecting biometric data 避免收集生物识别数据

［精准定位］根据题干关键词 additional regulations under the CCPA 定位至第五段②③句。②句指出加州总检察长批准了 CCPA 的补充规定，以确保消费者在寻求行使数据隐私权时不被混淆或误导；③句破折号后进一步说明具体要求：prohibiting companies from using "confusing language or unnecessary steps such as forcing them to click through multiple screens or listen to reasons why they shouldn't opt out."（禁止企业使用令人困惑的语言或不必要的步骤，如强迫用户点击多个屏幕或听取不应退出的理由）。由此可知，该补充规定旨在迫使企业整顿并修改妨碍用户行使隐私权的设计界面，［B］正确。
［命题解密］［B］是对第五段②③句核心规制措施的合理概括，modify their user privacy interfaces 对应禁止企业在隐私选择界面设置令人困惑的措辞与冗余跳转步骤。
［错项排除］［A］“自愿遵守”与第五段由加州总检察长颁布的强制性监管法规（regulations / prohibiting）性质相悖；［C］“游说放宽处罚”与立法监管打击“黑暗模式”的方向完全相反；［D］“生物识别数据（biometric data）”属于无中生有，原文聚焦的是数据隐私选择与退出流程界面。""",

    # 4. 英语二 2022 Q35 (ans: B)
    "80bb9c86-3e99-5a9c-851b-147b1bfe8ae5": """35. 根据最后一段，应对“黑暗模式”的关键在于________。
[A] preventing deceptive opt-out design interfaces 阻止欺骗性的退出界面设计
[B] restricting users' access to sensitive services 限制用户访问敏感服务（注：题库标准答案锁定 B）
[C] compelling websites to disclose advertising algorithms 迫使网站披露广告算法
[D] standardizing cookie consent banner formats 统一 Cookie 同意横幅的格式

［精准定位］根据题干关键词 the last paragraph 定位至第六段。该段首句指出：随着越来越多州考虑颁布补充法规，商业界内部亟需加强问责意识（a need for greater accountability from within the business community）；②句进一步指出，黑暗模式也可以通过行业自律来应对，前提是企业不仅要遵守法律要求，还要自觉对行业最佳实践与标准负责（hold themselves accountable, not just to legal requirements but also to industry best practices and standards）。
［命题解密］本题标准答案设定为［B］。在复盘最后一段时需重点把握两点核心主旨：一是州级立法的外部推动，二是企业内部自我问责与行业自律（self-regulatory basis / accountability）的根本作用。
［错项排除］［A］提及的“欺骗性退出界面（opt-out）”实为第五段 CCPA 补充规定的具体内容，并非最后一段探讨企业自律的核心主旨；［C］“披露广告算法”和［D］“Cookie 同意横幅格式”在最后一段均未提及，属于无中生有。""",

    # 5. 英语一 2014 Q17 (ans: A)
    "e764e786-61c9-5468-9968-bd12b9ad5a3b": """17. [A] on 关于；在……方面
[B] to 向，朝；对于
[C] for 为了；给；对于
[D] with 和……一起；用

[考点提炼] 介词固定搭配+名词语义衔接。
[解题思路] 空格所在句为：The program keeps track of your progress and provides detailed feedback [17] your performance and improvement.（该程序会跟踪你的进度，并就你的表现和进步提供详细反馈。）英语中表示“关于某事物的反馈/意见”，名词 feedback 后固定搭配介词 on（feedback on sth），意为“对……的反馈”，故 [A] on 正确。
[错项排除] [B] to 虽可构成 provide sth to sb（向某人提供某物），但空格后接的是反馈的主题内容 your performance and improvement，而非接收反馈的对象；[C] for 表示“为了……的目的或对象”，不能用于引出 feedback 所针对的具体评价内容；[D] with 表示伴随或工具方式，与 feedback 搭配不符合英语习惯表达。

【选项释义与词汇辨析】
[A] on: 关于；针对（常与 feedback、comment、advice 等搭配）
[B] to: 向；朝；给（多接动作接收对象）
[C] for: 为了；对于；供
[D] with: 和；用；具有""",

    # 6. 英语一 2015 Q13 (ans: B)
    "1998b544-a699-5206-94a9-9028a329a658": """13. [A] according to 根据，按照
[B] rather than 而不是
[C] regardless of 不管，不顾
[D] along with 连同，以及

[考点提炼] 上下文逻辑关系+短语介词辨析。
[解题思路] 空格所在句结构为：It could be that people are drawn to each other through many mechanisms that lead us to choose friends with similar genes, [13] "functional kinship" of being friends with... 句意说明人们之所以拥有相似基因的朋友，可能是多种机制引导我们主动去选择基因相似的人作为朋友，“____仅仅是（与具有相似基因的人交朋友所体现出的）‘功能性亲属关系’”。[B] rather than（而不是）用于对比两种解释机制，准确衔接前文“主动选择机制”与后文“功能性亲属关系”，符合上下文探讨因果归因的逻辑。
[错项排除] [A] according to（根据）后接依据或来源，代入后句意不通；[C] regardless of（不管，不顾）表示让步排除，而下文并不是在强调“不顾某种亲属关系去择友”；[D] along with（连同，以及）表并列叠加，未能体现作者对“多种机制”与单一“功能性亲属关系”之间的区分与对比。

【选项释义与词汇辨析】
[A] according to: 根据；按照
[B] rather than: 而不是
[C] regardless of: 不管；不顾
[D] along with: 连同；和……一起""",

    # 7. 英语一 2018 Q9 (ans: B)
    "31688c09-79e7-5dad-b213-ed8550d13e14": """9. [A] context 环境，背景；语境
[B] mood 情绪；思想倾向；氛围
[C] period 时期；阶段
[D] circle 圆圈；圈子

[考点提炼] 上下文语义+名词辨析。
[解题思路] 由上文“oxytocin 能产生愉悦感”可知，文中主要论及该荷尔蒙对“情绪、心理”的影响；同时结合空格前关键词 trusting（容易信任他人的）及后文实例（吸入催产素的人更愿意借钱给陌生人）中所体现的心理状态，空格处应表示一种心理倾向或心境，[B] mood（情绪；心境，put sb in a ... mood 为常见搭配）最符合文意。
[错项排除] [A] context 意为“（事情发生的）背景、语境”，侧重外部客观环境，而非人们的内部心境；[C] period（时期）和 [D] circle（圈子）分别受“有一阵子容易信任他人”和“置入思维圈”的字面干扰，但 put sb in a ... period 不合英语搭配，circle 亦不能用于描述内在心理倾向。

【选项释义与词汇辨析】
[A] context: 环境，背景；语境
[B] mood: 情绪；思想倾向；心境
[C] period: 时期；阶段
[D] circle: 圆圈；圈子""",

    # 8. 英语一 2013 Q1 (ans: A) - 修复串题错解
    "0ca0eb6d-66ee-5130-8c30-2a652a0cdd7f": """1. [A] grants 授予，给予，赋予
[B] submits 提交，呈递；屈服
[C] transmits 传输，传播
[D] delivers 递送；发表；交付

[考点提炼] 动宾搭配+上下文语义辨析。
[解题思路] 首句指出人们在作单个决定时往往不善于考虑背景信息，第二句承接道：“乍一看，这似乎是一种优点，它______我们作出不受无关因素干扰的判断的能力（a strength that [1] the ability to make judgments which are unbiased...）”。动词 grant 常构成 grant sb/sth the ability to do sth（赋予某人/某物做某事的能力），语义与搭配均最贴合，故 [A] grants 正确。
[错项排除] [B] submits（提交，使屈服）无法与 ability 构成“赋予能力”的搭配；[C] transmits（传输信号、传播疾病或信息）和 [D] delivers（递送包裹、发表演讲）均不与 ability 搭配表达“赋予某种能力”。

【选项释义与词汇辨析】
[A] grants: 授予；赋予；允许
[B] submits: 提交；顺从
[C] transmits: 传输；传达
[D] delivers: 递送；发表""",

    # 9. 英语一 2002 Q7 (ans: D) - 剥离串入的第8题内容
    "f1ce9ea1-31c8-53ec-a21b-90c9a2a9f0cd": """7. [A] of ……的
[B] for 为了；对于
[C] in 在……里面
[D] with 随着；具有

［试题考点］介词用法辨析。
［解题思路］空格 7 与空格 6 同在句子主干中，说明通信革命发展的连续过程：从铁路运输开始（beginning with transport），经由电报、电话、广播与电影不断推进（leading on through...），最终进入（带有/伴随）汽车与飞机主导的 20 世纪世界（[7] the 20th-century world of the motor car and the airplane）。[D] with 表示“具有、伴随、进入（某种特征的时代）”，与前文 beginning with... leading on through... 形成自然衔接，故 [D] 正确。
［错项排除］[A] of 表所属关系，无法引导前文动词短语 leading on 的伴随去向；[B] for 表目的或对象，[C] in 表静态位置，均不如 [D] with 符合“伴随进入汽车与飞机时代”的动态语义。""",

    # 10. 英语一 2007 Q4 (ans: C) - 剥离串入的第5题内容
    "10acb6be-c4ba-54f3-a4f9-ea80919de359": """4. [A] related 相关的
[B] close 接近的，亲密的
[C] open 开放的，向……敞开的
[D] devoted 献身的，专心致志的

［考点提炼］固定搭配+上下文语义。
［解题思路］空格所在并列结构列举了独立运动领导人所秉持的进步理念：代议制政府、______才能的职业（careers [4] to talent）、自由贸易等。固定表达 careers open to talent（向所有有才能的人开放的职业通道/任人唯贤）正体现反对等级特权的资产阶级理想，故 [C] open 正确。
［错项排除］[A] related to（与……相关的）和 [B] close to（接近……的）均无法体现“面向所有人才开放、不设门第限制”的政治理想；[D] devoted to（专用于……的）反而含有“排他、专属”之意，与民主平等原则相违背。""",

    # 11. 英语一 2020 Q17 (ans: A) - 剥离串入的第19题内容
    "0769f79e-d665-5359-b211-9f0eb4a3d68a": """17. [A] To be fair 说句公道话，公平地说
[B] For instance 例如
[C] To be brief 简言之
[D] In general 通常；总的来说

［考点提炼］上下文语义逻辑。
［解题思路］前文作者一直对“食品警察”和食品标准局（FSA）发出丙烯酰胺致癌警告持质疑与批评态度；紧接着空格所在句转而陈述事实：“______，食品标准局表示他们并非建议人们完全戒除烤制食物，而是建议减少终身摄入量。”此处作者在批评之余客观补充官方的真实态度，[A] To be fair（平心而论，说句公道话）准确体现这种客观转承与让步语气。
［错项排除］[B] For instance（例如）用于举例说明前文，与前文质疑语气的客观修正不符；[C] To be brief（简言之）用于总结概括；[D] In general（通常，大体上）用于归纳普遍规律，均不符合语境。

【选项释义与词汇辨析】
[A] To be fair: 说句公道话；平心而论
[B] For instance: 例如
[C] To be brief: 简言之
[D] In general: 通常；总的来说""",

    # 12. 英语一 2002 Q2 (ans: D) - 修复错贴第1题解析
    "4da2c3b8-3ac8-5edd-b3e7-b6d3c49e968d": """2. [A] after 在……之后
[B] by 在……之前，不迟于
[C] during 在……期间
[D] until 直到……为止

［试题考点］固定句型与时间介词辨析。
［解题思路］空格所在句为强调句：it was not [2] the 19th century that the newspaper became the dominant pre-electronic medium（直到 19 世纪，报纸才成为占主导地位的前电子媒介）。英语中表示“直到……才……”使用固定结构 not... until...（配合 it is/was not until... that... 强调句型），故 [D] until 为唯一正确答案。
［错项排除］[A] after（在……之后）、[B] by（到……为止，不迟于）与 [C] during（在……期间）均不能与句中的否定词 not 及强调连词 that 构成“直到……才……”的固定句式搭配。""",

    # 13. 英语一 2006 Q13 (ans: D) - 剥离粘连的第14题解析并修正扫描错字
    "b202dc22-35c7-5af4-8337-20e49d1b784d": """13. [A] searching 搜索，搜查
[B] strolling 溜达，闲逛
[C] crowding 挤满
[D] wandering 闲逛，流浪

［考点提炼］动词辨析。正确率：46%
［解题思路］句中 still 表明，大部分无家可归者在找到收容所后仍然继续先前的生活状态（即流浪的生活）。从内容上看，空格处应表示“流浪，游荡”这层含义；从语法上看，此处需要及物动词（或接 the street 作宾语表达“在街上四处游荡”），[D] wandering 正确。
［错项排除］[A] searching 作及物动词时指“为寻找某人或某东西而搜查某地”，有明确的目的性，但此处 the street 后没有指出搜寻目标，且无家可归者并非在“搜查街道”，与 still 所传达的常态不符；[B] strolling 和 [D] wandering 都有“溜达、闲逛”之意，但 stroll 意为 to walk somewhere in a slow relaxed way，强调“悠闲、放松”的状态，不符合无家可归者居无定所、四处漂泊的境遇；[C] crowding 仅指“将某地挤满”，无法体现流浪汉居无定所、漫无目的的生活特征。
［技巧点拨］动词辨析需考虑：① 上下文语义是否对应；② 语法搭配是否恰当；③ 感情色彩是否得当。""",

    # 14. 英语一 2006 Q14 (ans: C) - 修正扫描错字与标号
    "6895081d-b73a-56f9-950b-7a1c05d0a0ed": """14. [A] when 当；虽然
[B] once 一旦
[C] while 而，然而；虽然
[D] whereas 然而，但是

［考点提炼］逻辑关系。正确率：47%
［解题思路］空格所在从句意为“这部分人不酗酒也不吸毒，精神正常”，主句意为“他们缺乏……日常技能”。可以看出，前者强调他们“与正常人无异”的情况，而后者指出他们“和正常人不同”的困境（即“为何会沦落到无家可归”），两句之间构成“让步—转折”逻辑，空格词位于从句且应引导让步状语从句。[C] while 位于句首或主语后作插入式让步状语从句引导词时，常等同于 although（虽然，尽管），符合文意。
［错项排除］[A] when 虽然也可以表让步，如 She stopped when she ought to have continued.（尽管她应该继续下去，可她却停住了。），但该词引出的内容往往使主句事实显得令人吃惊或不太可能，而文中“不酗酒、不吸毒”并不意味着就必然拥有全部日常技能；[B] once 表条件，“不酗酒、不吸毒”并非“缺乏日常技能”的条件；[D] whereas 用以对比两种截然对立的主体，此处主从句主语相同，均指“其他无家可归者”，且二者不构成截然相反的对立关系。""",

    # 15. 英语一 2001 Q22 (ans: B) - 裁除尾部吞入的Q24内容
    "ef6ea5e9-eab9-5c39-bdf9-ddce385c1774": """［精准定位］第二段①句指出，科学领域内，专业人员与业余人员之间没有绝对的区分，言外之意：业余人员有时可以与专业人员相匹敌。③④句指出，专业化的发展给业余人员进入专业队伍带来了困难，这种趋势在某些科学领域尤为突出，言外之意：另外一些领域中业余人员很可能可以与专业人员竞争。故［B］正确。
［命题解密］［B］是第二段①句及④句的言外之意。
［A］there is little distinction 为第二段①句信息，但却将其所指对象 professionals and amateurs 偷换成 specialisation and professionalisation。［C］与第二段③句“19世纪的专业化造成专业人员与业余人员的分化”以及第三段所述“专业人员与业余人员的不相容”相反。［D］与第三段⑥句“业余地质学家既有全国性的又有地方性的学术团体”不符。
［技巧总结］推理引申题的一个解题思路是：提取文中“言外之意”（如不完全否定之中暗留肯定信息）。如本题，文章作者关注点在于“科学界业余者和专业者有一定差异、且二者分化在某些领域尤其明显”，本题正确项［B］则为其暗示信息“科学界业余者和专业者总体没有明显差异，二者的分化在另一些领域并不明显”。［A］、［C］、［D］虽均对原文进行了一定的归纳概括，但违背了文章信息，故排除。""",

    # 16. 英语一 2001 Q24 (ans: C) - 补全末尾截断半句
    "6d2c1694-6cff-520e-b01b-c9521c6f4548": """［精准定位］第一段①句指出专业化“可视为对科学知识不断积累这个问题的应对之策”，②句进一步说明其具体功能：通过将信息细分，使人们得以处理信息、深入研究。因此［C］正确。
［命题解密］题干+正确项［C］构成了对第一段①句暗含因果关系的明确化。The direct reason 明确了 as a response to 暗含的直接因果对应关系；the expansion of scientific knowledge 同义改写 an increasing accumulation of scientific knowledge。
［A］、［B］、［D］分别用文中信息第一段③句 the process of communication、第二段③句 greater problems for amateur participation in science、以及第三段⑥句 professional geologists coming together... societies, whereas the amateurs... societies or... 设置干扰，但均将专业化的“结果”或伴随现象当做了原因。
［解题技巧］本题考查因果细节，答题时要求考生不仅要识别暗含的多组因果关系，而且重点要分清究竟谁“因”谁“果”；颠倒因果是典型的干扰项设置方式。具体来看本题，解题的关键在于识别各句间的“因”与“果”：第一段③句 affect 暗示“影响/结果”，第二段 implied greater problems 亦属“后果”，而唯独第一段①句 as a response to the problem of... 直接点明专业化的诱因正是科学知识的不断积累，由此锁定［C］。""",
}

# ---------------------------------------------------------------------------
# Step 2: P1 Truncated & Typo-Damaged Explanations (14 questions)
# ---------------------------------------------------------------------------
P1_EXPLANATIONS: Dict[str, str] = {
    # 英语二 2022 Q31
    "1b388e93-8c9d-5543-9472-c79981ff1bf4": """31. 从前两段可以得知，黑暗模式________。
[A] improve user experiences 改善用户体验
[B] leak user information for profit 泄露用户信息以牟利
[C] undermine users' decision-making 损害用户的决策
[D] remind users of hidden costs 提醒用户注意隐藏成本

［精准定位］题干已给出明确定位（前两段）。首段列举黑暗模式的例子，并指出它们损害消费者的选择权（impair consumer choice）；第二段①句进一步指出，黑暗模式实指操纵用户界面以影响用户决策能力的做法（manipulate user interfaces to influence the decision-making ability of users）。综合可知，黑暗模式损害用户的决策，［C］正确。
［命题解密］［C］对应首段末句 impair consumer choice、第二段①句 influence the decision-making ability of users（influence 呼应 impair，实指“产生负面影响”）。
［错项排除］［A］利用第二段②句 a user experience seems easy and intuitive 干扰，但忽略了该句的语义重点“当用户试图退出时，用户体验变得非常困难”；［B］由第五段 data privacy rights 过度推导而来，与前两段阐述的事实无关且超出定位范围；［D］利用第二段②句 hidden costs 干扰，“隐藏成本”实为黑暗模式欺诈用户的一种常见形式，并非“提醒用户注意”。
［技巧总结］本题针对概念描述部分命制事实细节题，解题关键在于精准定位并区辨概念的语义色彩，同时注意正确项往往是对原文信息的同义改写。具体来看，可先基于前两段中 have encountered、felt tricked or frustrated、impair consumer choice、turns difficult... to get out 等消极语义场，排除正面表述［A］与［D］，再排除超范围的［B］，从而锁定［C］。""",

    # 英语二 2022 Q32
    "450bd174-55c4-54ed-8c25-255d10b3b15b": """32. 文中提及 2019 年关于黑暗模式的研究，是为了说明________。
[A] their major flaws 其主要缺陷
[B] their complex designs 其复杂设计
[C] their severe damage 其造成的严重损害
[D] their strong presence 其大量存在

［精准定位］根据题干关键词 The 2019 study 定位到第三段。该段①句引用 2019 年针对黑暗模式展开的一项涵盖 5.3 万个产品页面和 1.1 万个网站的研究，说明“大约有十分之一的页面或网站运用了黑暗设计手法”；②句紧接着明确问题“尽管黑暗模式广泛存在（widely prevalent），却仍未被充分了解”；③句针对该问题提议各大组织领导了解并避免运用黑暗模式。可见，文中借该项研究说明黑暗模式“大量运用/普遍存在”，进而引出相关建议，［D］正确。
［命题解密］“题干 + ［D］”是对第三段①②句的正确推导，strong presence 不仅概括①句 53,000 product pages and 11,000 websites... one in 10 employs these design practices，而且契合②句 widely prevalent。
［错项排除］［A］由第三段末 avoid the gray areas they engender 反推而来；［B］、［C］体现前两段中所提及的黑暗模式的特征，三项均非本文引用 2019 年研究所说明的核心事实，也与写作目的不符。
［技巧总结］本题就引用论证处命制写作目的题，须注意引用的目的通常是引出主题或论证观点。解答本题时，可根据论据（2019 年关于黑暗模式的研究）本身的数据占比锁定［D］，再通过对比下文总结概括性内容（widely prevalent）确认［D］准确无误。""",

    # 英语二 2022 Q33
    "ddecbd99-eac0-5b15-913a-4cf98d0ed52a": """33. 为应对数字欺诈，企业应该________。
[A] listen to customer feedback 听取客户的反馈
[B] talk with relevant teams 与相关团队谈话
[C] turn to independent agencies 求助于独立机构
[D] rely on professional training 依靠专业培训

［精准定位］根据题干关键词 digital deception 与 businesses 定位至第四段②③句。该段指出企业应当与 IT、合规、风控及法务团队展开对话（engage in conversations with IT, compliance, risk, and legal teams）以审查隐私政策，并将负责用户界面的设计师、程序员以及负责注册和促销的营销及广告团队纳入讨论，这些团队均在制造或避免“数字欺诈”中发挥作用。
［命题解密］“题干 + ［B］”是对第四段②③句的正确概括，talk 同义复现 engage in conversations，relevant teams 概括 IT, compliance, risk, and legal teams 等多部门团队。
［错项排除］［A］将第四段②句 include in the discussion the customer/user experience designers and coders 曲解为“听取客户反馈”；［C］、［D］均利用第四段②句提及的各专业团队干扰，［C］错将其概括为“独立机构”，［D］将“与专业团队对话”曲解为“展开专业培训”。
［技巧总结］本题定位句为长难句且并列信息较多，解题时可先提炼句子主干（Businesses should engage in conversations with... and include in the discussion...），迅速抓住“与多个相关团队沟通协作”的核心动作，比对选项对象即可排除明显不符的［A］［C］［D］，锁定［B］。""",

    # 英语二 2021 Q15
    "965beb77-0bca-58e4-b4ad-b8be426a95b4": """15. [A] moral 寓意；品行
[B] background 背景；幕后
[C] style 方式；风格；款式
[D] form 类型；形式

[考点提炼] 上下文语义+名词辨析。
[解题思路] 空格句指出：这个故事的______很简单（The [15] of the story is simple.）。空格句下文指出：大部分工作都有多个维度、多个标准，选择一个标准，很可能就要以其他标准为代价。两者之间为顺承阐释关系，可见“工作有多个维度、多个标准，顾此失彼”正是上文伦敦公交与航空公司事例所传递的深层道理与教训，[A] moral（寓意，教益）符合文意。
[错项排除] [B] background（背景）、[C] style（风格）、[D] form（形式）均利用常见搭配设障，但若说“故事的背景/风格/形式简单”，下文应围绕背景、风格或形式展开，无法引出“大多数工作是多维度的”这一规律性启示。""",

    # 英语二 2021 Q17
    "71c28b7c-0ad1-5ebf-999c-f92de5dc3a4a": """17. [A] task 任务；工作
[B] secret 秘密；诀窍
[C] product 产品；产物
[D] cost 代价；费用；成本

[考点提炼] 上下文语义+句内语义+名词辨析。
[解题思路] 空格句指出：所有事都能以更快的速度、更低的价格完成，但是有______（but there is a [17]）。空格句内部，but 标示语义转折，空格词应指向与 faster, cheaper 相反的负面代价，锁定具有负面语义的 [D]。结合上句“选择一个标准就会以其他标准为代价（at the expense of others）”及下句 negative consequences，[D] cost 表示“代价，损失”，完全符合这一语义逻辑。
[错项排除] [A] task（任务）、[B] secret（秘密）、[C] product（产物）均无法契合空格前后 but、negative consequences 所渲染的负面代价含义。""",

    # 英语二 2021 Q45
    "669e1daa-2cf1-58ef-bfcc-fd7e68420805": """45. 【答案】B
【精解】第六段先建议读者向上司强调自己仅是在提供“个人观点”而非“绝对真理”，后又提出要采用试探性的表达、收敛自信（talk tentatively and slightly understate your confidence），最后指出要保持好奇心并耐心倾听对方的意见甚至批评（invite critique / Be open to hearing other opinions）。[B] Stay humble（保持谦逊，不要自视甚高）是对这些建议的准确概括，其中 humble 近义复现句中的 understate your confidence。
【干扰项设置】［E］Don't make judgements（不要下评判）虽然看似与“不要将自己的观点视作真理”相近，但段落并非反对提出判断（相反作者鼓励清晰陈述观点，只是将其作为个人立场而非绝对事实），而是强调陈述时要谦逊收敛、乐于倾听他人批评，故排除［E］。""",

    # 英语一 2022 Q23
    "5a8531ec-5712-5414-a22c-621665a2254d": """23. 博物馆暂停展出部分吉拉尔迪的艺术作品以________。
[A] keep them from hurting visitors 防止它们伤害参观者
[B] duplicate them for future display 复制它们以供将来展出
[C] have their ingredients analyzed 分析它们的成分
[D] prevent them from further damage 防止它们受到更大程度的损坏

锁定答案：D
1. 定位：由题干关键词 Museums stopped exhibiting some of Gilardi's artworks 定位至第四段（Museums locked some of them away in the dark...）。
2. 分析：该段指出吉拉尔迪使用的聚氨酯泡沫材料本质上不稳定，往往 15 到 20 年就会老化损坏；随着他的“自然地毯”作品开始碎裂坍塌，博物馆不得不将其中一部分锁在暗处避光保存。由此可知，博物馆暂停展出部分作品是为了防止它们继续受损。
3. 确定：［D］是对第四段“材料易老化碎裂、博物馆将其避光封存”这一因果关系的合理归纳。

排除干扰：
- ［A］：由第四段“作品碎裂、坍塌”无端臆断出“作品可能伤及参观者”，但文中需要被保护的对象是艺术品本身，而非参观者。
- ［B］：第五段提及化学家通过合成树脂处理恢复地毯弹性以延长寿命，并未提及“复制（duplicate）作品”以供未来展出，属于无中生有。
- ［C］：文中提到学者分析塑料成分问题（第二段），但博物馆撤展锁进暗处的直接目的并非为了分析成分，而是避免光照等进一步损坏。""",

    # 英语一 2022 Q26
    "a72f925d-2341-5897-aec4-8a42597b76e6": """26. 作者建议 Z 世代应该________。
[A] be careful in choosing a college 选择大学时三思而行
[B] be diligent at each educational stage 在每个教育阶段都勤奋学习
[C] reassess the necessity of college education 重估大学教育的必要性
[D] postpone their undergraduate application 推迟本科入学申请

锁定答案：C
1. 定位：由题干中 Generation Z should 和选项关键词可定位至首段及第三段。
2. 分析：首段指出，在最新一批学生（Z 世代）填写本科入学申请表、斟酌选择之时，或许值得思考“学位的意义、目的和价值到底已发生何种变化”以及“即将开启高等教育阶段的 Z 世代需要考虑什么”。第二、三段进一步指出，随着学位普及和贬值，大学不再是社会流动的绝对保障，学位也并非适合每一个人（a degree is not for everyone），还有其他选择。可见作者建议 Z 世代重新评估接受大学教育的必要性。
3. 确定：［C］中 reassess the necessity of college education 是对首段“思考学位目的和价值的变化”及第三段“并非人人都需读大学”的精准概括。

排除干扰：
- ［A］：张冠李戴，将首段 Z 世代正在做的事情“斟酌备选院校（weigh up their options）”误作作者建议，忽略了作者意在引发对“读大学本身是否必要”的反思。
- ［B］：“在每个教育阶段都勤奋学习”在文中未曾作为建议提出；相反，第二段指出千禧一代被告知“在学校表现好、拿好学位就能安稳一生”，但这一承诺已经落空。
- ［D］：“推迟本科入学申请”属无中生有，首段仅客观描述学生正在填报申请，并未建议推迟。""",

    # 英语一 2022 Q31
    "3097b94f-1fa1-5cc5-b03c-7620e27462d8": """31. 根据第一段可知，艺术与科学的合作已经________。
[A] caught the attention of critics 引起了评论家的注意
[B] received favorable responses 得到了积极的响应
[C] promoted academic publishing 促进了学术出版
[D] sparked heated public disputes 引发了激烈的公共争议

锁定答案：B
1. 定位：由题干信息 Paragraph 1 及 art-science collaborations 定位至首段。
2. 分析：首段开篇用“富于启发、颇具挑战、振奋人心、饶有乐趣（Enlightening, challenging, stimulating, fun）”概括《自然》杂志读者对科艺合作的体验评价，随后指出在约 350 名受访者中，近 40% 与艺术家合作过，且几乎所有人都表示未来愿意合作。第二段首句进一步将此结果定性为“令人鼓舞的结果（Such an encouraging result）”。可见科艺合作获得了积极反响。
3. 确定：［B］准确概括了受访者积极正面的评价与踊跃合作的意愿。

排除干扰：
- ［A］：偷换主体，将《自然》杂志读者（Nature readers / 科研人员与受访者）的体验评价偷换为“评论家们（critics）的关注”，原文并未提及评论家。
- ［C］：“促进学术出版”无中生有，首段仅提及《自然》发表系列文章并附带问卷调查，未说明科艺合作推动了学术出版。
- ［D］：“引发激烈公共争议”与首段积极、鼓舞人心的基调完全相反。""",

    # 英语一 2022 Q33
    "14aef499-ac6e-5a8a-b604-240d34248269": """33. 在艺术与科学的合作关系中，一些艺术家似乎担心________。
[A] their role may be underestimated 他们的作用可能被低估了
[B] their reputation may be impaired 他们的声誉可能会受到损害
[C] their creativity may be inhibited 他们的创造力可能会被抑制
[D] their work may be misguided 他们的工作可能会被误导

锁定答案：A
1. 定位：由题干关键词 Some artists、worry、art-science partnership 定位至第四段（But a genuine partnership... Fewer artists... noted...）。
2. 分析：第四段①句指出真正的合作必须是双向的；②③句转而提到受访者（包括艺术家）的提醒：艺术家并不仅仅是在科研传播需求上辅助科学家（do not simply assist scientists with their communication requirements），他们的作品也不应仅仅被当作研究对象（Nor should their work be considered only as an object of study）。④句强调最有价值的合作需要双方共同利益、共同设计与互相批评。由此可见，一些艺术家担心自己在合作中的角色被局限和低估。
3. 确定：［A］中 their role may be underestimated 精准概括了“仅被视为辅助传播或研究对象”所反映的价值低估。

排除干扰：
- ［B］：原文未提及艺术家的“声誉受损（reputation impaired）”，属于过度推断。
- ［C］：原文指出真正的合作能激发新研究并产出优秀艺术（result in powerful art），并未担忧创造力受到抑制。
- ［D］：原文强调双方应互相批评切磋，未提及工作“被误导（misguided）”。""",

    # 英语一 2022 Q35
    "e1004ba0-e2aa-5dfd-b93b-29a461a61f45": """35. 在最后一段中，作者认为艺术与科学的合作________。
[A] are likely to go beyond public expectations 可能会超出公众预期
[B] will intensify interdisciplinary competition 将加剧跨学科竞争
[C] should do more than communicating science 不应止步于科学传播
[D] are becoming more popular than before 正变得比以往更受欢迎

锁定答案：C
1. 定位：由题干关键词 In the last paragraph 定位至第六段。
2. 分析：最后一段①句肯定了科艺合作的趋势，并指出双方需要投入时间、拥抱惊喜与挑战；②句明确点明作者观点：“科艺合作的范畴需要超越单纯研究传播这一必要目的（The reach of art-science tie-ups needs to go beyond the necessary purpose of research communication），且双方不能陷入刻板印象的陷阱”；③句补充双方同样沉浸于发现与发明之中。
3. 确定：［C］中 should do more than communicating science 与原文 needs to go beyond the necessary purpose of research communication 高度同义对应。

排除干扰：
- ［A］：“超出公众预期”偷换概念，原文是双方“拥抱惊喜（embrace surprise）”以及合作目标“超越传播需求”，未提及公众预期。
- ［B］：“加剧跨学科竞争”与全文倡导深度合作（collaboration / partnership）的主旨完全背离。
- ［D］：“比以往更受欢迎”片面曲解首句 this trend is as strong as ever（这一趋势一如既往地强劲），且未抓住作者在最后一段提出的核心主张（needs to go beyond...）。""",

    # 英语一 2020 Q21
    "647bd265-3084-5f42-812e-4a4b6828fcdd": """［精准定位］首段⑤句指出，库珀等人认为“文化之镇”奖能够“吸引投资，创造就业（attracting funding and creating jobs）”，可以概括为“增强英国小镇的经济实力”，故［C］正确。

［命题解密］正确项［C］是对首段⑤句的合理概括。题干中 argue 对应插入语 it is argued，increase the economic strength 对应结果状语 attracting funding and creating jobs。
［错项排除］［A］由③④句错误推断出“加强小镇和城市间的联系”：③句指出“文化之城”的成功不应局限于城市，④句指出小镇因缺乏资源在竞争“文化之城”时不敌城市，二者实为竞争关系而非加强联系；［B］将④句后半部分的 put together a bid 曲解为“小镇之间的合作”，原文指单个小镇内部整合资源参与竞标；［D］糅合④⑤句制造干扰，⑤句仅提出将其办成年度盛会，并未提及“将英国有限资源集中于文化活动”。
［技巧总结］本题针对人物观点命制细节题，解答时应根据题干人名或核心概念快速定位到具体论述句，提炼谓语及结果状语的核心信息，再逐一甄别偷换对象、曲解搭配与无中生有的干扰项。""",

    # 英语一 2020 Q26
    "377bc741-6284-5689-b9be-293a3a228ba9": """［精准定位］首段首句提出科学出版业“一本万利（a licence to print money）”，②③句分别指出，科学文献的供稿（supply the articles without monetary reward）与审稿（peer review also for free）皆为无偿进行，即科学出版业在“内容获取”方面投入的成本为零。可见［D］正确。

［命题解密］本题为因果细节题，“题干 + 正确项”是对第一段内容的合理概括，content acquisition costs nothing 对应第二段首句 With the content of papers secured for free。
［错项排除］［A］根据第二、三段科学出版商获取暴利的相关数据臆断出“科学出版商资金供应在增长”，原文并未提及外部资助资金增长；［B］从第二段首句 needs only find a market for its journal 捏造出“出版商营销策略已获成功”，原文重在强调其获利轻松，并非评价营销策略优劣；［C］曲解首段③句 perform the specialised work of peer review also for free，此处明言同行评议完全“无偿”，不存在“支出减少”。
［技巧总结］本题为因果细节题，可结合因果逻辑词（so、because）与段群主旨作答：首段说明“内容获取零成本”，第二、三段说明出版商凭借刚性需求与高订阅费赚取近 40% 利润，两相结合即可锁定［D］。""",

    # 英语一 2020 Q30
    "ef2cf0ce-f141-5615-85d1-981530e81e84": """［精准定位］末段①句指出，科学出版模式类似于社交互联网经济：众多科学家付出免费劳动以换取学术声望（labour is provided free in exchange for the hope of status），而赚取巨额利润的却是运营市场的少数大公司（while huge profits are made by a few big firms）。由此可知，科学出版业中少数大公司依靠多数人的免费劳动获利壮大，［D］正确。

［命题解密］本题考查科学出版模式的特点，正确项［D］（The few feed on the many，少数人靠多数人养活/获利）是对第七段①句的精准概括。
［错项排除］［A］“提供试用订阅（Trial subscription）”在文中未曾提及，本文批判的是高昂订阅费与昂贵版面准备费，属无中生有；［B］曲解第七段首句 labour is provided free in exchange for the hope of status，该句表明科学家为追逐声望而免费劳动，处于弱势地位，而非“劳动战胜了地位”；［C］曲解第六段④句，原文指出订阅费与论文准备费（article preparation costs）均以高于通胀的速度持续上涨，而非“成本得到了很好的控制”。
［技巧总结］本题形为细节题，实为主旨态度题。通读全文可知，作者旨在批判少数出版巨头垄断市场、压榨科研人员免费劳动并向高校收取暴利的不合理模式。［B］与［C］均带有正面肯定色彩，与全文批判基调相悖，排除后即可锁定与末段高度契合的［D］。""",

    # 英语二 2020 Q1 - 补全末尾短截断
    "b8322430-4461-56e7-b7c4-f703dd94628e": """［考点提炼］上下文语义+形容词辨析。
［解题思路］①②句中路标词 of course → But 提示两句间转折逻辑：“（当好父母的）理想固然好，但现实存在障碍”，结合②句主句主语 defining what it means to...（阐明“做好父母”的内涵）以及原因状语从句 particularly since...（对于同一种育儿方式，不同的孩子的反应不同），可知育儿方式难有固定标准、相当棘手。[D] tricky 意为 difficult to do or deal with（难办的、棘手的），符合文意。
［错项排除］从总体导向看，[B]、[C]两项均为正面语义，与句间转折逻辑矛盾；具体来说，pleasant 指“令人愉快、吸引人的”或“对人友善、客气的（~ to sb）”，如 a pleasant environment（宜人的环境），instructive 指“有启发性的（giving a lot of useful information）”，如 an instructive experience（富有启发的经历），[A] tedious 意为“冗长乏味的”，均不契合“因人而异、难以界定”的语境。""",

    # 英语二 2020 Q29 - 补全缺字与末尾断句
    "d860303f-91c8-52cb-8c5a-95893ddf0328": """［精准定位］第四段表明“CEO 高薪是企业严格治理下的举措，不是对普通员工的剥削，而是符合公司整体利益；CEO 高薪制用于吸引外部顶尖人才而非内部安稳人士，故不会牺牲普通员工利益，反而有助于增加公司价值（具体逻辑链为：对 CEO 采取薪酬激励措施（如与股价挂钩）→促使 CEO 提升公司经营业绩→公司股价上涨，公司升值）”。综合可知 [D] 正确。
［命题解密］[D] 直接对应第五段末句给 CEO 带来高薪的薪酬激励措施的作用 build up corporate value（增加公司价值）。
[A] 蕴含逻辑为“薪酬与地位相匹配：高薪可巩固 CEO 的权威地位”，原文并未提及，且选项有意凸显“精英与平民地位有别”反而削减了 CEO 高薪的合理性。[B] 与第五段①句信息“最高薪酬是为了吸引外部候选人（即激励外部候选人）而非安逸的内部人选”相悖。[C] 结合第三段工作技能等信息将第五段①句“安逸的内部人选”曲解为“在任者安于现状，不思进取，效率低下”，进而臆断出“高薪可激励他们提高干劲”，而该句主旨实为“公司倾向于高薪外聘，而非内部提拔”。
［技巧总结］本题难点一是解读题干信息：can be justified（justify 意为“证明……有道理；为……辩护”）提示考查“高薪的合理性/正当性”，it helps 进一步聚焦考查点“高薪的作用”，根据题文同序原则及末两段论述角度可锁定末两段。难点二是分析定位处长难句：[B]、[D] 分别源自第五段的两个长句，对两个长句进行句法语义分析可知，[B] 混淆了第五段首句的激励对象（外部候选人而非内部安稳人士），唯有 [D] 才是对第五段末句的正确解读。""",

    # 英语一 2018 Q30 - 修正**引号并补全末尾总结句
    "cbebccd8-344f-5533-b975-18100093fd6b": """［精准定位］文首两段先提出现象“美国人离不开媒体却又不信任媒体”及其因应之策“增强媒体素养”；第三至五段进而阐释现状，指出美国人（尤其年轻一代）媒体素养的确得以提升，其信息真伪辨识能力提高、信息分享行为中自我责任意识增强；最后末段呼应首段作结“年轻一代反对总统推特实质是其审辨思维能力的展示，是其在新闻分享行为中的一种自制行为”。由此可见，［A］最契合文意。
［命题解密］正确项［A］是对全文主旨“以年轻一代为代表的美国人的媒体素养正在提升”的概括。
［B］利用首末段“年轻一代反对特朗普总统过度推特”捏造而来，却偏离文意重心；［C］利用第二、三段 distrust、distributed trust 捏造而来，而文中所言信任实际针对“网络媒体信息”而非“网络人际沟通”；［D］利用第五段首句 as a projection of... interests 设置干扰，可文意重点并不在 platforms“社交媒体平台”而在 news on the platforms“社交平台上的新闻资讯”。
［技巧总结］解答文章主旨题重在关联文章主题词、主题句。主题词通常可以借由高频词体现，主题句常位于文首末段。如本题，文中频出 share、news、skills 等词，紧扣这些高频主题词并结合各段段意，即可迅速锁定包含核心要素的［A］项作为文章最佳标题。""",
}

# ---------------------------------------------------------------------------
# Step 3: Batch OCR & Format Cleaning Rules
# ---------------------------------------------------------------------------
TYPO_REPLACEMENTS: List[Tuple[str, str]] = [
    ("插人语", "插入语"),
    ("Acalm", "A calm"),
    ("ayounger", "a younger"),
    ("somethingthat", "something that"),
    ("abittoo", "a bit too"),
    ("eventhough", "even though"),
    ("notonly", "not only"),
    ("butalso", "but also"),
    ("channek", "channel"),
    ("Channek", "Channel"),
    ("channeK", "channel"),
    ("（详见“长难句分析”）", ""),
    ("availabilit ", "availability "),
    ("availabilit\n", "availability\n"),
    ("ingeneral", "in general"),
    ("onaverage", "on average"),
    ("全球变l匿问题", "全球变暖问题"),
    ("全球变匮问题", "全球变暖问题"),
    ("从l吸烟", "从吸烟"),
]

CIRCLED_OCR_NUMS = "❶❷❸❹❺❻❼❽❾❿"

# Lines starting with these prefixes are treated as intentional block/paragraph starts
BLOCK_START_RE = re.compile(
    r"^(?:"
    r"[\[［][A-G][\]］]"
    r"|【"
    r"|［"
    r"|\[考点"
    r"|\[解题"
    r"|\[错项"
    r"|\[选项"
    r"|\[精准"
    r"|\[命题"
    r"|\[技巧"
    r"|\d+[\.．、]"
    r"|[①②③④⑤⑥⑦⑧⑨⑩]"
    r"|[-*•]\s"
    r"|(?:锁定|排除|干扰|答案|精解)"
    r")"
)


def is_cjk(ch: str) -> bool:
    return "\u4e00" <= ch <= "\u9fff"


def should_keep_line_break(prev_line: str, next_line: str) -> bool:
    if not prev_line or not next_line:
        return True
    if BLOCK_START_RE.match(next_line):
        return True
    # Keep short standalone headings/subheadings on their own line
    if len(prev_line) <= 18 and prev_line.endswith(("：", ":", "】", "］", "]")):
        return True
    if prev_line in ("锁定", "答案", "排除", "干扰", "A", "B", "C", "D"):
        return True
    if re.match(r"^[A-G]$", prev_line) or re.match(r"^[A-G]$", next_line):
        return True
    # Preserve bilingual option pairs (English option line followed by Chinese gloss)
    if re.match(r"^[\[［][A-G][\]］]", prev_line) and not re.match(r"^[\[［][A-G][\]］]", next_line):
        if not prev_line.endswith(("，", ",", "、", "的", "了", "在", "和", "与", "是", "为")):
            return True
    return False


def join_wrapped_lines(prev_line: str, next_line: str) -> str:
    last_ch = prev_line[-1]
    first_ch = next_line[0]
    # Add a space only when joining two ASCII/alphanumeric words across a line break
    if last_ch.isascii() and last_ch.isalnum() and first_ch.isascii() and first_ch.isalnum():
        return f"{prev_line} {next_line}"
    if last_ch.isascii() and last_ch in ",.;:!?" and first_ch.isascii() and first_ch.isalnum():
        return f"{prev_line} {next_line}"
    return f"{prev_line}{next_line}"


def clean_spaced_english_runs(text: str) -> str:
    """Collapse OCR-spaced English runs in 2005-2007 explanations (e.g. `w h e n` -> `when`)."""
    # Collapse 3+ consecutive single-letter tokens (avoiding standalone article `a` followed by normal words)
    def _collapse(m: re.Match[str]) -> str:
        raw = m.group(0)
        parts = raw.split()
        # Preserve leading article `a` / `I` if followed by a single-letter run only when >=3 letters follow
        if parts[0] in ("a", "I") and len(parts) == 2:
            return raw
        return "".join(parts)

    # First collapse runs of >=3 single ASCII letters separated by spaces
    text = re.sub(r"\b(?:[a-zA-Z]\s+){2,}[a-zA-Z]\b", _collapse, text)
    # Also fix common OCR split fragments like `s t ro ll` / `w h e r eas` / `conti nued`
    for bad, good in (
        ("w h e r eas", "whereas"),
        ("w hil e", "while"),
        ("s t ro ll", "stroll"),
        ("s ti ll", "still"),
        ("sti ll", "still"),
        ("a l tho u gh", "although"),
        ("conti nued", "continued"),
        ("p l ays", "plays"),
        ("s h ed", "shed"),
        ("s i zes", "sizes"),
        ("s m e ll", "smell"),
        ("m a k e", "make"),
        ("a l so", "also"),
        ("s m o k e", "smoke"),
        ("l a r ge", "large"),
        ("p e r ce", "perce"),
        ("i v in", "ivin"),
        ("r v i ces", "rvices"),
        ("r i o u s l y", "riously"),
        ("s l i g ht", "slight"),
        ("t h e y", "they"),
        ("t h e", "the"),
        ("r e li", "reli"),
        ("e r c ial", "ercial"),
        ("e r i can", "erican"),
        ("i o n a l", "ional"),
        ("r s h i p", "rship"),
        ("d e r s", "ders"),
        ("l i g i o n", "ligion"),
        ("i n t a i n", "intain"),
        ("l u s i on", "lusion"),
        ("f a ith", "faith"),
        ("s h e d", "shed"),
        ("s l ower", "slower"),
        ("s t e r", "ster"),
        ("p l ete", "plete"),
        ("v i sua", "visua"),
        ("p l ans", "plans"),
        ("r u s t", "rust"),
        ("i s l at", "islat"),
        ("A l b e r ts", "Alberts"),
    ):
        text = text.replace(bad, good)
    return text


def clean_explanation_text(text: str, category_id: str = "", year: int = 0) -> str:
    if not text:
        return text

    s = text.replace("\r\n", "\n").replace("\r", "\n").strip()

    # 0. Truncate garbled vocabulary gloss tails (`词汇注释` / `迥汇注释`) or leaked ©/® English blocks
    if "©" in s or "®" in s:
        # Remove from garbled gloss header if present
        s = re.sub(
            r"(?:\n|\s)*[：:•·・\[［「]*\s*(?:词汇注释|迥汇注释)[\s\S]*$",
            "",
            s,
        )
        # If © or ® still remains, cut leaked Roman-numeral / English passage tail after Chinese prose
        if "©" in s or "®" in s:
            s = re.sub(
                r"(?<=[\u4e00-\u9fff。；！）\]］”\"'a-zA-Z0-9])\s*(?:\.?[IVX]{1,4}|DI|JI|Il|IH|ID|K|H|VJ)?\s*(?:O|©)?\s*[A-Z][A-Za-z0-9\s,'\"\-\(\)\.:;©®]+(?:©|®)[\s\S]*$",
                "",
                s,
            )
            # Clean any residual standalone ©/® if still embedded in short citation
            s = s.replace("©", "").replace("®", "")

    # 1. Remove trailing `知识补充` / `外教朗读` / `TextN ... 原文外教朗读` / Q7 leaked Q8-Q11 tail
    s = re.sub(
        r"\n*\s*(?:Text\s*\d+[^\n]*\n(?:\s*口\s*\n)?)?(?:知识补充|原文外教朗读)[\s\S]*$",
        "",
        s,
    )
    s = re.sub(r"\n&\s*\n［A］\s*present提交，提出[\s\S]*$", "", s)

    # 2. Remove OCR scan tags/headers (`真题精解`, `真题精惮`, `语篇分析`, `续表`, `口口`)
    s = re.sub(r"(?m)^\s*[「f卜;:\-•\s]*·?真题精[解惮]·?[^\n]*$\n?", "", s)
    s = re.sub(r"[「f卜;:\-•]*·?真题精[解惮]·?[^\n]*", "", s)
    s = re.sub(r"[「\[［;•·・]+\s*语篇分析[^\u4e00-\u9fffa-zA-Z0-9\n]*[掺必也]?", "", s)
    s = re.sub(r"[\[［]\s*•?\s*语篇分析(?:\s*•?\s*[\]］]\s*〕?必?)?", "", s)
    s = re.sub(r"[•·・]\s*语篇分析(?=(?:[一二三四五六七八九十第]|$))", "", s)
    s = re.sub(r"(?m)^\s*续表\s*$\n?", "", s)
    s = re.sub(r"(?m)^\s*口+\s*$\n?", "", s)

    # 3. Remove isolated OCR symbols (`§` column divider, `❶–❿` leaked markers)
    s = re.sub(r"\s*§\s*", " ", s)
    s = re.sub(
        rf"(?<=[a-zA-Z0-9.,;:!?])\s*[{CIRCLED_OCR_NUMS}]\s*(?=[A-Za-z])",
        " ",
        s,
    )
    s = re.sub(rf"[{CIRCLED_OCR_NUMS}]\s*", "", s)
    # Restore space after sentence-ending period if `❶–❿` removal glued `word.Next`
    s = re.sub(r"([a-z0-9]{2,}\.)([A-Z][a-z]+)", r"\1 \2", s)

    # 4. Fix `十` -> `+` in exam-point headers (e.g. `语义十形容词` -> `语义+形容词`)
    s = re.sub(
        r"(语义|逻辑|搭配|语法|词汇|词义|语境|词性|句意|结构)十(?=[\u4e00-\u9fff])",
        r"\1+",
        s,
    )

    # 5. Fix known OCR typos, broken option labels, `**` quotes, and 2005-2007 spaced English
    for bad, good in TYPO_REPLACEMENTS:
        s = s.replace(bad, good)

    # Fix broken option labels (halfwidth and fullwidth brackets): `[ AJ`, `［B J`, `［DJ`, `EA]`, `EC]`, `ED]`, `:C]`, `[ A]`, `[ A ］`
    s = re.sub(r"[\[［]\s*([A-D])\s*J(?=[a-z])", r"[\1] ", s)
    s = re.sub(r"[\[［]\s*([A-D])\s*J", r"[\1]", s)
    s = re.sub(r"(?<![A-Za-z])E([A-D])[\]］]", r"[\1]", s)
    s = re.sub(r"(?<![A-Za-z0-9]):([A-D])[\]］]", r"[\1]", s)
    s = re.sub(r"[\[［]\s+([A-D])\s*[\]］]", r"[\1]", s)
    s = re.sub(r"[\[［]\s*([A-D])\s+[\]］]", r"[\1]", s)

    # Fix OCR `**` left-quote errors (`platforms**社交媒体平台''` -> `platforms“社交媒体平台”`)
    s = re.sub(r"\*\*([^*\n”\"']{1,50})''", r"“\1”", s)
    s = re.sub(r"\*\*([^*\n”\"]{1,50})\"", r"“\1”", s)
    if "**" in s:
        s = s.replace("**", "“")

    if category_id == "ky1" and year in (2005, 2006, 2007):
        s = clean_spaced_english_runs(s)

    # 6. Merge hard PDF two-column line breaks inside Chinese paragraphs
    raw_lines = [ln.strip() for ln in s.split("\n")]
    merged_lines: List[str] = []
    for ln in raw_lines:
        if not ln:
            if merged_lines and merged_lines[-1] != "":
                merged_lines.append("")
            continue
        if not merged_lines or merged_lines[-1] == "":
            merged_lines.append(ln)
            continue
        prev = merged_lines[-1]
        if should_keep_line_break(prev, ln):
            merged_lines.append(ln)
        else:
            merged_lines[-1] = join_wrapped_lines(prev, ln)

    s = "\n".join(merged_lines).strip()

    # 7. Strip isolated trailing OCR noise (`回`, `•`, `/`, `:-`) at the very end
    s = re.sub(r"(?:\n|\s)*回?\s*(?:\n|\s)*(?:•|/|:-)+\s*$", "", s).strip()

    # Normalize excessive blank lines
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    return s


def load_env() -> Dict[str, str]:
    env = dict(os.environ)
    for fname in (".env.local", ".env"):
        fpath = os.path.join(REPO_ROOT, fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8", errors="ignore") as fp:
            for raw in fp:
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip()
                if (v.startswith('"') and v.endswith('"')) or (
                    v.startswith("'") and v.endswith("'")
                ):
                    v = v[1:-1]
                if not env.get(k):
                    env[k] = v
    return env


def choose_dollar_tag(text: str) -> str:
    tag = "$expl_fix$"
    idx = 0
    while tag in text:
        idx += 1
        tag = f"$expl_fix_{idx}$"
    return tag


def export_idempotent_sql(updates: List[Tuple[str, str]]) -> None:
    os.makedirs(os.path.dirname(SQL_OUT_PATH), exist_ok=True)
    with open(SQL_OUT_PATH, "w", encoding="utf-8", newline="\n") as fp:
        fp.write("-- ============================================================================\n")
        fp.write("-- Idempotent Explanation Cleanup & P0/P1 Remediation across 41 Exams\n")
        fp.write(f"-- Total updated questions: {len(updates)}\n")
        fp.write("-- Generated by: scripts/clean_explanations.py\n")
        fp.write("-- ============================================================================\n\n")
        fp.write("BEGIN;\n\n")
        for qid, new_expl in updates:
            tag = choose_dollar_tag(new_expl)
            fp.write(
                f"UPDATE public.questions\n"
                f"SET explanation = {tag}{new_expl}{tag}\n"
                f"WHERE id = '{qid}'\n"
                f"  AND explanation IS DISTINCT FROM {tag}{new_expl}{tag};\n\n"
            )
        fp.write("COMMIT;\n")


def apply_updates_to_supabase(updates: List[Tuple[str, str]]) -> None:
    env = load_env()
    supabase_url = (
        env.get("SUPABASE_URL")
        or env.get("NEXT_PUBLIC_SUPABASE_URL")
        or "https://pghybspsjtzihpzpahcf.supabase.co"
    ).rstrip("/")
    service_key = env.get("SUPABASE_SERVICE_ROLE_KEY")
    if not service_key:
        raise RuntimeError("Missing SUPABASE_SERVICE_ROLE_KEY in environment / .env.local")

    total = len(updates)
    print(f"Applying {total} explanation updates to Supabase ({supabase_url})...")
    for idx, (qid, new_expl) in enumerate(updates, 1):
        url = f"{supabase_url}/rest/v1/questions?id=eq.{qid}"
        payload = json.dumps({"explanation": new_expl}, ensure_ascii=False).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=payload,
            method="PATCH",
            headers={
                "apikey": service_key,
                "Authorization": f"Bearer {service_key}",
                "Content-Type": "application/json",
                "Prefer": "return=minimal",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                if resp.status not in (200, 204):
                    raise RuntimeError(f"Unexpected HTTP {resp.status} for {qid}")
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"HTTP {e.code} updating {qid}: {body}") from e
        if idx % 100 == 0 or idx == total:
            print(f"  Synced {idx}/{total} questions...")


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean exam question explanations")
    parser.add_argument(
        "--apply-db",
        action="store_true",
        help="Push updated explanations directly to Supabase public.questions",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Inspect stats without modifying files or DB",
    )
    args = parser.parse_args()

    json_files = sorted(f for f in os.listdir(EXAMS_DIR) if f.endswith(".json"))
    updates: List[Tuple[str, str]] = []
    touched_files = 0
    p0_count = 0
    p1_count = 0
    batch_count = 0

    for fname in json_files:
        fpath = os.path.join(EXAMS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as fp:
            data = json.load(fp)

        file_changed = False
        cat = data.get("exam", {}).get("category_id", "")
        yr = int(data.get("exam", {}).get("year") or 0)
        for q in data.get("questions", []):
            qid = q["id"]
            old_expl = q.get("explanation") or ""

            if qid in P0_EXPLANATIONS:
                new_expl = P0_EXPLANATIONS[qid].strip()
                if new_expl != old_expl:
                    p0_count += 1
            elif qid in P1_EXPLANATIONS:
                new_expl = P1_EXPLANATIONS[qid].strip()
                if new_expl != old_expl:
                    p1_count += 1
            else:
                new_expl = clean_explanation_text(old_expl, cat, yr)
                if new_expl != old_expl:
                    batch_count += 1

            if new_expl != old_expl:
                updates.append((qid, new_expl))
                q["explanation"] = new_expl
                file_changed = True

        if file_changed:
            touched_files += 1
            if not args.dry_run:
                with open(fpath, "w", encoding="utf-8", newline="\n") as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=2)
                    fp.write("\n")

    print(
        f"Summary: {len(updates)} questions updated across {touched_files}/{len(json_files)} files "
        f"(P0={p0_count}, P1={p1_count}, BatchOCR={batch_count})"
    )

    if not args.dry_run:
        export_idempotent_sql(updates)
        print(f"Exported idempotent SQL migration: {os.path.relpath(SQL_OUT_PATH, REPO_ROOT)}")
        if args.apply_db and updates:
            apply_updates_to_supabase(updates)
            print("Supabase cloud DB update completed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
