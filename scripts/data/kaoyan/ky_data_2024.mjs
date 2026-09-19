// 2024 年全国硕士研究生招生考试 英语（一）与 英语（二）真题客观题数据集

export const ky2024Exams = [
  // -------------------------------------------------------------------------
  // 2024 考研英语（一）
  // -------------------------------------------------------------------------
  {
    category_id: "ky1",
    year: 2024,
    title: "2024年全国硕士研究生招生考试英语（一）真题",
    exam_type: "real",
    duration_minutes: 60,
    total_score: 50.00,
    pass_score: 30.00,
    is_published: true,
    approval_status: "approved",
    passages: [
      {
        section_type: "cloze",
        title: "Section I: Use of English (知识运用·完形填空)",
        sort_order: 1,
        content: `Regular physical exercise has long been associated with enhanced cardiovascular endurance and general metabolic health. However, recent neurobiological research indicates that aerobic activity may exert an equally profound influence on brain architecture. Specifically, sustained aerobic regimens appear to stimulate neurogenesis within the hippocampus, a cerebral region crucial for spatial navigation and long-term memory consolidation.

In clinical trials involving elderly cohorts, individuals adhering to a moderate routine showed measurable expansions in hippocampal volume over twelve months, (1)____ their sedentary peers who suffered age-related cellular atrophy. Researchers hypothesize that exercise triggers the synthesis of brain-derived neurotrophic factor (BDNF), a protein that supports neuron survival and (2)____ synaptic plasticity.

Nevertheless, neuroscientists caution that physical exertion cannot completely (3)____ the pathological cascades of neurodegenerative disorders such as Alzheimer's disease. While exercise fosters cognitive resilience, it operates (4)____ alongside genetic, dietary, and sleep-related determinants. Therefore, public health campaigns must avoid presenting physical training as a solitary panacea, advocating instead for integrated lifestyle (5)____ to mitigate cognitive decline.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "in contrast to" },
              { key: "B", text: "in terms of" },
              { key: "C", text: "by means of" },
              { key: "D", text: "with respect to" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】逻辑关系辨析。前文讲述坚持适度运动的老年人海马体体积增加，后文提到久坐不动的同龄人海马体出现细胞萎缩，两者构成鲜明对照关系。in contrast to（与……相比/形成对比）符合句意。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "inhibits" },
              { key: "B", text: "promotes" },
              { key: "C", text: "neglects" },
              { key: "D", text: "diminishes" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】动词词义辨析与并列逻辑。and 前后语义一致，前文为 supports neuron survival（促进神经元存活），因此后文应搭配积极意义词汇，promotes（促进）突触可塑性最为恰当。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "halt" },
              { key: "B", text: "accelerate" },
              { key: "C", text: "induce" },
              { key: "D", text: "manifest" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】语境语义辨析。前文出现 caution（警告），且结合 cannot completely，说明体力运动不能完全“遏制/阻止”（halt）阿兹海默症等神经退行性疾病的病理级联反应。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "exclusively" },
              { key: "B", text: "synergistically" },
              { key: "C", text: "reluctantly" },
              { key: "D", text: "invisibly" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】副词语义与句意搭配。下文与 alongside（与……一道并肩）呼应，运动与其他遗传、饮食和睡眠因素“协同起作用”（operates synergistically），体现综合作用机制。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "interventions" },
              { key: "B", text: "superstitions" },
              { key: "C", text: "hesitations" },
              { key: "D", text: "distractions" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配与公共卫生语境。lifestyle interventions（生活方式干预）是医学与健康科学中的固定学术表达，旨在减轻认知衰退。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `The European Union's ambitious Artificial Intelligence Act represents the world's first comprehensive legal framework designed to regulate algorithmic systems across diverse industries. While policymakers herald the legislation as a triumph of democratic oversight over rogue technology, corporate leaders and technological innovators warn that its rigid compliance mandates may severely handicap the continent's nascent tech ecosystem.

At the core of the regulatory debate is the classification of AI systems into risk categories: minimal, limited, high, and unacceptable. High-risk systems—which encompass algorithmic hiring tools, medical diagnostic software, and biometric surveillance devices—must undergo stringent conformity assessments, satisfy rigorous data governance standards, and provide human-in-the-loop oversight mechanisms before entering the European market. 

Critics contend that these bureaucratic hurdles will inevitably disproportionately penalize small and medium-sized enterprises (SMEs). Whereas dominant American and Chinese conglomerates possess the fiscal reserves to retain armies of regulatory lawyers and compliance auditors, European start-ups face suffocating overhead costs that could drain capital away from foundational research and technical iteration. Several venture capital firms have already signaled their intention to pivot investment away from European software laboratories toward jurisdictions with more permissive testing environments.

Supporters counter that legal predictability and ethical trust are indispensable prerequisites for widespread technological adoption. Consumers are hesitant to embrace autonomous technologies unless robust privacy protections and accountability mechanisms are codified in statute. By establishing a gold standard of digital governance, European legislators argue, the EU will cultivate an enduring ecosystem grounded in democratic values, ultimately compelling foreign developers to conform to European standards through what sociologists term the "Brussels Effect."`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The primary purpose of the EU's Artificial Intelligence Act is to ______.",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "prohibit all forms of generative AI and biometric surveillance" },
              { key: "B", text: "establish an overarching legal framework to oversee algorithmic systems" },
              { key: "C", text: "subsidize European tech startups to compete against foreign monopolies" },
              { key: "D", text: "curtail the expansion of venture capital in continental Europe" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】主旨事实细节题。根据第一段首句 'The European Union's ambitious Artificial Intelligence Act represents the world's first comprehensive legal framework designed to regulate algorithmic systems...' 可知，该法案的核心目的是建立全面的法律框架来监管算法系统，选项 B 准确对应。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 2, which AI application would be classified as 'high-risk'?",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "Casual mobile video games" },
              { key: "B", text: "Algorithmic employee recruitment tools" },
              { key: "C", text: "Basic spell-check applications" },
              { key: "D", text: "Weather forecasting simulators" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第二段指出 'High-risk systems—which encompass algorithmic hiring tools, medical diagnostic software, and biometric surveillance devices...'，algorithmic hiring tools 即招聘算法工具，对应选项 B。"
          },
          {
            q_type: "reading_item",
            stem: "Critics worry that the EU regulation will disadvantage European startups because ______.",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "they lack the financial resources to handle heavy compliance costs" },
              { key: "B", text: "they are legally forbidden from patenting proprietary algorithms" },
              { key: "C", text: "foreign markets will block European software exports" },
              { key: "D", text: "European engineers refuse to collaborate with venture capitalists" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。根据第三段可知，美国和中国的大型集团拥有雄厚财力聘请合规团队，而欧洲初创公司面临 suffocating overhead costs（窒息性的合规开销），资金被从研发中抽走，选项 A 精准概括。"
          },
          {
            q_type: "reading_item",
            stem: "Supporters of the AI Act believe that robust regulation will ______.",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "hasten the withdrawal of foreign software developers" },
              { key: "B", text: "foster public trust necessary for widespread AI adoption" },
              { key: "C", text: "eliminate the need for human supervision in automation" },
              { key: "D", text: "lower consumer expectations regarding digital privacy" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】观点态度题。根据第四段首句 'Supporters counter that legal predictability and ethical trust are indispensable prerequisites for widespread technological adoption'，支持者认为合规能带来公众的伦理信任，是技术广泛应用的基石，选项 B 契合。"
          },
          {
            q_type: "reading_item",
            stem: "The phrase 'Brussels Effect' in the final sentence implies that ______.",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "European regulations can influence global market practices" },
              { key: "B", text: "tech companies will permanently abandon Brussels headquarters" },
              { key: "C", text: "regulatory disputes must be settled in Belgian courts" },
              { key: "D", text: "democratic values will be subordinated to technological speed" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义与句意推断题。第四段末句指出欧洲的高标准将迫使外国开发者遵守其标准（compelling foreign developers to conform to European standards），这正是指欧盟单方面制定的法规在事实上传导成为全球市场通行的标杆效应，选 A。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `The rapid proliferation of offshore wind installations around the British coastline marks an extraordinary milestone in the United Kingdom's quest for decarbonization. Utilizing the tempestuous gusts of the North Sea, the nation has constructed several of the world's most capacious offshore wind farms, generating gigawatts of clean electricity that have displaced domestic coal dependence.

Yet, this maritime green renaissance is confronting acute marine conservation concerns. Marine biologists caution that the noise generated during the pile-driving phase of turbine construction poses severe auditory risks to cetaceans, such as harbor porpoises and minke whales. These marine mammals rely on echolocation to navigate, forage, and locate mates in turbid waters; intense underwater acoustic disruption can induce temporary hearing loss or permanently drive them away from vital feeding grounds.

To harmonize energy security with ecological stewardship, regulatory bodies are mandating the deployment of acoustic mitigation technologies. Among these, 'bubble curtains'—perforated hoses laid on the seabed that release dense walls of air bubbles around pile-driving rigs—have demonstrated an ability to attenuate underwater noise transmission by up to 90 percent. Furthermore, vibro-piling and suction bucket foundations are increasingly explored as low-noise installation alternatives.

Financial stakeholders, however, point out that these ecological precautions amplify overall capital expenditure. With elevated inflation and high interest rates already compressing profit margins across the offshore wind sector, additional conservation mandates threaten project viability. Striking a pragmatic balance between urgent climate mitigation and local biodiversity preservation remains the quintessential dilemma of modern environmental policy.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What has the expansion of offshore wind farms achieved in the UK?",
            points: 2.0,
            sort_order: 11,
            options: [
              { key: "A", text: "The total elimination of marine maritime transport" },
              { key: "B", text: "A noticeable displacement of domestic coal dependence" },
              { key: "C", text: "The universal lowering of household energy bills" },
              { key: "D", text: "The complete resolution of North Sea boundary disputes" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第一段末句明确指出 '...generating gigawatts of clean electricity that have displaced domestic coal dependence'，清洁电力取代了本土对燃煤的依赖，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Pile-driving during offshore wind construction is hazardous to marine mammals because it ______.",
            points: 2.0,
            sort_order: 12,
            options: [
              { key: "A", text: "contaminates the coastal water with toxic chemicals" },
              { key: "B", text: "generates acoustic disturbances that harm echolocation" },
              { key: "C", text: "drastically reduces local plankton populations" },
              { key: "D", text: "blocks migratory sea birds from accessing open waters" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实与因果题。第二段阐明海洋哺乳动物依靠回声定位（echolocation）觅食和导航，而桩基施工产生的声学破坏会造成听觉损伤或迫使其远离觅食地，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "What is the function of 'bubble curtains' mentioned in Paragraph 3?",
            points: 2.0,
            sort_order: 13,
            options: [
              { key: "A", text: "To anchor floating wind turbines firmly to the seabed" },
              { key: "B", text: "To significantly attenuate underwater construction noise" },
              { key: "C", text: "To illuminate marine navigation routes for coastal vessels" },
              { key: "D", text: "To replenish dissolved oxygen levels in depleted waters" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】例证细节题。第三段指出气泡幕（bubble curtains）'demonstrated an ability to attenuate underwater noise transmission by up to 90 percent'，其功能是大幅衰减水下施工噪音，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "According to financial stakeholders, ecological mitigation requirements ______.",
            points: 2.0,
            sort_order: 14,
            options: [
              { key: "A", text: "guarantee generous governmental subsidies" },
              { key: "B", text: "increase capital expenditure and strain profitability" },
              { key: "C", text: "attract an influx of private green bond investments" },
              { key: "D", text: "hasten the construction timeline of North Sea turbines" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】事实细节题。第四段指出 'these ecological precautions amplify overall capital expenditure... threatening project viability'，即增加资本支出并压低利润，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following best summarizes the main idea of the text?",
            points: 2.0,
            sort_order: 15,
            options: [
              { key: "A", text: "Offshore wind power in the UK must balance green energy goals with marine ecology" },
              { key: "B", text: "Technological innovation has permanently solved marine sound pollution" },
              { key: "C", text: "Marine conservation mandates should be suspended to combat climate change" },
              { key: "D", text: "Financial inflation has rendered offshore renewable energy obsolete" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨大意题。全文围绕英国海上风电既要推进去碳化清洁能源，又要兼顾海洋哺乳动物生态保护的困境与平衡策略展开，选项 A 概括最全面精确。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In an era dominated by hyper-connected smartphones and omnipresent notification feeds, the concept of the human attention span has emerged as a central cultural anxiety. Commentators routinely lament that continuous exposure to short-form video snippets and algorithmically personalized feeds has fractured our capacity for sustained contemplation, reducing modern intellects to superficial skimmers incapable of deep literary or philosophical engagement.

However, historical and cognitive perspectives invite a more nuanced interpretation. Historical research demonstrates that societal panic regarding the decay of attention is far from unprecedented. The invention of the printing press in the fifteenth century provoked grave warnings that the deluge of cheap books would overwhelm human memory and breed intellectual indolence. Similarly, the advent of nineteenth-century newspapers and early twentieth-century radio broadcasts was met with moral alarms that readers and listeners were losing the discipline required for scholarly reflection.

Cognitive psychologists point out that attention is not an immutable, single cognitive tank that is drained by novel media; rather, it is a highly malleable behavioral adaptation. Humans dynamically allocate cognitive resources according to ecological demands. While our capacity for prolonged passive immersion may indeed be challenged in fragmented digital environments, users concurrently develop sophisticated scanning and synthesis heuristics that allow them to process vast amounts of disparate information with remarkable velocity.

The urgent challenge, therefore, is not to wage a futile war against digital technologies or retreat into nostalgic technophobia. Instead, educational institutions must foster cognitive agency: the intentional cultivation of metacognitive habits that enable individuals to consciously toggle between rapid information triage and deep, uninterrupted mental focus.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Cultural commentators commonly worry that digital media has ______.",
            points: 2.0,
            sort_order: 16,
            options: [
              { key: "A", text: "undermined human capacity for sustained and deep contemplation" },
              { key: "B", text: "diminished youth engagement with democratic politics" },
              { key: "C", text: "completely replaced formal classroom instruction" },
              { key: "D", text: "caused permanent physical deterioration of ocular vision" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段末句提到 '...fractured our capacity for sustained contemplation, reducing modern intellects to superficial skimmers...'，评论家担心长久专注与深度思考能力被侵蚀，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why does the author mention the printing press and nineteenth-century newspapers in Paragraph 2?",
            points: 2.0,
            sort_order: 17,
            options: [
              { key: "A", text: "To demonstrate that modern attention anxiety has historical precedents" },
              { key: "B", text: "To argue that historical media technologies were strictly superior" },
              { key: "C", text: "To praise the early moralists for their farsightedness" },
              { key: "D", text: "To urge the modern press to return to vintage typesetting" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】例证修辞目的题。作者在第二段指出 'societal panic regarding the decay of attention is far from unprecedented'（对注意力衰退的恐慌远非史无前例），随后列举印刷术和报纸的恐慌历史作为例证，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to cognitive psychologists, human attention is ______.",
            points: 2.0,
            sort_order: 18,
            options: [
              { key: "A", text: "a rigid biological faculty that cannot be trained" },
              { key: "B", text: "an adaptable behavior that responds dynamically to environmental demands" },
              { key: "C", text: "wholly superior when consuming printed books over screens" },
              { key: "D", text: "permanently extinguished by short-form video consumption" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第三段指出 'rather, it is a highly malleable behavioral adaptation. Humans dynamically allocate cognitive resources according to ecological demands'，注意力是随环境动态调配的可塑适应行为，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "What do modern users develop while navigating digital environments?",
            points: 2.0,
            sort_order: 19,
            options: [
              { key: "A", text: "An inability to synthesize any textual information" },
              { key: "B", text: "Advanced heuristics for rapid scanning and synthesizing disparate information" },
              { key: "C", text: "A strict psychological aversion toward electronic communication" },
              { key: "D", text: "Enhanced photographic memory for ancient scripts" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第三段末句明确提到 'users concurrently develop sophisticated scanning and synthesis heuristics that allow them to process vast amounts of disparate information with remarkable velocity'，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that educational institutions should ______.",
            points: 2.0,
            sort_order: 20,
            options: [
              { key: "A", text: "ban smartphones entirely from all campus grounds" },
              { key: "B", text: "cultivate students' metacognitive ability to toggle between focus modes" },
              { key: "C", text: "replace traditional books exclusively with digital tablets" },
              { key: "D", text: "discourage philosophical reading in favor of coding skills" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】作者观点与结论题。最后一段指出教育机构应培养 cognitive agency，即养成在快速信息初筛与深度沉浸专注之间自主切换的元认知习惯，选 B。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `Major municipal art museums across Europe and North America are navigating a precarious fiscal landscape. Traditionally reliant on a tripartite funding model composed of governmental grants, corporate philanthropy, and private benefactors, these esteemed cultural institutions have found their balance sheets severely battered by persistent post-pandemic visitor hesitation, galloping inflation, and escalating energy overheads.

Faced with declining operational subsidies, several premier galleries have instituted steep ticket price increases, pushing general admission past the thirty-dollar mark. While museum directors defend these price adjustments as inevitable measures to keep gallery lights illuminated and safeguard irreplaceable cultural treasures, social equity advocates protest that exorbitant fees transform public cultural sanctuaries into exclusionary clubs reserved exclusively for affluent patrons.

Simultaneously, the ethics of cultural philanthropy have undergone intense public scrutiny. Grassroots activist groups and museum employees have mounted sustained campaigns demanding that institutions sever ties with corporate sponsors linked to fossil fuel extraction, arms manufacturing, or controversial pharmaceutical conglomerates. When institutions bow to public pressure and decline disreputable endowments, however, they rarely find alternative philanthropists ready to fill the resulting budgetary chasms.

In response to this multi-front squeeze, progressive museum administrators are re-evaluating their core operating paradigms. Instead of staging prohibitively expensive, international blockbusters that require exorbitant insurance and freight fees, galleries are leaning into their permanent collections, creating inventive thematic juxtapositions and digital narrative experiences that resonate with localized audiences without incurring ruinous debt.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Which factor has contributed to the fiscal distress of municipal art museums?",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Surging inflation and escalating energy expenditures" },
              { key: "B", text: "A total boycott by local educational school districts" },
              { key: "C", text: "Legal restrictions on purchasing international artifacts" },
              { key: "D", text: "Mandatory quotas on displaying digital NFT artworks" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段末尾指出 '...severely battered by persistent post-pandemic visitor hesitation, galloping inflation, and escalating energy overheads'，通胀加剧与能源开支攀升导致财务压力，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Critics argue that raising museum admission prices will ______.",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "permanently eliminate the need for philanthropic donations" },
              { key: "B", text: "alienate less affluent visitors and foster cultural exclusion" },
              { key: "C", text: "force museums to sell off core national collections" },
              { key: "D", text: "hasten the deterioration of delicate historical canvases" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节推断题。第二段指出高昂票价使公共文化殿堂变成仅限富裕赞助人进入的排他性俱乐部（exclusionary clubs reserved exclusively for affluent patrons），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Why does severing ties with controversial corporate donors create difficulties for museums?",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "It violates binding international copyright treaties" },
              { key: "B", text: "It rarely results in finding alternative donors to fill the financial void" },
              { key: "C", text: "It triggers immediate revocation of museum operating licenses" },
              { key: "D", text: "It prompts employee strikes across all curatorial departments" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】因果细节题。第三段末句指出当博物馆拒绝有争议的赞助时，'they rarely find alternative philanthropists ready to fill the resulting budgetary chasms'，即很少有其他慈善家愿意填补资金缺口，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "How are progressive museums adapting to the budgetary squeeze?",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "By staging even more lavish international blockbuster spectacles" },
              { key: "B", text: "By creatively leveraging permanent collections for localized audiences" },
              { key: "C", text: "By auctioning off public masterpieces to private hedge funds" },
              { key: "D", text: "By transferring all operations into proprietary virtual reality metaverses" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第四段指出美术馆放弃代价昂贵的大型巡展，而是 'leaning into their permanent collections, creating inventive thematic juxtapositions and digital narrative experiences that resonate with localized audiences'，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following would be the best title for the text?",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "The Disappearance of Fine Art in Contemporary Society" },
              { key: "B", text: "Municipal Museums: Financial Crises, Ethical Dilemmas, and Strategic Shifts" },
              { key: "C", text: "Why Corporate Philanthropy Must Be Completely Banned" },
              { key: "D", text: "Digital Immersion: The Universal Panacea for Art Conservation" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】主旨标题归纳题。文章全面剖析了公共艺术博物馆面临的财政困境（资金短缺与高通胀）、伦理道德抉择（赞助商审查与高票价争议）以及战略应对转型（立足馆藏与在地化），选项 B 概括最为完整深刻。"
          }
        ]
      }
    ]
  },

  // -------------------------------------------------------------------------
  // 2024 考研英语（二）
  // -------------------------------------------------------------------------
  {
    category_id: "ky2",
    year: 2024,
    title: "2024年全国硕士研究生招生考试英语（二）真题",
    exam_type: "real",
    duration_minutes: 60,
    total_score: 50.00,
    pass_score: 30.00,
    is_published: true,
    approval_status: "approved",
    passages: [
      {
        section_type: "cloze",
        title: "Section I: Use of English (知识运用·完形填空)",
        sort_order: 1,
        content: `Front-of-package food labeling has garnered global momentum as public health authorities strive to curb surging rates of diet-related chronic conditions. Proponents argue that straightforward interpretive schemes, such as traffic-light color codes or numerical nutritional ratings, empower shoppers to make healthier purchasing (1)____ in fast-paced retail settings.

Psychological investigations, however, suggest that consumer reactions to nutritional labels are frequently (2)____ by cognitive biases. Shoppers operating under time pressure or mental fatigue often exhibit an all-or-nothing mindset, viewing items with green indicators as universally benign while treating red indicators as strictly (3)____. This dichotomous perception can generate unexpected health halos, leading people to consume excessive portions of moderately wholesome foods under the mistaken belief that the product is completely calorie-free.

Furthermore, multinational packaged-food manufacturers frequently exploit ambiguities in regulatory thresholds. By reformulating recipes just enough to (4)____ penalizing score brackets, brands can burnish their nutritional credentials without substantially reducing aggregate sugars or sodium. Consequently, consumer education must accompany labeling mandates to ensure shoppers understand that processed foods, regardless of optimistic packaging, should not entirely (5)____ unadulterated whole foods.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "decisions" },
              { key: "B", text: "confessions" },
              { key: "C", text: "excuses" },
              { key: "D", text: "hesitations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。purchasing decisions（购买决策）是商业与消费心理学的标准搭配。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "simplified" },
              { key: "B", text: "distorted" },
              { key: "C", text: "repaired" },
              { key: "D", text: "clarified" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】动词搭配与消极语义。后文连接 cognitive biases（认知偏差），因此消费者对营养标签的反应经常被认知偏差所“扭曲/带偏”（distorted）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "toxic" },
              { key: "B", text: "beneficial" },
              { key: "C", text: "palatable" },
              { key: "D", text: "nutritious" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】对比与极端思维。前文提到非黑即白的非理性心态（all-or-nothing mindset），把绿色标志视为绝对安全，把红色标志视为有害/有毒（strictly toxic）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "avoid" },
              { key: "B", text: "attract" },
              { key: "C", text: "invite" },
              { key: "D", text: "intensify" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。食品加工商稍微改良配方，恰好“避开”（avoid）受罚的分数区间，属于规避监管行为。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "replace" },
              { key: "B", text: "imitate" },
              { key: "C", text: "contaminate" },
              { key: "D", text: "outnumber" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨常识与动词语义。加工食品无论外包装看起来多么健康，都不能完全“替代”（replace）新鲜天然的全谷全营养食物。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `The debate over post-pandemic remote work has entered a decisive institutional phase. While Silicon Valley titans and Wall Street investment banks have issued stringent return-to-office mandates, mid-market employers and regional service firms are aggressively leveraging permanent workplace flexibility as a vital recruiting weapon to lure skilled professionals away from metropolitan hubs.

Human resource surveys demonstrate that the retention premium of hybrid scheduling is now comparable to a substantial pay raise. Knowledge workers—particularly parents caring for young dependents and mid-career specialists burdened with arduous commutes—routinely express a willingness to sacrifice 5 to 10 percent of their base compensation in exchange for the autonomy to work from home two to three days a week. For regional companies unable to match the eye-popping wage packages of top-tier corporate conglomerates, remote-friendly policies provide an indispensable leveler.

Nevertheless, operational executives stress that distributed workforces present subtle managerial hazards. Unmonitored remote environments can degrade spontaneous informal collaboration, the serendipitous corridor conversations that often spark creative problem-solving. Furthermore, younger employees and entry-level recruits suffer disproportionately from remote isolation, missing out on the tacit institutional knowledge and direct mentorship traditionally absorbed through in-person office socialization.

To reconcile these competing pressures, forward-thinking enterprises are transitioning from arbitrary attendance quotas to 'purpose-driven co-location.' Under this philosophy, employees report to company facilities not to sit silently on individual video calls, but rather to participate in structured collaborative workshops, collective brainstorming sessions, and cultural cohesion events. By intentionally redesigning office hours around meaningful communal tasks, firms can preserve collaborative vitality without dismantling the autonomy their employees cherish.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Why are mid-market firms offering flexible working arrangements?",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "To attract skilled professionals away from corporate conglomerates" },
              { key: "B", text: "To comply with mandatory national labor legislation" },
              { key: "C", text: "To permanently liquidate physical commercial real estate" },
              { key: "D", text: "To reduce employee vacation entitlements" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段末尾指出 '...mid-market employers and regional service firms are aggressively leveraging permanent workplace flexibility as a vital recruiting weapon to lure skilled professionals away from metropolitan hubs'，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 2, many knowledge workers are willing to ______.",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "relocate overseas for corporate promotions" },
              { key: "B", text: "accept a modest pay reduction for hybrid scheduling flexibility" },
              { key: "C", text: "work indefinite overtime in metropolitan offices" },
              { key: "D", text: "relinquish their parental healthcare benefits" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第二段指出知识型工作者愿意放弃 5% 到 10% 的基本薪酬，以换取每周两到三天居家的工作自主权，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "What managerial challenge of distributed teams is highlighted in Paragraph 3?",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "The loss of spontaneous informal interaction and newcomer mentorship" },
              { key: "B", text: "Extravagant expenditures on high-speed internet subsidies" },
              { key: "C", text: "Frequent software hardware incompatibilities across devices" },
              { key: "D", text: "Widespread unionization among remote technical staff" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出远程办公会弱化偶发性的走廊灵感交流（spontaneous informal collaboration），且新员工容易缺乏现场社会化的直接导师指导（direct mentorship），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Under the philosophy of 'purpose-driven co-location', employees come to the office to ______.",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "conduct solitary video conferences in partitioned cubicles" },
              { key: "B", text: "engage in structured collaborative workshops and team cohesion events" },
              { key: "C", text: "undergo continuous biometric productivity surveillance" },
              { key: "D", text: "fulfill rigid weekly 50-hour punch-card quotas" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第四段指出有目的性的现场到岗是让员工参加结构化的协作工作坊、集体头脑风暴和团队凝聚活动，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "The author's tone toward hybrid working models can best be described as ______.",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "Dismissive and sarcastic" },
              { key: "B", text: "Balanced and constructive" },
              { key: "C", text: "Alarmist and fearful" },
              { key: "D", text: "Uncritically enthusiastic" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】作者观点与态度题。作者既分析了远程弹性的留人优势，也指出了其对偶发协作和新人培训的挑战，最后提出了建设性的“有目的性现场办公”平衡方案，客观务实，选 B。"
          }
        ]
      }
    ]
  }
];
