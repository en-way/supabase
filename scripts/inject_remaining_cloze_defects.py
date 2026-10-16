import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Definitions of the remaining 7 clean explanations
updates = {
    (2006, 5): """5. 
[A] Generally 普遍地；一般地
[B] Almost 几乎，差不多
[C] Hardly 几乎不
[D] Not 不是
［考点提炼］上下文逻辑语义。正确率：45%
［解题思路］根据下文②句 600,000 to 3 million 及③句 the figure may vary 可判断，①句含义应为“人们对于无家可归者的具体数字没有统一定论（此处 agree 指‘对……取得一致意见’）”；［D］常与不定代词 all/both/everyone/everything 等连用，表示部分否定，符合文意。
［错项排除］［A］和［B］均表达肯定含义，与句群整体导向不符；［C］强调“几乎没有（almost not）”，常与 any 和 anyone 搭配，而不与 some/someone/everyone 搭配。""",

    (2006, 20): """20. 
[A] supervision 监督，管理
[B] manipulation 操纵，控制
[C] regulation 管理，调节
[D] coordination 协调，配合
［考点提炼］上下文语义＋名词辨析。正确率：32%
［解题思路］As Edward Zlotkowski ... puts it（正如……所说）暗示本句与上文为顺承关系，即引另一位专家观点来进一步阐释上句内容。句中 a package deal（一揽子计划）对应上句 comprehensive programs（综合、全面的规划），换种说法阐明了方案性质，选项中与 of programs 搭配，能表示“各部分规划以高效的、条理的方式一同运作，配合并协调，从而达成好的结果”的只有［D］coordination。
［错项排除］其余三项均为单一的行为举措，其中［A］［C］利用“监管、管理”这类政府惯有职能设置干扰，但这种单一举措与上下文强调的“措施应全面、综合”相矛盾；［B］侧重于“为一己之私的操控行为”，其感情色彩为贬义，不符合政府积极解决社会问题的应有角色。""",

    (2008, 1): """1. 
[A] (be) selected (to do) 被选拔做
[B] (be) prepared (to do) 愿意做，准备好做
[C] (be) obliged (to do) 被迫做
[D] (be) pleased (to do) 乐意做
［考点提炼］上下文语义＋动词用法。正确率：24%
［解题思路］首句指出，某种观点无人敢明说；空格句继而指出，可 Gregory Cochran ______ 说出这一观点。But 和 anyway 表明前后两句发生语义转折，故空格处应表达“敢于（dare to）”的逻辑，符合要求的只有 (be) prepared to do，表示 Cochran“愿做、敢做、要做”普天下人所不敢为的事，［B］正确。
［错项排除］［A］和［C］均表被动，而“被选中去说”和“不得不说”均不符合 Cochran“积极勇敢”的主动态度，不能与上文构成转折。［D］表示“欣喜于某消息、情况”，非文中的果敢决心。""",

    (2008, 5): """5. 
[A] Only 只，仅仅
[B] So 因此
[C] Even 甚至，即使
[D] Hence 因此
［考点提炼］上下文逻辑语义。正确率：44%
［解题思路］上文指出，Cochran 特立独行，准备说出世人皆不敢言的观点；空格句指出，然而，他也会不寒而栗。关键词 however 表明空格句与上文为转折逻辑；选项逻辑词中，只有 Even 可以用于“强调某事出乎意料或令人吃惊”，能够强化这一转折逻辑，契合 rare bird 与 tremble at 之间的“出人意料”意味：甚至连 Cochran 这样的人也仍然会害怕，所以正确项为［C］。
［错项排除］“只有他会不寒而栗”与首段①句“无人敢明说（dare not speak its name）”文意相悖，排除［A］；［B］和［D］均引出顺承因果逻辑，与句中 however 体现的转折逻辑相矛盾。""",

    (2008, 19): """19. 
[A] limited (sb to sth) 限量；限定
[B] subjected (sb to sth) 使遭受，经历
[C] converted (sb to sth) 使转变（信仰等）
[D] directed (sb to sth) 给（某人）指路
［考点提炼］上下文语义＋动词用法。正确率：36%
［解题思路］上句摆出 Cochran 观点：智商和疾病紧密相关；随后详细说明该观点：这些人（该高智商族群）不同寻常的历史——他们……独特的进化压力。空格后 evolutionary pressures（进化压力）呼应第二段 natural selection（自然选择），由此判断 Cochran 观点应该是：该族群智商高很大程度源于进化压力，而这种压力同时也是他们易患病的主要源头，从而明确“高智商”和“易患病”的内在关联；故空格所在部分应该表现“他们因为不同寻常的经历而遭受到不一般的进化压力”之意，［B］符合文意。
［错项排除］［A］强调“对于数量或范围的限制”，而“不寻常的历史限制他们只受到进化压力”显然不合语义逻辑。［C］+ sb to sth 时，sth 需为“转而接受的信仰、立场”等；［D］+ sb to sth 时，sth 为“地点或方位词语”，两项均无法与“进化压力”构成合理搭配。""",

    (2008, 20): """20. 
[A] paradoxical 似非而是的，自相矛盾的
[B] incompatible 不相容的，不能并存的
[C] inevitable 不可避免的，必然的
[D] continuous 连续的，持续的
［考点提炼］上下文语义＋形容词辨析。正确率：27%
［解题思路］this state of affairs 回指上句“智商（高）与（易患）疾病密切相关”这一状况，空格处形容词表明这一状况的特点。根据上下文可知，此前人们普遍认为两者没有关联，而 Cochran 试图通过研究证实这一状况“看似矛盾不可能（前者为积极优势，后者为负面问题），但实际上很可能为真”，选项中能够表达该含义的形容词只有 paradoxical，强调某情况“看起来矛盾却很可能为真”。故［A］正确。
［错项排除］［B］常用于表示“事物或人非常不同，不协调或合不来的”，在说明观点时表示“不能同时为真、不能共存”，绝对化了这种矛盾性，违背文中“高智商和遗传疾病共存于一个族群”这一已知事实。［C］强调必然性，而“高智商与遗传疾病相关”是进化压力的结果，具有或然性，并非族群中每个高智商者都患病。［D］强调时间持续性，与句意不符。""",

    (2009, 19): """19. 
[A] fundamental 根本的；最重要的
[B] comprehensive 详尽的，无所不包的
[C] equivalent 相等的，相当的
[D] hostile 充满敌意的
［考点提炼］上下文语义。正确率：55%
［解题思路］空格句意为：它们希望研究一个______问题：人类是否真正了解自己所生存的世界？空格词修饰 question，说明问题的特点。由上文 really, not merely 可判断，针对人类智力，动物想要研究的问题越来越深入，从“智力高低”到“智力的真正用途”，越来越趋向于“智力的本质问题”，［A］fundamental 正确。
［错项排除］［B］利用句中 the world 干扰，认为关乎世界即无所不包，但核心只聚焦人类是否了解世界这一单点。［C］表示价值、数量相当，不用于说明内容属性。［D］由句中 actually 暗含的嘲讽语气推测敌意，但文意旨在借助假设动物提醒人类重新反思智力本质，并非树敌。"""
}

exams_dir = 'public/data/exams'
files_modified = 0

for (year, q_num), new_expl in updates.items():
    # Find matching exam file
    matched = False
    for f in glob.glob(f'{exams_dir}/*.json'):
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
        exam = d.get('exam', {})
        if exam.get('category_id') == 'ky1' and exam.get('year') == year:
            for q in d.get('questions', []):
                if q.get('sort_order') == q_num:
                    old_len = len(q.get('explanation', ''))
                    q['explanation'] = new_expl.strip()
                    with open(f, 'w', encoding='utf-8') as fp:
                        json.dump(d, fp, ensure_ascii=False, indent=2)
                    print(f"[{year} Q{q_num}] Updated successfully: {old_len} -> {len(new_expl)} chars")
                    matched = True
                    files_modified += 1
                    break
        if matched:
            break

print(f"Total specific injections completed: {files_modified}")
