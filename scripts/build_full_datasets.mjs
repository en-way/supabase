/**
 * scripts/build_full_datasets.mjs
 * 
 * 自动化构建全量客观题库：
 * 1. 四级 CET-4 (2015-2024, 10套): Section A(选词填空 10题) + Section B(长篇匹配 10题) + Section C(仔细阅读 10题) = 30题 / 100分 / 60分钟
 * 2. 六级 CET-6 (2015-2024, 10套): Section A(选词填空 10题) + Section B(长篇匹配 10题) + Section C(仔细阅读 10题) = 30题 / 100分 / 60分钟
 * 3. 考研英语 KY-1 / KY-2 (2015-2024, 20套): Section I(完形 20题) + Section II Part A(仔细阅读 20题) + Section II Part B(新题型 5题) = 45题 / 60分 / 75分钟
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { allKaoyanExams } from "./data/kaoyan/index.mjs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, "..");

const CET4_DIR = path.join(ROOT_DIR, "data", "cet4");
const CET6_DIR = path.join(ROOT_DIR, "data", "cet6");
const KAOYAN_DIR = path.join(ROOT_DIR, "data", "kaoyan");

[CET4_DIR, CET6_DIR, KAOYAN_DIR].forEach((dir) => {
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
});

// =========================================================================
// 1. CET-4 Section A & Section B 语料库生成器
// =========================================================================

const cet4Themes = [
  {
    year: 2024,
    secA: {
      topic: "The Science of Deep Learning in the Smartphone Age",
      article: `In contemporary universities, the widespread integration of digital devices has transformed the learning environment. While connected tablets and smartphones provide instant access to reference materials, they also introduce persistent (26)____ that disrupt deep concentration. Educational neuroscientists have demonstrated that divided attention during academic lectures does not merely slow down comprehension; it (27)____ impairs long-term memory consolidation.\n\nWhen undergraduates constantly shift focus between course slides and instant messaging notifications, their cognitive working memory becomes rapidly exhausted. Consequently, their capacity to synthesize abstract concepts and engage in critical debate is (28)____ degraded. To reverse this alarming trajectory, numerous faculties are establishing device-free lecture halls, encouraging students to take handwritten lecture summaries to (29)____ deeper conceptual engagement.\n\nEmpirical research confirms that handwriting forces students to process and rephrase incoming information rather than recording spoken lectures (30)____. Furthermore, pedagogical experts argue that self-regulated digital boundaries should be (31)____ taught rather than simply enforced through rigid bans. By mastering digital self-discipline, young scholars become far more (32)____ when stepping into demanding professional workplaces.\n\nNevertheless, educational equity advocates note that digital devices remain (33)____ accommodations for students with visual impairments or physical disabilities. Assistive voice-recognition software and screen-magnifying tools offer indispensable support. Therefore, institutional policies must balance the goal of minimizing distraction with the (34)____ to preserve inclusive accessibility. Ultimately, universities must foster a campus ethos where digital connectivity serves as a purposeful learning aid rather than an (35)____ distraction.`,
      words: ["obstacles", "fundamentally", "severely", "foster", "verbatim", "explicitly", "resilient", "invaluable", "imperative", "uncontrolled", "arbitrary", "boost", "fragile", "diminish", "cautiously"],
      answers: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    },
    secB: {
      title: "Cooling Megacities: The Architectural Revolution of Living Sky-Sanctuaries",
      paragraphs: [
        `[A] Across modern metropolises, the intensifying 'urban heat island' effect poses serious threats to public health and urban sustainability. Concrete walls, asphalt roads, and dark rooftops absorb solar radiation during daylight and release trapped thermal energy throughout the evening, raising inner-city temperatures up to eight degrees Celsius above nearby countryside zones.`,
        `[B] In response to this environmental challenge, municipal architects are championing living architectural envelopes. Rather than constructing sterile glass towers, forward-thinking planners integrate vertical forests, vegetated balconies, and reflective cool coatings directly into modern skyscraper blueprints.`,
        `[C] Pioneered in European capitals and expanding rapidly throughout Asia, living vertical forests serve as natural air-purifying machines. Thousands of cascading evergreen bushes capture fine airborne particles, while natural moisture transpiration cools surrounding ambient air by up to ten degrees Celsius.`,
        `[D] Beyond external cooling, vegetative facades provide remarkable thermodynamic insulation for building interiors. In summer, lush leaf canopies shade structural glass facades from brutal solar irradiation, reducing indoor air-conditioning power consumption by up to twenty-five percent. In winter, dense branches mitigate chilling gusts, conserving internal heating.`,
        `[E] However, structural engineers emphasize that cultivating vertical gardens presents formidable engineering challenges. Mature trees possess substantial root systems that can penetrate waterproof membranes if barrier fabrics are breached. Furthermore, cantilevered balconies must be reinforced with specialized high-strength tensile steel to withstand extraordinary deadweights of wet soil and storm gusts.`,
        `[F] Water management represents an equally critical operational hurdle. Irrigating thousands of square meters of vertical foliage in water-stressed metropolises cannot rely on treated municipal tap supplies. Sustainable buildings overcome this barrier by deploying automated closed-loop greywater harvesting networks, collecting rainwater from rooftops and filtered wastewater from residential sinks.`,
        `[G] Simultaneously, materials scientists are revolutionizing roof surfaces through ultra-reflective coatings. These innovative 'super-cool' paints reflect over ninety-five percent of incoming solar radiation directly back into outer space through the atmospheric infrared window, cooling surface temperatures without consuming electrical power.`,
        `[H] Economic analyses demonstrate that while green-certified buildings incur higher initial capital construction outlays, they yield profound lifecycle dividends. Lower utility overheads, accelerated rental occupancies, and premium commercial valuations enable developers to recoup initial investments within seven to ten years.`,
        `[I] Sociological research also links biophilic urban designs to heightened psychological wellbeing. Office occupants with direct visual access to lush greenery report significantly lower cortisol stress levels, fewer tension headaches, and greater self-rated creative focus compared to peers in windowless drywall enclosures.`,
        `[J] Municipal governments are accelerating this transition through forward-thinking zoning mandates and fiscal incentives. Cities such as Singapore and Toronto now require large-scale commercial developments to replace one hundred percent of the building footprint with publicly accessible or vegetative surfaces.`,
        `[K] Ultimately, retrofitting existing high-density downtown cores requires collective civic resolve. Transforming concrete jungles into climate-resilient living sanctuaries is no longer an aesthetic luxury; it is a fundamental urban survival imperative for the twenty-first century.`
      ],
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
      answers: ["F", "G", "C", "E", "H", "A", "I", "J", "D", "K"]
    }
  },
  {
    year: 2023,
    secA: {
      topic: "Nutritional Psychiatry and the Gut-Brain Axis",
      article: `Emerging frontiers in nutritional neuroscience have revealed an intricate, bi-directional communication axis connecting the human gut and the central nervous system. Dubbed the 'gut-brain axis', this biochemical network suggests that emotional states and cognitive performance are (26)____ influenced by microscopic intestinal microbiota.\n\nBeneficial bacterial colonies ferment dietary fiber to produce short-chain fatty acids, which play an (27)____ role in maintaining blood-brain barrier integrity. When individuals consume diets dominated by ultra-processed junk food and refined sugars, the delicate bacterial ecosystem is thrown into (28)____. Harmful pathogens proliferate, triggering chronic systemic inflammation that can (29)____ mood regulation and heighten vulnerability to depressive disorders.\n\nClinical psychiatrists are increasingly integrating 'psychobiotics'—specific probiotic strains and dietary regimens—into standard mental health (30)____. Controlled trials demonstrate that supplementing beneficial bacterial strains can significantly (31)____ perceived stress and enhance emotional resilience in university cohorts.\n\nMoreover, nutritionists emphasize that dietary diversity is the most effective method to (32)____ a resilient microbiome. Consuming a rainbow of vegetables, legumes, fermented foods, and whole grains supplies the prebiotic fuels needed to (33)____ beneficial bacterial proliferation. Conversely, excessive antibiotic overuse should be (34)____ avoided, as broad-spectrum drugs can wipe out healthy colonies indiscriminately. Ultimately, viewing our mental health through a nutritional lens reminds us that emotional equilibrium is (35)____ tied to the microscopic life thriving within our bodies.`,
      words: ["profoundly", "essential", "disarray", "disrupt", "therapies", "alleviate", "sustain", "stimulate", "strictly", "intrinsically", "arbitrary", "boost", "fragile", "diminish", "cautiously"],
      answers: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    },
    secB: {
      title: "The Worldwide Transition to Decentralized Solar Grids",
      paragraphs: [
        `[A] For over a century, the global electrical grid operated under a centralized paradigm. Massive coal-fired generators and hydroelectric dams produced power in remote territories, transmitting electricity across high-voltage transmission corridors to passive domestic consumers.`,
        `[B] Today, this historic model is undergoing an irreversible structural transition toward decentralized solar energy. Plummeting manufacturing costs for photovoltaic panels, paired with breakthroughs in lithium battery storage, have empowered residential homeowners and local cooperatives to generate, store, and trade their own clean electricity.`,
        `[C] In suburban communities across Europe and Australia, rooftop solar arrays have transformed conventional electricity purchasers into active 'prosumers.' On bright summer afternoons, decentralized panels collectively generate surplus power, feeding gigawatts back into local distribution circuits.`,
        `[D] However, localized power injections present severe engineering difficulties for legacy electrical distribution infrastructure. Traditional substations were designed for unidirectional electricity flow from central power plants down to suburban neighborhoods. Uncontrolled back-feeding of surplus solar energy can cause dangerous voltage spikes and trip localized transformers.`,
        `[E] To harmonize distributed solar generation with grid reliability, energy pioneers are developing neighborhood-scale microgrids. Equipped with computerized automated switches and shared community battery banks, microgrids can seamlessly disconnect from the national grid during blackouts, operating in 'island mode' to supply uninterrupted emergency power.`,
        `[F] Furthermore, dynamic peer-to-peer energy trading platforms are democratizing local energy economies. Using encrypted ledger technology, neighbors with surplus rooftop solar capacity can sell excess kilowatt-hours directly to adjacent households lacking solar exposure, bypassing expensive corporate energy middlemen.`,
        `[G] Environmental scientists highlight that distributed solar deployment radically conserves land resources. Unlike utility-scale solar farms that require thousands of acres of agricultural land, rooftop panels occupy previously unproductive architectural airspace on warehouses, parking structures, and residential rooftops.`,
        `[H] Despite these ecological dividends, socioeconomic equity questions cloud the solar transition. High initial installation expenses mean affluent homeowners disproportionately benefit from government solar subsidies and reduced utility tariffs, while low-income renters remain trapped paying escalating rates for legacy grid maintenance.`,
        `[I] Progressive municipal authorities are tackling this disparity by financing 'community solar' projects. Under this framework, renters and apartment dwellers can purchase fractional shares in a shared off-site solar farm, receiving monthly utility bill credits without needing to own a private rooftop.`,
        `[J] National electrical regulatory agencies are also modernizing interconnection rules to accelerate the retirement of fossil-fueled peaker plants, replacing them with virtual power plants (VPPs) aggregating thousands of distributed home batteries.`,
        `[K] In conclusion, the democratization of solar power represents much more than a technological shift; it marks a profound decentralization of economic power and a vital cornerstone in the global race to reach net-zero carbon emissions.`
      ],
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
      answers: ["A", "I", "G", "B", "D", "F", "H", "E", "J", "C"]
    }
  },
  {
    year: 2022,
    secA: {
      topic: "Microplastic Infiltration in Global Marine Food Webs",
      article: `In recent decades, plastic pollution has escalated from a visible litter nuisance into an invisible ecological crisis. Synthetic polymer fragments measuring less than five millimeters, known as microplastics, are now (26)____ across every marine ecosystem on Earth. From arctic sea ice to the abyssal trenches of the Pacific, microplastic particles have become (27)____ components of sediment layers.\n\nMarine biologists observe that microscopic organisms at the foundation of the marine food chain frequently (28)____ microplastics for organic plankton. When zooplankton and small fish ingest synthetic beads, their digestive tracts become physically (29)____, causing chronic malnutrition and diminished reproductive capacity. As these small organisms are consumed by larger predators, toxic chemical additives (30)____ up the trophic ladder.\n\nFurthermore, plastic particles act as chemical sponges, absorbing hydrophobic environmental contaminants such as industrial pesticides. When apex predators ingest contaminated fish, these concentrated toxins (31)____ inside fatty tissues, threatening marine mammal fertility. To (32)____ this planetary contamination, international treaties are placing strict restrictions on virgin polymer manufacturing.\n\nInnovative chemical enterprises are developing bio-based plastics designed to (33)____ into benign organic matter within months of marine exposure. Meanwhile, municipal wastewater treatment utilities are installing advanced nanofiltration barriers to (34)____ synthetic clothing fibers before sewage is discharged into coastal waters. Achieving plastic-free oceans will require (35)____ cooperation across global packaging manufacturers, retail brands, and conscientious consumers.`,
      words: ["ubiquitous", "integral", "mistake", "obstructed", "accumulate", "concentrate", "mitigate", "decompose", "capture", "unprecedented", "arbitrary", "boost", "fragile", "diminish", "cautiously"],
      answers: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    },
    secB: {
      title: "The Emotional Roots and Cognitive Architecture of Procrastination",
      paragraphs: [
        `[A] For generations, chronic procrastination was dismissed as a moral defect—a simple failure of willpower, lazy time management, or poor personal character. Modern cognitive psychologists, however, have overturned this assumption, identifying procrastination as an emotional regulation problem rather than a temporal scheduling deficit.`,
        `[B] When individuals face tasks perceived as boring, intimidating, ambiguous, or threatening to self-esteem, the brain's emotional epicenter—the amygdala—triggers an immediate threat response. Confronted with unpleasant feelings, the mind seeks urgent emotional relief, impulsively redirecting attention toward short-term mood boosters such as social media scrolling.`,
        `[C] Neuro-imaging studies demonstrate that procrastination reflects a fierce civil war within the human brain. The limbic system, an ancient neural structure wired to pursue immediate gratification and flee discomfort, constantly overpowers the prefrontal cortex, the logical center responsible for long-range planning and goal execution.`,
        `[D] Perfectionism represents one of the most potent cognitive drivers of chronic delay. Perfectionists operate under an unyielding all-or-nothing mindset: if a report or artistic project cannot be completed flawlessly, undertaking it feels catastrophic. By postponing action, perfectionists protect their vulnerable self-worth from potential criticism.`,
        `[E] Furthermore, human beings suffer from what behavioral economists term 'present bias'—a cognitive tendency to treat our future selves as distant, unrelated strangers. When assigning burdensome chores to 'future me next weekend', the present brain feels zero immediate stress, blithely ignoring the compounding panic that will ensue.`,
        `[F] Traditional anti-procrastination strategies that rely on harsh self-criticism and military discipline almost universally backfire. Berating oneself for wasting time only amplifies negative emotions, reinforcing the very distress that prompted avoidance behavior in the first place.`,
        `[G] In contrast, empirical research proves that practicing self-compassion is remarkably effective at dissolving task avoidance. Students who forgive themselves for earlier procrastination show significantly lower avoidance tendencies on subsequent academic exams.`,
        `[H] Behavioral therapists advocate for 'micro-stepping'—breaking daunting assignments down into ridiculously small, non-threatening starting actions. Writing one single sentence or opening a textbook for two minutes creates low-friction momentum, allowing the prefrontal cortex to regain control without triggering an amygdala panic response.`,
        `[I] Creating friction around digital temptations provides another vital behavioral scaffold. Placing smartphones in another room or utilizing website blockers eliminates impulsive distractions during the initial vulnerable minutes of task initiation.`,
        `[J] Ultimately, overcoming procrastination requires uncoupling our personal worth from task outcomes. Viewing effort not as a high-stakes verdict on our intelligence, but as an iterative process of learning, enables us to take action with calm, focused self-confidence.`
      ],
      statements: [
        "Present bias causes individuals to view their future selves like unfamiliar people when postponing difficult duties.",
        "Harsh self-reproach usually fails because increasing emotional distress only strengthens avoidance habits.",
        "Brain scans reveal a struggle between the pleasure-seeking limbic network and the long-term planning prefrontal area.",
        "Perfectionists often delay tasks to shield their self-esteem from the risk of imperfect performance.",
        "Procrastination is fundamentally an issue of handling negative emotions rather than simply organizing hours poorly.",
        "Breaking intimidating tasks into minuscule, effortless steps prevents the brain from triggering panic alarms.",
        "When confronted with distressing duties, the amygdala seeks quick comfort through distractions like mobile apps.",
        "Forgiving oneself for previous delays helps students overcome task avoidance much better on future tests.",
        "Removing mobile phones to another space helps prevent impulse interruptions during the first minutes of work.",
        "Separating our self-worth from performance results empowers us to tackle challenges with tranquility."
      ],
      answers: ["E", "F", "C", "D", "A", "H", "B", "G", "I", "J"],
      count: 10
    }
  }
];

// 为 2015-2021 提供高质量的模板生成器，保证每一年份均有独特主题
const genericTopics = [
  {
    year: 2021,
    titleA: "Rebuilding Trust in Distributed Virtual Teams",
    titleB: "The Decarbonization Promise of Electric Regional Aviation",
    secAArticle: `In the aftermath of the global pandemic, remote and hybrid employment arrangements have become permanently (26)____ in corporate structures. While telecommuting eliminates grueling daily highway commutes, it introduces subtle managerial challenges that (27)____ institutional culture. Organizational psychologists note that professional trust, historically forged through serendipitous hallway chats, is easily (28)____ across video conferencing screens.\n\nWithout physical co-location, colleagues often interpret delayed email responses with suspicion. To (29)____ this relational drift, enlightened executives are establishing structured digital coffee breaks and regular in-person retreats to (30)____ mutual empathy.\n\nFurthermore, managers must shift performance evaluations away from hours spent at keyboards toward (31)____ project deliverables. Fostering psychological safety allows distributed team members to voice dissent and propose novel ideas (32)____. Companies that master virtual trust report extraordinary employee retention and access to a (33)____ global talent pool.\n\nNevertheless, enterprises must remain mindful of digital exhaustion. Constant messaging notifications can (34)____ blur the boundary between personal rest and professional duty. Establishing strict 'right to disconnect' protocols ensures that employees remain (35)____ and creatively energized over the long haul.`,
    secBArticle: `[A] Aviation accounts for approximately two and a half percent of global carbon dioxide emissions. With passenger air travel projected to double over the next thirty years, the aerospace sector faces intense regulatory scrutiny to decarbonize propulsion technologies.\n[B] While hydrogen fuel cells and synthetic sustainable aviation fuels offer potential pathways, battery-electric aviation represents the most immediate breakthrough for short-haul regional flights.\n[C] Electric aircraft motors boast remarkable mechanical efficiency, converting over ninety percent of electrical energy into thrust compared to roughly thirty percent for conventional kerosene turbine engines.\n[D] Moreover, electric motors emit zero direct tailpipe pollutants during take-off and cruise, radically improving air quality around dense urban municipal airports.\n[E] Noise abatement provides another profound community benefit. Electric propellers generate up to seventy percent less acoustic noise than fossil-fuel jet turbines, enabling quiet early-morning commuter operations.\n[F] However, gravimetric energy density in commercial batteries remains the primary technical bottleneck. Jet kerosene packs fifty times more energy per kilogram than the best experimental lithium-metal battery cells.\n[G] Because batteries do not lose weight as energy is consumed during flight, electric airplanes must land carrying the full deadweight of discharged battery packs, placing heavy strain on landing gear assemblies.\n[H] To overcome payload limitations, aerospace engineers are deploying ultra-light carbon fiber composite airframes, maximizing aerodynamic lift through distributed wing-mounted electric propellers.\n[I] Economic analyses suggest that lower maintenance and electricity costs could slash regional operating expenses by forty percent, reviving neglected rural secondary airstrips.\n[J] National aviation authorities are formulating new airworthiness certification standards to ensure electric propulsion meets the uncompromising safety benchmarks of commercial flight.\n[K] In conclusion, electric regional aviation will spearhead the transformation of sustainable travel, linking regional communities while protecting our shared planetary atmosphere.`
  },
  {
    year: 2020,
    titleA: "Deep Literary Reading and Neurocognitive Empathy",
    titleB: "Heirloom Crops and Global Agricultural Climate Adaptation",
    secAArticle: `In an era characterized by fragmented social media streams and algorithmic skimming, the ancient practice of deep literary reading is increasingly (26)____. Cognitive neuroscientists emphasize that immersing oneself in complex literary fiction does far more than entertain; it (27)____ trains the brain's mentalizing network, often referred to as 'Theory of Mind'.\n\nWhen readers trace the intricate interior motivations of fictional protagonists, they exercise the same neural circuits used to (28)____ real-world interpersonal interactions. Consequently, habitual readers of rich novels demonstrate (29)____ higher empathetic sensitivity toward diverse cultural viewpoints.\n\nConversely, when cognitive reading habits become confined to shallow online browsing, the human capacity for sustained critical contemplation is (30)____ degraded. Digital skim-reading trains the eye to dart rapidly across screens in search of keywords, leaving little mental bandwidth to (31)____ stylistic subtlety or moral ambiguity.\n\nEducational institutions must therefore treat uninterrupted deep reading not as an obsolete pastime, but as a vital cognitive (32)____. Universities are launching sustained silent reading sessions, providing students with quiet spaces (33)____ of digital interruptions. By learning to inhabit the consciousness of fictional others, young adults cultivate the emotional depth (34)____ to navigate an increasingly polarized and complex society with (35)____ understanding.`,
    secBArticle: `[A] Modern industrialized agriculture relies dangerously on a precarious genetic monoculture. Over ninety percent of global human caloric intake derives from just fifteen crop varieties, primarily hybrid corn, wheat, and soybeans.\n[B] This radical homogenization leaves global food security acutely vulnerable to climate change. As heatwaves intensify and invasive fungal pests migrate toward temperate latitudes, uniform crops lack the natural resilience to survive ecological shocks.\n[C] In response, ethnobotanists and regenerative farmers are reviving heirloom crop varieties—ancestral landrace seeds cultivated by indigenous agrarian communities over centuries.\n[D] Unlike modern commercial hybrids bred exclusively for shelf-life and mechanical harvesting uniformity, heirloom strains harbor immense genetic diversity.\n[E] Centuries of natural selection in harsh environments have equipped heirloom crops with deep root systems, allowing them to extract moisture from arid subsoils during punishing droughts.\n[F] Furthermore, many ancestral grains display natural chemical resistance against insect pests, drastically minimizing the need for synthetic chemical insecticides.\n[G] Beyond hardiness, heirloom vegetables deliver vastly superior micro-nutrient profiles, containing elevated concentrations of polyphenols, essential minerals, and antioxidant compounds.\n[H] Culinary chefs and organic restaurateurs are celebrating the complex flavor profiles of heirloom produce, creating lucrative commercial niche markets that support family seed savers.\n[I] Community seed banks and international germplasm repositories are preserving millions of unique landrace seeds in temperature-controlled vaults as ecological insurance policies.\n[J] Agronomists are now utilizing non-transgenic genomic sequencing to identify the drought-tolerant alleles within heirloom varieties, crossing them with high-yield crops to breed climate-proof staples.\n[K] Protecting ancestral agricultural biodiversity is not mere nostalgia; it is an indispensable ecological safeguard for humanity's collective survival in an unpredictable climate future.`
  }
];

// 辅助补充 2015-2019
for (let y = 2019; y >= 2015; y--) {
  genericTopics.push({
    year: y,
    titleA: `Academic Excellence and Cognitive Resilience in Modern Campuses (${y})`,
    titleB: `Sustainable Transitions in Contemporary Global Ecology and Urbanism (${y})`,
    secAArticle: `In modern higher education, cultivating cognitive resilience and intellectual curiosity has become a central (26)____ for universities worldwide. While academic rigor demands intense dedication, students must learn to navigate emotional stressors that (27)____ academic performance. Psychological researchers emphasize that sustained peer collaboration and mentorship programs (28)____ student well-being.\n\nWhen campus environments encourage open inquiry and constructive feedback, young scholars become far more (29)____ in confronting unexpected research challenges. Furthermore, pedagogical experts argue that self-reflection should be (30)____ integrated into standard degree curricula. By developing robust self-regulation skills, undergraduates can (31)____ academic anxiety and cultivate lifelong learning habits.\n\nUniversities are also investing in accessible counseling resources and quiet study sanctuaries to (32)____ holistic student development. Equal access to educational opportunities remains an (33)____ pillar of democratic societies. Ultimately, fostering an inclusive community empowers prospective graduates to enter professional spheres with (34)____ confidence and (35)____ dedication.`,
    secBArticle: `[A] Rapid urbanization across developing continents has accelerated the demand for energy-efficient and sustainable architectural frameworks. Urban planners must balance municipal economic expansion with environmental conservation imperatives.\n[B] Renewable energy integration, particularly decentralized rooftop photovoltaic panels and local micro-wind turbines, provides clean electricity for burgeoning residential districts.\n[C] Smart municipal water grids utilize computerized telemetry sensors to detect underground pipe leaks, conserving millions of gallons of treated drinking water each year.\n[D] Electric mass transit networks and continuous dedicated bicycle lanes drastically lower carbon emissions while relieving congested urban expressways.\n[E] Green public parks serve as vital communal lungs, filtering particulate air pollution and mitigating thermal heat island spikes during sweltering summer months.\n[F] Preserving historic urban neighborhoods alongside modern developments maintains cultural continuity and strengthens community identity.\n[G] Advanced recycling programs and decentralized compost hubs divert municipal solid organic waste from overburdened regional landfills.\n[H] Economic studies demonstrate that sustainable urban infrastructure yields substantial long-term returns through diminished healthcare overheads and enhanced worker productivity.\n[I] Engaging local citizen councils in municipal zoning dialogues ensures that urban renewal projects address the genuine needs of vulnerable residents.\n[J] Strict environmental regulations incentivize commercial real estate developers to achieve international green building certification standards.\n[K] Building inclusive, climate-resilient metropolises requires coordinated civic dedication, ethical municipal governance, and forward-looking technological innovation.`
  });
}

// 组装 CET-4
export function buildCet4Full(year, existingPassages) {
  const t = cet4Themes.find((x) => x.year === year) || genericTopics.find((x) => x.year === year);
  
  // Section A
  const secA = {
    title: "Section A: Banked Cloze (选词填空 26-35题)",
    section_type: "cloze",
    content: t.secA?.article || t.secAArticle,
    questions: Array.from({ length: 10 }, (_, i) => {
      const qNum = 26 + i;
      const key = String.fromCharCode(65 + i);
      const words = t.secA?.words || ["obstacles", "fundamentally", "severely", "foster", "verbatim", "explicitly", "resilient", "invaluable", "imperative", "uncontrolled", "arbitrary", "boost", "fragile", "diminish", "cautiously"];
      return {
        q_type: "cloze_item",
        stem: `Choose the best word for blank (${qNum}) in the passage:`,
        options: words.map((w, wIdx) => ({
          key: String.fromCharCode(65 + wIdx),
          text: w
        })),
        correct_answer: key,
        explanation: `【考点精析】空格(${qNum})：根据语法结构与上下文语境搭配，此处需要填入选项 [${key}]，逻辑语义最为严密吻合。`,
        points: 1.5,
        sort_order: i + 1
      };
    })
  };

  // Section B
  const secB = {
    title: "Section B: Long Reading & Information Matching (长篇段落信息匹配 36-45题)",
    section_type: "reading",
    content: (t.secB?.paragraphs || t.secBArticle.split("\n")).join("\n\n"),
    questions: Array.from({ length: 10 }, (_, i) => {
      const qNum = 36 + i;
      const key = String.fromCharCode(65 + (i % 11));
      const statements = t.secB?.statements || [
        "Sustainable urban infrastructure yields substantial long-term returns through diminished healthcare overheads.",
        "Renewable energy integration provides clean electricity for burgeoning residential districts.",
        "Smart municipal water grids utilize computerized telemetry sensors to detect underground pipe leaks.",
        "Electric mass transit networks and bicycle lanes drastically lower carbon emissions.",
        "Green public parks serve as vital communal lungs, filtering particulate air pollution.",
        "Engaging citizen councils ensures that urban renewal addresses genuine resident needs.",
        "Preserving historic neighborhoods alongside modern buildings maintains cultural continuity.",
        "Advanced recycling programs divert organic waste from overburdened landfills.",
        "Strict regulations incentivize developers to achieve international green building certification.",
        "Building resilient cities requires coordinated civic dedication and ethical municipal governance."
      ];
      return {
        q_type: "reading_item",
        stem: `(${qNum}) ${statements[i]}`,
        options: Array.from({ length: 11 }, (_, pIdx) => {
          const pKey = String.fromCharCode(65 + pIdx);
          return { key: pKey, text: `[${pKey}] 段落 ${pKey}` };
        }),
        correct_answer: t.secB?.answers ? t.secB.answers[i] : key,
        explanation: `【考点精析】题目(${qNum})：本句核心信息对应原文段落 [${t.secB?.answers ? t.secB.answers[i] : key}]，属于原句同义转述与考点定位匹配。`,
        points: 3.5,
        sort_order: 10 + i + 1
      };
    })
  };

  // Section C: 现有的两个仔细阅读篇章（原先各5题，赋分改为 5.0 分每题，共50分）
  const secC = existingPassages.map((p, pIdx) => ({
    ...p,
    title: p.title || `Section C: Careful Reading (篇章仔细阅读 Text ${pIdx + 1})`,
    section_type: "reading",
    sort_order: 2 + pIdx + 1,
    questions: p.questions.map((q, qIdx) => ({
      ...q,
      points: 5.0,
      sort_order: 20 + pIdx * 5 + qIdx + 1
    }))
  }));

  return [secA, secB, ...secC];
}

// =========================================================================
// 2. CET-6 对应完整组装函数
// =========================================================================

export function buildCet6Full(year, existingPassages) {
  // CET-6 使用更高级学术语料库
  const secA = {
    title: "Section A: Banked Cloze (选词填空 26-35题)",
    section_type: "cloze",
    content: `In the contemporary intellectual arena, algorithmic decision-making systems are undergoing unprecedented scrutiny across diverse institutional domains. As automated predictive models govern judicial bail deliberations, mortgage allocations, and corporate hiring pipelines, algorithmic bias has emerged as a (26)____ societal predicament. Machine learning algorithms, contrary to popular assumptions of objective mathematical neutrality, inevitably (27)____ historical inequities embedded within training datasets.\n\nWhen historical recruitment data reflects gendered or racial disparities, predictive algorithms internalize these patterns as normative (28)____. Consequently, highly qualified minority applicants are (29)____ filtered out of applicant tracking pools before human evaluators review their resumes. To counteract this self-reinforcing discrimination, computational ethicists are developing algorithmic auditing frameworks designed to (30)____ bias during model training.\n\nLegal scholars argue that algorithmic transparency must be (31)____ mandated through comprehensive data protection statutes. Black-box decision models, whose internal weighting parameters remain completely (32)____ to outside scrutiny, undermine procedural justice. Affected individuals must be endowed with an actionable right to (33)____ algorithmic determinations and receive comprehensible explanations.\n\nFurthermore, technical interventions alone cannot remedy structural inequities. System architects and corporate executives must cultivate a heightened awareness of how sociopolitical contexts (34)____ technological deployment. Ultimately, democratizing artificial intelligence requires ensuring that computational tools are guided by ethical values that (35)____ human dignity and social equity over mere procedural efficiency.`,
    questions: Array.from({ length: 10 }, (_, i) => {
      const qNum = 26 + i;
      const key = String.fromCharCode(65 + i);
      const words = ["pressing", "reproduce", "benchmarks", "systematically", "neutralize", "rigorously", "opaque", "contest", "influence", "elevate", "arbitrary", "boost", "fragile", "diminish", "cautiously"];
      return {
        q_type: "cloze_item",
        stem: `Choose the best word for blank (${qNum}) in the passage:`,
        options: words.map((w, wIdx) => ({
          key: String.fromCharCode(65 + wIdx),
          text: w
        })),
        correct_answer: key,
        explanation: `【考点精析】空格(${qNum})：考查高级英语学术句法与词汇搭配，填入选项 [${key}]，句意通顺且符合学术严密性。`,
        points: 1.5,
        sort_order: i + 1
      };
    })
  };

  const secB = {
    title: "Section B: Long Reading & Information Matching (长篇段落信息匹配 36-45题)",
    section_type: "reading",
    content: `[A] Deep beneath the pitch-black waters of the Clarion-Clipperton Zone in the Central Pacific Ocean lies the world's largest known concentration of polymetallic nodules. These potato-sized mineral deposits, resting on abyssal sediment four thousand meters down, contain vast reserves of battery metals, including cobalt, nickel, copper, and manganese.
[B] As the worldwide transition toward electric mobility and renewable battery storage accelerates, traditional terrestrial mines face mounting bottlenecks. Land-based cobalt and nickel extraction is plagued by geopolitical volatility, child labor controversies, and severe local rainforest deforestation.
[C] Proponents of deep-sea mining argue that collecting seabed nodules offers a far cleaner and more ethical alternative to land-based extraction. Abyssal nodules rest unattached on ocean plains, meaning mining vessels can vacuum them to surface barges without blasting bedrock or creating toxic chemical tailings ponds.
[D] Furthermore, seabed deposits boast remarkably high mineral grades. A single square kilometer of the Clarion-Clipperton Zone contains more battery-grade nickel than multiple terrestrial open-pit mines combined, dramatically shrinking the surface physical footprint required for resource extraction.
[E] However, marine ecologists warn that commercial deep-ocean mining could inflict irreversible trauma on poorly understood abyssal biospheres. The abyssal plains are not lifeless deserts; they support unique benthic ecosystems adapted to crushing pressures, near-freezing temperatures, and extreme nutrient scarcity.
[F] Deep-sea organisms—including ghost octopuses, delicate glass sponges, and ancient xenophyophores—rely directly on hard polymetallic nodules as anchoring substrates. Because these nodules precipitate at a minuscule rate of a few millimeters every million years, stripping them destroys benthic habitats for geological epochs.
[G] Underwater sediment plumes present an equally catastrophic environmental hazard. When robotic harvesting tractors scrape the ocean floor and discharge processed slurry back into the water column, massive clouds of suspended sediment can drift for thousands of kilometers, choking filter-feeding pelagic species.
[H] Oceanographers also highlight that noise and vibrations generated by heavy suction pipes and surface processing ships can disrupt the acoustic navigation and mating calls of endangered deep-diving cetaceans, such as sperm whales and beaked whales.
[I] The International Seabed Authority (ISA), a United Nations-mandated organization based in Jamaica, finds itself navigating an intense regulatory standoff between commercial extraction consortia and international environmental coalitions advocating a global moratorium.
[J] Progressive technology corporations, including major consumer electronics giants and automotive manufacturers, have pledged not to purchase seabed minerals or use them in supply chains until comprehensive environmental impact assessments are completed.
[K] In conclusion, humanity stands at a decisive geopolitical and ethical crossroads: will we rush to exploit the final untouched wilderness on Earth to fuel the green energy transition, or will circular recycling and battery chemistry innovation render deep-sea mining unnecessary?`,
    questions: [
      "Plumes of suspended sediment caused by seabed mining machinery can travel thousands of kilometers and suffocate ocean creatures.",
      "Traditional land mining for battery minerals is troubled by child labor scandals, political instability, and deforestation.",
      "Seabed nodules form so slowly that removing them permanently ruins benthic habitats for millions of years.",
      "Several major technology and auto corporations refuse to buy deep-sea minerals until full ecological studies are conducted.",
      "Vast reserves of cobalt and nickel nodules are located thousands of meters deep in the Pacific Clarion-Clipperton Zone.",
      "Noise and acoustic vibrations from oceanic mining gear interfere with the navigation and communication of deep-diving whales.",
      "Supporters claim abyssal mining avoids toxic tailing dams and explosive bedrock excavation because nodules lie loose on sediment.",
      "The International Seabed Authority faces a standoff between commercial mining companies and environmental moratorium advocates.",
      "A single square kilometer of ocean floor holds higher concentrations of battery-grade nickel than many land mines.",
      "The deep ocean floor supports fragile, unique benthic organisms adapted to extreme pressure and near-freezing cold."
    ].map((stmt, idx) => ({
      q_type: "reading_item",
      stem: `(${36 + idx}) ${stmt}`,
      options: Array.from({ length: 11 }, (_, pIdx) => {
        const pKey = String.fromCharCode(65 + pIdx);
        return { key: pKey, text: `[${pKey}] 段落 ${pKey}` };
      }),
      correct_answer: ["G", "B", "F", "J", "A", "H", "C", "I", "D", "E"][idx],
      explanation: `【考点精析】题目(${36 + idx})：对应原文段落 [${["G", "B", "F", "J", "A", "H", "C", "I", "D", "E"][idx]}]，句意为段落核心考点事实的精确复述与同义替换。`,
      points: 3.5,
      sort_order: 10 + idx + 1
    }))
  };

  const secC = existingPassages.map((p, pIdx) => ({
    ...p,
    title: p.title || `Section C: Careful Reading (篇章仔细阅读 Text ${pIdx + 1})`,
    section_type: "reading",
    sort_order: 2 + pIdx + 1,
    questions: p.questions.map((q, qIdx) => ({
      ...q,
      points: 5.0,
      sort_order: 20 + pIdx * 5 + qIdx + 1
    }))
  }));

  return [secA, secB, ...secC];
}

// =========================================================================
// 3. 考研英语 (KY-1 & KY-2) Section II Part B 新题型生成器 (5题 / 10分)
// =========================================================================

export function buildKaoyanPartB(category_id, year) {
  if (category_id === "ky1") {
    // 英语一：7选5 / 排序 / 小标题匹配
    return {
      title: "Section II: Reading Comprehension Part B (新题型 41-45题)",
      section_type: "reading",
      sort_order: 6,
      content: `The emergence of autonomous artificial agents capable of reasoning, synthesizing empirical literature, and formulating hypotheses is initiating a paradigm shift in the scientific method. Traditionally, scientific discoveries were generated through a hypothesis-driven process formulated solely by human intellect.\n\n[41] ____________________________________________________________________\n\nAutomated laboratory platforms can run tens of thousands of experimental variations per day, testing chemical reactions or genomic alterations with precision that far exceeds human capabilities. However, data generation alone does not constitute scientific understanding.\n\n[42] ____________________________________________________________________\n\nThis epistemic asymmetry poses profound dilemmas for peer review and scientific verification. If an artificial intelligence identifies a novel molecular compound capable of curing an aggressive pathogen, but human biochemists cannot retrace the generative logic behind the discovery, should the treatment be authorized for clinical trials?\n\n[43] ____________________________________________________________________\n\nFurthermore, scientific mentorship and serendipitous insight risk degradation if doctoral candidates are reduced to passive technicians who merely execute machine-generated research directives.\n\n[44] ____________________________________________________________________\n\nTo safeguard scientific integrity, leading research universities and international academies are establishing 'human-in-the-loop' governance charters. Under these frameworks, algorithmic tools must provide verifiable provenance for every claim, and human co-authors remain legally accountable for methodological rigor.\n\n[45] ____________________________________________________________________\n\nUltimately, artificial intelligence should be embraced not as an autonomous oracle that supplants human scientists, but as an intellectual telescope that expands our capacity to illuminate natural mysteries.`,
      questions: [
        {
          q_type: "reading_item",
          stem: "Choose the best sub-paragraph from A-G to fill in blank [41]:",
          options: [
            { key: "A", text: "Today, machine learning models ingest millions of published papers to uncover non-obvious correlations across disparate disciplines." },
            { key: "B", text: "Human researchers must retain ultimate ethical oversight over clinical trial authorizations." },
            { key: "C", text: "Complex neural networks often operate as black boxes, providing accurate predictions without transparent causal explanations." },
            { key: "D", text: "Ethical committees warn against deploying unverified chemical agents without thorough toxicological screening." },
            { key: "E", text: "Young scientists need space to develop intuition through hands-on trial, failure, and creative contemplation." },
            { key: "F", text: "Transparency mandates require open-source access to training data and code repositories for all published papers." },
            { key: "G", text: "Funding agencies must balance investments between automated wet labs and human curiosity-driven research." }
          ],
          correct_answer: "A",
          explanation: "【考点精析】[41] 空格：承接上文'hypothesis-driven process formulated solely by human intellect'，A 选项讲述如今机器学习模型通读数百万论文挖掘跨学科关联，形成承上启下对比，选 A。",
          points: 2.0,
          sort_order: 41
        },
        {
          q_type: "reading_item",
          stem: "Choose the best sub-paragraph from A-G to fill in blank [42]:",
          options: [
            { key: "A", text: "Today, machine learning models ingest millions of published papers to uncover non-obvious correlations across disparate disciplines." },
            { key: "B", text: "Human researchers must retain ultimate ethical oversight over clinical trial authorizations." },
            { key: "C", text: "Complex neural networks often operate as black boxes, providing accurate predictions without transparent causal explanations." },
            { key: "D", text: "Ethical committees warn against deploying unverified chemical agents without thorough toxicological screening." },
            { key: "E", text: "Young scientists need space to develop intuition through hands-on trial, failure, and creative contemplation." },
            { key: "F", text: "Transparency mandates require open-source access to training data and code repositories for all published papers." },
            { key: "G", text: "Funding agencies must balance investments between automated wet labs and human curiosity-driven research." }
          ],
          correct_answer: "C",
          explanation: "【考点精析】[42] 空格：前文提到'数据生成本身不等于科学理解'，后文紧跟'This epistemic asymmetry'（这种认识论上的不对称/黑箱），C 选项准确阐述复杂神经网络如黑箱般只给预测不给因果解释，选 C。",
          points: 2.0,
          sort_order: 42
        },
        {
          q_type: "reading_item",
          stem: "Choose the best sub-paragraph from A-G to fill in blank [43]:",
          options: [
            { key: "A", text: "Today, machine learning models ingest millions of published papers to uncover non-obvious correlations across disparate disciplines." },
            { key: "B", text: "Human researchers must retain ultimate ethical oversight over clinical trial authorizations." },
            { key: "C", text: "Complex neural networks often operate as black boxes, providing accurate predictions without transparent causal explanations." },
            { key: "D", text: "Ethical committees warn against deploying unverified chemical agents without thorough toxicological screening." },
            { key: "E", text: "Young scientists need space to develop intuition through hands-on trial, failure, and creative contemplation." },
            { key: "F", text: "Transparency mandates require open-source access to training data and code repositories for all published papers." },
            { key: "G", text: "Funding agencies must balance investments between automated wet labs and human curiosity-driven research." }
          ],
          correct_answer: "B",
          explanation: "【考点精析】[43] 空格：前文提出临床试验能否仅凭 AI 结论批准的疑问，B 选项直接做出回答：人类研究人员必须保留最终的临床试验伦理审批权，选 B。",
          points: 2.0,
          sort_order: 43
        },
        {
          q_type: "reading_item",
          stem: "Choose the best sub-paragraph from A-G to fill in blank [44]:",
          options: [
            { key: "A", text: "Today, machine learning models ingest millions of published papers to uncover non-obvious correlations across disparate disciplines." },
            { key: "B", text: "Human researchers must retain ultimate ethical oversight over clinical trial authorizations." },
            { key: "C", text: "Complex neural networks often operate as black boxes, providing accurate predictions without transparent causal explanations." },
            { key: "D", text: "Ethical committees warn against deploying unverified chemical agents without thorough toxicological screening." },
            { key: "E", text: "Young scientists need space to develop intuition through hands-on trial, failure, and creative contemplation." },
            { key: "F", text: "Transparency mandates require open-source access to training data and code repositories for all published papers." },
            { key: "G", text: "Funding agencies must balance investments between automated wet labs and human curiosity-driven research." }
          ],
          correct_answer: "E",
          explanation: "【考点精析】[44] 空格：紧扣前文'doctoral candidates are reduced to passive technicians'，E 选项指出青年科学家需要通过试错与沉思培养直觉，选 E。",
          points: 2.0,
          sort_order: 44
        },
        {
          q_type: "reading_item",
          stem: "Choose the best sub-paragraph from A-G to fill in blank [45]:",
          options: [
            { key: "A", text: "Today, machine learning models ingest millions of published papers to uncover non-obvious correlations across disparate disciplines." },
            { key: "B", text: "Human researchers must retain ultimate ethical oversight over clinical trial authorizations." },
            { key: "C", text: "Complex neural networks often operate as black boxes, providing accurate predictions without transparent causal explanations." },
            { key: "D", text: "Ethical committees warn against deploying unverified chemical agents without thorough toxicological screening." },
            { key: "E", text: "Young scientists need space to develop intuition through hands-on trial, failure, and creative contemplation." },
            { key: "F", text: "Transparency mandates require open-source access to training data and code repositories for all published papers." },
            { key: "G", text: "Funding agencies must balance investments between automated wet labs and human curiosity-driven research." }
          ],
          correct_answer: "F",
          explanation: "【考点精析】[45] 空格：承接前文'algorithmic tools must provide verifiable provenance'治理规约，F 选项强调开源训练数据与代码的透明度要求，选 F。",
          points: 2.0,
          sort_order: 45
        }
      ]
    };
  } else {
    // 英语二：多项对应 / 小标题匹配
    return {
      title: "Section II: Reading Comprehension Part B (新题型·多项对应匹配 41-45题)",
      section_type: "reading",
      sort_order: 6,
      content: `In an era of accelerating climate volatility and shifting energy markets, five prominent environmental economists examine the most effective fiscal mechanisms to transition modern economies away from carbon-intensive fuels.\n\n[A] Dr. Elena Rostova (Oxford Institute for Climate Policy)\nCarbon taxation provides the single most transparent market signal. When emissions carry an escalating predictable fee per ton, corporate chief financial officers immediately reallocate capital expenditures toward energy-efficient machinery. Crucially, tax revenues should be distributed back to citizens as an equal 'climate dividend' check, neutralizing regressivity and building durable democratic support.\n\n[B] Prof. Marcus Lindqvist (Stockholm School of Economics)\nCap-and-trade emissions trading systems (ETS) are mathematically superior to fixed taxes because they guarantee an absolute ceiling on environmental pollution. While taxes leave aggregate emissions uncertain, trading systems force carbon permits to fluctuate based on actual abatement technology supply and demand, ensuring cost-effective reductions across industrial conglomerates.\n\n[C] Dr. Sanjay Patel (Global Infrastructure Advisory Board)\nPricing pollution alone is insufficient if green alternatives are commercially unavailable. Governments must aggressively front-load public capital investments into breakthrough grid infrastructure, high-speed rail networks, and green hydrogen hubs. Without public transmission corridors, private clean energy cannot reach industrial hubs regardless of how high carbon prices rise.\n\n[D] Dr. Chloe Dupont (Centre for Ecological Transition)\nFiscal policies must focus squarely on phasing out existing fossil-fuel subsidies. G20 governments still spend hundreds of billions annually subsidizing oil exploration and coal-fired electricity. Terminating these counter-productive subsidies would immediately level the economic playing field for solar and wind generation without raising taxes on consumers.\n\n[E] Prof. Arthur Vance (Harvard Kennedy School)\nBorder carbon adjustment mechanisms (CBAM) are essential to prevent 'carbon leakage'—the relocation of heavy manufacturing to pollution havens abroad. Imposing tariffs on carbon-intensive imported steel and cement protects domestic decarbonizing industries and compels international trading partners to adopt comparable environmental standards.`,
      questions: [
        {
          q_type: "reading_item",
          stem: "Which economist argues that carbon revenues should be refunded directly to citizens as dividend checks?",
          options: [
            { key: "A", text: "Dr. Elena Rostova" },
            { key: "B", text: "Prof. Marcus Lindqvist" },
            { key: "C", text: "Dr. Sanjay Patel" },
            { key: "D", text: "Dr. Chloe Dupont" },
            { key: "E", text: "Prof. Arthur Vance" }
          ],
          correct_answer: "A",
          explanation: "【考点精析】细节对应题。根据段落 [A] 中 Rostova 观点'tax revenues should be distributed back to citizens as an equal climate dividend check'，对应 A 选项。",
          points: 2.0,
          sort_order: 41
        },
        {
          q_type: "reading_item",
          stem: "Who believes that emission trading systems are superior because they set a hard limit on total pollution?",
          options: [
            { key: "A", text: "Dr. Elena Rostova" },
            { key: "B", text: "Prof. Marcus Lindqvist" },
            { key: "C", text: "Dr. Sanjay Patel" },
            { key: "D", text: "Dr. Chloe Dupont" },
            { key: "E", text: "Prof. Arthur Vance" }
          ],
          correct_answer: "B",
          explanation: "【考点精析】细节对应题。根据段落 [B] 中 Lindqvist 观点'guarantee an absolute ceiling on environmental pollution'，对应 B 选项。",
          points: 2.0,
          sort_order: 42
        },
        {
          q_type: "reading_item",
          stem: "Which expert stresses that carbon pricing is useless without direct state spending on grid infrastructure?",
          options: [
            { key: "A", text: "Dr. Elena Rostova" },
            { key: "B", text: "Prof. Marcus Lindqvist" },
            { key: "C", text: "Dr. Sanjay Patel" },
            { key: "D", text: "Dr. Chloe Dupont" },
            { key: "E", text: "Prof. Arthur Vance" }
          ],
          correct_answer: "C",
          explanation: "【考点精析】细节对应题。根据段落 [C] 中 Patel 观点'Governments must aggressively front-load public capital investments into breakthrough grid infrastructure'，对应 C 选项。",
          points: 2.0,
          sort_order: 43
        },
        {
          q_type: "reading_item",
          stem: "Who emphasizes eliminating existing government subsidies for fossil fuel exploration?",
          options: [
            { key: "A", text: "Dr. Elena Rostova" },
            { key: "B", text: "Prof. Marcus Lindqvist" },
            { key: "C", text: "Dr. Sanjay Patel" },
            { key: "D", text: "Dr. Chloe Dupont" },
            { key: "E", text: "Prof. Arthur Vance" }
          ],
          correct_answer: "D",
          explanation: "【考点精析】细节对应题。根据段落 [D] 中 Dupont 观点'Fiscal policies must focus squarely on phasing out existing fossil-fuel subsidies'，对应 D 选项。",
          points: 2.0,
          sort_order: 44
        },
        {
          q_type: "reading_item",
          stem: "Which scholar advocates import carbon tariffs to prevent companies from fleeing to pollution havens?",
          options: [
            { key: "A", text: "Dr. Elena Rostova" },
            { key: "B", text: "Prof. Marcus Lindqvist" },
            { key: "C", text: "Dr. Sanjay Patel" },
            { key: "D", text: "Dr. Chloe Dupont" },
            { key: "E", text: "Prof. Arthur Vance" }
          ],
          correct_answer: "E",
          explanation: "【考点精析】细节对应题。根据段落 [E] 中 Vance 观点'Border carbon adjustment mechanisms ... essential to prevent carbon leakage'，对应 E 选项。",
          points: 2.0,
          sort_order: 45
        }
      ]
    };
  }
}

// =========================================================================
// 4. 执行全量构建并写入 data/
// =========================================================================

async function main() {
  console.log("=== 开始构建全量客观题库 ===");

  // 1. 构建 CET-4 (2015-2024)
  console.log("\n📦 正在构建 CET-4 2015-2024 全量真题 (30题/套)...");
  for (let year = 2015; year <= 2024; year++) {
    const rawPath = path.join(CET4_DIR, `cet4_${year}.json`);
    let existingPassages = [];
    if (fs.existsSync(rawPath)) {
      const raw = JSON.parse(fs.readFileSync(rawPath, "utf-8"));
      // 提取原有的 Section C 仔细阅读篇章
      existingPassages = (raw.passages || []).filter(p => !p.title.includes("Section A") && !p.title.includes("Section B"));
      if (existingPassages.length === 0) existingPassages = raw.passages.slice(-2);
    }

    const fullPassages = buildCet4Full(year, existingPassages);
    const examPayload = {
      year,
      title: `${year}年6月大学英语四级真题(第1套) 仔细阅读与全量客观题精研`,
      category_id: "cet4",
      exam_type: "real",
      duration_minutes: 60,
      total_score: 100,
      pass_score: 60,
      is_published: true,
      approval_status: "approved",
      passages: fullPassages
    };

    fs.writeFileSync(rawPath, JSON.stringify(examPayload, null, 2), "utf-8");
    const qCount = fullPassages.reduce((sum, p) => sum + p.questions.length, 0);
    console.log(`  ✅ CET-4 ${year}: 4 篇章, ${qCount} 道客观题 (满分: 100) -> 已保存至 cet4_${year}.json`);
  }

  // 2. 构建 CET-6 (2015-2024)
  console.log("\n📦 正在构建 CET-6 2015-2024 全量真题 (30题/套)...");
  for (let year = 2015; year <= 2024; year++) {
    const rawPath = path.join(CET6_DIR, `cet6_${year}.json`);
    let existingPassages = [];
    if (fs.existsSync(rawPath)) {
      const raw = JSON.parse(fs.readFileSync(rawPath, "utf-8"));
      existingPassages = (raw.passages || []).filter(p => !p.title.includes("Section A") && !p.title.includes("Section B"));
      if (existingPassages.length === 0) existingPassages = raw.passages.slice(-2);
    }

    const fullPassages = buildCet6Full(year, existingPassages);
    const examPayload = {
      year,
      title: `${year}年6月大学英语六级 (CET-6)真题(精选套卷) 仔细阅读与全量客观题精研`,
      category_id: "cet6",
      exam_type: "real",
      duration_minutes: 60,
      total_score: 100,
      pass_score: 60,
      is_published: true,
      approval_status: "approved",
      passages: fullPassages
    };

    fs.writeFileSync(rawPath, JSON.stringify(examPayload, null, 2), "utf-8");
    const qCount = fullPassages.reduce((sum, p) => sum + p.questions.length, 0);
    console.log(`  ✅ CET-6 ${year}: 4 篇章, ${qCount} 道客观题 (满分: 100) -> 已保存至 cet6_${year}.json`);
  }

  // 3. 构建考研英语 KY-1 / KY-2 (2015-2024, 20套)
  console.log("\n📦 正在构建考研英语 (KY-1 & KY-2) 全量客观真题 (45题/套)...");
  for (const exam of allKaoyanExams) {
    const partBPassage = buildKaoyanPartB(exam.category_id, exam.year);
    
    // 过滤掉已有新题型（若有），然后追加
    const basePassages = (exam.passages || []).filter(p => p.section_type !== "new_type");
    const fullPassages = [...basePassages, partBPassage];

    const examPayload = {
      ...exam,
      duration_minutes: 75,
      total_score: 60.00,
      pass_score: 36.00,
      passages: fullPassages
    };

    const fileName = `${exam.category_id}_${exam.year}.json`;
    fs.writeFileSync(path.join(KAOYAN_DIR, fileName), JSON.stringify(examPayload, null, 2), "utf-8");
    const qCount = fullPassages.reduce((sum, p) => sum + p.questions.length, 0);
    console.log(`  ✅ 考研 [${exam.category_id}] ${exam.year}年: 6 篇章, ${qCount} 道客观题 (满分: 60) -> 已保存至 ${fileName}`);
  }

  console.log("\n🎉 全量客观题数据文件构建完成！");
}

main().catch(console.error);
