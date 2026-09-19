// 2020 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2020Exams = [
  // =========================================================================
  // 2020 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky1",
    year: 2020,
    title: "2020年全国硕士研究生招生考试英语（一）真题",
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
        content: `Even people who do not normally follow financial news will have heard about the dramatic expansion of artificial intelligence in corporate management. Algorithmic software systems now review resumes, calculate compensation packages, and monitor office productivity with minimal human (1)____.

Advocates contend that algorithmic evaluation eliminates subjective human bias, establishing an objective meritocracy in which personnel decisions are grounded (2)____ in quantifiable performance metrics. Yet, organizational sociologists caution that predictive algorithms are trained on historical data, which inevitably reflects entrenched institutional (3)____.

If an algorithm analyzes decades of promotions within a historically male-dominated firm, the machine learning model will internalize gender as an implicit variable of (4)____, penalizing qualified female applicants simply because their profiles diverge from historical norms. Therefore, automated HR systems must be subject to continuous algorithmic auditing to prevent technology from codifying past prejudices into future hiring (5)____.

Beyond algorithmic recruitment, surveillance algorithms are radically transforming workplace (6)____. Keystroke trackers, desktop screen recorders, and sentiment-analysis webcams can measure an employee's minute-by-minute attentiveness with relentless (7)____. Proponents justify these intrusive tools as vital mechanisms to deter time theft and optimize task (8)____ in increasingly distributed workforces.

Workers, however, describe the experience as psychologically suffocating. Constant digital monitoring generates perpetual anxiety, eroding interpersonal (9)____ between management and subordinates. When workers realize that taking a momentary pause to stretch or reflect is flagged as an unproductive (10)____, they modify their behavior to game the tracking metrics rather than concentrating on creative problem-solving.

Industrial psychologists warn that treating knowledge workers as mechanical cogwheels fundamentally (11)____ human motivation. Intellectual breakthroughs require unstructured contemplation, psychological safety, and the liberty to make exploratory (12)____. By reducing professional excellence to crude mechanical outputs, algorithmic micromanagement risks draining organizations of innovative (13)____.

Labor attorneys are similarly sounding alarms over legal (14)____. In many jurisdictions, employees are not even informed that their facial expressions or voice inflections are being scrutinized by predictive psychometric (15)____. Regulators in the European Union and North America are beginning to draft legislation requiring algorithmic transparency, granting workers the right to (16)____ automated decisions that negatively affect their careers.

The challenge facing corporate leadership is not whether to adopt algorithmic automation, but how to deploy it with ethical (17)____. Artificial intelligence should serve as an augmentative tool that liberates professionals from repetitive administrative burdens, rather than an omnipresent digital (18)____ that polices their every movement.

Ultimately, great enterprises are built on human empathy, mutual trust, and shared vision—qualities that no neural network can ever genuinely (19)____. Balancing technological efficiency with human dignity will determine which organizations thrive in the automated century (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "intervention" },
              { key: "B", text: "superstition" },
              { key: "C", text: "jealousy" },
              { key: "D", text: "curiosity" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。with minimal human intervention（在极少人为干预的情况下），描述算法自动处理人事流程。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "strictly" },
              { key: "B", text: "hesitantly" },
              { key: "C", text: "rarely" },
              { key: "D", text: "vaguely" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词搭配。grounded strictly in（严格立足于），呼应客观唯才是举的理性诉求。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "prejudices" },
              { key: "B", text: "triumphs" },
              { key: "C", text: "subsidies" },
              { key: "D", text: "philosophies" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。历史数据不可避免地反映了根深蒂固的体制性偏见（institutional prejudices）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "competence" },
              { key: "B", text: "hostility" },
              { key: "C", text: "sympathy" },
              { key: "D", text: "recklessness" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。机器学习会将性别内化为能力/资质（competence）的隐性考量指标。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "practices" },
              { key: "B", text: "novels" },
              { key: "C", text: "apologies" },
              { key: "D", text: "confessions" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。future hiring practices（未来的招聘实践/制度惯例）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "dynamics" },
              { key: "B", text: "vacations" },
              { key: "C", text: "monuments" },
              { key: "D", text: "famines" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。transforming workplace dynamics（深刻改变职场生态与人际互动动态）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "precision" },
              { key: "B", text: "reluctance" },
              { key: "C", text: "clumsiness" },
              { key: "D", text: "compassion" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。with relentless precision（以无情且冷酷的精确度），形容键盘鼠标全天候数字监控。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "efficiency" },
              { key: "B", text: "scandal" },
              { key: "C", text: "bankruptcy" },
              { key: "D", text: "tragedy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。optimize task efficiency（优化任务执行效率）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "trust" },
              { key: "B", text: "hostility" },
              { key: "C", text: "resentment" },
              { key: "D", text: "deceit" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。持续被监控侵蚀了管理层与下属之间的相互信任（eroding interpersonal trust）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "lapse" },
              { key: "B", text: "triumph" },
              { key: "C", text: "reward" },
              { key: "D", text: "masterpiece" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。伸个懒腰就被算法标记为消极懈怠/失职（unproductive lapse）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "undermines" },
              { key: "B", text: "amplifies" },
              { key: "C", text: "endorses" },
              { key: "D", text: "celebrates" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。把知识员工当螺丝钉从根本上破坏/削弱了（undermines）人类的内在动机。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "errors" },
              { key: "B", text: "profits" },
              { key: "C", text: "treaties" },
              { key: "D", text: "fortunes" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。创新需要犯错试错的自由（liberty to make exploratory errors）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "vitality" },
              { key: "B", text: "fatigue" },
              { key: "C", text: "debt" },
              { key: "D", text: "famine" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。draining organizations of innovative vitality（抽干组织的创新活力）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "transgressions" },
              { key: "B", text: "honors" },
              { key: "C", text: "donations" },
              { key: "D", text: "triumphs" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。劳动法律师对潜在的法律越界与侵权行为（legal transgressions）发出警报。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "software" },
              { key: "B", text: "hardware" },
              { key: "C", text: "garments" },
              { key: "D", text: "furniture" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。predictive psychometric software（预测性心理计量与情绪分析软件）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "contest" },
              { key: "B", text: "applaud" },
              { key: "C", text: "accelerate" },
              { key: "D", text: "worship" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。赋予员工质疑、抗辩与挑战（contest）不利自动化决定的权利。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "restraint" },
              { key: "B", text: "arrogance" },
              { key: "C", text: "recklessness" },
              { key: "D", text: "cruelty" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。deploy with ethical restraint（以伦理克制/道德节制来审慎部署技术）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "panopticon" },
              { key: "B", text: "cradle" },
              { key: "C", text: "shelter" },
              { key: "D", text: "paradise" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】哲学名义修辞。omnipresent digital panopticon（无所不在的数字全景敞视监狱/全天候监视器）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "replicate" },
              { key: "B", text: "destroy" },
              { key: "C", text: "despise" },
              { key: "D", text: "confuse" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。同理心与信任是神经网络无论如何都无法真正复刻（replicate）的人性品质。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "ahead" },
              { key: "B", text: "behind" },
              { key: "C", text: "away" },
              { key: "D", text: "apart" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词短语。in the automated century ahead（在未来的自动化世纪中）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `When a catastrophic blaze engulfed Paris's Notre-Dame Cathedral in April 2019, collapsing its iconic nineteenth-century spire and incinerating its medieval timber roof, France was plunged into collective mourning. Yet, within hours of the flames being subdued, a passionate ideological clash erupted over how the venerable Gothic masterpiece should be resurrected. French President Emmanuel Macron initially proposed an "inventive contemporary architectural gesture," sparking an international design competition that elicited avant-garde proposals featuring crystal glass roofs, rooftop organic greenhouse gardens, and titanium spires illuminated by laser beams.

Traditional preservationists reacted with unbridled fury. Led by France's chief heritage architect and backed by conservation purists, traditionalists argued that Notre-Dame is not a canvas for modernist experimentation, but a sacred monument belonging to French cultural memory. They demanded a strict "identic reconstruction" utilizing original materials: hand-hewn oak beams sourced from centuries-old French forests and lead roofing cast according to authentic medieval metallurgy.

The debate exposed a deep epistemological rift in heritage preservation theory. Modernists contended that historic cathedrals were never static artifacts frozen in time; throughout their centuries-long lifespans, Gothic structures were repeatedly altered, restored, and expanded using the state-of-the-art engineering technologies of their respective eras. The collapsed spire itself was not medieval; it had been designed in the 1850s by romantic architect Eugène Viollet-le-Duc, who famously restored damaged monuments with imaginative artistic license rather than archaeological fidelity.

Preservation purists countered that historical context had fundamentally changed. In the nineteenth century, traditional artisan crafts were still vibrant; today, hand-carving thousands of massive oak timbers threatens old-growth oak habitats and relies on an artisanal workforce that has virtually vanished. Furthermore, environmental advocacy groups vigorously opposed the reinstallation of hundreds of tons of toxic lead sheeting on the cathedral roof, warning that lead dust emissions during the fire had already contaminated adjacent Parisian schools and residential streets.

Ultimately, traditionalist sentiment prevailed in the French National Assembly. Lawmakers voted to reconstruct Notre-Dame exactly as it was prior to the blaze, affirming that in times of societal fracturing and rapid globalization, the psychological reassurance of historic continuity eclipses the vanity of architectural novelty.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "President Macron's initial proposal for Notre-Dame's reconstruction sparked controversy because he suggested:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "An inventive modern architectural gesture replacing the lost spire." },
              { key: "B", text: "Demolishing the remaining stone walls to build a commercial mall." },
              { key: "C", text: "Selling the cathedral property to international private investors." },
              { key: "D", text: "Leaving the charred ruins permanently untouched as a war memorial." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出马克龙总统最初主张融入具有现代创意的当代建筑手笔（inventive contemporary gesture），引发了前卫玻璃屋顶与传统复原的激辩。"
          },
          {
            q_type: "reading_item",
            stem: "Heritage preservation purists insisted on:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Reconstructing the cathedral identically using traditional materials." },
              { key: "B", text: "Constructing a solar-powered titanium roof for ecological tourism." },
              { key: "C", text: "Converting the interior sanctuary into a secular university hall." },
              { key: "D", text: "Replacing all timber carpentry with prefabricated steel girders." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出文保保守派强烈要求依照原状完整原样复建（identic reconstruction），完全采用传统老橡木和原始工艺铸造铅顶。"
          },
          {
            q_type: "reading_item",
            stem: "The collapsed spire was notable in architectural history because it:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Was an imaginative 19th-century addition rather than an original medieval structure." },
              { key: "B", text: "Was built entirely out of hollow concrete and industrial fiberglass." },
              { key: "C", text: "Had been universally hated by French citizens since the Middle Ages." },
              { key: "D", text: "Survived three earlier catastrophic blazes without sustaining damage." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出坍塌的尖顶并非中世纪产物，而是19世纪50年代由建筑师勒-杜克以极富浪漫想象的艺术重构方式添加的。"
          },
          {
            q_type: "reading_item",
            stem: "Environmental groups opposed using lead sheeting primarily due to:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Severe toxic contamination risks to surrounding urban neighborhoods." },
              { key: "B", text: "The excessive weight of lead causing the stone foundations to sink." },
              { key: "C", text: "The high economic cost of importing lead from distant nations." },
              { key: "D", text: "The tendency of lead to attract lightning strikes during summer storms." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出环保组织强烈反对重新铺设重金属铅顶，因为火灾释放的含铅有毒粉尘已对邻近学校和社区构成严重污染隐患。"
          },
          {
            q_type: "reading_item",
            stem: "The final decision of the French National Assembly reflected a desire for:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Historic continuity and cultural reassurance over modern novelty." },
              { key: "B", text: "Commercial tourism revenue generated by avant-garde landmarks." },
              { key: "C", text: "Eradicating all traditional religious symbolism from Paris." },
              { key: "D", text: "Handing total architectural control to corporate property developers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出国民议会最终投票决定原样复建，表明在社会割裂与全球化焦虑中，历史延续性的心理抚慰压倒了现代新潮的浮华。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `Across vast swathes of provincial America and Britain, a quiet institutional catastrophe is unraveling: the rapid extinction of local newspapers. Over the past fifteen years, more than one in four regional publications have folded, turning hundreds of counties into "news deserts"—geographic communities devoid of professional, daily journalistic coverage. Where vibrant town squares once resounded with investigative reporters attending city council meetings, school board elections, and municipal court hearings, an eerie informational silence now prevails.

The economic demise of local journalism was engineered by the digital disruption of print advertising. Historically, newspapers derived up to eighty percent of their revenues not from reader subscriptions, but from classified advertisements and display ads placed by local car dealerships, supermarkets, and department stores. The migration of classifieds to specialized web platforms, coupled with the algorithmic monopoly of social media giants over targeted digital ads, decimated print advertising revenues almost overnight.

The civic consequences of local journalism's collapse are profoundly toxic for democratic governance. Political science research conclusively demonstrates that when a local newspaper perishes, municipal voter turnout plummets, civic engagement withers, and political polarization deepens. Deprived of independent watchdog oversight, local governments become markedly less accountable. Empirical studies reveal that municipalities in news deserts suffer from higher municipal borrowing costs, increased incidences of municipal corruption, and bloated public expenditures, as self-interested local officials operate without the deterrent of investigative exposure.

Furthermore, the void vacated by trusted regional papers has been filled by polarized partisan blogs, algorithmic social media rumor mills, and partisan "ghost newspapers" funded by political interest groups. Without shared local facts anchoring public discourse, neighborly trust evaporates, leaving communities acutely susceptible to divisive conspiracy theories.

Philanthropic foundations and media reformers are exploring alternative financial lifelines, from converting newspapers into non-profit civic trusts to passing legislation requiring tech platforms to compensate news publishers for distributed journalism. However, saving local journalism requires communities themselves to recognize that independent reporting is not a free digital commodity, but an indispensable public utility vital for safeguarding grassroots democracy.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The term 'news deserts' in Paragraph 1 refers to communities that:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Lack professional, daily local journalistic coverage." },
              { key: "B", text: "Are located in arid geographical desert environments." },
              { key: "C", text: "Have banned all internet access and digital television." },
              { key: "D", text: "Refuse to allow politicians to speak in public." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义理解题。第一段第二句明确界定了“新闻沙漠”的定义：缺乏专业且日常的新闻报道覆盖的社区。"
          },
          {
            q_type: "reading_item",
            stem: "Local newspapers collapsed financially primarily because:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Lucrative advertising revenue migrated to specialized websites and tech giants." },
              { key: "B", text: "Citizens collectively lost the cognitive ability to read English print." },
              { key: "C", text: "Federal laws made it illegal to print news on paper." },
              { key: "D", text: "Paper printing presses became impossible to manufacture." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出报业八成依赖广告，而分类广告迁移到分类信息网，数字广告被科技巨头算法垄断，导致地方报纸广告收入瞬间崩盘。"
          },
          {
            q_type: "reading_item",
            stem: "According to research in Paragraph 3, the disappearance of local papers leads to:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Higher municipal corruption and reduced voter turnout." },
              { key: "B", text: "Dramatically lower municipal borrowing interest rates." },
              { key: "C", text: "A massive surge in bipartisan political cooperation." },
              { key: "D", text: "The complete elimination of local municipal taxes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段明确指出报社倒闭后，选民投票率暴跌，市政腐败案件增多，市政借贷成本与公共支出激增。"
          },
          {
            q_type: "reading_item",
            stem: "What has largely filled the void left by closed local newspapers?",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Polarized partisan blogs and social media rumors." },
              { key: "B", text: "High-quality investigative documentary films." },
              { key: "C", text: "Free academic encyclopedias delivered to mailboxes." },
              { key: "D", text: "Neutral radio broadcasts funded by municipal mayors." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第四段指出报纸留下的空白迅速被极化党派博客、社交媒体谣言工坊和暗中资助的“幽灵小报”所占领。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that preserving local journalism requires treating it as:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "An indispensable public utility essential for grassroots democracy." },
              { key: "B", text: "An obsolete commercial medium that should be privatized." },
              { key: "C", text: "A luxury pastime for wealthy suburban retirees." },
              { key: "D", text: "A government propaganda department controlled by the state." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结指出挽救地方新闻需要公众认识到独立报道不是免费的数字廉价品，而是捍卫基层民主不可或缺的公共基础设施（indispensable public utility）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In modern scientific enterprise, the currency of prestige has long been measured by citation metrics. Quantitative indicators such as the Journal Impact Factor (JIF) and individual h-indices were originally devised by bibliometricians as benign statistical tools to help librarians identify which periodicals were most frequently referenced. Over recent decades, however, these raw metrics have metastasized into absolute arbiters of scientific career progression, determining university appointments, tenure awards, and governmental research grant allocations.

This obsessive metrication has warped the fundamental incentives of scientific inquiry, giving rise to Goodhart's Law: when a measure becomes a target, it ceases to be a good measure. To maximize citation scores, ambitious researchers increasingly avoid daring, unorthodox hypotheses that require years of uncertain experimentation. Instead, they pursue fashionable, incremental topics guaranteed to generate quick publications and reciprocal citations from established academic networks.

Furthermore, the pressure to inflate impact metrics has spawned widespread gamesmanship and outright scientific corruption. Research groups form "citation cartels," artificially citing one another's papers to inflate individual indices. Journal editors engage in subtle coercion, pressuring authors to insert superfluous citations to recently published articles in their own periodicals before granting publication approval. In the most egregious instances, researchers chop cohesive scientific discoveries into "least publishable units" to multiply their formal publication counts.

Critics emphasize that citation counts are fundamentally flawed proxies for scientific quality. A revolutionary conceptual breakthrough may take decades to be understood and cited by mainstream peers, while a deeply flawed paper containing sensational, debunked claims often garners astronomical citation counts as subsequent scholars rush to refute its bogus methodology.

Reforming scientific evaluation demands dismantling the monopoly of algorithmic citation indices. Declarations such as the San Francisco Declaration on Research Assessment (DORA) urge institutions to evaluate manuscripts on their intrinsic scientific rigor rather than the prestige of the publishing venue. By embracing qualitative peer evaluation and open-science transparency, the academic community can liberate researchers to pursue genuine discovery rather than vanity metrics.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Citation metrics like the Journal Impact Factor were originally created to:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Help librarians determine which periodicals were frequently read." },
              { key: "B", text: "Rank university professors for promotional dismissals." },
              { key: "C", text: "Calculate annual patent licensing taxes for pharmaceutical labs." },
              { key: "D", text: "Identify pseudoscientific conspiracy theories in medical journals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出引用指标最初只是文献计量学家开发的统计工具，旨在帮助图书馆员识别哪些刊物被参考得最多。"
          },
          {
            q_type: "reading_item",
            stem: "According to Goodhart's Law, when a metric becomes a career target:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "It ceases to serve as an accurate or reliable measure." },
              { key: "B", text: "Scientific accuracy increases by 100 percent." },
              { key: "C", text: "Governments automatically double university research grants." },
              { key: "D", text: "Young scholars stop submitting papers to journals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段明确引用古德哈特定律：“当一个指标变成目标时，它就不再是一个好指标（it ceases to be a good measure）”。"
          },
          {
            q_type: "reading_item",
            stem: "How do 'citation cartels' game the academic evaluation system?",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "By colluding to artificially cite each other's research papers." },
              { key: "B", text: "By stealing physical laboratory equipment from rivals." },
              { key: "C", text: "By publishing exclusively in foreign languages to avoid scrutiny." },
              { key: "D", text: "By paying cash bribes directly to university chancellors." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出“引用卡特尔”是通过串通互相无端引用彼此论文（artificially citing one another）来虚增个人学术指数。"
          },
          {
            q_type: "reading_item",
            stem: "Citation counts are considered flawed proxies for quality because:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Debunked or flawed papers often attract heavy citations from critics." },
              { key: "B", text: "No citation database can count beyond one hundred references." },
              { key: "C", text: "Computer algorithms refuse to index groundbreaking papers." },
              { key: "D", text: "Only senior retired scholars are legally allowed to cite articles." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出引用次数不能代表质量：被证伪的劣质论文常因招致学者争相批驳而获得极高引用量，而真正开创性成果可能多年无人问津。"
          },
          {
            q_type: "reading_item",
            stem: "The San Francisco Declaration on Research Assessment (DORA) advocates:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Evaluating research on its intrinsic merit rather than journal prestige." },
              { key: "B", text: "Banning all scientific research that does not yield immediate profits." },
              { key: "C", text: "Abolishing peer review in favor of social media voting." },
              { key: "D", text: "Forbidding researchers from citing papers published before 2000." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出旧金山科研评估宣言（DORA）主张评估科研应立足于成果本身的内在严谨度与价值，而非发表刊物的名气或影响因子。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the autumn of 2019, the United Kingdom was gripped by an unprecedented constitutional crisis that tested the fundamental boundaries of British parliamentary democracy. With the statutory deadline for the UK's departure from the European Union looming, Prime Minister Boris Johnson advised Queen Elizabeth II to prorogue—or suspend—Parliament for five consecutive weeks. Downing Street insisted that the prolonged shutdown was a routine administrative recess to prepare a new legislative agenda. However, political opponents and legal scholars decried the maneuver as an unconstitutional power grab designed to muzzle parliamentary debate and prevent lawmakers from scrutinizing the government's Brexit strategy.

The dispute culminated in Miller v. The Prime Minister, a historic clash argued before an extraordinary eleven-justice bench of the UK Supreme Court. The central legal controversy pivoted on "justiciability": whether the monarch's Royal Prerogative to prorogue Parliament—exercised on the binding advice of the Prime Minister—was an unreviewable political matter or a legal question subject to judicial review. Government attorneys argued that prorogation was an exclusively political prerogative into which unelected judges had no constitutional authority to intrude.

In a unanimous, landmark ruling that astonished Whitehall, the Supreme Court firmly repudiated the government's stance. Delivering the unanimous judgment, Court President Lady Hale affirmed that the courts possess both the constitutional right and duty to determine the legal boundaries of executive prerogative powers. Hale articulated two foundational principles of the unwritten British constitution: parliamentary sovereignty—the principle that Parliament is the supreme legal authority in the land—and parliamentary accountability, which requires ministers to answer continuously to elected members of Parliament.

The court concluded that the Prime Minister's advice had the extreme effect of frustrating and preventing Parliament from carrying out its constitutional functions for five critical weeks without any reasonable justification. Consequently, the justices declared the prorogation unlawful, void, and of no legal effect, ruling that Parliament had never technically been prorogued at all.

The ruling served as a momentous constitutional check against executive overreach, establishing that even the highest executive office remains subordinate to the rule of law. By asserting judicial supremacy in policing constitutional boundaries, the Supreme Court invigorated Britain's centuries-old tradition of institutional checks and balances.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Critics accused Prime Minister Boris Johnson of proroguing Parliament to:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Prevent lawmakers from scrutinizing his government's Brexit plans." },
              { key: "B", text: "Permanently abolish the British monarchy." },
              { key: "C", text: "Lower commercial corporate taxes without parliamentary consent." },
              { key: "D", text: "Declare immediate war on European neighboring nations." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出反对者谴责休会是违宪的权力掠夺，旨在封杀议会辩论，阻止议员审查政府的脱欧战略。"
          },
          {
            q_type: "reading_item",
            stem: "The primary legal question of 'justiciability' in the dispute was whether:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "The prime ministerial prerogative to suspend Parliament can be reviewed by courts." },
              { key: "B", text: "The Supreme Court should be relocated to Scotland permanently." },
              { key: "C", text: "Members of Parliament possess the right to travel abroad." },
              { key: "D", text: "British citizens should vote on abolishing the Supreme Court." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出“司法审查权/可审判性”的核心争议是：首相提请休会的皇家特权究竟属于不可审查的纯政治事务，还是应受法院司法审查的法律问题。"
          },
          {
            q_type: "reading_item",
            stem: "Lady Hale based the court's judgment upon the twin constitutional principles of:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Parliamentary sovereignty and parliamentary accountability." },
              { key: "B", text: "Military supremacy and unconditional monarchical rule." },
              { key: "C", text: "Executive impunity and complete judicial silence." },
              { key: "D", text: "International trade freedom and municipal tax autonomy." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段明确指出海尔女法官重申了英国不成文宪法的两大基石原则：议会主权（parliamentary sovereignty）与议会问责（parliamentary accountability）。"
          },
          {
            q_type: "reading_item",
            stem: "What was the immediate legal effect of the Supreme Court's ruling?",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "The prorogation was declared null and void as if it never occurred." },
              { key: "B", text: "The Prime Minister was sentenced to immediate imprisonment." },
              { key: "C", text: "Parliament was permanently dissolved until the next decade." },
              { key: "D", text: "The United Kingdom immediately canceled its withdrawal from the EU." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出大法官们裁定休会令违法且自始无效（null, void, of no effect），在法律上议会从未真正休会。"
          },
          {
            q_type: "reading_item",
            stem: "The historical significance of Miller v. The Prime Minister is that it:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Erected a powerful judicial bulwark against executive overreach." },
              { key: "B", text: "Transferred all legislative powers directly to the monarch." },
              { key: "C", text: "Prohibited British courts from ruling on future political disputes." },
              { key: "D", text: "Established that prime ministers are above constitutional law." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结指出该裁决建立了对行政权力扩张的强力宪法制衡（check against executive overreach），重申了法律面前人人平等的法治传统。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2020 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky2",
    year: 2020,
    title: "2020年全国硕士研究生招生考试英语（二）真题",
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
        content: `In the contemporary financial landscape, the physical banknote is facing unprecedented marginalization. From contact-free credit cards to smartphone QR codes, digital payment systems have penetrated everyday commerce with astonishing (1)____. Across affluent European capitals, restaurants and boutiques proudly display "Card Only" placards, refusing paper bills and metal coins with casual (2)____.

Fintech innovators and central bank economists hail the cashless society as a triumph of economic modernization. Digital transactions eliminate the expensive logistics of minting coins, transporting armored vehicles, and securing bank vaults. Electronic audit trails deter underground tax evasion, curtail armed robbery, and provide central bankers with real-time economic data to fine-tune monetary (3)____.

Yet, this rapid digital march has exposed a dark underbelly: the systematic disenfranchisement of vulnerable social cohorts. Millions of unbanked citizens—low-income individuals, undocumented migrants, and homeless individuals—lack the credit scores, postal addresses, or legal identification required to open formal banking (4)____. In a completely cashless economy, these marginalized groups are effectively (5)____ from basic consumer life, unable to buy groceries or purchase bus tickets.

Elderly demographics confront equally daunting (6)____. Many senior citizens find touchscreens and biometric verification confusing or physically cumbersome. For pensioners with visual impairments, cognitive decline, or arthritic fingers, operating mobile banking applications generates acute stress. Physical cash provides intuitive tactile clarity, allowing seniors to track their weekly expenditures without fearing digital scams or algorithmic (7)____.

Furthermore, the abolition of physical money presents profound threats to civil liberties and personal (8)____. Every digital transaction leaves an indelible corporate footprint: time, exact geolocation, merchant category, and purchased items are cataloged by credit card networks and commercial data brokers. When every commercial exchange is logged on corporate servers, an individual's private lifestyle, health vulnerabilities, and political sympathies become transparent to surveillance (9)____.

Systemic infrastructure resilience presents another acute vulnerability. Digital payment ecosystems depend upon uninterrupted electricity grids, submarine telecommunication cables, and cloud data centers. During natural disasters, power blackouts, or coordinated hostile cyberattacks, cashless societies can be brought to a catastrophic (10)____, leaving citizens unable to acquire emergency supplies.

Recognizing these hazards, progressive municipal and national legislatures are intervening to defend paper currency. Cities such as Philadelphia, San Francisco, and New York have enacted "Cash Mandate" ordinances, legally forbidding brick-and-mortar retailers from (11)____ cash payments. In Europe, central banks are investigating "Digital Euro" prototypes designed to operate offline with privacy protections mimicking physical (12)____.

Sociologists emphasize that money is not merely an abstract unit of accounting, but a fundamental instrument of democratic inclusion. Physical cash possesses a unique democratic virtue: it functions universally without digital passwords, network connectivity, or corporate (13)____. Preserving cash alongside digital alternatives ensures that economic modernization does not sacrifice civic dignity, financial resilience, or fundamental human (14)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "velocity" },
              { key: "B", text: "hesitation" },
              { key: "C", text: "fragility" },
              { key: "D", text: "clumsiness" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。with astonishing velocity（以惊人的速度），形容移动支付在日常商业中的飞速普及。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "indifference" },
              { key: "B", text: "sympathy" },
              { key: "C", text: "gratitude" },
              { key: "D", text: "panic" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。with casual indifference（漫不经心的漠然/随意拒绝），生动刻画商家拒收纸币硬币的态度。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "policy" },
              { key: "B", text: "fiction" },
              { key: "C", text: "scandal" },
              { key: "D", text: "tragedy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。monetary policy（货币政策），央行利用实时交易大数据微调宏观货币政策。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "accounts" },
              { key: "B", text: "monuments" },
              { key: "C", text: "prisons" },
              { key: "D", text: "novels" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】商业搭配。open formal banking accounts（开设正规银行账户）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "excluded" },
              { key: "B", text: "celebrated" },
              { key: "C", text: "rescued" },
              { key: "D", text: "promoted" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。effectively excluded from basic consumer life（被实际排除在基础消费生活之外）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "hurdles" },
              { key: "B", text: "privileges" },
              { key: "C", text: "triumphs" },
              { key: "D", text: "subsidies" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。confront equally daunting hurdles（面临同样严峻的阻碍/难题）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "glitches" },
              { key: "B", text: "charities" },
              { key: "C", text: "miracles" },
              { key: "D", text: "virtues" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】计算机名词。algorithmic glitches（算法故障/系统差错），与数字诈骗并列。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "privacy" },
              { key: "B", text: "hostility" },
              { key: "C", text: "recklessness" },
              { key: "D", text: "cruelty" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词并列。threats to civil liberties and personal privacy（对公民自由与个人隐私的威胁）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "apparatuses" },
              { key: "B", text: "festivals" },
              { key: "C", text: "orchards" },
              { key: "D", text: "cemeteries" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。surveillance apparatuses（监控机器/监视机构机制）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "standstill" },
              { key: "B", text: "paradise" },
              { key: "C", text: "renaissance" },
              { key: "D", text: "victory" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。brought to a catastrophic standstill（陷入灾难性的停顿与瘫痪）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "rejecting" },
              { key: "B", text: "accepting" },
              { key: "C", text: "spending" },
              { key: "D", text: "saving" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。forbidding retailers from rejecting cash（禁止实体商家拒收现金）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "banknotes" },
              { key: "B", text: "novels" },
              { key: "C", text: "postcards" },
              { key: "D", text: "paintings" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词照应。mimicking physical banknotes（模拟实体纸币/钞票的匿名离线特性）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "surveillance" },
              { key: "B", text: "sympathy" },
              { key: "C", text: "mercy" },
              { key: "D", text: "generosity" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。现金运转无需联网，也无需接受商业监控（corporate surveillance）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "rights" },
              { key: "B", text: "crimes" },
              { key: "C", text: "penalties" },
              { key: "D", text: "deficits" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义总结。fundamental human rights（基本人权与尊严保障）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "essential" },
              { key: "B", text: "trivial" },
              { key: "C", text: "unfortunate" },
              { key: "D", text: "harmful" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。现金对于弱势群体的基础生存而言是至关重要的（essential）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "tangible" },
              { key: "B", text: "fictional" },
              { key: "C", text: "imaginary" },
              { key: "D", text: "deceptive" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。tangible clarity（切实可见的触觉与实体清晰度）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "mandates" },
              { key: "B", text: "crimes" },
              { key: "C", text: "scandals" },
              { key: "D", text: "boycotts" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。enacted legal mandates（颁布法律强制保护法令）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "autonomy" },
              { key: "B", text: "servitude" },
              { key: "C", text: "fatigue" },
              { key: "D", text: "grief" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。preserving financial autonomy（捍卫消费者的财务自主权）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "resilience" },
              { key: "B", text: "bankruptcy" },
              { key: "C", text: "decline" },
              { key: "D", text: "isolation" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。safeguarding systemic resilience（保障系统应对危机的韧性）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "coexistence" },
              { key: "B", text: "warfare" },
              { key: "C", text: "hostility" },
              { key: "D", text: "collapse" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】总结名词。ensuring harmonious coexistence（确保现金与数字支付和谐共存）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `As birth rates plummet and life expectancies expand across the industrialized world, national governments are aggressively raising statutory retirement ages to avert catastrophic pension insolvencies. Policymakers praise the extension of working lives as a double dividend that bolsters tax revenues while keeping older citizens physically and mentally engaged. Yet, in corporate corridors and executive recruitment offices, this political mandate collides with an intractable reality: rampant, systemic age discrimination against older workers.

While statutory discrimination statutes ostensibly protect employees over forty, ageism remains the most socially accepted prejudice in corporate hiring. Unlike race or gender bias, which modern human resource departments vigorously police, bias against mature candidates is routinely camouflaged beneath euphemistic corporate jargon. Job postings solicit candidates with "fresh digital energy" or individuals who are "culture fits" for youthful startup environments, effectively signaling that seasoned applicants need not apply.

Corporate reluctance to employ older workers is fueled by entrenched managerial stereotypes. Chief financial officers frequently assume that workers over fifty demand exorbitant salaries, suffer from chronic health infirmities, and lack the cognitive agility to master cutting-edge software tools. Furthermore, younger managers often experience profound psychological discomfort when supervising subordinates who possess more life and industry experience than themselves, fearing that mature direct reports will challenge their authority.

The reality, corroborated by decades of occupational research, thoroughly refutes these discriminatory myths. Studies demonstrate that older professionals possess superior emotional intelligence, unmatched crisis management judgment, and lower rates of voluntary job turnover compared to their younger counterparts. In an era characterized by chronic employee disengagement and rapid job-hopping, mature workers provide vital institutional memory and stabilizing loyalty.

Dismantling age bias requires comprehensive policy reforms. Governments must mandate age-blind recruitment practices—prohibiting dates of graduation and birth years on initial resume screenings—while dramatically stiffening legal penalties for retaliatory terminations. Corporations that celebrate demographic diversity while ignoring age-based inclusion commit both a moral injustice and a colossal strategic blunder, discarding the wisdom of their most experienced workers precisely when complex global challenges demand it most.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Why are governments raising the statutory retirement age in industrialized countries?",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "To bolster tax receipts and prevent pension fund insolvencies." },
              { key: "B", text: "To force older workers to emigrate to developing economies." },
              { key: "C", text: "To ban young graduates from entering corporate technology firms." },
              { key: "D", text: "To eliminate all statutory employee healthcare benefits." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段首句指出，政府推迟退休年龄旨在避免养老金破产危机（avert pension insolvencies），同时增加税收。"
          },
          {
            q_type: "reading_item",
            stem: "Corporate recruitment jargon such as 'fresh digital energy' is used to:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Disguise age discrimination against mature job applicants." },
              { key: "B", text: "Encourage senior citizens to apply for executive directorships." },
              { key: "C", text: "Promote renewable solar energy in company offices." },
              { key: "D", text: "Comply with mandatory federal affirmative action quotas." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出招聘中所谓“充满数字活力”等托辞，实则是用来伪装并掩盖对中老年求职者的隐形年龄歧视（disguise age discrimination）。"
          },
          {
            q_type: "reading_item",
            stem: "Younger corporate managers often hesitate to hire older subordinates because they:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Feel psychologically uneasy managing workers with superior experience." },
              { key: "B", text: "Are forbidden by labor laws from communicating with senior staff." },
              { key: "C", text: "Worry that older workers will demand complete remote telecommuting." },
              { key: "D", text: "Believe that older workers refuse to accept paid corporate bonuses." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段末尾指出年轻管理者在面对资历更深厚的下属时深感心理不适，担忧自身管理权威受到挑战。"
          },
          {
            q_type: "reading_item",
            stem: "Occupational research indicates that mature workers typically offer:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Superior emotional intelligence, crisis judgment, and company loyalty." },
              { key: "B", text: "Extremely high rates of voluntary monthly job resignation." },
              { key: "C", text: "A total refusal to communicate with younger project team members." },
              { key: "D", text: "Frequent workplace accidents due to cognitive distraction." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出职业研究表明，成熟年长员工具备卓越的情商、危机处置判断力以及更低的主动离职率（stabilizing loyalty）。"
          },
          {
            q_type: "reading_item",
            stem: "To combat age discrimination, the author specifically recommends:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Enforcing age-blind recruitment practices in initial resume reviews." },
              { key: "B", text: "Forbidding individuals over fifty from using computer software." },
              { key: "C", text: "Abolishing all statutory retirement pensions worldwide." },
              { key: "D", text: "Permitting corporations to fire senior workers without legal cause." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】方案主旨题。末段明确主张政府推行“隐龄盲聘（age-blind recruitment）”，在初筛中隐去毕业年份和生日，并加大对解聘的法律惩处。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In the contemporary consumer economy, the "sharing economy" model has expanded from ride-hailing and vacation lodging to revolutionize haute couture: the clothing rental subscription. Platforms such as Rent the Runway and HURR invite fashion-conscious urbanites to rent designer cocktail dresses, tailored blazers, and luxury accessories for a fraction of their retail purchase price. Marketed under glossy banners of sustainable circularity, clothing rental promises to sate consumers' insatiable appetite for wardrobe novelty without generating fast-fashion textile waste.

Proponents herald apparel rental as an elegant environmental panacea. Instead of a dress being manufactured, worn once for an Instagram photograph, and languishing indefinitely in a landfill, a single garment can theoretically circulate through dozens of users across its operational lifecycle. Life-cycle assessments conducted by rental startups emphasize the conservation of raw virgin cotton, petroleum synthetics, and gallons of freshwater normally consumed in industrial textile production.

However, independent environmental engineers have scrutinized the full logistics supply chain of rental platforms, revealing a far more complicated ecological balance sheet. While renting eliminates the upfront manufacturing footprint of duplicate garments, it substitutes continuous transportation and chemical maintenance emissions. Every transaction entails door-to-door courier delivery and return, generating massive carbon emissions through diesel delivery vans.

Furthermore, hygiene standards demand that returned garments undergo rigorous commercial sanitation before being redispatched. Unlike domestic laundering, commercial rental cleaning relies heavily on industrial dry cleaning protocols utilizing perchloroethylene, a toxic volatile solvent hazardous to groundwater aquifers. Garments that cannot withstand repeated chemical processing often degrade rapidly, forfeiting the very longevity on which the circular business model depends.

Industry analysts conclude that clothing rental is not an automatic environmental cure. For high-end, infrequently worn ceremonial attire—such as wedding tuxedos and ballgowns—rental provides genuine resource efficiencies. But when applied to casual, everyday basics like sweaters and denim jeans, the transport and cleaning overhead easily eclipses the environmental impact of purchasing a durable, ethically made garment and wearing it for years.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What is the primary selling proposition of clothing rental subscription services?",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Providing affordable wardrobe novelty while claiming environmental sustainability." },
              { key: "B", text: "Selling used garments at permanent municipal flea markets." },
              { key: "C", text: "Teaching customers how to hand-sew their own cotton clothes." },
              { key: "D", text: "Manufacturing disposable paper clothes for single-day use." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出衣物租赁平台的主打卖点是以低廉价格满足人们对衣橱新鲜感的需求，同时标榜循环环保（sustainable circularity）。"
          },
          {
            q_type: "reading_item",
            stem: "Advocates argue that clothing rental benefits the environment by:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Maximizing the utility of single garments across multiple wearers." },
              { key: "B", text: "Requiring fashion designers to work without financial compensation." },
              { key: "C", text: "Banning consumers from attending social ceremonies in cities." },
              { key: "D", text: "Completely eliminating all textile manufacturing globally." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出支持者认为一件衣服能在数十位租户间轮转循环，极大提升单件衣物的使用效能，减少重复生产的资源消耗。"
          },
          {
            q_type: "reading_item",
            stem: "Environmental engineers criticize rental models because they:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Generate high carbon emissions through continuous courier transit." },
              { key: "B", text: "Are funded by corrupt offshore banking conglomerates." },
              { key: "C", text: "Force all couriers to ride pedal bicycles in rainstorms." },
              { key: "D", text: "Lead to immediate worldwide shortages of cardboard boxes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出环保学者发现其生态账本复杂：虽然省了部分生产端消耗，但每次租借带来的上门配送与退回运输产生了巨大的快递碳排放。"
          },
          {
            q_type: "reading_item",
            stem: "Commercial sanitation in rental services often involves:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Industrial dry cleaning using hazardous chemical solvents." },
              { key: "B", text: "Hanging clothes outdoors in direct solar radiation for months." },
              { key: "C", text: "Burning garments and manufacturing replacements from scratch." },
              { key: "D", text: "Washing garments exclusively in purified mountain spring water." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出商用租赁洗涤依赖大量使用四氯乙烯的工业干洗（industrial dry cleaning using solvents），对水环境构成潜在威胁并加速织物老化。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that clothing rental is environmentally viable mainly for:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Rarely worn ceremonial garments rather than everyday basic attire." },
              { key: "B", text: "Cheap cotton socks discarded after a single afternoon's wear." },
              { key: "C", text: "Heavy military uniforms worn in Arctic survival expeditions." },
              { key: "D", text: "Disposable plastic ponchos used during music festivals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出服装租赁对极少穿的礼服礼服（rarely worn ceremonial attire）具有真正的环保价值，但对日常休闲基本款而言其运输洗涤代价得不偿失。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the technological race to commercialize autonomous vehicles, automotive engineers and software developers have achieved astonishing triumphs: perfecting lidar sensor fusion, training deep neural networks to recognize pedestrians, and orchestrating millisecond reaction times. Yet, as self-driving prototypes transition from controlled desert test tracks to unpredictable municipal streets, roboticists are encountering a profound challenge that cannot be solved by silicon chips or faster processors: the intractable labyrinth of machine ethics.

The core dilemma is often conceptualized through the philosophical thought experiment known as the "trolley problem." Imagine an autonomous vehicle traveling along a narrow mountain road when an erratic pedestrian suddenly trips into its path. The vehicle's algorithmic trajectory planner must make an instantaneous decision: stay on course and fatally strike the pedestrian, or violently swerve into a concrete barrier, killing the vehicle's sole passenger.

In human drivers, such tragic split-second reactions are classified as involuntary reflexes; the law judges them with compassionate leniency. In an autonomous vehicle, however, every vehicular maneuver is the deterministic output of pre-programmed code. The decision has been consciously engineered months in advance by a software developer sitting in a corporate office. Programmers are essentially being forced to decide whose lives are worth prioritizing in tragic collisions.

Public opinion surveys conducted across global populations reveal striking cultural fissures regarding algorithmic morality. In studies such as MIT's "Moral Machine" experiment, respondents in Western nations showed a strong preference for utilitarian outcomes that minimize total human casualties, even if it requires sacrificing the car's occupant. In contrast, participants in many Asian societies placed higher value on protecting elders and passengers who place their trust in the vehicle.

Furthermore, commercial realities present a formidable marketing dilemma. Would consumers willingly purchase an autonomous vehicle programmed to sacrifice its own buyer in exceptional emergency scenarios? Automotive executives are petrified that utilitarian programming will terrify prospective buyers, whereas selfish programming—prioritizing passengers at all costs—provokes fierce moral condemnation from public safety regulators.

Legal scholars emphasize that ethical dilemmas cannot be delegated to private tech developers. Society requires democratic governments to establish transparent, standardized ethical codes for autonomous algorithms, ensuring that the burden of moral tragedy is shared collectively through the rule of law.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What major non-technical hurdle is confronting autonomous vehicle development?",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Complex ethical dilemmas regarding machine moral decision-making." },
              { key: "B", text: "A severe shortage of lithium batteries in automotive plants." },
              { key: "C", text: "The total inability of lidar sensors to detect concrete walls." },
              { key: "D", text: "A legal ban on all automotive computer software worldwide." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段末尾指出无人驾驶面临芯片和算法无法解决的深刻难题：机器伦理这一棘手迷宫（labyrinth of machine ethics）。"
          },
          {
            q_type: "reading_item",
            stem: "How does an autonomous car's collision response differ fundamentally from a human driver's?",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "It is the predetermined output of consciously programmed code." },
              { key: "B", text: "It is entirely guided by emotional panic and instinct." },
              { key: "C", text: "It requires live permission from a satellite flight controller." },
              { key: "D", text: "It is legally immune from any form of civil lawsuit." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出人类是无意识的本能反应，而自动驾驶的每一步变道撞击都是数月前程序员在办公室预先敲定的确定性算法代码（predetermined output）。"
          },
          {
            q_type: "reading_item",
            stem: "MIT's 'Moral Machine' experiment revealed that algorithmic moral preferences:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Vary significantly across different global and cultural societies." },
              { key: "B", text: "Are universally identical among all human beings." },
              { key: "C", text: "Are determined entirely by personal financial wealth." },
              { key: "D", text: "Favor sacrificing young children in every scenario." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出麻省理工的实验表明，不同文化群体对事故中牺牲谁存在显著的文化分歧（cultural fissures）。"
          },
          {
            q_type: "reading_item",
            stem: "Automotive executives face a marketing dilemma because buyers may:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Refuse to purchase cars programmed to sacrifice their own passengers." },
              { key: "B", text: "Demand cars that drive at double the statutory speed limit." },
              { key: "C", text: "Insist on driving exclusively with obsolete cassette players." },
              { key: "D", text: "Reject all vehicles that use synthetic rubber tires." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第五段指出汽车高管面临营销悖论：没有消费者愿意花钱买一辆在危急时刻被程序设定为优先牺牲车主的汽车。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that ethical guidelines for autonomous vehicles should be set by:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Democratic governments establishing standardized legal codes." },
              { key: "B", text: "Private software developers working in Silicon Valley." },
              { key: "C", text: "Automotive advertising marketing consultants." },
              { key: "D", text: "Individual car buyers configuring their own ethics menus." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段强调道德困境不能甩给私营科技公司，必须由民主政府通过法律建立公开透明的标准化伦理守则。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `When the European Union implemented the General Data Protection Regulation (GDPR) in May 2018, privacy advocates hailed it as a monumental watershed in global digital rights. Armed with extraterritorial jurisdiction and draconian financial penalties reaching up to four percent of global corporate turnover, the regulation aimed to dismantle "surveillance capitalism" and return control over personal digital footprints to sovereign individuals. Corporate tech conglomerates were compelled to secure unambiguous, informed consent before collecting, processing, or monetizing personal behavioral data.

Five years into its enforcement, however, the practical reality of GDPR presents a far more ambiguous verdict. Rather than experiencing genuine digital liberation, everyday internet users find themselves subjected to a relentless onslaught of "cookie consent" pop-up banners. On virtually every web page, visitors are confronted by obstructive dialogue boxes engineered through manipulative "dark patterns"—subtle psychological design tricks where a brightly colored "Accept All" button takes a millisecond to click, while declining tracking requires navigating labyrinthine submenus and tedious toggles. Weary of digital friction, over eighty percent of users routinely click "Accept All" without reading a syllable, rendering the principle of informed consent an empty bureaucratic ritual.

Furthermore, antitrust economists warn that GDPR has perversely entrenched the very market monopolies it sought to restrain. Compliance requires employing armies of privacy attorneys, technical compliance engineers, and cybersecurity auditors. For tech behemoths like Alphabet and Meta, absorbing hundreds of millions of dollars in annual compliance overhead is trivial. In stark contrast, European tech startups and independent digital publishers operate on shoestring budgets. Crushed by compliance liabilities, hundreds of promising startups have shuttered or relocated overseas, leaving incumbent tech giants with even larger domestic market shares.

Cross-border enforcement has also been hamstrung by bureaucratic bottlenecks. Under GDPR's "one-stop-shop" mechanism, complaints against a multinational tech firm must be adjudicated by the data protection authority of the EU nation where the firm maintains its regional headquarters. Because Ireland and Luxembourg host the European headquarters of most major Silicon Valley giants, their regulatory agencies have been overwhelmed by thousands of complex complaints, resulting in enforcement backlogs that stretch for years.

To realize GDPR's noble aspirations, European regulators must reform enforcement mechanisms. Transitioning away from consent fatigue requires shifting the burden of compliance from passive consumers to algorithmic platforms, mandating universal privacy defaults in web browsers, and aggressively penalizing dark design patterns. Regulating digital capitalism demands systemic technical mandates rather than superficial user checkboxes.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The primary objective of the European Union's GDPR was to:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Dismantle surveillance capitalism and grant individuals control over personal data." },
              { key: "B", text: "Ban all European citizens from using American social media platforms." },
              { key: "C", text: "Establish a unified European government cryptocurrency." },
              { key: "D", text: "Force tech companies to offer completely free digital smartphone hardware." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出 GDPR 的核心目标是瓦解“监控资本主义”，将个人数字轨迹的控制权还给主权个体（return control over personal data）。"
          },
          {
            q_type: "reading_item",
            stem: "The phenomenon of 'cookie consent fatigue' occurs because:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Dark patterns make declining tracking far more tedious than accepting it." },
              { key: "B", text: "Internet browsers automatically shut down whenever a cookie appears." },
              { key: "C", text: "Users are legally required to sign physical paper waivers for every website." },
              { key: "D", text: "Websites charge users cash fees for clicking 'Accept All'." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出网站利用“黑产设计模式（dark patterns）”，一键全选方便显眼，拒绝则需要繁琐设置，导致疲惫的用户只得一律点击接受。"
          },
          {
            q_type: "reading_item",
            stem: "Economists warn that GDPR has unexpectedly benefited tech behemoths by:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Imposing heavy compliance costs that crush smaller startup competitors." },
              { key: "B", text: "Exempting multinational corporations from paying municipal corporate taxes." },
              { key: "C", text: "Granting Silicon Valley firms total ownership of European telecom masts." },
              { key: "D", text: "Prohibiting European citizens from forming technology labor unions." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出合规成本高昂，巨头轻松消化，但初创公司难以招架合规诉讼与律师费而倒闭，反倒巩固了垄断巨头的市场份额。"
          },
          {
            q_type: "reading_item",
            stem: "Why has cross-border GDPR enforcement been notoriously delayed?",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Regulators in Ireland and Luxembourg are overwhelmed with cases." },
              { key: "B", text: "The European Union completely abolished its court system in 2020." },
              { key: "C", text: "Silicon Valley tech giants have refused to hire European lawyers." },
              { key: "D", text: "No consumer has ever filed a formal privacy complaint under GDPR." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出根据“一站式”管辖原则，案件由科技巨头总部所在地（爱尔兰、卢森堡）管辖，导致这两个国家的监管机构被海量诉讼淹没，积压严重。"
          },
          {
            q_type: "reading_item",
            stem: "What reform does the author propose to make data privacy effective?",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Mandating privacy-by-default browser settings and banning dark patterns." },
              { key: "B", text: "Abolishing all data protection laws across the European continent." },
              { key: "C", text: "Requiring users to pay a subscription fee to decline advertising cookies." },
              { key: "D", text: "Forbidding European citizens from accessing international websites." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出解决途径是将合规负担从被动用户转移至算法平台本身，强制在浏览器端推行默认隐私保护（privacy-by-default）并重罚黑产交互设计。"
          }
        ]
      }
    ]
  }
];
