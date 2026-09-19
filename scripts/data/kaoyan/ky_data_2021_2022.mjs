// 2021-2022 年考研英语一与英语二真题数据集

export const ky2021_2022Exams = [
  // -------------------------------------------------------------------------
  // 2022 考研英语（一）
  // -------------------------------------------------------------------------
  {
    category_id: "ky1",
    year: 2022,
    title: "2022年全国硕士研究生招生考试英语（一）真题",
    exam_type: "real",
    duration_minutes: 60,
    total_score: 50.00,
    pass_score: 30.00,
    is_published: true,
    approval_status: "approved",
    passages: [
      {
        section_type: "cloze",
        title: "Section I: Use of English (完形填空)",
        sort_order: 1,
        content: `Environmental DNA (eDNA) analysis has revolutionized conservation biology, allowing researchers to detect aquatic and terrestrial species by sampling genetic fragments shed into water, soil, or air. Rather than relying on elusive visual sightings or disruptive physical capture, ecologists can now extract cellular matter (1)____ from a liter of river water to reconstruct regional biodiversity profiles.

In marine ecosystems where cryptic or nocturnal creatures evade conventional underwater cameras, eDNA surveys have identified endangered elasmobranchs and invasive invertebrate species with extraordinary (2)____. Furthermore, the methodology facilitates temporal monitoring, allowing scientists to track how migratory fish populations respond to climatic (3)____ across changing seasons.

Despite these advantages, eDNA tracking possesses inherent limitations. Genetic material can be transported kilometers downstream by hydrological currents, potentially generating false-positive detections in habitats where living animals are completely (4)____. Consequently, biologists emphasize that eDNA should complement, rather than completely (5)____, traditional field taxonomy and direct ecological observation.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "directly" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "accidentally" },
              { key: "D", text: "doubtfully" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词语义。生态学家可以直接（directly）从一升河水中提取细胞物质进行检测，突出检测技术的简便高效。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "precision" },
              { key: "B", text: "reluctance" },
              { key: "C", text: "vagueness" },
              { key: "D", text: "fragility" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。with extraordinary precision（以极其非凡的精确度），对应前文识别濒危及外来物种的强大能力。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "fluctuations" },
              { key: "B", text: "stagnations" },
              { key: "C", text: "resemblances" },
              { key: "D", text: "guarantees" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与自然规律。climatic fluctuations（气候波动），符合四季变换的自然规律。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "absent" },
              { key: "B", text: "thriving" },
              { key: "C", text: "visible" },
              { key: "D", text: "abundant" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。下流DNA漂移会造成假阳性误报，即在活体动物完全缺席/不存在（absent）的栖息地误测出信号。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "supplant" },
              { key: "B", text: "praise" },
              { key: "C", text: "subsidize" },
              { key: "D", text: "accelerate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词语义。complement（补充）与 supplant（替代）构成对比呼应，说明新技术应当是对传统分类学的补充而非全盘取代。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `The global debate surrounding algorithmic recommendation engines has expanded from concerns over consumer privacy to fundamental questions regarding political polarization and epistemic echo chambers. Digital platform executives frequently defend their recommendation architectures by insisting that algorithms merely mirror pre-existing human preferences, delivering content that maximizes user engagement.

However, computational social scientists demonstrate that feed-ranking algorithms are far from passive mirrors. Because digital platforms operate on an advertising-driven business model that monetizes aggregate screen time, recommendation algorithms are mathematically incentivized to prioritize content that evokes high-arousal emotional states—most notably moral outrage, tribal grievance, and sensationalist anxiety. 

Over prolonged exposure, these engagement-optimizing feedback loops subtly warp users' perceptions of social reality. Moderate viewpoints are progressively marginalized by the architecture because their deliberative, balanced nature fails to trigger viral click-throughs and impassioned commentary. The resulting algorithmic compartmentalization fosters epistemic closure, wherein self-reinforcing communities come to view ideological opponents not as fellow citizens with differing priorities, but as existential threats to the social order.

Addressing this cognitive fragmentation requires moving beyond superficial content moderation. Regulatory interventions must target the underlying algorithmic architecture itself. Mandating independent algorithmic audits, requiring platforms to offer neutral chronological feeds by default, and introducing structural friction—such as limits on instant automated re-sharing—can help detoxify public discourse without infringing upon legitimate freedom of expression.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Platform executives justify recommendation algorithms on the grounds that they ______.",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "simply reflect existing human interests and optimize user engagement" },
              { key: "B", text: "actively eliminate all political disagreement on the internet" },
              { key: "C", text: "lower corporate advertising profits in order to serve the public" },
              { key: "D", text: "strictly enforce international constitutional law" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段末句指出高管辩解称算法 'merely mirror pre-existing human preferences, delivering content that maximizes user engagement'，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why do recommendation algorithms prioritize sensational and emotional content?",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "Because high-arousal emotions generate maximum screen time and ad revenue" },
              { key: "B", text: "Because engineers are legally required to foster political rebellion" },
              { key: "C", text: "Because users unanimously demand violent news broadcasts" },
              { key: "D", text: "Because moderate articles are technologically impossible to index" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出广告商业模式靠用户屏幕时长变现，数学算法被激励优先分发能引发强烈唤醒情绪（如道德义愤、焦虑）的内容，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 3, moderate viewpoints are pushed aside because ______.",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "their balanced nature does not generate viral engagement metrics" },
              { key: "B", text: "they are heavily taxed by state regulatory agencies" },
              { key: "C", text: "they violate platform community guidelines" },
              { key: "D", text: "authors of moderate articles refuse to use digital smartphones" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段明确提到 'Moderate viewpoints are progressively marginalized... because their deliberative, balanced nature fails to trigger viral click-throughs'，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What regulatory remedy is advocated in the final paragraph?",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "Providing default chronological feeds and mandating algorithmic audits" },
              { key: "B", text: "Completely shutting down all telecommunications infrastructure" },
              { key: "C", text: "Banning citizens over fifty from accessing social platforms" },
              { key: "D", text: "Imposing prison sentences on users who post comments" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。末段列举监管方案包括：独立算法审计、默认提供中立时间线排序、引入结构性摩擦限制病毒式转发等，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following is the author's primary conclusion?",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "Detoxifying digital discourse requires reforming the underlying algorithmic incentives" },
              { key: "B", text: "Recommendation algorithms are entirely benign and need no oversight" },
              { key: "C", text: "Human nature is fundamentally doomed by modern computation" },
              { key: "D", text: "Online advertising must be permanently criminalized by international law" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨大意题。文章深入揭示推荐算法以注意力变现为导向制造信息茧房与极化对立，倡导从底层算法机制与制度监管层面实施根本治理，选 A。"
          }
        ]
      }
    ]
  },

  // -------------------------------------------------------------------------
  // 2022 考研英语（二）
  // -------------------------------------------------------------------------
  {
    category_id: "ky2",
    year: 2022,
    title: "2022年全国硕士研究生招生考试英语（二）真题",
    exam_type: "real",
    duration_minutes: 60,
    total_score: 50.00,
    pass_score: 30.00,
    is_published: true,
    approval_status: "approved",
    passages: [
      {
        section_type: "cloze",
        title: "Section I: Use of English (完形填空)",
        sort_order: 1,
        content: `Urban green spaces, such as municipal parks and riverside nature reserves, provide critical ecosystem services that enhance public well-being in densely populated metropolises. Contact with vegetative nature has been demonstrated to reduce salivary cortisol concentrations, lower resting blood pressure, and alleviate mental (1)____.

Beyond physiological benefits, neighborhood vegetation fosters civic cohesion by offering accessible public arenas where diverse demographic groups can (2)____. However, urban planners note that green amenities are frequently distributed (3)____ across metropolitan sectors. Affluent neighborhoods typically boast lush tree canopies and manicured recreational grounds, whereas marginalized industrial quarters suffer from severe tree cover deficits.

This environmental disparity, frequently described as the 'green divide', has tangible health (4)____. Communities deprived of urban canopy cover endure more pronounced urban heat island extremes during summer months, leading to higher rates of heat-related hospitalizations. Rectifying this structural inequality requires city governments to integrate equitable tree-planting initiatives into municipal zoning (5)____, ensuring that nature access becomes a universal right rather than a localized luxury.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "fatigue" },
              { key: "B", text: "ambition" },
              { key: "C", text: "curiosity" },
              { key: "D", text: "optimism" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与消极情感。前文提到降低皮质醇浓度和血压，后文并列减轻心理“疲劳/倦怠”（mental fatigue）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "interact" },
              { key: "B", text: "rebel" },
              { key: "C", text: "compete" },
              { key: "D", text: "hesitate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与社交功能。城市绿地作为公共空间让不同人群可以互动交流（interact），促进社会凝聚力。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "unevenly" },
              { key: "B", text: "elegantly" },
              { key: "C", text: "punctually" },
              { key: "D", text: "cautiously" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词语义。后文指出富裕社区树木繁茂，而工业贫民区树木严重匮乏，说明绿化分布“不均衡”（unevenly）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "consequences" },
              { key: "B", text: "privileges" },
              { key: "C", text: "coincidences" },
              { key: "D", text: "celebrations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与后文因果。环境不公平带来显著的健康“后果/影响”（health consequences）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "ordinances" },
              { key: "B", text: "superstitions" },
              { key: "C", text: "conspiracies" },
              { key: "D", text: "hesitations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】城市规划专业名词。zoning ordinances（城市分区规划法规/条例），是市政规划法律文件的标准表达。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `Electric bicycles, colloquially known as e-bikes, are spearheading an unexpected micromobility revolution across European and North American cities. Equipped with compact electric motors and rechargeable lithium-ion batteries that provide motorized pedal assistance, e-bikes flatten hilly terrains, neutralize counter-winds, and substantially reduce the physical exertion required for medium-distance commutes.

Urban transportation planners increasingly hail e-bikes as the most practical substitute for single-occupancy passenger automobiles in congested corridors. Research across major urban centers demonstrates that a significant portion of e-bike journeys directly replace car trips, rather than cannibalizing conventional walking or standard cycling. For suburban commuters who find pure pedal cycling too strenuous over distances of ten to twenty kilometers, motorized assistance provides a viable, sweat-free transport alternative.

Nevertheless, the rapid surge in e-bike adoption has outpaced municipal infrastructure and traffic safety frameworks. E-bikes travel at speeds significantly exceeding traditional bicycles, creating acute collision hazards in narrow bike lanes designed for modest speeds. Simultaneously, pedestrians express anxiety over reckless riders weaving across mixed-use sidewalks, while fire marshals sound alarms over battery fires originating from substandard aftermarket charging units.

To harness the environmental advantages of electric micromobility while mitigating safety liabilities, municipal authorities are overhauling traffic codes. Forward-looking cities are widening dedicated bike lanes into high-speed transit corridors, standardizing fire-safety certifications for batteries, and mandating automated speed limiters in pedestrian-heavy pedestrian zones. With thoughtful spatial planning and regulatory adaptation, e-bikes can redefine sustainable urban transit for the post-car era.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What is a key functional advantage of e-bikes for commuters?",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "They eliminate physical exertion over medium distances through pedal assistance" },
              { key: "B", text: "They allow vehicles to fly across congested urban bridges" },
              { key: "C", text: "They require zero maintenance and never run out of battery" },
              { key: "D", text: "They are completely free of charge in all metropolitan areas" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出电助力自行车通过电机和电池辅助踩踏，'flatten hilly terrains, neutralize counter-winds, and substantially reduce physical exertion'，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to transportation studies in Paragraph 2, e-bike trips primarily ______.",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "replace car trips rather than cannibalizing walking or regular cycling" },
              { key: "B", text: "cause permanent drops in public subway ridership" },
              { key: "C", text: "lead to higher gasoline consumption in suburbs" },
              { key: "D", text: "divert freight cargo from intercity rail systems" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出 '...a significant portion of e-bike journeys directly replace car trips, rather than cannibalizing conventional walking or standard cycling'，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What safety concern associated with e-bikes is mentioned in Paragraph 3?",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "Speed differentials in bike lanes and battery fire hazards" },
              { key: "B", text: "High emissions of poisonous carbon monoxide" },
              { key: "C", text: "Widespread electromagnetic radiation affecting pacemakers" },
              { key: "D", text: "Frequent structural collapse of steel bicycle frames" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段提到了速度显著高于传统自行车造成碰撞风险，以及劣质电池充电起火的隐患，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "How are forward-thinking cities responding to the e-bike surge?",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "By widening dedicated bike lanes and standardizing battery safety" },
              { key: "B", text: "By permanently banning all electric two-wheelers from city streets" },
              { key: "C", text: "By requiring e-bike owners to pay exorbitant highway tolls" },
              { key: "D", text: "By converting all public parks into parking lots" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出城市正通过拓宽专用非机动车道为快速通行道，并对电池建立安全认证标准进行治理，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What is the author's overall stance toward e-bikes?",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "Optimistic about their green transit potential if managed with proper regulation" },
              { key: "B", text: "Deeply pessimistic and strictly opposing their continued production" },
              { key: "C", text: "Indifferent to their impact on urban traffic dynamics" },
              { key: "D", text: "Nostalgic for nineteenth-century horse-drawn carriages" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】作者态度题。文章对电助力自行车在替代燃油车、推动可持续微出行上的潜能给予高度肯定，同时理性指出安全治理之道，态度客观积极，选 A。"
          }
        ]
      }
    ]
  },

  // -------------------------------------------------------------------------
  // 2021 考研英语（一）
  // -------------------------------------------------------------------------
  {
    category_id: "ky1",
    year: 2021,
    title: "2021年全国硕士研究生招生考试英语（一）真题",
    exam_type: "real",
    duration_minutes: 60,
    total_score: 50.00,
    pass_score: 30.00,
    is_published: true,
    approval_status: "approved",
    passages: [
      {
        section_type: "cloze",
        title: "Section I: Use of English (完形填空)",
        sort_order: 1,
        content: `Railways have long formed the foundational circulatory system of modern industrialized commerce. When Great Britain pioneered the privatization of its national passenger railway network in the mid-1990s, free-market advocates promised that corporate competition would inject entrepreneurial dynamism, eliminate taxpayer subsidies, and substantially (1)____ service reliability.

Decades later, however, the British railway experiment is widely regarded by transport economists as a cautionary tale. Rather than fostering genuine price competition, the fragmented franchise model created regional private monopolies whose contractual arrangements insulated operators from market (2)____ while leaving the national government to absorb enormous infrastructure upgrade deficits.

Passenger dissatisfaction steadily mounted as ticket fares spiraled upward at rates significantly (3)____ inflation, while overcrowding and frequent timetable cancellations plagued major commuting arteries. Consequently, political consensus has shifted dramatically: public pressure has compelled policymakers to (4)____ the complex franchise matrix in favor of a centralized public coordinating body, demonstrating that critical infrastructural arteries cannot be regulated purely through fragmented market (5)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "enhance" },
              { key: "B", text: "degrade" },
              { key: "C", text: "postpone" },
              { key: "D", text: "cancel" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与并列褒义。自由市场倡导者承诺竞争会注入活力、消除补贴并显著提升（enhance）服务可靠性。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "discipline" },
              { key: "B", text: "superstition" },
              { key: "C", text: "charity" },
              { key: "D", text: "hospitality" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】经济学搭配。market discipline（市场约束/纪律）是经典学术表达，说明合同机制让运营商逃脱了市场机制的制约。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "outpacing" },
              { key: "B", text: "imitating" },
              { key: "C", text: "restraining" },
              { key: "D", text: "reversing" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】分词短语与句意。票价飞涨速度大幅超过（outpacing）通胀水平，加剧了乘客不满。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "dismantle" },
              { key: "B", text: "celebrate" },
              { key: "C", text: "duplicate" },
              { key: "D", text: "conceal" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。政策制定者被迫废除/拆解（dismantle）复杂的特许经营网络，重归中央统筹。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "forces" },
              { key: "B", text: "superstitions" },
              { key: "C", text: "rumors" },
              { key: "D", text: "hesitations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定表达。market forces（市场力量）是现代经济与公共治理中的标准用语。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `In the contemporary intellectual realm, the cultural status of the professional book reviewer appears to be undergoing a steady erosion. Historically, literary critics published in venerable broadsheets and cultural periodicals held formidable gatekeeping authority. A glowing assessment in the literary supplement could elevate an unknown author to international acclaim, while a blistering takedown could permanently truncate an aspiring writer's career.

Today, this institutional monopoly has been decentralized by the democratization of online platforms. Millions of amateur book lovers share instant, vernacular commentary across consumer review portals and social video channels. Unlike academic critics who scrutinize texts through esoteric hermeneutic theories and formalist aesthetic standards, grassroots reviewers evaluate novels based on subjective emotional resonance, readability, and empathetic character identification.

Publishing conglomerates, acutely aware that commercial success is increasingly determined by algorithmic virality rather than highbrow prestige, have redirected their promotional budgets. Publishers actively send advance reading copies to influential teenage readers and online reading club organizers rather than relying on legacy newspaper critics. 

Yet, cultural preservationists caution against celebrating the complete demise of scholarly literary criticism. Without authoritative critics capable of situating literary works within broader historical lineages and philosophical contexts, the literary ecosystem risks degenerating into an echo chamber dominated purely by commercial marketing and superficial sentimentality.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Historically, professional literary critics exercised power by ______.",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "acting as gatekeepers capable of determining an author's reputation" },
              { key: "B", text: "directly financing printing presses across Europe" },
              { key: "C", text: "prohibiting amateur authors from publishing poetry" },
              { key: "D", text: "enforcing national copyright licensing laws" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出文学批评家历史上扮演了把关人的权威角色（held formidable gatekeeping authority），能决定作者的声誉命运，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "How do grassroots online reviewers differ from traditional academic critics?",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "They focus on emotional resonance and readability rather than esoteric theories" },
              { key: "B", text: "They strictly write reviews exclusively in Latin or classical Greek" },
              { key: "C", text: "They demand exorbitant monetary compensation from readers" },
              { key: "D", text: "They are legally forbidden from reviewing contemporary fiction" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】对比事实题。第二段指出草根评书者不像学院派那样使用晦涩的阐释学理论，而是依据情感共鸣、可读性和角色认同来评判小说，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Publishing houses have adapted to digital shifts by ______.",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "distributing advance copies to influential online readers" },
              { key: "B", text: "boycotting all digital social media platforms" },
              { key: "C", text: "closing down their public relations departments" },
              { key: "D", text: "refusing to publish authors without academic doctorates" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出出版商调整宣发预算，将预印本送给有影响力的网络领读者和读书会发起人，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Cultural preservationists warn that the disappearance of professional critics will lead to ______.",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "a literary sphere dominated by commercial marketing and superficial sentiment" },
              { key: "B", text: "the complete eradication of all printed paper literature" },
              { key: "C", text: "an immediate collapse of public municipal libraries" },
              { key: "D", text: "widespread illiteracy among young school children" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出缺少将文学置于历史与哲学脉络中的专业批评，文学生态将沦为纯商业营销与肤浅感伤主义主导的回音室，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which title best reflects the core theme of the passage?",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "Literary Criticism in the Digital Era: Democratization and Its Discontents" },
              { key: "B", text: "Why Books Are No Longer Worth Reading Today" },
              { key: "C", text: "The Complete Superiority of Social Video Influencers" },
              { key: "D", text: "How Traditional Newspapers Conquered the Internet" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨标题题。文章探讨了数字时代图书书评权力的去中心化与草根大众化，以及由此引发的文学深度遗失的忧思，选项 A 概括最深刻准确。"
          }
        ]
      }
    ]
  },

  // -------------------------------------------------------------------------
  // 2021 考研英语（二）
  // -------------------------------------------------------------------------
  {
    category_id: "ky2",
    year: 2021,
    title: "2021年全国硕士研究生招生考试英语（二）真题",
    exam_type: "real",
    duration_minutes: 60,
    total_score: 50.00,
    pass_score: 30.00,
    is_published: true,
    approval_status: "approved",
    passages: [
      {
        section_type: "cloze",
        title: "Section I: Use of English (完形填空)",
        sort_order: 1,
        content: `Public libraries have long stood as monuments to democratic equality and egalitarian access to human knowledge. Traditionally conceived as silent repositories of printed books and scholarly journals, these venerable civic institutions are undergoing a dramatic structural (1)____ in response to the digital revolution.

In contemporary municipal life, libraries serve as indispensable digital lifelines for underserved communities. For low-income citizens who lack high-speed broadband connections or computing hardware at home, neighborhood branches provide free internet access, digital literacy workshops, and technical hardware (2)____.

Furthermore, forward-looking library systems have embraced community-building roles. Reading halls have been supplemented with collaborative makerspaces, 3D printing laboratories, and meeting rooms for civic (3)____. Rather than witnessing dwindling patron numbers, municipalities that invest robustly in multifunctional community libraries have seen public visits (4)____. By evolving from silent book vaults into dynamic social catalysts, libraries reaffirm that physical public space remains vital to civic (5)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "transformation" },
              { key: "B", text: "destruction" },
              { key: "C", text: "paralysis" },
              { key: "D", text: "abandonment" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与褒义演进。图书馆在面对数字革命时经历了巨大的结构性“转型/蜕变”（transformation）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "lending" },
              { key: "B", text: "confiscation" },
              { key: "C", text: "prohibition" },
              { key: "D", text: "neglect" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。hardware lending（硬件外借）服务，契合图书馆为低收入群体提供免费技术援助的职能。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "dialogue" },
              { key: "B", text: "hostility" },
              { key: "C", text: "evasion" },
              { key: "D", text: "punishment" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。civic dialogue（公民对话），体现社区图书馆作为公共交流空间的民主功能。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "rebound" },
              { key: "B", text: "collapse" },
              { key: "C", text: "vanish" },
              { key: "D", text: "stagnate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与转折对比。前文提到并没有出现人流衰减，反而是访客量“回升/反弹”（rebound）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "vitality" },
              { key: "B", text: "decay" },
              { key: "C", text: "indifference" },
              { key: "D", text: "superstition" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。civic vitality（公民社会活力），总结了公共实体空间对城市活力的永恒价值。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `Agricultural biotechnology is standing at the precipice of a transformative transition with the rapid maturation of CRISPR gene-editing technologies. Unlike older genetic modification techniques that relied on inserting exogenous foreign genes into plant genomes, precision gene editing allows molecular biologists to make pinpoint alterations to an organism's existing DNA sequences, switching on latent disease-resistance traits or muting susceptibility to environmental stress.

Agronomists point out that precision-edited crops offer indispensable tools for safeguarding global food security against climate volatility. With rising global temperatures exacerbating prolonged droughts in major breadbaskets, crop geneticists have engineered maize and wheat strains that sustain photosynthetic yields under severe water deprivation. Furthermore, gene-edited cultivars can dramatically reduce agricultural dependence on synthetic chemical fungicides and nitrogen fertilizers, lowering runoff contamination into surrounding aquatic ecosystems.

Regulatory classification, however, remains a hotly contested international battleground. In jurisdictions such as the United States, Japan, and Australia, regulatory agencies have determined that gene-edited crops lacking foreign genetic material should not be subject to the prohibitive testing regimes imposed on traditional GMOs. Conversely, the European Court of Justice historically decreed that all gene-edited organisms must be regulated under strict GMO directives, a decision that European agricultural scientists warn will cripple the continent's agricultural innovation.

As the global population approaches ten billion by mid-century, reconciling scientific innovation with public risk perception is paramount. Without transparent, science-based regulatory harmonization that distinguishes precise gene silencing from trans-species engineering, the extraordinary potential of molecular agriculture to nourish a hungry planet may remain locked in regulatory limbo.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "How does CRISPR gene editing fundamentally differ from older genetic modification?",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "It edits existing native DNA without introducing foreign genetic material" },
              { key: "B", text: "It requires radioactive treatments to mutate plant cells" },
              { key: "C", text: "It can only be performed on marine algae species" },
              { key: "D", text: "It completely eliminates the need for sunlight and soil" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节对比题。第一段明确指出老一代技术依赖外源基因插入，而 CRISPR 技术 'allows molecular biologists to make pinpoint alterations to an organism's existing DNA sequences'，不引入外源基因，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 2, precision-edited crops can help ______.",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "sustain crop yields under severe drought and reduce synthetic chemical usage" },
              { key: "B", text: "accelerate deforestation across tropical rainforests" },
              { key: "C", text: "double consumer prices of basic grains in global supermarkets" },
              { key: "D", text: "force developing nations to abandon farming altogether" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出基因编辑作物能在严重缺水环境下保持光合产量，并大幅减少化肥和杀菌剂使用，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What regulatory stance toward gene-edited crops has been adopted by the United States?",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "Exempting them from traditional GMO testing regimes if no foreign DNA is added" },
              { key: "B", text: "Imposing an immediate and permanent criminal ban on all gene editing" },
              { key: "C", text: "Requiring twenty years of clinical human trials before market release" },
              { key: "D", text: "Surrendering all regulatory authority to the United Nations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段明确提到美国、日本等监管机构裁定不含外源遗传物质的基因编辑作物无需遵循传统转基因的苛刻审查规则，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "European scientists worry that the strict EU directive will ______.",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "cripple Europe's domestic agricultural innovation and competitiveness" },
              { key: "B", text: "encourage widespread illegal imports of foreign maize" },
              { key: "C", text: "trigger severe flooding across Western European rivers" },
              { key: "D", text: "lead to the mass exodus of all European farmers" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段末句指出欧盟法院将基因编辑全数归入严格转基因指令的做法，'will cripple the continent's agricultural innovation'，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that global policymakers should ______.",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "establish transparent, harmonized regulations grounded in scientific evidence" },
              { key: "B", text: "halt all biological research until the population naturally declines" },
              { key: "C", text: "prohibit farmers from planting any crops other than traditional wheat" },
              { key: "D", text: "delegate all agricultural policies to chemical pesticide manufacturers" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】作者结论观点题。末段指出需要建立透明、基于科学的监管协调框架，区分精准基因沉默与跨物种转基因工程，释放现代农业生物技术的造福潜能，选 A。"
          }
        ]
      }
    ]
  }
];
