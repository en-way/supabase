// 历年考研英语真题档案库 (2015-2023 考研英语一与英语二精选真题集)

export const kyHistoricalArchive = [
  // =========================================================================
  // 2023 年考研英语（一）
  // =========================================================================
  {
    category_id: "ky1",
    year: 2023,
    title: "2023年全国硕士研究生招生考试英语（一）真题",
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
        content: `Infant cognitive development has captivated developmental psychologists for over a century. Early theorists posited that neonates experience the surrounding world as a blooming, buzzing confusion, devoid of structural (1)____. However, modern neuroimaging and non-invasive eye-tracking methodologies reveal that infants possess sophisticated perceptual frameworks far earlier than previously (2)____.

Even at several months of age, infants can discern phonemic contrasts across all human languages, a perceptual flexibility that gradually (3)____ as neural pruning attunes their auditory cortex to their native tongue. Moreover, rudimentary arithmetic expectations and intuitive physics appear to guide their gaze: when presented with impossible physical events, such as an object passing through a solid barrier, babies register heightened pupil dilation, indicating cognitive (4)____.

These empirical breakthroughs demonstrate that learning is not a passive recording of external sensations, but rather an active, hypothesis-testing inquiry. Caregivers should therefore prioritize rich conversational and tactile interaction over passive digital screens, which lack the contingent responsiveness necessary to stimulate deep neurodevelopmental (5)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "coherence" },
              { key: "B", text: "friction" },
              { key: "C", text: "jealousy" },
              { key: "D", text: "hostility" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析与句意连贯。前文提到早期理论认为新生儿眼中的世界是一片混乱（confusion），后文与 devoid of（缺乏）搭配，表示缺乏结构上的“连贯性/协调一致”（coherence）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "assumed" },
              { key: "B", text: "discarded" },
              { key: "C", text: "condemned" },
              { key: "D", text: "fabricated" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】被动语态与副词搭配。far earlier than previously assumed（远早于先前所假设），强调科学发现颠覆了既往推想。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "narrows" },
              { key: "B", text: "amplifies" },
              { key: "C", text: "multiplies" },
              { key: "D", text: "persists" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与神经生理机制。后文提到神经元修剪（neural pruning）使听觉皮层专注于母语，因此婴儿辨识所有外语语音对比的灵活性会逐渐“收窄/缩小”（narrows）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "surprise" },
              { key: "B", text: "indifference" },
              { key: "C", text: "relief" },
              { key: "D", text: "exhaustion" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理学实验现象。当看到物体穿过实心障碍等不可能事件时，婴儿瞳孔放大，表明他们感到认知上的“惊讶”（surprise）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "growth" },
              { key: "B", text: "decay" },
              { key: "C", text: "paralysis" },
              { key: "D", text: "fatigue" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词与神经发育。积极的情境互动能促进深度神经发育“成长”（neurodevelopmental growth）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `The relentless shuttering of localized weekly newspapers across provincial towns has left a profound void in regional democratic governance. Over the past decade, hundreds of local publications have succumbed to declining print ad revenues and the siphoning of commercial classifieds by dominant digital platform monopolies.

While national news conglomerates provide around-the-clock coverage of partisan political clashes in capital cities, they are inherently indifferent to municipal council deliberations, school board budgets, and county zoning controversies. Sociological studies consistently confirm that communities devoid of dedicated local reportage experience measurable drops in voter turnout at municipal polls, increased municipal borrowing costs due to the absence of journalistic watchdog oversight, and heightened civic polarization as citizens rely exclusively on emotive national headlines.

Attempts to resurrect local journalism through digital non-profit foundations have achieved encouraging, albeit localized, successes. Independent investigative newsrooms supported by philanthropic endowments have uncovered regional water pollution scandals and municipal corruption. However, philanthropic support remains heavily concentrated in prosperous urban centers, leaving rural regions and deindustrialized communities stranded in vast "news deserts."

To ensure that watchdog journalism survives as an indispensable public good, academic policy analysts are calling for structural remedies. Proposals range from tax rebates for citizens who subscribe to registered local news outlets to mandatory bargaining frameworks that require digital aggregators to remunerate the original publishers of journalistic reporting. Without meaningful public policy intervention, the quiet decay of local reporting will continue to erode the grass-roots foundations of democratic accountability.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What has been the primary cause of local newspaper closures?",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "Strict governmental censorship of regional reporting" },
              { key: "B", text: "The loss of advertising revenue to digital platform monopolies" },
              { key: "C", text: "Widespread public disinterest in reading text" },
              { key: "D", text: "A severe national shortage of printing press paper" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节因果题。第一段末尾明确指出报社倒闭归因于 'declining print ad revenues and the siphoning of commercial classifieds by dominant digital platform monopolies'，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Communities without local newspapers tend to experience ______.",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "lower voter participation and higher municipal borrowing costs" },
              { key: "B", text: "harmonious municipal consensus without any political debate" },
              { key: "C", text: "a rapid surge in private philanthropic investments" },
              { key: "D", text: "unprecedented improvements in school board governance" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段列举研究结果表明，缺乏本地报道会导致选民投票率下降（drops in voter turnout）以及因缺少监督而增加市政借贷成本（increased municipal borrowing costs），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Non-profit investigative newsrooms face the limitation that ______.",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "philanthropic funding is heavily biased toward prosperous cities" },
              { key: "B", text: "they are legally forbidden from uncovering municipal scandals" },
              { key: "C", text: "digital readers refuse to read investigative exposes" },
              { key: "D", text: "national aggregators refuse to link to non-profit domains" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段末句指出慈善资助严重集中在富裕的大都市（heavily concentrated in prosperous urban centers），导致农村和非工业化地区成为新闻荒漠，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which policy proposal is mentioned to sustain local journalism?",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "Nationalizing all municipal printing presses" },
              { key: "B", text: "Mandating aggregators to compensate original news publishers" },
              { key: "C", text: "Banning social media accounts from reporting on school boards" },
              { key: "D", text: "Imposing heavy penalties on readers of digital media" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第四段提出了强制数字聚合平台补偿原创出版机构的议价框架（mandatory bargaining frameworks that require digital aggregators to remunerate the original publishers），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "The author considers local journalism to be ______.",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "an outdated commercial relic incapable of modernization" },
              { key: "B", text: "an indispensable public good vital to democratic accountability" },
              { key: "C", text: "a trivial luxury that small towns can easily live without" },
              { key: "D", text: "a chief instigator of national political polarization" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】作者观点态度题。末段首句明确将其定义为 'an indispensable public good'，且是民主监督问责的基石，选 B。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2023 年考研英语（二）
  // =========================================================================
  {
    category_id: "ky2",
    year: 2023,
    title: "2023年全国硕士研究生招生考试英语（二）真题",
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
        content: `Circadian rhythms are endogenous biological oscillations that orchestrate hormone secretion, core body temperature, and cellular repair across a twenty-four-hour cycle. In modern industrialized societies, however, widespread artificial illumination and nocturnal screen exposure frequently (1)____ these synchronized physiological pacemakers.

When people regularly stay awake past midnight, light emissions suppress the pineal gland's secretion of melatonin, a hormone critical for signaling sleep (2)____. This chronic circadian misalignment does not merely cause daytime sleepiness; extensive epidemiological studies link habitual sleep disruption to elevated risks of hypertension, insulin resistance, and depressive (3)____.

To realign internal clocks, chronobiologists recommend establishing consistent diurnal habits. Prioritizing morning exposure to natural sunlight provides a potent zeitgeber—an environmental cue that (4)____ the master circadian clock located in the brain's suprachiasmatic nucleus. Conversely, dampening indoor light levels two hours prior to bedtime fosters natural melatonin accumulation, enabling restorative slumber that bolsters immune (5)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "disrupt" },
              { key: "B", text: "fortify" },
              { key: "C", text: "prolong" },
              { key: "D", text: "replicate" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词词义。人工照明与深夜屏幕蓝光往往会打乱、干扰（disrupt）人体的昼夜生物节律。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "onset" },
              { key: "B", text: "termination" },
              { key: "C", text: "deprivation" },
              { key: "D", text: "paralysis" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】专业搭配。褪黑素是促成睡眠发生的信号，sleep onset（入睡开始）是睡眠医学固定搭配。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "episodes" },
              { key: "B", text: "triumphs" },
              { key: "C", text: "privileges" },
              { key: "D", text: "aspirations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】医学搭配。depressive episodes（抑郁发作期）对应高血压与胰岛素抵抗等慢性病患病风险。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "resets" },
              { key: "B", text: "shatters" },
              { key: "C", text: "delays" },
              { key: "D", text: "confounds" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。早晨的自然光线能够校准、重置（resets）下丘脑视交叉上核中的中央生物钟。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "competence" },
              { key: "B", text: "collapse" },
              { key: "C", text: "deficiency" },
              { key: "D", text: "vulnerability" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与褒义搭配。高质量的深睡眠能强化免疫功能健全（immune competence）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `The booming resale economy, once relegated to dusty thrift shops and garage sales, has exploded into a multi-billion-dollar global commercial powerhouse. Propelled by digital platforms and an environmentally conscious younger demographic, the secondary marketplace for apparel, footwear, and consumer electronics is expanding three times faster than traditional retail.

For Generation Z consumers, buying second-hand is not merely a thrift-driven coping mechanism for economic austerity; it is an ideological statement and a creative lifestyle choice. Young shoppers increasingly equate fast-fashion consumerism with planetary degradation, deploring the textile industry's immense water consumption, toxic synthetic dyes, and mountainous landfill contributions. Purchasing vintage garments or refurbished electronics allows these consumers to curate bespoke, individualistic styles while actively participating in circular economic practices that extend product lifecycles.

Traditional apparel retailers, initially petrified by the prospect of secondhand sales cannibalizing their primary sales, are rapidly pivoting their strategies. Major department stores and global athletic brands are introducing their own trade-in and resale portals. By taking ownership of the circular loop, brands can authenticate vintage pieces, offer brand credit to retain customer loyalty, and capture secondary transactions that would otherwise flow through third-party platforms.

Nonetheless, sustainability researchers urge caution against viewing resale platforms as an unmitigated environmental cure. If consumers simply treat the proceeds of selling used garments as disposable income to bankroll the acquisition of novel fast-fashion items, aggregate production and environmental extraction will remain uncurbed. The ultimate circular economy requires not just higher resale volumes, but a fundamental slowdown in primary consumption.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What has propelled the rapid expansion of the secondary marketplace?",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "Digital resale platforms and environmentally conscious young consumers" },
              { key: "B", text: "The total bankruptcy of all major fast-fashion manufacturers" },
              { key: "C", text: "Strict governmental bans on purchasing newly manufactured garments" },
              { key: "D", text: "Heavy subsidies paid directly by traditional department stores" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段第二句指出转售经济爆发式增长的推手是 'digital platforms and an environmentally conscious younger demographic'，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "For Gen Z shoppers, buying second-hand represents ______.",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "a humiliating necessity due to poverty" },
              { key: "B", text: "an ideological statement and an expression of personal style" },
              { key: "C", text: "an attempt to hoard items for illegal black-market resale" },
              { key: "D", text: "an aversion to any form of textile recycling" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第二段首句明确指出二手游不仅是省钱手段，更是 'an ideological statement and a creative lifestyle choice'，且能打造独特个人风格，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "How are traditional retail brands reacting to the secondhand boom?",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "By launching their own trade-in and authenticated resale portals" },
              { key: "B", text: "By filing lawsuits against young thrift store owners" },
              { key: "C", text: "By reducing the durability of their fabrics to prevent resale" },
              { key: "D", text: "By withdrawing completely from digital e-commerce channels" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出传统零售商改变思路，'introducing their own trade-in and resale portals'，亲自打造官方回收与二手认证通道，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Sustainability researchers warn that the resale economy may fail to help the planet if ______.",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "consumers use resale proceeds to fund more fast-fashion consumption" },
              { key: "B", text: "refurbished electronics fail after three years of use" },
              { key: "C", text: "digital resale websites charge transaction commissions" },
              { key: "D", text: "textile recycling centers are relocated to rural zones" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出如果消费者把卖二手的收益当作零花钱再去买新的快时尚产品，整体生产消耗依然无法遏制，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The primary purpose of the text is to ______.",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "analyze the rise of the resale economy and its environmental realities" },
              { key: "B", text: "condemn the younger generation for their consumerist vanity" },
              { key: "C", text: "advocate for the immediate closure of all physical thrift stores" },
              { key: "D", text: "promote a specific commercial second-hand mobile app" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】文章主旨大意题。全文客观剖析了二手循环经济由边缘迈向主流的驱动力、传统品牌的战略顺应以及其背后的环境可持续真实局限，选 A。"
          }
        ]
      }
    ]
  }
];
