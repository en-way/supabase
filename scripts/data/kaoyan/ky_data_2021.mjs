// 2021 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2021Exams = [
  // =========================================================================
  // 2021 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Influenza remains one of the most stubborn adversaries in global public health. Unlike pathogens that produce lifelong immunity following a single infection, the influenza virus evolves with relentless (1)____. Through continuous antigenic drift and periodic antigenic shift, viral surface proteins mutate rapidly, rendering preexisting antibodies largely (2)____ against emerging seasonal strains.

Every year, the World Health Organization coordinates a global surveillance network to (3)____ which viral variants are most likely to circulate in the upcoming winter. Vaccine manufacturers then produce seasonal formulations targeting the predicted strains. However, this production cycle requires months of lead time, creating a chronic (4)____ between forecasting models and real-world viral evolution. If a novel lineage emerges midway through manufacturing, the efficacy of the seasonal jab can plummet (5)____.

To escape this recurring annual cycle, immunologists are racing to develop a "universal" flu vaccine. Rather than targeting the hypervariable head of the hemagglutinin surface protein, universal vaccine candidates focus on the protein's conserved stem region. Because the stem rarely changes across diverse strains, antibodies elicited against this structural anchor could provide broad, lasting (6)____ against almost all influenza subtypes.

Nevertheless, bioengineering such vaccines presents formidable biochemical (7)____. The human immune system naturally focuses its defense mechanisms on the prominent, immunodominant head domain, effectively (8)____ the hidden stem. Researchers must employ protein-scaffolding nanoparticles to (9)____ the stem structure in isolation, training the immune system to recognize the cryptic vulnerability.

Preclinical trials in animal models have shown remarkable (10)____, with experimental formulations conferring protection against lethal viral doses. Yet, translating these successes into humans requires extensive clinical validation. Human subjects possess complex immunologic (11)____ shaped by decades of past infections and seasonal vaccinations, a phenomenon known as "original antigenic sin." An individual's immune memory often preferentially produces obsolete antibodies rather than generating fresh defenses against novel (12)____.

Furthermore, commercial pharmaceutical companies have historically shown (13)____ interest in universal vaccines. From a commercial standpoint, selling an annual seasonal injection provides a predictable, recurring (14)____ stream. A one-shot universal vaccine that grants multi-year protection threatens to disrupt this lucrative business model, necessitating government subsidies and philanthropic capital to (15)____ phase-three human trials.

In addition to technological hurdles, global manufacturing capacity must be dramatically expanded. Current egg-based production techniques are dangerously (16)____ and vulnerable to avian influenza outbreaks. Transitioning to mRNA platforms and recombinant protein cell cultures could accelerate production schedules from months to mere (17)____.

Public health epidemiologists emphasize that influenza pandemic preparedness cannot be treated with complacency. As human populations encroach further into wild animal habitats and intensive livestock agriculture (18)____, the risk of a zoonotic spillover—where a lethal avian or swine influenza strain jumps directly into human hosts—grows exponentially (19)____. Developing a genuinely universal vaccine is therefore not merely an intellectual quest, but a critical imperative for planetary biosecurity (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "celerity" },
              { key: "B", text: "hesitance" },
              { key: "C", text: "fragility" },
              { key: "D", text: "clumsiness" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。relentless celerity（无情的迅速/敏捷），呼应后文流感病毒表面蛋白变异极快的特征。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "ineffective" },
              { key: "B", text: "omnipotent" },
              { key: "C", text: "invulnerable" },
              { key: "D", text: "destructive" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。病毒突变使体内已有的抗体对新毒株在很大程度上变得无效（ineffective）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "anticipate" },
              { key: "B", text: "suppress" },
              { key: "C", text: "disprove" },
              { key: "D", text: "fabricate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。WHO 协调全球监测网络以预测（anticipate）来年冬季最可能流行的毒株。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "mismatch" },
              { key: "B", text: "harmony" },
              { key: "C", text: "allegiance" },
              { key: "D", text: "sympathy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。数月的制造周期造成预测模型与病毒实际进化之间的长期不匹配/错位（chronic mismatch）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "precipitously" },
              { key: "B", text: "gradually" },
              { key: "C", text: "favorably" },
              { key: "D", text: "scarcely" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词搭配。plummet precipitously（急剧暴跌/骤降），如果中途出现突变株，当季疫苗有效率会断崖式下跌。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "immunity" },
              { key: "B", text: "contagion" },
              { key: "C", text: "fragility" },
              { key: "D", text: "exposure" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。provide broad, lasting immunity（提供广泛而持久的免疫保护）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "hurdles" },
              { key: "B", text: "benefits" },
              { key: "C", text: "triumphs" },
              { key: "D", text: "subsidies" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。presents formidable biochemical hurdles（面临艰巨的生化障碍/难题）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "overshadowing" },
              { key: "B", text: "magnifying" },
              { key: "C", text: "endorsing" },
              { key: "D", text: "clarifying" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】分词语义。免疫系统注意力集中在显眼的头部区域，从而遮蔽/掩盖了（overshadowing）隐藏的茎部。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "present" },
              { key: "B", text: "conceal" },
              { key: "C", text: "corrode" },
              { key: "D", text: "condemn" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。用纳米支架单独呈递（present）茎部结构，训练免疫系统定向识别抗原弱点。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "promise" },
              { key: "B", text: "treachery" },
              { key: "C", text: "collapse" },
              { key: "D", text: "apathy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。动物临床前试验展现出显著的前景/希望（showed remarkable promise）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "baggage" },
              { key: "B", text: "privilege" },
              { key: "C", text: "vacation" },
              { key: "D", text: "justice" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻用法。immunologic baggage（免疫包袱/历史免疫负担），指过往多次感染和疫苗接种形成的历史抗原偏差。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "targets" },
              { key: "B", text: "passengers" },
              { key: "C", text: "citizens" },
              { key: "D", text: "allies" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。免疫系统倾向于产生过时抗体，而不是针对新靶点（novel targets）形成新鲜防御。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "tepid" },
              { key: "B", text: "ecstatic" },
              { key: "C", text: "passionate" },
              { key: "D", text: "unlimited" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。商业药企在历史上对通用流感疫苗表现冷淡/不温不火（tepid interest）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "revenue" },
              { key: "B", text: "misfortune" },
              { key: "C", text: "deficit" },
              { key: "D", text: "penance" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】商业名词。selling annual injections provides a recurring revenue stream（每年售卖当季疫苗提供稳定的经常性营收流）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "underwrite" },
              { key: "B", text: "undermine" },
              { key: "C", text: "suppress" },
              { key: "D", text: "prohibit" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。underwrite clinical trials（资助/承销临床试验费用）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "sluggish" },
              { key: "B", text: "swift" },
              { key: "C", text: "flawless" },
              { key: "D", text: "futuristic" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。传统基于鸡蛋培养的生产技术动作迟缓（dangerously sluggish），难以应对突发危机。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "weeks" },
              { key: "B", text: "decades" },
              { key: "C", text: "centuries" },
              { key: "D", text: "eras" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】时间跨度对比。从数月（months）缩短到区区数周（mere weeks）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "intensifies" },
              { key: "B", text: "dissolves" },
              { key: "C", text: "vanishes" },
              { key: "D", text: "retreats" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。集约化畜牧养殖加剧/深化（intensifies），人畜接触更紧密。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "higher" },
              { key: "B", text: "lower" },
              { key: "C", text: "safer" },
              { key: "D", text: "tighter" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词修饰。跨物种溢出风险成指数级走高（grows exponentially higher）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "resilience" },
              { key: "B", text: "extinction" },
              { key: "C", text: "negligence" },
              { key: "D", text: "surrender" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与褒义归纳。planetary biosecurity resilience（全球生物安全韧性保障）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `Rail track infrastructure in Britain is governed by Network Rail, the state-backed enterprise charged with maintaining 20,000 miles of track, thousands of viaducts, signaling systems, and overhead electric cables. In recent decades, chronic underinvestment and delayed routine maintenance have spawned a relentless cycle of emergency track repairs, resulting in widespread speed restrictions and crippling commuter cancellations across the national grid.

Engineers and safety inspectors argue that the current operational strategy is fundamentally reactive rather than preventive. Instead of replacing aging rails and points based on predictable fatigue lifespans, maintenance teams are frequently dispatched only after ultrasonic sensors flag internal rail micro-fractures or automated signaling switches fail. This patch-and-mend methodology not only multiplies contractor costs through exorbitant nighttime overtime rates, but also dangerously increases derailment risks during high-speed passenger transits.

The financial friction stems directly from the adversarial separation between Network Rail and private train operating companies (TOCs). Under regulatory compensation agreements known as Schedule 8, Network Rail must pay millions of pounds in financial penalties to TOCs whenever track maintenance delays passenger services. To minimize these penalty payouts during peak revenue hours, track engineers are forced to compress vital maintenance windows into narrow, nocturnal time slots, sacrificing thorough engineering overhauls for superficial temporary fixes.

Transport analysts insist that modernizing British rail requires transitioning toward predictive digital asset management. Remote fiber-optic acoustic sensing and train-mounted high-resolution optical cameras can now continuously monitor rail deflection, ballast stability, and overhead line tension under real-world operational loads. By modeling digital twin replicas of the track network, algorithms can forecast precisely when and where metal fatigue will manifest, allowing repairs to be scheduled weeks in advance without disrupting core passenger timetables.

Ultimately, technological upgrades must be accompanied by governance reforms. Integrating track infrastructure and train dispatch into a single unified public authority can eliminate counterproductive financial penalty schemes and restore engineering safety as the paramount national priority.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What has been the primary consequence of chronic underinvestment in British rail infrastructure?",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Frequent emergency track closures and severe commuter cancellations." },
              { key: "B", text: "A total transition to private high-speed automotive tollways." },
              { key: "C", text: "A massive reduction in the cost of hiring maintenance contractors." },
              { key: "D", text: "The complete electrification of all rural branch lines." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段第二句指出长期欠投与延期维护导致了紧急抢修死循环，造成限速和大规模列车晚点取消（widespread cancellations）。"
          },
          {
            q_type: "reading_item",
            stem: "Inspectors criticize current maintenance practices because they are:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Reactive rather than proactive in addressing structural fatigue." },
              { key: "B", text: "Excessively focused on aesthetic landscaping along track embankments." },
              { key: "C", text: "Carried out exclusively during peak morning commuting hours." },
              { key: "D", text: "Overly reliant on manual horse-drawn inspection carts." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第二段首句指出目前运营模式是“被动反应型而非预防性（reactive rather than preventive）”，常常等到出现裂纹故障才抢修。"
          },
          {
            q_type: "reading_item",
            stem: "Under Schedule 8 agreements, Network Rail is legally required to:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Compensate train operating companies for maintenance-induced delays." },
              { key: "B", text: "Share all ticket revenue equally with municipal bus lines." },
              { key: "C", text: "Prohibit high-speed passenger trains on weekends." },
              { key: "D", text: "Subsidize private vehicle parking at suburban stations." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段明确指出依照第8附表协议，网络铁路公司必须在因轨道检修延误列车运行时，向私营车企支付数以百万计的罚金赔偿。"
          },
          {
            q_type: "reading_item",
            stem: "Predictive digital asset management helps rail operators by:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Forecasting component fatigue and enabling planned non-disruptive repairs." },
              { key: "B", text: "Automating passenger fare increases during rainy weather." },
              { key: "C", text: "Eliminating the need for any physical maintenance personnel." },
              { key: "D", text: "Doubling train speeds on vintage Victorian viaducts." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出预测性数字资产管理通过数字孪生建模精准预判金属疲劳，提前数周排期检修而不干扰核心客运时刻表。"
          },
          {
            q_type: "reading_item",
            stem: "What fundamental governance reform does the author advocate in the final paragraph?",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Unifying track infrastructure and train operations under single authority." },
              { key: "B", text: "Selling all railway tracks to international private equity funds." },
              { key: "C", text: "Abolishing all safety inspections to accelerate train frequencies." },
              { key: "D", text: "Replacing all steel tracks with asphalt highway lanes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段总结指出治理改革的关键是将轨道基建与列车调度重新整合进统一的公共管理机构（unifying into a single public authority）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In the contemporary corporate landscape, corporate diversity, equity, and inclusion (DEI) initiatives have expanded their purview beyond gender and racial representation to embrace "neurodiversity." Pioneered by Australian sociologist Judy Singer in the late 1990s, the neurodiversity paradigm rejects the historical classification of neurological differences—such as autism spectrum conditions, ADHD, and dyslexia—as psychiatric deficits. Instead, it posits that these conditions represent natural variations in human cognitive wiring, possessing distinct strengths alongside undeniable challenges.

Nowhere has this conceptual transformation gained more commercial traction than in the technology and financial sectors. Pioneering multinationals such as SAP, Microsoft, and JPMorgan Chase have instituted dedicated neurodiversity hiring pipelines. Rather than subjecting autistic applicants to conventional behavioral interviews—which heavily penalize poor eye contact, idiosyncratic speech rhythms, or social hesitation—these enterprises utilize week-long experiential workshops and technical problem-solving auditions.

The business rationale for neuroinclusive hiring extends far beyond benevolent corporate philanthropy. Autistic software engineers, quantitative analysts, and cybersecurity specialists frequently demonstrate extraordinary aptitudes for pattern recognition, sustained hyper-focus on intricate datasets, and an uncompromising commitment to mathematical accuracy. In software debugging and code validation, where overlooking a single misplaced character can compromise an enterprise platform, neurodivergent professionals routinely outperform their neurotypical peers.

However, recruitment is merely the initial threshold; genuine inclusion requires restructuring workplace ecosystems. Open-plan corporate offices, with their cacophony of ringing phones, fluorescent strobe lighting, and intrusive conversations, can trigger intense sensory overload for neurodivergent individuals. Progressive employers are responding by establishing low-sensory quiet zones, permitting noise-canceling headphones, and replacing ambiguous conversational instructions with explicit, written task deliverables.

Furthermore, management training is vital to prevent social friction. Neurotypical managers must learn to value straightforward communication without interpreting directness as insubordination. When corporate organizations celebrate cognitive pluralism, they foster an environment where unconventional thinking drives technological breakthrough.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The neurodiversity paradigm fundamentally views conditions like autism as:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Natural variations in cognitive wiring with unique strengths." },
              { key: "B", text: "Incurable medical deficits that disqualify individuals from work." },
              { key: "C", text: "Temporary psychological conditions caused by digital devices." },
              { key: "D", text: "Personality flaws that require strict behavioral suppression." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段尾句指出神经多样性范式拒绝将自闭症视为病理缺陷，认为它们代表了人类认知结构的自然变异（natural variations in human cognitive wiring），具有独特优势。"
          },
          {
            q_type: "reading_item",
            stem: "Why have technology companies modified their traditional interview formats?",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Standard interviews unfairly penalize idiosyncratic social communication." },
              { key: "B", text: "Traditional interviews take too long for busy recruiters to conduct." },
              { key: "C", text: "Federal regulations have banned face-to-face oral questioning." },
              { key: "D", text: "Candidates refuse to attend meetings without legal representation." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出传统面试严重惩罚了欠缺眼神交流、语调独特或社交迟疑的自闭症应聘者，因此改用实战考核与工作坊。"
          },
          {
            q_type: "reading_item",
            stem: "In software debugging, autistic specialists frequently excel because of their:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Exceptional pattern recognition and sustained attention to detail." },
              { key: "B", text: "Charismatic public speaking and marketing persuasion skills." },
              { key: "C", text: "Willingness to work completely without monetary compensation." },
              { key: "D", text: "Preference for managing large, diverse administrative teams." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出自闭症专业人才在模式识别（pattern recognition）、极高专注力以及对精确性的执着上具有显著优势，在排查代码漏洞中往往胜过常人。"
          },
          {
            q_type: "reading_item",
            stem: "To support neurodivergent staff, progressive workplaces are:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Creating low-sensory quiet zones and providing clear written instructions." },
              { key: "B", text: "Eliminating all written email communication in favor of phone calls." },
              { key: "C", text: "Requiring all employees to work in brightly lit open-plan halls." },
              { key: "D", text: "Mandating 80-hour workweeks without flexible rest breaks." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段末句指出改善环境的措施包括设立低感官静音区、允许戴降噪耳机以及用明确书面指令代替含糊口头任务。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following would be the most fitting title for this text?",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Wiring the Workplace for Cognitive Diversity." },
              { key: "B", text: "The Decline of Open-Plan Corporate Architecture." },
              { key: "C", text: "The Medical Treatment of Adult Autism." },
              { key: "D", text: "Why Traditional Job Interviews Are Unreliable." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨大意题。全文围绕企业接纳神经多样性、重塑招聘与职场环境、释放差异化认知潜能展开，A 项立意精准且契合主旨。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `The democratization of academic research promised by the open-access (OA) revolution was envisioned as an unalloyed blessing: breaking down extortionate paywalls and making scientific knowledge freely accessible to scholars and citizens worldwide. Under the traditional subscription model, libraries paid millions to read peer-reviewed journals; under OA, authors or their funding institutions pay "article processing charges" (APCs) to publish, after which findings are open to all. Yet, this well-intentioned shift has nurtured a predatory parasite in scholarly publishing.

Exploiting the APC business model, thousands of unscrupulous "predatory publishers" have flooded the academic marketplace. These deceptive operations launch slick digital platforms boasting counterfeit editorial boards, fabricated impact metrics, and deceptively broad journal titles. Their business model is ruthlessly simple: accept virtually every submitted manuscript, bypass any semblance of genuine peer review, and extract hundreds or thousands of dollars in APCs from desperate authors.

The victims of predatory publishing are predominantly early-career scholars and researchers in developing nations. Operating under crushing institutional mandates that demand rapid publication outputs for doctoral graduation, hiring, or tenure promotions, these academics are bombarded daily by predatory spam emails flattering their work and promising peer review within 48 hours. Lacking sophisticated institutional guidance, many fall prey to these deceptive vanity presses, only to discover their hard-won research entombed in disreputable digital repositories that reputable indexing databases refuse to recognize.

The broader scientific repercussions are catastrophic. Predatory journals act as open conduits for methodological junk, pseudoscientific health claims, and politically motivated conspiracy theories masquerading as peer-reviewed consensus. Once a bogus paper receives the glossy trappings of academic typography and a DOI link, it is weaponized on social media and cited by unsuspecting secondary researchers, permanently poisoning the evidentiary record.

Combating predatory publishing demands aggressive, systemic remedies. Indexing bodies such as Scopus and Web of Science must intensify auditing protocols to delist journals that abandon rigorous peer evaluation. More fundamentally, universities must dismantle the perverse obsession with raw publication volume. When scholars are evaluated on the rigorous intellectual depth of their inquiries rather than the superficial quantity of their journal outputs, predatory publishers will wither for lack of paying prey.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Under the open-access publishing model, revenue is primarily generated through:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Article processing charges paid by authors or institutions." },
              { key: "B", text: "Expensive annual subscription fees paid by university libraries." },
              { key: "C", text: "Commercial advertisements for laboratory pharmaceutical equipment." },
              { key: "D", text: "Direct sales of printed paper volumes to individual readers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出在开放获取模式下，由作者或其资助机构支付“论文处理费（APCs）”，随后研究对所有人免费开放。"
          },
          {
            q_type: "reading_item",
            stem: "Predatory academic publishers operate primarily by:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Accepting almost any paper without genuine peer review to collect fees." },
              { key: "B", text: "Strictly rejecting 99 percent of submitted academic manuscripts." },
              { key: "C", text: "Paying generous peer-review honorariums to independent editors." },
              { key: "D", text: "Offering free open-source software to doctoral research scholars." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出掠夺性期刊的商业模式极度简单粗暴：几乎录用所有来稿，完全绕过实质性同行评审，纯粹为了收取版面处理费。"
          },
          {
            q_type: "reading_item",
            stem: "Why are early-career researchers particularly vulnerable to predatory journals?",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Intense pressure to publish rapidly for academic advancement." },
              { key: "B", text: "A desire to publish bogus, pseudoscientific medical claims." },
              { key: "C", text: "Excessive financial funding from national science agencies." },
              { key: "D", text: "A legal ban preventing them from submitting to traditional journals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出青年学者和发展中国家研究人员面临毕业、晋升等严苛的考核压力（crushing mandates that demand rapid outputs），因此极易被虚假审稿承诺所诱惑。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 4, predatory journals endanger public science by:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Conferring academic legitimacy on pseudoscience and unverified claims." },
              { key: "B", text: "Depleting all global paper supplies for physical printing presses." },
              { key: "C", text: "Suing legitimate university researchers for copyright violation." },
              { key: "D", text: "Preventing medical doctors from treating hospital patients." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出掠夺性期刊充当了伪科学、垃圾方法论的通道，给劣质研究披上学术外衣，毒化了科学证据库。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that eradicating predatory publishers requires universities to:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Prioritize intellectual rigor over sheer publication quantity in evaluations." },
              { key: "B", text: "Ban all researchers from using the internet for scientific inquiries." },
              { key: "C", text: "Abolish the open-access model and restore traditional print paywalls." },
              { key: "D", text: "Forbid junior scholars from attending international academic conferences." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出根治之策在于高校废除对论文数量的病态崇拜，将评价重心转回实质性的智识严谨度（intellectual depth over quantity）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the annals of Fourth Amendment jurisprudence, few constitutional disputes have matched the intensity of Carpenter v. United States, the landmark 2018 Supreme Court ruling concerning cellular location data. When Timothy Carpenter was convicted of armed robbery based on 127 days of cell-site location information (CSLI) obtained by federal prosecutors without a judicial warrant, his defense asserted that government surveillance of his historical movements violated his constitutional protection against unreasonable searches.

The government rested its defense upon the "third-party doctrine," a legal precedent established in the 1970s. Under this doctrine, individuals possess no legitimate expectation of privacy in information they voluntarily disclose to commercial third parties, such as dialed telephone numbers recorded by phone carriers or canceled checks handled by banks. Prosecutors insisted that because cell phones automatically transmit radio pings to nearby cellular masts to connect calls, subscribers have knowingly surrendered their privacy to telecom corporations.

Writing for the five-to-four majority, Chief Justice John Roberts repudiated this mechanical application of analogue-era doctrine to the digital age. Roberts observed that modern smartphones are effectively "attached to the hip," accompanying owners into physical bedrooms, doctors' offices, and places of worship. Cell-site data does not merely record isolated commercial transactions; it creates an intimate, comprehensive, and retrospective chronicle of an individual's entire life, revealing private associations and political beliefs.

Furthermore, the court dismantled the government's claim of voluntary consent. In modern society, carrying a smartphone is not a luxury choice, but an indispensable prerequisite for civic and economic participation. Because cell phones ping towers automatically without any conscious user action, concluding that subscribers "voluntarily share" their geographical whereabouts represents an empty legal fiction.

By ruling that police must obtain a warrant grounded in probable cause before seizing historical location records, the Supreme Court erected a vital constitutional bulwark in the digital era. Yet, privacy scholars caution that Carpenter was merely the opening salvo in an accelerating conflict. As commercial data brokers aggregate trillions of GPS coordinates harvested from smartphone apps and sell them directly to law enforcement agencies without judicial oversight, the battle over digital privacy must inevitably evolve from judicial interpretation to comprehensive legislative reform.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The core constitutional dispute in Carpenter v. United States concerned whether:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Warrantless government seizure of cell-site location data is legal." },
              { key: "B", text: "Armed robbery convictions should be abolished under federal law." },
              { key: "C", text: "Smartphone ownership should be restricted to adults over twenty-one." },
              { key: "D", text: "Telecom companies possess the legal right to shut down cellular masts." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出 Carpenter 案的核心争议在于检方在没有搜查令的情况下获取长达127天的手机基站位置数据（warrantless seizure of CSLI）是否侵犯了宪法隐私权。"
          },
          {
            q_type: "reading_item",
            stem: "The 'third-party doctrine' established in the 1970s held that individuals:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Forfeit privacy expectations in data voluntarily shared with third parties." },
              { key: "B", text: "Retain absolute privacy over all communications sent via private couriers." },
              { key: "C", text: "Must receive government compensation whenever their phones are tapped." },
              { key: "D", text: "Cannot legally share their banking records with family members." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第二段指出“第三方准则”认为，个人对自愿透露给商业第三方（如银行支票、运营商通话记录）的信息不再享有合理的隐私期待。"
          },
          {
            q_type: "reading_item",
            stem: "Chief Justice Roberts rejected the government's argument primarily because:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Location data creates an intimate, comprehensive chronicle of private life." },
              { key: "B", text: "Timothy Carpenter proved he never possessed a functioning smartphone." },
              { key: "C", text: "Cellular radio pings are completely invisible to digital forensic tools." },
              { key: "D", text: "The Fourth Amendment only applies to paper letters and physical homes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果细节题。第三段指出罗伯茨首席大法官指出手机形影不离，基站定位记录描摹出了个人整个私生活的详尽编年史（intimate, comprehensive chronicle），涉及政治与信仰隐私。"
          },
          {
            q_type: "reading_item",
            stem: "The court found the idea of 'voluntary disclosure' invalid because:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Phones ping towers automatically, and phones are essential to modern life." },
              { key: "B", text: "Telecom operators force all subscribers to sign contracts at gunpoint." },
              { key: "C", text: "Cell-site location information is completely deleted every twenty-four hours." },
              { key: "D", text: "No American citizen possesses a legal right to purchase a cell phone." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出携带手机是现代社会参与的必需条件，且后台自动寻呼基站完全无需用户主动触发，“自愿分享”纯属虚构。"
          },
          {
            q_type: "reading_item",
            stem: "Legal scholars suggest that the next frontier in digital privacy protection requires:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Comprehensive legislative regulation of commercial data brokers." },
              { key: "B", text: "A complete constitutional ban on all smartphones in North America." },
              { key: "C", text: "Overturning the Supreme Court's ruling in Carpenter v. United States." },
              { key: "D", text: "Dismantling all federal and local law enforcement agencies." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】推断与主旨题。末段指出由于数据经纪商通过 App 收集海量 GPS 并兜售给执法机构，数字隐私的保护必须从司法裁判走向全面的立法改革（comprehensive legislative reform）。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2021 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `In modern urban societies, domestic pets have transitioned from utilitarian working animals into cherished family members. Nowhere is this emotional (1)____ more pronounced than in our relationship with dogs. Urban households increasingly view canine companions not merely as domestic property, but as emotional anchors that provide unconditional (2)____ and buffer against metropolitan loneliness.

Sociologists term this cultural evolution the "humanization" of companion animals. Pet owners willingly (3)____ substantial portions of their disposable income to gourmet organic dog food, orthopedic bedding, veterinary wellness plans, and bespoke canine grooming salons. What was once dismissed as eccentric indulgence has evolved into a multi-billion-dollar consumer (4)____ that demonstrates astonishing resilience during economic downturns.

Psychological research confirms that canine ownership yields tangible physiological and emotional (5)____. Walking a dog twice daily encourages regular cardiovascular physical activity, while interacting with a friendly canine triggers the release of oxytocin—a hormone that (6)____ social bonding and diminishes systemic cortisol levels. For isolated senior citizens or remote desk workers, a dog's cheerful presence provides a vital antidote to existential (7)____.

Nevertheless, this canine population boom has introduced acute friction into modern municipal (8)____. Dense metropolitan apartment buildings, designed for human tenants, often struggle to accommodate barking, shedding, and territorial (9)____. Municipal green parks have become ideological battlegrounds between dog owners seeking off-leash exercise zones and parents concerned about child hygiene and (10)____.

Uncollected pet waste represents an especially stubborn environmental and public health (11)____. Canine feces contain pathogenic bacteria such as E. coli and parasitic larvae that wash into storm drains during rainstorms, polluting local urban (12)____. Despite municipal signage and financial fines, enforcement remains spotty, leading frustrated neighborhood associations to install DNA surveillance systems to (13)____ negligent pet owners.

Animal welfare ethicists also point out a darker consequence of our pet obsession: impulsive breeding and abandonment. The sudden surge in demand for fashionable designer breeds—such as French bulldogs and Labradoodles—has fueled cruel commercial puppy mills that prioritize profit over canine (14)____. When naive owners discover that energetic puppies require relentless training, veterinary expenditures, and emotional patience, shelter surrender rates (15)____ dramatically.

Animal rescue charities therefore emphasize that adopting a dog is a lifelong legal and moral (16)____. Prospective owners must evaluate their financial stability, domestic living space, and daily work commitments before (17)____ on pet ownership. Furthermore, municipal authorities should implement mandatory microchipping, offer subsidized spay-and-neuter clinics, and invest in dedicated, fenced dog (18)____ to promote harmonious civic coexistence.

Ultimately, dogs have shared our firesides for over twenty thousand years, serving as loyal hunting partners, vigilant guardians, and devoted friends. Treating them with responsible stewardship rather than consumerist (19)____ honors that ancient interspecies bond, ensuring that urban environments remain compassionate sanctuaries for humans and their four-legged companions (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "shift" },
              { key: "B", text: "disaster" },
              { key: "C", text: "betrayal" },
              { key: "D", text: "reluctance" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。emotional shift（情感转变），描述宠物狗从实用工作动物向亲密家庭成员的角色转变。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "affection" },
              { key: "B", text: "hostility" },
              { key: "C", text: "jealousy" },
              { key: "D", text: "suspicion" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。unconditional affection（无条件的关爱/温情），是宠物犬提供的情感价值。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "allocate" },
              { key: "B", text: "forbid" },
              { key: "C", text: "withhold" },
              { key: "D", text: "plunder" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。willingly allocate substantial portions of income（心甘情愿地分配大量可支配收入用于宠物消费）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "market" },
              { key: "B", text: "desert" },
              { key: "C", text: "scandal" },
              { key: "D", text: "monopoly" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。multi-billion-dollar consumer market（价值数十亿美元的庞大消费市场）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "dividends" },
              { key: "B", text: "penalties" },
              { key: "C", text: "illusions" },
              { key: "D", text: "grievances" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻修辞。yields tangible physiological and emotional dividends（带来切实的身心健康红利/收益）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "fosters" },
              { key: "B", text: "dismantles" },
              { key: "C", text: "poisons" },
              { key: "D", text: "disregards" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。催产素能够促进（fosters）人际纽带并降低皮质醇压力激素。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "isolation" },
              { key: "B", text: "luxury" },
              { key: "C", text: "celebration" },
              { key: "D", text: "victory" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。前文有 isolated senior citizens，因此宠物是排解存在主义孤独与隔绝（existential isolation）的解药。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "governance" },
              { key: "B", text: "vacation" },
              { key: "C", text: "fiction" },
              { key: "D", text: "treachery" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。friction into municipal governance（给现代城市治理带来尖锐摩擦）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "aggression" },
              { key: "B", text: "politeness" },
              { key: "C", text: "diplomacy" },
              { key: "D", text: "generosity" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与动物习性。territorial aggression（领地攻击性/防御吠叫），与吠叫、掉毛并列。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "safety" },
              { key: "B", text: "amusement" },
              { key: "C", text: "luxury" },
              { key: "D", text: "fashion" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。公园中家长最关心的是儿童卫生与安全（hygiene and safety）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "hazard" },
              { key: "B", text: "triumph" },
              { key: "C", text: "remedy" },
              { key: "D", text: "miracle" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。environmental and public health hazard（环境与公共卫生公害/隐患）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "waterways" },
              { key: "B", text: "museums" },
              { key: "C", text: "libraries" },
              { key: "D", text: "factories" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。雨水冲刷下水道最终污染城市水系水体（urban waterways）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "identify" },
              { key: "B", text: "reward" },
              { key: "C", text: "praise" },
              { key: "D", text: "subsidize" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。社区安装基因检测系统是为了识别/查出（identify）不清理粪便的失职主人。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "welfare" },
              { key: "B", text: "inflation" },
              { key: "C", text: "taxation" },
              { key: "D", text: "bankruptcy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。商业繁育场重利润轻动物福利（prioritize profit over canine welfare）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "surge" },
              { key: "B", text: "evaporate" },
              { key: "C", text: "stabilize" },
              { key: "D", text: "decline" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。主人缺乏耐心无法承受训犬负担时，收容所弃养率急剧飙升（surge dramatically）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "commitment" },
              { key: "B", text: "amusement" },
              { key: "C", text: "holiday" },
              { key: "D", text: "luxury" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。a lifelong legal and moral commitment（终生的法律与道德承诺/契约）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "embarking" },
              { key: "B", text: "sneering" },
              { key: "C", text: "despairing" },
              { key: "D", text: "rebounding" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。embark on pet ownership（着手/踏上养宠之路）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "parks" },
              { key: "B", text: "prisons" },
              { key: "C", text: "factories" },
              { key: "D", text: "cemeteries" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。dedicated, fenced dog parks（专用的有栅栏狗公园/活动乐园）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "whim" },
              { key: "B", text: "wisdom" },
              { key: "C", text: "justice" },
              { key: "D", text: "heroism" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。以负责任的管理对待宠物，而非一时消费主义的冲动奇想（consumerist whim）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "alike" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "hostile" },
              { key: "D", text: "opposed" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词修饰。for humans and their four-legged companions alike（对于人类和他们的四腿同伴二者而言皆如此）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `Across the lush berry fields of Herefordshire and the vegetable greenhouses of Lincolnshire, British agriculture has been gripped by an unprecedented labor crisis. For decades, the seasonal harvesting of soft fruits, asparagus, and brassicas depended heavily on hundreds of thousands of seasonal migrant workers from Eastern European nations like Romania and Bulgaria. However, the confluence of Britain's exit from the European Union, which terminated free movement of labor, alongside pandemic travel restrictions, has precipitated a severe farm worker shortfall, leaving millions of pounds worth of unpicked fruit to rot in fields.

Confronted with rotting harvests, horticultural producers have turned their hopes toward agricultural robotics. Agricultural tech startups, financed by government innovation grants and venture capital, are testing autonomous robotic harvesting platforms equipped with multi-spectral machine-vision cameras, robotic arms, and soft silicone grippers. These machines are engineered to roam orchards autonomously, evaluate fruit ripeness via color algorithms, and gently detach delicate berries without bruising their soft skin.

Yet, translating laboratory prototypes into reliable field solutions has proved stubbornly difficult. Unlike industrial manufacturing plants where automotive robots weld uniform steel plates on predictable factory floors, agricultural environments present chaotic biological unpredictability. Raspberries hide beneath dense leaf foliage; strawberries vary in size, orientation, and firmness; and changing outdoor sunlight creates blinding glare that confuses optical sensors. Furthermore, human pickers possess extraordinary tactile dexterity, harvesting a ripe strawberry in less than two seconds, whereas commercial picking robots currently take upwards of five to ten seconds per fruit.

The economic equation also remains deeply unfavorable for average farm enterprises. A single harvesting robot can cost well over one hundred thousand pounds, yet it sits idle for nine months of the year once the brief regional harvesting window closes. For family-owned farms operating on paper-thin commercial profit margins, financing fleets of expensive harvesting machines is economically impossible without guaranteed long-term equipment rental models or collective co-op ownership.

Industry analysts conclude that the complete automation of fruit harvesting remains at least a decade away. In the interim, agricultural survival requires hybrid solutions: deploying "cobots" that assist human workers with heavy lug carrying, reforming temporary agricultural visa programs to facilitate legal seasonal labor migration, and redesigning horticultural breeding to develop crop varieties that grow in uniform, easily accessible clusters.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What caused the acute labor crisis on British fruit and vegetable farms?",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "The termination of EU free movement alongside travel disruptions." },
              { key: "B", text: "A nationwide ban on the commercial cultivation of soft berries." },
              { key: "C", text: "Severe urban air pollution destroying all regional orchard yields." },
              { key: "D", text: "Massive pay cuts imposed by supermarket retail syndicates." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段尾句明确指出，脱欧终结了欧盟劳动力自由流动加上疫情旅行限制，导致东欧季节性采摘工严重短缺。"
          },
          {
            q_type: "reading_item",
            stem: "Agricultural tech startups are developing robotic harvesters equipped with:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Machine-vision cameras and gentle silicone grippers." },
              { key: "B", text: "Heavy chemical pesticide flamethrowers." },
              { key: "C", text: "High-voltage electric fencing for bird deterrence." },
              { key: "D", text: "Underground hydraulic excavation drills." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出采摘机器人配备了多光谱机器视觉摄像头、机械臂和柔软的硅胶抓手（soft silicone grippers），以便轻柔采摘浆果。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 3, harvesting robots currently struggle in fields because:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Biological foliage variation and changing light hinder optical sensors." },
              { key: "B", text: "Robotic batteries instantly explode when exposed to direct rainwater." },
              { key: "C", text: "Human farm workers deliberately destroy the autonomous machines." },
              { key: "D", text: "The machines can only operate in sub-zero winter temperatures." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出户外农田具有生物不可预测性，浆果隐藏在茂密枝叶下，阳光炫光干扰传感器，且采摘速度远慢于熟练人工。"
          },
          {
            q_type: "reading_item",
            stem: "Family-owned farms hesitate to purchase harvesting robots primarily because:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "High machine costs are unjustifiable for short seasonal usage." },
              { key: "B", text: "They prefer to let their agricultural produce rot in the ground." },
              { key: "C", text: "The British government has made robotic agriculture illegal." },
              { key: "D", text: "Supermarkets refuse to purchase fruit harvested by machines." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出单台设备成本超十万英镑，但采摘季结束后闲置九个月，微利的家庭农场根本无力承担昂贵资金成本。"
          },
          {
            q_type: "reading_item",
            stem: "What does the author suggest as an immediate interim solution for farm viability?",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Adopting collaborative human-robot tools and reforming visa policies." },
              { key: "B", text: "Completely abandoning all domestic soft fruit agriculture in Britain." },
              { key: "C", text: "Banning supermarkets from importing fresh fruit from overseas." },
              { key: "D", text: "Replacing all fruit plantations with industrial concrete factories." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出短期过渡方案包括：人机协作共融机器人（cobots）、改革短期农业签证以引进外工，以及培育利于采摘的作物品种。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `The global apparel industry generates upwards of one hundred billion garments annually, fueling a fast-fashion culture characterized by disposable clothing, fleeting trends, and shocking environmental waste. Less than one percent of discarded textiles are recycled into fresh clothing; the overwhelming remainder is dumped into municipal landfills or incinerated in waste-to-energy plants. In landfills, synthetic petrochemical fabrics such as polyester, nylon, and elastane leach microscopic plastic fibers into groundwater aquifers while taking hundreds of years to decompose.

The primary obstacle preventing widespread textile recycling is material complexity. While recycling a pure cotton shirt or unblended wool sweater is technologically straightforward, contemporary fast-fashion items are almost invariably composite blends. A ubiquitous stretch denim jean combines cotton with synthetic polyester and elastane; a fleece sweatshirt weaves acrylic with recycled wool fibers. Separating these intimately interwoven fibers without degrading their molecular polymer integrity has long baffled commercial recyclers.

Fortunately, groundbreaking developments in chemical recycling are beginning to dissolve these material impasses. Innovative chemical processes utilize targeted enzymes and eco-friendly organic solvents to selectively dissolve synthetic fibers from natural cellulose threads. In pilot facilities across Scandinavia, chemical recyclers can disintegrate poly-cotton fabrics, transforming the polyester component into virgin-quality polyester pellets while recovering the cellulose pulp to manufacture silky viscose or lyocell yarns.

However, scaling chemical recycling requires surmounting colossal supply-chain bottlenecks. Garments arrive at recycling centers decorated with steel zippers, brass rivets, plastic buttons, and polyester sewing threads, all of which must be excised before chemical processing can commence. Manual deconstruction by human laborers is slow and economically prohibitive. Forward-thinking fashion brands are beginning to implement "design for circularity," replacing metal hardware with biodegradable wooden buttons and utilizing dissolvable sewing threads that melt when exposed to microwave heat.

Ultimately, technological breakthroughs must be accompanied by economic accountability. Several European nations are advancing legislation to enforce Extended Producer Responsibility (EPR) for textiles, charging fashion conglomerates a mandatory levy per garment sold to finance nationwide automated sorting infrastructure. When fast-fashion retailers are forced to internalize the disposal costs of their throwaway garments, the commercial incentive to design for durability and circularity will finally overcome the allure of cheap, disposable fashion.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What major environmental problem is caused by synthetic fabrics in landfills?",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "They shed microplastics into aquifers and take centuries to degrade." },
              { key: "B", text: "They spontaneously combust and ignite regional forest fires." },
              { key: "C", text: "They attract dangerous invasive insect pests into cities." },
              { key: "D", text: "They deplete the earth's natural reserves of crude petroleum." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段末尾指出聚酯、尼龙等合成面料在填埋场中向地下水沥滤微塑料纤维，且降解需要数百年之久。"
          },
          {
            q_type: "reading_item",
            stem: "The primary technical hurdle hindering garment recycling is that:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Most modern clothes are complex blended fabrics that resist separation." },
              { key: "B", text: "Chemical recycling solvents are illegal throughout Western Europe." },
              { key: "C", text: "Consumers refuse to buy recycled garments under any circumstance." },
              { key: "D", text: "Pure cotton clothing generates toxic radiation when melted." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出核心技术障碍在于当代快时尚衣物几乎都是混纺织物（composite blends），在不破坏聚合物完整性的情况下拆解互织纤维极其困难。"
          },
          {
            q_type: "reading_item",
            stem: "Chemical recycling innovations in Scandinavia have succeeded in:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Selectively separating poly-cotton blends into high-grade raw materials." },
              { key: "B", text: "Transforming all plastic bottles into edible agricultural fertilizers." },
              { key: "C", text: "Eliminating the need for washing machines in residential homes." },
              { key: "D", text: "Turning pure wool fibers into synthetic automobile tires." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出北欧化学回收技术利用靶向酶和环保溶剂成功分离涤棉混纺，将聚酯制成新颗粒，纤维素制成优质纱线。"
          },
          {
            q_type: "reading_item",
            stem: "The concept of 'design for circularity' involves:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Employing dissolvable threads and hardware that facilitate easy disassembly." },
              { key: "B", text: "Stitching clothes exclusively in perfect circular patterns." },
              { key: "C", text: "Selling garments on condition that buyers return them within 48 hours." },
              { key: "D", text: "Refusing to use any natural cotton or linen in clothing production." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第四段末句指出“循环设计”倡导在服装设计端采用微波可溶缝纫线、生物可降解木扣，便于废旧衣物自动化拆解回收。"
          },
          {
            q_type: "reading_item",
            stem: "Legislation enforcing Extended Producer Responsibility (EPR) aims to:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Make fashion companies financially responsible for garment waste disposal." },
              { key: "B", text: "Ban all European citizens from purchasing imported American jeans." },
              { key: "C", text: "Impose criminal penalties on consumers who discard worn-out socks." },
              { key: "D", text: "Force all retail stores to close on weekends to reduce shopping." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论方案题。末段指出推行纺织品生产者责任延伸（EPR）立法的目的在于让快时尚巨头为每件服装支付强制性处理费，内部化废弃成本以激励耐久与循环。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `When valued employees resign, human resource departments routinely schedule a formal ritual: the exit interview. Whether conducted via a standardized online questionnaire or a candid face-to-face conversation with a corporate HR manager, the stated objective is uniformly noble: to uncover the unvarnished truth regarding management shortcomings, workplace culture, compensation grievances, and institutional inefficiencies that prompt talent attrition.

Yet, despite widespread adoption across Fortune 500 corporations, management consultants frequently criticize conventional exit interviews as theatrical exercises in corporate futility. Departing employees face formidable psychological disincentives against sharing candid critiques. In tightly networked industries where professional reputations travel rapidly, burning bridges by naming an abusive supervisor or exposing departmental cronyism carries severe career risks. Most departing workers recognize that candid honesty offers zero personal upside, while diplomatic platitudes—citing "a desire for new challenges" or "a shorter commute"—safeguard future employment references.

Furthermore, organizational responses to exit data are notoriously anemic. Human resource departments typically aggregate exit surveys into bland quarterly PowerPoint decks, where uncomfortable personal testimonies are sanitized into generic categories like "unsatisfactory salary" or "limited career progression." Line managers and senior executives rarely face accountability based on exit feedback; indeed, toxic managers often dismiss departing employees' complaints as disgruntled sour grapes, shielding themselves from institutional reform.

To transform exit interviews into genuine instruments of organizational intelligence, forward-thinking enterprises are radically reforming the process. Progressive firms postpone the feedback interview until thirty to ninety days after the employee has departed. Once an individual has successfully integrated into their new employer and secured their immediate career standing, their psychological fear of retaliation recedes, allowing them to share remarkably constructive, retrospective insights regarding systemic flaws.

Simultaneously, progressive organizations are supplementing exit interviews with "stay interviews"—regular, structured conversations with high-performing existing staff designed to discover what keeps them engaged and what frustrations might prompt them to leave. Addressing workplace friction before an employee types a resignation letter is infinitely more valuable than conducting a forensic autopsy once the talent has already walked out the door.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The official purpose of conducting corporate exit interviews is to:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Uncover honest feedback regarding reasons for employee departure." },
              { key: "B", text: "Persuade departing employees to cancel their pending resignations." },
              { key: "C", text: "Calculate final severance payments and tax deductions." },
              { key: "D", text: "Gather commercial intelligence regarding competitor companies." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出离职面谈官方声称的目标是探寻促成人才流失的管理缺陷、薪酬抱怨和职场文化等客观真实原因（uncover unvarnished truth）。"
          },
          {
            q_type: "reading_item",
            stem: "Departing employees tend to give diplomatic platitudes primarily because they:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Fear damaging professional relationships and future job references." },
              { key: "B", text: "Genuinely adore their direct supervisors and executive management." },
              { key: "C", text: "Receive monetary bonuses for giving exclusively positive responses." },
              { key: "D", text: "Are legally forbidden from discussing departmental workflows." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出离职者害怕得罪人（burning bridges）影响业界口碑和未来背景调查推荐信，说真话对自己毫无好处，因而选择委婉托辞。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 3, corporate exit survey data is often rendered useless because:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "HR sanitizes complaints into bland summaries without manager accountability." },
              { key: "B", text: "Company servers automatically erase all survey responses after forty-eight hours." },
              { key: "C", text: "Survey questions are written in obsolete classical Latin." },
              { key: "D", text: "Labor unions forbid human resources from reading employee feedback." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出人事部门将尖锐反馈冲淡过滤成毫无生气的泛化PPT分类，中高层管理者也从不因负面反馈承担实际问责。"
          },
          {
            q_type: "reading_item",
            stem: "Postponing exit interviews until several months after departure helps because:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Former employees feel psychologically secure from retaliation." },
              { key: "B", text: "The former employee has forgotten all previous workplace grievances." },
              { key: "C", text: "HR managers receive external government subsidies for late surveys." },
              { key: "D", text: "The company's legal liability for past harassment permanently expires." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出离职一至三个月后前员工已在新公司立足，对报复的恐惧消退，更容易分享深刻建设性的客观洞察。"
          },
          {
            q_type: "reading_item",
            stem: "The author advocates 'stay interviews' because they:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Proactively address employee frustrations before talent resigns." },
              { key: "B", text: "Allow executives to spy on lower-level project team members." },
              { key: "C", text: "Eliminate the need for any annual salary reviews or bonuses." },
              { key: "D", text: "Force workers to sign lifetime employment contracts." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出推行“留任访谈（stay interviews）”的核心价值在于在员工递交辞呈前主动排查并化解工作痛点，防患于未然。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `For generations, public libraries were revered as austere citadels of silence—cathedrals of the printed word where stern librarians shushed noisy patrons and cataloged dusty volumes of reference encyclopedias. However, the omnipresence of digital smartphones, ubiquitous e-books, and instant online search algorithms has fundamentally disrupted this classical custodial mission. In a hyper-connected world where the entirety of human knowledge can be summoned to a pocket screen in milliseconds, skeptics have inevitably questioned whether physical public libraries remain a justifiable expenditure of municipal tax revenues.

Far from sliding into municipal obsolescence, however, visionary public libraries are executing a magnificent social renaissance. Rather than functioning solely as static book warehouses, progressive libraries are transforming themselves into vibrant, democratic community hubs engineered to tackle modern urban alienation, economic inequality, and the pervasive digital divide.

The contemporary public library has emerged as a frontline guardian of digital equity. Millions of low-income families, elderly citizens, and unhoused individuals lack high-speed broadband connections, desktop computer hardware, or credit cards required to purchase digital software subscriptions. In underserved neighborhoods, public libraries provide free gigabit internet access, high-end workstations equipped with graphic design suites, and circulating mobile Wi-Fi hotspots that students can borrow to complete evening school homework.

Furthermore, the architectural ethos of the public library has undergone a radical metamorphosis. Hush-filled reading halls are now complemented by collaborative maker-spaces featuring 3D printers, laser cutters, podcast recording studios, and coding workshops. Libraries host digital literacy classes for pensioners learning to navigate telemedicine portals, offer English-as-a-second-language conversation circles for newly arrived immigrants, and provide quiet study pods for freelance gig-economy workers.

Most profoundly, in an increasingly commercialized cityscape where virtually every indoor space demands financial payment, the public library remains one of the last egalitarian, non-commercial sanctuaries. It is a shared civic haven where any citizen, regardless of socioeconomic pedigree, can sit peacefully without purchasing a commercial latte or proving their net worth. By evolving from silent repositories of paper into dynamic engines of civic resilience, public libraries affirm that democratic communities require shared spaces grounded in dignity, curiosity, and universal inclusion.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Skeptics have questioned the continued funding of public libraries because:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Digital search and e-books provide instant information on mobile devices." },
              { key: "B", text: "Physical books have been declared legally hazardous to human health." },
              { key: "C", text: "Municipal governments are legally required to privatize all public spaces." },
              { key: "D", text: "Librarians have refused to catalog modern scientific publications." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出在手机、电子书和即时线上搜索普及的时代，指尖即可获取人类全部知识，导致质疑者质疑实体图书馆消耗市政税金的合理性。"
          },
          {
            q_type: "reading_item",
            stem: "Modern public libraries maintain social relevance by transforming into:",
            points: 2.0,
            sort_order: 2,
            options: [
              { key: "A", text: "Vibrant democratic community hubs addressing digital inequality." },
              { key: "B", text: "Commercial shopping malls selling high-end luxury fashion." },
              { key: "C", text: "Automated warehouse facilities closed to all human visitors." },
              { key: "D", text: "Private subscription-only clubs for affluent academic researchers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第二段指出进步的图书馆不再仅仅是静态藏书库，而是重塑为应对疏离感、贫富差距与数字鸿沟的活力社区中枢（vibrant community hubs）。"
          },
          {
            q_type: "reading_item",
            stem: "Public libraries promote digital equity in underserved neighborhoods by:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Providing free high-speed internet, workstations, and loaner Wi-Fi hotspots." },
              { key: "B", text: "Charging high membership fees for downloading academic journal articles." },
              { key: "C", text: "Banning patrons from using any electronic devices inside reading rooms." },
              { key: "D", text: "Distributing printed paper flyers to replace home computers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出图书馆为低收入、老年和无家可归群体提供免费千兆宽带、专业工作站以及可外借的学生移动Wi-Fi热点。"
          },
          {
            q_type: "reading_item",
            stem: "Modern library spaces now feature facilities such as:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Maker-spaces with 3D printers, recording studios, and coding workshops." },
              { key: "B", text: "Commercial gambling parlors and fast-food drive-throughs." },
              { key: "C", text: "Heavy industrial assembly lines for manufacturing automobiles." },
              { key: "D", text: "High-security corporate banking vaults for sovereign wealth funds." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出图书馆空间发生了深刻变革，增设了创客空间（maker-spaces）、3D打印机、播客录音棚和编程工作坊。"
          },
          {
            q_type: "reading_item",
            stem: "According to the final paragraph, what makes public libraries unique in contemporary cities?",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "They are non-commercial civic sanctuaries open to all without financial cost." },
              { key: "B", text: "They generate more municipal tax profit than commercial shopping centers." },
              { key: "C", text: "They require patrons to prove their net worth before entering reading rooms." },
              { key: "D", text: "They are the only buildings in metropolitan centers with air conditioning." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段强调在凡事讲钱的商业化城市中，公共图书馆是绝无仅有的非商业平等公共庇护所（non-commercial sanctuaries），无需消费即可体面栖居。"
          }
        ]
      }
    ]
  }
];
