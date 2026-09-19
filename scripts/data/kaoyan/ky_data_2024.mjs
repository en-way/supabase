// 2024 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2024Exams = [
  // =========================================================================
  // 2024 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Regular physical exercise has long been associated with enhanced cardiovascular endurance and general metabolic health. However, recent neurobiological research indicates that sustained aerobic activity may exert an equally (1)____ influence on brain architecture. Specifically, sustained aerobic regimens appear to stimulate neurogenesis within the hippocampus, a cerebral region (2)____ for spatial navigation and long-term memory consolidation.

In clinical trials involving elderly cohorts, individuals adhering to a moderate routine showed measurable expansions in hippocampal volume over twelve months, (3)____ their sedentary peers who suffered age-related cellular atrophy. Researchers hypothesize that exercise triggers the synthesis of brain-derived neurotrophic factor (BDNF), a protein that supports neuron survival and (4)____ synaptic plasticity.

Nevertheless, neuroscientists caution that physical exertion cannot completely (5)____ the pathological cascades of neurodegenerative disorders such as Alzheimer's disease. While exercise fosters cognitive (6)____, it operates (7)____ alongside genetic, dietary, and sleep-related determinants. Furthermore, intense physical training can occasionally induce excessive oxidative stress if rest intervals are (8)____. 

Medical authorities therefore emphasize that exercise prescriptions must be carefully (9)____ to individual physiological baselines. A brisk daily walk may provide optimal neuroprotective stimuli for a frail pensioner, (10)____ an elite marathoner requires substantially higher workloads to induce comparable cellular adaptations.

In addition to cellular remodeling, aerobic exertion markedly elevates cerebral blood perfusion. This heightened vascular flow delivers oxygen and glucose (11)____ to metabolically active cortical zones, accelerating the clearance of toxic metabolic (12)____ such as amyloid-beta aggregates. Consequently, subjects routinely report acute elevations in executive functioning and attentional (13)____ immediately following moderate workouts.

Psychologists note that the emotional benefits of fitness are equally (14)____. Sustained muscular contraction prompts the endogenous release of endorphins and dopamine, neurotransmitters that blunt pain perception and cultivate feelings of (15)____. For individuals battling clinical anxiety or depressive symptoms, regular exercise serves as an effective therapeutic adjunct, often (16)____ standard pharmacological interventions by restoring neurochemical equilibrium.

Yet, despite widespread awareness of these neurological dividends, global physical inactivity rates remain stubbornly (17)____. Modern sedentary occupational patterns and pervasive digital screen reliance (18)____ people to spend prolonged periods immobile. Public health campaigns must therefore move beyond passive health warnings, actively designing urban environments that (19)____ incidental physical movement into everyday commuting. Ultimately, viewing physical exercise not as an onerous chore, but as an indispensable biological (20)____, will be essential for safeguarding cognitive longevity in aging global populations.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "profound" },
              { key: "B", text: "negligible" },
              { key: "C", text: "destructive" },
              { key: "D", text: "temporary" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。根据前文 equally 及后文刺激海马体神经发生等重大发现可知，有氧运动对大脑构造同样具有深远、深刻的（profound）影响。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "crucial" },
              { key: "B", text: "harmful" },
              { key: "C", text: "useless" },
              { key: "D", text: "reluctant" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词与介词搭配。海马体是负责空间导航和长期记忆巩固的关键（crucial for）脑区。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "in contrast to" },
              { key: "B", text: "in terms of" },
              { key: "C", text: "by means of" },
              { key: "D", text: "with respect to" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】逻辑对比关系。坚持适度锻炼的老人海马体体积增加，与其久坐少动、细胞萎缩的同龄人形成鲜明对比（in contrast to）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "promotes" },
              { key: "B", text: "inhibits" },
              { key: "C", text: "diminishes" },
              { key: "D", text: "neglects" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。and 连接两个积极并列动作，BDNF 蛋白支持神经元存活并促进（promotes）突触可塑性。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "halt" },
              { key: "B", text: "trigger" },
              { key: "C", text: "accelerate" },
              { key: "D", text: "induce" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与语境转折。虽然运动有益，但科学家警告运动不能完全阻止/遏制（halt）神经退行性疾病的病理级联恶化。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "resilience" },
              { key: "B", text: "paralysis" },
              { key: "C", text: "decay" },
              { key: "D", text: "decline" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。运动培养的是认知韧性与恢复力（cognitive resilience），属于积极神经学术语。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "synergistically" },
              { key: "B", text: "exclusively" },
              { key: "C", text: "reluctantly" },
              { key: "D", text: "superficially" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词搭配。与 alongside 并列呼应，运动与其他遗传和饮食因素协同起作用（operates synergistically）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "inadequate" },
              { key: "B", text: "excessive" },
              { key: "C", text: "plentiful" },
              { key: "D", text: "luxurious" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。如果休息间隔不充分、不足（inadequate），高强度训练可能引发过量氧化应激损伤。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "tailored" },
              { key: "B", text: "blinded" },
              { key: "C", text: "condemned" },
              { key: "D", text: "delayed" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与介词搭配。运动处方必须针对个人生理基线量身定制（tailored to）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "whereas" },
              { key: "B", text: "because" },
              { key: "C", text: "unless" },
              { key: "D", text: "until" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】逻辑连词辨析。前半句讲快步走适合体弱老人，后半句对比精英马拉松运动员需要更大负荷，两者为转折对比，用 whereas（而/然而）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "directly" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "doubtfully" },
              { key: "D", text: "accidentally" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词语义。血液循环增强将氧气和葡萄糖直接（directly）输送到大脑皮层代谢活跃区域。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "byproducts" },
              { key: "B", text: "treasures" },
              { key: "C", text: "incentives" },
              { key: "D", text: "privileges" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】专业名词搭配。metabolic byproducts（代谢副产物/代谢废物），如淀粉样蛋白沉积。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "focus" },
              { key: "B", text: "hostility" },
              { key: "C", text: "paralysis" },
              { key: "D", text: "fatigue" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与褒义并列。运动后执行功能与注意力专注度（attentional focus）显著提升。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "striking" },
              { key: "B", text: "invisible" },
              { key: "C", text: "meaningless" },
              { key: "D", text: "harmful" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。心理学家指出，运动在情绪层面的裨益同样显著、引人注目（striking）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "well-being" },
              { key: "B", text: "anxiety" },
              { key: "C", text: "guilt" },
              { key: "D", text: "grief" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与多巴胺效应。内啡肽与多巴胺能缓解疼痛，培养幸福感与身心健康感（feelings of well-being）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "complementing" },
              { key: "B", text: "condemning" },
              { key: "C", text: "eradicating" },
              { key: "D", text: "ruining" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动名词搭配。运动作为辅助治疗手段，通常对标准药物疗法起到补充、协同辅助作用（complementing standard interventions）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "high" },
              { key: "B", text: "low" },
              { key: "C", text: "rare" },
              { key: "D", text: "negligible" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词与转折词 despite 呼应。尽管运动好处多，全球缺乏运动的比例依然顽固居高不下（stubbornly high）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "condition" },
              { key: "B", text: "forbid" },
              { key: "C", text: "liberate" },
              { key: "D", text: "rescue" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词语义。condition sb to do sth（使某人习惯于……/制约某人），现代久坐工作模式让人习惯性长时间静止不动。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "weave" },
              { key: "B", text: "extinguish" },
              { key: "C", text: "postpone" },
              { key: "D", text: "dissect" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。weave ... into ...（将……编织融入……中），城市规划应将身体活动自然融入日常通勤。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "necessity" },
              { key: "B", text: "luxury" },
              { key: "C", text: "superstition" },
              { key: "D", text: "coincidence" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义对比。前文为 not as an onerous chore（不应被视为繁重负担），后文转折为 indispensable biological necessity（不可或缺的生命生理必需品）。"
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
            sort_order: 21,
            options: [
              { key: "A", text: "prohibit all forms of generative AI and biometric surveillance" },
              { key: "B", text: "establish an overarching legal framework to oversee algorithmic systems" },
              { key: "C", text: "subsidize European tech startups to compete against foreign monopolies" },
              { key: "D", text: "curtail the expansion of venture capital in continental Europe" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】主旨事实细节题。第一段首句明确指出该法案是世界上首个旨在跨行业规范算法系统的综合法律框架（world's first comprehensive legal framework to regulate algorithmic systems），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 2, which AI application would be classified as 'high-risk'?",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Casual mobile video games" },
              { key: "B", text: "Algorithmic employee recruitment tools" },
              { key: "C", text: "Basic spell-check applications" },
              { key: "D", text: "Weather forecasting simulators" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第二段指出高风险系统包括算法招聘工具、医疗诊断及生物识别监视设备，对应 algorithmic employee recruitment tools，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Critics worry that the EU regulation will disadvantage European startups because ______.",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "they lack the financial resources to handle heavy compliance costs" },
              { key: "B", text: "they are legally forbidden from patenting proprietary algorithms" },
              { key: "C", text: "foreign markets will block European software exports" },
              { key: "D", text: "European engineers refuse to collaborate with venture capitalists" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段阐明中小初创公司缺乏雄厚资金聘请合规审计律师，沉重的管理合规开支将挤占基础研发资金，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Supporters of the AI Act believe that robust regulation will ______.",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "hasten the withdrawal of foreign software developers" },
              { key: "B", text: "foster public trust necessary for widespread AI adoption" },
              { key: "C", text: "eliminate the need for human supervision in automation" },
              { key: "D", text: "lower consumer expectations regarding digital privacy" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】观点细节题。第四段首句阐明法律确定性与伦理信任是技术被普遍接纳不可或缺的前提（ethical trust are indispensable prerequisites for widespread technological adoption），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "The phrase 'Brussels Effect' in the final sentence implies that ______.",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "European regulations can influence global market practices" },
              { key: "B", text: "tech companies will permanently abandon Brussels headquarters" },
              { key: "C", text: "regulatory disputes must be settled in Belgian courts" },
              { key: "D", text: "democratic values will be subordinated to technological speed" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义推断题。第四段末句指出欧盟设立高标准后迫使外国开发者也遵从欧盟规范，即布鲁塞尔效应指的是欧盟法规单方面塑造全球市场标准的现象，选 A。"
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
            sort_order: 26,
            options: [
              { key: "A", text: "The total elimination of marine maritime transport" },
              { key: "B", text: "A noticeable displacement of domestic coal dependence" },
              { key: "C", text: "The universal lowering of household energy bills" },
              { key: "D", text: "The complete resolution of North Sea boundary disputes" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第一段末句明确提到清洁电力替代了国内对煤炭的依赖（displaced domestic coal dependence），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Pile-driving during offshore wind construction is hazardous to marine mammals because it ______.",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "contaminates the coastal water with toxic chemicals" },
              { key: "B", text: "generates acoustic disturbances that harm echolocation" },
              { key: "C", text: "drastically reduces local plankton populations" },
              { key: "D", text: "blocks migratory sea birds from accessing open waters" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】因果推断题。第二段指出打桩水下噪音破坏了海洋哺乳动物赖以导航觅食的回声定位能力（echolocation），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "What is the function of 'bubble curtains' mentioned in Paragraph 3?",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "To anchor floating wind turbines firmly to the seabed" },
              { key: "B", text: "To significantly attenuate underwater construction noise" },
              { key: "C", text: "To illuminate marine navigation routes for coastal vessels" },
              { key: "D", text: "To replenish dissolved oxygen levels in depleted waters" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】例证细节题。第三段指出水下气泡幕能够将施工噪音衰减达 90%（attenuate underwater noise transmission by up to 90 percent），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "According to financial stakeholders, ecological mitigation requirements ______.",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "guarantee generous governmental subsidies" },
              { key: "B", text: "increase capital expenditure and strain profitability" },
              { key: "C", text: "attract an influx of private green bond investments" },
              { key: "D", text: "hasten the construction timeline of North Sea turbines" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】事实细节题。第四段指出环保降噪措施增加了总体资本支出，在通胀和高利率下压缩了行业利润率（amplify overall capital expenditure... compressing profit margins），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following best summarizes the main idea of the text?",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Offshore wind power in the UK must balance green energy goals with marine ecology" },
              { key: "B", text: "Technological innovation has permanently solved marine sound pollution" },
              { key: "C", text: "Marine conservation mandates should be suspended to combat climate change" },
              { key: "D", text: "Financial inflation has rendered offshore renewable energy obsolete" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】文章主旨大意题。全文围绕英国大力推进海上风电减碳与保护海洋生物声学环境之间的平衡难题展开，选 A。"
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
            sort_order: 31,
            options: [
              { key: "A", text: "undermined human capacity for sustained and deep contemplation" },
              { key: "B", text: "diminished youth engagement with democratic politics" },
              { key: "C", text: "completely replaced formal classroom instruction" },
              { key: "D", text: "caused permanent physical deterioration of ocular vision" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出评论家担心短视频与算法信息流击碎了人类持续沉思的能力（fractured our capacity for sustained contemplation），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why does the author mention the printing press and nineteenth-century newspapers in Paragraph 2?",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "To demonstrate that modern attention anxiety has historical precedents" },
              { key: "B", text: "To argue that historical media technologies were strictly superior" },
              { key: "C", text: "To praise the early moralists for their farsightedness" },
              { key: "D", text: "To urge the modern press to return to vintage typesetting" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】例证修辞目的题。作者在第二段列举印刷术和报纸的恐慌史，旨在说明针对注意力衰退的社会恐慌自古有之、并非史无前例（far from unprecedented），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to cognitive psychologists, human attention is ______.",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "a rigid biological faculty that cannot be trained" },
              { key: "B", text: "an adaptable behavior that responds dynamically to environmental demands" },
              { key: "C", text: "wholly superior when consuming printed books over screens" },
              { key: "D", text: "permanently extinguished by short-form video consumption" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第三段指出注意力并非一成不变的蓄水池，而是一种高度可塑的行为适应能力（highly malleable behavioral adaptation），根据环境需求动态调配，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "What do modern users develop while navigating digital environments?",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "An inability to synthesize any textual information" },
              { key: "B", text: "Advanced heuristics for rapid scanning and synthesizing disparate information" },
              { key: "C", text: "A strict psychological aversion toward electronic communication" },
              { key: "D", text: "Enhanced photographic memory for ancient scripts" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第三段末句指出数字环境中的用户发展出了快速扫读和综合归纳复杂信息的启发式技能（sophisticated scanning and synthesis heuristics），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that educational institutions should ______.",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "ban smartphones entirely from all campus grounds" },
              { key: "B", text: "cultivate students' metacognitive ability to toggle between focus modes" },
              { key: "C", text: "replace traditional books exclusively with digital tablets" },
              { key: "D", text: "discourage philosophical reading in favor of coding skills" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】作者观点与结论题。第四段指出教育机构不应退回技术恐惧症，而应培养认知自主性（cognitive agency），让学生能在快速初筛与深度专注之间自如切换，选 B。"
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
            sort_order: 36,
            options: [
              { key: "A", text: "Surging inflation and escalating energy expenditures" },
              { key: "B", text: "A total boycott by local educational school districts" },
              { key: "C", text: "Legal restrictions on purchasing international artifacts" },
              { key: "D", text: "Mandatory quotas on displaying digital NFT artworks" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段末尾指出博物馆财政受到访客观望、恶性通胀及能源支出激增的沉重打击（galloping inflation, and escalating energy overheads），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Critics argue that raising museum admission prices will ______.",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "permanently eliminate the need for philanthropic donations" },
              { key: "B", text: "alienate less affluent visitors and foster cultural exclusion" },
              { key: "C", text: "force museums to sell off core national collections" },
              { key: "D", text: "hasten the deterioration of delicate historical canvases" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节推断题。第二段指出高票价将公共文化殿堂变为了唯富人专享的排他性俱乐部（exclusionary clubs reserved exclusively for affluent patrons），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Why does severing ties with controversial corporate donors create difficulties for museums?",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "It violates binding international copyright treaties" },
              { key: "B", text: "It rarely results in finding alternative donors to fill the financial void" },
              { key: "C", text: "It triggers immediate revocation of museum operating licenses" },
              { key: "D", text: "It prompts employee strikes across all curatorial departments" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】因果细节题。第三段末句阐明拒绝声誉不佳的捐赠后，很难找到替代资助者填补预算鸿沟（rarely find alternative philanthropists ready to fill the resulting budgetary chasms），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "How are progressive museums adapting to the budgetary squeeze?",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "By staging even more lavish international blockbuster spectacles" },
              { key: "B", text: "By creatively leveraging permanent collections for localized audiences" },
              { key: "C", text: "By auctioning off public masterpieces to private hedge funds" },
              { key: "D", text: "By transferring all operations into proprietary virtual reality metaverses" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第四段指出美术馆放弃烧钱的国际巡展，而是深挖馆藏常设展（leaning into their permanent collections），创造共鸣且低负债的策展体验，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following would be the best title for the text?",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "The Disappearance of Fine Art in Contemporary Society" },
              { key: "B", text: "Municipal Museums: Financial Crises, Ethical Dilemmas, and Strategic Shifts" },
              { key: "C", text: "Why Corporate Philanthropy Must Be Completely Banned" },
              { key: "D", text: "Digital Immersion: The Universal Panacea for Art Conservation" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】主旨标题题。文章系统剖析了公共艺术博物馆面临的财政赤字、捐助伦理争议及立足馆藏的战略转向，选项 B 概括最为准确深刻。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2024 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Front-of-package food labeling has garnered global momentum as public health authorities strive to curb surging rates of diet-related chronic conditions. Proponents argue that straightforward interpretive schemes, such as traffic-light color codes or numerical nutritional ratings, empower shoppers to make healthier purchasing (1)____ in fast-paced retail settings.

Psychological investigations, however, suggest that consumer reactions to nutritional labels are frequently (2)____ by cognitive biases. Shoppers operating under time pressure or mental fatigue often exhibit an all-or-nothing mindset, viewing items with green indicators as universally benign while treating red indicators as strictly (3)____. This dichotomous perception can generate unexpected health halos, leading people to consume excessive portions of moderately wholesome foods under the mistaken belief that the product is completely (4)____.

Furthermore, multinational packaged-food manufacturers frequently exploit ambiguities in regulatory thresholds. By reformulating recipes just enough to (5)____ penalizing score brackets, brands can burnish their nutritional credentials without substantially reducing aggregate sugars or sodium. Consequently, consumer education must accompany labeling mandates to ensure shoppers understand that processed foods, regardless of optimistic packaging, should not entirely (6)____ unadulterated whole foods.

Nutritionists emphasize that dietary literacy involves deciphering subtle deceptive marketing. Terms like 'organic', 'all-natural', and 'gluten-free' are routinely (7)____ by marketing strategists to project an aura of vitality, even when applied to ultra-processed snacks packed with refined starches. When consumers encounter these buzzwords, their critical evaluation faculties are often (8)____, leading them to overlook elevated saturated fat levels.

In response, several governments are testing mandatory warning seals rather than voluntary positive badges. Black octagonal warning labels on Chilean food packaging, indicating excessive calories or sugar, have driven significant (9)____ in sugary beverage purchases. Seeing a bold warning sign provokes immediate risk aversion, prompting shoppers to reconsider impulsive pantry (10)____.

Nevertheless, industry lobbyists continue to mount fierce resistance, claiming that graphic warning labels induce unnecessary consumer (11)____ and harm national agricultural commerce. They lobby for complex monochrome tables printed unobtrusively on package backs, where shoppers (12)____ have time to read fine print during weekly grocery runs.

Academic researchers point out that socioeconomic disparities also shape how labeling systems (13)____. Higher-income households with greater nutritional education actively interpret micro-nutrient percentages, (14)____ lower-income families experiencing economic strain are primarily constrained by shelf prices. A food item carrying a green nutritional badge remains unattainable if it costs twice as much as an ultra-processed staple.

Public health economists conclude that labeling alone cannot remedy systemic dietary (15)____. Fiscal policies, such as targeted subsidies for fresh vegetables combined with excise taxes on sugary drinks, must operate in (16)____ with informational labels. Creating an equitable food environment requires making wholesome choices not merely visually identifiable, but economically (17)____.

Schools and community centers must also play a foundational role, integrating practical meal-planning skills into primary curricula. Teaching children how to prepare balanced meals from raw ingredients cultivates lifelong dietary (18)____, insulating future generations against aggressive fast-food advertising.

Ultimately, front-of-package labels should be viewed as a valuable first step in a protracted public health (19)____. Empowering citizens to reclaim sovereignty over their nutritional choices will require sustained political will, regulatory vigilance, and a collective commitment to prioritizing human wellness over corporate food (20)____.`,
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
            explanation: "【考点精析】固定搭配。purchasing decisions（购买决策）符合零售场景。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "distorted" },
              { key: "B", text: "simplified" },
              { key: "C", text: "repaired" },
              { key: "D", text: "clarified" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与消极宾语。消费者对营养标签的反应常被认知偏差带偏、扭曲（distorted by cognitive biases）。"
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
            explanation: "【考点精析】对比极端思维。非黑即白心态下，绿色被当作完全有益，红色被视为严格有毒有害（strictly toxic）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "calorie-free" },
              { key: "B", text: "unaffordable" },
              { key: "C", text: "poisonous" },
              { key: "D", text: "artificial" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】语境推理。健康光环效应导致人们误以为该食品完全零热量、无卡路里（calorie-free）而过量摄入。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "avoid" },
              { key: "B", text: "attract" },
              { key: "C", text: "intensify" },
              { key: "D", text: "invite" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。微调配方以避开（avoid）低分处罚区间。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "replace" },
              { key: "B", text: "imitate" },
              { key: "C", text: "contaminate" },
              { key: "D", text: "exceed" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。加工食品不能完全替代（replace）新鲜未掺杂的天然全食物。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "weaponized" },
              { key: "B", text: "condemned" },
              { key: "C", text: "prohibited" },
              { key: "D", text: "eliminated" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻修辞。营销人员把“有机”、“纯天然”等词汇武器化（weaponized），用作诱导消费的光环工具。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "dulled" },
              { key: "B", text: "sharpened" },
              { key: "C", text: "celebrated" },
              { key: "D", text: "restored" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。被流行词汇吸引时，消费者的批判评估能力往往被钝化、麻痹（dulled），忽视了高脂肪含量。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "declines" },
              { key: "B", text: "surges" },
              { key: "C", text: "rebounds" },
              { key: "D", text: "expansions" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与警示标签效果。黑色八角警示标签导致含糖饮料购买量显著下降（declines）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "purchases" },
              { key: "B", text: "complaints" },
              { key: "C", text: "inspections" },
              { key: "D", text: "lawsuits" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。重估冲动性食品购买（impulsive pantry purchases）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "panic" },
              { key: "B", text: "trust" },
              { key: "C", text: "joy" },
              { key: "D", text: "pride" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。食品游说团体声称警示标签会引起不必要的消费者恐慌（consumer panic）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "seldom" },
              { key: "B", text: "always" },
              { key: "C", text: "eagerly" },
              { key: "D", text: "cheerfully" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】频度副词。顾客在快节奏超市购物中很少（seldom）有闲暇去细读包装背面微小的营养成分表。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "function" },
              { key: "B", text: "collapse" },
              { key: "C", text: "decay" },
              { key: "D", text: "freeze" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词语义。社会阶层差距影响了标签系统如何实际发挥功能（how labeling systems function）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "whereas" },
              { key: "B", text: "because" },
              { key: "C", text: "unless" },
              { key: "D", text: "since" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】逻辑对比连词。高收入家庭分析微量营养素百分比，而（whereas）低收入家庭主要受商品价格约束。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "disparities" },
              { key: "B", text: "triumphs" },
              { key: "C", text: "remedies" },
              { key: "D", text: "privileges" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。单一标签无法纠正系统性的饮食差距与不公（dietary disparities）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "tandem" },
              { key: "B", text: "isolation" },
              { key: "C", text: "opposition" },
              { key: "D", text: "dispute" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。operate in tandem with（与……紧密协同配合运行）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "affordable" },
              { key: "B", text: "prohibitive" },
              { key: "C", text: "unpopular" },
              { key: "D", text: "tasteless" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词对比。健康选择不仅要在视觉上清晰可辨，更要在经济上负担得起（economically affordable）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "resilience" },
              { key: "B", text: "indifference" },
              { key: "C", text: "hostility" },
              { key: "D", text: "addiction" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与褒义搭配。从小培养烹饪技能可塑造终身饮食抵抗力/韧性（dietary resilience），抵制垃圾食品诱惑。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "campaign" },
              { key: "B", text: "superstition" },
              { key: "C", text: "scandal" },
              { key: "D", text: "retreat" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。protracted public health campaign（长期的公共卫生运动/战役）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "profits" },
              { key: "B", text: "charities" },
              { key: "C", text: "superstitions" },
              { key: "D", text: "donations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】价值判断对比。优先考虑人类健康，而非企业食品暴利（corporate food profits）。"
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
            sort_order: 21,
            options: [
              { key: "A", text: "To attract skilled professionals away from corporate conglomerates" },
              { key: "B", text: "To comply with mandatory national labor legislation" },
              { key: "C", text: "To permanently liquidate physical commercial real estate" },
              { key: "D", text: "To reduce employee vacation entitlements" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出中型企业利用常态化弹性工时作为招聘利器，从大都市巨头处吸引熟练专业技术人才，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 2, many knowledge workers are willing to ______.",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "relocate overseas for corporate promotions" },
              { key: "B", text: "accept a modest pay reduction for hybrid scheduling flexibility" },
              { key: "C", text: "work indefinite overtime in metropolitan offices" },
              { key: "D", text: "relinquish their parental healthcare benefits" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第二段明确指出知识型员工愿意放弃 5% 到 10% 的基本薪酬，以换取每周两到三天居家的工作自主权，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "What managerial challenge of distributed teams is highlighted in Paragraph 3?",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "The loss of spontaneous informal interaction and newcomer mentorship" },
              { key: "B", text: "Extravagant expenditures on high-speed internet subsidies" },
              { key: "C", text: "Frequent software hardware incompatibilities across devices" },
              { key: "D", text: "Widespread unionization among remote technical staff" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段阐述远程模式削弱了偶发性走廊头脑风暴，且新员工易被孤立并缺少导师直接传授经验，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Under the philosophy of 'purpose-driven co-location', employees come to the office to ______.",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "conduct solitary video conferences in partitioned cubicles" },
              { key: "B", text: "engage in structured collaborative workshops and team cohesion events" },
              { key: "C", text: "undergo continuous biometric productivity surveillance" },
              { key: "D", text: "fulfill rigid weekly 50-hour punch-card quotas" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第四段指出有目的性的到岗是让员工参加结构化的协作工作坊与团队凝聚活动，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "The author's tone toward hybrid working models can best be described as ______.",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Dismissive and sarcastic" },
              { key: "B", text: "Balanced and constructive" },
              { key: "C", text: "Alarmist and fearful" },
              { key: "D", text: "Uncritically enthusiastic" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】态度意图题。作者理性权衡了灵活性优势与管理协作隐忧，并提出建设性到岗方案，态度客观平衡且具建设性，选 B。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `Electric vehicles (EVs) are transitioning from a niche green status symbol into the cornerstone of global automotive production. Propelled by generous state purchase subsidies, stringent emissions mandates, and tumbling battery manufacturing costs, electric cars have captured significant market shares across Western Europe, China, and North America.

However, the rapid influx of battery-electric cars onto public thoroughfares is colliding with a profound suburban infrastructure bottleneck: residential and public charging availability. While affluent homeowners with detached suburban houses and private garages can effortlessly install overnight charging stations, apartment dwellers and dense urban residents who park on public curbs face severe charging scarcity. These 'garage-less' drivers must rely on public fast-charging plazas, which often suffer from broken hardware, incompatible proprietary plug connectors, and volatile pricing structures during peak hours.

Utility grid operators voice parallel concerns regarding localized distribution capacity. If millions of commuter vehicles plug into charging circuits simultaneously upon arriving home at 6:00 PM, suburban neighborhood electrical substations risk thermal overloads, tripping circuit breakers and triggering localized blackouts.

To avert catastrophic grid failures while democratizing electric mobility, municipal planners are pioneering smart-charging architectures and bi-directional 'vehicle-to-grid' (V2G) systems. Under dynamic pricing models, smart chargers automatically schedule vehicle charging during deep overnight troughs when overall power demand collapses and wind generation surges. In addition, V2G-equipped cars can discharge surplus stored battery energy back into regional grids during peak heatwaves, transforming idling automobiles into decentralized batteries that fortify national energy resilience.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What problem do urban apartment residents face when adopting electric vehicles?",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "A severe lack of private overnight home charging access" },
              { key: "B", text: "A complete legal ban on driving electric cars in cities" },
              { key: "C", text: "An inability to purchase automobile insurance" },
              { key: "D", text: "Excessive gasoline consumption during short commutes" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出没有私人车库的公寓居民无法安装夜间充电桩，面临严重的公共充电匮乏，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Utility grid operators worry that mass EV adoption could lead to ______.",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "substation overloads and localized blackouts during peak hours" },
              { key: "B", text: "the complete evaporation of petroleum reserves" },
              { key: "C", text: "widespread electromagnetic interference with television sets" },
              { key: "D", text: "a sharp drop in domestic renewable power generation" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出傍晚下班集中充电可能导致配电变电站过载并触发局域停电（thermal overloads, tripping circuit breakers and triggering localized blackouts），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Smart chargers mitigate grid stress by ______.",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "automatically shifting charging sessions to overnight low-demand hours" },
              { key: "B", text: "cutting off electrical power to household refrigerators" },
              { key: "C", text: "converting battery energy directly into diesel fuel" },
              { key: "D", text: "disabling automotive motors whenever highways are congested" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出智能充电桩通过动态电价，自动将充电调度至深夜负荷低谷期，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What is the function of 'vehicle-to-grid' (V2G) technology?",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "It allows parked vehicles to discharge stored energy back into the grid during peaks" },
              { key: "B", text: "It transmits high-speed satellite internet to municipal traffic lights" },
              { key: "C", text: "It physically locks tires when a vehicle exceeds the speed limit" },
              { key: "D", text: "It automatically reports speeding infractions to insurance firms" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】概念例证题。第四段指出双向车网互动允许车辆在电网负荷高峰期将电池储存的多余电能反哺回电网，将闲置车辆变为分布式蓄电池，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that successful EV transition requires ______.",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "intelligent grid coordination and accessible charging solutions" },
              { key: "B", text: "an immediate return to traditional internal combustion engines" },
              { key: "C", text: "banning all apartment dwellers from buying automobiles" },
              { key: "D", text: "nationalizing all private electric car manufacturers" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。全文围绕电动车普及必须攻克充电桩公平接入与电网智能交互双重瓶颈展开，选 A。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `Urban green corridors—continuous networks of vegetated linear parks, tree-lined canals, and re-wilded railway tracks—have emerged as essential infrastructure for climate adaptation in contemporary landscape architecture. Rather than treating parks as isolated recreational islands encircled by concrete expressways, ecological urbanists advocate for interconnected ecological arteries that weave through the metropolitan fabric.

Ecological assessments reveal that connected corridors yield biodiversity benefits far superior to fragmented green patches. Wildlife species, including pollinators, migratory songbirds, and small mammals, require connected migratory routes to forage, disperse genetic material, and escape localized environmental disturbances. Isolated urban parks frequently suffer from genetic inbreeding and localized extinctions, whereas linked corridors sustain robust ecological gene flow.

Moreover, green corridors provide profound thermal mitigation for human populations. Cities across the globe endure punishing 'urban heat island' effects, wherein asphalt highways and dark masonry absorb solar radiation, elevating ambient temperatures by four to eight degrees Celsius relative to outlying rural zones. Vegetated corridors channel cooling breezes from outlying river valleys deep into suffocating downtown centers, while dense tree canopies shade pedestrian sidewalks and evaporate moisture, substantially reducing air-conditioning loads in adjacent office towers.

Securing continuous rights-of-way through hyper-dense urban centers, however, represents a formidable political and fiscal challenge. Municipal governments face intense pressure from commercial developers who covet vacant transit strips for high-yield luxury real estate. Visionary cities are responding through innovative land-use regulations, enacting mandates that require private developers to incorporate publicly accessible green easements into skyscraper designs. By harmonizing commercial development with ecological connectivity, metropolises can cultivate resilience in an increasingly volatile climate future.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "How do urban green corridors differ from traditional city parks?",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "They are continuous, interconnected linear networks rather than isolated patches" },
              { key: "B", text: "They are built exclusively underground beneath subway tracks" },
              { key: "C", text: "They prohibit all pedestrian access and recreation" },
              { key: "D", text: "They are manufactured entirely from artificial synthetic turf" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节对比题。第一段指出传统公园是孤立绿岛，而生态绿道是穿透城市机理的互联互通线性网络（continuous networks of vegetated linear parks），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why are connected corridors superior for urban wildlife?",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "They enable migration and maintain healthy genetic gene flow" },
              { key: "B", text: "They provide cages that protect animals from wild predators" },
              { key: "C", text: "They eliminate the need for animals to drink freshwater" },
              { key: "D", text: "They allow rare birds to nest directly inside automobiles" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出孤立公园容易导致近亲繁殖和物种局部灭绝，而连续廊道为野生动物提供了觅食和基因交流的通道，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Green corridors alleviate urban heat islands by ______.",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "channeling cooling breezes and providing protective shade and evaporation" },
              { key: "B", text: "painting asphalt roadways with thick white reflective paint" },
              { key: "C", text: "prohibiting the installation of air-conditioning units" },
              { key: "D", text: "flooding downtown street intersections with sea water" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出绿道能将外围凉风输送至内城，并通过树冠遮阴与水分蒸腾显著降温，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What obstacle hinders the creation of continuous green corridors?",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Competition for vacant land from lucrative commercial developers" },
              { key: "B", text: "A severe national shortage of tree seeds and saplings" },
              { key: "C", text: "Universal citizen protests against pedestrian walking trails" },
              { key: "D", text: "Strict constitutional bans on planting grass near buildings" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出商业地产商觊觎地块用于开发高回报豪华物业，土地竞争激烈（pressure from commercial developers who covet vacant transit strips），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following best reflects the author's message?",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Interconnected green corridors are vital for sustainable, climate-resilient cities" },
              { key: "B", text: "Modern skyscrapers should be permanently banned from all metropolises" },
              { key: "C", text: "Traditional municipal parks are entirely useless and should be paved over" },
              { key: "D", text: "Urban heat island effects are harmless natural phenomena" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】文章主旨大意题。全文系统阐明了互联互通的城市绿色廊道在保护物种基因、降温防灾及提升城市气候韧性中的不可替代价值，选 A。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `The traditional linear narrative of post-graduate career trajectories—graduating from university, securing an entry-level position at an established firm, and ascending a predictable corporate ladder—has largely disintegrated for modern graduates. In a labor market characterized by rapid technological obsolescence and recurring economic restructuring, early-career professionals face unpredictable employment pathways.

Labor economists note that the half-life of professional technical skills has contracted to less than five years. The rapid advent of workplace automation, generative artificial intelligence, and algorithmic workflow management has rendered purely technical proficiencies insufficient for long-term career resilience. Consequently, employers are shifting hiring criteria away from narrow technical degree credentials toward adaptive cognitive capabilities, such as systemic problem-solving, cross-disciplinary synthesis, and emotional intelligence.

In response to this fluid landscape, graduates are embracing lifelong upskilling as a permanent career strategy. Rather than viewing education as a terminal credential achieved in one's early twenties, ambitious professionals continually enroll in micro-credential bootcamps, executive certifications, and modular online courses to recalibrate their skill portfolios. Concurrently, fractional employment, project-based freelancing, and portfolio careers are shedding their historic stigma, increasingly recognized as viable avenues for cultivating diversified professional autonomy.

Universities and corporate employers must adapt their developmental frameworks to support this new paradigm. Higher education institutions must transcend rigid disciplinary silos, embedding dynamic experiential internships and adaptive problem-solving curricula into undergraduate education. Employers, for their part, must recognize that investing in ongoing workforce education is not an altruistic luxury, but an essential operational imperative to prevent organizational stagnation in a hyper-competitive global economy.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "How has the post-graduate career trajectory changed for modern graduates?",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "The predictable corporate ladder has been replaced by fluid, unpredictable paths" },
              { key: "B", text: "Graduates are guaranteed lifetime tenure upon completing high school" },
              { key: "C", text: "Most graduates are legally forced to work in heavy agriculture" },
              { key: "D", text: "University degrees have become completely illegal in corporate hiring" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出传统的线性晋升阶梯瓦解，取而代之的是高度流动的非线性职业路径，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why are employers shifting away from narrow technical credentials?",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Technical skills rapidly become obsolete due to automation and AI" },
              { key: "B", text: "Graduates with technical degrees demand excessive salaries" },
              { key: "C", text: "Modern corporations no longer utilize computers in office operations" },
              { key: "D", text: "Technical training makes employees emotionally argumentative" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出技能半衰期已缩短至不足五年，自动化和 AI 使单一技术技能迅速过时，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 3, modern professionals are adopting ______.",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "lifelong upskilling and flexible portfolio careers" },
              { key: "B", text: "total retirement from all employment by age thirty" },
              { key: "C", text: "a refusal to learn any new digital software applications" },
              { key: "D", text: "exclusive reliance on lifelong family financial allowances" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出年轻从业者将终身学习（lifelong upskilling）作为长久生存策略，并积极践行多元化的组合式职业生涯（portfolio careers），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "How should higher education institutions adapt to this labor reality?",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "By breaking disciplinary silos and integrating experiential problem-solving" },
              { key: "B", text: "By closing all humanities and social science faculties" },
              { key: "C", text: "By extending undergraduate bachelor programs to ten years" },
              { key: "D", text: "By banning students from participating in corporate internships" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出大学必须打破学科壁垒（transcend rigid disciplinary silos），融入体验式实习与自适应问题解决能力培养，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following best summarizes the main theme of the text?",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Navigating Career Resilience: Lifelong Learning in an Era of Job Disruption" },
              { key: "B", text: "Why University Education Should Be Completely Abolished" },
              { key: "C", text: "The Universal Superiority of Lifetime Corporate Tenured Employment" },
              { key: "D", text: "How Artificial Intelligence Will Starve All Human Workers" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨标题题。全文探讨了职业模式剧变背景下，从业人员如何通过终身进阶技能学习构建职业韧性，以及高校与雇主的相应变革，选项 A 概括最契合。"
          }
        ]
      }
    ]
  }
];
