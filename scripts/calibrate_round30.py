import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Calibration dictionary
CALIBRATIONS = {
    # 1. 2021 ky2 (4ebd819e-c832-5890-9048-ba16040a5607)
    '4ebd819e-c832-5890-9048-ba16040a5607': {
        2: {
            'explanation': """2. [A] Emphasize 强调；重视
[B] Identify 确认；找到
[C] Assess 评定；估算
[D] Explain 解释；说明
[考点提炼]上下文语义+动词辨析。
[解题思路]③④句指出，与工作相关的行为含有多个要素，______其中一个，其他就会变得扭曲。此两句与①②句“目标设定会带来不良影响”之间不存在任何显性关联词，表明两者间存在顺承关系，③④句“______一个会扭曲其他”应意在解释说明①②句“目标设定的不良影响”，空格词应该与“目标设定（想要达到的标准）”相关，指向“关注，聚焦，以……为目标/重点”等意，[A] Emphasize表示to give special importance to sth“重视”，“重视一个要素”即“将之设立为目标”，故正确。
[错项排除]总体而言，“确认/评估/解释某一个要素”与“其他要素被扭曲”不存在因果关联（and暗藏因果关联），且其语义内涵与“目标设定”关系较远。具体来看，[B] Identify可表示“找到，找出”，例：First of all we must identify the problem areas.（首先我们必须找出问题所在。）但由上句可知，各个要素是“已知的、显现的”。[C] Assess指的是对人/物的性质、质量而非构成成分进行评定。[D] Explain重“介绍事物的细节或原因以使他人理解”，其解释的对象应该是“某种复杂难解的事物或行为等”，而one已经是“被分解的、不难理解的一个要素”。"""
        },
        11: {
            'explanation': """11. [A] friendly 友好的；亲切的
[B] quiet 文静的；稳重的
[C] cautious 小心的；谨慎的
[D] diligent 勤勉的；刻苦的
[考点提炼]条件关系+句内语义。
[解题思路]空格句指出，如果标准变成了安全，就会有更多______司机，他们会遵守交通法规。________ drivers 一方面是条件从句“标准变成了安全”带来的结果，另一方面应该与drivers的定语从句who obeyed traffic laws的语义指向一致，[C] cautious表示being careful about what you say or do, especially to avoid danger"小心谨慎的"，符合上述两项条件。
[错项排除]均利用常规思维“公交车司机友好、稳重、勤奋”设障，但均无法契合条件句所传递的语境“安全”，不能与“将安全作为标准”构成“条件一结果”关联。"""
        },
        36: {
            'stem': "Nalini Ambady's study deals with ________.",
            'explanation': """【精准定位】由题干中的Nalini Ambady's study定位至第一、二段安巴迪的“行为薄片撷取”能力研究。第一段①句指出人们擅长通过第一印象即thin slices of experience评判他人，②句顺而指出安巴迪就thin slicing这一能力进行了研究，说明安巴迪的研究与人们的第一印象有关。再结合第一段③⑤句、第二段②句所指出的“安巴迪将参与者和学生对教师的评分进行对比，评估参与者对教师的第一印象的准确性”，可知安巴迪的研究涉及“第一印象的可靠性”，故［B］正确。

【命题解密】正确项［B］是对第一、二段中安巴迪的研究内容的正确概述，其中first impressions对应主题词first impressions、thin slices of experience，reliability是对correlated strongly、just as accurate、Accuracy dropped dramatically的高度概括。

【排除干扰】
［A］将第一段④句中对参与者的干扰occupying their conscious working memory断章取义为安巴迪的研究涉及人们的记忆，但原文并未提及记忆的力量。
［C］对第一段②③句中的关键信息professors, instructor, students强加关联，捏造出安巴迪的研究涉及“教师与学生的互动”。
［D］将第二段①②句中“参与者被要求写下评分理由，导致他们的评分准确性大幅下降”这一研究发现错误解读为“研究人员影响了参与者的判断”，而原文的真实含义是“写出评分理由”这一思考行为降低了评分的准确性。

【技巧总结】本题考查对细节信息进行整合概括的能力，解题时需要厘清段内、段际逻辑关系。
1. 从段内逻辑来看，第一段①句指出第一印象即“经验薄片（thin slices of experience）”，②句直接说明安巴迪的研究关乎“行为薄片撷取（thin slicing）”，从两者的重合内容thin slice可推断安巴迪的研究关乎“第一印象”。另外，第一段②③句和④⑤句呈现相似的句间关系：先说明参与者在不同条件下根据第一印象对教师评分，后描述该评分的准确性。这也说明安巴迪的研究重点是“第一印象的准确性”，由此锁定答案［B］。
2. 从段际逻辑来看，第一、二段都涉及安巴迪的研究，但两段之间构成对比关系：第一段的前两组参与者情况表明，当参与者根据第一印象评分时，评分结果往往非常准确；而第二段的第三组参与者（①②句）和另一项研究（④句）表明，过多思考反而会干扰我们判断的准确性。将两段逻辑串联可知，这两段的两项研究都在论证首段首句：我们很擅长运用第一印象来评判他人，此时深思不仅没有必要，而且会造成干扰。由此，进一步锁定答案［B］。［A］［C］［D］均运用各项研究对参与者的不同要求捏造干扰，可排除。"""
        }
    },

    # 2. 2022 ky1 (6d676d85-a38a-5fe4-9506-31de03b648b6)
    '6d676d85-a38a-5fe4-9506-31de03b648b6': {
        36: {
            'stem': "The personal grievance provisions of the ERA are intended to ________.",
            'explanation': """【锁定答案】D
1. 定位：结合题干关键词personal grievance provisions与are intended to可定位至第二段①句(Personal grievance procedures were designed to...)。
2. 分析：第二段①句指出，ERA的个人申诉程序旨在保护普通员工的工作岗位，避免员工被“不正当解雇”，意即：保障普通员工“免遭不正当解雇”的权利。
3. 确定：题干+ D项契合第二段①句文意：are intended to protect the rights of ordinary workers同义改写were designed to guard the jobs of ordinary workers from "unjustified dismissals"。

【排除干扰】
[A] 1. 定位：由选项关键词corporate practices可定位至第二段②句(conduct by management)。
2. 排除：A项错将条款的惩罚对象由“随意的解雇行为”扩大为“一切可疑的企业行为”；此外，惩罚只是个人申诉条款达到“保护普通员工的工作岗位”这一目的的途径，而非目的本身。
[B] 1. 定位：由选项关键词procedures可定位至第一段③句(procedurally)以及第二段①句(procedures)。
2. 排除：第一段③句的procedurally与第二段①句的procedures分别指“解雇流程”“个人申诉的流程”，B项论及的“招聘流程”这一细节与原文不符；其主体内容“完善流程”也并非条款目的所在，与题干所问不符。
[C] 1. 定位：由选项关键词employers可定位至第一段(an employer/Employers)。
2. 排除：C项“免除雇主的特定责任”与第一段中条款的具体规定“雇主必须给出解雇理由，并通过公正的程序解雇员工”的言外之意“雇主必须承担更多的责任”相悖。

【技巧总结】目的细节题的基本解题思路为：根据表达目的的标记词(aim at、intend to、with the purpose of、so as to、in order to等)锁定目的相关内容，然后选取对其进行改写或概括的选项。第二段①句以were designed to引出“ERA的个人申诉条款”的目的：guard the jobs of ordinary workers from "unjustified dismissals"。由此可知，个人申诉条款的目的在于“保护”，保护群体为“普通员工”，保护内容为“避免被不正当解雇的权益”，D项同时包含三个方面的内容，故锁定为正确项。"""
        },
        39: {
            'stem': "What might be an effect of ERA's unjustified dismissal procedures?",
            'explanation': """【锁定答案】B
1. 定位：结合题文同序的出题规律及本题关键词effect, unjustified dismissal procedures，可定位至第六、七段(caused/because/suffers from/affect/hamper, unjustified dismissal procedures)。
2. 分析：第六段介绍“ERA的不正当解雇程序对高薪经理自身的伤害”：使能力平平的经理们更难被雇用，并使包括经理在内的全体员工薪酬减少。第七段介绍ERA的不正当解雇程序对社会整体的伤害“阻碍社会繁荣与整体福祉”。
3. 确定：B项Employees suffer from salary cuts同义改写第六段④句中ERA的不正当解雇程序对全体员工的伤害firms pay staff less。

【排除干扰】
[A] 1. 定位：由选项关键词Highly paid managers可定位至第六段①③句(highly paid managers, manager)。
2. 排除：A项虽契合第六段①句的概述“使高薪经理受害”，但其强调的经理所受的具体伤害“直接下岗”与②句所述“企业更难解雇员工(costlier to fire an employee)”不符。
[C] 1. 定位：由选项关键词overall well-being可定位至第七段②句(overall well-being)。
2. 排除：C项将第七段②句中不正当解雇程序对整体福祉产生的影响由“阻碍”窜改为“助长”。
[D] 1. 定位：由选项关键词hire new staff可定位至第六段②句(hiring new staff)。
2. 排除：D项将第六段②句中ERA的不正当解雇程序对雇主招聘的影响由“招工更加谨慎(主观态度)”窜改为“招工需求扩大(客观情况)”。

【技巧总结】本题就“同一事物对不同主体的影响”命制细节题，常规解题思路为“题干/选项定位法+排除法”：1. 首先根据题干已知关键信息ERA's unjustified dismissal procedures以及考研命题规律“题文同序(38题针对第五段末句设题、40题针对第八段设题)”可初步定位至第六、七段；2. 随后根据各个选项所涉及的受影响主体分别进行定位，A项对应第六段①③句，B项对应第六段④句，C项对应第七段②句，D项对应第六段②句；3. 将选项与原文相比对，详见“锁定答案”与“排除干扰”。"""
        }
    },

    # 3. 2003 ky1 (91ff038a-e3f9-5b6d-82c5-1328735be1d1)
    '91ff038a-e3f9-5b6d-82c5-1328735be1d1': {
        30: {
            'stem': "From the text we learn that Stephen Cooper is ________.",
            'explanation': """［精准定位］根据题干中的人名Stephen Cooper定位到第四段第⑤句。该句提到，Stephen Cooper 是一位名人，曾大胆陈述动物研究的价值，因此可知他支持动物研究，正确项为［D］。
［命题解密］正确项［D］是对⑤句中who引导的定语从句的概括性改写。
［A］将句中 well-known personality 偷换成 well-known humanist。［B］用句中与 Stephen Cooper 无关的信息medical treatment设置干扰。［C］反向干扰，将Stephen Cooper由“动物研究的支持者”改为“动物权利倡导者”。
［技巧总结］长难句因其信息量大，内部关系复杂而成为常考点；且命题方式多样，几乎可采用任何考研题型（因果细节题、人物观点题、词义理解题、推理引申题等）。解答此类题的关键在于：运用语法、语义、语用等知识，并结合上下文准确理解句意；认识到偷梁换柱（将句中某处信息偷改一词或数词）、糅杂信息（将句中两处不相干信息糅杂到一起）、改变逻辑（改变句中因果关系等）是常见干扰方式。
本题采用“事实细节题”的形式对第四段⑤句这一长难句进行考查。分析该长难句句法结构不难发现，Stephen Cooper之前的上义词和随后的定语从句提供了解题所需信息：well-known personalities, courageous statements about the value of animal research（即“动物研究的支持者”），故［D］为正确项。［A］、［C］偷偷改变文中相关信息；［B］则利用文中无关信息捏造干扰。"""
        }
    },

    # 4. 2007 ky1 (e560bab8-4d9a-5149-a93f-1ee1d7bf4225)
    'e560bab8-4d9a-5149-a93f-1ee1d7bf4225': {
        41: {
            'explanation': """41. 答案 F（正确率：54%）
［标题匹配］第二段指出，父母应帮助孩子了解自身优缺点并一起克服缺点，以此发现孩子的兴趣所在，为未来的职业做准备，也即父母应着重引导孩子正确认识自我、了解自身特点，［F］“帮助孩子弄清楚他们是谁，即帮助孩子认清自我”（Help Your Kids Figure Out Who They Are）与该主旨相符，标题主题词 figure out 与段落关键词 identify 近义。
［干扰项排除］［D］Talk about the Future on a Regular Basis 虽然与文中部分信息 Periodically review / careers 有所重叠，但文中“寻找未来职业”是家长采取某些措施的目的，并非措施本身，这些措施并未涉及“谈论未来”，故排除。"""
        }
    }
}

def main():
    print("=== 开始 Round 30 数据校准 ===")
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
                    print(f"[{eid}] Q{order} stem updated: {repr(q.get('stem'))} -> {repr(upd['stem'])}")
                    q['stem'] = upd['stem']
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

    print(f"=== Round 30 数据校准完成，更新试题数: {total_updated} ===")

if __name__ == '__main__':
    main()
