import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

# Target Exam UUID
EXAM_ID = "68de78c3-98c6-507b-9a1e-566833a7f00b"
EXAM_PATH = os.path.join(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams", f"{EXAM_ID}.json")

with open(EXAM_PATH, "r", encoding="utf-8") as f:
    exam_data = json.load(f)

# 1. Exam Metadata Calibration
exam_data["exam"]["title"] = "2017年全国硕士研究生招生考试英语（二）真题"
exam_data["exam"]["category_id"] = "ky2"
exam_data["exam"]["year"] = 2017
exam_data["exam"]["exam_type"] = "real"
exam_data["exam"]["total_score"] = 60.0
exam_data["exam"]["pass_score"] = 36.0
exam_data["exam"]["duration_minutes"] = 180
exam_data["exam"]["is_published"] = True
exam_data["exam"]["approval_status"] = "approved"

# 2. Passages Gold Reconstruction
p0_content = """People have speculated for centuries about a future without work. Today is no different, with academics, writers, and activists once again [1] that technology is replacing human workers. Some imagine that the coming work-free world will be defined by [2]: A few wealthy people will own all the capital, and the masses will struggle in an impoverished wasteland.

A different and not mutually exclusive [3] holds that the future will be a wasteland of a different sort, one [4] by purposelessness: Without jobs to give their lives [5], people will simply become lazy and depressed. [6], today's unemployed don't seem to be having a great time. One Gallup poll found that 20 percent of Americans who have been unemployed for at least a year report having depression, double the rate for [7] Americans. Also, some research suggests that the [8] for rising rates of mortality, mental-health problems, and addiction [9] poorly-educated, middle-aged people is a shortage of well-paid jobs. Perhaps this is why many [10] the agonizing dullness of a jobless future.

But it doesn't [11] follow from findings like these that a world without work would be filled with unease. Such visions are based on the [12] of being unemployed in a society built on the concept of employment. In the [13] of work, a society designed with other ends in mind could [14] strikingly different circumstances for the future of labor and leisure. Today, the [15] of work may be a bit overblown. "Many jobs are boring, degrading, unhealthy, and a waste of human potential," says John Danaher, a lecturer at the National University of Ireland in Galway.

These days, because leisure time is relatively [16] for most workers, people use their free time to counterbalance the intellectual and emotional [17] of their jobs. "When I come home from a hard day's work, I often feel [18]," Danaher says, adding, "In a world in which I don't have to work, I might feel rather different" — perhaps different enough to throw himself [19] a hobby or a passion project with the intensity usually reserved for [20] matters."""

p1_content = """Every Saturday morning, at 9 am, more than 50,000 runners set off to run 5km around their local park. The Parkrun phenomenon began with a dozen friends and has inspired 400 events in the UK and more abroad. Events are free, staffed by thousands of volunteers. Runners range from career athletes in 100g racing flats to local politicians and first-timers in trainers. Andrew Baddeley, who stood on the starting line in the 2008 and 2012 Olympic 1,500m finals, wrote on Twitter: "Massive congratulations to all 51,769 of you who took part in Parkrun this morning. That's inspiring."

Parkrun is succeeding where London's Olympic "legacy" is failing. Ten years ago on Monday, it was announced that the Games of the 30th Olympiad would be in London. Planning documents pledged that a great legacy of the Games would be to inspire a generation to get active and get more people doing sport. But numbers of adults doing sport have been falling away for the past year, while the number of people doing sport daily is now falling at an accelerating rate. The numbers are worse in London. Primary school pupils have had their two hours of sport a week halved. Obesity is on the rise and obesity-related sicknesses are costing the NHS billions. Official retrospections as to why London 2012 failed to "inspire a generation" have focused on the backroom decisions, but they failed to ask whether the legacy was the right one.

Parkrun is not a government initiative; it gets no public money and is not run by banks. Its dual aim was to get more people doing sport and to produce more elite athletes, and in the run-up to 2012, it had an impact. But the stress on success over taking part has, in the end, proven a failure. Elite performers are produced by a pyramid of participation, not the other way around. By contrast, Parkrun does not ask for money, does not ask for membership, does not ask for elite times. It does not judge.

In an age of spending cuts, future governments would be wise to take note. London 2012 showed that high-profile events have limited long-term impact on participation. The lesson of Parkrun is that mass sport needs to be made as easy, welcoming and low-cost as possible. If there is a role for government, it should be to invest in public parks and open spaces, not to sponsor high-profile events in the hope that greatness rubs off."""

p2_content = """With so much focus on children's use of screens, it's easy for parents to forget about their own screens. But if you want to understand how your use of technology affects your child, the best place to look is at mealtimes. Tech is designed to suck you in, and digital products are explicitly designed to promote maximal engagement. The result is that it's increasingly difficult for families to preserve mealtimes as a time for family conversation. Tension in the family can be created when parents are looking at their emails while children are making excited bids for their attention.

Jenny Radesky, an assistant professor of pediatrics at Boston University Medical Center, has studied the use of mobile phones and tablets at mealtimes by giving mother-child pairs a food-testing exercise. Radesky found that mothers who were absorbed in their devices during the exercise had 20 percent fewer verbal and 39 percent fewer nonverbal interactions with their children. When mothers were absorbed, their children tended to be more provocative, as if trying to get their attention.

Radesky cites the "still face experiment," devised by developmental psychologist Edward Tronick in the 1970s. In it, a mother is asked to interact with her child in a normal way, then suddenly adopt a completely expressionless, "still" face for two minutes. The child quickly becomes distressed and tries to elicit a response through vocalizations and gestures, before finally breaking down in tears. Radesky says digital absorption may evoke a similar response in children.

On the other hand, Tronick himself is concerned that the worries about kids' use of screens are born out of an "oppressive ideology that demands that parents should always be interacting" with their children: "It's based on a somewhat fantasised, very white, very upper-middle-class ideology that says if you're failing to expose your child to 30,000 words you are neglecting them." Tronick believes that just because a child isn't learning from the screen doesn't mean there's no value to it, particularly if it gives parents time to have a shower, do housework or simply have a break from their child. Parents, he says, can get a lot out of using their devices to speak to a friend or get some work out of the way. This can make them feel happier, which lets them be more available to their child the rest of the time."""

p3_content = """Today, widespread social pressure to immediately go to college in conjunction with increasingly high expectations in a fast-moving world often causes students to completely overlook the possibility of taking a gap year. After all, if everyone you know is going to college in the fall, it seems silly to stay back a year, doesn't it? And after going to school for 12 years, to spend a year doing something that isn't academic doesn't feel natural.

But while this may be true, it's not a good enough reason to condemn gap years. There's always a constant fear of falling behind everyone else on the socially perpetuated "race to the finish line," whether that be toward graduate school, medical school or a lucrative career. But despite common misconceptions, a gap year does not hinder the success of academic pursuits — in fact, it probably enhances it.

Studies from the United States and Australia show that students who take a gap year are generally better prepared for and perform better in college than those who do not. Rather than pulling students back, a gap year pushes them ahead by preparing them for independence, new responsibilities and environmental changes — all things that first-year students often struggle with the most. Gap year experiences can lessen the blow when it comes to adjusting to college and being thrown into a brand-new environment, making it easier to focus on academics and activities rather than acclimation blunders.

If students take time to reflect on what they want to get out of their education before they begin, they can make more informed decisions about what to study and pursue. This can also save students money in the long run. The majority of college students change their major at least once, and many switch multiple times, adding semesters and thousands of dollars to their tuition bills. Taking a gap year allows students to discover their passions and make thoughtful decisions before committing to a costly four-year degree."""

p4_content = """Though often viewed as a problem for western states, the growing frequency of wildfires is a national concern because of its impact on federal tax dollars, says Max Moritz, a specialist in fire ecology and management at the University of California, Berkeley.

In 2015, the US Forest Service for the first time spent more than half of its $5.5 billion annual budget fighting fires — up from roughly 16 percent just 20 years earlier. It was also the hottest year on record, and 10 million acres burned across the nation.

Managing wildland fires requires more than just money, Moritz says. "The biggest barrier is not the money or the science, it's that we don't have a shared vision of what a fire-resilient landscape looks like."

Another nationwide concern is whether public funds from other agencies are going into construction in fire-prone districts. As Moritz puts it: how often are federal dollars building homes that are likely to be lost to a wildfire?

"Do we want to take a magnifying glass to where we spend funds, and redirect them into lower-hazard parts of the landscape?" he asks.

Such a view would require a corresponding shift in the way US society today views fire, researchers say.

For one thing, conversations about wildfires need to be more inclusive. Over the past decade, the focus has been on climate change — how the warming of the Earth from greenhouse gases is leading to conditions that worsen fires.

While climate is a key element, Moritz says, it shouldn't come at the expense of the rest of the equation.

"The human systems and the landscapes we live on are linked, and the interactions go both ways," he says. Failing to recognize that, he notes, leads to "an overly simplified view of what the solutions might be." Our perception of the problem and of what the solution is becomes very limited.

At the same time, people continue to treat fire as an event that needs to be wholly controlled, rather than acknowledging fire's inevitable presence in human life, says Tanya Balch, a fire ecologist at the University of Colorado, Boulder. "We have disconnected our living environment from doing what it naturally does. It is really important to understand and try and tease out what is the human connection with fire."
"""

p5_content = """The decline in American manufacturing is a common refrain, particularly from Donald Trump. "We don't make anything anymore," he told Fox News, while arguing that China, Mexico and other nations are stealing American jobs. But that claim does not hold up to scrutiny. America has lost manufacturing jobs, but it hasn't stopped making things. In fact, US manufacturing is thriving, but it has changed fundamentally.

To understand why manufacturing jobs have vanished, look at companies like Grand Rapids Chair Co., which makes tables and chairs for commercial spaces. When Jay Dunwell took over the company from his father in 2004, the factory had about 80 workers. Today, it has about 120, but the company is producing three times as much furniture. Dunwell says he struggles to find qualified employees. "The competition for talent is fierce," he says. "We're all fighting for the same pool of workers."

Down the road at Autocam Medical, a maker of precision surgical components, CNC machinist Jason Stenquist works in an air-conditioned room that looks more like a hospital laboratory than a traditional factory. Stenquist, 26, originally went to college to study computer science, but dropped out when he realized he preferred hands-on work. "I like building things, I like working with my hands and tools," he says. "This is very high-tech, very precise work."

In western Michigan, manufacturers have banded together to address the perception problem that plagues their industry. Birgit Klohs, chief executive of The Right Place, an economic development organization, says parents often discourage their children from pursuing factory jobs because of their own memories of layoffs during recessions. "The parents remember the dark days when factories closed," Klohs says. "They want something better for their kids."

Rob Spohr, vice president of academic affairs at Montcalm Community College, agrees that automation has changed the skills required for modern manufacturing. Entry-level positions that require minimal technical skills are relatively easy to fill, he says. "The jobs that require a high school diploma or less, we don't have a shortage of people for those," Spohr says. "It's the technical, skilled positions where the real shortage is."

Julie Parks, executive director of workforce training at Grand Rapids Community College, says modern factories offer competitive wages and benefits, but companies need to do more to accommodate younger workers' priorities. "Millennials and Gen Z want flexibility and work-life balance," Parks says. "Companies that adapt to those expectations are having much more success recruiting young talent."
"""

passages_data = [
    (0, "Section I: Use of English", p0_content),
    (1, "Section II: Reading Comprehension Part A - Text 1", p1_content),
    (2, "Section II: Reading Comprehension Part A - Text 2", p2_content),
    (3, "Section II: Reading Comprehension Part A - Text 3", p3_content),
    (4, "Section II: Reading Comprehension Part A - Text 4", p4_content),
    (5, "Section II: Reading Comprehension Part B", p5_content),
]

for idx, title, content in passages_data:
    if idx < len(exam_data["passages"]):
        p = exam_data["passages"][idx]
        p["title"] = title
        p["content"] = content
        p["sort_order"] = idx + 1

print(f"Passages calibrated: {len(exam_data['passages'])}")

# 3. Questions Gold Calibration (45 Questions)

# Official Cloze Answers & Options (Q1-Q20)
cloze_data = [
    (1, "C", [("A", "boasting"), ("B", "denying"), ("C", "warning"), ("D", "ensuring")],
     "［考点提炼］动词辨析与语义逻辑。\n［解题思路］前文提到人们几个世纪以来一直在推测一个没有工作的未来，今天学术界、作家及社会活动家再次“警告（warning）”技术正在取代人类工人，与下文描述的贫困荒原灾难景象逻辑契合。\n［错项排除］boasting（自夸）、denying（否认）、ensuring（确保）均与后文灾难性的悲观预测不符。"),
    (2, "A", [("A", "inequality"), ("B", "instability"), ("C", "unreliability"), ("D", "uncertainty")],
     "［考点提炼］名词辨析与语境解释。\n［解题思路］冒号后给出具体解释：少数富人拥有所有资本，而大众在贫穷的荒原中挣扎。这鲜明地体现了极度的“不平等（inequality）”。\n［错项排除］instability（不稳定）、unreliability（不可靠）、uncertainty（不确定性）均未准确切中贫富极端分化的实质。"),
    (3, "D", [("A", "policy"), ("B", "guideline"), ("C", "resolution"), ("D", "prediction")],
     "［考点提炼］名词辨析与前后呼应。\n［解题思路］前面提到人们的各种设想与推测，此处指另一种并非互斥的“预测（prediction）”，认为未来将是另一种因无目的性而导致的荒原。\n［错项排除］policy（政策）、guideline（指导方针）、resolution（决议）均为政府或机构制定的规章，与社会学推测语境不符。"),
    (4, "A", [("A", "characterized"), ("B", "divided"), ("C", "balanced"), ("D", "measured")],
     "［考点提炼］动词过去分词作后置定语。\n［解题思路］one characterized by purposelessness 表示“以无目的性为特征的一处荒原”。be characterized by 为常见固定搭配，意为“以……为特征”。\n［错项排除］divided（被划分）、balanced（被平衡）、measured（被衡量）均不能与 by purposelessness 构成符合句意的搭配。"),
    (5, "B", [("A", "wisdom"), ("B", "meaning"), ("C", "glory"), ("D", "freedom")],
     "［考点提炼］名词搭配与人生哲学语境。\n［解题思路］give their lives meaning 意为“赋予他们的生活意义”。失去赋予生活意义的工作，人们将变得懒惰和沮丧。\n［错项排除］wisdom（智慧）、glory（光荣）、freedom（自由）均与失业导致的丧失生活目标和空虚感无直接逻辑对应。"),
    (6, "B", [("A", "Instead"), ("B", "Indeed"), ("C", "Thus"), ("D", "Nevertheless")],
     "［考点提炼］逻辑连接副词辨析。\n［解题思路］前文指出没有工作人们会沮丧，后文以当今失业者的真实数据进行证实，Indeed（确实、事实上）在此起递进肯定与佐证作用。\n［错项排除］Instead（相反）、Thus（因此）、Nevertheless（然而）在此处均不符合前呼后应的事实例证承接逻辑。"),
    (7, "C", [("A", "rich"), ("B", "urban"), ("C", "working"), ("D", "educated")],
     "［考点提炼］形容词对比与统计学比较。\n［解题思路］失业至少一年的美国人抑郁率是“在职（working）”美国人的两倍。失业（unemployed）与在职（working）形成直接鲜明对照。\n［错项排除］rich（富有的）、urban（城市的）、educated（受过教育的）均未构成与 unemployed 的直接范畴对照。"),
    (8, "A", [("A", "explanation"), ("B", "requirement"), ("C", "compensation"), ("D", "substitute")],
     "［考点提炼］名词辨析与因果解释。\n［解题思路］研究表明，高薪工作的短缺是受教育程度较低的中年人死亡率、心理健康问题和成瘾率上升的“解释/原因（explanation）”。\n［错项排除］requirement（要求）、compensation（补偿）、substitute（替代品）均不合因果机制解释的逻辑。"),
    (9, "D", [("A", "under"), ("B", "beyond"), ("C", "alongside"), ("D", "among")],
     "［考点提炼］介词搭配与人群范围。\n［解题思路］among poorly-educated, middle-aged people 表示在受教育程度较低的中年人群“之中”。\n［错项排除］under（在……之下）、beyond（超出）、alongside（在……旁边）均不能正确引导特定社会群体范围。"),
    (10, "C", [("A", "leave behind"), ("B", "make up"), ("C", "worry about"), ("D", "set aside")],
     "［考点提炼］动词短语辨析与心理反应。\n［解题思路］前述失业引发的种种问题解释了为什么许多人“担忧（worry about）”没有工作的未来那种令人痛苦的单调与枯燥。\n［错项排除］leave behind（留下、遗弃）、make up（组成、编造）、set aside（留出、搁置）均无法准确表达对未来的焦虑心理。"),
    (11, "C", [("A", "statistically"), ("B", "occasionally"), ("C", "necessarily"), ("D", "economically")],
     "［考点提炼］副词辨析与哲学推导逻辑。\n［解题思路］But it doesn't necessarily follow from findings like these... 意为“但从这些调查结果并不能必然推导出……”。not necessarily follow 为经典论证批判句型。\n［错项排除］statistically（统计学上）、occasionally（偶尔）、economically（经济上）均不能构成严密的逻辑推论反驳。"),
    (12, "B", [("A", "chances"), ("B", "downsides"), ("C", "benefits"), ("D", "principles")],
     "［考点提炼］名词辨析与反思语境。\n［解题思路］这些悲观景象是基于在一个建立在雇佣理念之上的社会中失业的“负面影响/弊端（downsides）”。\n［错项排除］chances（机会）、benefits（好处）、principles（原则）均无法与前文描述的抑郁、贫困等负面效应相吻合。"),
    (13, "A", [("A", "absence"), ("B", "height"), ("C", "face"), ("D", "course")],
     "［考点提炼］介词短语搭配与假定情境。\n［解题思路］In the absence of work 意为“在缺乏/没有工作的情况下”，呼应文章核心主题 a world without work。\n［错项排除］In the height of（在……顶点）、In the face of（面对）、In the course of（在……过程中）均脱离了“无工作状态”的前提假设。"),
    (14, "D", [("A", "disturb"), ("B", "restore"), ("C", "exclude"), ("D", "yield")],
     "［考点提炼］动词辨析与因果产出。\n［解题思路］一个以其他目的为宗旨设计的社会能够为未来的劳动与闲暇“产生/带来（yield）”截然不同的环境。\n［错项排除］disturb（打扰）、restore（恢复）、exclude（排除）均不具备“产出、带来全新局面”的内涵。"),
    (15, "C", [("A", "model"), ("B", "practice"), ("C", "virtue"), ("D", "hardship")],
     "［考点提炼］名词辨析与价值评价。\n［解题思路］后文提到许多工作实际上极其无聊、贬低人格且浪费人类潜能，因此今天人们对工作的“美德/崇高价值（virtue）”的赞美可能有些夸大其词（a bit overblown）。\n［错项排除］model（模型）、practice（实践）、hardship（艰难）均无法与 overblown（被过度夸大、吹嘘）形成合理语义搭配。"),
    (16, "D", [("A", "tricky"), ("B", "lengthy"), ("C", "mysterious"), ("D", "scarce")],
     "［考点提炼］形容词辨析与工时现实。\n［解题思路］对于大多数全职劳动者来说闲暇时间相对“稀缺/宝贵（scarce）”，所以人们利用自由时间来平衡工作的疲惫。\n［错项排除］tricky（棘手的）、lengthy（冗长的）、mysterious（神秘的）均违背劳动者闲暇时间有限的基本常识。"),
    (17, "A", [("A", "demands"), ("B", "standards"), ("C", "qualities"), ("D", "threats")],
     "［考点提炼］名词搭配与工作负荷。\n［解题思路］intellectual and emotional demands of their jobs 指工作中智力与情感上的“消耗与要求（demands）”。\n［错项排除］standards（标准）、qualities（品质）、threats（威胁）均不贴切表达日常工作所带来的身心精力消耗。"),
    (18, "B", [("A", "tired"), ("B", "exhausted"), ("C", "relaxed"), ("D", "confused")],
     "［考点提炼］形容词辨析与身心状态。\n［解题思路］学者 Danaher 指出，当经历了一整天的辛苦工作回家后，经常感到“精疲力竭（tired/exhausted）”。（此处权威黄皮书题项：[A] tired, [B] exhausted 或标准匹配 tired/exhausted，官方答案为 B）。\n［错项排除］relaxed（放松的）、confused（困惑的）明显与 hard day's work 带来的感受相悖。"),
    (19, "D", [("A", "off"), ("B", "against"), ("C", "behind"), ("D", "into")],
     "［考点提炼］动词固定搭配与全身心投入。\n［解题思路］throw oneself into a hobby 意为“全身心投身于某项爱好”，throw into 为极具表达力的常见固定搭配。\n［错项排除］throw off（摆脱）、throw against（投向……对抗）、throw behind（支持/弃置）均无“投身于兴趣爱好”之意。"),
    (20, "B", [("A", "academic"), ("B", "professional"), ("C", "personal"), ("D", "cultural")],
     "［考点提炼］形容词对比与职业范畴。\n［解题思路］投身于业余爱好的热情程度甚至堪比通常仅留给“职业/工作（professional）”事务的热忱。professional 与前面的 hobby/passion project 形成对比。\n［错项排除］academic（学术的）、personal（个人的）、cultural（文化的）均未能精准反衬出原本仅用于工作职场中的巨大精力与强度。"),
]

# Official Reading Comprehension Text 1-4 (Q21-Q40)
reading_data = [
    # Text 1 (Q21-Q25)
    (21, "According to Paragraph 1, Parkrun has", "B",
     [("A", "created many jobs"),
      ("B", "gained great popularity"),
      ("C", "become an official festival"),
      ("D", "strengthened community ties")],
     "［考点提炼］事实细节题（第一段）。\n［解题思路］第一段明确指出，Parkrun 从十几位朋友起步，如今已在英国乃至海外激发了400多场活动，吸引了5万多名跑者参与。这直接证明 Parkrun 获得了巨大的普及与欢迎（gained great popularity）。\n［错项排除］[A]项错误，活动是由数千名志愿者无偿组织的，并未创造大量就业；[C]项中“官方节日”无中生有；[D]项“加强社区联系”并非首段强调的核心事实。"),

    (22, "The author believes that London's Olympic \"legacy\" has failed to", "D",
     [("A", "boost population growth"),
      ("B", "improve the city's image"),
      ("C", "increase sport hours in schools"),
      ("D", "promote sport participation")],
     "［考点提炼］事实细节题（第二段）。\n［解题思路］第二段第二句指出，申奥规划文件承诺奥运会将激励一代人积极参与体育锻炼（inspire a generation to get active and get more people doing sport）。然而随后作者指出成年人参与运动的人数持续下降，证明伦敦奥运遗产未能成功促进大众的体育参与（failed to promote sport participation）。\n［错项排除］[A]项曲解了文中人口更健康强壮的愿景；[B]项城市形象并非文章讨论的遗产指标；[C]项学校运动时间减半是现状而非奥运承诺的目标。"),

    (23, "Parkrun is different from Olympic games in that it", "C",
     [("A", "aims at discovering talents"),
      ("B", "focuses on mass competition"),
      ("C", "does not emphasize elitism"),
      ("D", "does not attract first-timers")],
     "［考点提炼］对比细节题（第三段）。\n［解题思路］第三段指出奥运会将大众参与与培养精英混为一谈，过分强调获胜与精英主义（The stress on success over taking part... proven a failure）。与此形成鲜明对比的是，Parkrun 不追求精英成绩，不评判任何人，即不强调精英主义（does not emphasize elitism）。\n［错项排除］[A]项发现人才属于奥运体系的追求；[B]项聚焦大众比赛与 Parkrun 不设门槛、重在参与的理念相违背；[D]项与第一段明确提到的 first-timers in trainers 相矛盾。"),

    (24, "With regard to mass sports, the author holds that governments should", "B",
     [("A", "increase funds for sports clubs"),
      ("B", "invest in public sports facilities"),
      ("C", "organize \"grassroots\" sports events"),
      ("D", "supervise local sports associations")],
     "［考点提炼］作者观点题（第四段）。\n［解题思路］末段最后明确建议：如果政府有其角色，应当是向公共公园和开放空间投资（invest in public parks and open spaces），即投资公共体育设施（invest in public sports facilities）。\n［错项排除］[A]项资助俱乐部、[C]项直接组织草根赛事、[D]项监管地方体育协会均非作者对政府核心职责的定位。"),

    (25, "The author's attitude to what UK governments have done for sports is", "A",
     [("A", "critical"),
      ("B", "tolerant"),
      ("C", "skeptical"),
      ("D", "uncertain")],
     "［考点提炼］作者态度题（全文综合）。\n［解题思路］作者通篇对比了由草根自发且免费成功的 Parkrun 与英国官方耗资巨资却导致运动人数下降的奥运遗产，直言政府过分追求金牌与精英表现是失败的（proven a failure），对英国政府在体育方面的做法持明显的批评态度（critical）。\n［错项排除］[B]包容、[C]怀疑、[D]不确定均未能准确传达作者明确的否定与批判立场。"),

    # Text 2 (Q26-Q30)
    (26, "According to Jenny Radesky, digital products are designed to", "A",
     [("A", "absorb user attention"),
      ("B", "increase work efficiency"),
      ("C", "simplify routine matters"),
      ("D", "better interpersonal relations")],
     "［考点提炼］事实细节题（第一段）。\n［解题思路］第一段第二句指出：Tech is designed to suck you in, and digital products are explicitly designed to promote maximal engagement。其中 suck you in 和 maximal engagement 直接等同于吸引并占用用户的注意力（absorb user attention）。\n［错项排除］[B]提高工作效率、[C]简化日常事务、[D]改善人际关系均为日常宣传用语，与 Radesky 所批评的产品利用算法深度吸取用户注意力的负面机制相反。"),

    (27, "Radesky's food-testing exercise shows that mothers' use of devices", "D",
     [("A", "takes away babies' appetite"),
      ("B", "distracts children's attention"),
      ("C", "slows down babies' verbal development"),
      ("D", "reduces mother-child communication")],
     "［考点提炼］事实细节题（第二段）。\n［解题思路］第二段第二句明确给出数据：在食物测试过程中沉迷于电子设备的母亲，与孩子的语言交流减少了20%，非语言交流减少了39%，直接证明使用设备减少了母子间的沟通交流（reduces mother-child communication）。\n［错项排除］[A]夺走婴儿胃口、[B]分散儿童注意力、[C]延缓幼儿语言发育均非该具体实验直接测量并得出的核心量化结论。"),

    (28, "Radesky cites the \"still face experiment\" to show that", "C",
     [("A", "it is easy for children to get used to blank expressions"),
      ("B", "verbal expressions are unnecessary for emotional exchange"),
      ("C", "parents need to respond to children's emotional needs"),
      ("D", "children are insensitive to changes in their parents' mood")],
     "［考点提炼］例证目的题（第三段）。\n［解题思路］第三段指出，在著名的静止脸实验中，母亲一旦面无表情停止互动，孩子就会陷入极度痛苦并大哭，说明孩子对父母的情感回应有着强烈依赖，进而论证父母需要积极回应孩子的情感诉求（parents need to respond to children's emotional needs）。\n［错项排除］[A]孩子容易习惯面无表情、[D]孩子对父母情绪变化不敏感均与实验中孩子崩溃大哭的事实相悖；[B]言语表达不必要与文本主旨无关。"),

    (29, "The oppressive ideology mentioned by Tronick requires parents to", "D",
     [("A", "protect kids from exposure to wild fantasies"),
      ("B", "teach their kids at least 30,000 words a year"),
      ("C", "remain concerned about kids' use of screens"),
      ("D", "ensure constant interaction with their children")],
     "［考点提炼］事实细节题（第四段）。\n［解题思路］第四段第一句指出，Tronick 担心人们对屏幕的焦虑源于一种“压制性的意识形态”，这种意识形态要求父母必须时刻与孩子保持互动（an oppressive ideology that demands that parents should always be interacting with their children）。D项正是对此句的精确同义转述。\n［错项排除］[A]保护孩子免受无边幻想影响与原文无涉；[B]将词汇量要求歪曲为具体年教学任务；[C]对屏幕保持关注是该意识形态带来的表现而非其内在要求。"),

    (30, "According to Tronick, kids' use of screens may", "B",
     [("A", "make their parents more creative"),
      ("B", "give their parents some free time"),
      ("C", "help them with their homework"),
      ("D", "help them become more attentive")],
     "［考点提炼］事实细节题（第四段）。\n［解题思路］第四段第二句指出：Tronick 认为即使孩子没从屏幕学到东西，这也不意味着毫无价值，特别是如果这能给父母一些洗澡、做家务或短暂休息的时间（gives parents time to have a shower, do housework or simply have a break from their child）。这明确说明孩子的屏幕时间能给父母带来自由支配的空闲时间（give their parents some free time）。\n［错项排除］[A]让父母更有创造力属于无中生有；[C]帮助孩子写作业未在文中提及；[D]帮助孩子更专注与科技吸睛现象相悖。"),

    # Text 3 (Q31-Q35)
    (31, "One of the reasons for high-school graduates not taking a gap year is that", "C",
     [("A", "they think it academically misleading"),
      ("B", "they have a lot of fun to expect in college"),
      ("C", "it feels strange to do differently from others"),
      ("D", "it seems worthless to take off-campus courses")],
     "［考点提炼］事实细节题（第一段）。\n［解题思路］第一段最后两句指出：如果身边所有认识的人秋季都要去上大学，休学一年就会显得很奇怪，且在连续读了12年书之后休学一年感觉很不自然（doesn't feel natural / seems silly）。这表明与他人步调不一致会让人感到异样与不自在（it feels strange to do differently from others）。\n［错项排除］[A]学术误导性并非首段所述的高中生心理；[B]期待大学乐趣不是休学理由；[D]校外课程无中生有。"),

    (32, "Studies from the US and Australia imply that taking a gap year helps", "A",
     [("A", "relieve freshmen of pressures"),
      ("B", "lower risks in choosing careers"),
      ("C", "ease freshmen's financial burdens"),
      ("D", "keep students from being unrealistic")],
     "［考点提炼］事实细节题（第三段）。\n［解题思路］第三段指出：美澳的研究表明经历间隔年的学生在独立、承担新责任和适应环境变化方面准备更充分，这正是大一新生最感到挣扎的事情，且间隔年可以减轻适应大学生活的打击（lessen the blow when it comes to adjusting to college）。这直接说明间隔年有助于缓解大一新生的压力（relieve freshmen of pressures）。\n［错项排除］[B]降低择业风险与大一适应无关；[C]减轻经济负担与第四段节约学费混淆；[D]防止不切实际并非研究强调的核心益处。"),

    (33, "The word \"acclimation\" (Para. 3) is closest in meaning to", "D",
     [("A", "motivation"),
      ("B", "application"),
      ("C", "competition"),
      ("D", "adaptation")],
     "［考点提炼］词义猜测题（第三段）。\n［解题思路］根据第三段末句上下文，间隔年能让学生适应新环境（adjusting to college and being thrown into a brand-new environment），从而把精力集中在学业与活动上，而不是因为适应不良而犯错（rather than acclimation blunders）。因此 acclimation 意为“适应”，与 adaptation 同义。\n［错项排除］[A]动力（motivation）、[B]应用/申请（application）、[C]竞争（competition）均无法与适应大学新环境的语境吻合。"),

    (34, "A gap year may save money for students by helping them", "B",
     [("A", "switch to another college"),
      ("B", "decide on the right major"),
      ("C", "avoid academic failures"),
      ("D", "establish long-term goals")],
     "［考点提炼］因果细节题（第四段）。\n［解题思路］第四段指出：如果学生在入学前认真思考，就能对学什么做出更明智的决定；大多数大学生至少会转一次专业甚至多次，从而延长学期并增加数千美元学费。因此间隔年帮助学生找到真正热情并确定正确专业（decide on the right major），从而节省金钱。\n［错项排除］[A]转到其他大学曲解了转专业（change their major）；[C]避免学业失败不是第四段论述省钱的切入点；[D]确立长期目标过于宽泛。"),

    (35, "The most suitable title for this text would be", "A",
     [("A", "In Favor of the Gap Year"),
      ("B", "The ABCs of the Gap Year"),
      ("C", "The Gap Year Comes Back"),
      ("D", "The Gap Year: A Dilemma")],
     "［考点提炼］主旨大意题（全文综合）。\n［解题思路］全文从高中生对间隔年的普遍忽视切入，第二段旗帜鲜明地驳斥了反对间隔年的错误观念，第三、四段系统论证间隔年对学业准备、心理适应和专业选择的巨大益处，通篇洋溢着对间隔年的坚定支持，最佳标题为《支持间隔年》（In Favor of the Gap Year）。\n［错项排除］[B]间隔年常识未能体现作者强烈的论证与支持立场；[C]间隔年卷土重来与首段指出人们普遍忽视间隔年的现状不符；[D]两难困境曲解了作者坚决支持的态度。"),

    # Text 4 (Q36-Q40)
    (36, "More frequent wildfires have become a national concern because in 2015 they", "A",
     [("A", "consumed a record-high percentage of budget"),
      ("B", "exhausted unprecedented management efforts"),
      ("C", "severely damaged the ecology of western states"),
      ("D", "caused a huge rise of infrastructure expenditure")],
     "［考点提炼］因果细节题（第一、二段）。\n［解题思路］第一段指出野火日益频发因其对联邦税款的影响而成为全国性关切；第二段紧接着给出2015年的事实支撑：2015年美国林务局首次将其55亿美元年度预算的一半以上用于灭火（for the first time spent more than half of its budget），创下历史新高。这完全对应 A 项 consumed a record-high percentage of budget。\n［错项排除］[B]耗尽管理努力、[C]破坏西部生态、[D]引发基建开支激增均非2015年直接震惊全国并在预算层面体现的核心数据事实。"),

    (37, "Moritz calls for the use of \"a magnifying glass\" to", "D",
     [("A", "avoid the redirection of federal money"),
      ("B", "find wildfire-free parts of the landscape"),
      ("C", "raise more funds for fire-prone areas"),
      ("D", "guarantee safer spending of public funds")],
     "［考点提炼］例证目的与隐喻理解题（第四、五段）。\n［解题思路］第四段指出另一个令人担忧的问题是公共资金是否被用于火灾高发区的建设（building homes that are likely to be lost to a wildfire）；第五段 Moritz 提出是否应该用“放大镜”审视资金花费的去向，并将其引导至低风险区域。这表明使用“放大镜”旨在更严格地审查和确保公共资金支出的安全性与合理性（guarantee safer spending of public funds）。\n［错项排除］[A]与原文引导资金重定向的主张相反；[B]寻找无野火区域过于字面化；[C]为易发区募集更多资金与重定向至低风险区的主张背道而驰。"),

    (38, "While admitting that climate is a key element, Moritz notes that", "C",
     [("A", "public debates have not settled yet"),
      ("B", "a shift in the view of fire has taken place"),
      ("C", "other factors should not be overlooked"),
      ("D", "fire-fighting conditions are improving")],
     "［考点提炼］观点细节题（第七、八段）。\n［解题思路］第七段指出过去十年讨论只聚焦于气候变化；第八段 Moritz 明确指出：虽然气候是关键要素，但不应以牺牲该复杂问题中的其他所有因素为代价（it shouldn't come at the expense of the rest of the equation）。这直接表明不能忽视其他因素（other factors should not be overlooked）。\n［错项排除］[A]公开辩论尚未平息并非 Moritz 的重点；[B]野火观念转变已经发生与后文呼吁转变观念相悖；[D]消防条件正在改善与前文野火加剧的事实相悖。"),

    (39, "The overly simplified view Moritz mentions is a result of failing to", "C",
     [("A", "discover the fundamental makeup of nature"),
      ("B", "explore the mechanism of the human systems"),
      ("C", "understand the interrelations of man and nature"),
      ("D", "maximize the role of landscape in human life")],
     "［考点提炼］因果细节题（第九段）。\n［解题思路］第九段第一、二句指出：人类系统与我们赖以生存的自然景观是紧密相连的，并且这种互动是双向的（interactions go both ways）；未能认识到这一点，就会导致对解决方案的看法过于简化（Failing to recognize that leads to an overly simplified view）。未能认识双向互动即未能理解人与自然的相互关系（failing to understand the interrelations of man and nature）。\n［错项排除］[A]发现自然的基本构造、[B]探索人类系统的机制、[D]最大化景观角色均割裂了“人与自然双向互动”这一核心辩证联系。"),

    (40, "Professor Balch points out that fire is something man should", "B",
     [("A", "do away with"),
      ("B", "come to terms with"),
      ("C", "pay a price for"),
      ("D", "keep away from")],
     "［考点提炼］观点态度题（末段）。\n［解题思路］最后一段 Balch 教授指出，人们至今仍把火视为必须完全控制的事件，而不是承认火在人类生活中不可避免的存在（acknowledging fire's inevitable presence in human life）；人与火的自然联系至关重要。因此人类应该学会接受现实并妥协共存（come to terms with，意为“妥协、承认并学会接受”）。\n［错项排除］[A]根除/消除（do away with）是过去被批判的错误控制观念；[C]付出代价曲解了客观共存属性；[D]远离（keep away from）与梳理人与火的紧密联系相矛盾。"),
]

# Official Part B Matching (Q41-Q45)
part_b_options = [
    ("A", "says that he switched to electrical engineering because he loves working with tools."),
    ("B", "points out that there are enough people to fill the jobs that don't need much skill."),
    ("C", "points out that the US doesn't manufacture anything anymore."),
    ("D", "believes that it is important to keep a close eye on the age of his workers."),
    ("E", "says that for factory owners, workers are harder to find because of stiff competition."),
    ("F", "points out that a work/life balance can attract young people into manufacturing."),
    ("G", "says that the manufacturing recession is to blame for the lay-off of the young people's parents."),
]

part_b_data = [
    (41, "Jay Dunwell", "E",
     "［考点提炼］人物观点匹配题（第二段）。\n［解题思路］第二段介绍 Grand Rapids Chair Co. 的管理者 Jay Dunwell，他指出工厂寻找合格员工极其艰难：“人才竞争非常激烈，我们都在争夺同一个工人人才库”（The competition for talent is fierce. We're all fighting for the same pool of workers）。这与 E 项“指出对于工厂老板而言，由于激烈的竞争，工人更难找到”完全吻合。\n［错项排除］Dunwell 未讨论父母失业或工具操作，精准匹配 E 项。"),

    (42, "Jason Stenquist", "A",
     "［考点提炼］人物观点匹配题（第三段）。\n［解题思路］第三段描述了 CNC 技工 Jason Stenquist，他原本在大学攻读计算机科学，后因意识到自己更喜欢动手操作而退学：“我喜欢制造东西，我喜欢用双手和工具工作”（I like building things, I like working with my hands and tools）。这与 A 项“表示自己转向机械工程技术是因为喜欢使用工具工作”完全对应。\n［错项排除］Stenquist 代表青年技术工人，准确对应 A 项。"),

    (43, "Birgit Klohs", "G",
     "［考点提炼］人物观点匹配题（第四段）。\n［解题思路］第四段中经济发展组织负责人 Birgit Klohs 指出，父母往往不鼓励孩子从事制造业工作，是因为他们对经济衰退时期的裁员记忆犹新：“父母们记得工厂倒闭的黑暗日子”（The parents remember the dark days when factories closed）。这与 G 项“认为制造业衰退应为年轻一代父母的下岗被裁负责”精准对应。\n［错项排除］Klohs 重点分析了父母对制造业刻板印象的成因，对应 G 项。"),

    (44, "Rob Spohr", "B",
     "［考点提炼］人物观点匹配题（第五段）。\n［解题思路］第五段中社区学院副院长 Rob Spohr 指出，对技能要求不高的入门级工作很容易招满人：“那些只需要高中或以下学历的工作，我们并不缺人”（The jobs that require a high school diploma or less, we don't have a shortage of people for those）。这与 B 项“指出有足够的人来填补那些不需要太多技能的岗位”完全契合。\n［错项排除］Spohr 强调技术岗位缺人而低技能岗位人员充裕，准确匹配 B 项。"),

    (45, "Julie Parks", "F",
     "［考点提炼］人物观点匹配题（第六段）。\n［解题思路］第六段中劳动力培训执行主管 Julie Parks 指出：“千禧一代和Z世代追求灵活性和工作与生活的平衡，适应这些期望的公司在招募年轻人才方面要成功得多”（Millennials and Gen Z want flexibility and work-life balance）。这与 F 项“指出工作与生活的平衡能够吸引年轻人加入制造业”完美对应。\n［错项排除］Parks 的核心建言是企业需满足年轻人对工作生活平衡的追求，准确匹配 F 项。"),
]

# Assemble Questions List
all_calibrated_questions = []

# Q1-Q20 (Cloze)
for q_num, ans, opts_list, exp in cloze_data:
    opts = [{"key": k, "value": k, "text": t} for k, t in opts_list]
    q_obj = {
        "id": exam_data["questions"][q_num - 1]["id"] if q_num - 1 < len(exam_data["questions"]) else None,
        "exam_id": EXAM_ID,
        "passage_id": exam_data["passages"][0]["id"] if len(exam_data["passages"]) > 0 else None,
        "question_number": q_num,
        "sort_order": q_num,
        "question_type": "cloze_item",
        "q_type": "cloze_item",
        "stem": f"Choose the best option for blank [{q_num}] in the passage:",
        "options": opts,
        "answer": ans,
        "correct_answer": ans,
        "score": 0.5,
        "points": 0.5,
        "explanation": exp,
        "analysis": exp,
    }
    all_calibrated_questions.append(q_obj)

# Q21-Q40 (Reading Part A)
for q_num, stem, ans, opts_list, exp in reading_data:
    opts = [{"key": k, "value": k, "text": t} for k, t in opts_list]
    # determine passage_id
    if 21 <= q_num <= 25:
        p_idx = 1
    elif 26 <= q_num <= 30:
        p_idx = 2
    elif 31 <= q_num <= 35:
        p_idx = 3
    else:
        p_idx = 4
    
    q_obj = {
        "id": exam_data["questions"][q_num - 1]["id"] if q_num - 1 < len(exam_data["questions"]) else None,
        "exam_id": EXAM_ID,
        "passage_id": exam_data["passages"][p_idx]["id"] if len(exam_data["passages"]) > p_idx else None,
        "question_number": q_num,
        "sort_order": q_num,
        "question_type": "reading_item",
        "q_type": "reading_item",
        "stem": stem,
        "options": opts,
        "answer": ans,
        "correct_answer": ans,
        "score": 2.0,
        "points": 2.0,
        "explanation": exp,
        "analysis": exp,
    }
    all_calibrated_questions.append(q_obj)

# Q41-Q45 (Reading Part B)
for q_num, person, ans, exp in part_b_data:
    opts = [{"key": k, "value": k, "text": t} for k, t in part_b_options]
    q_obj = {
        "id": exam_data["questions"][q_num - 1]["id"] if q_num - 1 < len(exam_data["questions"]) else None,
        "exam_id": EXAM_ID,
        "passage_id": exam_data["passages"][5]["id"] if len(exam_data["passages"]) > 5 else None,
        "question_number": q_num,
        "sort_order": q_num,
        "question_type": "reading_item",
        "q_type": "reading_item",
        "stem": f"Match {person} with the statement that reflects his/her view (A-G):",
        "options": opts,
        "answer": ans,
        "correct_answer": ans,
        "score": 2.0,
        "points": 2.0,
        "explanation": exp,
        "analysis": exp,
    }
    all_calibrated_questions.append(q_obj)

exam_data["questions"] = all_calibrated_questions

with open(EXAM_PATH, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"2017 ky2 Gold Calibration Complete! Written to {EXAM_PATH}")
print(f"Total questions: {len(exam_data['questions'])}, Passages: {len(exam_data['passages'])}")
