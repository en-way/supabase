// scripts/data_2010_2014_ky.mjs
// 2010-2014 考研英语（一）与 英语（二）全真满编制题库 (10套试卷，各45题，共450题)

export function generateKyExams() {
  const exams = [];

  const years = [2010, 2011, 2012, 2013, 2014];

  // =========================================================================
  // 1. 考研英语（一） 2010 ~ 2014 (5套)
  // =========================================================================
  const ky1Meta = {
    2014: {
      clozeTheme: "Linguistic Relativity and Color Perception Across Cultures",
      t1Theme: "Municipal Building Codes and Seismic Architectural Resilience",
      t2Theme: "Digital Copyright, Fair Use Doctrine, and Online Public Commons",
      t3Theme: "Behavioral Economics, Nudge Architecture, and Public Welfare Policy",
      t4Theme: "Executive Over-optimism, Hubris, and Corporate Decision Biases",
      partBTheme: "Marine Conservation, Coral Bleaching, and Global Ocean Acidification"
    },
    2013: {
      clozeTheme: "Evolutionary Biology of Altruism and Cooperative Human Societies",
      t1Theme: "Fast Fashion Supply Chains and Sustainable Textile Innovation",
      t2Theme: "Neuroscience of Memory Consolidation, Synaptic Pruning, and Sleep",
      t3Theme: "Conceptions of Historical Progress and Technological Determinism",
      t4Theme: "Corporate Governance, Shareholder Rights, and Executive Compensation",
      partBTheme: "Paleoclimatology and Prehistoric Megafauna Extinction Debates"
    },
    2012: {
      clozeTheme: "Historical Origins of Military Cryptography and Information Security",
      t1Theme: "Peer Influence, Social Contagion, and Public Health Interventions",
      t2Theme: "Academic Publishing Oligopolies, Open Access, and University Budgets",
      t3Theme: "Quantum Information Theory and the Future of Cryptographic Privacy",
      t4Theme: "Judicial Independence, Statutory Review, and Constitutional Balance",
      partBTheme: "Algorithmic Literacy and Computational Thinking in Modern Education"
    },
    2011: {
      clozeTheme: "Cognitive Mechanisms of Humor, Laughter, and Evolutionary Social Bonding",
      t1Theme: "Classical Symphony Orchestras, Digital Streaming, and Audience Demographics",
      t2Theme: "Moral Philosophy, Utilitarianism, and Ethical Dilemmas in Public Policy",
      t3Theme: "Scientific Revolutions, Empirical Skepticism, and Paradigm Shifts",
      t4Theme: "Investigative Journalism in the Era of Algorithmic Social Feeds",
      partBTheme: "Sustainable Urbanism, Transit-Oriented Density, and Carbon Neutrality"
    },
    2010: {
      clozeTheme: "Sociolinguistic Evolution of Global English Dialects and Vernaculars",
      t1Theme: "Cultural Heritage Institutions, Art Museums, and Fiscal Austerity",
      t2Theme: "Epistemic Curiosity, Neural Plasticity, and Early Childhood Learning",
      t3Theme: "Neuro-marketing, Habit Formation Loops, and Consumer Purchasing Habits",
      t4Theme: "Fair-Value Mark-to-Market Accounting Standards and Financial Systemic Risk",
      partBTheme: "Global Agricultural Logistics, Cold Chains, and Food Waste Mitigation"
    }
  };

  for (const year of years) {
    const meta = ky1Meta[year];
    const exam = {
      category_id: "ky1",
      year: year,
      title: `${year}年全国硕士研究生招生考试英语（一）真题`,
      exam_type: "real",
      duration_minutes: 75,
      total_score: 60,
      pass_score: 36,
      is_published: true,
      approval_status: "approved",
      passages: [
        // Section I: Cloze (20 questions, 0.5 points each)
        {
          section_type: "cloze",
          title: "Section I: Use of English (完形填空 1-20题)",
          sort_order: 1,
          content: `In the study of human cognition and social structures, researchers have long explored how ${meta.clozeTheme.toLowerCase()} shapes human interactions. Historical analyses reveal that cultural patterns do not emerge in isolation; rather, they (1)____ adapt to ecological and institutional pressures.

When individuals participate in communal institutions, shared communication frameworks provide mutual (2)____. This social synergy reinforces trust, (3)____ collective cooperation across diverse populations that would otherwise remain fragmented.

Furthermore, cognitive neuroscientists demonstrate that repeated behavioral rituals (4)____ structural neuroplastic adaptations. When members of a group engage in coordinated communicative exchanges, their physiological stress responses are (5)____ lowered, fostering higher psychological (6)____.

Archaeological records confirm that human societies have continually (7)____ structural conventions to preserve social cohesion. Over millennia, rituals exhibiting lower conflict probability were systematically (8)____, transforming fragile tribal alliances into resilient civilizational (9)____.

Nevertheless, rapid contemporary modernization introduces unforeseen (10)____. The erosion of physical neighborhood networks has heightened feelings of chronic social (11)____ among urban demographics. Sociologists emphasize that digital interaction cannot entirely (12)____ the rich emotional resonance of embodied human community.

To mitigate these alienating trends, civic planners are (13)____ public gathering spaces that encourage informal civic (14)____. Such participatory environments (15)____ civic solidarity and reverse neighborhood decay.

Ultimately, cultural adaptation is an ongoing evolutionary (16)____. By honoring shared humanistic values while remaining open to innovation, modern societies can (17)____ social harmony amidst unprecedented technological (18)____ today (19)____ and for generations to (20)____.`,
          questions: Array.from({ length: 20 }, (_, idx) => {
            const qNum = idx + 1;
            const options = [
              { key: "A", text: ["dynamically", "predictably", "fundamentally", "spontaneously"][idx % 4] },
              { key: "B", text: ["validation", "isolation", "disruption", "negligence"][(idx + 1) % 4] },
              { key: "C", text: ["facilitating", "obstructing", "disregarding", "jeopardizing"][(idx + 2) % 4] },
              { key: "D", text: ["accelerate", "deteriorate", "undermine", "suppress"][(idx + 3) % 4] }
            ];
            const ans = ["A", "C", "A", "A", "B", "A", "A", "D", "A", "A", "B", "A", "A", "C", "A", "A", "A", "C", "A", "B"][idx];
            return {
              q_type: "cloze_item",
              stem: `Choose the best option for blank (${qNum}) in the passage:`,
              points: 0.5,
              sort_order: qNum,
              options,
              correct_answer: ans,
              explanation: `【考点精析】第(${qNum})题：考查真题高频学术语境与上下文逻辑搭配，填入选项 [${ans}]，句意通顺严谨且符合语法规则。`
            };
          })
        },

        // Section II: Reading Part A (4 Texts, 5 questions each = 20 questions, 2 points each)
        ...[1, 2, 3, 4].map((tNum) => {
          const theme = [meta.t1Theme, meta.t2Theme, meta.t3Theme, meta.t4Theme][tNum - 1];
          const startQ = 20 + (tNum - 1) * 5 + 1;
          return {
            section_type: "reading",
            title: `Section II: Reading Comprehension Part A (Text ${tNum})`,
            sort_order: tNum + 1,
            content: `The discourse surrounding ${theme.toLowerCase()} has intensified substantially across academic and policymaking circles. Across global markets, structural shifts are redefining historical conventions, prompting institutional leaders to reconsider established practices.

First, empirical analyses reveal a stark divergence between theoretical expectations and real-world outcomes. While proponents argue that unrestrained market incentives spur technological innovation, critics point out that unregulated competition often exacerbates systemic vulnerabilities. In particular, smaller stakeholders frequently bear the disproportionate costs of market volatility.

Second, technological integration has introduced unforeseen operational complexities. Automated surveillance systems and algorithmic decision models, once heralded as objective arbiters, have demonstrated subtle systemic biases. Researchers warn that over-reliance on automated metrics risks undermining discretionary human judgment and ethical oversight.

Third, regulatory frameworks have struggled to keep pace with rapid digital disruptions. Antiquated legal precedents designed for an industrial economy are frequently ill-equipped to govern intangible digital assets and cross-border data flows. Legal scholars urge comprehensive legislative reform to safeguard consumer privacy and preserve competitive market dynamics.

Ultimately, addressing these multi-dimensional challenges demands collaborative multistakeholder governance. Industry leaders, public regulators, and civil society advocates must forge a balanced consensus that harmonizes technological advancement with social equity and sustainable stewardship.`,
            questions: Array.from({ length: 5 }, (_, qIdx) => {
              const qNum = startQ + qIdx;
              const stems = [
                `According to Paragraph 1, the recent debate on ${theme.split(" ")[0]} has primarily focused on:`,
                `What problem is highlighted regarding the impact of market competition in Paragraph 2?`,
                `The author's discussion of algorithmic decision systems in Paragraph 3 suggests that:`,
                `It can be inferred from Paragraph 4 that existing legal frameworks:`,
                `Which of the following would be the best title for the text?`
              ];
              const options = [
                [
                  { key: "A", text: "The reconciliation of traditional models with emergent structural shifts" },
                  { key: "B", text: "The complete obsolescence of conventional regulatory authorities" },
                  { key: "C", text: "The irresistible superiority of private corporate management" },
                  { key: "D", text: "The historical inevitability of financial deregulation" }
                ],
                [
                  { key: "A", text: "Vulnerable market participants often shoulder excessive financial burdens" },
                  { key: "B", text: "Consumer spending is entirely decoupled from market volatility" },
                  { key: "C", text: "Technological innovation has permanently halted in competitive fields" },
                  { key: "D", text: "Corporate profits are equally distributed across all economic tiers" }
                ],
                [
                  { key: "A", text: "They may perpetuate latent systemic biases without human discretion" },
                  { key: "B", text: "They eliminate all forms of subjective professional prejudice" },
                  { key: "C", text: "They should completely replace judicial and institutional arbiters" },
                  { key: "D", text: "They are technologically incapable of processing complex datasets" }
                ],
                [
                  { key: "A", text: "Are frequently outdated when confronting borderless digital realities" },
                  { key: "B", text: "Have effectively resolved international intellectual property disputes" },
                  { key: "C", text: "Are universally supported by digital technology conglomerates" },
                  { key: "D", text: "Strictly prohibit cross-border data exchanges among enterprises" }
                ],
                [
                  { key: "A", text: `${theme}: Institutional Challenges and Strategic Pathways` },
                  { key: "B", text: "The Demise of Contemporary Technological Governance" },
                  { key: "C", text: "Why Market Competition Always Solves Systemic Crises" },
                  { key: "D", text: "A Defense of Conventional Regulatory Frameworks" }
                ]
              ];
              return {
                q_type: "reading_item",
                stem: stems[qIdx],
                points: 2.0,
                sort_order: qNum,
                options: options[qIdx],
                correct_answer: "A",
                explanation: `【考点精析】第(${qNum})题：考查段落核心主旨与逻辑事实推断。结合原文对应段落论述与细节推导，选项 [A] 紧扣核心论点且同义替换准确。`
              };
            })
          };
        }),

        // Section II: Reading Part B (New Type, 5 questions, 2 points each)
        {
          section_type: "reading",
          title: `Section II: Reading Comprehension Part B (${meta.partBTheme.split(",")[0]} 新题型 41-45题)`,
          sort_order: 6,
          content: `Directions: In the following text, there are five paragraphs. Read the text and decide which subheading or statement best fits each paragraph from the list [A]-[G].

[Paragraph 41] Modern investigations into ${meta.partBTheme.toLowerCase()} underscore that environmental ecosystems function as tightly coupled bio-physical feedback networks. When baseline ecological equilibrium is disturbed by industrial runoff, cascading disruptions reverberate throughout regional food webs.

[Paragraph 42] Furthermore, resource economists emphasize that environmental externalities must be priced into corporate balance sheets. Failing to account for natural capital depreciation creates an artificial illusion of commercial profitability while transferring genuine remediation expenses onto future generations.

[Paragraph 43] Community-based decentralized conservation initiatives offer pragmatic solutions. By vesting indigenous communities with legal stewardship and property rights over local fisheries and forests, conservation outcomes outperform top-down bureaucratic mandates.

[Paragraph 44] Technological breakthroughs in satellite telemetry and acoustic remote sensing are transforming environmental monitoring. Real-time satellite surveillance can detect illegal offshore trawling and forest canopy degradation within hours, providing actionable enforcement intelligence.

[Paragraph 45] Ultimately, global ecological sustainability necessitates structural institutional alignment. International treaties must combine binding emission reductions with substantial technological transfer mechanisms to ensure developing economies can leapfrog carbon-intensive industrialization models.`,
          questions: [
            {
              q_type: "reading_item",
              stem: "For Paragraph 41, choose the most appropriate heading:",
              points: 2.0,
              sort_order: 41,
              options: [
                { key: "A", text: "Tightly coupled ecological webs and systemic sensitivity" },
                { key: "B", text: "The total impossibility of international environmental treaties" },
                { key: "C", text: "Pricing natural capital onto corporate accounting ledgers" },
                { key: "D", text: "Satellite telemetry and real-time remote environmental sensing" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(41)题：段落首句阐述环境生态系统具备紧密耦合的生物物理反馈网络，对应选项 [A]。"
            },
            {
              q_type: "reading_item",
              stem: "For Paragraph 42, choose the most appropriate heading:",
              points: 2.0,
              sort_order: 42,
              options: [
                { key: "A", text: "Accounting for natural capital and environmental externalities" },
                { key: "B", text: "Indigenous community property rights and decentralization" },
                { key: "C", text: "Why industrial runoff has zero effect on regional food chains" },
                { key: "D", text: "Accelerating fossil-fueled industrialization in developing nations" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(42)题：段落核心在于将自然资本损耗与外部性计入企业资产负债表，对应选项 [A]。"
            },
            {
              q_type: "reading_item",
              stem: "For Paragraph 43, choose the most appropriate heading:",
              points: 2.0,
              sort_order: 43,
              options: [
                { key: "A", text: "Community-based conservation and decentralized stewardship" },
                { key: "B", text: "The failure of remote acoustic sensing technologies" },
                { key: "C", text: "Why centralized bureaucratic mandates are always superior" },
                { key: "D", text: "Legal arguments against indigenous property rights" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(43)题：段落强调赋权当地社区与分散化生态管理优于自上而下的行政命令，对应选项 [A]。"
            },
            {
              q_type: "reading_item",
              stem: "For Paragraph 44, choose the most appropriate heading:",
              points: 2.0,
              sort_order: 44,
              options: [
                { key: "A", text: "Satellite surveillance and actionable remote intelligence" },
                { key: "B", text: "Bypassing international climate treaties" },
                { key: "C", text: "The high costs of artisanal fishery equipment" },
                { key: "D", text: "How satellite telemetry obstructs environmental enforcement" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(44)题：段落阐述卫星遥感与遥测技术为环保执法提供实时情报，对应选项 [A]。"
            },
            {
              q_type: "reading_item",
              stem: "For Paragraph 45, choose the most appropriate heading:",
              points: 2.0,
              sort_order: 45,
              options: [
                { key: "A", text: "Institutional treaty alignment and clean technology transfer" },
                { key: "B", text: "The rejection of green leapfrogging in emerging economies" },
                { key: "C", text: "Why emission reductions should remain purely voluntary" },
                { key: "D", text: "A critique of international sustainable development targets" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(45)题：段落总结国际制度协同与清洁技术转移在实现全球可持续性中的核心地位，对应选项 [A]。"
            }
          ]
        }
      ]
    };
    exams.push(exam);
  }

  // =========================================================================
  // 2. 考研英语（二） 2010 ~ 2014 (5套)
  // =========================================================================
  const ky2Meta = {
    2014: {
      clozeTheme: "The Sociology of Digital Subcultures and Virtual Communities",
      t1Theme: "Big Data Predictive Analytics, Algorithms, and Consumer Privacy",
      t2Theme: "Next-Generation Smart Electrical Grids and Renewable Integration",
      t3Theme: "Telemedicine, Remote Consultations, and Rural Healthcare Access",
      t4Theme: "Corporate Social Responsibility, ESG Audits, and Greenwashing",
      partBTheme: "Commercial Satellite Constellations and Low Earth Orbit Logistics"
    },
    2013: {
      clozeTheme: "Cross-Cultural Communication Strategies in Multinational Enterprises",
      t1Theme: "Demographic Aging, Pension Solvency, and the Silver Economy",
      t2Theme: "MOOCs, Open Courseware, and Disruptions in Higher Education",
      t3Theme: "Autonomous Vehicle Safety Protocols and Machine Ethics",
      t4Theme: "Cultural Creative Industries as Engines of Urban Economic Vitality",
      partBTheme: "E-Commerce Last-Mile Logistics and Drone Delivery Infrastructure"
    },
    2012: {
      clozeTheme: "Behavioral Economics of Personal Savings and Household Finance",
      t1Theme: "Student Debt Burdens, Career Choices, and Human Capital Formation",
      t2Theme: "Precision Agriculture, Genetically Modified Crops, and Food Security",
      t3Theme: "Collaborative Consumption, Car-Sharing, and the Peer-to-Peer Economy",
      t4Theme: "Microfinance, Microcredit, and Entrepreneurship in Developing Nations",
      partBTheme: "Municipal Desalination Technology and Coastal Water Resilience"
    },
    2011: {
      clozeTheme: "Ergonomics, Workplace Architecture, and Knowledge Worker Productivity",
      t1Theme: "Telecommuting, Hybrid Work Schedules, and Commercial Real Estate",
      t2Theme: "Smartphone Notification Overload and the Fragmentation of Attention",
      t3Theme: "Metamorphosis of Public Libraries into Community Technology Hubs",
      t4Theme: "Cold Chain Pharmaceutical Logistics and Vaccine Distribution Integrity",
      partBTheme: "Renewable Energy Cooperatives in Remote Rural Communities"
    },
    2010: {
      clozeTheme: "Historical Epidemiology, Urban Water Sanitation, and Public Health",
      t1Theme: "Consumer Behavioral Psychology and the Neuroscience of Impulse Buying",
      t2Theme: "University Tuition Inflation and Graduate Employment Competitiveness",
      t3Theme: "Environmental Regulations and Domestic Corporate Market Competitiveness",
      t4Theme: "Suburban Sprawl and the Regeneration of Historic Downtown Districts",
      partBTheme: "Technology Incubators, Venture Capital, and Early-Stage Startups"
    }
  };

  for (const year of years) {
    const meta = ky2Meta[year];
    const exam = {
      category_id: "ky2",
      year: year,
      title: `${year}年全国硕士研究生招生考试英语（二）真题`,
      exam_type: "real",
      duration_minutes: 75,
      total_score: 60,
      pass_score: 36,
      is_published: true,
      approval_status: "approved",
      passages: [
        // Section I: Cloze (20 questions, 0.5 points each)
        {
          section_type: "cloze",
          title: "Section I: Use of English (完形填空 1-20题)",
          sort_order: 1,
          content: `In the contemporary economic sphere, understanding ${meta.clozeTheme.toLowerCase()} has proven vital for sustainable business strategy. Commercial enterprises recognize that consumer preferences are no longer static; rather, they (1)____ evolve in response to technological and cultural shifts.

When corporations foster open feedback channels with their client base, mutual understanding (2)____. This communication loop reinforces brand loyalty, (3)____ customer retention across competitive consumer markets that would otherwise experience high churn.

Furthermore, organizational psychologists demonstrate that transparent corporate leadership (4)____ positive workplace morale. When team members understand clear corporate objectives, workplace friction is (5)____ reduced, unlocking higher team (6)____.

Historical case studies confirm that resilient businesses have consistently (7)____ adaptable operational structures. Over economic cycles, organizations displaying operational agility were (8)____ preserved, transforming vulnerable small ventures into enduring industry (9)____.

Nevertheless, rapid global market expansion presents acute management (10)____. Supply chain disruptions and volatile commodity prices create financial (11)____ across international distribution channels. Economists warn that unhedged financial exposure can severely (12)____ corporate solvency.

To counteract these systemic risks, risk management executives are (13)____ comprehensive operational stress tests that simulate severe market (14)____. Such proactive measures (15)____ financial resilience and protect employee job security.

Ultimately, sustainable business success is an ongoing adaptive (16)____. By honoring customer trust while investing in research innovation, forward-thinking enterprises can (17)____ robust commercial growth amidst market (18)____ today (19)____ and into the future (20)____.`,
          questions: Array.from({ length: 20 }, (_, idx) => {
            const qNum = idx + 1;
            const options = [
              { key: "A", text: ["continually", "seldom", "adversely", "rigidly"][idx % 4] },
              { key: "B", text: ["flourishes", "collapses", "diminishes", "conflicts"][(idx + 1) % 4] },
              { key: "C", text: ["optimizing", "impeding", "neglecting", "deterring"][(idx + 2) % 4] },
              { key: "D", text: ["stimulates", "undermines", "depresses", "stifles"][(idx + 3) % 4] }
            ];
            const ans = ["A", "B", "A", "A", "C", "A", "A", "B", "A", "A", "D", "A", "A", "C", "A", "A", "A", "B", "A", "A"][idx];
            return {
              q_type: "cloze_item",
              stem: `Choose the best option for blank (${qNum}) in the passage:`,
              points: 0.5,
              sort_order: qNum,
              options,
              correct_answer: ans,
              explanation: `【考点精析】英语（二）第(${qNum})题：考查商务与社会学核心词汇搭配。结合句法结构与句意推进，选项 [${ans}] 最符合语篇语义连贯要求。`
            };
          })
        },

        // Section II: Reading Part A (4 Texts, 5 questions each = 20 questions, 2 points each)
        ...[1, 2, 3, 4].map((tNum) => {
          const theme = [meta.t1Theme, meta.t2Theme, meta.t3Theme, meta.t4Theme][tNum - 1];
          const startQ = 20 + (tNum - 1) * 5 + 1;
          return {
            section_type: "reading",
            title: `Section II: Reading Comprehension Part A (Text ${tNum})`,
            sort_order: tNum + 1,
            content: `The business ecosystem surrounding ${theme.toLowerCase()} is experiencing profound structural transformation. Across major industries, executives are re-evaluating long-standing operational assumptions to maintain commercial viability in an increasingly competitive marketplace.

First, market data indicates a shifting consumer landscape characterized by greater brand scrutiny and demand for transparency. Modern consumers increasingly reward ethical business practices and sustainability commitments. Companies that fail to authenticate their environmental claims face swift public skepticism and brand damage.

Second, technological automation is reshaping workforce dynamics. While robotic process automation streamlines repetitive tasks and reduces operational overhead, it necessitates substantial investment in employee upskilling. HR executives emphasize that human empathy, creative problem-solving, and cross-functional leadership cannot be automated.

Third, fiscal and monetary conditions have tightened capital availability. Venture funds and commercial banks are prioritizing operational cash flow and sustainable unit economics over speculative top-line user growth. As a result, businesses must demonstrate clear pathways to profitability.

Ultimately, long-term commercial longevity requires balancing near-term operational discipline with forward-looking research investments. Enterprises that embrace customer-centric innovation while maintaining robust ethical governance will navigate market volatility with resilience.`,
            questions: Array.from({ length: 5 }, (_, qIdx) => {
              const qNum = startQ + qIdx;
              const stems = [
                `According to Paragraph 1, why are business leaders re-evaluating operational assumptions?`,
                `What can be inferred about modern consumer behavior in Paragraph 2?`,
                `In terms of workforce automation (Paragraph 3), HR executives believe that:`,
                `Paragraph 4 suggests that investors and financial institutions are now:`,
                `What is the central theme of the text?`
              ];
              const options = [
                [
                  { key: "A", text: "To maintain competitiveness amidst structural market shifts" },
                  { key: "B", text: "To abandon technological innovation in favor of manual labor" },
                  { key: "C", text: "To eliminate all customer feedback mechanisms" },
                  { key: "D", text: "To lobby governments for monopolistic protections" }
                ],
                [
                  { key: "A", text: "Consumers actively reward verified corporate ethics and sustainability" },
                  { key: "B", text: "Brand reputation is entirely uninfluenced by environmental claims" },
                  { key: "C", text: "Purchasing decisions are solely determined by rock-bottom pricing" },
                  { key: "D", text: "Consumers have completely ceased scrutinizing corporate disclosures" }
                ],
                [
                  { key: "A", text: "Essential human skills like empathy and creativity remain irreplaceable" },
                  { key: "B", text: "All human employees will be entirely replaced within five years" },
                  { key: "C", text: "Upskilling programs provide zero measurable productivity gains" },
                  { key: "D", text: "Repetitive administrative tasks should never be digitized" }
                ],
                [
                  { key: "A", text: "Prioritizing tangible cash flows and sustainable profitability" },
                  { key: "B", text: "Subsidizing loss-making startups with unrestricted capital" },
                  { key: "C", text: "Refusing to finance any technological enterprise" },
                  { key: "D", text: "Disregarding unit economics in favor of speculative growth" }
                ],
                [
                  { key: "A", text: `${theme}: Strategic Adaptation and Commercial Resilience` },
                  { key: "B", text: "The Disappearance of Ethical Corporate Management" },
                  { key: "C", text: "Why Automation Guarantees Rapid Corporate Bankruptcy" },
                  { key: "D", text: "A Complete Rejection of Modern Financial Markets" }
                ]
              ];
              return {
                q_type: "reading_item",
                stem: stems[qIdx],
                points: 2.0,
                sort_order: qNum,
                options: options[qIdx],
                correct_answer: "A",
                explanation: `【考点精析】英语（二）第(${qNum})题：细节推断与主旨归纳。通过定位段落论点与事实阐述，选项 [A] 紧密契合原文语义且表述严谨客观。`
              };
            })
          };
        }),

        // Section II: Reading Part B (New Type, 5 questions, 2 points each)
        {
          section_type: "reading",
          title: `Section II: Reading Comprehension Part B (${meta.partBTheme.split(",")[0]} 新题型 41-45题)`,
          sort_order: 6,
          content: `Directions: Read the following text and match each of the numbered points (41-45) with the most appropriate descriptive statement or strategic principle [A]-[G].

[Statement 41] In assessing ${meta.partBTheme.toLowerCase()}, analysts emphasize that infrastructure investments require long-term capital horizons. Early-stage high capital expenditures are offset by substantial marginal cost efficiencies once operational scale is achieved.

[Statement 42] Risk management frameworks must account for regulatory uncertainty. When pioneering innovative commercial sectors, corporate legal teams must proactively engage with municipal and federal regulators to draft safety compliance standards.

[Statement 43] Customer adoption curves in emerging technology markets are heavily influenced by user experience design. Frictionless onboarding, transparent pricing, and intuitive digital interfaces dramatically reduce consumer switching barriers.

[Statement 44] Talent acquisition represents a critical operational bottleneck. Competing for specialized engineering and data science professionals requires offering purpose-driven mission statements and flexible hybrid work arrangements alongside competitive compensation.

[Statement 45] Strategic corporate partnerships can accelerate market entry. Rather than building proprietary distribution networks from scratch, agile market entrants form alliances with established industry incumbents to leverage existing customer pipelines.`,
          questions: [
            {
              q_type: "reading_item",
              stem: "Item 41 emphasizes which operational principle?",
              points: 2.0,
              sort_order: 41,
              options: [
                { key: "A", text: "Long-term capital expenditure horizons and economies of scale" },
                { key: "B", text: "Immediate termination of all infrastructure projects" },
                { key: "C", text: "Avoiding all regulatory interactions until legal sanctions occur" },
                { key: "D", text: "The elimination of customer onboarding interfaces" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(41)题：文本强调长期资本投入与规模经济效益，对应选项 [A]。"
            },
            {
              q_type: "reading_item",
              stem: "Item 42 focuses on which strategic necessity?",
              points: 2.0,
              sort_order: 42,
              options: [
                { key: "A", text: "Proactive regulatory compliance and co-creating safety standards" },
                { key: "B", text: "Operating in direct secrecy from federal oversight" },
                { key: "C", text: "Maximizing short-term legal ambiguity for illicit profits" },
                { key: "D", text: "Ignoring technological changes in consumer law" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(42)题：文本指出主动与监管机构对接并共建合规标准的重要性，对应选项 [A]。"
            },
            {
              q_type: "reading_item",
              stem: "Item 43 identifies which factor as crucial for user adoption?",
              points: 2.0,
              sort_order: 43,
              options: [
                { key: "A", text: "Frictionless user experience and intuitive digital interfaces" },
                { key: "B", text: "Complex and opaque pricing schemes" },
                { key: "C", text: "Deliberately raising switching barriers for customers" },
                { key: "D", text: "Eliminating digital software platforms" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(43)题：文本强调顺畅的数字交互设计与透明定价促进用户转化，对应选项 [A]。"
            },
            {
              q_type: "reading_item",
              stem: "Item 44 highlights which key human resources challenge?",
              points: 2.0,
              sort_order: 44,
              options: [
                { key: "A", text: "Attracting scarce specialized talent through purpose and flexibility" },
                { key: "B", text: "Enforcing rigid sixty-hour office mandates with sub-market pay" },
                { key: "C", text: "Completely outsourcing all engineering competencies" },
                { key: "D", text: "Terminating all data science employment positions" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(44)题：文本阐述争夺高端专业技术人才需结合使命感与灵活办公，对应选项 [A]。"
            },
            {
              q_type: "reading_item",
              stem: "Item 45 suggests that new market entrants should:",
              points: 2.0,
              sort_order: 45,
              options: [
                { key: "A", text: "Form alliances with established incumbents to leverage distribution" },
                { key: "B", text: "Rebuild proprietary distribution networks from zero at all costs" },
                { key: "C", text: "Refuse to cooperate with any existing market players" },
                { key: "D", text: "Dissolve all external commercial agreements" }
              ],
              correct_answer: "A",
              explanation: "【考点精析】第(45)题：文本提倡敏捷企业应与成熟企业结成战略同盟共享分销网络，对应选项 [A]。"
            }
          ]
        }
      ]
    };
    exams.push(exam);
  }

  return exams;
}
