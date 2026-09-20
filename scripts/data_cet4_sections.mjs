import { buildBankedCloze, buildMatching } from "./data_helpers.mjs";

export const cet4Sections = {
  2024: {
    sectionA: buildBankedCloze({
      title: "Section A: Banked Cloze (选词填空 26-35题)",
      articleWithBlanks: `In contemporary higher education, the rapid proliferation of digital learning tools has profoundly reshaped the classroom environment. While portable laptops and smartphones offer instant access to reference materials, they also introduce persistent (26)____ that undermine deep concentration. Psychological researchers have discovered that multi-tasking during lectures does not merely divide students' attention; it (27)____ impairs long-term memory encoding.\n\nWhen students toggle between note-taking applications and social messaging feeds, their cognitive working memory becomes rapidly exhausted. Consequently, their capacity to synthesize abstract theories and participate in analytical discussions is (28)____ degraded. To counteract this trend, several progressive universities are establishing 'device-free' lecture halls, encouraging undergraduates to take handwritten notes to (29)____ deeper conceptual engagement.\n\nPreliminary surveys indicate that handwritten note-taking forces students to summarize concepts in their own words rather than transcribing spoken sentences (30)____. Furthermore, pedagogical experts emphasize that self-regulated digital boundaries should be (31)____ taught rather than simply imposed through punitive bans. By learning how to manage technological temptations, prospective graduates will be far more (32)____ when entering fast-paced professional workplaces where self-discipline is essential.\n\nNevertheless, educational equity advocates note that digital devices remain (33)____ tools for students with specialized learning accommodations. Audio recording software and screen-reading applications provide indispensable support for individuals with visual impairments or dyslexia. Therefore, administrative policies must balance the goal of minimizing distraction with the (34)____ to maintain inclusive access. Ultimately, universities must cultivate a campus culture where technology serves as a deliberate educational catalyst rather than an (35)____ master.`,
      wordBank: [
        "A) obstacles",
        "B) fundamentally",
        "C) severely",
        "D) foster",
        "E) verbatim",
        "F) explicitly",
        "G) resilient",
        "H) invaluable",
        "I) imperative",
        "J) uncontrolled",
        "K) arbitrary",
        "L) boost",
        "M) fragile",
        "N) diminish",
        "O) cautiously"
      ],
      answers: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
      explanations: [
        "【考点精析】空格(26)：根据空前 persistent（持续的）以及后文'undermine deep concentration'可知，需要填入复数名词作宾语，选 A) obstacles（障碍）。",
        "【考点精析】空格(27)：修饰动词 impairs，需要副词。选 B) fundamentally（从根本上），表示从根本上损害了长期记忆的编码。",
        "【考点精析】空格(28)：在 is ... degraded 被动语态中作状语修饰动词，选 C) severely（严重地），表认知能力遭到严重削弱。",
        "【考点精析】空格(29)：不定式 to ... 后接动词原形，后接'deeper conceptual engagement'，选 D) foster（促进、培养）。",
        "【考点精析】空格(30)：修饰动词 transcribing，对比手写概括，机器打字常是逐字逐句记录，选 E) verbatim（一字不差地、逐字地）。",
        "【考点精析】空格(31)：在 should be ... taught 中作状语，选 F) explicitly（明确地、系统地），表示数字边界应被系统明确地教授。",
        "【考点精析】空格(32)：在 will be far more ... 结构中充当表语形容词，选 G) resilient（有适应力的、韧性强的）。",
        "【考点精析】空格(33)：修饰名词 tools，选 H) invaluable（极其宝贵的），强调对特殊学生而言数字设备是极宝贵的工具。",
        "【考点精析】空格(34)：与 the ... to 搭配的名词，选 I) imperative（当务之急、紧迫要求）。",
        "【考点精析】空格(35)：修饰 master，对比前文 catalyst，选 J) uncontrolled（不受控制的）。"
      ]
    }),
    sectionB: buildMatching({
      title: "Section B: Long Reading & Information Matching (长篇段落信息匹配 36-45题)",
      articleWithParagraphs: `[A] As climate change intensifies worldwide, urban centers face the alarming reality of the 'urban heat island' effect. Dark asphalt pavements, concrete towers, and metallic rooftops absorb radiant solar energy during daylight hours and re-radiate thermal energy throughout the night. Consequently, metropolitan air temperatures often hover between three and eight degrees Celsius higher than surrounding rural valleys.\n\n[B] In response to this compounding environmental hazard, visionary municipal architects are pioneering green architectural strategies. Rather than treating skyscrapers as inert concrete monoliths, developers are incorporating living vegetative envelopes, reflective cool roofs, and natural wind corridors into modern building designs.\n\n[C] Living vertical forests—skyscrapers enveloped by hundreds of evergreen trees and thousands of cascading shrubs—have garnered international acclaim. Pioneered in Milan and now expanding across East Asia, these biophilic towers act as decentralized air filtration systems. Photosynthetic foliage captures airborne particulate pollutants while transpirational cooling reduces external surface temperatures by as much as ten degrees.\n\n[D] Beyond external cooling, vegetative facades provide remarkable thermodynamic insulation for building interiors. In summer, lush leaf canopies shade structural glass facades from brutal solar irradiation, reducing indoor air-conditioning power consumption by up to twenty-five percent. In winter, dense branches mitigate chilling gusts, conserving internal heating.\n\n[E] However, structural engineers emphasize that cultivating vertical gardens presents formidable engineering challenges. Mature trees possess substantial root systems that can penetrate waterproof membranes if barrier fabrics are breached. Furthermore, cantilevered balconies must be reinforced with specialized high-strength tensile steel to withstand extraordinary deadweights of wet soil and storm gusts.\n\n[F] Water management represents an equally critical operational hurdle. Irrigating thousands of square meters of vertical foliage in water-stressed metropolises cannot rely on treated municipal tap supplies. Sustainable buildings overcome this barrier by deploying automated closed-loop greywater harvesting networks, collecting rainwater from rooftops and filtered wastewater from residential sinks.\n\n[G] Simultaneously, materials scientists are revolutionizing roof surfaces through ultra-reflective coatings. These innovative 'super-cool' paints reflect over ninety-five percent of incoming solar radiation directly back into outer space through the atmospheric infrared window, cooling surface temperatures without consuming electrical power.\n\n[H] Economic analyses demonstrate that while green-certified buildings incur higher initial capital construction outlays, they yield profound lifecycle dividends. Lower utility overheads, accelerated rental occupancies, and premium commercial valuations enable developers to recoup initial investments within seven to ten years.\n\n[I] Sociological research also links biophilic urban designs to heightened psychological wellbeing. Office occupants with direct visual access to lush greenery report significantly lower cortisol stress levels, fewer tension headaches, and greater self-rated creative focus compared to peers in windowless drywall enclosures.\n\n[J] Municipal governments are accelerating this transition through forward-thinking zoning mandates and fiscal incentives. Cities such as Singapore and Toronto now require large-scale commercial developments to replace one hundred percent of the building footprint with publicly accessible or vegetative surfaces.\n\n[K] Ultimately, retrofitting existing high-density downtown cores requires collective civic resolve. Transforming concrete jungles into climate-resilient living sanctuaries is no longer an aesthetic luxury; it is a fundamental urban survival imperative for the twenty-first century.`,
      statements: [
        "In water-scarce metropolitan areas, sustainable towers recycle rainwater and sink runoff instead of using drinking water.",
        "Reflective paints cool building roofs by bouncing solar radiation through the atmospheric window into space.",
        "Living towers absorb airborne pollutants and cool outdoor surface temperatures through foliage transpiration.",
        "Extra high-strength steel reinforcement is necessary to support the immense weight of damp earth and withstand gales.",
        "Higher upfront building expenditures can be recovered within a decade thanks to reduced utility bills and higher rents.",
        "Urban heat islands result from concrete and asphalt absorbing daylight solar energy and re-releasing heat after dusk.",
        "Exposure to vegetative elements within architectural spaces is scientifically correlated with reduced worker stress.",
        "Some progressive city authorities have legislated that new commercial structures must substitute their entire base area with green spaces.",
        "Leafy exterior building covers cut summer cooling power demand by shielding glass walls from direct sun.",
        "Converting dense urban areas into resilient green sanctuaries has become an indispensable requirement for survival."
      ],
      answers: ["F", "G", "C", "E", "H", "A", "I", "J", "D", "K"],
      explanations: [
        "【考点精析】对应段落 [F]：段落指出在缺水城市中通过 closed-loop greywater harvesting 收集雨水与水槽废水替代自来水灌溉。",
        "【考点精析】对应段落 [G]：段落介绍 super-cool paints 将超过 95% 的太阳辐射反射回太空（back into outer space through the atmospheric window）。",
        "【考点精析】对应段落 [C]：段落说明 biophilic towers 通过光合作用截留空气微粒并通过叶片蒸腾降低表面温度 10 度。",
        "【考点精析】对应段落 [E]：段落指出悬挑阳台必须采用 high-strength tensile steel 加固以承受湿土和狂风暴风雨的巨大重量。",
        "【考点精析】对应段落 [H]：段落指出尽管初期投入较高，但通过降低能耗和溢价租金可在 7 到 10 年内收回成本（recoup initial investments within seven to ten years）。",
        "【考点精析】对应段落 [A]：段落解释城市热岛效应产生机制在于混凝土和沥青路面白天吸热并在夜间散发辐射热。",
        "【考点精析】对应段落 [I]：段落指出视觉接触绿植的员工皮质醇压力水平显著降低、更有创造专注力。",
        "【考点精析】对应段落 [J]：段落提到新加坡和多伦多等城市出台法规，强制要求大型商业建筑以绿色地表百分之百置换建筑占地足迹。",
        "【考点精析】对应段落 [D]：段落提到茂密树冠遮挡阳光直射玻璃幕墙，使夏季空调降温能耗降低多达 25%。",
        "【考点精析】对应段落 [K]：段落结尾总结将水泥丛林改造为气候韧性庇护所已不再是审美奢侈，而是生存基本要务。"
      ],
      paraCount: 11
    })
  },
  2023: {
    sectionA: buildBankedCloze({
      title: "Section A: Banked Cloze (选词填空 26-35题)",
      articleWithBlanks: `Emerging frontiers in nutritional neuroscience have revealed an intricate, bi-directional communication axis connecting the human gut and the central nervous system. Dubbed the 'gut-brain axis', this biochemical network suggests that emotional states and cognitive performance are (26)____ influenced by microscopic intestinal microbiota.\n\nBeneficial bacterial colonies ferment dietary fiber to produce short-chain fatty acids, which play an (27)____ role in maintaining blood-brain barrier integrity. When individuals consume diets dominated by ultra-processed junk food and refined sugars, the delicate bacterial ecosystem is thrown into (28)____. Harmful pathogens proliferate, triggering chronic systemic inflammation that can (29)____ mood regulation and heighten vulnerability to depressive disorders.\n\nClinical psychiatrists are increasingly integrating 'psychobiotics'—specific probiotic strains and dietary regimens—into standard mental health (30)____. Controlled trials demonstrate that supplementing beneficial bacterial strains can significantly (31)____ perceived stress and enhance emotional resilience in university cohorts.\n\nMoreover, nutritionists emphasize that dietary diversity is the most effective method to (32)____ a resilient microbiome. Consuming a rainbow of vegetables, legumes, fermented foods, and whole grains supplies the prebiotic fuels needed to (33)____ beneficial bacterial proliferation. Conversely, excessive antibiotic overuse should be (34)____ avoided, as broad-spectrum drugs can wipe out healthy colonies indiscriminately. Ultimately, viewing our mental health through a nutritional lens reminds us that emotional equilibrium is (35)____ tied to the microscopic life thriving within our bodies.`,
      wordBank: [
        "A) profoundly",
        "B) essential",
        "C) disarray",
        "D) disrupt",
        "E) therapies",
        "F) alleviate",
        "G) sustain",
        "H) stimulate",
        "I) strictly",
        "J) intrinsically",
        "K) arbitrary",
        "L) boost",
        "M) fragile",
        "N) diminish",
        "O) cautiously"
      ],
      answers: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
      explanations: [
        "【考点精析】空格(26)：修饰动词 influenced，选 A) profoundly（深刻地、极大地）。",
        "【考点精析】空格(27)：修饰名词 role，固定搭配 play an essential role，选 B) essential（至关重要的）。",
        "【考点精析】空格(28)：短语 throw into disarray（使陷入混乱/失衡），选 C) disarray（混乱）。",
        "【考点精析】空格(29)：情态动词 can 后接动词原形，与 heighten 并列，选 D) disrupt（扰乱、破坏）。",
        "【考点精析】空格(30)：名词充当 integrating ... into 的宾语，选 E) therapies（治疗方案/疗法）。",
        "【考点精析】空格(31)：后接 perceived stress（感知到的压力），选 F) alleviate（缓解、减轻）。",
        "【考点精析】空格(32)：动词原形后接 a resilient microbiome，选 G) sustain（维持、保持）。",
        "【考点精析】空格(33)：后接 proliferation，选 H) stimulate（刺激、促进）。",
        "【考点精析】空格(34)：修饰动词 avoided，选 I) strictly（严格地）。",
        "【考点精析】空格(35)：在 is ... tied to 中修饰，选 J) intrinsically（内在本质地、密不可分地）。"
      ]
    }),
    sectionB: buildMatching({
      title: "Section B: Long Reading & Information Matching (长篇段落信息匹配 36-45题)",
      articleWithParagraphs: `[A] For over a century, the global electrical grid operated under a centralized paradigm. Massive coal-fired generators and hydroelectric dams produced power in remote territories, transmitting electricity across high-voltage transmission corridors to passive domestic consumers.\n\n[B] Today, this historic model is undergoing an irreversible structural transition toward decentralized solar energy. Plummeting manufacturing costs for photovoltaic panels, paired with breakthroughs in lithium battery storage, have empowered residential homeowners and local cooperatives to generate, store, and trade their own clean electricity.\n\n[C] In suburban communities across Europe and Australia, rooftop solar arrays have transformed conventional electricity purchasers into active 'prosumers.' On bright summer afternoons, decentralized panels collectively generate surplus power, feeding gigawatts back into local distribution circuits.\n\n[D] However, localized power injections present severe engineering difficulties for legacy electrical distribution infrastructure. Traditional substations were designed for unidirectional electricity flow from central power plants down to suburban neighborhoods. Uncontrolled back-feeding of surplus solar energy can cause dangerous voltage spikes and trip localized transformers.\n\n[E] To harmonize distributed solar generation with grid reliability, energy pioneers are developing neighborhood-scale microgrids. Equipped with computerized automated switches and shared community battery banks, microgrids can seamlessly disconnect from the national grid during blackouts, operating in 'island mode' to supply uninterrupted emergency power.\n\n[F] Furthermore, dynamic peer-to-peer energy trading platforms are democratizing local energy economies. Using encrypted ledger technology, neighbors with surplus rooftop solar capacity can sell excess kilowatt-hours directly to adjacent households lacking solar exposure, bypassing expensive corporate energy middlemen.\n\n[G] Environmental scientists highlight that distributed solar deployment radically conserves land resources. Unlike utility-scale solar farms that require thousands of acres of agricultural land, rooftop panels occupy previously unproductive architectural airspace on warehouses, parking structures, and residential rooftops.\n\n[H] Despite these ecological dividends, socioeconomic equity questions cloud the solar transition. High initial installation expenses mean affluent homeowners disproportionately benefit from government solar subsidies and reduced utility tariffs, while low-income renters remain trapped paying escalating rates for legacy grid maintenance.\n\n[I] Progressive municipal authorities are tackling this disparity by financing 'community solar' projects. Under this framework, renters and apartment dwellers can purchase fractional shares in a shared off-site solar farm, receiving monthly utility bill credits without needing to own a private rooftop.\n\n[J] National electrical regulatory agencies are also modernizing interconnection rules to accelerate the retirement of fossil-fueled peaker plants, replacing them with virtual power plants (VPPs) aggregating thousands of distributed home batteries.\n\n[K] In conclusion, the democratization of solar power represents much more than a technological shift; it marks a profound decentralization of economic power and a vital cornerstone in the global race to reach net-zero carbon emissions.`,
      statements: [
        "Traditional power stations and dams transmitted electricity in one direction to passive consumers for decades.",
        "Shared community solar farms allow apartment renters to enjoy utility discounts without owning a private roof.",
        "Rooftop installations save vast amounts of open land by utilizing otherwise unused architectural surface area.",
        "Rapidly falling photovoltaic production costs enable individual homeowners to produce and store clean power.",
        "Older substations risk transformer damage and voltage fluctuations when surplus solar electricity flows backward.",
        "Peer-to-peer trading platforms enable residents to sell excess electricity directly to nearby neighbors without middlemen.",
        "Wealthy property owners gain more from clean energy incentives, leaving poorer tenants to shoulder grid upkeep bills.",
        "Microgrids can detach from main grids during external power failures and continue supplying local electricity in island mode.",
        "Virtual power plants pool thousands of home battery systems to supplant traditional fossil-fuel reserve stations.",
        "Suburban households with rooftop arrays produce extra clean electricity on sunny days, turning consumers into prosumers."
      ],
      answers: ["A", "I", "G", "B", "D", "F", "H", "E", "J", "C"],
      explanations: [
        "【考点精析】对应段落 [A]：描述上个世纪中心化发电站通过高压线路单向输电给被动消费者的模式。",
        "【考点精析】对应段落 [I]：介绍 community solar 项目允许没有屋顶的租客和公寓住户购买份额享受账单抵扣。",
        "【考点精析】对应段落 [G]：强调屋顶光伏利用了闲置建筑表面，极大节约了农业与生态用地（conserves land resources）。",
        "【考点精析】对应段落 [B]：指出光伏制造成本断崖式下跌与电池突破赋能家庭自主发电储电。",
        "【考点精析】对应段落 [D]：解释传统变电站是按单向流动设计的，多余电能倒灌易造成电压骤升甚至跳闸损坏变压器。",
        "【考点精析】对应段落 [F]：描述点对点交易平台让有富余电量的居民直接卖给邻居，绕过昂贵的能源中介。",
        "【考点精析】对应段落 [H]：指出初始高昂成本导致富裕家庭过度享受补贴，低收入租客却承受电网维护费用的公平性问题。",
        "【考点精析】对应段落 [E]：介绍微电网在外部断电时可切断连接并以“孤岛模式”（island mode）持续自给供电。",
        "【考点精析】对应段落 [J]：介绍虚拟电厂聚合数千个分布式家庭储能电池取代化石能源调峰电站。",
        "【考点精析】对应段落 [C]：描述晴朗夏日屋顶多余发电回馈电网，消费者升级为集生产与消费于一身的“生产型消费者”（prosumers）。"
      ],
      paraCount: 11
    })
  }
};
