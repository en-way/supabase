#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calibrate_round35.py
Round 35 法医级文本校对与纯净化：
1. 2004 ky1 Text 3 (Q31-Q35):
   - Q35: 切除堆叠双语题干/选项，清除末尾残留的模拟题乱码与答案（全库彻底清除"参考答案"）；
   - Q31-Q34: 切除堆叠双语题干/选项，规范化解析结构与符号；
2. 2021 ky2 Text 1 (Q21, Q23, Q24, Q25):
   - Q21: 规范题干下划线，切除堆叠双语题干/选项，切除末尾 OCR 倒灌残片 \nU ❶；
   - Q23: 规范题干下划线，切除堆叠双语题干/选项，切除末尾 OCR 倒灌残片 \n皿❶；
   - Q24: 规范题干下划线，补齐黄皮书官方完整［精准定位］，切除堆叠双语题干/选项；
   - Q25: 规范题干下划线，补齐黄皮书官方完整［精准定位］，切除堆叠双语题干/选项；
3. 清理 9 处正文截断倒灌与尾部残片：
   - 2014 ky1 Q28: 切除末尾 \nV ❶画 The ot，纠正 BP可快速 为 即可快速；
   - 2001 ky1 Q34: 切除末尾 \nIV ❶ Examples of benef；
   - 2018 ky1 Q29: 切除末尾 \nVI ❶ So when young people；
   - 2017 ky1 Q23: 切除末尾 \nVI ❶It has not gotten anywhere close to that...；
   - 2010 ky1 Q28: 切除末尾 \n\nIV ❶ The Bilski case involves...；
   - 2020 ky1 Q24: 切除末尾 \nIV ❶ A u town of culture could be...；
   - 2013 ky1 Q38: 切除末尾 \nVI ❶The 8-0 objection to President Obama...；
   - 2013 ky1 Q39: 切除末尾 \nVII ❶ Some powers do belong exclusively®...；
   - 2022 ky1 Q45: 切除末尾 \n\n奢三、语篇分析 及 41 题正文倒灌。
"""

import json
import glob
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 定义 18 道试题的校对更新字典
UPDATES = {
    # 1. 2004 ky1 Text 3 Q31
    '8ae79ee8-871c-587d-bf94-ef6d7093c69e': {
        'explanation': (
            "【精准定位】\n"
            "该句子的下文，即从②句 but 开始论述的都是经济衰退对美甲师斯佩罗的影响，如：“她修剪、锉磨、上油的指甲没有自己希望的那样多了”；“老顾客突然不光顾了”；“自己也在削减开支”等。But 表明上文和下文之间存在转折关系，下文均为负面信息，由此可推出，上文（即所考查句）应该为正面信息，选项[D]符合此逻辑。\n\n"
            "【命题解密】\n"
            "本题考查考生通过上下文猜测 bite one's nails 的正确含义。作者借用 not bite one's nails 这个形象的比喻来说明斯佩罗并非“处于非常糟糕的情况中”，正确项[D]是所考查的句子在文中的特定意义。\n"
            "[A]与[B]根据下文细节设置干扰，不符合首句与下文之间的转折关系：[A]与 but 后面表述的内容一样都是负面的，不能构成转折关系；[B]与文章首句前半部分 when it comes to the slowing economy 放在一起，语义上说不通。[C]望文生义，拘泥于 bite her nails 的字面意思，将其理解为“咬指甲”这种坏习惯，显然与上下文语意不连贯。"
        )
    },
    # 2. 2004 ky1 Text 3 Q32
    '5a36d105-1b62-5efc-84d4-61de64148997': {
        'explanation': (
            "【精准定位】\n"
            "第二段前四句先列举了经济减速的表现，⑤句谈及公众的反应：消费者似乎只是一些担心（only mildly concerned），没有恐慌（not panicked）。即使稍微缩减开支的时候，他们对经济的前景也仍是乐观的（optimistic）。因此[A]符合文意。\n\n"
            "【命题解密】\n"
            "第二段论述了消费者对经济滑坡的态度。本题主要考查学生对他们态度的正确把握。正确项[A]是公众态度的正确反映，第二段末句出现了 optimistic 一词，第三、四段首句（not in despair 和 see silver linings）也都暗示了公众的乐观态度。\n"
            "[B]无中生有，无法推断。[C]夸大其辞，从 mildly concerned 和 do some modest belt-tightening，可以看出公众对于目前状况的态度并不是无忧无虑的。[D]反向干扰，文中为 not panicked。"
        )
    },
    # 3. 2004 ky1 Text 3 Q33
    'acc5f066-e32d-5469-8363-d8bcbe42ae02': {
        'explanation': (
            "【精准定位】\n"
            "直接定位至第三段②句，该句引用股票经纪人原话对曼哈顿房地产市场状况进行评价。其上句①句是观点句：大部分地区房价（home prices）保持稳定，②至⑥句是例证和引证，支撑①句的观点，都是围绕房地产价格展开的论述。而且②、⑥句中 real-estate broker（房地产经纪人）明确指出论述内容，答案应为[B]。\n\n"
            "【命题解密】\n"
            "本题考查学生通过上下文获取信息的能力，另一方面也考查了考生对 real estate 的理解能力。正确项[B]是对所述话题的正确理解。②句论述了曼哈顿房地产市场的火热，其中 a new gold rush 是比喻义，喻指“房地产投资热”；the $4 million to $10 million range 指“房价的范围”，predominantly fueled by... 指“房地产投资的资金来源”。\n"
            "[A]对句中 gold 望文生义。[C]根据②句中 Wall Street bonuses 设置干扰，但它指的是房产投资的资金来源。[D]无中生有。"
        )
    },
    # 4. 2004 ky1 Text 3 Q34
    '6841be11-2586-504d-b1ac-eeb8462504cd': {
        'explanation': (
            "【精准定位】\n"
            "根据题干定位到最后一段首句。下文罗列了多个事例对其加以说明：买房人会因低利率而欢呼；雇主不介意人才市场少些泡沫；投资者把股市波动看作繁荣必不可少的一部分；就餐者也可以光顾以前根本订不到位子的餐厅。从这些事实中我们可以推出，“银色的衬里”指他们得到的好处，因此，正确答案为[A]。其他项均不能概括这些例子的共同特点。\n\n"
            "【命题解密】\n"
            "本题一箭双雕，一方面考查 silver linings 的语意理解，一方面考查例证的作用。正确项[A] benefit 源于对 silver linings 的演绎。silver linings 来自谚语 Every cloud has a silver lining，意思是“黑暗中总有一线光明”或“在逆境中总有值得宽慰的或有希望的一面”。文中借用 silver linings 来表示“人们在经济滑坡中依然看到希望”。\n"
            "[B]偷梁换柱，将③句 stock-market swings 改为 signs of recovery；[C]与[D]无中生有。"
        )
    },
    # 5. 2004 ky1 Text 3 Q35
    'b0053232-03f5-5c69-b119-72064e26eba0': {
        'stem': 'To which of the following is the author likely to agree?',
        'explanation': (
            "【精准定位】\n"
            "这篇文章主要涉及美国经济，开篇以一个事例引出话题：美国经济滑坡。紧接着第二段谈到，人们已经感觉到了经济在滑坡，但消费者只是有一些担心而没有恐慌。第三、四段分析消费者没有处于绝望境地的原因。综合全文，[C]最能反映出作者对当前经济形势的态度。\n\n"
            "【命题解密】\n"
            "本题实际考查考生对文章主旨的理解能力。正确项[C]中 Caution all right 对应第二段②句 cautious，panic not 则对应第二段②句 not panicked，第二段⑥句 But don't sound any alarms just yet 最能反映作者对经济滑坡的态度：还没有糟糕到拉响警钟的时刻。\n"
            "[A]和[B]夸大其辞；[A]过于乐观，[B]过于悲观；[D]无中生有，“投资或机会”不是文中重点论述的内容。"
        )
    },

    # 6. 2021 ky2 Text 1 Q21
    '9de58b50-9efc-5fc5-aeaf-cc2db9a08723': {
        'stem': 'Research by the World Economic Forum suggests ________.',
        'explanation': (
            "［精准定位］根据题干关键词Research by the World Economic Forum定位至首段③句，该句介绍世界经济论坛的研究发现：到2022年，各类职业中平均42%的“核心技能”将发生变化。这一研究发现支撑了②句“工作岗位的技能需求将迅速发生变化”这一时代趋势。结合末句“到2022年是非常短的时间”可知，未来的工作岗位迫切需要新的工作技能，［B］正确。\n"
            "［命题解密］正确项［B］中 demand for new job skills 是对③句 \"core skills\" within job roles will change 和②句 the jobs in demand will change rapidly 的同义转述，urgent 对应末句 a very short timeline。\n"
            "［A］利用首段①句a lot of would-be workers设置干扰，将我们对未来的期望“潜在劳动力不被大量抛弃”误解为“全职就业岗位将增多”，但原文并未涉及“全职工作”这一话题。［C］利用②句the jobs in demand will change rapidly设置干扰，但文中the jobs in demand实指“社会所需的工作（技能）”而非“社会提供的工作机会”，且“迅速变化”不意味着“稳步增长”。［D］由③句“平均42%的核心技能将发生变化”主观臆断出“核心技能存在争议”，但文中并未提及人们对核心技能的不同看法。\n"
            "［技巧总结］本题为事实细节题，解题关键在于准确锁定关键词。如本题，根据题干可定位至首段③句，其内容是“到2022年，各类职业中42%的核心技能将发生变化”，关键词是core skills和change。“工作的核心技能发生变化”也即“需要新的工作技能”，浏览四个选项可轻松锁定［B］。而并未涉及“工作技能”，［D］虽触及“工作（核心）技能”，但“争议”在文中并未提及。"
        )
    },
    # 7. 2021 ky2 Text 1 Q23
    'fe5b4695-503e-53e2-8a56-dd3de111dc1e': {
        'stem': 'Efforts to resolve the skills mismatch in Canada ________.',
        'explanation': (
            "［精准定位］第二段末句指出，加拿大及其他地方所作的努力充其量只能说是迟缓无力的，这导致即便在高失业率的时期和地区，雇主也常急缺雇员。可见，加拿大为解决技能不匹配问题所作的努力仍然不够，［D］正确。\n"
            "［命题解密］正确项［D］是对第二段末句 Efforts in Canada and elsewhere have been arguably languid at best的同义改写。languid 一词虽超纲，但结合上下文可知，“失业率高的时候雇主还是急缺雇员”实际描述的是上句“技能不匹配（skills mismatch）”的现象，即低技能员工大量失业、高技能员工极其紧缺。上句还提及“人们希望政府来解决这一问题（government to handle）”，但加拿大政府付出了努力却没有解决问题，可见其努力“仍然不够”。\n"
            "［A］根据加拿大努力不够导致的局面“雇主急缺雇员”主观臆断出“劳动力成本上升”，文中并未明确提出劳工成本问题。［B］将“即便是在高失业率时期，雇主也常常急缺雇员”这一矛盾局面（即加拿大努力不够导致的结果），偷换成“加拿大所作的努力本身是自相矛盾的”。［C］由文意“人们希望政府来解决，但政府所作努力不够有力”主观臆测出“加拿大所作的努力遭到了强烈的反对”，而文中并未提及公众的不满。\n"
            "［技巧总结］本题定位比较容易，但难点在于定位处关键信息languid 一词可能陌生。解题时可先看选项，［A］、［C］指向努力导致的“结果”，［B］、［D］指向对努力本身的“评价”。简单分类后，再看定位句 have given us a situation where...对应“结果”，have been arguably languid at best 对应“评价”。最后将各项与原文比对，比对信息时切忌主观臆断（如［A］、［C］项）以及偷换逻辑（如［B］项）。"
        )
    },
    # 8. 2021 ky2 Text 1 Q24
    '0f9fe0e4-019a-52f1-a9ee-0819ad6b68ac': {
        'stem': 'We can learn from Paragraph 3 that there was ________.',
        'explanation': (
            "［精准定位］第三段①句指出，疫情期间失业率居高不下。随后，②③句以具体数据说明疫情导致失业率大幅走高（潜在逻辑：疫情加剧—用人单位用工需求下降—失业率大幅走高），然后转折指出员工短缺的问题依然存在。④句进而以医疗领域员工短缺的现象为例予以佐证。由此可见，［C］正确。\n"
            "［命题解密］题干 +正确项［C］是对第三段④句 there were still clear shortages of doctors, nurses and other medical personnel 的同义改写。\n"
            "［A］根据该段所述客观现象“失业率走高、医护人员短缺”主观臆断出“人民不满政府的作为，呼吁调整政策”，但文中并未提及人们对政府政策的诉求。［B］将②③句“二月（疫情初期）员工短缺问题普遍存在—五月（疫情高峰期）员工短缺问题大多不复存在”所体现的“用工需求发生变化”窜改为“用工制度/雇佣惯例发生变化”。［D］与②③句所述现象“失业率由低到高、经济走向低迷”相悖。\n"
            "［技巧总结］让步转折处常常引出信息重点，也是命题人的关注点。本题对应的第三段中③句后半句although many. . . not all...形成让步转折，并将语义重点落在“员工短缺问题依然存在（not all had done so）”上；随后④句以“医务人员短缺”进行例证。掌握信息关键点后，很容易就能锁定正确项［C］。"
        )
    },
    # 9. 2021 ky2 Text 1 Q25
    '7334576a-351e-52fc-a957-43cb124b5e57': {
        'stem': 'Scandinavian Airlines decided to ________.',
        'explanation': (
            "［精准定位］由题干关键词Scandinavian Airlines快速定位至末段③句。该句指出，北欧航空公司决定重新培训其下岗员工，以期让他们支援医护人员。［B］与此意相符。\n"
            "［命题解密］正确项［B］中prepare. . . for...（给某人进行预备教育或训练）对应末段③句 retraining/reskilled, other jobs 即指末段③句 to support hospital staff。\n"
            "［A］将北欧航空公司的方案“培训内部失业人员支援外部紧缺人员”曲解为“在公司内部为失业人员创造更多空缺职位”。［C］窜改原文信息：首先将培训对象“下岗空乘人员”扩大为“（所有）空乘人员”，其次将培训目的“支援医护人员”窜改为“提升航空服务”。［D］利用末段末句a Swedish university设置干扰，原文实指“一所瑞典大学也参与了北欧航空公司的下岗员工再培训方案”，而非“北欧航空公司决定资助所有员工接受大学教育”。\n"
            "［技巧总结］本题容易定位且定位内容只有一句，除了常规的“将原文定位内容与选项一一对比”这种解题方法，还可以从选项出发。首先纵观各项涉及的对象：［A］ the unemployed泛指“所有失业人员”，［B］ their laid-off workers 特指“该公司下岗员工”，［C］ their cabin staff 和［D］ their staff 指向“该公司所有（空乘）员工”。而定位句 forced to furlough. . . their cabin staff、the laid-off workers 针对的是“该公司下岗（空乘）员工”，与此相符的只有［B］项。然后将该项进一步与定位句对比，发现prepare. . . for other jobs 对应原文 reskilled. . . to support hospital staff，从而敲定［B］为正确项。"
        )
    },

    # 10. 2014 ky1 Q28
    'a87b5c5d-02e7-5888-bca4-8eb41694dc29': {
        'clean_tail_regex': r'(\n?V\s*❶画\s*The\s*ot.*)$',
        'replace_text': ('BP可快速找寻到正确答案。', '即可快速找寻到正确答案。')
    },
    # 11. 2001 ky1 Q34
    'f7fe5edd-8e01-578b-8ca0-31da1a49b77f': {
        'clean_tail_regex': r'(\n?IV\s*❶\s*Examples\s*of\s*benef.*)$'
    },
    # 12. 2018 ky1 Q29
    'e1dcfb71-970b-5ceb-b499-d65e4f6f4231': {
        'clean_tail_regex': r'(\n?VI\s*❶\s*So\s*when\s*young\s*people.*)$'
    },
    # 13. 2017 ky1 Q23
    '3f6ff517-1825-52c3-812e-d1404a09dcfd': {
        'clean_tail_regex': r'(\n?VI\s*❶\s*It\s*has\s*not\s*gotten.*)$'
    },
    # 14. 2010 ky1 Q28
    '61936c47-02aa-5ed2-be24-6eef11c0ecd4': {
        'clean_tail_regex': r'(\n+IV\s*❶\s*The\s*Bilski\s*case.*)$'
    },
    # 15. 2020 ky1 Q24
    '3fc7536b-21dd-5e4e-8645-9f1f0ab59d14': {
        'clean_tail_regex': r'(\n?IV\s*❶\s*A\s*u\s*town\s*of\s*culture.*)$'
    },
    # 16. 2013 ky1 Q38
    'e439d071-3be0-5cab-994f-952a8976c042': {
        'clean_tail_regex': r'(\n?VI\s*❶\s*The\s*8-0\s*objection.*)$'
    },
    # 17. 2013 ky1 Q39
    '815dc9d8-0b8c-5c08-b7ff-8c0fed082bad': {
        'clean_tail_regex': r'(\n?VII\s*❶\s*Some\s*powers\s*do\s*belong.*)$'
    },
    # 18. 2022 ky1 Q45
    '70efe185-a6ea-5e0a-9eec-72e4c109d093': {
        'clean_tail_regex': r'(\n\s*奢三、语篇分析.*)$'
    }
}

def calibrate():
    exams = sorted(glob.glob('public/data/exams/*.json'))
    modified_files = set()
    calibrated_counts = 0

    import re

    for fpath in exams:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        file_changed = False
        for q in data.get('questions', []):
            qid = q.get('id')
            if qid in UPDATES:
                upd = UPDATES[qid]
                # Direct override of stem
                if 'stem' in upd:
                    q['stem'] = upd['stem']
                    file_changed = True
                # Direct override of explanation
                if 'explanation' in upd:
                    q['explanation'] = upd['explanation']
                    file_changed = True
                    calibrated_counts += 1
                    print(f"Updated full explanation for {qid}")
                # Tail cleanup
                if 'clean_tail_regex' in upd:
                    orig_expl = q.get('explanation', '')
                    cleaned_expl = re.sub(upd['clean_tail_regex'], '', orig_expl, flags=re.DOTALL).rstrip()
                    if 'replace_text' in upd:
                        old_s, new_s = upd['replace_text']
                        cleaned_expl = cleaned_expl.replace(old_s, new_s)
                    if cleaned_expl != orig_expl:
                        q['explanation'] = cleaned_expl
                        file_changed = True
                        calibrated_counts += 1
                        print(f"Cleaned leakage tail for {qid}: len {len(orig_expl)} -> {len(cleaned_expl)}")

        if file_changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            modified_files.add(fpath)

    print(f"\nCalibration complete! Modified {len(modified_files)} exam files, calibrated {calibrated_counts} questions.")

if __name__ == '__main__':
    calibrate()
