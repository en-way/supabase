import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

CALIBRATIONS = {
    # 1. 2021 ky2 (4ebd819e-c832-5890-9048-ba16040a5607)
    '4ebd819e-c832-5890-9048-ba16040a5607': {
        14: {
            'explanation': """14. [A] break 间歇；间断；暂停
[B] trip 旅行；出行
[C] departure 起程；班次；违反
[D] transfer 中转；搬迁；调动
[考点提炼] 上下文语义+名词辨析。
[解题思路] 空格句指出，航空公司只是修改了一下_______所需的时间。后一句具体介绍航空公司如何修改时间：一小时的航程被号称为两小时（one-hour flight -> two-hour flight）。可见，航空公司修改的是“一趟航行/航程（flight）”所需的时间，空格词应与flight近义，[B] trip表示“出行，旅行”，正确。
[错项排除] 分别利用航班的“经停/起飞/中转”时间捏造干扰，但由one-hour flight -> two-hour flight可知，航空公司修改的不是旅程中间某一阶段所花费的时间，而是整个旅程总共耗费的时间；另外，departure time指航班起飞的时间点，与is meant to take（时间段）无法搭配。"""
        }
    },

    # 2. 2007 ky1 (e560bab8-4d9a-5149-a93f-1ee1d7bf4225)
    'e560bab8-4d9a-5149-a93f-1ee1d7bf4225': {
        15: {
            'explanation': """15. [A] support 支持
[B] cry 叫喊
[C] plea 请愿
[D] wish 愿望
［考点提炼］习惯搭配。正确率：71%
［解题思路］③句表明，多数领导者主张继续保留天主教的国教地位，而有一些则想终结这一局面；④句继而指出，捍卫天主教成为了保守势力团结的口号。句中conservative forces回指上文most leaders所代表的保守势力；因此a rallying cry一方面要对The defense of the Church这一行为定性，另一方面还应体现保守派想维护天主教地位的迫切心情；rallying cry为固定搭配，指“（团结并鼓励人们支持某人/事的）战斗口号、信念”，［B］为正确项。
［错项排除］rally意为“集合、召集（人们以支持某人/事）”，［A］和［C］均可以与之构成合理的动宾搭配，分别表示“（为某人/物）争取支持”、“召集人们共同请愿”，介词for引出“支持、请愿的具体对象或目标”，如They aimed at rallying support for the new plan.（他们的目的在于为这项新计划争取支持。）；而文中rallying由不定冠词限定，表明rallying“作定语修饰空格名词”而非“表示动作，引出宾语”；两者由rallying修饰，行文逻辑就变为“支持、请愿有利于团结人们”，混淆“团结的目的（支持某人/事、为某人/事而请愿）”与“有助于团结的因素”。［D］利用字面含义“捍卫宗教成为了保守派的一致心愿”设置干扰，但wish同样不能由rallying修饰。"""
        }
    },

    # 3. 2004 ky1 (47036de0-e57d-5ccb-9bc8-b3f86d4e6457)
    '47036de0-e57d-5ccb-9bc8-b3f86d4e6457': {
        25: {
            'explanation': """【精准定位】第五段首句提到：即使那些不找工作的人也会觉得“搜索代理”有用。因此［C］正确。

【命题解密】这种题型有一定的难度，它要求考生对全文有综合性的理解，因此在解题时可以考虑将排除法和定位法相结合。这题看似涉及全篇文章，实际上只是考查对最后一段的理解。［C］与［D］选项意思相反，而正确答案一般就在两个相反的选项中产生。正确项［C］为第五段首句的同义改写：those already employed对应文中those who aren't hunting for jobs，helpful对应原文中worthwhile。

【排除干扰】
［A］夸大其辞，将第三段中used as a kind of tip service（当作一种提示性服务）改成了indispensable（必不可少的）。
［B］偷换概念，将第五段首句“在职者通过搜索代理跟踪市场对自己所在行业的需求”改成了“网站跟踪求职者的需求”。
［D］反向干扰，agents stop sending information对应第五段首句中maintains his agent（保留搜索代理）。"""
        },
        30: {
            'explanation': """【精准定位】纵观全文，首段提出主题：姓氏字母排序歧视现象，接着第二、三段举例说明杰出人物多为姓氏字母排序靠前的人，第四段指出姓氏字母排序造成了儿童受教育机会的不平等，第五段继续列举了生活中更多姓氏字母排序造成的不平等。由此可见，全文都围绕姓氏字母排序这种不公平现象展开论述，［D］正确。

【命题解密】本题考查考生对文章整体内容的把握。本题和第26、27题都以不同的方式考查了文章主旨。正确项［D］是全文要表达的信息，putting things alphabetically是文章讨论的对象alphabetism的同义替换；unintentional bias不仅是第一段的定义中提到的本质特点，也在第四、五段的举例中得到论证。

【排除干扰】
［A］偷梁换柱，将第一段末句中with a letter in the lower half of the alphabet偷换成with N to Z，文章只是泛泛提到姓氏字母排序靠后的人处于劣势，并没有具体到从哪个字母开始。
［B］夸大其辞，将“一些杰出人物的姓氏字母排前”泛化为“重要人物都从姓氏字母排序中获益很大”，第三段虽然提到很多杰出人物在姓氏字母排序中靠前，但不能泛泛说成是重要人物都从中获益。
［C］过度引申，从“姓氏字母排序现象的隐蔽性”引申出“消除该现象的艰巨性”，本文只停留于对“姓氏字母排序现象的不公平性”的论证，而没有提及该现象的消除。"""
        }
    },

    # 4. 2022 ky1 (6d676d85-a38a-5fe4-9506-31de03b648b6)
    '6d676d85-a38a-5fe4-9506-31de03b648b6': {
        27: {
            'stem': 'The percentage of UK graduates in non-graduate roles reflects ________.',
            'explanation': """【锁定答案】B
1. 定位：根据题干中 The percentage...roles 可定位至第二段⑤句(28 per cent...roles...)。
2. 分析：第二段⑤句指出，超过四分之一的英国大学毕业生从事着无需本科学历的工作。再看前文内容：随着大学学位的普及，其价值不免降低；教育不再是实现社会阶层流动的可靠途径。联系可知，⑤句所援引的数据是在说明大学学位不再被就业市场看重，意即学位价值降低。
3. 确定：B项 the shrinking value of a degree 是对⑤句信息的准确概括，且复现③句 degrees...became devalued。

【排除干扰】
[A] 1. 定位：根据选项内容可定位至第二段①②句(Millennials were told...But...)。
2. 排除：选项将题干直接定位句(第二段⑤句)结合该段第①②句进行过度引申：“大学学位不再是体面生活的保证”使得千禧一代“改变了对工作的看法，开始对所有工作一视同仁”，故大学毕业生从事无需本科学历的工作比例增加，但文中并未提及千禧一代的工作观。
[C] 1. 定位：根据选项内容可定位至第二段③④句(degrees...devalued...Education was no longer...)。
2. 排除：选项将题干定位句第二段⑤句结合③④句进行过度引申：“大学学位的价值降低，大学教育不再能实现社会阶层跃升，公众对此颇为不满，故大学毕业生从事非毕业生工作的比例增加”。文中并未提及公众对教育的不满。
[D] 1. 定位：根据选项内容可定位至第二段④句(Education...mobility)。
2. 排除：题干+ D项将第④⑤句理解为取舍关系“教育不再是实现社会流动性的可靠途径，从事无需本科学历的工作才是”，而实际上两者是观点一例证关系“教育不再能保证社会流动：很大一批大学毕业生从事着无需本科学历的工作”。

【技巧总结】本题属于写作目的题。解答此类题时需注意，援引某个数据、事例目的都是为了服务于段落/文章主旨，因此，检验选项正确与否需看其是否符合段落/文章主旨。此外，由于主旨必不能脱离文本，故检验选项时亦可依据其是否确为文中所提及的信息。
如本题，读题可发现解答本题的关键在于分清“导致英国大量大学毕业生从事无需本科学历的工作的原因”，且正确项必须符合两个要求：1. 确为文中所提及的信息；2. 和题干信息(对应第二段⑤句)存在因果关系。B项是文中所提及的信息(they/degrees became devalued)，且能和题干信息形成合理的因果关系(学位贬值 -> 大量大学毕业生从事无需本科学历的工作)，故正确；而千禧一代的工作观(Millennial's opinion)、公众的不满(public discontent)、实现社会阶层流动的理想途径(the desired route)文中均未提及，故A、C、D三项皆可排除。"""
        },
        32: {
            'stem': 'The reworked version of The Four Seasons is mentioned to show that ________.',
            'explanation': """【锁定答案】A
1. 定位：根据题干 The reworked version of The Four Seasons 定位至第三段①句。
2. 分析：第三段以“例如”开头，说明本段内容是对第二段内容的例证。第二段主要阐述了科学家日益寻求与艺术家合作，艺术家能够帮助科学家以新的方式传播他们的科研成果。第三段详细列举了《四季》的改编版本如何通过艺术形式向公众传达气候变化的科学数据。因此，提到《四季》的改编版本是为了说明艺术能够帮助公众理解科学。
3. 确定：A项 art can offer audiences easy access to science（艺术能让受众更好地理解科学）契合第二段主旨与第三段的例证目的。

【排除干扰】
[B] 科学有助于人们表达情感：第三段强调的是通过音乐表达科学数据，而非用科学表达情感，主客体倒置。
[C] 公众参与科学有很好的前景：文中并未提及公众直接参与科研，而是公众作为受众接触科学。
[D] 艺术有助于促进科学创新：第三段强调的是艺术在传播科学（research communication）方面的作用，而非促进科学本身的创新（innovations）。

【技巧总结】本题为写作目的题（例证题）。解答例证题的关键在于寻找事例所服务的论点。论点通常出现在事例之前（即第二段末或第二段主旨句）。由第二段 Scientists are increasingly seeking out visual artists... Artists help scientists... 这一语义链条可知其重在说明“艺术家对于科学家传播科学的作用”，从而锁定A项。D项利用考生做题时间紧而来不及细看或不把选项读到底的倾向设置干扰，对此应保持警惕。"""
        },
        37: {
            'stem': 'It can be learned from Paragraph 3 that the provisions may ________.',
            'options': [
                {'key': 'A', 'text': 'hinder business development', 'value': 'A'},
                {'key': 'B', 'text': "undermine managers' authority", 'value': 'B'},
                {'key': 'C', 'text': 'affect the public image of the firms', 'value': 'C'},
                {'key': 'D', 'text': 'worsen labor-management relations', 'value': 'D'}
            ],
            'explanation': """【锁定答案】A
1. 定位：由题干关键词Paragraph 3, the provisions可定位至第三段（these provisions）。
2. 分析：第三段①句概述指出“个人申诉条款（these provisions所指）如应用于企业管理人员，会给企业带来不少难题”。②句明确个人申诉条款给企业带来的具体难题：限制企业解雇表现不佳的管理人员，阻碍企业生产效率以及整体业绩的提高，即阻碍企业发展。
3. 确定：A项 hinder business development 高度概括了②句中 a handbrake on boosting productivity and overall performance，契合①句中 create difficulties for businesses。

【排除干扰】
[B] 1. 定位：由选项关键词managers' authority可关联至第三段③句中对经理等级的表述（C-grade and A-grade managers）。
2. 排除：B项错误有二：1. ③句中A级与C级界定的是工作能力高低而非其职权大小；2. 根据⑤句“无法仅凭工作能力不足就解雇员工”，可知条款“巩固”而非“动摇”了经理的职权。
[C] 1. 定位：选项 affect the public image of the firms 对第三段②句 handbrake on... overall performance断章取义。
2. 排除：C项将②句中个人申诉条款的影响对象overall performance由“企业的整体业绩”曲解为“企业的公众形象”，文中并无信息支持。
[D] 1. 定位：选项关键词 labor-management relations 对第三段③④句 The difference between... managers... workers 断章取义。
2. 排除：D项将③④句中论述的“管理人员能力差”与“员工下岗”之间经济上的消极因果关联窜改为“企业与劳动者之间的不和谐雇佣关系”，故错误。

【技巧总结】联系选项谓语hinder、undermine、affect、worsen与题干关键词the provisions可知，本题询问“条款的影响（重点关注消极影响）”，实际为因果细节题。因果题解题时应紧抓文章的显性（如because、for、due to等）和隐性因果标志词（如contribute to、harm、affect等），具体到本题：1. 在题干限定的范围“第三段”找到因果标志词：create difficulties for、constraining... from、is a handbrake on... The difference between... and... may very well be the difference between... or... Between... or...；2. 提取因果关系链：①条款使企业发展困难；②条款限制企业解雇表现不佳的高薪经理 -> 阻碍企业生产效率及整体业绩的提高；③经理水平高低 -> 决定企业成败 -> 决定低能的普通员工是否能保住工作。3. 对比选项：A项契合前两个因果关系，B项与第二个因果关系不符，C项与以上三个因果关系均无直接关联，D项窜改第三个因果关系。"""
        },
        38: {
            'stem': 'Which of the following measures would the Productivity Commission support?',
            'explanation': """【锁定答案】D
1. 定位：由题干关键词Productivity Commission可定位至第五段②句(Productivity Commission)。
2. 分析：第五段①句提出论点：限制企业主解雇表现不佳的经理可能限制企业生产效率和员工薪资。②句引用新西兰生产力委员会的结论具体说明：管理能力低下是该国生产率增长数据不佳的原因之一。联系委员会的职责“促进本国生产率增长”可反推其可能支持企业解雇表现不佳的经理，以提高整体管理能力。
3. 确定：D项 Dismissing poorly performing managers 由第五段①句 constrain... from dismissing under-performing managers、②句 the low quality of managerial capabilities 反推而来。

【排除干扰】
[A] 1. 定位：由选项关键词wage restraints可定位至第五段①句(constraint on... wages)。
2. 排除：由第五段①句 constraint on firm productivity and therefore on workers' wages可知“员工薪资受限”是“企业生产效率受限”产生的结果，而非“提高生产效率的手段”，故A项错误。
[B] 1. 定位：由选项关键词employment protection laws可定位至第五段①句(employment protection laws)。
2. 排除：第五段①句指出“就业保护法限制了企业的生产效率”，故B项“强制实施就业保护法”这一措施会进一步加剧该国生产率增长的不良状况，不符合生产力委员会的职责。
[C] 1. 定位：由选项关键词business owners可定位至第五段①句(business owners)。
2. 排除：结合第五段①句与第三段②句可知为了促进本国生产率增长，生产力委员会需“保障”而非“限制”企业主的合理解雇权，排除C项。

【技巧总结】本题由题干关键词the Productivity Commission定位至第五段②句，但句中仅言及生产力委员会的研究发现，并未直接谈及委员会的对策，解题时需对第五段②句进行分析推理。推理题应避免拘泥于细枝末节，而需抓取大方向，如关注点、基本关系以及褒贬倾向。具体来看，第五段②句中in "An International..." (2014)部分点明信息来源，为细节信息，可略过不看；主干的谓语部分 singled out A as a cause of B提示基本关系“管理能力低下导致新西兰生产率增长数据不佳”，联系主语“生产力委员会”这一名称可知：委员会关注点在于“提高生产力”及其影响因素“管理能力强弱”。对比选项后发现：A项措施为企业管理的内容之一，对管理能力强弱无影响；B、C两项措施均有损企业的“管理能力”；D项措施有利于增强企业“管理能力”，故锁定为正确项。"""
        }
    },

    # 5. 2022 ky2 (cc4bf627-e456-538f-87e2-4a99ebb613ed)
    'cc4bf627-e456-538f-87e2-4a99ebb613ed': {
        27: {
            'stem': 'It can be inferred from Paragraph 3 that Americans tend to think that ________.',
            'explanation': """【精准定位】根据题干定位至第三段。该段①②句指出美国人不退休的两个原因“财务需求”和“个人满足感/情感需求”，③句援引受访者的看法具体说明：有人不退休是为了心理健康，有人是为了生计。可见，美国人认为不退休可以避免财务或健康问题，换言之即退休可能会引发这些问题，故［A］正确。

【命题解密】［A］是对美国人的看法“不退休以避免财务或健康问题”的合理推断。

【排除干扰】
［B］利用第三段②句boredom干扰，但与该句暗含文意“不退休可防止无聊”恰好相反。
［C］利用第三段②③句复现词mentally fit干扰，但原文实指“一些人不退休是为了保持心理健康”，并未提及“退休人员的心理健康是否得到关注”。
［D］中the economy源自第三段①句Financial needs，但根据本段末句making ends meet（维持生计）及上段末句even if they had enough money可知，文意实指“不退休旨在满足个人的财务需求”，而非“利于宏观经济发展”。

【技巧总结】推理引申题往往难以直接选出正确项，可采用排除法。本题中，［A］没有明显定位词，难以直接判断正误，可先保留。［B］可根据关键词boredom轻松定位，并判断出该项与文意相悖，故排除。［C］虽近义复现文中关键词mentally fit，但其核心义is overlooked在文中并无依据，故排除。［D］可根据the economy定位至第三段①③句，但回文阅读后发现该项曲解原文含义，故排除。此时再检视［A］，发现该项可由本段主旨“美国人为避免财务和心理问题而不退休”反推而来，故正确。"""
        }
    }
}

def main():
    print("=== 开始 Round 31 数据校准 ===")
    total_updated = 0
    for eid, q_updates in CALIBRATIONS.items():
        filepath = f"public/data/exams/{eid}.json"
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        modified = False
        for q in data.get('questions', []):
            order = q.get('sort_order')
            if order in q_updates:
                upd = q_updates[order]
                if 'stem' in upd and q.get('stem') != upd['stem']:
                    print(f"[{eid}] Q{order} stem updated:\n  Old: {repr(q.get('stem'))}\n  New: {repr(upd['stem'])}")
                    q['stem'] = upd['stem']
                    modified = True
                if 'options' in upd and q.get('options') != upd['options']:
                    print(f"[{eid}] Q{order} options updated: {q.get('options')} -> {upd['options']}")
                    q['options'] = upd['options']
                    modified = True
                if 'explanation' in upd and q.get('explanation') != upd['explanation']:
                    print(f"[{eid}] Q{order} explanation updated: len {len(q.get('explanation', ''))} -> {len(upd['explanation'])}")
                    q['explanation'] = upd['explanation']
                    modified = True
                total_updated += 1
        
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Successfully saved {filepath}\n")

    print(f"=== Round 31 数据校准完成，更新试题数: {total_updated} ===")

if __name__ == '__main__':
    main()
