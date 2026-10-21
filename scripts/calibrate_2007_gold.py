import json
import re

json_path = 'public/data/exams/e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json'

with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

print("Starting forensic calibration for 2007 ky1...")

# 1. Calibrate Exam Title if needed
exam_data['exam']['title'] = "2007年全国硕士研究生入学统一考试英语（一）真题"

# 2. Reconstruct Passages 0 to 5
p0_clean = """By 1830 the former Spanish and Portuguese colonies had become independent nations. The roughly 20 million [1] of these nations looked [2] to the future. Born in the crisis of the old regime and Iberian colonialism, many of the leaders of independence [3] the ideals of representative government, careers [4] to talent, freedom of commerce and trade, the [5] to private property, and a belief in the individual as the basis of society. [6] there was a belief that the new nations should be sovereign and independent states, large enough to be economically viable and integrated by a [7] set of laws.

On the issue of [8] of religion and the position of the Church, [9], there was less agreement [10] the leadership. Roman Catholicism had been the state religion and the only one [11] by the Spanish crown. [12] most leaders sought to maintain Catholicism [13] the official religion of the new states, some sought to end the [14] of other faiths. The defense of the Church became a rallying [15] for the conservative forces.

The ideals of the early leaders of independence were often egalitarian, valuing equality of everything. Bolivar had received aid from Haiti and had [16] in return to abolish slavery in the areas he liberated. By 1854 slavery had been abolished everywhere except Spain's [17] colonies.

Early promises to end Indian tribute and taxes on people of mixed origin came much [18] because the new nations still needed the revenue such policies [19]. Egalitarian sentiments were often tempered by fears that the mass of the population was [20] self-rule and democracy."""

p1_clean = """If you were to examine the birth certificates of every soccer player in 2006's World Cup tournament, you would most likely find a noteworthy quirk: elite soccer players are more likely to have been born in the earlier months of the year than in the later months. If you then examined the European national youth teams that feed the World Cup and professional ranks, you would find this strange phenomenon to be even more pronounced.

What might account for this strange phenomenon? Here are a few guesses: a) certain astrological signs confer superior soccer skills; b) winter-born babies tend to have higher oxygen capacity, which increases soccer stamina; c) soccer-mad parents are more likely to conceive children in springtime, at the annual peak of soccer mania; d) none of the above. Anders Ericsson, a 58-year-old psychology professor at Florida State University, says he believes strongly in "none of the above."

Ericsson grew up in Sweden, and studied nuclear engineering until he realized he would have more opportunity to conduct his own research if he switched to psychology. His first experiment, nearly 30 years ago, involved memory: training a person to hear and then repeat a random series of numbers. "With the first subject, after about 20 hours of training, his digit span had risen from 7 to 20," Ericsson recalls. "He kept improving, and after about 200 hours of training he had risen to over 80 numbers."

This success, coupled with later research showing that memory itself is not genetically determined, led Ericsson to conclude that the act of memorizing is more of a cognitive exercise than an intuitive one. In other words, whatever inborn differences two people may exhibit in their abilities to memorize, those differences are swamped by how well each person "encodes" the information. And the best way to learn how to encode information meaningfully, Ericsson determined, was a process known as deliberate practice. Deliberate practice entails more than simply repeating a task. Rather, it involves setting specific goals, obtaining immediate feedback and concentrating as much on technique as on outcome.

Ericsson and his colleagues have thus taken to studying expert performers in a wide range of pursuits, including soccer. They gather all the data they can, not just performance statistics and biographical details but also the results of their own laboratory experiments with high achievers. Their work makes a rather startling assertion: the trait we commonly call talent is highly overrated. Or, put another way, expert performers—whether in memory or surgery, ballet or computer programming—are nearly always made, not born."""

p2_clean = """For the past several years, the Sunday newspaper supplement Parade has featured a column called "Ask Marilyn." People are invited to query Marilyn vos Savant, who at age 10 had tested at a mental level of someone about 23 years old; that gave her an IQ of 228, the highest score ever recorded. IQ tests ask you to complete verbal and visual analogies, to envision paper after it has been folded and cut, and to deduce numerical sequences, among other similar tasks. So it is a bit confusing when vos Savant fields such queries from the average Joe (whose IQ is 100) as, What's the difference between love and fondness? Or what is the nature of luck and coincidence? It's not obvious how the capacity to visualize objects and to figure out numerical patterns suits one to answer questions that have eluded some of the best poets and philosophers.

Clearly, intelligence encompasses more than a score on a test. Just what does it mean to be smart? How much of intelligence can be specified, and how much can we learn about it from neurology, genetics, computer science and other fields?

The defining term of intelligence in humans still seems to be the IQ score, even though IQ tests are not given as often as they used to be. The test comes primarily in two forms: the Stanford-Binet Intelligence Scale and the Wechsler Adult Intelligence Scale (both have children's versions). Generally costing several hundred dollars, they are usually given only by psychologists, although variations of them populate bookstores and the World Wide Web. Superhigh scores like vos Savant's are no longer possible, because scoring is now based on a statistical population distribution among age peers, rather than simply dividing the mental age by the chronological age and multiplying by 100. Other standardized tests, such as the Scholastic Assessment Test (SAT) and the Graduate Record Exam (GRE), capture the main aspects of IQ tests.

Such standardized tests may not assess all the important elements necessary to succeed in school and in life, argues Robert J. Sternberg. In his article "How Intelligent Is Intelligence Testing?", Sternberg notes that traditional tests best assess analytical and verbal skills but fail to measure creativity and practical knowledge, components also critical to problem solving and life success.

Moreover, IQ tests do not necessarily predict so well once populations or situations change. Research has found that IQ predicted leadership skills when the tests were given under low-stress conditions, but under high-stress conditions, IQ was negatively correlated with leadership—that is, it predicted the opposite. Anyone who has toiled through SAT will testify that test-taking skill also matters, whether it's knowing when to guess or what questions to skip."""

p3_clean = """During the past generation, the American middle-class family that once could count on hard work and fair play to keep itself financially secure has been transformed by economic risk and new realities. Now a pink slip, a bad diagnosis, or a disappearing spouse can reduce a family from solidly middle class to newly poor in a few months.

In just one generation, millions of mothers have gone to work, transforming basic family economics. Scholars, policymakers, and critics of all stripes have debated the social implications of these changes, but few have looked at the side effect: family risk has risen as well. Today's families have budgeted to the limits of their new two-paycheck status. As a result, they have lost the parachute they once had in times of financial setback—a back-up earner (usually Mom) who could go into the workforce if the primary earner got laid off or fell sick. This "added worker effect" could support the safety net offered by unemployment insurance or disability insurance to help families weather bad times. But today, with both parents already in the workforce, a disruption to family fortunes can no longer be made up with extra hours or an outside job.

During the same period, families have been asked to absorb much more risk in their retirement income. Steelworkers, airline employees, and now those in the auto industry are joining millions of families who must worry about interest rates, stock market fluctuation, and the harsh reality that they may outlive their retirement money. For much of the past year, President Bush campaigned to move Social Security to a savings-account model, with retirees trading much or all of their guaranteed payments for payments depending on investment returns. For younger families, the picture is not any better. Both the absolute cost of healthcare and the share of it borne by families have risen—and newly fashionable health-savings plans are spreading from legislative halls to Wal-Mart workers, with much higher deductibles and a large new dose of investment risk for families' future healthcare. Even demographics are working against the middle-class family, as the odds of having a weak elderly parent—and all the attendant need for physical and financial assistance—have jumped eightfold in just one generation.

From the middle-class family perspective, much of this, understandably, looks far less like an opportunity to exercise more financial responsibility, and a good deal more like a frightening acceleration of the wholesale shift of financial risk onto their already overburdened shoulders. The financial fallout has begun, and the political fallout may not be far behind."""

p4_clean = """It never rains but it pours. Just as bosses and boards have finally sorted out their worst accounting and compliance troubles, and improved their feeble corporation governance, a new problem threatens to earn them—especially in America—the sort of nasty headlines that inevitably lead to heads rolling in the executive suite: data insecurity. Left, until now, to odd, low-level IT staff to put right, and seen as a concern only of data-rich industries such as banking, telecoms and air travel, information protection is now high on the boss's agenda in businesses of every variety.

The scramble to organize security checks was sparked by massive leakages of customer and employee data this year—from organizations as diverse as Time Warner, the American defense contractor Science Applications International Corp. and the card processor CardSystems Solutions. These have left managers hurriedly peering into their own IT systems in search of potential vulnerabilities.

"Data is becoming an asset which needs to be guarded as much as any other asset," says Haim Mendelson of Stanford University's business school. "The ability to guard customer data is the key to market value, which the board is responsible for on behalf of shareholders." Indeed, just as there is the concept of Generally Accepted Accounting Principles (GAAP), perhaps it is time for GASP, Generally Accepted Security Practices, suggested Eli Noam of New York's Columbia Business School. "Setting the proper investment level for security, redundancy, and recovery is a management issue, not a technical one," he says.

The mystery is that this should come as a surprise to any boss. Surely it should be obvious to even the dimmest executive that trust, that most valuable of economic assets, is easily destroyed and hugely expensive to restore—and that few things are more likely to destroy trust than a company letting sensitive personal data get into the wrong hands.

The current state of affairs may have been encouraged—though not justified—by the lack of legal penalty (in America, but not Europe) for data leakage. Until California recently passed a law, American firms did not have to tell anyone, even the victim, when data went astray. That may change fast: lots of proposed data security legislation is now doing the rounds in Washington, D.C. Meanwhile, the theft of information about some 40 million credit-card accounts in America, disclosed on June 17th, overshadowed a hugely important decision a day earlier by America's Federal Trade Commission (FTC) that puts corporate America on notice that regulators will act if firms fail to provide adequate data security."""

p5_clean = """How Can a Parent Help?

Mothers and fathers can do a lot to ensure a safe landing in early adulthood for their kids. Even if a job's starting salary seems too small to satisfy an emerging adult's need for rapid content, the transition from school to work can be less of a setback if the start-up adult is ready for the move. Here are a few measures, drawn from my book Ready or Not, Here Life Comes, that parents can take to prevent what I call "work-life unreadiness":

[41] ____________________ You can start this process when they are 11 or 12. Periodically review their emerging strengths and weaknesses with them and work together on any shortcomings, like difficulty in communicating well or collaborating. Also, identify the kinds of interests they keep coming back to, as these offer clues to the careers that will fit them best.

[42] ____________________ Kids need a range of authentic role models—as opposed to members of their clique, pop stars and vaunted athletes. Have regular dinner-table discussions about people the family knows and how they got where they are. Discuss the joys and downsides of your own career and encourage your kids to form some ideas about their own future. When asked what they want to do, they should be discouraged from saying "I have no idea." They can change their minds 200 times, but having only a foggy view of the future is of little good.

[43] ____________________ Teachers are responsible for teaching kids how to learn; parents should be responsible for teaching them how to work. Assign responsibilities around the house and make sure homework deadlines are met. Encourage teenagers to take a part-time job. Kids need plenty of practice delaying gratification and deploying effective organizational skills, such as managing time and setting priorities.

[44] ____________________ Playing video games encourages immediate content. And hours of watching TV shows with canned laughter only teaches kids to process information in a passive way. At the same time, listening through earphones to the same monotonous beats for long stretches encourages kids to stay inside their bubble instead of pursuing other endeavors. All these activities can prevent the growth of important communication and thinking skills and make it difficult for kids to develop the kind of sustained concentration they will need for most jobs.

[45] ____________________ They should know how to deal with setbacks, stresses and feelings of inadequacy. They should also learn how to solve problems and resolve conflicts, ways to brainstorm and think critically. Discussions at home can help kids practice doing these things and help them apply these skills to everyday life situations."""

passages_meta = [
    (p0_clean, 'cloze', 1),
    (p1_clean, 'reading', 1),
    (p2_clean, 'reading', 2),
    (p3_clean, 'reading', 3),
    (p4_clean, 'reading', 4),
    (p5_clean, 'reading_part_b', 5)
]

for idx, (content, p_type, p_num) in enumerate(passages_meta):
    exam_data['passages'][idx]['content'] = content
    exam_data['passages'][idx]['type'] = p_type
    exam_data['passages'][idx]['passage_number'] = p_num

print("Passages updated.")

# 3. Calibrate Questions
stems_map = {
    21: "The birthday phenomenon found among soccer players is mentioned to ________.",
    22: 'The word "mania" (Line 4, Paragraph 2) most probably means ________.',
    23: "According to Ericsson, good memory ________.",
    24: "Ericsson and his colleagues believe that ________.",
    25: "Which of the following proverbs is closest to the message the text tries to convey?",
    26: "Which of the following may be required in an intelligence test?",
    27: "What can be inferred about intelligence testing from Paragraph 3?",
    28: "People nowadays can no longer achieve IQ scores as high as vos Savant's because ________.",
    29: "We can conclude from the last paragraph that ________.",
    30: "What is the author's attitude towards IQ tests?",
    31: "Today's double-income families are at greater financial risk in that ________.",
    32: "As a result of President Bush's reform, retired people may have ________.",
    33: "According to the author, health-savings plans will ________.",
    34: "It can be inferred from the last paragraph that ________.",
    35: "Which of the following is the best title for this text?",
    36: 'The statement "It never rains but it pours" is used to introduce ________.',
    37: "According to Paragraph 2, some organizations check their systems to find out ________.",
    38: "In bringing up the concept of GASP the author is making the point that ________.",
    39: "According to Paragraph 4, what puzzles the author is that some bosses fail to ________.",
    40: "It can be inferred from Paragraph 5 that ________."
}

# Explanations for Q32, Q37, Q38, Q41-Q45
q32_gold_exp = """［精准定位］由题干关键词 President Bush's reform 和 retired people 定位至第三段③句。该句的 with 结构指出布什改革的后果：退休人员的大部分或全部有保障的收入变成了依赖投资收益的收入，可见［B］符合文意。
［命题解密］正确项［B］是对第三段③句 with retirees trading much or all of their guaranteed payments for payments depending on investment returns 的高度概括。
［错项排除］［A］a higher sense of security 利用第三段①句 have been asked to absorb much more risk 反向干扰，但布什改革是“人们承担更多风险”的“推进力量”而非“对抗力量”，故选项完全错误。［C］将③句内容“改革将人们的退休收入变成了要依靠投资收益，即退休收入成了一种投资”改为与之相悖的“改革使退休人员投资机会减少”。［D］颠倒前后变化，将第三段③句 trading... their guaranteed payments for... 所表明的“布什改革前情形——（尚有部分）退休金是有保障的收入”改为“布什改革的结果——退休者有一个有保障的将来”，实际上，改革之后退休人员的未来没有了保障。
［技巧总结］本题针对长难句中涉及的因果关系设题。考生需注意：①清晰划分句群，理解所考句和上下文的关系，并关注词汇褒贬色彩、把握作者基本态度；②正确解读长难句，理清句中逻辑关系。"""

q37_gold_exp = """［精准定位］第二段明确指出，数起严重数据泄露事件使得公司管理层急忙检查自身的信息系统以寻找潜在的薄弱点。［A］选项正确。
［命题解密］题干 to find out ＋正确项［A］是对破折号后内容 in search of potential vulnerabilities 的同义表述。
［错项排除］［B］将“查找漏洞以便做好防范”篡改为“找出已经失窃的数据”。［C］将段中泛指各公司管理人员的 managers 曲解为特指几起数据泄露事件所涉公司管理人员；并将“寻找可能性漏洞”偷换为“确定事件责任人”。［D］把段中 peering into... in search of potential vulnerabilities 过度推断成“寻找间谍嫌疑人”，大幅偏离文意。
［技巧总结］本题看似考查事实细节，实则考查长难句的句意。解答关键在紧抓句子主干、捕捉关键信息。细观独句成段的第二段，发现关键信息在破折号后内容（即谓宾部分），而仔细比对题干＋选项发现，题目考查“管理人员检测自身系统的目的（to find out）”，正好对应目的标识词 in search of，由此断定［A］正确。"""

q38_gold_exp = """［精准定位］第三段①④句引用专家观点“应建立数据信息保护管理规则”旨在说明“数据信息保护至关重要，应予以足够重视”，［B］正确。
［命题解密］正确项［B］是对第三段 Data is becoming an asset... it is time for GASP... Setting the proper investment level for security, redundancy, and recovery is a management issue 所述观点的合理概括。
［错项排除］［A］将②句 the board is responsible for on behalf of shareholders 旨在说明的“为了股东利益，董事会有责任保护客户数据信息以保证市场价值”就事论事为“股东利益应得到适当维护”。［C］将文意“以 GAAP 类比引出 GASP”反向偷换为“引入 GASP 是为了说明 GAAP 的相关内容——公司应提高自身财会安全水平”。［D］首先将原文意在强调“保护客户数据”偷换为“市场价值”，其次将文意提及市场价值旨在说明“数据信息保护的重要性”偷换为“市场价值的重要性”。
［技巧总结］本题实质借写作目的之形考查段落主旨。解答此类题时，考生可由内向外逐层分析：一、首先锁定题干部分所在句，弄清其含义；二、随后寻找上下文与其关联最为紧密的语句，并整合成意群加以理解；三、最后从段落的宏观角度明确该意群与段落其他部分间的逻辑关联，提取段落的主旨观点。"""

q41_gold_exp = """［标题匹配］第二段指出，父母应帮助孩子了解自身优缺点并一起克服缺点，以此发现孩子的兴趣所在，为未来的职业做准备，也即父母应着重引导孩子正确认识自我、了解自身特点，［F］“帮助孩子弄清楚他们是谁，即帮助孩子认清自我”与该主旨相符，标题主题词 figure out 与段落关键词 identify 近义。
［干扰项排除］［D］Talk about the Future on a Regular Basis 虽与文中部分信息 Periodically review / careers 有所重叠，但文中“寻找未来职业”是家长采取某些措施的目的，并非措施本身，这些措施并未涉及“谈论未来”，故排除。"""

q42_gold_exp = """［标题匹配］第三段指出，父母应通过经常谈论孩子身边真实榜样的事迹，包括外人的成就和家长的职业生涯，引导孩子对自己的未来进行设想和规划，关键词 Have regular dinner-table discussions 强调这种“涉及未来”的对话应是经常性的、定期的。［D］“经常讨论未来”契合本段主旨。
［干扰项排除］［A］Set a Good Example for Your Kids 虽然复现首句 role models 一词，且段落前三句均围绕“榜样”展开，但“孩子树立榜样”的目的是“通过参照这些榜样的事迹来规划自身的未来”，也即“树立榜样”是“规划未来”的一种辅助方式，并非重点，故排除。"""

q43_gold_exp = """［标题匹配］第四段意在提醒家长通过有意识的布置家务活、鼓励孩子做兼职来培养孩子基本的工作技能，首句“家长应教孩子如何工作”（how to work）为主旨句，［B］“培养孩子工作技能”与该主旨一致。
［干扰项排除］［G］Build Your Kids' Sense of Responsibility 虽然复现段中 responsibility 一词，但首句提及该词是为了说明“教师和家长对孩子的责任”，并非“孩子的责任感”；第二句提及该词是为了说明“家长可通过给孩子布置家务活来培养工作技能”，也与“孩子的责任感”无关，故排除。"""

q44_gold_exp = """［标题匹配］第五段无主旨句，亦未涉及家长的内容，而是以长时间玩乐活动对孩子造成危害来侧面提醒家长应进行干预：控制孩子的娱乐时长，［C］“对娱乐活动时间加以控制”符合本段主旨，其中 Leisure Activities 总结概括 Playing... / watching... / listening... 等活动，Place Time Limits 由文中的 hours of / long stretches 反向引申而来。
［干扰项排除］［B］的主题词 Work Skills 虽与段末提及的“工作所需的能力，如交流和思考能力、持续注意力”相关联，但“工作能力”仅是细枝末节，选项遗漏重要信息“长时间娱乐活动及其危害”，故排除。"""

q45_gold_exp = """［标题匹配］第六段①句涉及家长应采取的措施“组织家庭讨论”，但“讨论的内容和讨论的目的”模糊不清，还需结合前两句总结得出讨论的目的；前两句关键词 deal with / solve / resolve 表明家长应帮助孩子培养和运用“应对问题”的能力，故家长应通过组织家庭讨论这种形式来重点帮助孩子培养应对问题的能力，［E］“帮助孩子制定应对策略”与之相符，Coping Strategies 是对前两句内容的概括。
［干扰项排除］［B］中 Work Skills 可能会被误解为本段末句 these skills 的具体指代，但上文所述的几种能力“应对挫折、压力，解决问题、冲突等”不一定是工作技能，在生活中也适用，［B］以偏概全。"""

for i in range(len(exam_data['questions'])):
    q_num = i + 1
    q = exam_data['questions'][i]
    q['question_number'] = q_num
    
    # Stem calibration
    if q_num <= 20:
        q['stem'] = f"Choose the best option for blank [{q_num}] in the passage:"
    elif q_num in stems_map:
        q['stem'] = stems_map[q_num]
    elif 41 <= q_num <= 45:
        q['stem'] = f"Choose the best heading [A]-[G] for paragraph ({q_num}):"
        
    # Option text cleaning
    for opt in q.get('options', []):
        opt_text = opt.get('text', '')
        if q_num == 1 and opt.get('key') == 'A':
            opt['text'] = 'natives'
        elif q_num == 25:
            opt['text'] = opt_text.replace('“', '"').replace('”', '"').replace('', '"')
        elif q_num == 26 and opt.get('key') == 'A':
            opt['text'] = 'Answering philosophical questions.'
        elif q_num == 31 and opt.get('key') == 'B':
            opt['text'] = 'their chances of being laid off have greatly increased'
        elif q_num == 33 and opt.get('key') == 'D':
            opt['text'] = "increase the families' investment risk"
        elif q_num == 39 and opt.get('key') == 'B':
            opt['text'] = 'perceive the sensitivity of personal data'
            
    # Explanation cleaning & gold replacement
    if q_num == 32:
        q['explanation'] = q32_gold_exp
    elif q_num == 37:
        q['explanation'] = q37_gold_exp
    elif q_num == 38:
        q['explanation'] = q38_gold_exp
    elif q_num == 41:
        q['explanation'] = q41_gold_exp
    elif q_num == 42:
        q['explanation'] = q42_gold_exp
    elif q_num == 43:
        q['explanation'] = q43_gold_exp
    elif q_num == 44:
        q['explanation'] = q44_gold_exp
    elif q_num == 45:
        q['explanation'] = q45_gold_exp
    elif 21 <= q_num <= 40:
        # Strip header garbage before ［精准定位］ or ［命题解密］
        exp = q.get('explanation', '')
        pos = -1
        for marker in ['［精准定位］', '［命题解密］', '［解题思路］', '【精准定位】', '【命题解密】', '【解题思路】']:
            p = exp.find(marker)
            if p != -1:
                if pos == -1 or p < pos:
                    pos = p
        if pos > 0:
            q['explanation'] = exp[pos:].strip()

print("Questions calibrated.")

# Save calibrated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"Calibrated 2007 JSON successfully written to {json_path}")
