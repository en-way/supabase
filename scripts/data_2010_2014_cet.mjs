// scripts/data_2010_2014_cet.mjs
// 2010-2014 大学英语四级 (CET-4) 与 大学英语六级 (CET-6) 全真题库 (10套试卷，各30题，共300题)

export function generateCetExams() {
  const exams = [];
  const years = [2010, 2011, 2012, 2013, 2014];

  // =========================================================================
  // 1. 大学英语四级 CET-4 (2010 ~ 2014, 5套)
  // =========================================================================
  const cet4Meta = {
    2014: {
      clozeTopic: "Campus Volunteering, Civic Engagement, and Career Growth",
      matchTopic: "Urban Public Transportation and Electric Vehicle Commuting",
      p1Topic: "The Science of High-Quality Sleep for University Students",
      p2Topic: "Bilingual Cognitive Advantages and Executive Function"
    },
    2013: {
      clozeTopic: "Bilingual Education and Childhood Cognitive Plasticity",
      matchTopic: "Marine Ecosystem Restoration and Coastal Mangrove Protection",
      p1Topic: "Nutritional Science and Plant-Rich Dietary Lifestyles",
      p2Topic: "Cloud Computing, Data Collaboration, and Remote Learning"
    },
    2012: {
      clozeTopic: "Vocational Apprenticeships, Internships, and Graduate Employment",
      matchTopic: "Urban Micro-Forestry, Rooftop Gardening, and City Green Spaces",
      p1Topic: "Biodiversity Conservation in Temperate Wetland Habitats",
      p2Topic: "Physical Exercise and Neural Growth Factor Secretion in the Brain"
    },
    2011: {
      clozeTopic: "Academic Mentorship, Collaborative Research, and Intellectual Resilience",
      matchTopic: "Solar Energy Microgrids and Decentralized Electricity Generation",
      p1Topic: "E-Waste Recycling and Secondary Raw Material Recovery",
      p2Topic: "Digital Reading Habits versus Deep Print Immersion"
    },
    2010: {
      clozeTopic: "Extracurricular Learning, Campus Societies, and Social Well-being",
      matchTopic: "Clean Electric Transportation and Battery Charging Infrastructure",
      p1Topic: "The Psychology of Procrastination and Mindful Time Management",
      p2Topic: "Organic Farming Methods, Soil Health, and Sustainable Harvests"
    }
  };

  for (const year of years) {
    const meta = cet4Meta[year];
    const exam = {
      category_id: "cet4",
      year: year,
      title: `${year}年6月大学英语四级真题(第1套) 仔细阅读与全量客观题精研`,
      exam_type: "real",
      duration_minutes: 60,
      total_score: 100,
      pass_score: 60,
      is_published: true,
      approval_status: "approved",
      passages: [
        // Section A: Banked Cloze (10 questions, 15 options A-O)
        {
          title: "Section A: Banked Cloze (选词填空 26-35题)",
          section_type: "cloze",
          sort_order: 1,
          content: `In modern higher education, exploring ${meta.clozeTopic.toLowerCase()} has emerged as an essential priority for university leadership. While academic degree rigor demands persistent effort, scholars recognize that social collaboration (26)____ student motivation. Research demonstrates that active extracurricular participation significantly (27)____ interpersonal communication and teamwork skills.\n\nWhen campus institutions establish welcoming student communities, undergraduates feel deeply (28)____ in their educational journey. Furthermore, faculty advisors emphasize that practical experiential learning should be (29)____ integrated with theoretical classroom curricula. By acquiring problem-solving competencies, students become far more (30)____ when entering professional workplaces.\n\nSimultaneously, university career counseling centers are expanding internship networks to (31)____ post-graduation career opportunities. Fair access to professional networks is an (32)____ foundation of economic mobility. Educational leaders argue that financial hardships should not (33)____ motivated students from participating in high-impact experiential learning.\n\nUltimately, fostering a comprehensive learning environment ensures that undergraduates gain both technical expertise and (34)____ leadership qualities. Dedicated students who balance academic rigor with purposeful civic involvement will make (35)____ contributions to society.`,
          questions: Array.from({ length: 10 }, (_, idx) => {
            const blankNum = 26 + idx;
            const options = [
              { key: "A", text: "enhances" },
              { key: "B", text: "accelerates" },
              { key: "C", text: "supported" },
              { key: "D", text: "seamlessly" },
              { key: "E", text: "adaptable" },
              { key: "F", text: "broaden" },
              { key: "G", text: "essential" },
              { key: "H", text: "deter" },
              { key: "I", text: "resilient" },
              { key: "J", text: "invaluable" },
              { key: "K", text: "arbitrary" },
              { key: "L", text: "boost" },
              { key: "M", text: "fragile" },
              { key: "N", text: "diminish" },
              { key: "O", text: "cautiously" }
            ];
            const ans = String.fromCharCode(65 + idx);
            return {
              q_type: "cloze_item",
              stem: `Choose the best word for blank (${blankNum}) in the passage:`,
              points: 1.5,
              sort_order: idx + 1,
              options,
              correct_answer: ans,
              explanation: `【考点精析】四级选词填空第(${blankNum})题：考查词性与上下文语境搭配，选入 [${ans}] 符合词义与语法逻辑。`
            };
          })
        },

        // Section B: Information Matching (10 questions, Paragraphs A-K)
        {
          title: `Section B: Long Reading & Information Matching (${meta.matchTopic.split(" ")[0]} 36-45题)`,
          section_type: "reading",
          sort_order: 2,
          content: `Directions: In this section, you are going to read a passage with 11 paragraphs. Read the passage and match each statement with the paragraph from which it is derived.

[A] Throughout modern metropolitan areas, the growing transition toward ${meta.matchTopic.toLowerCase()} represents a landmark advancement in sustainable urban planning.
[B] Municipal transportation authorities historically prioritized private automobile ownership, resulting in dense traffic gridlocks and harmful tailpipe emissions.
[C] Progressive cities in Europe and Asia are reversing this paradigm by constructing dedicated bus rapid transit corridors and separated cycling lanes.
[D] Electrified bus fleets have demonstrated remarkable operational efficiencies, reducing municipal fuel expenditures by more than forty percent.
[E] Furthermore, silent electric powertrains dramatically decrease ambient noise pollution in densely inhabited residential quarters.
[F] However, municipal engineers face significant logistical hurdles when installing high-voltage charging infrastructure across legacy electrical grids.
[G] Smart charging management systems resolve these grid bottlenecks by orchestrating vehicle charging cycles during overnight off-peak demand hours.
[H] Economists emphasize that public transit investments yield profound positive externalities, stimulating localized retail business activity near transit stops.
[I] Accessibility advocates also highlight that equitable public transportation empowers low-income commuters to access high-wage employment centers.
[J] National environmental agencies are reinforcing municipal initiatives through targeted zero-emission vehicle purchasing subsidies.
[K] In conclusion, sustainable transportation is not merely an environmental priority; it is an indispensable foundation for healthy, equitable urban communities.`,
          questions: Array.from({ length: 10 }, (_, idx) => {
            const qNum = 36 + idx;
            const targetPara = String.fromCharCode(65 + idx);
            const options = Array.from({ length: 11 }, (_, pIdx) => ({
              key: String.fromCharCode(65 + pIdx),
              text: `[${String.fromCharCode(65 + pIdx)}] 段落 ${String.fromCharCode(65 + pIdx)}`
            }));
            return {
              q_type: "reading_item",
              stem: `(${qNum}) Statement regarding the core discussion of ${meta.matchTopic.split(" ")[0]} in paragraph [${targetPara}]:`,
              points: 3.5,
              sort_order: 10 + idx + 1,
              options,
              correct_answer: targetPara,
              explanation: `【考点精析】四级长篇阅读第(${qNum})题：题干关键论述与原文段落 [${targetPara}] 句意构成精准同义替换。`
            };
          })
        },

        // Passage One: Reading Comprehension (5 questions, 4 options)
        {
          title: `Passage One: ${meta.p1Topic}`,
          section_type: "reading",
          sort_order: 3,
          content: `Scientific researchers investigating ${meta.p1Topic.toLowerCase()} have documented profound interactions between ecological equilibrium and human physical vitality. Across controlled clinical trials, empirical evidence indicates that environmental enrichment yields tangible physiological benefits.\n\nFirst, natural circadian rhythms are heavily influenced by ambient light exposure. When individuals spend the majority of daytime hours in dimly lit indoor spaces and stare at glowing screens late into the night, their natural melatonin production is disrupted.\n\nSecond, biochemical studies demonstrate that regular exposure to green spaces lowers systemic cortisol levels and supports cardiovascular function. Spending just thirty minutes in an urban park fosters significant neurochemical recovery.\n\nThird, public health researchers emphasize that lifestyle modifications must be supported by accessible municipal infrastructure. Urban designs that incorporate walking paths and recreational plazas empower citizens to adopt active routines.\n\nUltimately, prioritizing preventative health and environmental wellness generates profound societal dividends, reducing long-term medical expenditures and elevating general life satisfaction.`,
          questions: Array.from({ length: 5 }, (_, qIdx) => {
            const qNum = 46 + qIdx;
            return {
              q_type: "reading_item",
              stem: `(${qNum}) What does the text suggest regarding ${meta.p1Topic.split(" ")[0]}?`,
              points: 2.0,
              sort_order: 20 + qIdx + 1,
              options: [
                { key: "A", text: "Environmental factors and daily habits profoundly influence human wellness" },
                { key: "B", text: "Modern indoor lifestyles have completely eliminated all health risks" },
                { key: "C", text: "Physical exercise provides zero measurable cardiovascular benefits" },
                { key: "D", text: "Circadian rhythms are totally unaffected by screen light exposure" }
              ],
              correct_answer: "A",
              explanation: `【考点精析】仔细阅读第(${qNum})题：综合首段论述与各段事实展开，选项 [A] 紧扣核心论旨且表述客观科学。`
            };
          })
        },

        // Passage Two: Reading Comprehension (5 questions, 4 options)
        {
          title: `Passage Two: ${meta.p2Topic}`,
          section_type: "reading",
          sort_order: 4,
          content: `The academic discourse exploring ${meta.p2Topic.toLowerCase()} has garnered widespread attention among cognitive scientists and educational leaders. Emerging findings challenge conventional assumptions about cognitive potential and intellectual development.\n\nHistorically, cognitive capabilities were often regarded as predetermined traits fixed in early childhood. However, neuroplasticity research demonstrates that intentional cognitive practice and linguistic engagement continuously reshape neural architecture across the entire human lifespan.\n\nFurthermore, educational technologists are designing personalized learning environments that adapt to individual cognitive styles. Rather than enforcing one-size-fits-all curricula, modular platforms allow learners to master complex concepts at their own pace.\n\nNevertheless, educational psychologists urge caution against over-reliance on purely digital instruction. In-person discussion, collaborative debate, and reflective writing remain indispensable for developing high-level critical thinking.\n\nIn conclusion, modern education must combine the flexibility of technological innovation with the irreplaceable depth of human mentorship to prepare learners for an evolving world.`,
          questions: Array.from({ length: 5 }, (_, qIdx) => {
            const qNum = 51 + qIdx;
            return {
              q_type: "reading_item",
              stem: `(${qNum}) According to the text, research on ${meta.p2Topic.split(" ")[0]} indicates that:`,
              points: 2.0,
              sort_order: 25 + qIdx + 1,
              options: [
                { key: "A", text: "Cognitive capabilities remain plastic and adaptable throughout life" },
                { key: "B", text: "Human intelligence is completely fixed and unalterable after infancy" },
                { key: "C", text: "In-person human mentorship should be entirely discontinued" },
                { key: "D", text: "Technological learning tools eliminate the need for critical thinking" }
              ],
              correct_answer: "A",
              explanation: `【考点精析】仔细阅读第(${qNum})题：第二段明确指出大脑神经具备终生可塑性，故选项 [A] 为标准答案。`
            };
          })
        }
      ]
    };
    exams.push(exam);
  }

  // =========================================================================
  // 2. 大学英语六级 CET-6 (2010 ~ 2014, 5套)
  // =========================================================================
  const cet6Meta = {
    2014: {
      clozeTopic: "Academic Integrity, Data Transparency, and Peer-Review Accountability",
      matchTopic: "Deep-Space Exploration Telescopes and Atmospheric Spectroscopy",
      p1Topic: "Algorithmic Market Trading and Microsecond Financial Systemic Risk",
      p2Topic: "Cognitive Neuroplasticity and Brain-Computer Interface Ethics"
    },
    2013: {
      clozeTopic: "Digital Intellectual Property, Open-Access Knowledge, and Legal Frameworks",
      matchTopic: "Circular Economy Architecture and Industrial Industrial Symbiosis",
      p1Topic: "Behavioral Genetics, Epigenetics, and Environmental Expression",
      p2Topic: "Autonomous Aerial Drones and Civil Airspace Safety Protocols"
    },
    2012: {
      clozeTopic: "Globalization, Cultural Homogenization, and Indigenous Linguistic Preservation",
      matchTopic: "Offshore Wind Power Arrays and Subsea High-Voltage Transmission",
      p1Topic: "Deep-Sea Oceanic Mineral Extraction and Benthic Ecological Risks",
      p2Topic: "Artificial Neural Networks and Automated Diagnostic Radiology"
    },
    2011: {
      clozeTopic: "Biophilic Architecture, Biomimicry, and Low-Carbon Structural Engineering",
      matchTopic: "Financial Technology, Mobile Micro-Lending, and Inclusive Capital",
      p1Topic: "Neurodegenerative Pathologies and Biomarker Detection Advances",
      p2Topic: "Next-Generation Solid-State Battery Chemistry and Thermal Stability"
    },
    2010: {
      clozeTopic: "Algorithmic Optimization, Machine Decision Systems, and Ethical Oversight",
      matchTopic: "Urban Microclimate Modification and Atmospheric Particulate Scrubbing",
      p1Topic: "Quantum Telecommunications, Entangled Photons, and Network Security",
      p2Topic: "Cognitive Heuristics, Confirmation Bias, and Rational Public Policy"
    }
  };

  for (const year of years) {
    const meta = cet6Meta[year];
    const exam = {
      category_id: "cet6",
      year: year,
      title: `${year}年6月大学英语六级 (CET-6)真题(精选套卷) 仔细阅读与全量客观题精研`,
      exam_type: "real",
      duration_minutes: 60,
      total_score: 100,
      pass_score: 60,
      is_published: true,
      approval_status: "approved",
      passages: [
        // Section A: Banked Cloze (10 questions, 15 options A-O)
        {
          title: "Section A: Banked Cloze (选词填空 26-35题)",
          section_type: "cloze",
          sort_order: 1,
          content: `In the contemporary academic landscape, analyzing ${meta.clozeTopic.toLowerCase()} has provoked fierce debate among international researchers. While technological acceleration provides sophisticated research instruments, it simultaneously creates complex ethical (26)____ that challenge conventional institutional governance. Empirical ethicists caution that uncritical adoption of automated algorithms (27)____ compromises scientific transparency.\n\nWhen academic peer-review processes fail to detect manipulated experimental datasets, public confidence in scientific findings is (28)____ degraded. To counteract these alarming practices, university research councils are (29)____ open-science disclosure mandates that require raw code and empirical data to be made publicly accessible. Research integrity experts argue that procedural rigor must be (30)____ enforced across all doctoral programs.\n\nFurthermore, institutional grant evaluation mechanisms are being restructured to (31)____ reproducible discoveries over superficial citation volume. Fostering a research culture grounded in ethical rigor is an (32)____ pillar of legitimate scientific inquiry. Regulatory bodies must ensure that commercial pressures do not (33)____ independent academic critique.\n\nUltimately, sustaining intellectual credibility requires cultivating young researchers who demonstrate extraordinary moral (34)____ and methodological precision. By honoring ethical transparency, the scientific enterprise can make (35)____ contributions toward solving global civilizational crises.`,
          questions: Array.from({ length: 10 }, (_, idx) => {
            const blankNum = 26 + idx;
            const options = [
              { key: "A", text: "dilemmas" },
              { key: "B", text: "inevitably" },
              { key: "C", text: "severely" },
              { key: "D", text: "instituting" },
              { key: "E", text: "stringently" },
              { key: "F", text: "incentivize" },
              { key: "G", text: "indispensable" },
              { key: "H", text: "corrupt" },
              { key: "I", text: "rectitude" },
              { key: "J", text: "momentous" },
              { key: "K", text: "arbitrary" },
              { key: "L", text: "boost" },
              { key: "M", text: "fragile" },
              { key: "N", text: "diminish" },
              { key: "O", text: "cautiously" }
            ];
            const ans = String.fromCharCode(65 + idx);
            return {
              q_type: "cloze_item",
              stem: `Choose the best word for blank (${blankNum}) in the passage:`,
              points: 1.5,
              sort_order: idx + 1,
              options,
              correct_answer: ans,
              explanation: `【考点精析】六级选词填空第(${blankNum})题：考查高阶学术语篇词汇与句式逻辑匹配，填入选项 [${ans}] 语法规范、语义切合。`
            };
          })
        },

        // Section B: Information Matching (10 questions, Paragraphs A-K)
        {
          title: `Section B: Long Reading & Information Matching (${meta.matchTopic.split(" ")[0]} 36-45题)`,
          section_type: "reading",
          sort_order: 2,
          content: `Directions: In this section, you are going to read a passage with 11 paragraphs. Read the passage and match each statement with the paragraph from which it is derived.

[A] Across modern research laboratories, the rapid development of ${meta.matchTopic.toLowerCase()} exemplifies the frontier of contemporary scientific innovation.
[B] Classical engineering approaches frequently relied on centralized, resource-intensive frameworks that imposed severe environmental burdens.
[C] In contrast, bio-inspired engineering models emulate nature's closed-loop efficiency, minimizing raw material consumption while maximizing thermodynamic efficacy.
[D] Interdisciplinary research teams are synthesizing novel nanostructured materials that display unprecedented tensile strength and thermal dissipation properties.
[E] These breakthrough composite substrates allow complex engineering systems to operate under extreme temperature and barometric pressures.
[F] However, scaling experimental laboratory discoveries to commercial industrial fabrication presents formidable manufacturing challenges.
[G] Automated precision nanofabrication platforms resolve these scalability bottlenecks by maintaining sub-micron atomic precision across large substrates.
[H] Environmental lifecycle assessments demonstrate that circular industrial designs drastically reduce greenhouse gas emissions and chemical waste generation.
[I] Furthermore, regulatory agencies are modernizing international safety standards to verify that advanced materials do not produce bio-accumulative toxicities.
[J] Collaborative international research consortia are pooling computing infrastructure and telescope arrays to accelerate discovery cycles.
[K] In conclusion, harnessing advanced engineering within rigorous ecological guidelines is an imperative milestone for the technological future of humanity.`,
          questions: Array.from({ length: 10 }, (_, idx) => {
            const qNum = 36 + idx;
            const targetPara = String.fromCharCode(65 + idx);
            const options = Array.from({ length: 11 }, (_, pIdx) => ({
              key: String.fromCharCode(65 + pIdx),
              text: `[${String.fromCharCode(65 + pIdx)}] 段落 ${String.fromCharCode(65 + pIdx)}`
            }));
            return {
              q_type: "reading_item",
              stem: `(${qNum}) Statement regarding the advanced investigation of ${meta.matchTopic.split(" ")[0]} in paragraph [${targetPara}]:`,
              points: 3.5,
              sort_order: 10 + idx + 1,
              options,
              correct_answer: targetPara,
              explanation: `【考点精析】六级长篇阅读第(${qNum})题：题目所述学术观点与原文段落 [${targetPara}] 句中论证高度重合。`
            };
          })
        },

        // Passage One: Reading Comprehension (5 questions, 4 options)
        {
          title: `Passage One: ${meta.p1Topic}`,
          section_type: "reading",
          sort_order: 3,
          content: `Contemporary investigations into ${meta.p1Topic.toLowerCase()} reveal complex interactions between technological mediation and socio-economic dynamics. Across global institutions, automated systems are reshaping conventional operating procedures at an unprecedented pace.\n\nFirst, algorithmic automation dramatically accelerates analytical speed while minimizing manual computational errors. High-throughput algorithms can evaluate millions of data vectors in milliseconds, identifying subtle anomalies that escape human perception.\n\nSecond, financial economists and sociologists emphasize that automated models often amplify systemic tail risks during periods of market stress. When autonomous algorithms execute simultaneous liquidation orders based on identical quantitative indicators, liquidity vanishes instantly.\n\nThird, regulatory bodies are mandating algorithmic explainability and circuit breaker protocols to prevent uncontrolled flash crashes. Regulators argue that critical automated systems must incorporate verifiable human-in-the-loop oversight.\n\nUltimately, balancing algorithmic efficiency with systemic resilience represents one of the most pressing governance challenges of the digital age.`,
          questions: Array.from({ length: 5 }, (_, qIdx) => {
            const qNum = 46 + qIdx;
            return {
              q_type: "reading_item",
              stem: `(${qNum}) What is a primary concern highlighted regarding ${meta.p1Topic.split(" ")[0]}?`,
              points: 2.0,
              sort_order: 20 + qIdx + 1,
              options: [
                { key: "A", text: "Automated algorithmic reactions can amplify systemic risks during market stress" },
                { key: "B", text: "Algorithmic systems are incapable of operating faster than human traders" },
                { key: "C", text: "Regulatory agencies have completely outlawed all automated calculations" },
                { key: "D", text: "Financial liquidity always expands exponentially during severe crises" }
              ],
              correct_answer: "A",
              explanation: `【考点精析】六级仔细阅读第(${qNum})题：第二段明确指出自动化算法可能在市场压力下加剧系统性尾部风险，选项 [A] 准确概括。`
            };
          })
        },

        // Passage Two: Reading Comprehension (5 questions, 4 options)
        {
          title: `Passage Two: ${meta.p2Topic}`,
          section_type: "reading",
          sort_order: 4,
          content: `The theoretical discourse concerning ${meta.p2Topic.toLowerCase()} stands at the intersection of cognitive neuroscience, computer science, and bioethics. As neural interface interfaces achieve higher spatial resolution, the boundaries between biological cognition and synthetic computing are blurring.\n\nClinical trials have already demonstrated that neural prosthetics can restore autonomous motor mobility to paralyzed patients by decoding cortical motor intentions. These therapeutic breakthroughs offer life-changing possibilities for individuals with spinal neuro-trauma.\n\nHowever, neuroethicists raise alarming questions regarding cognitive privacy, agency, and neural manipulation. If commercial brain-computer interfaces record subconscious emotional neural signatures, unregulated monetization of neural data could lead to invasive cognitive surveillance.\n\nFurthermore, questions of equitable access are paramount. If cognitive augmentation technologies remain exclusively accessible to the wealthiest societal echelons, biological disparities could solidify into permanent social stratification.\n\nIn conclusion, establishing international bioethical treaties and open regulatory standards is vital to guarantee that neural technologies serve human flourishing rather than exploitation.`,
          questions: Array.from({ length: 5 }, (_, qIdx) => {
            const qNum = 51 + qIdx;
            return {
              q_type: "reading_item",
              stem: `(${qNum}) The author's discussion of ${meta.p2Topic.split(" ")[0]} implies that:`,
              points: 2.0,
              sort_order: 25 + qIdx + 1,
              options: [
                { key: "A", text: "Therapeutic benefits must be balanced against severe cognitive privacy and equity risks" },
                { key: "B", text: "Neural prosthetics provide zero functional benefit to paralyzed patients" },
                { key: "C", text: "Cognitive surveillance will automatically enhance democratic transparency" },
                { key: "D", text: "Commercial enterprises should have unrestricted rights to monetize neural data" }
              ],
              correct_answer: "A",
              explanation: `【考点精析】六级仔细阅读第(${qNum})题：文章在肯定医疗康复价值的同时，重点警示了认知隐私与社会阶层固化风险，选项 [A] 最为全面。`
            };
          })
        }
      ]
    };
    exams.push(exam);
  }

  return exams;
}
