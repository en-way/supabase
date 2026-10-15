import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 2021 ky2 Q38
EXPL_2021_KY2_Q38 = """38. Judith Hall mentions driving to show that ・
38. 朱迪斯•霍尔提及驾驶是为了表明 。
[A] reflection can be distracting [A] 深思熟虑有时反会让人分心
[B] memory may be selective [B] 记忆可能具有选择性
[C] social skills must be cultivated [C] 社交技能须经培养才能获得
[D] deception is difficult to detect [D] 欺骗行为难以察觉

［精准定位］由题干中的人名Judith Hall及关键词driving定位至第三段。②句指出，朱迪斯•霍尔认为，深思如同开手动挡车，多思反而会让人忘记要做什么，而任由直觉发挥作用往往会开得很好；首句也指出，当我们依靠直觉而非深思时，更能从“行为薄片”中觉察到欺骗；言外之意即直觉比深思更可靠。［A］符合题意。
［命题解密］正确项［A］是对朱迪斯•霍尔比较手动挡汽车驾驶员的两种心态之目的的正确解读。
［错项排除］［B］对②句you can't remember what you're doing断章取义。该句意在说明"深入思考会将注意力导向其他事物，忘记原本所要做的事”，而非“记忆具有选择性”。［C］由末句碎片信息“社交生活”捏造而来，本文并未论及获得社交技能的途径。［D］由首句中we're better at detecting deception逆向推导而来，但该句意在指出依靠直觉作出的判断比依靠深思更准确。
［技巧总结］人物观点+写作目的题。解答此类题时，除直接从人物观点本身推断出答案外，亦可借助论据（人物观点）与论点（作者观点）的关系进行判断：由首句作者观点可知，朱迪斯•霍尔提及驾驶是为了表明（处理社交信息时）深思熟虑反会让人分心，[A]正确。"""

# Load and update 2021 ky2
f_2021_ky2 = 'public/data/exams/4ebd819e-c832-5890-9048-ba16040a5607.json'
d = json.load(open(f_2021_ky2, encoding='utf-8'))
for q in d['questions']:
    if q['sort_order'] == 38:
        q['explanation'] = EXPL_2021_KY2_Q38
        print("Updated 2021 ky2 Q38 explanation")
json.dump(d, open(f_2021_ky2, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# Load and update 2016 ky1 Q42
f_2016_ky1 = 'public/data/exams/666cdb4e-7fd3-53c2-8c91-a12fa3160c09.json'
d = json.load(open(f_2016_ky1, encoding='utf-8'))
for q in d['questions']:
    if q['sort_order'] == 42:
        idx = q['explanation'].find('\n\n43.')
        if idx != -1:
            q['explanation'] = q['explanation'][:idx].strip()
            print("Cut bleed in 2016 ky1 Q42")
json.dump(d, open(f_2016_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# Load and update 2013 ky1 Q33
f_2013_ky1 = 'public/data/exams/6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json'
d = json.load(open(f_2013_ky1, encoding='utf-8'))
for q in d['questions']:
    if q['sort_order'] == 33:
        idx = q['explanation'].find('\n\n34\n\n•')
        if idx != -1:
            q['explanation'] = q['explanation'][:idx].strip()
            print("Cut bleed in 2013 ky1 Q33")
json.dump(d, open(f_2013_ky1, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print("Applied precision fixes to the 3 remaining cases.")
