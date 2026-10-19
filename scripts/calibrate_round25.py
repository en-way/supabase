import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 25 Calibration Script ===")

# Helper to find exam by year and category
def load_exam(year, category):
    for fn in os.listdir('public/data/exams'):
        if fn.endswith('.json'):
            path = os.path.join('public/data/exams', fn)
            with open(path, 'r', encoding='utf-8') as f:
                d = json.load(f)
                if d['exam']['year'] == year and d['exam']['category_id'] == category:
                    return path, d
    raise FileNotFoundError(f"Exam {year} {category} not found")

calibrated_count = 0

# 1. 2009 ky1 Q38
p09, d09 = load_exam(2009, 'ky1')
for q in d09['questions']:
    if q['sort_order'] == 38:
        q['stem'] = "The early ministers and political leaders in Massachusetts Bay"
        q['explanation'] = (
            "［精准定位］第二段末句提到，这些人（即上文提到的马萨诸塞湾早期移民中的牧师和政治领袖）大量著书并出版，读者甚多，为新英格兰营造了一种热切的求知氛围，因此［D］正确。\n"
            "［命题解密］正确项［D］同义改写末句giving New England an atmosphere of intellectual earnestness。\n"
            "［A］将③句reaching... audiences意在表明“这些人书作被读者熟知”曲解为“这些人因书作而闻名(famous)”。［B］将②句learned ministers who came to Massachusetts churches意在说明“这些知识渊博的牧师来到马萨诸塞教会后，与政治领袖们一起营造了新英格兰的文化求知氛围”而非“他们在宗教事务中的重要性日益增加”；况且上一段很明确指出本文从文化而非宗教角度考查这些早期移民，所以排除。［C］将②句official of the Crown before he journeyed to Boston意在描述“马萨诸塞早期移民中政治领袖代表约翰·温思罗普”的细节偷换到“所有早期移民到该地区的牧师及政治领袖身上”。\n"
            "［技巧总结］命题人在命制试题的过程中，一般会遵循文章主旨和主要线条，使五道题目均匀地分散于全文，也就是说文章主旨能为大部分题目提供解题指导。在考查事实细节的题目中，题干＋正确项通常也能体现文章主旨。考生在快速解题时可适当使用此技巧。具体到本题，考生可结合本文主旨来快速解题。\n"
            "由前两段可知，本文围绕“早期新英格兰的文化生活”这一话题，从“移民对欧洲文化的传承和融入”角度进行论述。第三段介绍早期来到马萨诸塞湾的牧师和政治领袖具体说明主旨，即他们是如何承载欧洲文化并融入新大陆、如何影响新英格兰的文化生活。选项中只有［D］符合这一推测，其他选项均偏离文章主旨：［A］拘泥于“写书”这一行为本身；［B］涉及宗教，与第二段表明的本文全新研究视角相矛盾；［C］聚焦于他们远渡重洋所付出的社会地位成本，与“新大陆的文化生活”无关。"
        )
        calibrated_count += 1
with open(p09, 'w', encoding='utf-8') as f:
    json.dump(d09, f, ensure_ascii=False, indent=2)
print("Updated 2009 ky1 Q38")

# 2. 2012 ky1 Q22 & Q39
p12, d12 = load_exam(2012, 'ky1')
for q in d12['questions']:
    if q['sort_order'] == 22:
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "learn from advertisers' experience"
            elif opt['key'] == 'D':
                opt['text'] = "recognize the limitations of advertisements"
        calibrated_count += 1
    elif q['sort_order'] == 39:
        q['explanation'] = (
            "［精准定位］根据题干关键词Wisconsin定位到第六段，该段实际接续第五段（段落主旨句①句）文意“公共部门改革遭到工会强烈反对”：段首指出由于当前不合理体制的代价越来越明显，政治家们已开始采取强硬措施（进行改革），随后提及威斯康辛州各工会集结大批支持者反对州长（政治家之一）。可见，作者意在借此例说明工会阻碍了应有的公共部门改革。［C］正确。\n"
            "［命题解密］第六段承接第五段而来，因此第六段中事例论证实际是出现于第五段首句的观点。［C］是第五段首句Reform has been vigorously opposed (by the trade unions)的同义改写。\n"
            "［A］将第六段②句渗透之意一“工会反对意在改革现行体制的州长，以维护现有体制”反向曲解为“工会反对现行政治体制”；［B］、［D］将该句渗透之意二“工会召集成千上万的支持者反对强硬的州长”分别曲解为“工会能够改变人们的政治态度”、“工会在政府内占据主导地位”。\n"
            "［技巧总结］面对“事例写作目的题”，考生应：理清行文脉络、区分论点论据，体味事例以点带面的性质。具体解答思路为：①圈定“事例范围”并将其作为一个整体加以理解，并从上下文中寻找作者“观点结论”或“意在说明的现象”，注意搜索范围不是“段”，而是“意群”（有时需跨段寻找）；②注意正确项特征：不仅能完整概括事例，还需明显大于事例本身，且能和上下文顺滑衔接，成为一体；③了解干扰项设置方式：直接摘取文中细枝末节；歪曲事例中具体细节；扭曲论点（事例说明对象）。\n"
            "具体到本题为：先根据关键词the unions in Wisconsin定位到第六段②句，并进而将事例讲述范围扩大到①②句，将事例本身大致概括为“威斯康辛州工会集合力量反对州长行动”。然后向上段寻找论点/事例说明对象，发现明显观点句为Reforms has been vigorously opposed (by unions)，而［C］(unions) may be a barrier to public-sector reforms和该句近义，且体现了事例以点带面的性质，故很可能是正确项。而［A］、［B］、［D］均歪曲事例中具体细节（直接反向干扰、偷换因果关系、夸大其词），故将其排除。"
        )
        calibrated_count += 1
with open(p12, 'w', encoding='utf-8') as f:
    json.dump(d12, f, ensure_ascii=False, indent=2)
print("Updated 2012 ky1 Q22 & Q39")

# 3. 2016 ky1 Q35
p16, d16 = load_exam(2016, 'ky1')
for q in d16['questions']:
    if q['sort_order'] == 35:
        q['correct_answer'] = "B"
        q['answer'] = "B"
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "The necessary amount of companies' spending on it is unknown."
            elif opt['key'] == 'C':
                opt['text'] = "Companies' financial capacity for it has been overestimated."
        q['explanation'] = (
            "［精准定位］末段首句指出，研究未能回答“企业应该在CSR上投入多少”这一问题，也即企业在CSR上具体的必要花费数额尚不得而知，［B］正确。\n"
            "［命题解密］正确项［B］是对末段首句their study does not answer the question of how much businesses ought to spend on CSR的同义改写。\n"
            "［A］误认为末段③句get into trouble with the law ... costly punishment是在介绍“CSR被人们所忽视的负面影响”，而实际上该句是在说明CSR最起码的积极作用。［C］将末段①句信息“研究未能解答企业应该在CSR上投入多少”曲解为“研究高估了企业的CSR支出能力/CSR财政能力”。［D］根据末段②句词汇banking望文生义、捏造出“CSR能为银行业带来很多收益”，而实际上banking on意为“指望”，和“银行业”无关。\n"
            "［技巧总结］从原文来看，命题的陷阱在于取舍结构、倒装句、否定句等特殊句式。从选项来看，命题人通常会采用望文生义（文中取某词僻义或特殊用法，选项却用其常见含义）、断章取义（不是整体理解句子信息，而是将个别词汇糅杂到一起形成完整的语句）等方式形成干扰。本题中，根据［A］negative effect、［B］spending on、［C］financial capacity、［D］banking industry不难分别定位至③句，①句，①句，②句，但需要借助语法知识、语义逻辑、以及文章主题等才能理解到［C］曲解文意、［A］断章取义、［D］望文生义，只有［B］是对①句主要内容的同义表达。"
        )
        calibrated_count += 1
with open(p16, 'w', encoding='utf-8') as f:
    json.dump(d16, f, ensure_ascii=False, indent=2)
print("Updated 2016 ky1 Q35")

# 4. 2010 ky1 Q23, Q24, Q31
p10, d10 = load_exam(2010, 'ky1')
for q in d10['questions']:
    if q['sort_order'] == 23:
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "It is writers' duty to fulfill journalistic goals."
        calibrated_count += 1
    elif q['sort_order'] == 24:
        q['stem'] = "What can be learned about Cardus according to the last two paragraphs?"
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "His music criticism may not appeal to readers today."
            elif opt['key'] == 'B':
                opt['text'] = "His reputation as a music critic has long been in dispute."
        calibrated_count += 1
    elif q['sort_order'] == 31:
        q['stem'] = "By citing the book The Tipping Point, the author intends to"
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "discuss influentials' function in spreading ideas"
        calibrated_count += 1
with open(p10, 'w', encoding='utf-8') as f:
    json.dump(d10, f, ensure_ascii=False, indent=2)
print("Updated 2010 ky1 Q23, Q24, Q31")

# 5. 2001 ky1 Q22
p01, d01 = load_exam(2001, 'ky1')
for q in d01['questions']:
    if q['sort_order'] == 22:
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "there is little distinction between specialisation and professionalisation"
            elif opt['key'] == 'B':
                opt['text'] = "amateurs can compete with professionals in some areas of science"
            elif opt['key'] == 'C':
                opt['text'] = "professionals tend to welcome amateurs into the scientific community"
            elif opt['key'] == 'D':
                opt['text'] = "amateurs have national academic societies but no local ones"
        calibrated_count += 1
with open(p01, 'w', encoding='utf-8') as f:
    json.dump(d01, f, ensure_ascii=False, indent=2)
print("Updated 2001 ky1 Q22")

# 6. 2002 ky1 Q34
p02, d02 = load_exam(2002, 'ky1')
for q in d02['questions']:
    if q['sort_order'] == 34:
        for opt in q['options']:
            if opt['key'] == 'D':
                opt['text'] = "the price rise of crude leads to the shrinking of heavy industry"
        calibrated_count += 1
with open(p02, 'w', encoding='utf-8') as f:
    json.dump(d02, f, ensure_ascii=False, indent=2)
print("Updated 2002 ky1 Q34")

# 7. 2013 ky1 Q37 & Q39
p13, d13 = load_exam(2013, 'ky1')
for q in d13['questions']:
    if q['sort_order'] == 37:
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "Federal officers' duty to withhold immigrants' information."
            elif opt['key'] == 'C':
                opt['text'] = "States' legitimate role in immigration enforcement."
            elif opt['key'] == 'D':
                opt['text'] = "States' independence from federal immigration law."
        calibrated_count += 1
    elif q['sort_order'] == 39:
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "is dependent on the states' support"
        calibrated_count += 1
with open(p13, 'w', encoding='utf-8') as f:
    json.dump(d13, f, ensure_ascii=False, indent=2)
print("Updated 2013 ky1 Q37 & Q39")

# 8. 2014 ky1 Q21, Q28, Q37
p14, d14 = load_exam(2014, 'ky1')
for q in d14['questions']:
    if q['sort_order'] == 21:
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "encourage jobseekers' active engagement in job seeking"
            elif opt['key'] == 'C':
                opt['text'] = "guarantee jobseekers' legitimate right to benefits"
        calibrated_count += 1
    elif q['sort_order'] == 28:
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "lawyers' and clients' strong resistance"
            elif opt['key'] == 'D':
                opt['text'] = "non-professionals' sharp criticism"
        calibrated_count += 1
    elif q['sort_order'] == 37:
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "safeguard individuals' rights to education"
        calibrated_count += 1
with open(p14, 'w', encoding='utf-8') as f:
    json.dump(d14, f, ensure_ascii=False, indent=2)
print("Updated 2014 ky1 Q21, Q28, Q37")

# 9. 2015 ky1 Q23
p15, d15 = load_exam(2015, 'ky1')
for q in d15['questions']:
    if q['sort_order'] == 23:
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "Aristocrats' excessive reliance on inherited wealth."
        calibrated_count += 1
with open(p15, 'w', encoding='utf-8') as f:
    json.dump(d15, f, ensure_ascii=False, indent=2)
print("Updated 2015 ky1 Q23")

# 10. 2017 ky1 Text 2 (Q31-Q35)
p17, d17 = load_exam(2017, 'ky1')
for q in d17['questions']:
    so = q['sort_order']
    if so == 31:
        q['explanation'] = (
            "［精准定位］第一段①句引用肯尼迪对GDP的评价指出GDP衡量一切，除了那些令人生真正有价值的东西（即GDP存在巨大缺陷）。②句以英国看似不可理解的做法“明知GDP会减缓却还执意脱欧”暗证Kennedy观点正确性，并进而引出话题“是时候评定Kennedy的GDP论了”。可知，作者引用意在正向立意：GDP有极大局限性，［D］正确。\n"
            "［命题解密］正确项［D］中had a low opinion是对everything except that which makes life worthwhile“明褒实贬”态度的明确。\n"
            "［A］干扰源自第二段④句，但该句是在介绍GDP的最新计算结果，且随后一句对其进行了质疑，并非表明肯尼迪对英国GDP的赞扬。［B］将肯尼迪“认为GDP不能衡量幸福”改为与之相悖的“将GDP等同于幸福”。［C］将作者对肯尼迪观点的“赞同”改为“否定”：首段②句以及第二段④⑤句暗含作者观点“GDP不能反映实际民生状况”，即赞同肯尼迪观点。\n"
            "［技巧总结］本题就“开篇所引人物话语”设置写作目的题，间接考查“人物观点”与“文章主旨/作者观点”的关系。解题时应首先分析开篇段句际逻辑、初步得出正确项；随后借助下文进行检验、最终确定答案。需注意选项陷阱：文中特殊句式、与人物观点无直接关系的文中内容。\n"
            "具体来看，首先可发现第一段逻辑“①句介绍Kennedy观点（GDP有重大缺陷）—②句以英国脱欧事件提出应认真考量Kennedy观点”，初步确定本文开篇属于“正向援引”，目的在于借他人话语表明作者探讨对象，［D］很可能正确。再粗略浏览后文即可验证这一判断。"
        )
        calibrated_count += 1
    elif so == 32:
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = "GDP as the measure of success is widely defied in the UK"
            elif opt['key'] == 'D':
                opt['text'] = "policymakers in the UK are paying less attention to GDP"
        q['explanation'] = (
            "［精准定位］第二段④⑤句展现矛盾情形“GDP数据显示英国当前形势喜人；多数英国人却投票选择脱欧、且无视这会对其经济前景的影响”，这一情形实则暗示：GDP作为衡量一国整体发展成就的标准如今在英国广受质疑，［B］正确。\n"
            "［命题解密］［B］正确解读第二段④⑤句言外之意：GDP as the measure of success对应④句the UK's GDP has been the envy of the Western world；is widely defied in the UK对应⑤句以反问和转折表明的质疑态度（over 17 million people对应widely）。\n"
            "［A］由④句the UK's GDP has been the envy of the Western world主观推出“英国目前经济发展极好，因此不愿改变现有模式”，但⑤句实则以反问表明与之相反的信息“英国人并不认可GDP体现的表面繁荣，反而希望脱欧带来改变”。［C］由⑤句“英国经济前景很可能会受脱欧影响”过度推出“英国对世界经济的贡献将会减少”，但二者并不存在直接关联，且选项将“可能（warnings, could）”绝对化为“必然（will）”。［D］将①句“政策制定者多年来受GDP问题困扰”改为与之存在巨大偏差的“英国政策制定者当前对GDP的关注降低”，即同时偷换了时间、人物、以及人物态度。\n"
            "［技巧总结］“推理引申题”重在考查学生把握句际关系，明辨整体语义的能力。答题时需注意：①细节背后必有主旨，应抓取文字背后整体信息；②特殊句式（反问句、双重否定句、转折句式等）暗含强烈观点，需作为重要推理对象；③情感色彩词汇易成为命题人设置干扰的陷阱，需注意排除断章取义的选项。\n"
            "具体看本题，首先浏览第二段可大概抓住本段主线：质疑GDP的效用。以此为据进一步推理④⑤句，可知作者重在以反问说明英国人总体上不再信任GDP作为衡量国家是否成功的标尺，从而大致判断［B］正确。随后可进一步发现，［A］、［C］重点落在“英国经济模式”、“英国对世界经济的贡献”，与本段主线无关，且扭曲文中细节，［D］虽然涉及关注对象GDP，但严重改变文中事实，故均可排除。"
        )
        calibrated_count += 1
    elif so == 33:
        q['explanation'] = (
            "［精准定位］第三段首句针对上段末反问“英国如果真像GDP反映的那么喜人，人民为何还支持脱欧？”作出回答：最近一项年度调查提供了一些解释；随后介绍调查结果：在“经济增长-民生福祉”的转化方面，英国表现最差。第四段进而对比“富国VS穷国”情况：前者在健康、教育等方面持续下滑，后者却在民主、公平等方面提升显著。第五段作出评论：富国应吸取教训——以GDP以外的标准进行衡量，情况会大不相同。可见作者通过调查结果启示富国：“唯GDP论”掩盖国家整体发展实情（“富”未必“福”），由此解答了英国人民执意脱欧的疑问，因此［D］正确。\n"
            "［命题解密］正确项［D］enlightening是第三段首句sheds some light on的同义替换，同时与第五段a lesson that rich countries can learn相符。\n"
            "［A］将第三段②句163国家承担的角色“研究对象”偷换为“研究发起者”。［B］将第三段③句研究指标“不止包括GDP，还有其他多套不同标准”曲解为“不包括GDP”。［C］将第三段③句暗含的对研究“采取多套衡量标准”的肯定态度篡改为否定态度。\n"
            "［技巧总结］本题需要对文中大篇幅（第三至五段）涉及的大量信息（涉及研究方法，研究结论，研究细节，研究意义等）进行概括引申，难以直接确定正确答案。解题可以首先从选项入手，通过排除法锁定潜在正确项，再判断段落或段群主旨，对锁定的选项进行验证。另外需注意：与段落乃至全文核心无关联的选项为干扰项。"
        )
        calibrated_count += 1
    elif so == 34:
        q['explanation'] = (
            "［精准定位］第六段指出GDP不足以衡量国家的整体发展状况，因为它无法衡量“环境质量、教育成果”等能提升民众幸福感的重要因素。第七段则给出应对建议：政策制定者不应一味忧心GDP，而应采取实际行动、努力提升社会福利。可见，考虑GDP以外的因素极为重要，［C］正确。\n"
            "［命题解密］正确项［C］是对第六段it is no longer enough/It does not include important factors...和第七段refocus efforts on improving well-being rather than simply worrying about GDP...的概括改写。\n"
            "［A］将第七段“预测显示英国经济将因脱欧遭受重创”篡改为与之完全相悖的“英国将迎来经济繁荣”。［B］将第七段①句a decline和文中关键词high GDP之间强加因果关联：实际并非“高GDP预示经济下滑”，而是“经济打击会导致日常服务下滑，从而影响国民幸福感，只求高GDP则无法避免这一厄运”。［D］将第七段②句“要重新努力‘提升福利’而非‘忧心GDP数字’”偷换为“要谨慎处理经济问题”。\n"
            "［技巧总结］本题借作者认可之观点考查末两段主旨。解答此类题时需注意：1）否定词、否定句以及取舍关系词尤其体现文章观点，应作为重点关注对象；2）干扰项常由细节信息篡改而来或把细节信息与文章高频词杂糅而得，应予以警惕。\n"
            "具体来说，第六段完全否定词no longer，否定句it does not include明确GDP局限、暗示对“关乎民众幸福感、生活质量等民生因素”进行衡量之重要；第七段再度以取舍关系词rather than强调民生因素（well-being）的重要性及“唯GDP论”的错误性，选项［C］最为契合。［A］、［D］由细节信息篡改而来，［B］将细节信息与高频词杂糅。"
        )
        calibrated_count += 1
    elif so == 35:
        q['stem'] = "Which of the following is the best title for the text?"
        calibrated_count += 1
with open(p17, 'w', encoding='utf-8') as f:
    json.dump(d17, f, ensure_ascii=False, indent=2)
print("Updated 2017 ky1 Q31-Q35")

# 11. 2019 ky1 Text 4 (Q36-Q40)
p19, d19 = load_exam(2019, 'ky1')
for q in d19['questions']:
    so = q['sort_order']
    if so == 36:
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "better businesses' relations with states"
            elif opt['key'] == 'D':
                opt['text'] = "force some states to cut sales tax"
        q['explanation'] = (
            "［精准定位］开篇段指出，最高法院周四裁定各州可强制更多的人为在线购物支付销售税，［C］正确。\n"
            "［命题解密］正确项［C］是对第一段more people to pay sales tax when they make online purchases的同义改写。\n"
            "［A］利用“裁定使各州有权（责令企业为它们）收取销售税”所隐含的“企业将增加与各州的联系”错误推断出“企业与各州之间关系会改善”，但双方单纯是命令的发布者与命令的执行者，裁定无关双方关系的改善（抑或恶化）。［B］将第二段中新裁定的影响范围“某些网购商品（certain online purchases）”篡改为“大多数在线商家（most online businesses）”，并捏造出新裁定“使他们陷入困境”的说法。［D］与“裁定使各州有权对更多网购商品征收销售税（即扩大销售税征收范围）”相悖。\n"
            "［技巧总结］首段一方面是长难句，另一方面又是对全文的高度概括，所以很容易成为命题点。解答本题时，可在锁定本题答案来源的基础上，从语法结构和语义逻辑角度分析长难句，并与选项对比后得出答案。\n"
            "具体来看，首段长句由States will be able to...及under a Supreme Court decision Thursday that...构成，前半部分指出各州可对更多的在线购物强制推行销售税；后半部分指出最高法院的裁定让消费者的钱流入各州财政。因此本题题干+答案应能体现“最高法院裁定—州政府—在线消费者”的逻辑，而题干给出的信息是“最高法院裁定”，那么答案应能表明州政府与在线消费者之间的联系（政府让消费者交税）；通读选项后即可确定答案为［C］。"
        )
        calibrated_count += 1
    elif so == 37:
        q['stem'] = "It can be learned from paragraphs 2 and 3 that the overruled decisions"
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "have led to the dominance of e-commerce"
            elif opt['key'] == 'B':
                opt['text'] = "have cost consumers a lot over the years"
            elif opt['key'] == 'C':
                opt['text'] = "were widely criticized by online purchasers"
            elif opt['key'] == 'D':
                opt['text'] = "were considered unfavorable by states"
        q['explanation'] = (
            "［精准定位］第二段首先指出，各州称遭到推翻的两起裁定每年都给他们带来巨额损失，加大了对某些网购商品的销售税征收难度。第三段具体说明州政府财政如何损失：原裁定导致未在本州设立实体存在的州外商家无需为本州代收销售税，而原则上需要交税的消费者也很少自行缴纳。由此可知，各州认为原裁定对他们不利，［D］正确。\n"
            "［命题解密］正确项［D］与第二段①句中的...states said cost them billions of dollars in lost revenue annually直接对应。\n"
            "［A］将“原裁定加大对某些网购商品的销售税征收难度”蕴含的“某些电商（线上商家）得利”偷换为“电子商务取得了主导地位”，而文中并未对不同商务模式的市场地位进行比较，“主导地位”纯属无中生有。［B］、［C］的干扰均源于第三段②句“大多数消费者不知道自己欠税，上缴销售税的消费者也很少”，但前者与“大多数消费者实际得利”相悖，后者将“大多数消费者未自行缴税”错误地归结为“他们对原裁定不满并广泛批评”。\n"
            "［技巧总结］本题就“同一事件对不同主体的影响”命制事实细节题。解题可结合“从文章出发明确事件影响”和“从选项出发明确各主体所受影响”两个方向。具体来看：第二段介绍被推翻的裁定给各州带来财政损失；第三段说明被推翻的裁定认为在本州没有实体存在的商家不用代收销售税，而消费者对需要自交销售税大多不知情且很少人交。因此，被推翻的裁定对各州不利、对某些商家及消费者有利，初步排除［B］、［C］，并确定［D］正确。而剩下的［A］涉及“电子商务”，其特点“占据主导地位”在文中没有提到，因此同样排除。"
        )
        calibrated_count += 1
    elif so == 38:
        q['stem'] = "According to Justice Anthony Kennedy, the physical presence rule has"
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "hindered economic development"
            elif opt['key'] == 'B':
                opt['text'] = "brought prosperity to the country"
            elif opt['key'] == 'C':
                opt['text'] = "harmed fair market competition"
            elif opt['key'] == 'D':
                opt['text'] = "boosted growth in states' revenue"
        q['explanation'] = (
            "［精准定位］第四段②句指出，实体存在规则脱离经济现实，使各州蒙受巨额收入损失；③句进一步指出它使市场参与者无法在公平的环境下展开竞争，［C］正确。\n"
            "［命题解密］正确项［C］是对has prevented market participants from competing on an even playing field的同义改写。\n"
            "［A］将实体存在规则“使各州蒙受巨额财政损失”曲解为它“阻碍了经济发展”，但原文讨论的是各州“税收收入（sales tax, revenue）”而非整体“经济发展（economic development）”。［B］、［D］分别与第四段②句和③句实体存在规则“限制了各州寻求长久繁荣的能力”及“使各州蒙受巨额收入损失”相悖。\n"
            "［技巧总结］本题针对人物观点命制事实细节题，解题关键在于准确定位、把握观点核心；同时需要避开曲解观点（如过度推断、反向干扰）、张冠李戴等常见干扰形式。具体来看，第四段是肯尼迪大法官观点的集中体现：①句总述原裁定有缺陷，②③句具体阐述缺陷，即实体存在规则（原裁定）的问题所在，因此首先可排除两个显然带有正面含义的选项［B］、［D］（属于反向干扰）；经过与原文的比对后可进一步排除曲解文意的［A］，并最终确定［C］为正确答案。"
        )
        calibrated_count += 1
    elif so == 39:
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "Internet entrepreneurs."
            elif opt['key'] == 'B':
                opt['text'] = "Big-chain owners."
            elif opt['key'] == 'C':
                opt['text'] = "Third-party sellers."
            elif opt['key'] == 'D':
                opt['text'] = "Small retailers."
        q['explanation'] = (
            "［精准定位］第五段①句指出，本次裁定对在多州设有实体机构的大型连锁店而言是一次胜利，所以最有可能欢迎此次裁定的应该是大型连锁店店主，［B］正确。\n"
            "［命题解密］正确项［B］Big-chain owners与第五段①句big chains所指相同，句中a victory体现出新裁定给他们带来的巨大利好，因此他们应该最欢迎（welcome）此次裁定。\n"
            "［A］与第七段④句“互联网企业家完全没有受到本次裁定的周全考虑”相悖。［C］、［D］与第五段④句和第六段②句“第三方商家和小型零售商原本无需代收销售税，而此次裁定迫使他们开始收税”所暗示的“不会欢迎本次裁定”相悖。\n"
            "［技巧总结］题干设问句表明，本题是就“事件对各方影响”设置的事实判断题，解题关键在于准确定位各方受到的影响。具体来看，对第五、六段描述各类商家所受影响可定位如下：第五段①句明确指出新裁定对大型连锁店而言是胜利（a victory for big chains with a presence in many states）；第六段③句指出，根据新裁定，各州可立法强制要求州外商家（包括第三方卖家和小型零售商）开始代收销售税（requiring out-of-state sellers to collect the state's sales tax from customers），由此排除［C］、［D］并初步确定［B］为答案。最后，根据末段信息“互联网企业家没有受到本次裁定的周全考虑（internet entrepreneurs are not well served at all by this decision）”排除［A］。"
        )
        calibrated_count += 1
    elif so == 40:
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "gives a factual account of it and discusses its consequences"
            elif opt['key'] == 'B':
                opt['text'] = "describes the long and complicated process of its making"
            elif opt['key'] == 'C':
                opt['text'] = "presents its main points with conflicting views on them"
            elif opt['key'] == 'D':
                opt['text'] = "cites some cases related to it and analyzes their implications"
        q['explanation'] = (
            "［精准定位］本文首段概述事件：最高法院裁定各州可对在线购物征收销售税。第二至四段对新裁定的来龙去脉进行客观描述，包括其推翻的原裁定内容及推翻的原因。第五至七段介绍了新裁定对各类商家的影响及他们的反应。由此可见，［A］正确。\n"
            "［命题解密］正确项［A］体现文章“概述事件—详述事件—说明影响”的整体结构。\n"
            "［B］把第三、四段对原裁定的回溯及其缺陷的分析曲解为新裁定的形成过程，但本文并未介绍新裁定形成前所经历的复杂司法程序；另外，该选项完全没有涉及第五至七段关于新裁定影响的论述。［C］利用末段不同团体（零售贸易团体和在线零售商）对裁定的不同反应干扰，但显然无力概括全文。［D］源于第三段①句The cases the court overturned，但文中是为了分析原裁定的缺陷，从而说明做出新裁定的必要性，而非列举相关案例；另外，本文第五至七段分析的是新裁定的影响，而非其他案件的影响。\n"
            "［技巧总结］本题与2018年Text 1最后一题相似，同样考查全篇论证结构，考生需站在全文高度抓取文章主线，切忌囿于个别段内容。具体来看，题干中的the Supreme Court decision Thursday提示它是全文关注核心，答案应体现文章如何围绕它展开论述。根据第二至四段的事实细节及第五至七段的事件影响及各方反应可确定［A］为答案。同时结合排除法确保答案正确：文中并不涉及本次裁定的形成过程（大法官内部争论），排除［B］；并无针对裁定结果本身的观点交锋，排除［C］；并无案件引述，排除［D］。"
        )
        calibrated_count += 1
with open(p19, 'w', encoding='utf-8') as f:
    json.dump(d19, f, ensure_ascii=False, indent=2)
print("Updated 2019 ky1 Q36-Q40")

print(f"\nTotal calibrated questions across all exams: {calibrated_count}")
