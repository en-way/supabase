import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 12 Additional Deep Calibrations (2011 & 2009) ===")

# 1. 2011 ky1 calibration
path_2011 = "public/data/exams/111d6c78-81a1-53dc-a039-dad4c94ebd35.json"
with open(path_2011, "r", encoding="utf-8") as f:
    data_2011 = json.load(f)

# Fix cloze passage
content_2011 = data_2011["passages"][0]["content"]
old_sub = "Studies dating back to the 1930s indicate that laughter relaxes muscle tissues for up to [8] minutes, decreasing muscle tone for up to 45 minutes after the laugh dies down."
new_sub = "Studies dating back to the 1930s indicate that laughter [8] muscles, decreasing muscle tone for up to 45 minutes after the laugh dies down."
if old_sub in content_2011:
    data_2011["passages"][0]["content"] = content_2011.replace(old_sub, new_sub)
    print("-> Restored 2011 cloze passage blank [8]!")
else:
    print("-> Note: 2011 cloze passage already contains new_sub or pattern changed.")

# Fix Q3
expl_2011_q3 = """3. [A] stabilizing （使）变得稳定、稳固
[B] boosting 使增长
[C] impairing 损害；削弱，减少
[D] determining 查明，测定；决定

【考点提炼】句内语义+上下文语义。正确率：60%
【解题思路】空格短语作方式状语，说明笑是如何引起心脏和血管功能短期变化的；因此空格词既要表现“产生、变化”这一语义，又要体现“积极的”这一方向，只有[B]符合要求。
【错项排除】[A]虽体现积极影响，但强调“使某物稳定不变”，与文中 short-term changes 体现出的变化矛盾。[C]宾语多为“能力/数量”，文中宾语可与 impair 搭配，表“削弱心率和耗氧量”，但体现消极含义，与文意相反。[D]可表“查明”，此时逻辑主语为“人或某调查”；而“笑”并不能“查明”心率和耗氧量；该词还可表“决定”，此时逻辑主语为“某因素”，“笑”虽可算作一种因素，但显然不能“决定”心率和耗氧量。"""

# Fix Q7
expl_2011_q7 = """7. [A] opposite 相反的
[B] impossible 不可能的
[C] average 正常的
[D] expected 预期要发生的

【考点提炼】上下文语义逻辑。正确率：80%
【解题思路】句中取舍结构 instead of... 表明“笑”和“运动”对肌肉的作用方式是不同的。空格句为运动的影响：使肌肉紧张，下文指出笑的影响：降低肌肉紧张度，由此明确两者对身体的作用相反，[A]正确。
【错项排除】[B]表“笑达到了不可能达到的效果”，暗示“笑威力巨大”，与上下文强调的“笑对身体影响有限”矛盾。[C]表“达到平均值”，但该内容在文中无具体所指，且立场中性，仍不能体现“笑的影响有限”这一逻辑。[D]表“达到预期”，该内容实际上肯定了“笑的功用”，违背上下文论述重点。"""

# Fix Q8
expl_2011_q8 = """8. [A] hardens 硬化
[B] weakens 使松动
[C] tightens （使）变紧
[D] relaxes （使）放松

【考点提炼】句内语义逻辑。正确率：55%
【解题思路】空格句指出：研究表明，笑 ______ 肌肉，它能在笑声平息后降低肌肉紧张度。后半句 decreasing muscle tone... 作状语修饰空格词，指“降低肌肉紧张度”，也即“放松肌肉”，因此[D]正确。
【错项排除】[A]强调“物理属性上的使变硬，硬化”，而文中“笑”显然不能让肌肉硬化，同时与“降低紧张度”不符。[B]利用其“使松动”这一含义设置干扰，但其内涵为“削弱某物的坚定性、使其更易被破坏”，而“笑使肌肉松动”一方面有违常理，另一方面暗示“笑对肌肉产生消极影响”，与文意不符。[C]利用其“使（身体某部分）变得僵硬”设置反向干扰。"""

# Fix Q11
expl_2011_q11 = """11. [A] Except for 除……之外（表补充）
[B] According to 依据，按照（表来源和依据）
[C] Due to 因为，由于（表原因）
[D] As for 至于，关于（引出新对象）

【考点提炼】句内逻辑。正确率：90%
【解题思路】本句逗号前为“某理论”，逗号后是“对情绪VS身体反应之间关系的说明”；而上文②句通过 Anyway, ... does...（而且，确实）支持①句观点，故此处是对该观点的进一步实证，即通过“引用理论”来证明上文观点，选项中能表示引入信息来源的只有[B]。
【错项排除】[A]用法为“通过对局部的否定来凸显对主要部分的肯定”，但其所排除的对象与重点肯定的对象应属同一类别，而文中 one classical theory of emotion 与 our feelings 并非同类。[C]用于“引出造成某情况的原因”，但“理论”与“我们的感受部分……身体反应”根本不能构成因果关系。[D]用来引出“仍然与前文相关却稍有不同的话题”，而上文并未交代有关情绪的其他理论。"""

# Fix Q39
expl_2011_q39 = """39. According to Paragraph 4, the message conveyed by celebrity magazines is ________.
[A] soothing 令人宽慰的
[B] ambiguous 模棱两可的
[C] compensatory 具有补偿性的
[D] misleading 具有误导性的

【精准定位】第四段指出名人杂志传达的为人父母形象非常不现实：事实上为人父母者不如无子女夫妻幸福，单亲父母最不幸福（因为养育子女需要付出巨大艰辛）；而媒体传达的却是“明星单亲妈妈独自抚养孩子简直是小菜一碟”。可见，名人杂志的信息具有误导性，[D]正确。
【命题解密】正确项[D]结合②③句，对第四段①句关键词 hugely unrealistic 同义改写。
【干扰项设置】[A]对③句 raising a kid... is a piece of cake 断章取义，认为这一信息“令人宽慰”，但这是名人杂志本身宣扬的内容，并非段中对它的评价“极度失实（hugely unrealistic）”；[B]将②③句“说明名人杂志宣扬信息和现实育儿情形并不一致”误解为“说明名人杂志模棱两可，可以做出不同的解读”；[C]将②③句所述“现实情形”和“名人杂志信息”之间的“不一致、相悖关系”曲解为“补充、补偿关系”。"""

# Fix Q40
expl_2011_q40 = """40. Which of the following can be inferred from the last paragraph?
[A] Having children contributes little to the glamour of celebrity moms. 生孩子对明星妈妈的魅力几乎没有帮助。
[B] Celebrity moms have influenced our attitude towards child rearing. 明星妈妈已经影响了我们对养育子女的态度。
[C] Having children intensifies our dissatisfaction with life. 生孩子增强了我们对生活的不满。
[D] We sometimes neglect the happiness from child rearing. 我们有时会忽略生儿育女的快乐。

【精准定位】第五段末句指出，经常看到名人杂志上报道的幸福完美的为人父母形象正在造成我们对现实育儿体验的不满。可见，明星妈妈对我们养育孩子的态度/看法产生了影响，[B]为正确项。
【命题解密】正确项[B]是对第五段②句 the images... contributing to our own dissatisfactions with the actual experience 的概括引申。
【干扰项设置】[A]将①句信息“明星妈妈的魅力形象不大可能会影响许多人生孩子的决定（It's hard to imagine... many people... want children just because... glamorous celebrity moms）”曲解为“生孩子对明星妈妈的魅力没有太大影响”；[C]将②句中“造成我们对生活不满”的根源“我们每周看到的快乐轻松的为人父母形象（we see every week of stress-free, happiness-enhancing parenthood）”偷换成“生孩子”；[D]利用②句 stress-free, happiness-enhancing parenthood 捏造干扰 the happiness from child rearing，但文中并未提到我们忽略了这种快乐（neglect 无从得知）。"""

for q in data_2011["questions"]:
    so = q.get("sort_order")
    if so == 3:
        q["explanation"] = expl_2011_q3
    elif so == 7:
        q["stem"] = "Choose the best option for blank [7] in the passage:"
        q["options"] = [
            {"key": "A", "text": "opposite", "value": "A"},
            {"key": "B", "text": "impossible", "value": "B"},
            {"key": "C", "text": "average", "value": "C"},
            {"key": "D", "text": "expected", "value": "D"},
        ]
        q["correct_answer"] = "A"
        q["answer"] = "A"
        q["explanation"] = expl_2011_q7
    elif so == 8:
        q["stem"] = "Choose the best option for blank [8] in the passage:"
        q["options"] = [
            {"key": "A", "text": "hardens", "value": "A"},
            {"key": "B", "text": "weakens", "value": "B"},
            {"key": "C", "text": "tightens", "value": "C"},
            {"key": "D", "text": "relaxes", "value": "D"},
        ]
        q["correct_answer"] = "D"
        q["answer"] = "D"
        q["explanation"] = expl_2011_q8
    elif so == 11:
        q["explanation"] = expl_2011_q11
    elif so == 39:
        q["explanation"] = expl_2011_q39
    elif so == 40:
        q["stem"] = "Which of the following can be inferred from the last paragraph?"
        q["options"] = [
            {"key": "A", "text": "Having children contributes little to the glamour of celebrity moms.", "value": "A"},
            {"key": "B", "text": "Celebrity moms have influenced our attitude towards child rearing.", "value": "B"},
            {"key": "C", "text": "Having children intensifies our dissatisfaction with life.", "value": "C"},
            {"key": "D", "text": "We sometimes neglect the happiness from child rearing.", "value": "D"},
        ]
        q["correct_answer"] = "B"
        q["answer"] = "B"
        q["explanation"] = expl_2011_q40

with open(path_2011, "w", encoding="utf-8") as f:
    json.dump(data_2011, f, ensure_ascii=False, indent=2)
print("-> Restored 2011 ky1 Q3, Q7, Q8, Q11, Q39, Q40 successfully!")

# 2. 2009 ky1 Q11 explanation calibration
path_2009 = "public/data/exams/9369aa41-c91e-548c-bf99-1ad46a07ac25.json"
with open(path_2009, "r", encoding="utf-8") as f:
    data_2009 = json.load(f)

expl_2009_q11 = """11. [A] features 特色，特点
[B] influences 影响，作用
[C] results 后果，结果
[D] costs 成本；代价

【考点提炼】上下文语义。正确率：26%
【解题思路】空格句指出，新研究没有……，而是含蓄地提出问题：我们智力的真正 ______ 会是什么。it 指代 this new research，因此这一问题应该与段首句问题“不那么聪明是否更具备适应能力”相统一，而 of our own intelligence 表明本句论述主体为“人类的智力（＝非常聪明）”，因此两个问题是反向呼应关系，选项中能体现“不利”逻辑的只有 cost，即：人类为了获得更高的智力，损失了许多，这也与上文从实验得出的结论 Intelligence is a high-priced option 相吻合。因此正确项为[D]。
【错项排除】the real features 暗指实验聚焦于研究“人类智力区别于其他物种的特征”，偏离文章主题“智力的代价高昂”，故排除[A]；[B]、[C] 皆用中文思维近义干扰，但错在“真正的动作/结果”缺乏方向性（两者既可以指“好影响/结果”，也可指“坏影响/结果”），不足以表现“代价不利”这一语义逻辑。"""

for q in data_2009["questions"]:
    if q.get("sort_order") == 11:
        q["options"] = [
            {"key": "A", "text": "features", "value": "A"},
            {"key": "B", "text": "influences", "value": "B"},
            {"key": "C", "text": "results", "value": "C"},
            {"key": "D", "text": "costs", "value": "D"},
        ]
        q["correct_answer"] = "D"
        q["answer"] = "D"
        q["explanation"] = expl_2009_q11

with open(path_2009, "w", encoding="utf-8") as f:
    json.dump(data_2009, f, ensure_ascii=False, indent=2)
print("-> Restored 2009 ky1 Q11 options and explanation successfully!")

print("=== Additional Deep Calibrations Complete! ===")
