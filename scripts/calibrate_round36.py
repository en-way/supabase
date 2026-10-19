#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calibrate_round36.py
Round 36 法医级文本校对与纯净化：
1. 完型填空 6 题段落正文及句式倒灌切除与官方题解提纯：
   - 2014 ky1 Q14 (dd0833e2-bb69-54d6-b435-80fbb9b447f3)
   - 2013 ky1 Q7 (7f812c56-89b5-5b69-b7d7-37d99c282e63)
   - 2015 ky1 Q2 (29fac009-87d6-5c7e-89b0-fa0f193e34ea)
   - 2012 ky1 Q9 (ca9df23f-59cf-5738-b7b7-bfe73b44b986)
   - 2012 ky1 Q14 (19ac0af4-ab1b-589c-b036-683542855e9d)
   - 2012 ky1 Q17 (2d6dbe40-7478-5906-a339-64f68063de87)
2. 2021 ky2 Text 2 (Q26-Q30) 全组 5 题官方黄金校准：
   - Q26 (0715c893-3ad4-5307-9cb0-795e2d8879a1): 补全题干下划线，切除双语堆叠题干/选项，以［精准定位］开头；
   - Q27 (3b20caf0-2eba-5411-a80c-719671620399): 补全题干下划线，切除双语堆叠题干/选项，以［精准定位］开头；
   - Q28 (e95671c2-be38-5b29-ab31-4b2c046ea997): 补全题干下划线，切除双语堆叠题干/选项，补齐被截断的技巧总结，切除混入的第6段正文；
   - Q29 (45172221-b859-553c-af50-68353e84f4af): 补全题干下划线，切除双语堆叠题干/选项，补齐被截断的技巧总结；
   - Q30 (bc3a6553-5c28-5abb-9a82-0ec7a0ea2615): 纠正 author^s 为 author's，补全题干下划线，切除双语堆叠，补齐技巧总结，切除末尾倒灌的 Text 3 标题。
"""

import json
import glob
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

UPDATES_R36 = {
    # 1. 2014 ky1 Q14
    'dd0833e2-bb69-54d6-b435-80fbb9b447f3': {
        'clean_tail_regex': r'(\nIV\s*❶\s*The\s*Web-based\s*program.*)$'
    },
    # 2. 2013 ky1 Q7
    '7f812c56-89b5-5b69-b7d7-37d99c282e63': {
        'explanation': (
            "7. ［A］ if如果 ［B］ until直到... 为止 ［C］ though虽然，尽管 ［D］ unless除非，如果不\n"
            "［考点提炼］句内语义逻辑+虚拟语气。正确率：20%\n"
            "［解题思路］从语义角度看，空格前“法官因害怕表现得对犯罪宽容，更可能对下一位被告加重处罚”是结果，空格后“法官已经对五六名其他被告轻判”是前提条件，故空格处应引导条件逻辑；从语法角度看，根据关键词theorised（理论情况，是一种假设）以及句中时态（might be. .. had sentenced）可判断本句为虚拟语气，选项中既能引出条件，又可用于虚拟语气的只有［A］。\n"
            "［错项排除］［B］表时间，但“将某人送入监狱直到他对五六位其他被告予以轻判”与文意不符；［C］可表让步，还可表轻微转折，用于主句后，引出补充说明，使语气变弱，但语义重点仍在主句，此处空格上下文为顺承逻辑，不存在让步或转折逻辑；［D］虽表条件，但用于否定句或虚拟句时语义与 if not 相当，置入文中表示“除非他此前对五六名其他被告轻判，否则法官才会对下一名被告重判”，语义相反。"
        )
    },
    # 3. 2015 ky1 Q2
    '29fac009-87d6-5c7e-89b0-fa0f193e34ea': {
        'clean_tail_regex': r'(\n[：\s]*iiMi注释.*)$'
    },
    # 4. 2012 ky1 Q9
    'ca9df23f-59cf-5738-b7b7-bfe73b44b986': {
        'clean_tail_regex': r'(\s*IV\n*IV\s*❶\s*The\s*framers.*)$'
    },
    # 5. 2012 ky1 Q14
    '19ac0af4-ab1b-589c-b036-683542855e9d': {
        'clean_tail_regex': r'(\nV\s*❶\s*Constitutional\s*law\s*is\s*political.*)$'
    },
    # 6. 2012 ky1 Q17
    '2d6dbe40-7478-5906-a339-64f68063de87': {
        'clean_tail_regex': r'(\nVI\s*❶\s*The\s*justices\s*must.*)$'
    },

    # 7. 2021 ky2 Text 2 Q26
    '0715c893-3ad4-5307-9cb0-795e2d8879a1': {
        'stem': 'Some people argue that food self-sufficiency in the UK would ________.',
        'explanation': (
            "［精准定位］根据题干关键词food self-sufficiency in the UK定位至第二段，该段①句指出，脱欧促使一些人提出“英国粮食自给自足”的美好设想；②句进而在破折号后补充其设想的内容：通过增加本国粮食产量，英国可以实现自给自足；③句紧接着解释自给自足的好处：不仅能减少对外国粮食的依赖，还能促进本国农业发展。［B］与②③句文意相符。\n"
            "［命题解密］正确项［B］中 reduce its agricultural imports 对应③句 reduce our dependence on foreign food。\n"
            "［A］根据第一段②句由于人口增长带来的粮食需求，主观臆断出“英国粮食自给自足将被人口增长所阻碍”，但由第二段②句可知，作者提出“英国粮食自给自足”正是为了应对人口增长的挑战。［C］利用第二段③句 boost the farming industry 故意反向干扰，窜改为“对农业构成挑战”。［D］曲解文意，文中并未提及饮食传统的改变。"
        )
    },
    # 8. 2021 ky2 Text 2 Q27
    '3b20caf0-2eba-5411-a80c-719671620399': {
        'stem': 'The report by the University of Leeds shows that in the UK ________.',
        'explanation': (
            "［精准定位］根据题干关键词The report by the University of Leeds定位到第三段①句：英国利兹大学发表了一份关于“英国粮食生产”的报告，该报告指出英国土地总面积的85%与肉类及奶制品的生产相关联，［C］正确。\n"
            "［命题解密］“题干 + ［C］”是对第三段①句的概括，其中 most land is used for meat and dairy production 对应 85 per cent of the country's total land area is associated with meat and dairy production。\n"
            "［A］、［B］、［D］的干扰均源于第四段②句，分别来自句中 farm more intensively、more factory-style production 以及 fewer green fields。但该句并非陈述报告展示的实际情形，而是作者基于报告数据，就“英国提高自给率”做出的设想（若要大幅提高自给率，英国将需要……），均不合题干要求。更何况［A］推导错误：由“农业需要更集约化”错误推导出“目前农田的利用效率低下”；［B］曲解信息：将“工厂式生产需要增加”理解为“工厂式生产需要改革”。\n"
            "［技巧总结］本题就“报告内容”命制事实细节题，解答关键在于精准定位，辨别“报告内容”与“作者基于报告所做设想”：第四段②句中 To become much more self-sufficient, the UK would need to 表明这里已经超越报告内容，作者开始就“英国如何才可能提升自给率”进行设想，因此不管是曲解作者设想的还是符合其内容的［D］，都需排除。合理概括第三段①句报告内容陈述（According to a report...）的［C］才是正确项。"
        )
    },
    # 9. 2021 ky2 Text 2 Q28
    'e95671c2-be38-5b29-ab31-4b2c046ea997': {
        'stem': 'Crop-growing in the UK is restricted due to ________.',
        'explanation': (
            "［精准定位］第五段首句指出转向以植物为主的饮食也不会有太大意义，随后各句具体解释原因。其中②句指出英国大部分地带都不具备适宜商业化种植的土壤和气候，可知限制作物种植的因素是自然条件，［C］正确。\n"
            "［命题解密］［C］中 natural conditions 是对原文 the right soil or climate 的正确概括。\n"
            "［A］由第四段②句 more factory-style production 臆断而来，但“工厂式生产增加”是集约农业的特点，并不等同于耕作技术的高低，更非作物种植受限的原因。［B］颠倒因果，将第五段②句“作物种植受限，所以农业以畜牧业为主（饮食以动物性食品为主）”颠倒为“饮食传统限制了作物种植”。［D］利用 on a commercial basis 捏造干扰，将文中“受自然条件限制，英国大部分地带不适合商业化/大规模种植”曲解为“商业利益限制了作物种植”。\n"
            "［技巧总结］本题考查英国作物种植受限的原因，解题关键在于锁定因果关系，并准确概括原因，警惕颠倒因果、强加关联的选项。第五段②句 There is a good reason why 及随后的冒号提示该处存在因果逻辑，梳理可知关系为“土壤、气候等自然条件不适宜→作物种植受限→畜牧业占大头”，故［C］正确。［A］、［D］均以碎片信息捏造干扰，［B］则颠倒因果。"
        )
    },
    # 10. 2021 ky2 Text 2 Q29
    '45172221-b859-553c-af50-68353e84f4af': {
        'stem': 'It can be learned from the last paragraph that British people ________.',
        'explanation': (
            "［精准定位］末段①句指出“如今英国人食用的果蔬中仅有23%产自本国”，可知其余77%/大部分都依靠进口，［A］正确。\n"
            "［命题解密］［A］中 rely largely on imports 是对①句 Just 23 per cent... are currently home-grown 的正确计算和合理推断。\n"
            "［B］错误理解段中23%和30%两个数据的含义，这里是在指出“产自本国的果蔬占果蔬总食用量的23%，采用最极端手段可以达到30%”，并非“果蔬食用量上升”。［C］和［D］分别将②句“英国人若采用极端手段尽力满足果蔬需求，则需要另找地方种植提供大部分卡路里摄入的谷物等（look for... the grains, sugars, seeds... the vast bulk of our current calorie intake）”曲解为“英国人正寻求减少卡路里摄入”和“英国人正努力培育新的谷物类型”。\n"
            "［技巧总结］题目就末段考查事实细节，需要将各项核心关键词回文比对，进行合理引申推断，关键在于理清数据关系（①句23%, 30%），辨别信息虚实（②句是在以假定情形说明采用极端手段种植果蔬不可行）：分别利用选项关键名词［A］ fresh produce, ［B］ fruit consumption, ［C］ calorie intake, ［D］ grains 定位原文，然后进行比对，发现［B］、［C］、［D］其余部分 enjoy a steady rise、are seeking effective ways to cut、are trying to grow new varieties 歪曲了文中信息，可排除；而［A］ rely largely on imports 是对 Just 23 per cent of the fruit and vegetables... are currently home-grown 的正确推算，故为正确项。"
        )
    },
    # 11. 2021 ky2 Text 2 Q30
    'bc3a6553-5c28-5abb-9a82-0ec7a0ea2615': {
        'stem': "The author's attitude to food self-sufficiency in the UK is ________.",
        'explanation': (
            "［精准定位］本文整体脉络为：引出话题“英国粮食自给自足是否可行”（第二段末）——分析问题，先指出就算采用极端手段，也无法满足英国人对动物性食品的需求，唯一可能就是减少动物性饮食，转向植物性饮食（第三、四段），然后进一步指出转向植物性饮食同样不可行，就算采用极端手段，可用土地也无法满足人们的总体需求（第五、六段），可见作者对英国实现自给自足持怀疑态度，［B］正确。\n"
            "［命题解密］［B］ doubtful 准确概括了第二段末 Sounds great—but how feasible is this vision? 第三段末 even covering... wouldn't allow us、第五段末 Even if... we would achieve only... 第六段末 That is before we look for... 等传递出的作者态度。\n"
            "［A］错误理解文章总体脉络，将文章“提出一种观点——指出这种美好愿景很难实现”理解为“提出一种观点，为之进行辩护”。［C］将第三段末、第五段末的让步表达（就算……，……）曲解为作者对计划的容忍，但作者实际是以极度夸张的提议来强调计划的不合理。［D］将第二段的“其他人的观点（作者认为很难实现）”当成作者的观点。\n"
            "［技巧总结］本题考查作者态度，应注意区分作者观点和他人观点，同时注意理解特殊表达传达的作者态度。如第五段末句“就算把所有条件适宜的土地都变成果蔬园地，取消所有的自然保护区，让成千上万的人们搬离家园——我们能实现的粮食产量增长也只有30%而已”并非说明作者真的认为“可以考虑把所有土地变成果蔬园地”，而是要凸显“就算如此，仍不能解决问题，更何况这本身实行起来会造成巨大代价”。"
        )
    }
}

def calibrate():
    exams = sorted(glob.glob('public/data/exams/*.json'))
    modified_files = set()
    calibrated_counts = 0

    for fpath in exams:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        file_changed = False
        for q in data.get('questions', []):
            qid = q.get('id')
            if qid in UPDATES_R36:
                upd = UPDATES_R36[qid]
                if 'stem' in upd:
                    q['stem'] = upd['stem']
                    file_changed = True
                if 'explanation' in upd:
                    q['explanation'] = upd['explanation']
                    file_changed = True
                    calibrated_counts += 1
                    print(f"Updated full explanation for {qid}")
                if 'clean_tail_regex' in upd:
                    orig_expl = q.get('explanation', '')
                    cleaned_expl = re.sub(upd['clean_tail_regex'], '', orig_expl, flags=re.DOTALL).rstrip()
                    if cleaned_expl != orig_expl:
                        q['explanation'] = cleaned_expl
                        file_changed = True
                        calibrated_counts += 1
                        print(f"Cleaned leakage tail for {qid}: len {len(orig_expl)} -> {len(cleaned_expl)}")

        if file_changed:
            with open(fpath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            modified_files.add(fpath)

    print(f"\nCalibration Round 36 complete! Modified {len(modified_files)} exam files, calibrated {calibrated_counts} questions.")

if __name__ == '__main__':
    calibrate()
