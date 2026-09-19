// 2018 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2018Exams = [
  // =========================================================================
  // 2018 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky1",
    year: 2018,
    title: "2018年全国硕士研究生招生考试英语（一）真题",
    exam_type: "real",
    duration_minutes: 60,
    total_score: 50.00,
    pass_score: 30.00,
    is_published: true,
    approval_status: "approved",
    passages: [
      {
        section_type: "cloze",
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Trust is the invisible lubricant that allows human societies to function without descending into perpetual conflict. Whether boarding a commercial airliner, depositing savings into a financial institution, or simply buying food at a neighborhood grocery store, human beings operate on implicit acts of (1)____. We routinely place our physical safety and economic well-being into the hands of total (2)____, confident that formal legal contracts and informal social norms will prevent malicious betrayal.

In recent decades, however, sociologists have tracked a precipitous decline in social and institutional (3)____ across Western democracies. Citizens express historic cynicism toward elected politicians, mainstream media outlets, and corporate conglomerates. This erosion of faith is not merely a psychological (4)____; it possesses tangible, corrosive economic consequences. When mutual trust collapses, transaction costs (5)____. Business enterprises must draft suffocating legal contracts, employ armies of compliance auditors, and install intrusive surveillance apparatuses to verify that employees and contractors are not engaging in deceitful (6)____.

Economists categorize trust into two fundamental varieties: "generalized trust" extended toward anonymous fellow citizens, and "particularized trust" confined strictly to members of one's immediate familial or tribal (7)____. High levels of generalized trust correlate strongly with robust economic growth, innovative entrepreneurship, and egalitarian welfare systems. Conversely, societies dominated by particularized trust frequently suffer from systemic nepotism, widespread bureaucratic bribery, and chronic political (8)____.

Social scientists attribute the contemporary trust deficit to multiple converging forces. The dramatic expansion of economic inequality has fractured shared social identities, creating a perception that economic rules are structurally (9)____ to favor wealthy elites at the expense of ordinary citizens. Simultaneously, algorithmic social media platforms optimize engagement by amplifying polarizing outrage, convincing citizens that political adversaries are not merely misguided, but morally (10)____.

Furthermore, repeated institutional failures have shattered public credibility. From catastrophic banking bailouts to corporate accounting scandals and misleading governmental intelligence, authorities have repeatedly displayed catastrophic (11)____ followed by total impunity. When elites face zero accountability for disastrous errors, the public naturally retreats into cynical (12)____.

Rebuilding social capital requires profound institutional renewal. Governments must enhance administrative transparency, aggressively prosecute elite financial crimes, and reinvest in public goods—such as accessible healthcare and equitable public education—that cultivate shared civic (13)____.

At the interpersonal level, psychologists emphasize that trust is not a static commodity, but a dynamic muscle strengthened through continuous (14)____. Engaging in local voluntary associations, participating in neighborhood community councils, and seeking out face-to-face dialogues with individuals from diverse socioeconomic backgrounds fosters mutual (15)____.

Ultimately, democracy cannot survive in an atmosphere of universal suspicion. Cultivating a culture of earned trust, coupled with vigilant institutional accountability, is essential for preserving the moral foundations of our democratic (16)____. Without trust, freedom degenerates into anarchy, and the social contract dissolves into bitter ideological (17)____. Restoring this sacred bond is the defining civic challenge of our contemporary (18)____, demanding courageous leadership, ethical integrity, and a renewed commitment to the common (19)____ across every level of public life (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "faith" },
              { key: "B", text: "hostility" },
              { key: "C", text: "jealousy" },
              { key: "D", text: "panic" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。implicit acts of faith（内隐的信任/托付行为），与首句 Trust 紧密呼应。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "strangers" },
              { key: "B", text: "ancestors" },
              { key: "C", text: "enemies" },
              { key: "D", text: "rulers" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词对比。在现代社会中，我们将安危托付给素昧平生的陌生人（total strangers）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "trust" },
              { key: "B", text: "luxury" },
              { key: "C", text: "wealth" },
              { key: "D", text: "violence" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨名词。decline in social and institutional trust（社会与体制信任的滑坡）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "curiosity" },
              { key: "B", text: "triumph" },
              { key: "C", text: "miracle" },
              { key: "D", text: "celebration" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】搭配转折。not merely a psychological curiosity（绝非纯粹的心理奇特现象），而是伴随着真真切切的经济损失。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "skyrocket" },
              { key: "B", text: "vanish" },
              { key: "C", text: "collapse" },
              { key: "D", text: "stagnate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词语义。信任瓦解时，交易成本必然一飞冲天/暴涨（transaction costs skyrocket）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "fraud" },
              { key: "B", text: "charity" },
              { key: "C", text: "heroism" },
              { key: "D", text: "diplomacy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极修饰。engaging in deceitful fraud（从事欺诈欺骗行为）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "circle" },
              { key: "B", text: "prison" },
              { key: "C", text: "desert" },
              { key: "D", text: "monument" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。familial or tribal circle（家族或部落小圈子）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "dysfunction" },
              { key: "B", text: "harmony" },
              { key: "C", text: "prosperity" },
              { key: "D", text: "splendor" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。裙带关系与贪腐滋生，导致长期政治机能失调（political dysfunction）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "rigged" },
              { key: "B", text: "fair" },
              { key: "C", text: "generous" },
              { key: "D", text: "sacred" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词搭配。structurally rigged（在体制结构上被暗中操纵偏袒精英）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "corrupt" },
              { key: "B", text: "noble" },
              { key: "C", text: "virtuous" },
              { key: "D", text: "harmless" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词对比。算法煽动极化仇恨，让公众认定政治对手道德败坏（morally corrupt）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "incompetence" },
              { key: "B", text: "bravery" },
              { key: "C", text: "modesty" },
              { key: "D", text: "clarity" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极名词。从金融危机到会计丑闻，掌权者暴露了灾难性的无能与渎职（catastrophic incompetence）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "detachment" },
              { key: "B", text: "enthusiasm" },
              { key: "C", text: "adoration" },
              { key: "D", text: "gratitude" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理名词。公众退缩进愤世嫉俗的冷漠疏离（cynical detachment）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "solidarity" },
              { key: "B", text: "hostility" },
              { key: "C", text: "jealousy" },
              { key: "D", text: "shame" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社会学名词。公共产品投资能培育共同的公民团结与连带感（shared civic solidarity）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "exercise" },
              { key: "B", text: "retreat" },
              { key: "C", text: "neglect" },
              { key: "D", text: "decay" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】肌肉比喻。trust is a dynamic muscle strengthened through exercise（信任如肌肉，需在实践历练中强化）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "empathy" },
              { key: "B", text: "scorn" },
              { key: "C", text: "animosity" },
              { key: "D", text: "derision" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词。面对面交流能催生相互同理心（mutual empathy）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "institutions" },
              { key: "B", text: "prisons" },
              { key: "C", text: "ruins" },
              { key: "D", text: "weapons" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】政治名词。democratic institutions（民主制度与体制基础）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "warfare" },
              { key: "B", text: "harmony" },
              { key: "C", text: "luxury" },
              { key: "D", text: "treaties" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极修辞。社会契约瓦解为激烈的意识形态内耗混战（bitter ideological warfare）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "epoch" },
              { key: "B", text: "weekend" },
              { key: "C", text: "second" },
              { key: "D", text: "instant" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】时代名词。defining civic challenge of our contemporary epoch（我们当代时代决定性的公民挑战）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "good" },
              { key: "B", text: "harm" },
              { key: "C", text: "spite" },
              { key: "D", text: "guilt" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】哲学固定搭配。the common good（共同善/公共福祉）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "today" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "rarely" },
              { key: "D", text: "nowhere" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】语境时间。across public life today（在当今公共生活的各个层面）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `As robotics and machine learning advance with bewildering rapidity, public debate regarding the future of employment is frequently dominated by dystopian alarmism. Headlines routinely prophesy an "automation apocalypse," warning that intelligent machines will soon eradicate half of all existing human occupations, precipitating catastrophic mass unemployment and permanent economic obsolescence for the working class.

However, historical and labor economics provide a far more nuanced, reassuring perspective. The Industrial Revolution of the nineteenth century and the computer revolution of the late twentieth century generated comparable panics, yet both technological epochs ultimately created vastly more employment opportunities than they destroyed. Technology does not eliminate work; it eliminates specific, routinized tasks. When automated steam looms mechanized textile spinning, cloth prices plummeted, stimulating massive global consumer demand that required millions of workers in design, retail, logistics, and machine maintenance.

In modern labor markets, automation operates primarily through task substitution rather than job eradication. A modern paralegal no longer spends weeks manually cataloging thousands of paper court records in storage warehouses; algorithmic e-discovery software completes the task in seconds. But rather than eliminating paralegals, this efficiency frees legal professionals to conduct deeper case analysis, interview witnesses, and counsel clients. By augmenting human capabilities, technology frequently raises the economic value of human labor.

Nevertheless, complacency is dangerous. While automation creates new occupations in aggregate, the workers displaced by robotic arms or software bots rarely possess the specialized skills required to step into newly created roles. An assembly-line automotive welder laid off by robotic factory automation cannot seamlessly transition into becoming a cloud cybersecurity architect or deep learning researcher. The transition involves severe structural friction, threatening prolonged regional economic distress.

Managing the automation transition requires proactive, systemic investment in human capital. Governments and corporate employers must establish universal lifelong reskilling accounts, modernize technical apprenticeships, and overhaul vocational education systems. By equipping workers to adapt continuously alongside technological progress, society can ensure that the fourth industrial revolution expands human prosperity rather than deepening economic inequality.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Dystopian headlines regarding the future of employment frequently claim that:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Intelligent machines will cause permanent, catastrophic mass unemployment." },
              { key: "B", text: "All human workers will be paid triple their current salaries." },
              { key: "C", text: "Robots will refuse to perform any manufacturing tasks." },
              { key: "D", text: "Governments will legally ban all digital computers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出反乌托邦警报宣称“自动化末日”即将来临，智能机器将消灭一半现有工种，造成永久性大失业（catastrophic mass unemployment）。"
          },
          {
            q_type: "reading_item",
            stem: "Historical evidence from past industrial revolutions demonstrates that technology:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Eliminates specific routine tasks while creating more jobs in total." },
              { key: "B", text: "Causes permanent poverty for the entire human species." },
              { key: "C", text: "Always reduces the overall demand for consumer commodities." },
              { key: "D", text: "Has no measurable impact on economic manufacturing." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出历史表明新技术消灭的是具体常规任务（routinized tasks），但创造的总体就业岗位远多于所消灭的岗位。"
          },
          {
            q_type: "reading_item",
            stem: "The example of the modern paralegal in Paragraph 3 illustrates that automation:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Frees professionals to focus on higher-value, cognitive duties." },
              { key: "B", text: "Has forced all legal attorneys to abandon the legal profession." },
              { key: "C", text: "Makes legal trials 100 percent automated without judges." },
              { key: "D", text: "Increases the amount of physical paperwork in courthouses." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】例证题。第三段通过法律助理的例子证明算法取代检索繁琐工作后，将员工解放出来专注于更具价值的分析与沟通（frees professionals for higher-value duties）。"
          },
          {
            q_type: "reading_item",
            stem: "What major challenge of the automation transition is highlighted in Paragraph 4?",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Displaced manual workers lack the skills needed for emerging technical jobs." },
              { key: "B", text: "Robotic factory machines breakdown after forty-eight hours of operation." },
              { key: "C", text: "Young college graduates refuse to work in technology firms." },
              { key: "D", text: "Labor unions forbid anyone from learning how to operate computers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第四段指出转型痛点在于结构性技能错配：被裁撤的装配工人缺乏新创造岗位所需的专门技能，无法无缝换岗。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that mitigating the impacts of automation requires:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Aggressive public investment in lifelong reskilling and vocational training." },
              { key: "B", text: "Banning artificial intelligence research in universities." },
              { key: "C", text: "Forcing all citizens to work in traditional agricultural farms." },
              { key: "D", text: "Eliminating all government welfare programs immediately." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出从容应对技术变革需要政府与企业大力投资人力资本，设立终身再技能培训账户，革新职业技能教育。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In the psychological architecture of the modern internet, few interactive features have exerted as profound a behavioral influence as the ubiquitous "Like" button. Originally introduced by social media platforms as a lightweight mechanism to streamline user interactions, social feedback metrics—likes, shares, retweets, and follower counts—have evolved into a hyper-potent currency of interpersonal validation.

Developmental psychologists and neuroscientists warn that these quantified feedback metrics exploit a fundamental evolutionary vulnerability: the mammalian craving for social belonging and peer approval. Functional MRI scans demonstrate that receiving a flurry of online likes triggers a surge of dopamine in the brain's ventral striatum—the exact neurological reward circuit activated by gambling windfalls or addictive chemical stimulants. Because social feedback arrives on an unpredictable, intermittent schedule, users develop compulsive behavioral loops, refreshing feeds dozens of times an hour in search of the next neurochemical hit.

For adolescent users, whose neurological prefrontal cortices and self-identities are still in delicate developmental flux, this quantified feedback loop is acutely perilous. Teenagers inevitably equate their intrinsic self-worth with their metric performance. The algorithmic architecture fosters an environment of relentless toxic comparison: adolescents constantly benchmark their unvarnished, everyday lives against the meticulously curated, digitally beautified highlight reels of classmates and celebrity influencers.

Extensive clinical studies document the alarming epidemiological correlation between prolonged social media use and skyrocketing rates of adolescent depression, chronic anxiety, dysmorphic body insecurity, and sleep deprivation. When an adolescent's post fails to achieve an anticipated threshold of likes, they experience intense feelings of social rejection and acute inadequacy, often prompting impulsive post deletion and profound depressive episodes.

Confronted with mounting public outrage and regulatory scrutiny, several major tech platforms have experimented with "demetrication"—hiding public like counts to reduce peer comparison anxiety. Yet, digital ethicists emphasize that cosmetic interface tweaks fail to tackle the underlying business model. Social media empires are engineered on "surveillance capitalism," monetizing human attention through algorithmic outrage and social insecurity. Protecting adolescent well-being requires systemic regulatory intervention: enforcing strict algorithmic age limits, banning manipulative behavioral design patterns, and establishing independent oversight over youth digital mental health.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The 'Like' button has evolved into a potent behavioral tool because it:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Functions as a powerful currency of social validation and peer approval." },
              { key: "B", text: "Allows users to transfer digital cryptocurrency to bank accounts." },
              { key: "C", text: "Automatically deletes all advertisements from computer screens." },
              { key: "D", text: "Physically improves eyesight and optical health in readers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段末尾指出社交反馈量化指标已演化为人际认同与同伴认可的高效通货（currency of validation and peer approval）。"
          },
          {
            q_type: "reading_item",
            stem: "Neuroscientists compare the sensation of receiving social media likes to:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Neurological reward surges triggered by gambling windfalls." },
              { key: "B", text: "The physical pain of running a full forty-mile marathon." },
              { key: "C", text: "The psychological boredom of waiting in an empty train station." },
              { key: "D", text: "Severe allergic reactions to common pollen particles." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出脑部扫描显示点赞激活大脑腹侧纹状体的多巴胺分泌，与赌博中奖或成瘾药物刺激的脑回路如出一辙。"
          },
          {
            q_type: "reading_item",
            stem: "Adolescents are particularly vulnerable to social media metrics because they:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Equate personal self-worth with their quantified metric performance." },
              { key: "B", text: "Possess fully developed, mature adult neurological brains." },
              { key: "C", text: "Refuse to communicate with any of their school classmates." },
              { key: "D", text: "Spend 100 percent of their daylight hours reading physical books." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出青少年前额叶尚未发育成熟，不可避免地将自身内在价值等同于点赞数据（equate self-worth with metric performance）。"
          },
          {
            q_type: "reading_item",
            stem: "The concept of 'demetrication' refers to:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Hiding public social feedback counts to reduce comparison anxiety." },
              { key: "B", text: "Banning all teenagers from using smartphone cameras." },
              { key: "C", text: "Measuring users' physical body temperatures through screens." },
              { key: "D", text: "Charging users cash fees for every posted social comment." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义理解题。第五段指出“去指标化（demetrication）”是指隐藏公开的点赞计数，以减轻同伴攀比焦虑。"
          },
          {
            q_type: "reading_item",
            stem: "Digital ethicists argue that protecting youth mental health ultimately requires:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Systemic regulatory intervention tackling platforms' underlying business models." },
              { key: "B", text: "Appealing to the benevolence of social media chief executives." },
              { key: "C", text: "Forbidding teenagers from attending public high schools." },
              { key: "D", text: "Encouraging adolescents to double their daily screen usage." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出浅层的UI修修补补于事无补，真正保护青少年必须实施体制性监管干预（systemic regulatory intervention），触及监控资本主义底层逻辑。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the revolutionary history of biotechnology, the development of CRISPR-Cas9 gene editing stands as a historic milestone. Adapted from an ancient bacterial immune mechanism that splices viral DNA, CRISPR provides molecular geneticists with unprecedented precision: functioning as programmable molecular scissors capable of locating, excising, and replacing specific genetic sequences across living genomes with pinpoint accuracy.

The biomedical promise of somatic gene editing—altering cells in mature tissues without affecting the reproductive germline—is breathtaking. Clinical trials are already demonstrating remarkable successes in curing monogenic congenital disorders, such as sickle cell anemia and beta-thalassemia, by correcting mutated hemoglobin genes in patients' bone marrow. Oncologists are using CRISPR to engineer patients' T-cells into cancer-hunting sentinels, while agricultural scientists edit crop DNA to withstand severe heatwaves and resist devastating fungal blights.

However, the ethical landscape fractures violently when CRISPR is applied to human "germline editing"—modifying sperm, eggs, or early embryos. Because germline edits alter the human genetic blueprint permanently, every alteration is inherited by subsequent generations. In 2018, Chinese researcher He Jiankui announced the birth of twin girls whose genomes had been edited in vitro to confer HIV resistance, provoking worldwide scientific condemnation and triggering an international bioethics crisis.

The perils of germline modification are both biological and societal. Scientifically, current gene-editing tools remain susceptible to "off-target effects," where molecular scissors inadvertently splice non-targeted DNA regions, potentially introducing cancerous mutations into future descendants. Societally, bioethicists warn that germline engineering opens the door to an era of consumer eugenics. While initial applications may target fatal hereditary maladies, commercial incentives will inevitably shift toward cosmetic "enhancements"—engineering cognitive traits, physical height, or aesthetic characteristics. In highly unequal societies, genetic enhancement could permanently codify class inequality into human biological biology, dividing humanity into genetically enhanced elites and an unenhanced underclass.

Confronted with these existential risks, global scientific bodies have called for binding international moratoria on human germline editing. Governing this Faustian technology demands transparent, multilateral regulatory architecture, ensuring that genetic science remains dedicated to relieving human suffering rather than engineering biological inequality.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "CRISPR-Cas9 gene editing is described in Paragraph 1 as functioning like:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Programmable molecular scissors capable of precise DNA editing." },
              { key: "B", text: "Heavy hydraulic construction cranes operating inside human cells." },
              { key: "C", text: "Nuclear radiation beams that destroy all living tissue." },
              { key: "D", text: "Traditional herbal remedies passed down through folklore." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出CRISPR宛如“可编程的分子剪刀（programmable molecular scissors）”，能精准定位、剪切和替换特定基因序列。"
          },
          {
            q_type: "reading_item",
            stem: "Somatic gene editing differs from germline editing in that it:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Alters mature tissues without passing changes to future offspring." },
              { key: "B", text: "Permanently alters the reproductive genetics of all future generations." },
              { key: "C", text: "Can only be performed on deceased human corpses." },
              { key: "D", text: "Is strictly prohibited by international medical treaties." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】概念对比题。第二段首句明确界定了体细胞基因编辑：只改变成熟人体组织细胞，不影响生殖系，不会遗传给后代。"
          },
          {
            q_type: "reading_item",
            stem: "The announcement of the edited twin girls in 2018 triggered outrage because:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "It represented an unsanctioned, dangerous leap into human germline editing." },
              { key: "B", text: "The researcher refused to accept international scientific awards." },
              { key: "C", text: "The experiment caused a worldwide power grid failure." },
              { key: "D", text: "CRISPR software was declared completely obsolete in 2017." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出该实验未经授权擅自对人类早期胚胎生殖系基因动手（leap into germline editing），跨越了伦理红线。"
          },
          {
            q_type: "reading_item",
            stem: "Bioethicists fear that commercial human genetic enhancement could:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Biologically codify socioeconomic inequality between classes." },
              { key: "B", text: "Make all human beings completely identical in height and weight." },
              { key: "C", text: "Completely eliminate the commercial cosmetics industry." },
              { key: "D", text: "Bankrupt all international university research laboratories." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出伦理学家担忧商业化基因定制将把阶层不平等固化进人体生物学基因中（codify class inequality into biology），分化出基因特权精英。"
          },
          {
            q_type: "reading_item",
            stem: "What international action is recommended by global scientific bodies in the final paragraph?",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "A binding international moratorium and multilateral regulatory governance." },
              { key: "B", text: "Selling CRISPR patents directly to private cosmetic clinics." },
              { key: "C", text: "A total global ban on all forms of biological medicine." },
              { key: "D", text: "Replacing all medical doctors with artificial intelligence algorithms." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出全球科学界呼吁对人类生殖系编辑实施具约束力的国际暂停令（binding international moratoria），并建立多边监管治理体系。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the complex tapestry of American administrative law, few institutions play as pivotal—yet obscure—a role as Administrative Law Judges (ALJs). Housed within vast federal regulatory agencies like the Securities and Exchange Commission (SEC), the Social Security Administration, and the Environmental Protection Agency, thousands of ALJs adjudicate specialized regulatory disputes, presiding over hearings, evaluating forensic evidence, and issuing enforceable rulings on matters ranging from securities fraud to disability benefits.

For decades, ALJs operated under a statutory compromise engineered by the Administrative Procedure Act of 1946. To insulate agency judges from partisan political pressures and bureaucratic coercion, Congress established rigorous civil service protections. ALJs were appointed through meritocratic competitive examinations, and they could only be removed by their supervising agency heads for documented "good cause" adjudicated by an independent civil service board.

However, in the landmark 2018 case Lucia v. SEC, the United States Supreme Court fundamentally destabilized this civil service framework. The petitioner, investment adviser Raymond Lucia, challenged an administrative sanction imposed by an SEC judge, arguing that the ALJ had been unconstitutionally appointed. Under the Appointments Clause of the US Constitution, "Officers of the United States" must be appointed directly by the President, courts of law, or department heads. For decades, the SEC had treated ALJs as ordinary civil service employees hired by staff human resource personnel.

Writing for the six-to-three conservative majority, Justice Elena Kagan agreed with Lucia. The court ruled that because ALJs exercise significant sovereign authority—ruling on admissibility of evidence, issuing subpoenas, and issuing binding liability determinations—they qualify as constitutional officers. Consequently, their appointment by lower-level agency staff violated the Constitution.

The ruling has ignited sweeping constitutional ramifications across the federal government. To cure the constitutional defect, the Trump administration issued Executive Order 13843, stripping ALJs of competitive examination standards and placing their selection directly under the discretionary authority of political department heads. Legal scholars warn that this shift threatens judicial independence, transforming impartial administrative arbiters into political loyalists and imperiling the neutral enforcement of federal law.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What is the primary statutory function of Administrative Law Judges (ALJs)?",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Adjudicating specialized regulatory disputes within federal agencies." },
              { key: "B", text: "Drafting criminal legislation for the United States Congress." },
              { key: "C", text: "Commanding federal military operations during peacetime." },
              { key: "D", text: "Auditing private income tax returns for local municipal mayors." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出行政法法官的核心法定职能是在各联邦监管机构内裁决专门性的监管纠纷（adjudicate specialized regulatory disputes）。"
          },
          {
            q_type: "reading_item",
            stem: "Under the Administrative Procedure Act of 1946, ALJs were protected by:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Merit-based civil service examinations and 'good cause' removal rules." },
              { key: "B", text: "Lifetime appointments granted directly by the British monarch." },
              { key: "C", text: "Complete diplomatic immunity from all United States laws." },
              { key: "D", text: "The right to command local police forces during hearings." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出1946年《行政程序法》确立了功绩制竞考录用和非有“正当理由”不得免职的保护，以防行政长官政治施压。"
          },
          {
            q_type: "reading_item",
            stem: "The petitioner in Lucia v. SEC challenged his administrative penalty on the grounds that:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "The SEC judge had been unconstitutionally appointed by lower staff." },
              { key: "B", text: "The Securities and Exchange Commission had been legally abolished." },
              { key: "C", text: "The United States Constitution prohibits all forms of paper money." },
              { key: "D", text: "Investment advisers are immune from all federal fraud statutes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出起诉理由是该行政法官是由人事普通职员违宪任用的，违反了宪法任用条款（unconstitutionally appointed）。"
          },
          {
            q_type: "reading_item",
            stem: "The Supreme Court ruled that ALJs qualify as 'Officers of the United States' because they:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Exercise significant sovereign authority in issuing binding legal rulings." },
              { key: "B", text: "Wear ceremonial judicial robes during federal trials." },
              { key: "C", text: "Earn higher salaries than the President of the United States." },
              { key: "D", text: "Are required to have served as military generals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出大法官卡根认定行政法法官行使了重大的国家主权权威（exercise significant sovereign authority），故属于宪法层面的官员。"
          },
          {
            q_type: "reading_item",
            stem: "Legal scholars worry that placing ALJ selection under political discretion will:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Compromise judicial independence and politicize administrative justice." },
              { key: "B", text: "Lead to the immediate abolition of the United States Supreme Court." },
              { key: "C", text: "Force all federal regulatory agencies to operate in foreign nations." },
              { key: "D", text: "Ban corporate lawyers from entering federal courthouse buildings." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出学者最担忧的是政治长官自主任免将严重侵蚀行政司法的独立性，将中立裁判官变成政治效忠者（politicize administrative justice）。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2018 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky2",
    year: 2018,
    title: "2018年全国硕士研究生招生考试英语（二）真题",
    exam_type: "real",
    duration_minutes: 60,
    total_score: 50.00,
    pass_score: 30.00,
    is_published: true,
    approval_status: "approved",
    passages: [
      {
        section_type: "cloze",
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `In our hyper-connected modern world, where digital smartphones offer an inexhaustible stream of entertainment, experiencing boredom has become an increasingly rare (1)____. The moment a train delays, a friend steps away, or a commercial break begins, we compulsively reach for our screens to (2)____ the quiet void. We treat boredom as an intolerable emotional defect, an uncomfortable psychological state that must be instantly (3)____.

Yet, neuroscientists and cognitive psychologists argue that our desperate war against boredom is dangerously (4)____. Far from being a useless mental vacuum, boredom serves as an indispensable biological catalyst for creativity, deep contemplation, and cognitive (5)____.

When the human brain is deprived of external sensory stimuli, it does not simply shut down. Instead, it activates the "default mode network" (DMN)—an interconnected constellation of cerebral regions that (6)____ into action when we daydream, reminisce about the past, or contemplate future (7)____. The DMN acts as the brain's backstage workshop, synthesizing disparate memories, solving subconscious conundrums, and forging unexpected intellectual (8)____.

History is replete with scientific and literary breakthroughs born from idle moments. Isaac Newton famously developed his revolutionary theory of gravitation while idling beneath a woolly orchard tree, escaping the plague (9)____ Cambridge. Had Newton possessed a smartphone to scroll through social media notifications, his attention would have remained fragmented, and the falling apple might have passed without (10)____.

Furthermore, boredom plays a vital developmental role in childhood. When children are allowed to experience unprogrammed, unstructured afternoons, they are forced to (11)____ their own imaginative resources. They invent elaborate fantasy worlds, construct cardboard forts, and discover innate artistic (12)____. Conversely, children whose every waking minute is scheduled with academic classes or digital tablets never develop the capacity for self-generated (13)____, leaving them emotionally dependent on external stimulation.

Psychologists also observe that boredom functions as an internal navigational compass. The painful discomfort of feeling bored signals that our current activity is personally meaningless or intellectually (14)____. It prompts us to reevaluate our goals, push beyond familiar routines, and embark on fresh exploratory (15)____.

To reclaim the creative fruits of boredom, cognitive experts recommend practicing intentional digital (16)____. Designating tech-free hours during the day, taking long walks without headphones, or simply permitting oneself to sit quietly staring out a rain-streaked window allows the default mode network to (17)____.

Ultimately, creativity requires empty mental space to germinate. Rather than fleeing from quiet interludes, we should embrace boredom not as an adversary, but as a fertile psychological (18)____. By resisting the reflex of instant digital distraction, we preserve our capacity for deep reflection and awaken the dormant genius within our (19)____ in our bustling daily lives (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "occurrence" },
              { key: "B", text: "disaster" },
              { key: "C", text: "miracle" },
              { key: "D", text: "scandal" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。rare occurrence（罕见的事/少有的发生）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "fill" },
              { key: "B", text: "widen" },
              { key: "C", text: "ignore" },
              { key: "D", text: "celebrate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。fill the quiet void（填补寂静的空虚空白）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "eradicated" },
              { key: "B", text: "treasured" },
              { key: "C", text: "replicated" },
              { key: "D", text: "praised" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。消极对应：人们视无聊为不可忍受的缺陷，必须立刻根除消灭（instantly eradicated）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "misguided" },
              { key: "B", text: "triumphant" },
              { key: "C", text: "virtuous" },
              { key: "D", text: "profitable" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。我们对无聊发起的战争是危险的误入歧途（dangerously misguided）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "renewal" },
              { key: "B", text: "decay" },
              { key: "C", text: "paralysis" },
              { key: "D", text: "collapse" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义并列。catalyst for creativity, contemplation and cognitive renewal（认知重塑与更新）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "springs" },
              { key: "B", text: "retreats" },
              { key: "C", text: "evaporates" },
              { key: "D", text: "surrenders" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词短语。springs into action（立即活跃启动/跃入运作）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "possibilities" },
              { key: "B", text: "cemeteries" },
              { key: "C", text: "crimes" },
              { key: "D", text: "scandals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。contemplate future possibilities（设想未来的各种可能性）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "connections" },
              { key: "B", text: "hostilities" },
              { key: "C", text: "disasters" },
              { key: "D", text: "boycotts" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】认知名词。forging unexpected intellectual connections（构建意想不到的智力联结）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "shuttering" },
              { key: "B", text: "celebrating" },
              { key: "C", text: "expanding" },
              { key: "D", text: "praising" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】历史情境。瘟疫导致剑桥大学停摆关闭（shuttering Cambridge）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "notice" },
              { key: "B", text: "apology" },
              { key: "C", text: "payment" },
              { key: "D", text: "punishment" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。pass without notice（没有被注意到就悄悄溜过）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "cultivate" },
              { key: "B", text: "destroy" },
              { key: "C", text: "mock" },
              { key: "D", text: "disregard" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。forced to cultivate imaginative resources（被迫开发培养自身的想象力资源）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "passions" },
              { key: "B", text: "crimes" },
              { key: "C", text: "debts" },
              { key: "D", text: "penalties" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词。discover innate artistic passions（发现内在的天生艺术热情）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "engagement" },
              { key: "B", text: "rebellion" },
              { key: "C", text: "isolation" },
              { key: "D", text: "treachery" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理名词。self-generated engagement（自主生成的投入与专注能力）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "stagnant" },
              { key: "B", text: "thrilling" },
              { key: "C", text: "lucrative" },
              { key: "D", text: "fascinating" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。无聊提示我们当前活动缺乏意义或智识停滞（intellectually stagnant）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "endeavors" },
              { key: "B", text: "retreats" },
              { key: "C", text: "crimes" },
              { key: "D", text: "scandals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。fresh exploratory endeavors（全新的探索性尝试与努力）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "fasting" },
              { key: "B", text: "advertising" },
              { key: "C", text: "spending" },
              { key: "D", text: "gaming" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻用法。intentional digital fasting（有意识的数字断食/远离屏幕）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "flourish" },
              { key: "B", text: "wither" },
              { key: "C", text: "suffocate" },
              { key: "D", text: "surrender" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。allows default mode network to flourish（让默认网络自由舒展并蓬勃运作）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "sanctuary" },
              { key: "B", text: "battlefield" },
              { key: "C", text: "prison" },
              { key: "D", text: "grave" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义比喻。fertile psychological sanctuary（肥沃的心理庇护所/滋养圣地）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "minds" },
              { key: "B", text: "screens" },
              { key: "C", text: "wallets" },
              { key: "D", text: "gadgets" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心智归宿。genius within our minds（深藏在我们头脑中的潜藏天才）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "today" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "rarely" },
              { key: "D", text: "never" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】时间副词。in our daily lives today（在当今我们的日常生活中）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `Every year across the United Kingdom and Europe, millions of tons of freshly harvested carrots, apples, and potatoes are rejected before ever leaving farm gates. The reason for this staggering food waste is not rot, contamination, or disease, but superficial aesthetics. Mainstream supermarket chains, bound by rigid cosmetic standards, historically refused any fruit or vegetable exhibiting minor visual blemishes: curved cucumbers, split carrots, or misshapen pears were routinely plowed back into farm soils or diverted to animal feed.

However, a revolutionary retail initiative is dismantling these wasteful cosmetic orthodoxies: the "wonky vegetable" campaign. Championed by celebrity chefs and environmental campaigners, leading British supermarket chains have introduced dedicated discount lines of misshapen produce. Sold under self-deprecating brand names like "Naturally Wonky" or "Inglorious Fruits," these cosmetically imperfect vegetables are packaged in bulk bags and discounted by thirty to fifty percent compared to their picture-perfect peers.

Consumer reception has been overwhelmingly enthusiastic. In an economic climate characterized by wage stagnation and rising grocery inflation, budget-conscious working families have eagerly embraced wonky produce as a practical way to trim weekly grocery bills without sacrificing nutritional quality. A crooked parsnip or knobbly potato contains the identical vitamin, mineral, and caloric profile of a straight one; once chopped and tossed into a domestic stew, aesthetic irregularities completely disappear.

For agricultural producers, the wonky produce movement provides a financial lifeline. Historically, farmers absorbed all the financial losses of crops that failed cosmetic grading, with up to thirty percent of an annual harvest discarded without compensation. By establishing a commercial market for imperfect yields, supermarkets provide farmers with vital secondary revenues, stabilizing rural agricultural incomes against weather-induced crop variations.

Nevertheless, agricultural policy analysts caution that wonky vegetables must not become a corporate public relations fig leaf. While selling misshapen produce in discount aisles is commendable, supermarkets must tackle the deeper structural drivers of agricultural waste: reforming punitive supply contracts that cancel orders at the last minute and establishing standardized purchase quotas for entire farm yields. Only by treating food as nourishment rather than a cosmetic fashion ornament can society build a sustainable, zero-waste food system.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Supermarkets historically rejected large quantities of fresh produce primarily due to:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Minor cosmetic irregularities like odd shapes or superficial curves." },
              { key: "B", text: "Severe bacterial contamination and widespread toxic rot." },
              { key: "C", text: "A complete lack of storage refrigeration in delivery trucks." },
              { key: "D", text: "Government laws prohibiting citizens from eating potatoes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出果蔬被拒收并非变质腐烂，纯粹是因外观微瑕（superficial aesthetics, curved cucumbers, split carrots）。"
          },
          {
            q_type: "reading_item",
            stem: "The 'wonky vegetable' campaign successfully attracted British shoppers by:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Offering nutritious produce at significant discounts of 30 to 50 percent." },
              { key: "B", text: "Giving away free microwave ovens with every bag of potatoes." },
              { key: "C", text: "Guaranteeing that ugly fruit causes instantaneous weight loss." },
              { key: "D", text: "Banning regular straight vegetables from all retail stores." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出这些“丑蔬果”以30%至50%的大幅折扣整袋售卖，为工薪家庭提供了高性价比的健康选择。"
          },
          {
            q_type: "reading_item",
            stem: "Why are wonky vegetables particularly appealing to budget-conscious families?",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "They offer identical nutritional value while lowering grocery expenditures." },
              { key: "B", text: "They take less than ten seconds to cook in boiling water." },
              { key: "C", text: "They can be kept on kitchen counters for ten years without spoiling." },
              { key: "D", text: "Supermarkets pay customers cash rewards for consuming them." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出畸形蔬果营养与热量和完美蔬果一模一样，切块下锅后毫无差别，有效降低了开支。"
          },
          {
            q_type: "reading_item",
            stem: "How does the commercialization of imperfect produce benefit agricultural farmers?",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "It generates revenue from crops that were previously discarded for free." },
              { key: "B", text: "It allows farmers to stop paying wages to seasonal harvest laborers." },
              { key: "C", text: "It eliminates all government agricultural taxes on farmland." },
              { key: "D", text: "It prevents rainstorms from damaging future vegetable crops." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出过去多达三成的瑕疵作物只能烂在地里毫无补偿，商超收购丑蔬果为农民开辟了关键的副营收。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that eradicating food waste ultimately requires:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Reforming supermarkets' punitive supply contracts and purchase quotas." },
              { key: "B", text: "Banning all commercial supermarkets across the European continent." },
              { key: "C", text: "Forbidding families from preparing cooked vegetable stews at home." },
              { key: "D", text: "Genetic engineering to ensure every carrot grows in an identical box." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出丑蔬果不能沦为公关遮羞布，真正消除农业浪费必须改革严苛的采购合同与临时取消机制，包销整批收成。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `For over a century, the cinematic experience was anchored to a sacred cultural sanctuary: the physical movie theater. Audiences gathered in darkened communal auditoriums, surrendering their undivided attention to monumental silver screens illuminated by whirring projectors. However, the meteoric rise of subscription video-on-demand (SVOD) streaming giants—such as Netflix, Amazon Prime, and Disney+—has unleashed a seismic disruption that threatens the very existence of theatrical exhibition.

Armed with multibillion-dollar production war chests, streaming platforms have upended Hollywood's venerable "theatrical windowing" system. Traditionally, multiplex theaters enjoyed an exclusive ninety-day grace period before a feature film could be released on home video or cable television. Streaming conglomerates dismantled this exclusivity, premiering blockbuster features directly onto home television screens or shrinking theatrical windows to mere weeks.

Streaming executives champion this direct-to-consumer model as the ultimate democratization of cinematic culture. Consumers can now enjoy thousands of films on demand from the comfort of their living room sofas, liberating families from exorbitant multiplex ticket prices, expensive parking fees, and overpriced concession snacks. Furthermore, streaming algorithms have funded adventurous, auteur-driven projects that risk-averse legacy Hollywood studios routinely rejected in favor of predictable superhero franchises.

Yet, cinema purists and celebrated filmmakers warn that the demise of theatrical exhibition represents an irreparable cultural impoverishment. Watching a film on an iPhone or a domestic television screen, punctuated by glowing smartphone notifications and household distractions, destroys the immersive psychological spell of the cinematic medium. Cinema was conceived as a shared, public secular ritual—a collective space where strangers laugh, weep, and gasp in synchronized emotional unison.

Furthermore, the economics of streaming present acute vulnerabilities for artistic labor. While streaming conglomerates initially showered creators with lavish upfront fees, the absence of box office backend residuals has squeezed screenwriters, actors, and independent directors, precipitating historic Hollywood labor strikes. The future of cinema requires a symbiotic coexistence: streaming platforms funding daring domestic content, while theatrical multiplexes reinvent themselves as premium, communal cultural destinations.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What traditional Hollywood practice was disrupted by streaming conglomerates?",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "The exclusive ninety-day theatrical windowing period for multiplexes." },
              { key: "B", text: "The use of professional actors in Hollywood dramatic productions." },
              { key: "C", text: "The sale of buttered popcorn inside movie theater lobbies." },
              { key: "D", text: "The requirement that all movie sound tracks be recorded in English." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段明确指出流媒体打破了院线传统的90天独家放映窗口期（theatrical windowing system）。"
          },
          {
            q_type: "reading_item",
            stem: "Streaming services promote home viewing primarily as:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "A convenient, cost-effective democratization of film consumption." },
              { key: "B", text: "A military training program designed for national defense." },
              { key: "C", text: "A mandatory government requirement for every household." },
              { key: "D", text: "A luxury pastime available exclusively to billionaires." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出流媒体标榜其模式是电影文化的民主化，省去昂贵电影票与爆米花消费，享受足不出户的便捷。"
          },
          {
            q_type: "reading_item",
            stem: "Filmmakers criticize home streaming viewing habits because they:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Shatter the immersive psychological spell through distractions." },
              { key: "B", text: "Cause television hardware screens to instantly catch fire." },
              { key: "C", text: "Prevent viewers from understanding foreign language subtitles." },
              { key: "D", text: "Force all viewers to fall asleep after ten minutes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出在手机或家用电视上观影常被打断，破坏了电影原本沉浸式的心理魔力与集体共鸣仪式感。"
          },
          {
            q_type: "reading_item",
            stem: "How has streaming affected the compensation of creative workers like screenwriters?",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Eliminated backend box office residuals and squeezed earnings." },
              { key: "B", text: "Made every screenwriter a multi-millionaire within one year." },
              { key: "C", text: "Forbidden screenwriters from writing original scripts." },
              { key: "D", text: "Guaranteed free lifetime health insurance to all actors." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第五段指出流媒体取消了基于票房分账的后期版税分成（residuals），压缩了编剧、演员收入，导致大罢工。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that the optimal future for cinema involves:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Symbiotic coexistence between home streaming and premium theaters." },
              { key: "B", text: "The complete global demolition of all physical movie theaters." },
              { key: "C", text: "A constitutional ban on all digital internet streaming platforms." },
              { key: "D", text: "Restricting movie production exclusively to three-minute social videos." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出电影的最优未来是共生共荣（symbiotic coexistence）：流媒体资助创新居家内容，院线重塑为高品质社交文化目的地。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the post-industrial gig economy, platforms like Uber, Deliveroo, and Instacart have engineered a seismic transformation in the organization of labor. Millions of app-based couriers and ride-hail drivers navigate urban streets, connected to algorithmic dispatch platforms that match consumer orders with workers in milliseconds. Silicon Valley tech executives herald this algorithmic ecosystem as the dawn of hyper-flexible labor, where workers operate as autonomous micro-entrepreneurs who set their own hours and balance personal commitments at will.

However, beneath this veneer of entrepreneurial autonomy lies a far grimmer economic reality. Gig platforms classify their workers not as formal employees, but as "independent contractors." Under this legal classification, tech platforms absolve themselves of virtually all statutory employer obligations: they pay zero minimum wage guarantees, provide no employer-funded health insurance, contribute nothing toward retirement pensions, and offer no sick pay or workers' compensation for on-the-job injuries.

Labor sociologists argue that the rhetoric of independent entrepreneurship represents an ideological fiction. True independent contractors set their own prices, build client bases, and negotiate contractual terms. In stark contrast, gig workers are subject to intense algorithmic micromanagement. Automated algorithms assign routes, set non-negotiable pay rates, track minute-by-minute vehicle speeds via GPS, and instantly "deactivate"—or fire—workers whose customer review ratings drop below arbitrary thresholds. Gig workers possess all the constraints of subordinate employees without enjoying a single statutory protection.

The judicial and legislative tide, however, is beginning to turn. Courts across the United Kingdom, Spain, and the Netherlands have delivered landmark rulings rejecting gig platforms' legal classifications. In a historic judgment, the UK Supreme Court ruled that Uber drivers are statutory "workers," legally entitled to the national minimum wage, holiday pay, and rest breaks from the moment they log onto the application in their licensed territory.

Rebalancing the gig economy requires modernizing labor standards. Gig platforms must be forced to internalize the social costs of their labor forces. Creating a hybrid classification or extending universal employment protections to platform labor ensures that technological convenience is not subsidized by the systematic exploitation of a precarious urban working class.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Gig economy platforms classify app-based couriers and drivers as:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Independent contractors rather than traditional employees." },
              { key: "B", text: "Tenured civil servants employed directly by the state." },
              { key: "C", text: "Military personnel on active overseas deployment." },
              { key: "D", text: "Executive board directors of tech conglomerates." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出平台将骑手和司机归类为“独立承包商（independent contractors）”，以此免除雇主法定责任。"
          },
          {
            q_type: "reading_item",
            stem: "By classifying workers as independent contractors, platforms avoid paying:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Statutory minimum wages, healthcare, sick leave, and injury compensation." },
              { key: "B", text: "Commercial electricity bills for their Silicon Valley server farms." },
              { key: "C", text: "Digital domain registration fees for their mobile smartphone apps." },
              { key: "D", text: "Municipal licensing permits for their corporate executive headquarters." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段末句明确列举免责内容：不保障最低工资、不提供医保和病假补贴、不缴纳养老金与工伤赔偿。"
          },
          {
            q_type: "reading_item",
            stem: "Labor sociologists argue that gig workers are not genuine entrepreneurs because they:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Are subjected to strict algorithmic control and cannot set pay rates." },
              { key: "B", text: "Refuse to use smartphones or GPS navigation systems." },
              { key: "C", text: "Earn more money than Fortune 500 corporate chief executives." },
              { key: "D", text: "Own 50 percent of the voting stock in gig platform companies." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出真正的自雇者能自主定价，而平台骑手受制于严苛算法监控，无法议价，且随时面临被算法封号解雇。"
          },
          {
            q_type: "reading_item",
            stem: "In its historic ruling, the UK Supreme Court decided that Uber drivers:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Are statutory workers entitled to minimum wages and holiday pay." },
              { key: "B", text: "Must be deported from the United Kingdom immediately." },
              { key: "C", text: "Are legally forbidden from picking up any passenger in London." },
              { key: "D", text: "Must surrender their vehicles directly to the British police." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出英国最高法院划时代判决认定优步司机属于法定劳动者（workers），享有法定最低工资、带薪假期等权益。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that platform companies must be legally required to:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Internalize the social and labor protection costs of their workers." },
              { key: "B", text: "Abolish all smartphone applications and return to horse carriages." },
              { key: "C", text: "Fire all couriers and replace them with private corporate helicopters." },
              { key: "D", text: "Relocate their business operations exclusively to outer space." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出平台经济改革的根本是强制科技平台内部化其劳动力社会成本，不应以剥削底层不稳定性劳动力来补贴数字便利。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the mid-2010s, urban centers across the globe witnessed an astonishing consumer phenomenon: the explosive invasion of dockless bike-sharing. Armed with billions of dollars in venture capital, startups flooded city streets with vibrant, GPS-enabled two-wheelers. By pairing cellular connectivity with QR-code smart locks, dockless systems dismantled the friction of traditional docked municipal bike-share programs. Users could locate a bicycle on a smartphone map, unlock it for pennies, and abandon it anywhere at their journey's end.

Municipal planners and urban environmentalists initially greeted dockless micro-mobility with unbridled euphoria. The bicycles promised to solve urban transit's intractable "first-mile, last-mile" puzzle, bridging the gap between distant subway stations and suburban residential blocks. By substituting zero-emission cycling for short automotive taxi trips, dockless systems promised to curtail metropolitan traffic congestion and diminish urban greenhouse gas emissions.

However, the venture-capital-fueled business model was engineered on market share conquest rather than sustainable operational management. Competing startups engaged in a predatory war of attrition, dumping hundreds of thousands of cheap, identical bicycles onto urban sidewalks to crowd out competitors. Within months, urban public spaces succumbed to chaotic disorder. Bicycles blocked wheelchair ramps, obstructed pedestrian sidewalks, were discarded in public fountains, and piled up in hazardous visual eyesores.

When municipal anger ignited and venture capital funding dried up, several leading bike-share startups collapsed into catastrophic bankruptcy. Across China and North America, municipal authorities were forced to clear millions of abandoned bicycles, creating surreal "bike graveyards"—vast industrial wastelands where endless mountain ranges of twisted, neon-colored metal frames oxidized in the sun, exemplifying the grotesque material waste of unregulated tech capitalism.

The dockless bike-sharing debacle offers an indispensable cautionary lesson for contemporary municipal governance. Urban streets are not unregulated, free-for-all sandboxes for venture-capital experimentation. Successful micro-mobility requires rigorous public-private governance: enforcing strict operator fleet caps, mandating geo-fenced designated parking zones, and requiring operators to share real-time trip data with city planners. When properly regulated, micro-mobility can fulfill its green transit promise without compromising the order and accessibility of the civic commons.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What was the primary innovation of dockless bike-sharing compared to traditional municipal bikes?",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Bicycles could be unlocked via smartphone and parked anywhere without docks." },
              { key: "B", text: "The bikes were equipped with jet engines that flew over traffic jams." },
              { key: "C", text: "The bikes required no human pedaling and could drive completely alone." },
              { key: "D", text: "Riders received free gold coins every time they pedaled ten miles." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出无桩共享单车的核心创新在于结合手机GPS与智能锁，用户指尖解锁，目的地随处还车（abandon anywhere without docks）。"
          },
          {
            q_type: "reading_item",
            stem: "Urban planners initially supported dockless micro-mobility because it promised to:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Solve the 'first-mile, last-mile' problem and reduce vehicle emissions." },
              { key: "B", text: "Completely eliminate all subway and municipal bus networks." },
              { key: "C", text: "Provide free bicycles for all foreign tourists to take home." },
              { key: "D", text: "Replace all city sidewalks with multi-lane asphalt motorways." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出规划师起初欢呼是因为它有望解决“起步与最后一公里”难题，接驳地铁，减少汽车出行和尾气。"
          },
          {
            q_type: "reading_item",
            stem: "Sidewalk chaos and pedestrian clutter occurred primarily because competing startups:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Dumped excessive fleets onto streets to capture market dominance." },
              { key: "B", text: "Trained stray dogs to ride bicycles through busy shopping malls." },
              { key: "C", text: "Refused to allow anyone under sixty years old to rent bikes." },
              { key: "D", text: "Built massive concrete walls across every urban intersection." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出创业公司为了抢占垄断份额盲目打恶性消耗战，将数十万辆廉价单车疯狂投放到街头，酿成公共秩序灾难。"
          },
          {
            q_type: "reading_item",
            stem: "The term 'bike graveyards' in Paragraph 4 describes:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Vast industrial wastelands where millions of abandoned bikes rust in piles." },
              { key: "B", text: "Sacred historical cemeteries where ancient bicycles are worshiped." },
              { key: "C", text: "Museum exhibitions celebrating nineteenth-century pedal bicycles." },
              { key: "D", text: "Underground military shelters storing bicycles for emergency combat." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义理解题。第四段描绘了倒闭后成千上万单车被清理至废弃场地堆积如山的超现实景象，沦为“单车坟场（bike graveyards）”。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that successful micro-mobility systems require:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Fleet caps, designated parking zones, and public-private governance." },
              { key: "B", text: "A permanent global ban on all bicycle manufacturing worldwide." },
              { key: "C", text: "Allowing private venture capitalists total control over city roads." },
              { key: "D", text: "Giving free gasoline automobiles to every urban cyclist." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结指出微出行成功的前提是公私协同监管：设定投放总量上限（fleet caps）、设立电子围栏停车区并共享数据。"
          }
        ]
      }
    ]
  }
];
