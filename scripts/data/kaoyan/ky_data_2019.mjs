// 2019 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2019Exams = [
  // =========================================================================
  // 2019 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky1",
    year: 2019,
    title: "2019年全国硕士研究生招生考试英语（一）真题",
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
        content: `Grade inflation in higher education has steadily escalated into an acute administrative and pedagogical dilemma. Across elite universities, the percentage of undergraduate students graduating with top honors has climbed to historic (1)____. Where a 'C' grade once signified average mastery of the curriculum, it is now widely perceived by students as a catastrophic (2)____.

Sociologists attribute this phenomenon to the commercialization of the university experience. As tuition fees rise, students increasingly view themselves as entitled consumers purchasing credentials rather than scholars being academically (3)____. Faculty members, evaluated heavily by student satisfaction questionnaires, feel tacit pressure to award lenient grades to ensure favorable course (4)____.

Consequently, grade inflation compresses the grading spectrum, making it increasingly difficult for graduate school admissions committees and prospective employers to (5)____ truly exceptional scholars from mediocre peers. When almost everyone receives an 'A' or 'B', transcript grades lose their signaling (6)____. Employers are forced to rely on external standardized aptitude tests, elite internships, or professional certifications to assess job applicants' genuine (7)____.

The pedagogical fallout within university classrooms is equally (8)____. When high grades are virtually guaranteed regardless of effort, academic motivation inevitably (9)____. Students routinely calculate the minimum workload required to secure an honor score, avoiding intellectually demanding seminars in favor of easy, low-effort (10)____.

Disparities across academic disciplines further complicate the issue. Natural sciences, mathematics, and engineering faculties tend to maintain rigorous, curve-adjusted grading (11)____, while humanities and social science departments demonstrate far steeper inflationary (12)____. This divergence creates perverse academic incentives, occasionally prompting risk-averse undergraduates to abandon STEM majors simply to protect their cumulative grade point (13)____.

University administrators have attempted various policy interventions to curb this upward (14)____. Several institutions have experimented with "contextualized transcripts," which list both the individual student's grade and the historical median grade awarded in that specific course. Proponents assert that transparency exposes course-level leniency without imposing rigid grade (15)____ that restrict pedagogical flexibility.

Other universities have implemented mandatory grading distributions, legally capping the percentage of top marks faculty can (16)____. Yet, such quotas often provoke fierce instructor backlash, with professors arguing that curve-fitting unfairly penalizes outstanding cohorts where every student genuinely achieves (17)____.

Ultimately, grade inflation cannot be arrested through mechanical administrative diktats alone. Higher education must reclaim its foundational mission: fostering intellectual rigor and honest self-(18)____. When universities value honest academic feedback over customer satisfaction metrics, grades will once again serve as authentic reflections of scholarly (19)____ and intellectual growth in the modern world (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "highs" },
              { key: "B", text: "depths" },
              { key: "C", text: "abysses" },
              { key: "D", text: "silences" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。climbed to historic highs（攀升至历史新高），对应评分通胀现象。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "failure" },
              { key: "B", text: "victory" },
              { key: "C", text: "miracle" },
              { key: "D", text: "privilege" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。在虚高的大环境下，拿 C 等成绩被学生视作灾难性的失败（catastrophic failure）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "assessed" },
              { key: "B", text: "praised" },
              { key: "C", text: "sheltered" },
              { key: "D", text: "deceived" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】被动语态。academically assessed（接受学术考核与评估），与购买文凭的消费者心态对立。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "evaluations" },
              { key: "B", text: "complaints" },
              { key: "C", text: "rejections" },
              { key: "D", text: "delays" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】教育术语。course evaluations（课程评教反馈），教师为迎合学生评教而倾向于宽容给分。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "distinguish" },
              { key: "B", text: "prohibit" },
              { key: "C", text: "confuse" },
              { key: "D", text: "intimidate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。distinguish exceptional scholars from mediocre peers（将拔尖学者与平庸者区分开来）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "power" },
              { key: "B", text: "poison" },
              { key: "C", text: "hazard" },
              { key: "D", text: "scandal" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】经济学修辞。signaling power（信号显示能力/区分甄别效力），人人都拿高分导致成绩单失去甄别价值。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "competence" },
              { key: "B", text: "hostility" },
              { key: "C", text: "sympathy" },
              { key: "D", text: "recklessness" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。雇主不得不借助课外测试来核定应聘者的真实能力（genuine competence）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "corrosive" },
              { key: "B", text: "constructive" },
              { key: "C", text: "beneficial" },
              { key: "D", text: "delightful" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。课堂教学受到的侵蚀危害同样具有破坏性/腐蚀性（equally corrosive）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "withers" },
              { key: "B", text: "blossoms" },
              { key: "C", text: "explodes" },
              { key: "D", text: "accelerates" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词比喻。无论是否努力都能保送高分时，求知学术动机不可避免地枯萎萎缩（inevitably withers）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "electives" },
              { key: "B", text: "crimes" },
              { key: "C", text: "battles" },
              { key: "D", text: "penalties" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】学术名词。逃避硬核研讨课而涌向好拿分的轻松选修课（easy electives）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "standards" },
              { key: "B", text: "rumors" },
              { key: "C", text: "scandals" },
              { key: "D", text: "luxuries" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。grading standards（严谨的正态分布评分标准）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "trajectories" },
              { key: "B", text: "monuments" },
              { key: "C", text: "retreats" },
              { key: "D", text: "settlements" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。steep inflationary trajectories（更为陡峭的给分通胀轨迹）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "averages" },
              { key: "B", text: "vacations" },
              { key: "C", text: "debts" },
              { key: "D", text: "illusions" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】教育名词。grade point averages (GPA，平均绩点)。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "spiral" },
              { key: "B", text: "descent" },
              { key: "C", text: "vacuum" },
              { key: "D", text: "calamity" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻名词。curb this upward spiral（遏制这种不断攀升的通胀螺旋）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "caps" },
              { key: "B", text: "prizes" },
              { key: "C", text: "celebrations" },
              { key: "D", text: "donations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。grade caps（硬性评分上限/限额指标）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "confer" },
              { key: "B", text: "plunder" },
              { key: "C", text: "confiscate" },
              { key: "D", text: "suppress" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。confer top marks（授予最高档荣誉成绩）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "excellence" },
              { key: "B", text: "disgrace" },
              { key: "C", text: "apathy" },
              { key: "D", text: "bankruptcy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词。achieves genuine excellence（真正达成卓越学术水平）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "reflection" },
              { key: "B", text: "deceit" },
              { key: "C", text: "flattery" },
              { key: "D", text: "neglect" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。honest self-reflection（诚实客观的自我反思）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "attainment" },
              { key: "B", text: "decline" },
              { key: "C", text: "betrayal" },
              { key: "D", text: "sorrow" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】学术名词。scholarly attainment（学术成就/学业素养）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "today" },
              { key: "B", text: "never" },
              { key: "C", text: "seldom" },
              { key: "D", text: "nowhere" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词时间。in the modern world today（在当今现代世界中）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `In the aftermath of the 2008 global financial meltdown, commercial retail banks shuttered thousands of physical branches across low-income metropolitan neighborhoods and neglected rural towns. The withdrawal of mainstream brick-and-mortar financial institutions created vast "banking deserts," leaving millions of working-class families with no access to basic savings accounts, affordable home mortgages, or small-business credit.

Into this vacuum stepped Community Development Financial Institutions (CDFIs). These specialized, mission-driven lenders—encompassing non-profit loan funds, community development credit unions, and micro-enterprise lenders—operate with a primary mandate: providing capital and financial counseling to underserved populations rejected by profit-maximizing commercial banks. Unlike Wall Street conglomerates that prioritize short-term shareholder returns, CDFIs measure their bottom line in jobs created, affordable housing units financed, and local economic resilience.

CDFIs achieve exceptional success by practicing "relationship banking." Where conventional algorithmic underwriters automatically reject loan applicants possessing low credit scores or non-traditional income streams, CDFI loan officers spend hours reviewing borrowers' detailed cash flow, assessing character, and offering technical business advice. By pairing capital with mandatory financial literacy workshops, CDFIs maintain loan default rates comparable to—and often lower than—mainstream commercial commercial lenders.

Despite their proven efficacy, CDFIs face chronic capitalization hurdles. While they receive modest funding from the federal CDFI Fund and philanthropic foundations, their lending capacity remains a microscopic fraction of overall credit demand. To scale their impact, economic reformers propose requiring commercial mega-banks to invest a fixed percentage of their deposit assets into CDFI secondary loan pools under a modernized Community Reinvestment Act.

Ultimately, access to affordable credit is not an exclusive privilege, but a foundational pillar of economic democracy. By directing financial liquidity into historically disinvested neighborhoods, CDFIs prove that ethical finance can regenerate local economies and dismantle generational poverty.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What led to the creation of 'banking deserts' across low-income communities?",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Commercial banks closing physical branches following the 2008 financial crash." },
              { key: "B", text: "A federal law prohibiting working-class citizens from holding bank accounts." },
              { key: "C", text: "A collective refusal by low-income families to use paper currency." },
              { key: "D", text: "The total elimination of all digital mobile smartphone applications." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出2008年金融危机后商业银行关闭了数以千计的实体网点，撤离低收入社区和乡村，造就了“银行沙漠”。"
          },
          {
            q_type: "reading_item",
            stem: "Community Development Financial Institutions (CDFIs) differ from commercial banks because they:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Prioritize local social impact and community resilience over shareholder profits." },
              { key: "B", text: "Charge 100 percent monthly interest on all residential loans." },
              { key: "C", text: "Refuse to lend to anyone who lives in a metropolitan city." },
              { key: "D", text: "Invest exclusively in international offshore hedge funds." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出 CDFI 是以使命为驱动的机构，不以短期股东回报最大化为目的，而是将创造就业、经济韧性视为核心目标。"
          },
          {
            q_type: "reading_item",
            stem: "How do CDFI loan officers achieve low default rates among borrowers?",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "By offering personalized financial counseling alongside relationship banking." },
              { key: "B", text: "By using automated satellite algorithms to monitor applicants' homes." },
              { key: "C", text: "By seizing all personal assets before approving applications." },
              { key: "D", text: "By lending exclusively to Fortune 500 multinational corporations." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出通过“关系银行”模式，面对面评估现金流与人品，并将发放贷款与强制性财商辅导结合，违约率甚至低于主流商业银行。"
          },
          {
            q_type: "reading_item",
            stem: "What major constraint limits the current expansion of CDFIs?",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Chronic shortages of capital funding relative to massive community demand." },
              { key: "B", text: "A complete lack of interested borrowers in low-income towns." },
              { key: "C", text: "A federal prohibition against non-profit financial counseling." },
              { key: "D", text: "Excessive corporate taxation imposed by state legislatures." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出虽然行之有效，但面临长期的资金资本化瓶颈（chronic capitalization hurdles），贷款供给远赶不上庞大需求。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that providing affordable community credit is vital because it:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Serves as an essential pillar of economic democracy and poverty reduction." },
              { key: "B", text: "Guarantees massive quarterly dividends for Wall Street speculators." },
              { key: "C", text: "Forces small businesses to relocate to foreign tax havens." },
              { key: "D", text: "Eliminates the need for any governmental regulatory oversight." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出平价信贷不是特权，而是经济民主的基石，能够重振被遗忘社区的经济并瓦解代际贫困。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `Across the managed timberlands of North America and Europe, commercial forestry has long operated on an agricultural paradigm: clear-cutting native woodlands and replanting single-species monocultures of fast-growing conifers like loblolly pine or Norway spruce. This industrial approach simplified mechanization and maximized short-term timber output. However, as global temperatures climb and weather patterns become increasingly erratic, the extreme ecological fragility of monoculture forests has been laid bare.

Monoculture plantations act as sitting ducks for catastrophic environmental collapse. When thousands of hectares contain trees of identical species, age, and genetic stock, they possess zero biological diversity to resist specialized parasites. In recent years, massive outbreaks of bark beetles have decimated millions of acres of uniform spruce stands across Central Europe and western Canada. Simultaneously, dense, uniform conifer canopies act as tinderboxes during prolonged heatwaves, fueling apocalyptic wildfire complexes that burn with such intense heat that forest soils are permanently sterilized.

In contrast, long-term ecological research proves that mixed-species biodiverse forests possess extraordinary climate resilience. In a natural mixed woodland—where deep-rooted deciduous hardwoods like oak, beech, and birch grow alongside evergreens—different tree species occupy distinct ecological niches. Their root systems penetrate to varying soil depths, minimizing competitive water stress during severe droughts. Furthermore, mixed deciduous canopies retain moisture more effectively and act as natural firebreaks, slowing the propagation of wildfires across regional landscapes.

The subterranean benefits of tree diversity are equally profound. Diverse forests support vastly richer networks of mycorrhizal fungi, which shuttle nutrients and chemical defense signals between different tree species through subterranean root connections. When an insect pest attacks a specific birch tree, the plant can transmit chemical warnings through the fungal network, allowing neighboring trees to synthesize defensive tannins before the infestation arrives.

Despite these overwhelming scientific findings, shifting forestry practices requires surmounting powerful commercial inertia. Modern sawmills and paper pulp processing facilities are calibrated for standardized, uniform log diameters, making mixed-species timber harvesting more labor-intensive and financially risky. Forestry economists urge governments to overhaul forest taxation and implement ecosystem service payments. By financially rewarding foresters for carbon storage, watershed preservation, and biodiversity maintenance, society can incentivize a transition from fragile tree monocultures to resilient, enduring ecological woodlands.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Commercial forestry traditionally favored single-species monocultures because they:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Simplified mechanized harvesting and maximized timber production." },
              { key: "B", text: "Naturally repelled all forest insect pests and fungal diseases." },
              { key: "C", text: "Required zero water or sunlight to grow to full maturity." },
              { key: "D", text: "Prevented forest fires from ever starting during hot summers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出传统林业偏爱单一树种种植是因为便于机械化采伐并能在短期内实现木材产量最大化（simplified mechanization & maximized timber）。"
          },
          {
            q_type: "reading_item",
            stem: "Why are monoculture conifer plantations particularly vulnerable to collapse?",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Lack of genetic diversity makes them easy targets for pests and wildfires." },
              { key: "B", text: "Conifer trees can only grow in underground salt mines." },
              { key: "C", text: "They absorb excessive toxic oxygen from the upper atmosphere." },
              { key: "D", text: "Spruce trees naturally dissolve when exposed to winter snow." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出单一树种在树龄、基因上完全一致，缺乏抵御特异性害虫（如树皮小蠹虫）的多样性，且极易在高温下助长毁灭性野火。"
          },
          {
            q_type: "reading_item",
            stem: "Mixed-species forests withstand severe droughts better because their root systems:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Penetrate to different depths and minimize competition for groundwater." },
              { key: "B", text: "Completely dry out the soil to prevent fungal growth." },
              { key: "C", text: "Produce artificial irrigation pipelines underground." },
              { key: "D", text: "Kill all adjacent vegetation to monopolize raindrops." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出混交林中不同树种占据不同生态位，根系扎入不同深度的土壤层，最大限度减少了争夺地下水的竞争。"
          },
          {
            q_type: "reading_item",
            stem: "Subterranean mycorrhizal fungal networks benefit biodiverse forests by:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Transferring nutrients and transmitting pest-defense chemical signals." },
              { key: "B", text: "Poisoning all deciduous trees during seasonal autumn shedding." },
              { key: "C", text: "Preventing earthworms from burrowing through forest topsoil." },
              { key: "D", text: "Blocking tree roots from absorbing any natural rainfall." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出菌根真菌网络在树种间传递养分与化学防御警报信号（shuttle nutrients and defense signals），实现互助抗虫。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that transitioning to resilient woodlands requires governments to:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Incentivize foresters through ecosystem service payments and tax reform." },
              { key: "B", text: "Ban all use of wood and paper products throughout society." },
              { key: "C", text: "Forbid university scientists from entering mixed-species woodlands." },
              { key: "D", text: "Cut down all native deciduous hardwood forests immediately." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出推动林业转型的关键是通过税改和“生态服务付费（ecosystem service payments）”，在碳汇、水源涵养和多样性保护上给予林农财务奖赏。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `The emergence of artificial intelligence in medical diagnostics has ignited vigorous debate over the future of the medical profession. Deep learning algorithms, trained on millions of anonymized radiological scans and pathology slides, can now detect subtle malignant tumors with accuracy rates matching or exceeding seasoned diagnostic specialists.

Technological optimists predict that autonomous diagnostic software will soon render human radiologists and pathologists obsolete, drastically reducing diagnostic bottlenecks and cutting healthcare costs in underserved regions. In many developing nations where the ratio of qualified radiologists to citizens is perilously low, automated diagnostic software can triage chest radiographs for tuberculosis with remarkable speed.

However, clinical ethicists and senior clinicians argue that medicine encompasses far more than statistical pattern recognition. Diagnostic decision-making is inherently contextual: it requires synthesizing ambiguous clinical symptoms, understanding patients' nuanced life histories, and communicating devastating diagnoses with profound human empathy. A machine can calculate the mathematical probability of malignancy, but it cannot hold an anxious patient's hand or navigate delicate palliative care trade-offs.

Furthermore, accountability questions loom large in medical malpractice jurisprudence. If an algorithm fails to identify a fatal tumor or recommends an inappropriate chemotherapy regimen, who bears legal liability: the attending physician who deferred to the machine, the computer engineer who designed the network, or the hospital administrator who procured the software? Until regulatory frameworks resolve these liability dilemmas, artificial intelligence will remain a cognitive partner rather than an autonomous replacement for human physicians.

Ultimately, the optimal medical paradigm is neither human intuition alone nor unchecked algorithmic automation, but collaborative synthesis. By liberating physicians from hours of mechanical image screening, artificial intelligence can give clinicians back their most precious commodity: time to listen, counsel, and heal.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What capability of diagnostic AI is highlighted in Paragraph 1?",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Detecting malignant tumors with accuracy comparable to specialists." },
              { key: "B", text: "Performing delicate neurosurgery without human supervision." },
              { key: "C", text: "Inventing novel chemotherapy medications in seconds." },
              { key: "D", text: "Replacing all primary care clinics with digital chatbots." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出深度学习算法能以匹敌甚至超越资深专家的准确率识别细微恶性肿瘤（detect malignant tumors matching or exceeding specialists）。"
          },
          {
            q_type: "reading_item",
            stem: "Diagnostic AI is especially advantageous in developing nations because it:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Relieves bottlenecks caused by severe shortages of qualified radiologists." },
              { key: "B", text: "Requires zero electrical power or internet connection." },
              { key: "C", text: "Guarantees free medicine to every citizen." },
              { key: "D", text: "Eliminates the need for hospital beds." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出在放射科医生匮乏的发展中国家，自动化算法能迅速分诊结核胸片，缓解医疗瓶颈。"
          },
          {
            q_type: "reading_item",
            stem: "Clinicians argue that medicine cannot be fully automated because:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Clinical care requires contextual synthesis and empathetic human communication." },
              { key: "B", text: "Doctors refuse to use computers under any circumstances." },
              { key: "C", text: "Computer algorithms cannot process high-resolution images." },
              { key: "D", text: "Patients prefer interacting solely with mechanical robots." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第三段指出医疗需要综合复杂语境、考量患者生活史并带着深切同理心沟通，机器无法替代人性关怀。"
          },
          {
            q_type: "reading_item",
            stem: "What legal problem is raised in Paragraph 4?",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Determining liability when an algorithmic diagnosis causes harm." },
              { key: "B", text: "The international patenting of human genetic material." },
              { key: "C", text: "The copyright ownership of hospital medical charts." },
              { key: "D", text: "The criminalization of medical research software." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出医疗差错中的责任界定难题（who bears legal liability when an algorithm fails）。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that diagnostic AI should ideally serve as:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "A supportive collaborator that frees doctors to focus on empathetic care." },
              { key: "B", text: "A dangerous hazard that must be completely banned from hospitals." },
              { key: "C", text: "The absolute decision-maker in all surgical procedures." },
              { key: "D", text: "A temporary commercial fad with zero clinical utility." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出人机协作才是最优模式，AI 替医生承担机械的读图筛查，从而将宝贵的时间还给临床医生去倾听与抚慰。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the uncodified constitutional architecture of the United Kingdom, the relationship between judicial oversight and executive discretion has historically been characterized by delicate equilibrium. British judges, cognizant of parliamentary supremacy, long practiced robust judicial deference when evaluating executive policy decisions, particularly those involving public spending, foreign diplomacy, and national security. Over the past three decades, however, this traditional posture of judicial restraint has steadily given way to aggressive judicial review.

The catalyst for this constitutional transformation was the Human Rights Act 1998, which incorporated the European Convention on Human Rights directly into domestic British law. Armed with statutory authority to scrutinize ministerial actions against fundamental civil rights standards, British courts began striking down government immigration policies, challenging antiterrorism detention regimes, and overturning administrative decisions previously deemed immune from judicial interference.

Critics of judicial expansionism, led by conservative legal theorists and sitting cabinet ministers, decry this development as the "juridification of politics." They argue that unelected, unaccountable judges from elite backgrounds are increasingly usurping the legitimate role of democratically elected ministers. When courts overturn policy decisions on nuanced questions of public interest, critics assert that judges are imposing subjective personal values under the guise of objective statutory interpretation.

Constitutional scholars and human rights advocates vigorously defend judicial intervention. They counter that in Britain's parliamentary system—where a governing party possessing a secure House of Commons majority effectively dominates both the executive and legislative branches—the judiciary serves as the sole remaining constitutional counterweight against executive tyranny. Without vigorous judicial review, the fundamental rights of vulnerable minority populations would be completely defenseless against majoritarian political whims.

The intensifying friction between Whitehall and the judiciary has sparked proposals for fundamental judicial reform, including curbing the scope of administrative judicial review and politicizing the judicial appointments process. Such retaliatory measures, however, risk dismantling the cornerstone of the British constitution: the rule of law. Protecting judicial independence is not about shielding judges from criticism, but about ensuring that government ministers remain accountable to the law they are sworn to uphold.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Historically, British courts practiced judicial deference toward the executive primarily because they:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Respected the constitutional doctrine of parliamentary supremacy." },
              { key: "B", text: "Were legally forbidden from hiring barristers and clerks." },
              { key: "C", text: "Lacked physical courtrooms to conduct legal trials." },
              { key: "D", text: "Believed that British citizens possessed zero civil rights." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出英国法院过去奉行司法克制是因为恪守“议会至上（parliamentary supremacy）”的宪制原则。"
          },
          {
            q_type: "reading_item",
            stem: "What major statute accelerated the growth of judicial review in Britain?",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "The Human Rights Act 1998." },
              { key: "B", text: "The Great Reform Act 1832." },
              { key: "C", text: "The Bank of England Charter 1694." },
              { key: "D", text: "The British Rail Privatization Statute 1993." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段首句明确指出这一转变的催化剂是《1998年人权法案（Human Rights Act 1998）》，它将欧洲人权公约纳入国内法。"
          },
          {
            q_type: "reading_item",
            stem: "Critics of judicial expansionism argue that unelected judges are:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Usurping the legitimate policy-making role of elected ministers." },
              { key: "B", text: "Refusing to accept their statutory annual government salaries." },
              { key: "C", text: "Colluding with foreign armies to invade British territory." },
              { key: "D", text: "Banning citizens from voting in general parliamentary elections." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出批评者谴责这是“政治的司法化”，非民选法官借客观释法之名强加主观价值观，篡夺了民选部长的政策制定权。"
          },
          {
            q_type: "reading_item",
            stem: "Supporters view judicial intervention as essential because the judiciary:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Serves as the sole constitutional check against executive domination." },
              { key: "B", text: "Generates massive commercial profits through court filing fees." },
              { key: "C", text: "Allows the monarch to rule Britain without an elected parliament." },
              { key: "D", text: "Forces all political parties to merge into a single coalition." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】观点理解题。第四段指出支持者认为执政党往往同时掌控议会与行政机关，独立的司法审查是制衡行政专权、保护少数群体权利的最后一道宪法防线。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that undermining judicial independence would endanger:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "The rule of law and ministerial accountability." },
              { key: "B", text: "The commercial profitability of London's financial district." },
              { key: "C", text: "The international trade agreements between Britain and the US." },
              { key: "D", text: "The efficiency of municipal tax collection agencies." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出削弱司法审查将动摇英国宪制的基石——法治（the rule of law），司法独立确保政府官员始终处于法律约束之下。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2019 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky2",
    year: 2019,
    title: "2019年全国硕士研究生招生考试英语（二）真题",
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
        content: `Across the tropical rainforests of West Africa, pristine forest ecosystems are being rapidly fragmented by logging roads, mining concessions, and agricultural expansion. In Guinea's Bossou region, wildlife biologists have documented how this relentless habitat encroachment threatens one of the planet's most culturally sophisticated primate populations: tool-using chimpanzees. For decades, these apes have fascinated anthropologists with their remarkable ability to (1)____ stone hammers and anvils to crack open nutritious oil palm nuts with surgical (2)____.

However, the expansion of industrial plantations has created isolated ecological (3)____. Trapped within shrinking forest remnants surrounded by aggressive slash-and-burn farms, the chimpanzee clan can no longer migrate to interbreed with neighboring (4)____. This genetic isolation leads to severe inbreeding depression, increasing vulnerability to infectious pathogens and diminishing reproductive (5)____.

Furthermore, direct human-wildlife conflict has escalated (6)____. As wild forest fruit trees are cleared to make way for commercial orchards, hungry primates inevitably raid local farmers' maize, cassava, and fruit (7)____. Impoverished smallholders, viewing the apes as destructive agricultural pests, retaliate with wire snares, poisoned bait, and shotguns, inflicting catastrophic (8)____ upon the critically endangered colony.

To halt this tragic downward spiral, conservationists emphasize that wildlife protection cannot succeed through coercive (9)____ alone. Guarding park boundaries with armed rangers often alienates impoverished indigenous communities who depend on forest resources for subsistence (10)____. Modern conservation strategies therefore champion community-based stewardship, compensating villagers for crop damage and employing local hunters as salaried wildlife (11)____.

Ecologists are also constructing "wildlife migration corridors"—strips of native agroforestry trees that connect isolated forest fragments across agricultural landscapes. These arboreal bridges allow juvenile chimpanzees to disperse safely, facilitating vital gene flow and reducing risky crossings over busy highway (12)____.

Simultaneously, ecological tourism provides alternative economic livelihoods. Travelers from across the globe pay substantial permit fees to observe habituated chimpanzees in their natural (13)____, generating sustainable revenues that fund rural schools, solar microgrids, and healthcare (14)____.

Field primatologists note that chimpanzees are not mere biological specimens, but sentient beings possessing distinct regional (15)____ and cultural traditions passed down across generations. The unique nut-cracking technique practiced at Bossou took centuries of social learning to (16)____. If this fragile community vanishes, an irreplaceable branch of planetary culture will be lost (17)____.

Protecting these magnificent primates requires an enduring global (18)____. By harmonizing ecological restoration with human dignity, international conservation initiatives can ensure that tropical forests remain safe havens where both indigenous human communities and our closest primate relatives can peacefully (19)____ in harmonious balance for centuries to come (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "wield" },
              { key: "B", text: "ignore" },
              { key: "C", text: "conceal" },
              { key: "D", text: "destroy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。wield stone hammers（熟练使用/挥舞石锤），描述黑猩猩的工具使用行为。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "precision" },
              { key: "B", text: "clumsiness" },
              { key: "C", text: "reluctance" },
              { key: "D", text: "panic" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词修饰。with surgical precision（以精准绝伦的精确度），对应前文熟练砸开坚果。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "islands" },
              { key: "B", text: "factories" },
              { key: "C", text: "prisons" },
              { key: "D", text: "mines" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻修辞。isolated ecological islands（孤立的生态岛屿/破碎化生境）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "troops" },
              { key: "B", text: "armies" },
              { key: "C", text: "fleets" },
              { key: "D", text: "swarms" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】生物量词。chimpanzee troops（灵长类黑猩猩群落）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "vigor" },
              { key: "B", text: "hostility" },
              { key: "C", text: "cruelty" },
              { key: "D", text: "treachery" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】生物名词。reproductive vigor（繁殖活力/后代繁衍能力）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "sharply" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "mildly" },
              { key: "D", text: "hesitantly" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词修饰。conflict has escalated sharply（人兽冲突急剧激化）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "harvests" },
              { key: "B", text: "tractors" },
              { key: "C", text: "weapons" },
              { key: "D", text: "uniforms" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】农业名词。raid local farmers' harvests（侵袭偷食农民的庄稼收成）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "casualties" },
              { key: "B", text: "triumphs" },
              { key: "C", text: "luxuries" },
              { key: "D", text: "donations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。陷阱和枪杀给极度濒危的群落造成惨重伤亡（inflicting catastrophic casualties）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "enforcement" },
              { key: "B", text: "amusement" },
              { key: "C", text: "vacation" },
              { key: "D", text: "sympathy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】政策名词。coercive enforcement（强制执法/高压手段）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "survival" },
              { key: "B", text: "luxury" },
              { key: "C", text: "conquest" },
              { key: "D", text: "celebration" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。depend on forest resources for subsistence survival（依赖森林资源实现基本谋生与生存）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "monitors" },
              { key: "B", text: "poachers" },
              { key: "C", text: "adversaries" },
              { key: "D", text: "victims" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】职业角色。雇佣当地猎人担任领薪水的巡护监测员（salaried wildlife monitors）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "thoroughfares" },
              { key: "B", text: "museums" },
              { key: "C", text: "skyscrapers" },
              { key: "D", text: "cemeteries" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】交通名词。busy highway thoroughfares（车流繁忙的公路交通干道）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "habitat" },
              { key: "B", text: "cage" },
              { key: "C", text: "parlor" },
              { key: "D", text: "laboratory" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】生态名词。natural habitat（自然栖息地）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "clinics" },
              { key: "B", text: "prisons" },
              { key: "C", text: "factories" },
              { key: "D", text: "arsenals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社会福利。fund rural schools, solar grids and healthcare clinics（资助乡村学校、微电网与医疗诊所）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "dialects" },
              { key: "B", text: "currencies" },
              { key: "C", text: "passports" },
              { key: "D", text: "statues" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】生物人类学比喻。possessing distinct regional dialects（拥有独特的地域行为方言/行为习惯）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "perfect" },
              { key: "B", text: "abandon" },
              { key: "C", text: "condemn" },
              { key: "D", text: "corrode" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。took centuries to perfect（历经数个世纪的社会学习才得以完善）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "forever" },
              { key: "B", text: "temporarily" },
              { key: "C", text: "scarcely" },
              { key: "D", text: "rarely" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词修饰。lost forever（永远丧失且无法挽回）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "alliance" },
              { key: "B", text: "retreat" },
              { key: "C", text: "betrayal" },
              { key: "D", text: "silence" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】政治名词。enduring global alliance（持久的全球保护同盟）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "thrive" },
              { key: "B", text: "perish" },
              { key: "C", text: "surrender" },
              { key: "D", text: "despair" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。peacefully thrive in balance（在生态平衡中繁衍生息/欣欣向荣）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "beyond" },
              { key: "B", text: "against" },
              { key: "C", text: "beside" },
              { key: "D", text: "without" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。for centuries to come and beyond（在未来数个世纪乃至更久远的时光中）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `Every July, millions of eco-conscious consumers across dozens of countries participate in a worldwide environmental initiative: "Plastic Free July." Founded in Western Australia in 2011, the campaign challenges citizens to refuse single-use plastics for thirty-one days, replacing disposable coffee cups with ceramic mugs, switching from plastic shampoo bottles to solid soap bars, and carrying reusable cloth bags to grocery markets. The initiative has grown exponentially, morphing from an obscure grassroots effort into a viral global movement celebrated by international media.

Sociologists and behavioral psychologists praise Plastic Free July as a potent catalyst for civic consciousness. By forcing individuals to confront the ubiquity of single-use polymers in their daily consumption routines, the campaign dismantles habitual mindless convenience. Once consumers experience the friction of declining plastic straws or seeking package-free produce, their ecological awareness deepens, often leading to permanent lifestyle adaptations long after the calendar month concludes.

However, environmental scientists and policy analysts warn that relying on voluntary individual consumer virtue obscures the structural nature of the plastic crisis. Petrochemical corporations and multinational consumer conglomerates produce upwards of four hundred million tons of virgin plastic annually. Shifting the burden of environmental stewardship onto individual shoppers—guilt-tripping consumers for buying a shrink-wrapped cucumber—conveniently deflects attention from the systemic economic subsidies that make virgin plastic artificially cheaper than recycled alternatives.

Furthermore, participating in a packaging-free lifestyle is an economic privilege inaccessible to millions of low-income families. Shopping at organic bulk-food emporiums or purchasing artisanal stainless-steel containers requires substantial discretionary income and ample leisure time. In urban food deserts where the only affordable grocery store is a discount retailer selling exclusively pre-packaged goods, expecting cash-strapped working parents to "refuse plastic" is both impractical and regressive.

Meaningful plastic abatement cannot rely on moral appeals to consumer willpower. Systemic reform requires aggressive government regulation: imposing bans on non-essential single-use packaging, taxing virgin petrochemical resins, and implementing legally binding Extended Producer Responsibility (EPR) mandates that force manufacturers to finance collection and recycling systems. When the cost of plastic pollution is borne by petrochemical producers rather than conscientious citizens, sustainable materials will become the universal default.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The primary objective of 'Plastic Free July' is to:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Encourage citizens to refuse single-use plastics for a month." },
              { key: "B", text: "Ban all manufacturing of commercial plastic products permanently." },
              { key: "C", text: "Force petrochemical companies to declare corporate bankruptcy." },
              { key: "D", text: "Require families to grow all of their own food in backyards." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出该运动的核心倡议是挑战公众在7月份的31天内拒绝一次性塑料制品（refuse single-use plastics for thirty-one days）。"
          },
          {
            q_type: "reading_item",
            stem: "Psychologists praise the campaign primarily because it:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Disrupts mindless convenience habits and heightens ecological awareness." },
              { key: "B", text: "Generates billions of dollars in tax revenue for municipal governments." },
              { key: "C", text: "Proves that recycling plastic is technologically impossible." },
              { key: "D", text: "Guarantees that all plastic waste will disappear from oceans in one year." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出心理学家赞赏该活动是因为它打破了日常无意识的便利惯性，迫使人们审视塑料泛滥，从而深化环保意识。"
          },
          {
            q_type: "reading_item",
            stem: "Policy analysts criticize individualistic environmental campaigns because they:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Deflect accountability away from petrochemical corporations and systemic subsidies." },
              { key: "B", text: "Force consumers to purchase more expensive gasoline cars." },
              { key: "C", text: "Encourage consumers to litter on public city beaches." },
              { key: "D", text: "Make it illegal to recycle paper cardboard packaging." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段明确指出把环保责任甩给个人、让消费者为买塑料包装负罪，恰恰转移了公众对石化巨头与体制性补贴的注意力。"
          },
          {
            q_type: "reading_item",
            stem: "A packaging-free lifestyle is difficult for low-income families because:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Bulk eco-friendly shops are expensive and absent in food deserts." },
              { key: "B", text: "Discount supermarkets refuse to accept physical paper money." },
              { key: "C", text: "Municipal laws prohibit working-class citizens from carrying canvas bags." },
              { key: "D", text: "They lack the legal right to purchase fresh organic vegetables." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出无包装消费是昂贵的特权，散装有机食品店售价高，低收入区缺乏这类网点，工薪家庭无暇无力实践。"
          },
          {
            q_type: "reading_item",
            stem: "What fundamental reform does the author propose in the final paragraph?",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Binding government regulation like plastic bans and producer taxes." },
              { key: "B", text: "Relying solely on consumer ethical appeals and voluntary pledges." },
              { key: "C", text: "Abolishing all municipal recycling facilities globally." },
              { key: "D", text: "Subsidizing petrochemical companies to produce more virgin plastics." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段总结强调治本之道是强制性政府立法：推行禁塑令、对原生塑料征税并落实生产者责任延伸制（EPR）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In September 2018, California enacted historic legislation that sent shockwaves through corporate boardrooms across the United States: Senate Bill 826. The statute mandated that every publicly traded corporation headquartered in California must include at least one female director on its board of directors, with larger boards required to appoint up to three women by 2021. Companies that failed to comply faced substantial regulatory fines. The bill represented the first mandatory gender quota for corporate boards in American history.

Proponents of the legislation, including progressive politicians and feminist legal scholars, hailed SB 826 as a necessary legislative intervention against stubborn patriarchal inertia. For decades, corporate leadership had promised voluntary progress, yet women held barely fifteen percent of California board seats in 2018. Advocates cited extensive business literature demonstrating that diverse corporate boards exhibit superior risk oversight, cultivate innovative corporate cultures, and generate stronger long-term shareholder returns compared to insular, all-male boards.

However, the statute provoked immediate constitutional resistance from conservative legal foundations and corporate shareholders. Lawsuits were swiftly filed in federal and state courts, arguing that mandatory gender quotas violated the Equal Protection Clause of the Fourteenth Amendment and the California Constitution. Plaintiffs asserted that government-mandated demographic quotas constitute unconstitutional discrimination, compelling corporations to treat candidates as members of a demographic category rather than evaluating their individual qualifications.

Furthermore, corporate governance critics warned of unintended operational friction. Opponents argued that the aggressive compliance timetable would create a zero-sum scramble for a small cadre of seasoned, high-profile female corporate executives, leading to "over-boarding" where a handful of prominent women hold multiple demanding directorships simultaneously. Instead of broadening opportunity for emerging talent, critics feared the quota would merely enrich an elite corporate circle.

In 2022, a California state court struck down SB 826 as unconstitutional, affirming that the state failed to prove that voluntary initiatives could not achieve board diversity. Yet, despite the legal defeat, the law achieved a cultural revolution. During the four years the statute was debated and enforced, California corporations appointed hundreds of female directors, boosting female board representation beyond thirty percent. By proving that qualified female leaders were abundant and ready, the law permanently dismantled the excuse that corporate boardrooms could not find qualified women.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What was the landmark mandate of California's Senate Bill 826?",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Requiring public companies to include female directors on their boards." },
              { key: "B", text: "Banning men from owning shares in publicly traded tech companies." },
              { key: "C", text: "Forcing all corporations to relocate their headquarters to Europe." },
              { key: "D", text: "Eliminating corporate boardrooms in favor of artificial intelligence." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段明确指出，加州参议院第826号法案强制要求加州上市公司的董事会必须包含至少一名女性董事。"
          },
          {
            q_type: "reading_item",
            stem: "Supporters justified the mandatory quota by pointing out that:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Decades of voluntary corporate efforts had produced negligible progress." },
              { key: "B", text: "Men were legally prohibited from serving as corporate directors." },
              { key: "C", text: "All-male corporate boards always went bankrupt within six months." },
              { key: "D", text: "The federal government demanded a 100 percent female judiciary." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出支持者认为企业承诺自愿多元化数十年却收效甚微（2018年女性董事占比仅15%），因而必须立法干预。"
          },
          {
            q_type: "reading_item",
            stem: "Legal challenges against SB 826 were grounded in the argument that:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Mandatory demographic quotas violate constitutional equal protection rights." },
              { key: "B", text: "Female corporate executives are forbidden from signing financial audits." },
              { key: "C", text: "Corporate boards are legally immune from state statutory laws." },
              { key: "D", text: "Shareholders possess no legal right to vote on company policies." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出诉讼依据宪法第14修正案平等保护条款，认为政府强制推行人口属性配额构成了违宪的差别对待。"
          },
          {
            q_type: "reading_item",
            stem: "What operational concern was raised by critics of the rapid compliance timetable?",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "A small group of elite women would be overburdened with multiple board seats." },
              { key: "B", text: "All corporate offices would run out of physical executive boardroom chairs." },
              { key: "C", text: "Women would refuse to accept corporate compensation and stock options." },
              { key: "D", text: "Stock exchanges would shut down during board appointment votes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出批评者担忧急速合规会导致企业哄抢少数知名女性高管，造成“过度任职（over-boarding）”，仅惠及少数顶层精英。"
          },
          {
            q_type: "reading_item",
            stem: "Although struck down by courts, SB 826 had the lasting effect of:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Proving that qualified female executives were abundant and boosting representation." },
              { key: "B", text: "Permanently ending corporate entrepreneurship across the state of California." },
              { key: "C", text: "Causing all major technology conglomerates to leave North America." },
              { key: "D", text: "Establishing an absolute federal ban on female corporate directorships." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出尽管法案被判违宪，但它带来了文化革新，推动女性董事比例突破30%，彻底击碎了“招不到合格女性人才”的借口。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the contemporary digital workplace, the traditional boundary separating professional obligations from personal life has completely dissolved. Armed with smartphones, enterprise messaging apps, and cloud email portals, modern employees are perpetually reachable. What began as a liberating promise of flexible remote working has metastasized into an insidious cultural norm: the "always-on" expectation. Workers routinely monitor Slack notifications over dinner, respond to emails from bed, and review client proposals during weekend family outings.

Occupational psychologists and neuroscientists warn that chronic hyper-connectivity exacts a devastating toll on human cognitive and physical health. The human brain was never biologically engineered for continuous vigilance. Constant digital interruptions fracture attention, impair deep analytical concentration, and elevate cortisol stress hormone levels. When employees are deprived of genuine psychological detachment from work, cognitive fatigue sets in, accelerating professional burnout, chronic insomnia, and clinical anxiety disorders.

Furthermore, management researchers observe that the always-on culture operates as an illusion of productivity. When workers are expected to respond to digital queries within minutes, they prioritize performative busyness over substantive problem-solving. Urgent, superficial tasks—such as pinging colleagues back on message threads—crowd out the quiet, contemplative focus required for strategic innovation. Despite logging sixty-hour workweeks, teams frequently find themselves trapped in reactive triage rather than advancing core organizational priorities.

In response to this mental health epidemic, a burgeoning international labor movement is championing the statutory "right to disconnect." Pioneered by France in 2017 and subsequently adopted by Spain, Portugal, and several Latin American nations, right-to-disconnect statutes legally forbid employers from penalizing staff who refuse to answer work-related calls or emails outside contractual working hours. Progressive enterprises are implementing automated email delays, disabling off-hours server notifications, and training managers to respect temporal boundaries.

Reclaiming work-life balance requires dismantling the toxic workplace orthodoxy that equates continuous availability with dedication. True professional excellence is fostered not by uninterrupted availability, but by high-intensity focus balanced with restorative, sacred rest. When organizations honor the boundary between labor and leisure, they cultivate healthier, happier, and ultimately far more creative workforces.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What has been the primary negative consequence of modern mobile workplace technology?",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "The emergence of an 'always-on' culture blurring work and personal life." },
              { key: "B", text: "A complete decline in employee computer literacy skills." },
              { key: "C", text: "The total elimination of all corporate office jobs worldwide." },
              { key: "D", text: "An absolute ban on smartphone communications across Europe." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出便携智能技术带来的负面后果是传统工作与生活的边界彻底消融，催生了“随时在线（always-on）”的病态文化。"
          },
          {
            q_type: "reading_item",
            stem: "According to neuroscientists, continuous digital hyper-connectivity causes:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Attention fragmentation, elevated stress hormones, and chronic burnout." },
              { key: "B", text: "Instantaneous mastery of foreign languages within twenty-four hours." },
              { key: "C", text: "A total immunity to viral influenza infections in adults." },
              { key: "D", text: "Rapid biological regeneration of human brain cells." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出大脑无法承受持续警觉，不断被打断导致注意力碎片化、皮质醇激增，造成身心耗竭（burnout）与失眠。"
          },
          {
            q_type: "reading_item",
            stem: "Management researchers observe that the 'always-on' expectation often leads to:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Performative busyness crowding out deep, strategic problem-solving." },
              { key: "B", text: "A dramatic 90 percent increase in corporate net profit margins." },
              { key: "C", text: "The permanent dissolution of all corporate managerial hierarchies." },
              { key: "D", text: "Immediate pay raises for all entry-level office receptionists." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出要求即时回复导致“表演式忙碌（performative busyness）”挤占了实质性的深度思考与战略创新。"
          },
          {
            q_type: "reading_item",
            stem: "The statutory 'right to disconnect' established in France and other nations ensures that:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Employees cannot be punished for ignoring off-hours work communications." },
              { key: "B", text: "Workers are prohibited from using smartphones inside their private homes." },
              { key: "C", text: "Companies must disconnect electricity to all offices every afternoon." },
              { key: "D", text: "Labor unions possess the legal right to seize corporate computers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出“断连权（right to disconnect）”保障员工在合同约定工时之外有权不接工作电话或邮件，且不受雇主惩罚。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that sustainable professional excellence depends upon:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Balancing high-intensity focus with restorative personal rest." },
              { key: "B", text: "Working eighty hours per week without taking vacation days." },
              { key: "C", text: "Replying to every corporate message within ten seconds." },
              { key: "D", text: "Permanently abandoning all digital communication technology." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结指出卓越不是靠无休止在线实现的，而需要将高强度专注与恢复性休憩（restorative rest）结合起来。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the sociological analysis of modern urban alienation, few concepts have captured the civic imagination as vividly as sociologist Eric Klinenberg's notion of "social infrastructure." In his seminal treatise Palaces for the People, Klinenberg defines social infrastructure as the physical spaces and community organizations that shape our interactions and determine whether social capital develops. Where robust physical infrastructure—bridges, electrical grids, and aqueducts—facilitates the movement of commodities and power, social infrastructure nurtures the trust, cohesion, and civic bonds that prevent democratic societies from disintegrating.

At the pinnacle of vital social infrastructure stands the neighborhood public library. Unlike commercial cafes that require financial purchases or private athletic clubs that impose exclusionary membership fees, public libraries represent universally accessible civic sanctuaries. In an era marked by historic economic inequality and social atomization, libraries welcome everyone: from infants attending early-literacy story hours to impoverished jobseekers drafting resumes, and elderly pensioners escaping sweltering summer heatwaves.

Klinenberg's empirical research illuminates the life-or-death stakes of social infrastructure. Examining the catastrophic 1995 Chicago heatwave, which claimed over seven hundred lives, Klinenberg discovered that neighborhood mortality rates diverged dramatically between demographically identical communities. Neighborhoods with dense social infrastructure—flourishing public libraries, busy commercial sidewalks, and active community parks—experienced vastly lower mortality because vulnerable seniors were connected to active social networks and had safe, air-conditioned public spaces to seek refuge.

Nevertheless, public libraries across the Anglo-American world face relentless fiscal starvation. In times of municipal budget austerity, city councils invariably target library systems for operating hour reductions, staff layoffs, and branch closures. Short-sighted municipal leaders, evaluating public spending through narrow accounting balance sheets, dismiss libraries as sentimental relics made obsolete by digital e-readers.

Starving public libraries of operational capital is catastrophic civic myopia. By transforming public libraries into funded social infrastructure, municipal governments invest in grassroots democratic resilience. Repairing the frayed fabric of our fractured society begins by recognizing that our shared public palaces are not fiscal luxuries, but the indispensable foundation of a compassionate, interconnected civilization.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Sociologist Eric Klinenberg defines 'social infrastructure' as:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Physical spaces and community organizations that cultivate civic trust." },
              { key: "B", text: "Private high-speed fiber-optic telecommunications networks." },
              { key: "C", text: "Commercial shopping centers that maximize retail consumer sales." },
              { key: "D", text: "High-security corporate banking headquarters in financial districts." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出克莱嫩伯格将“社会基础设施（social infrastructure）”界定为塑造人际互动、催生信任与社会资本的物理空间与社区组织。"
          },
          {
            q_type: "reading_item",
            stem: "Public libraries are distinguished from commercial cafes because they:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Are universally accessible sanctuaries that do not demand payment." },
              { key: "B", text: "Sell imported gourmet coffee at half the market price." },
              { key: "C", text: "Forbid anyone without a university degree from entering." },
              { key: "D", text: "Operate exclusively inside private gated suburban estates." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第二段指出不同于咖啡厅的消费门槛，公共图书馆是全民皆可免费进入的平等庇护所（universally accessible sanctuaries）。"
          },
          {
            q_type: "reading_item",
            stem: "Klinenberg's research on the 1995 Chicago heatwave demonstrated that:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Robust social infrastructure significantly reduced mortality rates." },
              { key: "B", text: "Neighborhoods with libraries suffered higher casualty numbers." },
              { key: "C", text: "Air conditioning was completely ineffective against heat exhaustion." },
              { key: "D", text: "Low-income seniors preferred to remain inside sealed apartments." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出对芝加哥热浪的研究表明，拥有完善社会基础设施（如图书馆和活跃公园）的社区老人死亡率大幅降低。"
          },
          {
            q_type: "reading_item",
            stem: "Why do municipal governments frequently cut library funding during budget deficits?",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Short-sighted leaders view libraries through narrow balance sheets." },
              { key: "B", text: "Citizens collectively demand the total demolition of all books." },
              { key: "C", text: "Federal regulations require all city budgets to be spent on highways." },
              { key: "D", text: "Public libraries have reported multi-billion-dollar cash surpluses." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出短视的市政领导仅从狭隘财务账目评估支出，误将图书馆视作在电子书时代过时的情怀遗迹。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that public libraries should be recognized as:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Indispensable foundations of compassionate civic resilience." },
              { key: "B", text: "Commercial properties that should be auctioned to private developers." },
              { key: "C", text: "Antiquated relics that should be replaced with automated vending machines." },
              { key: "D", text: "Exclusive scholarly research institutes closed to the public." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出削减图书馆资金是公民短视，公共图书馆绝非财政奢侈品，而是构筑充满关爱与互联的文明社会不可或缺的基石（indispensable foundation）。"
          }
        ]
      }
    ]
  }
];
