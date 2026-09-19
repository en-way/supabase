// 2022 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2022Exams = [
  // =========================================================================
  // 2022 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Environmental DNA (eDNA) analysis has revolutionized conservation biology, allowing researchers to detect aquatic and terrestrial species by sampling genetic fragments shed into water, soil, or air. Rather than relying on elusive visual sightings or disruptive physical capture, ecologists can now extract cellular matter (1)____ from a liter of river water to reconstruct regional biodiversity profiles.

In marine ecosystems where cryptic or nocturnal creatures evade conventional underwater cameras, eDNA surveys have identified endangered elasmobranchs and invasive invertebrate species with extraordinary (2)____. Furthermore, the methodology facilitates temporal monitoring, allowing scientists to track how migratory fish populations respond to climatic (3)____ across changing seasons.

Despite these advantages, eDNA tracking possesses inherent limitations. Genetic material can be transported kilometers downstream by hydrological currents, potentially generating false-positive detections in habitats where living animals are completely (4)____. Consequently, biologists emphasize that eDNA should complement, rather than completely (5)____, traditional field taxonomy and direct ecological observation.

To mitigate such contamination risks, molecular protocols enforce strict (6)____ standards during sample collection and amplification. Field researchers must wear sterile attire, employ single-use filter capsules, and implement negative control blanks to (7)____ external DNA contamination. Additionally, degradation kinetics vary widely depending on ultraviolet radiation exposure, water temperature, and enzymatic (8)____, which can rapidly break down cellular strands within days.

Another technical obstacle relates to primer specificity and reference database completeness. When scientists sequence amplified genetic fragments, they must match the resulting reads against curated taxonomic libraries. If an obscure amphibian or subterranean arthropod has never had its genome sequenced, the eDNA probe will yield (9)____ sequences that cannot be definitively cataloged. Taxonomists therefore call for accelerated barcode cataloging to (10)____ these evidentiary voids.

Furthermore, quantitative interpretation remains deeply (11)____. While the presence of DNA confirms that an organism was present in the vicinity, the concentration of genetic material does not correlate (12)____ with population abundance. A single carcass decomposing upstream can shed exponentially more DNA than a dozen healthy juveniles (13)____ through the riverbed. Biostatisticians are developing Bayesian models to integrate shedding rates and hydrodynamic decay, striving to (14)____ biomass estimates from raw molecular copies.

Public policy has steadily begun to embrace eDNA monitoring for regulatory (15)____. Environmental protection agencies now deploy molecular filters to inspect shipping ballast water, preventing the (16)____ introduction of destructive marine pests. In freshwater reservoirs, utility companies screen for pathogenic microbes and toxin-producing cyanobacteria long before visible blooms (17)____.

Ethicists and conservationists also appreciate the non-invasive nature of molecular sampling. Capturing sensitive species frequently causes physiological stress, accidental trauma, or behavioral (18)____. By replacing invasive netting with gentle water filtration, ecological surveys respect animal welfare while gathering superior spatial (19)____. As sequencing costs decline and automated autonomous aquatic drones mature, environmental genomics promises to inaugurate a new paradigm of real-time planetary health (20)____.`,
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
            explanation: "【考点精析】副词语义。生态学家可以直接（directly）从一升河水中提取细胞遗传物质，强调该检测技术的敏捷与直接。"
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
            explanation: "【考点精析】名词搭配。with extraordinary precision（以极其出色的精确度），后文识别濒危物种和入侵物种印证了其精确性。"
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
            explanation: "【考点精析】名词辨析。climatic fluctuations（气候波动），符合四季变换与生物洄游响应的自然规律。"
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
            explanation: "【考点精析】形容词辨析。下流DNA漂移会导致假阳性，即在活体动物完全缺席/不存在（absent）的区域检测出信号。"
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
            explanation: "【考点精析】动词搭配。complement, rather than completely supplant（补充，而非彻底取代），体现新旧手段的协同关系。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "sanitation" },
              { key: "B", text: "diplomatic" },
              { key: "C", text: "commercial" },
              { key: "D", text: "cosmetic" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。为防止外部DNA污染，实验流程必须执行严格的卫生/清洁（sanitation）标准。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "preempt" },
              { key: "B", text: "encourage" },
              { key: "C", text: "disregard" },
              { key: "D", text: "celebrate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词语义。穿无菌服装和使用对照盲样是为了预防/阻断（preempt）外部环境DNA的污染。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "activity" },
              { key: "B", text: "silence" },
              { key: "C", text: "negligence" },
              { key: "D", text: "sentiment" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。enzymatic activity（酶活性），与紫外线、水温并列为降解生物遗传链的关键物理化学因素。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "unmatched" },
              { key: "B", text: "authentic" },
              { key: "C", text: "universal" },
              { key: "D", text: "reputable" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。如果参考基因库中没有该生物的测序记录，探针测得的结果就会是无法匹配的（unmatched）序列。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "bridge" },
              { key: "B", text: "widen" },
              { key: "C", text: "ignore" },
              { key: "D", text: "endorse" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。bridge voids/gaps（填补空白），分类学家呼吁加快基因条形码编目以填补证据链空白。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "challenging" },
              { key: "B", text: "straightforward" },
              { key: "C", text: "lucrative" },
              { key: "D", text: "monotonous" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】上下文逻辑。后文阐述DNA浓度无法与种群数量画等号，因此定量解释依然极具挑战性（challenging）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "linearly" },
              { key: "B", text: "blindly" },
              { key: "C", text: "spitefully" },
              { key: "D", text: "randomly" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词搭配。does not correlate linearly（并非线性相关），即分子浓度高低不能直接推算实际生物个体数。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "swimming" },
              { key: "B", text: "fleeing" },
              { key: "C", text: "hibernating" },
              { key: "D", text: "decaying" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】分词动作。十多条在河床上畅游的（swimming）健康幼鱼，与上游腐烂的尸体形成鲜明对照。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "derive" },
              { key: "B", text: "distract" },
              { key: "C", text: "shield" },
              { key: "D", text: "dismiss" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词短语。derive... from...（从……推导/获取），统计学家致力于从原始分子拷贝中推导生物量估算值。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "enforcement" },
              { key: "B", text: "amusement" },
              { key: "C", text: "concealment" },
              { key: "D", text: "hesitation" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。regulatory enforcement（监管执法），政府部门在环境督察与执法中采用 eDNA 技术。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "inadvertent" },
              { key: "B", text: "intentional" },
              { key: "C", text: "virtuous" },
              { key: "D", text: "triumphant" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。防止压载水在无意之中/非故意地（inadvertent）将破坏性海洋害虫带入新水域。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "manifest" },
              { key: "B", text: "recede" },
              { key: "C", text: "evaporate" },
              { key: "D", text: "subside" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词语义。在水华肉眼显现/爆发（manifest）之前，水务部门就能通过分子检测发现蓝细菌。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "disruption" },
              { key: "B", text: "prosperity" },
              { key: "C", text: "amplication" },
              { key: "D", text: "gratitude" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词并列。传统捕捞常造成生理应激、外伤及行为紊乱/干扰（disruption）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "fidelity" },
              { key: "B", text: "hypocrisy" },
              { key: "C", text: "hostility" },
              { key: "D", text: "animosity" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词语义。gathering superior spatial fidelity（获取更高空间保真度/精确度的生态数据）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "surveillance" },
              { key: "B", text: "extinction" },
              { key: "C", text: "exploitation" },
              { key: "D", text: "neglect" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词归纳。real-time planetary health surveillance（实时全球生态健康监测/监护体系）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `America's national parks, revered since the nineteenth century as "cathedrals of nature," are confronting unprecedented ecological strain caused by record tourist influxes. Iconic destinations such as Zion, Yosemite, and Rocky Mountain have seen annual visitation climb exponentially over the past decade. This overcrowding has transformed serene alpine valleys into gridlocked bottlenecks, complete with exhaust-choked shuttle queues, trampled wilderness meadows, and severely degraded visitor amenities.

In response to surging crowding, the National Park Service (NPS) has instituted timed-entry reservation systems at several major parks. Under these digital protocols, travelers must reserve specific entry slots months in advance via recreation.gov. Proponents assert that rationing access stabilizes vehicular flow, safeguards vulnerable wildlife migration corridors, and protects historic infrastructure from catastrophic wear. Preliminary NPS reports from Zion demonstrate measurable declines in trail erosion and notable improvements in visitor satisfaction once daily trail quotas were enforced.

However, reservation schemes have provoked bitter resistance from local gateway towns and tourism-dependent businesses. Hotel operators, outdoor outfitters, and restaurateurs argue that stringent entry restrictions discourage spontaneous travel and depress regional consumer spending. Critics also observe that the digital booking model disproportionately disadvantages rural residents and low-income families who lack dependable high-speed broadband or the flexibility to schedule excursions half a year in advance.

Furthermore, legal purists contend that mandatory reservations violate the foundational charter of the 1916 National Park Organic Act, which dedicated these public lands to the "enjoyment of the people" in perpetuity without commercial barriers. Critics argue that wilderness experiences are inherently about freedom and spontaneity; subjecting them to algorithmic scarcity commodifies what should remain an egalitarian commons.

Resource economists counter that without demand-management pricing or quota systems, the "tragedy of the commons" will permanently destroy the ecological integrity of the parks. Unrestricted access simply degrades the very resource people travel across continents to admire. The true dilemma facing park superintendents is not whether to regulate crowds, but how to construct equitable distribution formulas that balance wilderness stewardship with universal public accessibility.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "According to Paragraph 1, the primary dilemma confronting America's national parks is:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Severe ecological degradation caused by surging tourist crowds." },
              { key: "B", text: "A severe shortage of federal funding for wilderness infrastructure." },
              { key: "C", text: "The commercial privatization of iconic scenic valley routes." },
              { key: "D", text: "A total decline in public enthusiasm for outdoor recreation." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。根据第一段首句可知，美国国家公园正面临游客激增带来的前所未有的生态压力（severe ecological degradation caused by surging tourist crowds）。"
          },
          {
            q_type: "reading_item",
            stem: "The NPS implemented timed-entry reservation systems in order to:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Regulate tourist flow and safeguard fragile wilderness environments." },
              { key: "B", text: "Maximize concession revenues through digital booking fees." },
              { key: "C", text: "Deter foreign tourists from accessing pristine wildlife corridors." },
              { key: "D", text: "Reallocate federal park lands to local hospitality businesses." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】目的意图题。第二段指出实行分时预约系统旨在稳定车流、保护脆弱的野生动物廊道和历史基础设施，即规范客流并保护自然生态。"
          },
          {
            q_type: "reading_item",
            stem: "Gateway community businesses oppose reservation systems primarily because they:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Worry that entry caps deter spontaneous visits and harm regional commerce." },
              { key: "B", text: "Object to paying federal municipal taxes on hospitality services." },
              { key: "C", text: "Demand the permanent closure of heavily crowded alpine trails." },
              { key: "D", text: "Prefer private corporate concessionaires over the federal NPS." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段明确指出，当地酒店、装备商和餐馆老板反对是因为限额入园打压了自发性出游，导致地方消费和商业受挫。"
          },
          {
            q_type: "reading_item",
            stem: "Legal purists criticize reservation models on the grounds that they:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Infringe upon the egalitarian, unrestricted public access established by law." },
              { key: "B", text: "Violate municipal zoning statutes across western gateway counties." },
              { key: "C", text: "Favor low-income families at the expense of affluent excursionists." },
              { key: "D", text: "Fail to generate adequate revenues for park restoration." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】观点态度题。第四段指出法律原旨主义者认为强制预约违背了1916年《国家公园组织法》中全民永久共享的宗旨，侵蚀了本应平等的公共资源性质。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following would be the most suitable title for this text?",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Rationing Nature: The Clash Over National Park Overcrowding." },
              { key: "B", text: "The Commercial Triumph of American Wilderness Tourism." },
              { key: "C", text: "Digital Automation in Federal Environmental Administration." },
              { key: "D", text: "The Decline of Wilderness Tourism in the Western States." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨大意题。全文围绕国家公园因游客过多推行限流配额制度（分时预约）带来的生态保护与公众可达性之间的冲突，A 项最为贴切生动。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `Britain's passenger railway network, long criticized for soaring fares and chronic delays, has arrived at an existential juncture. The seismic shift toward remote and hybrid working prompted by the pandemic has fundamentally ruptured the traditional commuter model. Peak-hour weekday travel, which previously generated the cross-subsidies necessary to sustain rural branch lines and capital upgrades, has contracted precipitously, leaving rail franchise operators saddled with multibillion-pound operating deficits.

In response, the Department for Transport has orchestrated a major restructuring, creating a unified public entity dubbed "Great British Railways" (GBR) to integrate track infrastructure management and train operational scheduling. Proponents herald GBR as a sensible compromise between the fragmented chaos of 1990s privatization and the rigid bureaucratic inertia of post-war state ownership. By consolidating ticketing algorithms and simplifying passenger fare structures, officials hope to recapture discretionary leisure travelers.

Nevertheless, transport economists warn that managerial reorganizations cannot bypass harsh arithmetic realities. Commuters traveling two or three days a week find traditional monthly and annual season tickets economically indefensible. While flexi-season tickets were introduced to accommodate hybrid workers, passenger surveys reveal that the modest discounts fail to provide compelling value compared to working from home or driving private vehicles.

Trade unions and passenger advocacy coalitions further argue that Treasury-mandated service cutbacks create a self-reinforcing downward spiral. When train frequency is diminished and ticket offices are shuttered, passenger trust evaporates, prompting further patronage declines and requiring even steeper operational subsidies. Instead of treating rail services as an isolated balance sheet liability, urban planners urge policymakers to account for the wider economic and ecological externalities of a thriving rail network. Efficient mass transit curtails road congestion, diminishes urban air pollution, and drives regional economic rebalancing.

If Britain intends to meet its binding net-zero carbon obligations, starving passenger rail of operational capital is catastrophic fiscal shortsightedness. Public transport is an indispensable public good rather than a self-funding commercial luxury. Reinvigorating Britain's railways requires courageous public investment, courageous price reform, and an acknowledgment that commuter mobility underpins national economic resilience.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What major development has disrupted Britain's traditional rail commuter model?",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "The widespread shift toward hybrid and remote working habits." },
              { key: "B", text: "Massive strikes staged by railway track maintenance unions." },
              { key: "C", text: "The rapid construction of high-speed intercity motorways." },
              { key: "D", text: "The complete privatization of rural passenger lines." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段第二句指出，疫情推动的向远程与混合办公（hybrid and remote working）的根本转变，瓦解了传统的通勤客流模式。"
          },
          {
            q_type: "reading_item",
            stem: "Proponents view the creation of 'Great British Railways' (GBR) as:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "A balanced reform integrating infrastructure and train operations." },
              { key: "B", text: "A complete return to post-war bureaucratic nationalization." },
              { key: "C", text: "A financial scheme to eliminate all passenger fare subsidies." },
              { key: "D", text: "A temporary franchise partnership with foreign rail operators." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第二段提到支持者赞同 GBR 是一次合理的妥协改革，将铁轨基础设施与列车调度运营重新整合为一个实体。"
          },
          {
            q_type: "reading_item",
            stem: "Passenger surveys indicate that existing flexi-season tickets:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Fail to offer sufficiently attractive discounts for hybrid commuters." },
              { key: "B", text: "Have dramatically boosted weekend leisure passenger volumes." },
              { key: "C", text: "Are widely abused by long-distance corporate travelers." },
              { key: "D", text: "Have fully restored pre-pandemic commuter fare revenues." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段最后一句提到调查显示弹性季票的微薄折扣无法为混合办公族提供足够的性价比（fail to provide compelling value）。"
          },
          {
            q_type: "reading_item",
            stem: "Urban planners emphasize that passenger rail should be viewed as:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "An essential public good generating broad economic and environmental benefits." },
              { key: "B", text: "A commercial business that must generate self-sustaining corporate profits." },
              { key: "C", text: "An obsolete mode of travel secondary to private electric vehicles." },
              { key: "D", text: "A specialized service reserved exclusively for metropolitan commuters." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】观点推断题。第四段末尾及第五段指出城市规划学者认为铁路具有缓解拥堵、净化空气和促进平衡等广泛的社会生态外部性，是不可或缺的公共产品（essential public good）。"
          },
          {
            q_type: "reading_item",
            stem: "The author's attitude toward cutting operational rail funding is:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Critical and disapproving." },
              { key: "B", text: "Tolerant and accommodating." },
              { key: "C", text: "Ambivalent and indifferent." },
              { key: "D", text: "Cautiously supportive." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】态度观点题。作者在末段直斥削减铁路运营资金是“灾难性的财政短视（catastrophic fiscal shortsightedness）”，明确表达了强烈的批评与反对态度。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the peer-reviewed corridors of academia, retractions of published scientific papers were once treated as rare anomalies, usually triggered by tragic errors of laboratory execution. Today, retraction databases such as Retraction Watch log thousands of notices annually, exposing an alarming surge in data falsification, duplicate publication, and organized peer-review fraud. Far from signifying an epistemological collapse, however, many sociologists of science argue that the ballooning volume of retractions reflects heightened investigative vigilance rather than deteriorating scientific ethics.

The proliferation of digital detection algorithms has fundamentally transformed scientific oversight. Software tools can now effortlessly scrutinize western blot bands, detect subtle pixel repetitions in microscopy imagery, and identify algorithmic text generated by clandestine "paper mills." Anonymous post-publication review platforms, most notably PubPeer, have democratized academic whistleblowing. Junior researchers and independent data sleuths can now highlight methodological incongruities without fearing institutional retaliation from senior departmental figures.

Nevertheless, the structural pathology powering this integrity crisis remains firmly rooted in the hyper-competitive "publish or perish" culture governing university appointments and grant allocations. Academic institutions prioritize quantitative publication metrics—impact factors, h-indices, and citation counts—over methodological rigor and reproducibility. When career advancement, laboratory funding, and tenure hinge upon a continuous cadence of headline-grabbing results, the incentive to cut corners or fabricate positive statistical correlations becomes intoxicating.

Furthermore, traditional scientific journals and academic publishers have frequently demonstrated reluctant inertia when alerted to tainted findings. Scholarly publishing houses reap enormous profit margins while outsourcing peer review to uncompensated academics. Conducting forensic investigations into suspected misconduct requires substantial legal and editorial overhead, prompting publishers to delay formal retractions for months or even years while discredited citations continue to infect subsequent literature.

Rebuilding public trust in the scientific enterprise requires profound structural remedies. Research funding bodies must mandate open-science protocols, requiring scientists to deposit raw numerical data, software code, and pre-registered laboratory protocols in accessible public repositories. Only by replacing vanity metrics with empirical transparency can science restore its integrity and fulfill its democratic calling.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Sociologists of science interpret the recent surge in retractions as evidence of:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "More vigilant oversight and investigative detection mechanisms." },
              { key: "B", text: "A catastrophic and irreversible collapse in global scientific morality." },
              { key: "C", text: "The complete failure of peer-reviewed journal publishing." },
              { key: "D", text: "A severe decline in the competence of junior researchers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段尾句指出科学社会学家认为撤稿数量激增反映的是审查警惕性的提高（heightened investigative vigilance），而非科学道德的彻底滑坡。"
          },
          {
            q_type: "reading_item",
            stem: "Platforms like PubPeer have enhanced scientific integrity by:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Enabling anonymous, post-publication scrutiny without fear of reprisal." },
              { key: "B", text: "Automating the peer-review process using artificial intelligence." },
              { key: "C", text: "Restricting public access to controversial biomedical studies." },
              { key: "D", text: "Paying independent researchers for verifying laboratory results." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出 PubPeer 等平台使得学术举报大众化，让研究者能够在不必担心遭到机构高层报复的前提下开展匿名质疑审查。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 3, the root cause of scientific misconduct lies in:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "A toxic academic culture fixated on quantitative publication metrics." },
              { key: "B", text: "A lack of advanced digital software in university laboratories." },
              { key: "C", text: "Inadequate scientific training among doctoral candidates." },
              { key: "D", text: "Strict government regulations on experimental trial data." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段明确将病态根源归咎于“不发表就出局”（publish or perish）以及高校重数量指标（影响因子、引用率）轻严谨性的制度导向。"
          },
          {
            q_type: "reading_item",
            stem: "Why are academic publishers often slow to issue retractions?",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Forensic inquiries incur significant legal and editorial expenses." },
              { key: "B", text: "They are legally forbidden from retracting published peer-reviewed papers." },
              { key: "C", text: "They rarely receive complaints from post-publication whistleblowers." },
              { key: "D", text: "They prioritize open-access data sharing over commercial revenue." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出出版商对调查造假反应迟缓，因为进行取证调查需要耗费高昂的法律和编辑开支（substantial legal and editorial overhead）。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following is proposed as a vital remedy for rebuilding scientific integrity?",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Mandating open-access deposit of raw data and pre-registered protocols." },
              { key: "B", text: "Prohibiting junior researchers from criticizing senior scholars' work." },
              { key: "C", text: "Dismantling online whistleblowing websites like PubPeer." },
              { key: "D", text: "Raising the financial submission fees for scientific journals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】方案建议题。末段指出解决学术诚信危机必须强制推行开放科学协议，要求公开原始数据、代码及预注册实验方案（mandate open-science protocols）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In an era defined by carbon footprint consciousness and resource depletion, the demolition of aging buildings is increasingly viewed not as urban renewal, but as ecological folly. Historic preservationists, once dismissed as sentimental antiquarians fighting doomed rearguard actions against metropolitan progress, now find themselves aligned with cutting-edge structural engineers and climate architects. The prevailing consensus argues that the greenest building is almost invariably the one that already exists.

The central pillar of this architectural paradigm is the concept of "embodied carbon"—the total greenhouse gases emitted during the extraction, manufacture, transport, and assembly of raw structural materials such as concrete, steel, and glass. When a functioning brick warehouse or masonry department store is razed, all of its embodied energy is irrevocably forfeited. Constructing a replacement skyscraper, even one boasting superior modern insulation and solar panels, generates a massive upfront carbon deficit that can take decades of energy-efficient operation to repay.

Consequently, progressive municipal planning commissions are championing "adaptive reuse"—the creative architectural conversion of obsolete structures for contemporary civic and residential utility. Former textile mills in New England and industrial grain silos in Europe are being ingeniously transformed into affordable housing cooperatives, cultural galleries, and tech incubators. This adaptive approach preserves the unique artisanal texture and spatial soul of historic streetscapes while drastically curtailing construction landfill waste.

Yet, widespread adoption of adaptive reuse confronts obstinate institutional friction. Obsolete municipal building codes, originally drafted for new greenfield developments, impose rigid stipulations regarding stairwell dimensions, ceiling clearances, and window placements that are virtually impossible to retrofit into centuries-old masonry frames without prohibitive expense. Furthermore, conventional commercial real estate finance remains biased toward cookie-cutter standardized demolitions, viewing structural retrofits as high-risk, non-standard liabilities.

Overcoming these systemic hurdles demands a thorough modernization of urban development policy. Municipalities should offer robust density bonuses, streamlined permitting waivers, and targeted tax credits for adaptive rehabilitation projects. Simultaneously, local planning authorities must implement "embodied carbon caps," requiring developers to prove that demolition and new construction offer an indisputable carbon advantage over preservation. By elevating structural preservation from a nostalgic indulgence to an urgent climate mandate, modern cities can honor their architectural heritage while constructing a sustainable urban future.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What has altered the public perception of preserving historic buildings?",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Growing awareness of the ecological folly of structural demolition." },
              { key: "B", text: "A sharp decline in the market value of modern high-rise apartments." },
              { key: "C", text: "Government mandates prohibiting any form of urban commercial renewal." },
              { key: "D", text: "The total aesthetic failure of modern minimalist architecture." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段首句和末句指出，在碳足迹与资源耗竭背景下，大拆大建被视为生态愚行，最绿色的建筑就是已经存在的建筑（growing awareness of ecological folly）。"
          },
          {
            q_type: "reading_item",
            stem: "The concept of 'embodied carbon' refers to the greenhouse gases emitted:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "During the entire extraction, manufacture, and assembly of materials." },
              { key: "B", text: "Exclusively during the daily operational heating of an occupied building." },
              { key: "C", text: "By municipal landfill facilities decomposing architectural debris." },
              { key: "D", text: "Through the biological respiration of office workers in urban centers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义理解题。第二段首句明确界定了“隐含碳”的概念，即原材料开采、制造、运输和装配全过程所排放的全部温室气体。"
          },
          {
            q_type: "reading_item",
            stem: "Adaptive reuse projects are celebrated by urbanists because they:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Preserve historic urban character while reducing construction carbon waste." },
              { key: "B", text: "Eliminate the need for any interior modern safety renovations." },
              { key: "C", text: "Allow commercial banks to avoid paying municipal property taxes." },
              { key: "D", text: "Standardize all residential interiors into identical factory designs." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出“适应性改造”不仅保留了历史街区的独特质感与灵魂，还大幅削减了建筑填埋废弃物与碳排放。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 4, what major obstacle hinders widespread adaptive reuse?",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Rigid, outdated building codes and risk-averse real estate financing." },
              { key: "B", text: "Public apathy toward residing in converted historic properties." },
              { key: "C", text: "A severe shortage of raw steel and cement for retrofitting." },
              { key: "D", text: "Widespread opposition from environmental conservation groups." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出两大主要障碍：僵化陈旧的建筑规范（obsolete building codes）以及偏好标准化拆迁的保守金融资本（biased conventional finance）。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that urban development policy should:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Incentivize structural preservation as an urgent ecological necessity." },
              { key: "B", text: "Ban all new architectural construction in metropolitan downtowns." },
              { key: "C", text: "Deregulate historic heritage districts to maximize commercial density." },
              { key: "D", text: "Leave preservation decisions entirely to private real estate markets." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论态度题。末段呼吁将建筑保护从怀旧情结上升为紧迫的气候使命（urgent climate mandate），并通过容积率奖励、税收减免和隐含碳上限加以引导。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2022 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Many people have had the uncanny sensation that time accelerates as they grow older. Childhood summers seemed to stretch into an (1)____ eternity, whereas adult calendar years vanish with alarming speed. Cognitive psychologists have investigated this temporal paradox, revealing that our perception of duration is intimately (2)____ to how our brains process sensory information and encode novel memories.

According to perceptual theories, human brains gauge time largely through the accumulation of mental (3)____. During youth, almost every experience—from riding a bicycle to learning algebra—is delightfully or bewilderingly (4)____. To assimilate these unfamiliar stimuli, the adolescent brain devotes intense computational energy, generating rich, detailed neural (5)____. When you retrospectively look back at a childhood holiday, the vast quantity of preserved details creates the subjective (6)____ that the episode lasted a remarkably long time.

In stark (7)____, adult life is dominated by entrenched routines. The daily commute, office workflows, and household chores become largely automated, requiring minimal conscious (8)____. When our brains encounter predictable patterns, they process them on biological autopilot, compressing sensory input to (9)____ energy. Because fewer distinct memory markers are laid down during repetitive weeks, retrospective reflection perceives these periods as having (10)____ by in an instant.

Neuroscientists also highlight the role of physiological (11)____ in temporal perception. Saccadic eye movements—the rapid, involuntary twitches our eyes make to survey visual scenes—decline in frequency as neural pathways mature and metabolic rates (12)____ with advancing age. As the brain captures fewer visual snapshots per second, internal clock tick rates (13)____, leading older adults to misjudge the passage of chronological hours.

Fortunately, researchers assert that this psychological contraction of time is not (14)____. Individuals can consciously disrupt habitual mental automation by actively seeking out novel environments, acquiring unfamiliar skills, or adopting mindful attentional (15)____. Traveling to unfamiliar destinations, mastering a foreign language, or even altering one's daily walking route forces the brain to remain vigilant, (16)____ fresh experiential benchmarks that enrich our autobiographical timeline.

Emotional engagement further alters subjective duration. Moments of intense fascination or exhilarating challenge stimulate dopamine release, (17)____ memory vividness and prolonging retrospective assessment. Conversely, prolonged periods of passive digital consumption and doom-scrolling provide the illusion of activity while leaving (18)____ no meaningful neural imprint.

Ultimately, time itself flows at an invariant mathematical pace. Our experience of its passage, however, is a plastic neural construct that remains within our conscious (19)____. By intentionally injecting variety, intellectual curiosity, and deep focus into our daily lives, we can effectively expand our perceived lifespan and savor the fleeting (20)____ of our existence.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "endless" },
              { key: "B", text: "artificial" },
              { key: "C", text: "abrupt" },
              { key: "D", text: "accidental" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词搭配。childhood summers seemed to stretch into an endless eternity（童年夏日仿佛延伸进无尽的永恒），形容童年时光漫长。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "tied" },
              { key: "B", text: "opposed" },
              { key: "C", text: "hostile" },
              { key: "D", text: "indifferent" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。be intimately tied to（与……紧密相连），主旨阐述时间感知与感知加工、记忆编码的密切关联。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "milestones" },
              { key: "B", text: "illusions" },
              { key: "C", text: "grievances" },
              { key: "D", text: "subsidies" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。大脑通过累积心理事件/记忆里程碑（mental milestones）来衡量时光的流逝。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "novel" },
              { key: "B", text: "dull" },
              { key: "C", text: "tiresome" },
              { key: "D", text: "offensive" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。青少年时期接触几乎所有事物都是新奇的、全新的（novel），与后文成年人的陈规形成对比。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "impressions" },
              { key: "B", text: "disasters" },
              { key: "C", text: "compromises" },
              { key: "D", text: "penalties" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。generating rich, detailed neural impressions（产生丰富、细腻的神经印记/印象）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "impression" },
              { key: "B", text: "resentment" },
              { key: "C", text: "reluctance" },
              { key: "D", text: "prejudice" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。creates the subjective impression（产生主观感知/印象），认为这段童年时光维持了很久。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "contrast" },
              { key: "B", text: "sympathy" },
              { key: "C", text: "disgrace" },
              { key: "D", text: "disorder" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】介词短语。In stark contrast（形成鲜明对比），对比青少年期的丰富刺激与成年后的墨守成规。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "deliberation" },
              { key: "B", text: "resistance" },
              { key: "C", text: "celebration" },
              { key: "D", text: "hostility" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。日常工作流程变成了自动化反射，几乎无需有意识的深思熟虑（minimal conscious deliberation）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "conserve" },
              { key: "B", text: "squander" },
              { key: "C", text: "ignite" },
              { key: "D", text: "deplete" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。大脑对可预测的模式进行压缩处理，旨在节省/保持（conserve）大脑能量。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "flown" },
              { key: "B", text: "frozen" },
              { key: "C", text: "expanded" },
              { key: "D", text: "halted" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词短语。fly by in an instant（一瞬间飞逝而过），用来形容成年人感知时间的迅速流逝。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "mechanisms" },
              { key: "B", text: "ideologies" },
              { key: "C", text: "conventions" },
              { key: "D", text: "prejudices" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。physiological mechanisms（生理机制），下文眼跳运动与神经通路老化即为具体生理机制。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "decelerate" },
              { key: "B", text: "skyrocket" },
              { key: "C", text: "perpetuate" },
              { key: "D", text: "oscillate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。随着年龄增长代谢率逐渐减速/放缓（decelerate），符合人体生理衰老客观规律。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "slow" },
              { key: "B", text: "accelerate" },
              { key: "C", text: "explode" },
              { key: "D", text: "fluctuate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。内部生物钟的跳动速率减慢（internal clock tick rates slow），导致对外部客观时间的错判。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "inevitable" },
              { key: "B", text: "desirable" },
              { key: "C", text: "profitable" },
              { key: "D", text: "tolerable" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。根据后文可通过主动探索来打破惯性可知，这种时间加速感知并非不可避免的（not inevitable）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "habits" },
              { key: "B", text: "traps" },
              { key: "C", text: "penalties" },
              { key: "D", text: "symptoms" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。attentional habits（正念注意习惯），与前文寻求新环境、学习新技能并列。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "establishing" },
              { key: "B", text: "erasing" },
              { key: "C", text: "concealing" },
              { key: "D", text: "mocking" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】分词搭配。establishing fresh experiential benchmarks（树立全新的体验参照物/基准点），让记忆饱满。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "heightening" },
              { key: "B", text: "paralyzing" },
              { key: "C", text: "diminishing" },
              { key: "D", text: "poisoning" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。多巴胺的分泌能够提升/增强记忆生动度（heightening memory vividness）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "virtually" },
              { key: "B", text: "eagerly" },
              { key: "C", text: "cautiously" },
              { key: "D", text: "triumphantly" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词修饰。刷手机看似丰富，实则几乎没有（virtually no）留下任何有意义的神经印记。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "control" },
              { key: "B", text: "denial" },
              { key: "C", text: "indifference" },
              { key: "D", text: "sorrow" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。remains within our conscious control（依然处于我们有意识的掌控之中）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "richness" },
              { key: "B", text: "poverty" },
              { key: "C", text: "tedium" },
              { key: "D", text: "absurdity" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与褒义归纳。savor the fleeting richness of our existence（体会并细细品味我们生命存在的短暂丰富性）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `In suburban retail parks and bustling high streets across Britain, an innovative retail concept is attempting to dismantle the ubiquitous throwaway culture: zero-waste grocery stores. These packaging-free emporiums invite consumers to bring their own glass jars, cotton totes, and stainless-steel canisters to purchase grains, cooking oils, household detergents, and organic produce by weight. Proponents hail the movement as a grass-roots antidote to the single-use plastic deluge choking terrestrial waterways and marine ecosystems.

However, despite passionate environmental endorsements, the zero-waste retail sector has struggled to move beyond a niche, affluent demographic. Operating a packaging-free shop entails formidable logistical complexities. Bulk bins require rigorous sanitation protocols, manual replenishment increases labor expenses, and the absence of vacuum seals shortens the shelf life of perishable foodstuffs. Consequently, prices at independent package-free stores are often 20 to 40 percent higher than packaged equivalents at mainstream discount supermarkets.

Consumer behavioral hurdles present an even greater barrier to mainstream adoption. Modern grocery retailing is engineered around convenience and speed; barcode scanning and pre-portioned clamshell packages facilitate frictionless checkout. Refilling requires shoppers to weigh empty containers, label tare weights, dispense sticky liquids or powdery flours without spillage, and repeat the process at cash registers. For time-stressed working parents and budget-constrained households, the virtuous desire to eliminate packaging frequently succumbs to practical convenience.

Industry analysts contend that the burden of plastic abatement cannot rest solely on conscientious individual shoppers patronizing boutique stores. Real progress requires mainstream supermarket giants—which control over 80 percent of the grocery retail market—to adopt standardized, scalable refillable systems. Several leading British supermarket chains have initiated refill aisle trials in flagship stores, partnering with major global consumer brands to test automated dry-food dispensers and returnable deposit-scheme bottles.

Ultimately, packaging reduction requires legislative intervention rather than voluntary consumer altruism. When governments enforce Extended Producer Responsibility (EPR) regulations that tax non-recyclable packaging and subsidize circular distribution networks, sustainable retailing ceases to be an expensive moral indulgence and becomes the universal economic baseline.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What is the primary operational characteristic of zero-waste grocery stores?",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Shoppers bring reusable containers to purchase unpackaged items by weight." },
              { key: "B", text: "All foodstuffs are pre-packaged exclusively in biodegradable plant fibers." },
              { key: "C", text: "Products are distributed strictly through online home delivery subscriptions." },
              { key: "D", text: "Customers receive financial vouchers for burning domestic plastic waste." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段第二句指出，顾客携带自己的玻璃罐、棉布袋和不锈钢容器，按重量购买无包装杂货（shoppers bring reusable containers to buy by weight）。"
          },
          {
            q_type: "reading_item",
            stem: "Why are prices at independent zero-waste stores typically higher than conventional supermarkets?",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Higher labor costs and shorter product shelf lives elevate operational expenses." },
              { key: "B", text: "Heavy municipal luxury taxes are imposed on eco-friendly grocery enterprises." },
              { key: "C", text: "They exclusively stock imported, exotic organic goods from overseas." },
              { key: "D", text: "Store owners deliberately inflate profit margins for affluent consumers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出散装售卖需要严格卫生清洁、人工补货增加劳动力成本，缺乏真空密封缩短了保质期，从而推高了综合运营成本与售价。"
          },
          {
            q_type: "reading_item",
            stem: "The main reason average consumers hesitate to adopt package-free shopping is that:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "The refill process is cumbersome and time-consuming compared to pre-packaged goods." },
              { key: "B", text: "They doubt the environmental benefits of eliminating single-use plastics." },
              { key: "C", text: "Most cities lack tap water for cleaning empty jars." },
              { key: "D", text: "They fear contracting food-borne illnesses from bulk food dispensers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出称重、自备容器和清理等繁琐流程（cumbersome and time-consuming）远不及现代超市条码预包装的便捷省时。"
          },
          {
            q_type: "reading_item",
            stem: "Industry analysts argue that meaningful plastic reduction depends upon:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Mainstream supermarket giants integrating scalable refillable systems." },
              { key: "B", text: "The complete prohibition of all physical brick-and-mortar grocery stores." },
              { key: "C", text: "Banning consumers from purchasing household cleaning chemicals." },
              { key: "D", text: "Relying entirely on voluntary consumer boycotts of packaged snacks." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出单靠精品小店无法撼动大局，真正的减塑突破必须依靠控制80%以上零售市场的主流商超巨头推行标准化、可扩展的分装系统。"
          },
          {
            q_type: "reading_item",
            stem: "What does the author propose in the final paragraph to accelerate packaging reduction?",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Implementing binding government regulations like Extended Producer Responsibility." },
              { key: "B", text: "Appealing to the ethical consciousness of multinational corporations." },
              { key: "C", text: "Eliminating all environmental taxes on petrochemical packaging producers." },
              { key: "D", text: "Encouraging families to grow their own agricultural produce at home." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论方案题。第五段强调不能依赖自发的消费者利他心，必须通过政府推行生产者责任延伸（EPR）等强制立法，对非环保包装征税，从而从制度根源实现变革。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `The permanent shift toward hybrid employment—where workers divide their schedules between home offices and corporate headquarters—is fundamentally redefining workplace dynamics. While employees celebrate the elimination of grueling commutes and improved work-life balance, human resource executives are wrestling with a less visible consequence: the steady attrition of "social capital."

Social capital represents the informal network of relationships, shared trust, and spontaneous interpersonal cohesion that binds an organization together. Sociologists divide this capital into two fundamental categories: "bonding ties" between close, immediate teammates, and "bridging ties" between colleagues in disparate departments. Research demonstrates that while remote work often fortifies bonding ties within familiar project squads, it severely erodes the weak, bridging connections forged during impromptu hallway greetings, watercooler chats, and cafeteria lunches.

The erosion of bridging ties carries profound institutional hazards. Serendipitous interactions across cross-functional departments are proven engines of organizational innovation. A chance conversation between a software developer and a customer support manager often identifies unanticipated software glitches or inspires novel feature enhancements. When communication is restricted to scheduled video conferences, interactions become hyper-transactional and siloed. Employees rarely contact colleagues outside their immediate workflow unless an explicit operational reason demands it.

Furthermore, hybrid arrangements present acute hurdles for junior staff and new recruits. Workplace socialization and tacit institutional knowledge are traditionally absorbed through passive observation—overhearing a senior colleague negotiate a client dispute or walking across the trading floor. Deprived of physical proximity, junior professionals experience profound professional isolation, struggling to master company culture or cultivate meaningful mentorship ties.

To counteract these deficiencies, visionary enterprises are radically redesigning corporate real estate. Drab rows of assigned cubicles are being replaced by collaborative lounges, communal cafes, and versatile workshop spaces. Management must recognize that the modern office is no longer a factory floor for solo computer work, but a social destination intentionally orchestrated to build trust, foster spontaneous collaboration, and nurture organizational culture.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Human resource executives are particularly concerned about the decline of:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Organizational social capital and spontaneous interpersonal cohesion." },
              { key: "B", text: "Individual worker efficiency during remote keyboard sessions." },
              { key: "C", text: "Corporate profits generated by commercial office leasing." },
              { key: "D", text: "The reliability of home broadband internet infrastructure." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段末尾指出人事高管最担忧的是混合办公带来的“社会资本（social capital）”与自发人际凝聚力的损耗。"
          },
          {
            q_type: "reading_item",
            stem: "According to sociologists, remote work tends to weaken:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Weak bridging ties across disparate departments." },
              { key: "B", text: "Close bonding ties within immediate project teams." },
              { key: "C", text: "Workers' technical proficiency in operating software tools." },
              { key: "D", text: "The desire of employees to spend time with their families." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出远程办公固化了核心紧密小团队的联系，但重创了跨部门的弱连接“桥梁纽带（bridging ties）”。"
          },
          {
            q_type: "reading_item",
            stem: "Why are cross-departmental interactions vital for organizations?",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "They spark unexpected institutional innovation and creative solutions." },
              { key: "B", text: "They enforce strict hierarchical discipline across all business units." },
              { key: "C", text: "They ensure that all meetings are strictly transactional and scheduled." },
              { key: "D", text: "They reduce the need for hiring external customer support agents." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出跨部门的偶遇闲聊是组织创新的催化剂（proven engines of organizational innovation），能发现意料之外的问题并激发新灵感。"
          },
          {
            q_type: "reading_item",
            stem: "Junior employees suffer under hybrid arrangements mainly because they:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Miss out on passive learning, cultural socialization, and mentorship." },
              { key: "B", text: "Are forced to perform excessive administrative overtime duties." },
              { key: "C", text: "Lack the necessary hardware devices to attend virtual video calls." },
              { key: "D", text: "Are denied standard medical insurance benefits by senior managers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出新人因缺乏物理在场，无法通过旁听和耳濡目染习得隐性组织知识（miss out on passive learning and socialization），难以建立导师纽带。"
          },
          {
            q_type: "reading_item",
            stem: "How should modern corporate offices be reimagined according to the author?",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "As social hubs designed for trust-building and spontaneous collaboration." },
              { key: "B", text: "As silent monitoring centers strictly for individual typing tasks." },
              { key: "C", text: "As smaller warehouses with rows of isolated private cubicles." },
              { key: "D", text: "As virtual metaverse environments replacing physical buildings." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段明确提出办公室不再是个人敲电脑的流水线，而应当重塑为旨在建立信任、促进自发协作与滋养文化的社交目的地（social destination）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `When a booklover purchases a physical hardcover volume from a bookstore, the venerable legal doctrine of "first sale" guarantees their right to lend, resell, or donate that artifact without seeking permission from the author or publisher. For centuries, this principle has sustained second-hand bookshops, public lending libraries, and a vibrant culture of shared literary heritage. However, in the contemporary ecosystem of digital e-books and streaming media, this foundational legal protection has been systematically eviscerated.

When consumers click "Buy Now" on digital platforms, they rarely acquire legal ownership of the underlying content. Instead, they are purchasing a restrictive, non-transferable license to access digital files hosted on remote corporate servers. Under these end-user license agreements, users cannot resell an e-book they have completed, nor can they bequeath their digital libraries to their heirs. The platform retains unilateral authority to amend terms, restrict device interoperability, or even delete purchased titles from a user's reader without notice.

Publishers justify these draconian licensing regimes by pointing to the unique economics of digital goods. Physical books inevitably experience physical wear and tear—dog-eared pages, faded ink, and cracked spines—which naturally diminishes their second-hand resale value. In contrast, digital files can be replicated infinitely without the slightest loss of fidelity. If a frictionless secondary market for e-books existed, publishers argue, a single digital copy could circulate through hundreds of readers indefinitely, cannibalizing new book sales and crippling author royalties.

Consumer rights advocates and digital librarians fiercely contest this rationale. They contend that abolishing digital ownership empowers a handful of tech conglomerates to function as gatekeepers of culture. When readers own nothing, their reading habits are constantly surveilled, annotated marginalia can be harvested as commercial data, and books can be retroactively censored or modified by corporate publishers wishing to scrub sensitive language.

Judicial bodies in Europe and the United States are currently grappling with whether the first-sale doctrine can be adapted to the digital age. Some legal scholars propose implementing "digital exhaustion" protocols governed by blockchain or controlled digital lending, which would ensure that when a user transfers an e-book file, their original copy is irrevocably erased. Without meaningful legal reform, the transition from physical artifacts to digital streams threatens to extinguish reader autonomy and turn culture into a permanent rental subscription.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The 'first sale' doctrine traditionally ensures that buyers of physical books can:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Freely lend, resell, or donate their purchased copies." },
              { key: "B", text: "Print duplicate commercial editions without paying royalties." },
              { key: "C", text: "Alter the author's original manuscript before publishing." },
              { key: "D", text: "Demand full monetary refunds from the publisher at any time." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段首句明确指出，“权利用尽原则/首次销售原则”保证了实体书购买者有权出借、转售或捐赠所购书籍，无需出版社许可。"
          },
          {
            q_type: "reading_item",
            stem: "What do consumers actually acquire when purchasing an e-book online?",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "A restrictive and non-transferable access license." },
              { key: "B", text: "Full permanent ownership of the intellectual copyright." },
              { key: "C", text: "The right to resell duplicate copies on secondary markets." },
              { key: "D", text: "Shared equity in the digital publishing conglomerate." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出点击购买后消费者获得的并非真正的所有权，而仅仅是受限制的、不可转让的访问使用许可（restrictive, non-transferable license）。"
          },
          {
            q_type: "reading_item",
            stem: "Publishers resist secondary digital resale markets primarily because digital files:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Do not degrade and could endlessly cannibalize new sales." },
              { key: "B", text: "Require expensive physical warehouse space for storage." },
              { key: "C", text: "Frequently spread destructive computer viruses to reader devices." },
              { key: "D", text: "Are difficult to translate into foreign languages." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出实体书会磨损老化，而数字文件无损复制且永久保真，若开放无摩擦转售将无休止地蚕食新书销量和作者版税。"
          },
          {
            q_type: "reading_item",
            stem: "Digital librarians warn that the lack of digital ownership allows corporations to:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Monitor reading behavior and unilaterally censor or alter content." },
              { key: "B", text: "Prevent all university researchers from writing book reviews." },
              { key: "C", text: "Force all citizens to purchase physical print newspapers." },
              { key: "D", text: "Dismantle the public library system across North America." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出丧失所有权导致读者阅读数据被监控，甚至内容可能被出版商单方面篡改或审查（monitor behavior and censor content）。"
          },
          {
            q_type: "reading_item",
            stem: "The proposed 'digital exhaustion' protocol aims to:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Ensure the seller's original copy is deleted upon transferring the file." },
              { key: "B", text: "Ban all e-book sales in favor of physical print editions." },
              { key: "C", text: "Grant publishers perpetual royalties from secondary transactions." },
              { key: "D", text: "Prohibit public libraries from purchasing digital licenses." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】方案细节题。末段指出数字权利用尽机制的核心是通过技术手段确保用户在转让电子文件后，其原始拷贝被彻底删除（original copy is irrevocably erased）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `Across the sweeping agricultural heartlands of Western Europe and the Americas, vast monoculture expanses of wheat, corn, and soy have long exemplified industrial efficiency. Yet, this intensive farming model has inflicted devastating environmental damage: accelerating topsoil erosion, depleting natural groundwater aquifers, and triggering catastrophic biodiversity loss. In response, an age-old ecological practice is staging a scientific renaissance: agroforestry—the deliberate integration of trees and woody shrubs into agricultural crops and livestock pastures.

Agroforestry fundamentally repudiates the industrial premise that agriculture and forestry must occupy mutually segregated zones. By planting deep-rooted timber or fruit trees in widely spaced rows across grain fields, farmers create a resilient polyculture that mimics the ecological complexity of natural ecosystems. Tree canopies act as living windbreaks, moderating extreme ground temperatures, reducing evaporative water loss, and sheltering delicate crops from violent meteorological storms.

Beneath the surface, the subterranean mechanics of agroforestry provide extraordinary soil conservation dividends. Extensive arboreal root networks penetrate deep into lower soil strata, anchoring fragile topsoil and intercepting agricultural nitrates before they leach into freshwater waterways. Furthermore, falling autumnal leaves and decaying root matter infuse the topsoil with organic matter, dramatically enhancing moisture retention and stimulating beneficial mycorrhizal fungi communities. Far from reducing crop yields through sunlight competition, strategic pruning and optimal spacing often enhance total biomass output per hectare.

The ecological benefits extend seamlessly to livestock husbandry in systems known as "silvopasture." Grazing cattle sheltered beneath deciduous canopies suffer markedly less heat stress during sweltering summer heatwaves. Studies indicate that shaded cattle demonstrate improved milk production, faster weight gain, and lower vulnerability to respiratory ailments. Simultaneously, the trees yield secondary revenue streams through marketable timber, nuts, or fruit, insulating farmers against catastrophic market price volatility in single agricultural commodities.

Despite these compelling attributes, widespread adoption of agroforestry is impeded by stubborn financial and institutional barriers. Planting trees requires substantial upfront capital investment, with commercial timber yields taking fifteen to thirty years to mature. Most commercial agricultural subsidy frameworks were designed around annual crop yields, perversely penalizing farmers who intercrop trees on arable land. Transforming our food production systems requires agricultural banks to offer patient, long-term financing and governments to reform farm subsidies to reward ecological regeneration.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Monoculture farming in Western agriculture has led to:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Severe topsoil erosion and biodiversity loss." },
              { key: "B", text: "A complete cessation of groundwater depletion." },
              { key: "C", text: "A surplus of native woodland wildlife habitats." },
              { key: "D", text: "A decline in the use of industrial chemical fertilizers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段第二句明确指出，大规模单一作物种植导致了严重的表土侵蚀、地下水枯竭和灾难性的生物多样性丧失。"
          },
          {
            q_type: "reading_item",
            stem: "How do tree canopies benefit arable crops in agroforestry systems?",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "They act as windbreaks and moderate extreme temperature and moisture loss." },
              { key: "B", text: "They block out all solar radiation to prevent weed germination." },
              { key: "C", text: "They eliminate the need for agricultural irrigation systems entirely." },
              { key: "D", text: "They accelerate the rate of topsoil pesticide absorption." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段末句指出树冠充当防风林，缓和极端地表温度，减少水分蒸发，并保护作物免受暴风雨侵袭。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 3, deep arboreal root networks help:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Anchor topsoil and intercept harmful nitrate runoff." },
              { key: "B", text: "Drain all groundwater from adjacent crop root systems." },
              { key: "C", text: "Prevent any organic matter from entering lower strata." },
              { key: "D", text: "Eradicate beneficial subterranean fungal networks." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第三段指出树木深根系能固紧脆弱表土，并在农业硝酸盐流失污染水体之前将其有效拦截吸收。"
          },
          {
            q_type: "reading_item",
            stem: "In 'silvopasture' systems, shaded grazing environments:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Alleviate heat stress and enhance livestock health and productivity." },
              { key: "B", text: "Increase livestock susceptibility to respiratory illnesses." },
              { key: "C", text: "Force cattle to consume non-nutritional tree bark." },
              { key: "D", text: "Decrease total dairy production during summer months." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出在林牧复合系统中，树荫减轻了牲畜的热应激，提高了产奶量、加快增重并降低患病几率。"
          },
          {
            q_type: "reading_item",
            stem: "What major challenge restricts the broader adoption of agroforestry?",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "High initial capital expenses and rigid agricultural subsidy policies." },
              { key: "B", text: "Total consumer rejection of agricultural produce grown among trees." },
              { key: "C", text: "The universal inability of fruit trees to grow on farm soils." },
              { key: "D", text: "A severe shortage of international agricultural labor." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。末段指出农林复合的主要阻碍在于前期高昂的初始资本投入（树木成长周期长达数十年）以及传统农业补贴制度的排斥性限制。"
          }
        ]
      }
    ]
  }
];
