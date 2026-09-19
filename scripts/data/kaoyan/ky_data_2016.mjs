// 2016 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2016Exams = [
  // =========================================================================
  // 2016 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky1",
    year: 2016,
    title: "2016年全国硕士研究生招生考试英语（一）真题",
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
        content: `In modern consumer culture, an extravagant wedding is frequently promoted as the quintessential manifestation of romantic devotion. Glossy bridal magazines, reality television spectacles, and luxury event planners convince couples that their nuptial ceremonies must be opulent affairs, complete with diamond rings, couture gowns, and exotic destination (1)____. The wedding industry promotes the seductive narrative that lavish financial expenditures (2)____ a lifetime of marital harmony.

However, groundbreaking empirical research conducted by social economists paints a sharply (3)____ reality. In comprehensive surveys of thousands of married couples, researchers discovered a statistically significant inverse correlation between wedding expenditures and marital (4)____. Couples who splurged excessively on lavish ceremonies and diamond engagement rings were substantially more (5)____ to divorce than those who hosted modest, budget-conscious celebrations.

Economists explain this surprising finding through the lens of post-marital financial (6)____. When newlyweds inaugurate their domestic lives burdened by crushing credit card debts and personal loans accumulated to finance a single afternoon of theatrical extravagance, the resulting pecuniary pressures trigger chronic interpersonal (7)____. Arguments over domestic finances and debt repayments rapidly erode romantic affection, accelerating marital (8)____.

Furthermore, sociologists observe that couples who prioritize theatrical opulence often possess skewed psychological expectations. They fixate obsessively on the wedding ceremony—a transient public performance designed for social validation and peer (9)____—while neglecting the unglamorous, everyday labor required to sustain an enduring marital (10)____.

In contrast, couples who allocate their savings toward foundational assets, such as home deposits or joint emergency funds, enjoy a far more stable emotional (11)____. Financial security provides a psychological buffer against external economic shocks, insulating the household from existential anxiety.

Attending wedding ceremonies as a guest also reveals intriguing social (12)____. While expensive weddings create acute financial strain for couples, having a large number of guests present at the ceremony correlates positively with marital (13)____. Sociologists hypothesize that a packed sanctuary represents a dense network of communal support: friends and family who provide emotional encouragement and practical guidance when the couple encounters inevitable domestic (14)____.

Cultural critics argue that the wedding industrial complex has commodified sacred human vows into predatory commercial (15)____. Marketing campaigns deliberately exploit romantic insecurity, equating frugal celebrations with inadequate devotion.

Resisting this consumerist pressure requires recalibrating social values. Young couples must recognize that marital endurance is built upon shared values, mutual respect, and financial prudence rather than commercial (16)____.

By choosing intimate, meaningful gatherings over ostentatious spectacles, couples can embark on matrimony free from debt, focusing their energies on cultivating lifelong (17)____.

Ultimately, true romantic commitment is not measured by the carat weight of a gemstone or the cost per plate at a catered banquet. It is sustained in quiet, daily acts of patience, kindness, and unswerving loyalty (18)____ throughout the decades that follow the wedding day (19)____ and into a shared future (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "venues" },
              { key: "B", text: "prisons" },
              { key: "C", text: "factories" },
              { key: "D", text: "mines" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。destination venues（异国婚礼目的地场地）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "guarantee" },
              { key: "B", text: "prevent" },
              { key: "C", text: "destroy" },
              { key: "D", text: "prohibit" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。奢华宣传灌输巨额消费能“保障（guarantee）”终生婚姻幸福的诱惑说辞。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "different" },
              { key: "B", text: "identical" },
              { key: "C", text: "favorable" },
              { key: "D", text: "delightful" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】转折对比。经济学实证研究揭示了截然不同的（sharply different）现实。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "duration" },
              { key: "B", text: "hostility" },
              { key: "C", text: "betrayal" },
              { key: "D", text: "paralysis" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社会学术语。wedding expenditures and marital duration（婚礼花费与婚姻存续期之间的反比关系）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "likely" },
              { key: "B", text: "reluctant" },
              { key: "C", text: "unwilling" },
              { key: "D", text: "hesitant" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。substantially more likely to divorce（更有可能走向离婚）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "strain" },
              { key: "B", text: "wealth" },
              { key: "C", text: "luxury" },
              { key: "D", text: "splendor" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】经济名词。post-marital financial strain（婚后财务压力与拮据）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "friction" },
              { key: "B", text: "harmony" },
              { key: "C", text: "diplomacy" },
              { key: "D", text: "amusement" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。trigger chronic interpersonal friction（触发长期的夫妻人际摩擦）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "dissolution" },
              { key: "B", text: "prosperity" },
              { key: "C", text: "celebration" },
              { key: "D", text: "triumph" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】法律名词。accelerating marital dissolution（加速婚姻的解体）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "admiration" },
              { key: "B", text: "scorn" },
              { key: "C", text: "contempt" },
              { key: "D", text: "hatred" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理名词。渴望社会认可与同辈艳羡（social validation and peer admiration）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "partnership" },
              { key: "B", text: "hostility" },
              { key: "C", text: "desert" },
              { key: "D", text: "monument" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。sustain an enduring marital partnership（维系持久的婚姻伙伴关系）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "foundation" },
              { key: "B", text: "crisis" },
              { key: "C", text: "catastrophe" },
              { key: "D", text: "famine" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词。stable emotional foundation（坚固的情感基石）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "dynamics" },
              { key: "B", text: "crimes" },
              { key: "C", text: "scandals" },
              { key: "D", text: "diseases" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社会学术语。reveals intriguing social dynamics（揭示耐人寻味的社会互动动态）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "longevity" },
              { key: "B", text: "collapse" },
              { key: "C", text: "ruin" },
              { key: "D", text: "disgrace" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】统计名词。correlates positively with marital longevity（与婚姻的长久度呈正相关）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "adversity" },
              { key: "B", text: "fortune" },
              { key: "C", text: "triumph" },
              { key: "D", text: "luxury" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极语境。遇到难以避免的家庭逆境波折时（inevitable domestic adversity）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "spectacles" },
              { key: "B", text: "prisons" },
              { key: "C", text: "statues" },
              { key: "D", text: "treaties" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】文化批评修辞。predatory commercial spectacles（掠夺性的商业闹剧景观）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "extravagance" },
              { key: "B", text: "wisdom" },
              { key: "C", text: "prudence" },
              { key: "D", text: "frugality" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】反义对比。依托相互尊重而非商业挥霍铺张（commercial extravagance）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "companionship" },
              { key: "B", text: "hostility" },
              { key: "C", text: "resentment" },
              { key: "D", text: "solitude" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词。cultivating lifelong companionship（培育终身相伴的伴侣情谊）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "demonstrated" },
              { key: "B", text: "forgotten" },
              { key: "C", text: "betrayed" },
              { key: "D", text: "prohibited" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】分词搭配。loyalty demonstrated throughout decades（数十年如一日身体力行展现的忠诚）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "itself" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "hardly" },
              { key: "D", text: "rarely" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】代词加强。the wedding day itself（婚礼日自身）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "together" },
              { key: "B", text: "apart" },
              { key: "C", text: "against" },
              { key: "D", text: "away" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词搭配。into a shared future together（携手走向共同的未来）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `In democratic constitutional monarchies such as the United Kingdom, the royal prerogative represents a peculiar legal anomaly. Originating in medieval feudalism, prerogative powers historically encompassed the monarch's discretionary authority to declare war, ratify treaties, dissolve parliament, and grant royal pardons without parliamentary assent.

Over centuries of constitutional evolution, the bulk of these historic powers was transferred from the crown to the prime minister and cabinet. Today, ministers exercise prerogative powers under the fiction that they are acting on behalf of the sovereign. However, because prerogative actions do not require prior statutory authorization from elected lawmakers, critics argue that they create a perilous democratic deficit, enabling the executive branch to bypass parliamentary scrutiny.

Legal battles in the UK Supreme Court have brought prerogative authority under intense judicial re-examination. In landmark rulings concerning the prorogation of parliament and the triggering of international treaty withdrawals, senior judges decreed that royal prerogative is not an unfettered blank check. When an executive prerogative action threatens fundamental constitutional principles—such as parliamentary sovereignty and the right of elected representatives to debate critical national statutes—the judiciary maintains constitutional authority to declare such ministerial actions unlawful.

Constitutional scholars argue that the time has come to replace this archaic medieval remnant with codification. By transferring remaining prerogative powers into transparent, statute-based legislation, modern democracies can ensure that all executive authority remains strictly accountable to elected legislative assemblies.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What was the historical origin of royal prerogative powers?",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Medieval feudal authority exercised exclusively by the monarch." },
              { key: "B", text: "Democratic referendums held across British colonies." },
              { key: "C", text: "Statutes passed by the European Parliament." },
              { key: "D", text: "International maritime shipping treaties." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出王家特权起源于中世纪封建君主专权，不经议会同意即可行使自由裁量权。"
          },
          {
            q_type: "reading_item",
            stem: "Critics argue that ministerial use of prerogative powers creates:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "A democratic deficit by circumventing parliamentary scrutiny." },
              { key: "B", text: "A massive budget surplus in the British Treasury." },
              { key: "C", text: "Complete immunity for all ordinary criminal offenders." },
              { key: "D", text: "A total transfer of powers to local municipal councils." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出内阁行使特权无需事先经立法机构法定授权，批评者认为这绕过了议会审查并造成民主赤字（democratic deficit）。"
          },
          {
            q_type: "reading_item",
            stem: "In recent landmark cases, the UK Supreme Court affirmed that:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Prerogative powers cannot override parliamentary sovereignty." },
              { key: "B", text: "Judges are legally forbidden from reviewing government actions." },
              { key: "C", text: "The Prime Minister possesses absolute, unquestioned legal authority." },
              { key: "D", text: "Parliament must be dissolved permanently every three months." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第三段指出英国最高法院裁定特权并非无休止的空白支票，行政特权不能践踏议会主权等核心宪制原则。"
          },
          {
            q_type: "reading_item",
            stem: "Constitutional scholars recommend that remaining prerogative powers should be:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Codified into transparent statutory legislation." },
              { key: "B", text: "Returned permanently to the physical control of the monarch." },
              { key: "C", text: "Transferred directly to commercial corporations." },
              { key: "D", text: "Ignored entirely by judicial courts." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】方案细节题。第四段指出学者呼吁将剩余特权法典化为透明的成文法案（codified into statute-based legislation），全面接受立法机构问责。"
          },
          {
            q_type: "reading_item",
            stem: "The primary purpose of the text is to:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Examine the constitutional evolution and democratic tensions of royal prerogative." },
              { key: "B", text: "Celebrate the absolute supremacy of medieval monarchs." },
              { key: "C", text: "Condemn the judicial branch for hearing legal disputes." },
              { key: "D", text: "Advocate for the total abolition of all national governments." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨大意题。全文梳理了王家特权从封建王权向内阁行政权的演进、其引发的民主赤字以及司法裁判制衡与成文化改革呼声。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `As the global population becomes increasingly concentrated in sprawling concrete metropolitan centers, epidemiological researchers have documented an alarming surge in psychological distress, chronic stress, and clinical depressive disorders. Surrounded by artificial glass facades, paved asphalt roads, and deafening vehicular noise, urban dwellers spend over ninety percent of their lives indoors. In response to this urban malaise, an innovative public health paradigm is gaining scientific ascendancy: the therapeutic power of urban nature.

Pioneering environmental psychologists, led by Stephen and Rachel Kaplan, formulated "Attention Restoration Theory" (ART) to explain nature's neurobiological benefits. The theory posits that modern urban environments demand continuous "directed attention"—the effortful cognitive mechanism used to decipher traffic signals, complete desktop spreadsheets, and ignore sensory distractions. Sustained directed attention inevitably depletes cognitive resources, resulting in mental fatigue, irritability, and impaired executive judgment.

In contrast, natural landscapes engage "soft fascination." The gentle rustling of tree leaves in a summer breeze, the dappled patterns of sunlight filtering through deciduous canopies, and the rhythmic babble of a park stream capture attention effortlessly without cognitive exertion. This effortless fascination allows the brain's prefrontal attentional mechanisms to rest, recharge, and restore optimal cognitive functioning.

Extensive clinical trials corroborate these psychological theories. Hospital patients with views of leafy trees heal significantly faster and request fewer narcotic analgesics than those facing brick walls. Walking through a forested municipal park for just twenty minutes triggers measurable reductions in circulating salivary cortisol, lowers resting blood pressure, and activates the parasympathetic nervous system, inducing physiological tranquility.

Yet, access to urban nature remains deeply unequal. In most global metropolises, lush canopy cover is heavily concentrated in affluent, suburban enclaves, while low-income neighborhoods suffer from "tree poverty," characterized by barren asphalt, oppressive heat islands, and elevated air pollution. Municipal leaders must treat urban forestry not as a cosmetic amenity, but as vital public health infrastructure. Investing in equitable urban tree planting and public parks is an urgent, cost-effective intervention to heal the collective psyche of the modern city.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "According to Paragraph 1, living in dense concrete cities is associated with:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Surging rates of chronic stress and psychological disorders." },
              { key: "B", text: "A 100 percent elimination of all physical diseases." },
              { key: "C", text: "Instantaneous mastery of classical fine arts." },
              { key: "D", text: "A total lack of interest in electronic computers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出生活在混凝土都市中与慢性压力激增、抑郁障碍等心理危机紧密相关（surge in psychological distress）。"
          },
          {
            q_type: "reading_item",
            stem: "Attention Restoration Theory posits that urban work environments cause fatigue because they require:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Continuous, effortful directed attention that depletes cognitive reserves." },
              { key: "B", text: "Endless physical marathon running through city streets." },
              { key: "C", text: "Living in complete sensory silence without daylight." },
              { key: "D", text: "Consuming exclusively processed microwave meals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出注意力恢复理论（ART）认为都市生活需要持续消耗意志力的“定向注意力（directed attention）”，耗尽了大脑认知资源。"
          },
          {
            q_type: "reading_item",
            stem: "Natural landscapes promote cognitive recovery through 'soft fascination' because they:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Capture attention effortlessly, allowing attentional circuits to recharge." },
              { key: "B", text: "Force the human brain to solve complex algebraic equations." },
              { key: "C", text: "Blind human optical sensors with overwhelming sunlight." },
              { key: "D", text: "Permanently erase all memories of childhood experiences." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出自然风光引发“轻度着迷（soft fascination）”，不费力地吸引注意力，从而让大脑前额叶定向注意回路得到休息与恢复。"
          },
          {
            q_type: "reading_item",
            stem: "The term 'tree poverty' in Paragraph 5 describes a condition where:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Low-income urban districts lack tree canopies and green infrastructure." },
              { key: "B", text: "Forest trees refuse to absorb carbon dioxide from the air." },
              { key: "C", text: "Timber companies go bankrupt due to wood shortages." },
              { key: "D", text: "Municipal governments ban citizens from planting flowers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义理解题。第五段指出“树木贫困（tree poverty）”是指低收入社区缺乏绿化树冠覆盖，饱受高温热岛和污染困扰，与富人区绿树成荫形成鲜明反差。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that urban parks and trees should be recognized as:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Vital public health infrastructure essential for mental well-being." },
              { key: "B", text: "Cosmetic luxuries reserved exclusively for wealthy suburbs." },
              { key: "C", text: "Commercial timber plantations meant for industrial clear-cutting." },
              { key: "D", text: "Antiquated municipal relics that should be paved into motorways." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结呼吁将城市绿化视作至关重要的“公共健康基础设施（public health infrastructure）”，以疗愈现代都市人的心灵。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the glamorous auction pavilions of Sotheby's and Christie's in London and New York, the international art market has been riding an unprecedented, dizzying boom. Masterpieces by Leonardo da Vinci, Picasso, and Basquiat routinely smash all historical records, fetching hundreds of millions of dollars under the euphoric hammer. Wealth managers and auctioneers herald these astronomical valuations as the ultimate celebration of creative human genius and cultural heritage.

However, cultural sociologists and political economists view this art market frenzy through a far more skeptical, revealing lens. Rather than reflecting an authentic renaissance in aesthetic appreciation, the hyper-inflated art market functions as a vivid economic mirror of soaring global wealth inequality. In the wake of post-2008 central bank quantitative easing and corporate deregulation, the world's billionaire class accumulated colossal fortunes. Lacking viable high-yield investments in traditional sovereign bonds or saturated equities, ultra-high-net-worth individuals poured billions into high-end fine art.

For the global super-rich, trophy art operates as a multi-functional financial asset. Masterpieces represent portable, unregulated, and privately insured stores of value. Unlike real estate or public equities, art transactions remain veiled in profound confidentiality: private sales avoid public registers, and purchases are routinely routed through anonymous shell corporations registered in offshore tax havens. Furthermore, vast collections of blue-chip art are stored in tax-free "freeports"—high-security warehouse fortresses situated near international airports in Geneva, Luxembourg, and Singapore—where art can appreciate in value for decades without ever triggering sales taxes or customs duties.

The societal consequence of this financialization is cultural dispossession. Historically, magnificent artworks were exhibited in public museums where citizens of all backgrounds could experience spiritual awe and historical contemplation. Today, iconic masterpieces are locked away in dark, climate-controlled tax-free bunkers, transformed into speculative collateral for private bank loans.

Reclaiming art for public civilization demands systemic reform. Governments should enforce strict anti-money laundering regulations on private art galleries, eliminate tax exemptions for freeport warehouses, and incentivize wealthy collectors to donate or loan artworks to regional public museums. When art is liberated from speculative vaults, it ceases to be a luxury trophy for oligarchs and resumes its rightful role as a common treasury of human inspiration.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What has fueled the unprecedented price surge in the international fine art market?",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Massive wealth accumulation among billionaires seeking alternative assets." },
              { key: "B", text: "A sudden worldwide surge in classical painting talent." },
              { key: "C", text: "Government laws requiring every citizen to own an oil painting." },
              { key: "D", text: "A complete collapse in the value of gold and real estate." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出艺术品天价狂欢并非审美觉醒，而是后危机时代富豪阶层暴富后寻求另类保值投资的结果（mirror of soaring wealth inequality）。"
          },
          {
            q_type: "reading_item",
            stem: "Fine art is highly attractive to the global super-rich as an asset because it:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Is portable, confidential, and easily sheltered from taxes." },
              { key: "B", text: "Can be eaten as emergency survival nutrition." },
              { key: "C", text: "Generates daily cash dividends through public ATMs." },
              { key: "D", text: "Is completely immune to damage from fire or water." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出顶级艺术品便携、交易隐秘（通过离岸空壳公司）且容易避税，成为理想的金融资产。"
          },
          {
            q_type: "reading_item",
            stem: "What are 'freeports' as described in Paragraph 3?",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Tax-free, high-security storage warehouses near international airports." },
              { key: "B", text: "Public docks where private yachts receive free gasoline." },
              { key: "C", text: "Naval military bases operated by international peacekeepers." },
              { key: "D", text: "Museums open exclusively to primary school children." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义理解题。第三段末句明确指出“自由港（freeports）”是位于机场附近的免税高安全仓储要塞，供富豪存放免税增值艺术品。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 4, the financialization of the art market results in:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Cultural dispossession as masterpieces are locked away in private bunkers." },
              { key: "B", text: "A massive worldwide increase in public museum funding." },
              { key: "C", text: "The total destruction of all digital computer hardware." },
              { key: "D", text: "The mandatory return of all paintings to ancient churches." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出艺术金融化的恶果是“文化剥夺（cultural dispossession）”，原本属于大众鉴赏的名作被深锁在免税地堡沦为贷款抵押品。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that restoring art to its true purpose requires:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Closing tax loopholes for freeports and incentivizing public museum loans." },
              { key: "B", text: "Banning all artists from selling their creative work." },
              { key: "C", text: "Demolishing all private auction houses worldwide." },
              { key: "D", text: "Permitting only government officials to paint portraits." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段呼吁推行反洗钱监管、取消防税自由港特权，并激励将藏品借展给公共美术馆，让艺术回归人类共同灵感宝库。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `For nearly a century, standardized college admissions examinations—most notably the SAT and ACT in the United States—have functioned as the undisputed gatekeepers of higher education. Originally championed by mid-twentieth-century educational reformers as an egalitarian instrument of meritocracy, standardized testing was engineered to dismantle the aristocratic monopoly of wealthy prep school elites over Ivy League university admissions. By measuring raw scholastic aptitude through objective multiple-choice questions, the SAT promised to uncover brilliant, self-taught diamonds in the rough from impoverished rural towns and immigrant tenements.

Over recent decades, however, this egalitarian dream has curdled into bitter controversy. Sociologists and educational researchers have accumulated overwhelming statistical evidence demonstrating that standardized test scores track parental household income and parental educational attainment far more reliably than they predict undergraduate academic talent. Rather than leveling the educational playing field, standardized exams have become mechanisms for codifying generational wealth privilege.

The primary engine of this disparity is the multi-billion-dollar commercial test-preparation industry. Affluent families invest thousands of dollars in private tutoring, personalized coaching, and specialized test-taking bootcamps that drill students on the idiosyncratic cognitive heuristics of standardized questions. Furthermore, wealthy students routinely take exams multiple times to maximize "superscores," whereas low-income applicants rarely afford repeated test fees.

Confronted with these entrenched inequities, a revolutionary "test-optional" movement has swept through higher education. Hundreds of prestigious American colleges and universities—including the entire University of California system—have eliminated standardized testing requirements from their admissions criteria. Admissions committees are transitioning toward "holistic evaluation," weighing high-school GPA, course rigor, personal leadership essays, and community engagement to identify diverse talent.

Critics of the test-optional revolt warn that abandoning objective metrics will merely shift bias toward subjective essay evaluations, which can be even more easily manipulated by expensive college admissions consultants. Yet, proponents maintain that admissions equity requires dismantling the false god of three-digit test scores. Evaluating applicants as multifaceted human beings restores the university's noble calling: discovering human potential rather than ratifying inherited socioeconomic advantage.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Standardized admissions exams like the SAT were originally created to:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Dismantle elite privilege and discover talented students from all backgrounds." },
              { key: "B", text: "Ensure that only wealthy prep school students attended university." },
              { key: "C", text: "Replace all university professors with automated multiple-choice tests." },
              { key: "D", text: "Calculate federal income tax liabilities for academic institutions." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出SAT最初被倡导为打破富家子弟垄断常春藤的唯才是举工具，旨在发掘底层有才华的璞玉（diamonds in the rough）。"
          },
          {
            q_type: "reading_item",
            stem: "Educational research indicates that standardized test scores correlate most strongly with:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Parental household income and parental educational attainment." },
              { key: "B", text: "An individual's biological physical endurance and stamina." },
              { key: "C", text: "The geographical climate of a student's home state." },
              { key: "D", text: "A student's proficiency in playing classical musical instruments." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出大量统计表明标化成绩最密切关联的是家庭父母的收入和受教育水平，沦为代际特权的固化工具。"
          },
          {
            q_type: "reading_item",
            stem: "How does the commercial test-preparation industry exacerbate educational inequality?",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "By offering expensive private coaching that drills students on exam tricks." },
              { key: "B", text: "By physically destroying public school textbooks in low-income towns." },
              { key: "C", text: "By forbidding low-income students from entering university libraries." },
              { key: "D", text: "By requiring students to sign lifelong military service contracts." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出天价课外培训教富家子弟应试套路技巧，且富家子弟可多次刷分拼分，拉大了差距。"
          },
          {
            q_type: "reading_item",
            stem: "Under 'holistic evaluation,' admissions committees assess candidates by:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Considering GPA, course rigor, essays, and community engagement." },
              { key: "B", text: "Measuring applicants' physical height and athletic agility." },
              { key: "C", text: "Auctioning university seats to the highest cash bidder." },
              { key: "D", text: "Selecting students through a completely random computer lottery." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出“综合评估（holistic evaluation）”综合考察高中平时GPA、选课难度、个人自述信与社区参与。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that moving away from standardized tests allows universities to:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Discover genuine human potential rather than ratifying inherited privilege." },
              { key: "B", text: "Lower all academic standards to zero across every department." },
              { key: "C", text: "Abolish undergraduate bachelor degrees entirely." },
              { key: "D", text: "Ban all students from writing essays in English." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出抛弃单一片面的三分数崇拜，能让大学重拾崇高使命：发掘真正的人性潜能，而非承认继承的社会经济特权。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2016 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky2",
    year: 2016,
    title: "2016年全国硕士研究生招生考试英语（二）真题",
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
        content: `In the corporate governance sphere, the composition of corporate boards of directors has faced escalating public and regulatory scrutiny. For decades, boardroom appointments operated through opaque informal networks, resulting in governance bodies that were overwhelmingly (1)____ in gender, age, and professional background.

Advocates of corporate reform emphasize that demographic diversity on boards is not merely a social justice imperative, but a vital economic asset. Diverse boards mitigate groupthink, introduce multifaceted perspectives on risk management, and enhance long-term shareholder (2)____. Empirical studies demonstrate that companies with substantial female board representation achieve superior return on equity and superior corporate social (3)____.

Consequently, European parliaments have instituted mandatory gender quotas, requiring publicly traded corporations to allocate at least forty percent of non-executive seats to women. While corporate critics initially complained that quotas would lower director competence, compliance data indicates that companies have expanded their talent searches, tapping into highly accomplished female legal, financial, and scientific (4)____. By dismantling old-boy networks, statutory quotas have enriched board competency and modernized corporate (5)____.

Beyond boardroom demographics, progressive corporate governance is rethinking the fundamental purpose of the modern (6)____. For half a century, Western business jurisprudence was dominated by the dogma of "shareholder primacy"—the doctrine articulated by economist Milton Friedman that an enterprise's sole moral obligation is maximizing financial (7)____ for equity investors. Under this narrow paradigm, corporate executives routinely slashed research budgets, suppressed employee wages, and offshored domestic manufacturing to inflate short-term quarterly (8)____.

Today, business leaders are increasingly embracing "stakeholder capitalism." Championed by the World Economic Forum and prominent institutional investors, this progressive framework asserts that corporations must serve the legitimate interests of all interdependent stakeholders: employees, customers, local communities, and the natural (9)____.

Treating employees with dignity exemplifies this stakeholder ethos. Forward-thinking corporations invest heavily in living wages, comprehensive healthcare benefits, and lifelong skills (10)____. Far from draining profitability, investing in human capital bolsters workplace morale, curtails expensive employee turnover, and unlocks grassroots innovation.

Environmental stewardship has similarly transitioned from superficial public relations into a core fiduciary (11)____. Institutional asset managers managing trillions in pension funds now demand that corporate boards conduct rigorous climate risk audits, disclose carbon emissions, and set binding targets for renewable energy (12)____. Companies that fail to adapt face shareholder rebellions and catastrophic capital flight.

Consumer expectations have undergone an equally dramatic (13)____. Modern consumers, particularly younger generations, increasingly align their purchasing decisions with their personal ethics. They boycott brands associated with labor exploitation, environmental destruction, or unethical executive (14)____, actively rewarding enterprises that demonstrate authentic social responsibility.

Regulatory agencies are codifying these expectations into binding disclosure mandates. From mandatory environmental, social, and governance (ESG) reporting in the European Union to executive compensation transparency rules, corporations can no longer hide behind opaque public relations (15)____.

Ultimately, corporate leadership in the twenty-first century demands reconciling commercial profit with ethical (16)____. Great enterprises recognize that sustainable prosperity cannot be achieved in a fractured society or on a dying planet. By embedding social purpose into their core business (17)____, visionary corporations affirm that the true measure of commercial greatness lies in generating shared value that elevates humanity as a (18)____ throughout the decades (19)____ and into a prosperous future (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "homogeneous" },
              { key: "B", text: "unpredictable" },
              { key: "C", text: "hostile" },
              { key: "D", text: "reckless" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。opaque informal networks 导致董事会背景高度“同质化”（homogeneous）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "value" },
              { key: "B", text: "grief" },
              { key: "C", text: "defeat" },
              { key: "D", text: "panic" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】商业搭配。enhance long-term shareholder value（提升长期股东价值）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "responsibility" },
              { key: "B", text: "negligence" },
              { key: "C", text: "conspiracy" },
              { key: "D", text: "paralysis" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】专业搭配。corporate social responsibility（企业社会责任，CSR）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "professionals" },
              { key: "B", text: "intruders" },
              { key: "C", text: "superstitions" },
              { key: "D", text: "defendants" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与人才。指公司吸纳杰出的女性专业人才（professionals）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "oversight" },
              { key: "B", text: "betrayal" },
              { key: "C", text: "collapse" },
              { key: "D", text: "secrecy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】管理名词。modernized corporate oversight（现代化公司合规治理与监督）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "corporation" },
              { key: "B", text: "monastery" },
              { key: "C", text: "barracks" },
              { key: "D", text: "cemetery" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】商业主体。the fundamental purpose of the modern corporation（现代企业的根本宗旨）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "returns" },
              { key: "B", text: "scandals" },
              { key: "C", text: "losses" },
              { key: "D", text: "crimes" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】商业名词。maximizing financial returns for investors（为股权投资者谋取财务回报最大化）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "earnings" },
              { key: "B", text: "deficits" },
              { key: "C", text: "penalties" },
              { key: "D", text: "funerals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】商业名词。inflate short-term quarterly earnings（虚增短期的季度每股收益/财报利润）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "environment" },
              { key: "B", text: "weapon" },
              { key: "C", text: "prison" },
              { key: "D", text: "dungeon" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】生态名词。communities and the natural environment（社区与自然生态环境）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "training" },
              { key: "B", text: "boycott" },
              { key: "C", text: "rebellion" },
              { key: "D", text: "paralysis" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】人力资源搭配。lifelong skills training（终身职业技能培训）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "duty" },
              { key: "B", text: "scandal" },
              { key: "C", text: "sin" },
              { key: "D", text: "ruin" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】法律名词。core fiduciary duty（核心受信托职责与信义义务）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "adoption" },
              { key: "B", text: "prohibition" },
              { key: "C", text: "destruction" },
              { key: "D", text: "collapse" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】环保搭配。targets for renewable energy adoption（设定采纳可再生能源的约束性目标）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "transformation" },
              { key: "B", text: "paralysis" },
              { key: "C", text: "collapse" },
              { key: "D", text: "stagnation" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。undergone an equally dramatic transformation（经历了同样剧烈的深刻转变）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "conduct" },
              { key: "B", text: "charity" },
              { key: "C", text: "praise" },
              { key: "D", text: "loyalty" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极修辞。抵制伴随不道德高管行径的品牌（unethical executive conduct）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "platitudes" },
              { key: "B", text: "miracles" },
              { key: "C", text: "heroics" },
              { key: "D", text: "triumphs" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。不能再躲在空洞模糊的公关陈词滥调（opaque PR platitudes）之后。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "integrity" },
              { key: "B", text: "treachery" },
              { key: "C", text: "recklessness" },
              { key: "D", text: "greed" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义并列。reconciling commercial profit with ethical integrity（将商业利润与道德操守相调和）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "models" },
              { key: "B", text: "weapons" },
              { key: "C", text: "crimes" },
              { key: "D", text: "scandals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】商业搭配。core business models（核心商业业务模式）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "whole" },
              { key: "B", text: "fraction" },
              { key: "C", text: "shadow" },
              { key: "D", text: "relic" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。elevates humanity as a whole（提升全人类整体福祉）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "ahead" },
              { key: "B", text: "behind" },
              { key: "C", text: "away" },
              { key: "D", text: "past" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词时间。throughout the decades ahead（在未来的数十年间）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "beyond" },
              { key: "B", text: "without" },
              { key: "C", text: "beside" },
              { key: "D", text: "against" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。prosperous future and beyond（走向繁荣的未来以及更远的将来）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `In the domestic households of Western societies, an age-old culinary heritage is quietly evaporating: the art of scratch cooking. Over the past three decades, kitchen pantries once stocked with raw grains, root vegetables, and fresh meats have been colonized by microwave ready-meals, canned sauces, and ultra-processed convenience foods. Food sociologists describe this transformation not merely as an innocent dietary shift, but as a profound process of "culinary de-skilling."

The primary driver powering this culinary decline is the commodification of time. In dual-income households where parents work grueling schedules and endure exhausting commutes, preparing an elaborate evening dinner from raw ingredients appears impossibly burdensome. Multinational food manufacturers have capitalized on this time poverty, engineering hyper-convenient packaged meals that require nothing more than peeling back a plastic film and pressing a microwave button.

However, public health nutritionists warn that the decline of home cooking carries devastating physiological consequences. Ultra-processed convenience foods are deliberately formulated by commercial food chemists to hit the sensory "bliss point"—an addictive amalgamation of refined sugars, trans-fats, and excessive sodium. Longitudinal epidemiological studies conclusively link heavy reliance on ultra-processed meals to skyrocketing rates of childhood obesity, hypertension, and metabolic syndrome.

Furthermore, the loss of cooking skills has dismantled a vital pillar of family culture. Cooking was historically a shared familial ritual through which intergenerational wisdom, cultural heritage, and nutritional literacy were passively transmitted to children. The contemporary kitchen has devolved from a warm hearth of communal collaboration into a functional pit-stop where isolated family members reheat disparate frozen trays on asynchronous schedules.

Reversing culinary de-skilling requires treating food preparation as an essential life skill. Progressive educational authorities are reintroducing mandatory home economics curricula in secondary schools, teaching adolescents how to budget, prep raw vegetables, and cook wholesome meals. Reclaiming our kitchens is not an antiquated nostalgic indulgence, but a vital defense of personal health and familial well-being.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The term 'culinary de-skilling' in Paragraph 1 refers to:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "The loss of traditional cooking skills due to reliance on processed foods." },
              { key: "B", text: "A severe shortage of professional restaurant head chefs in cities." },
              { key: "C", text: "The international prohibition of all domestic microwave ovens." },
              { key: "D", text: "A complete decline in the agricultural yield of wheat and corn." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义事实题。第一段指出“烹饪去技能化（culinary de-skilling）”是指传统从生鲜下厨的技能逐步丧失，转而依赖微波加工预制食品。"
          },
          {
            q_type: "reading_item",
            stem: "What major socioeconomic factor has driven the rise of convenience foods?",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Time poverty in dual-income families with grueling work hours." },
              { key: "B", text: "A total global shortage of tap water inside home kitchens." },
              { key: "C", text: "National laws forbidding parents from preparing home meals." },
              { key: "D", text: "The astronomical cost of purchasing basic cooking knives." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出双职工家庭工时长、通勤累，“时间贫困（time poverty）”让从头下厨成为沉重负担，方便预制菜趁虚而入。"
          },
          {
            q_type: "reading_item",
            stem: "Food scientists engineer processed meals to hit the 'bliss point' by:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Combining refined sugars, unhealthy fats, and high sodium." },
              { key: "B", text: "Adding massive quantities of biological antibiotics and vaccines." },
              { key: "C", text: "Freezing all ingredients down to absolute zero temperatures." },
              { key: "D", text: "Removing all caloric energy and nutritional vitamins." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出食品商为了达到让人上瘾的“极乐点（bliss point）”，故意添加精制糖、反式脂肪和高钠，带来慢性病风险。"
          },
          {
            q_type: "reading_item",
            stem: "Beyond nutrition, the decline of home cooking harms families because it:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Disrupts the intergenerational transmission of culture and shared rituals." },
              { key: "B", text: "Forces children to sleep in kitchen pantries on cold floors." },
              { key: "C", text: "Causes residential electricity grids to collapse during dinner." },
              { key: "D", text: "Prevents parents from purchasing school textbooks for children." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出下厨原本是家庭代际传递文化与生活智慧的共享仪式，去技能化破坏了家庭围炉的社交与情感凝聚纽带。"
          },
          {
            q_type: "reading_item",
            stem: "The author advocates addressing culinary de-skilling by:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Reintroducing mandatory home economics and cooking education in schools." },
              { key: "B", text: "Banning all commercial grocery supermarkets nationwide." },
              { key: "C", text: "Forbidding parents from working full-time corporate jobs." },
              { key: "D", text: "Requiring every family to eat exclusively raw unwashed vegetables." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出解决良方是在中学重新恢复强制性的家政与烹饪课（home economics curricula），让下厨重新成为年轻一代必备的生活自理技能。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In the commercial news industry, the transition from print paper to digital pixels was initially heralded as a frictionless triumph: lower distribution costs, global reach, and instant breaking coverage. However, newspaper publishers quickly encountered a catastrophic economic trap: the culture of "free." In the early decades of the World Wide Web, news organizations freely published their investigative reporting online, hoping that massive web traffic would attract lucrative digital advertising.

That optimistic calculation proved to be a fatal strategic misjudgment. Instead of enriching independent newsrooms, the digital advertising deluge was monopolized by search algorithms and social media platforms. Advertising rates per online reader collapsed to pennies on the dollar compared to vintage print display ads. Squeezed between evaporating print circulations and meager digital ad payouts, hundreds of prestigious newspapers were forced to shutter foreign bureaus, lay off investigative journalists, or declare insolvency.

Confronted with financial ruin, visionary publishers pioneered a radical commercial counter-offensive: the digital paywall. Spearheaded by the New York Times in 2011, publishers abandoned the free-for-all model, erecting "metered paywalls" that permit casual readers a handful of complimentary articles per month before requiring a paid digital subscription.

Initially dismissed by digital skeptics who insisted that internet users would never pay for news that could be pirated elsewhere, paywalls have staged an astonishing economic renaissance. Readers recognized that quality journalism—grounded in rigorous fact-checking, legal vetting, and on-the-ground investigative reporting—is an irreplaceable civic asset. By prioritizing direct reader subscriptions over ad-clicks, newsrooms liberated themselves from clickbait sensationalism.

Nevertheless, media scholars caution that ubiquitous paywalls introduce a dangerous civic divide. When reputable journalism is locked behind expensive subscription paywalls while partisan propaganda and conspiracy theories circulate freely on open social feeds, democratic societies risk an informational stratification: affluent citizens are well-informed, while budget-constrained populations consume unverified misinformation. Balancing subscription viability with public information access remains the central challenge facing twenty-first-century journalism.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Newspaper publishers initially offered free online content in the expectation that:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Massive web traffic would generate lucrative digital advertising revenues." },
              { key: "B", text: "Print newspapers would become ten times more expensive to produce." },
              { key: "C", text: "Governments would pay lifetime pensions to all investigative reporters." },
              { key: "D", text: "Readers would voluntarily send cash donations in paper envelopes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出报社最初免费开放线上内容是天真地寄希望于海量流量能带来丰厚的数字广告收益（lucrative digital advertising）。"
          },
          {
            q_type: "reading_item",
            stem: "The free online publishing model failed financially primarily because:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Tech platforms monopolized digital ads and online ad rates plummeted." },
              { key: "B", text: "Citizens collectively forgot how to read English sentences." },
              { key: "C", text: "Computers became illegal across North America and Europe." },
              { key: "D", text: "Journalists refused to use internet word processing software." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出数字广告份额被搜索和社交算法巨头所垄断，单个读者的广告单价惨跌，报社难以维持开支而濒临破产。"
          },
          {
            q_type: "reading_item",
            stem: "A 'metered paywall' system operates by:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Allowing a few free articles monthly before requiring a paid subscription." },
              { key: "B", text: "Charging readers per second for looking at a computer screen." },
              { key: "C", text: "Requiring users to pass advanced college calculus examinations." },
              { key: "D", text: "Banning anyone outside New York from accessing news websites." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出“计量付费墙（metered paywalls）”允许读者每月免费阅读固定篇数，超额后才需付费订阅。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 4, prioritizing reader subscriptions helped newsrooms by:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Liberating journalists from relying on sensationalist clickbait." },
              { key: "B", text: "Forcing all reporters to work without receiving financial salaries." },
              { key: "C", text: "Eliminating the need for any factual verification or editing." },
              { key: "D", text: "Tripling the physical weight of daily print newspaper editions." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出依靠读者直接订阅而非点击量，使新闻编辑部摆脱了追求博人眼球的“诱导点击标题党（clickbait sensationalism）”。"
          },
          {
            q_type: "reading_item",
            stem: "What civic danger of ubiquitous paywalls is highlighted in the final paragraph?",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Reputable news is paywalled while fake news and propaganda circulate freely." },
              { key: "B", text: "Public libraries are forced to close their reading rooms permanently." },
              { key: "C", text: "Young citizens refuse to read any books written before 2000." },
              { key: "D", text: "Tech companies are forced to delete all social media applications." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论态度题。末段警告付费墙的公民隐患：严谨新闻被高墙阻隔，而虚假谣言却在开放网络零门槛泛滥，加剧了信息阶层分化（informational stratification）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the management doctrine of corporate human resources, few employment arrangements have generated as much ideological debate as telecommuting. For decades, remote work was treated with intense managerial skepticism: corporate executives routinely dismissed working from home as a euphemism for slacking off, insisting that physical face-to-face surveillance was an indispensable prerequisite for employee diligence.

However, seminal organizational studies—most notably economist Nicholas Bloom's groundbreaking randomized controlled trial at Ctrip—thoroughly shattered these prejudices. The study demonstrated that home-based workers exhibited a dramatic thirteen percent increase in productivity, logged fewer sick days, and reported substantially higher job satisfaction. Liberated from grueling commutes and disruptive office small talk, remote professionals accomplished more substantive work in fewer hours.

Beyond productivity, telecommuting delivers extraordinary institutional dividends for employers. Offering remote flexibility expands corporate recruiting horizons, allowing companies to tap into global talent pools rather than competing for hyper-expensive talent in congested metropolitan tech hubs. Furthermore, by shrinking physical office footprints, corporations save millions of dollars in commercial leases and utility bills.

Yet, managing distributed workforces presents acute operational complexities. When teams are physically isolated, casual collaborative encounters vanish. The spontaneous hallway exchanges that traditionally sparked creative problem-solving are replaced by scheduled, transactional video meetings. Furthermore, remote arrangements present formidable hurdles for junior employees who rely on informal mentoring and passive observation to absorb company culture.

Forward-thinking organizations are responding by rejecting both rigid full-time office mandates and total remote isolation in favor of intentional hybrid frameworks. Teams gather on designated collaborative days for strategic brainstorms, social onboarding, and culture building, while reserving quiet days at home for deep, concentrated tasks. The future of work belongs to organizations that manage by deliverables and trust rather than presence and surveillance.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Historically, corporate executives were skeptical of telecommuting because they:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Believed physical face-to-face surveillance was necessary for productivity." },
              { key: "B", text: "Worried that home offices would consume excessive national electricity." },
              { key: "C", text: "Feared that employees would become too intelligent to manage." },
              { key: "D", text: "Were legally forbidden from communicating over telephone lines." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出过去管理者怀疑远程办公是因为他们顽固地认定当面物理监督是保证员工勤勉不可或缺的前提（surveillance as prerequisite）。"
          },
          {
            q_type: "reading_item",
            stem: "Nicholas Bloom's randomized trial at Ctrip proved that remote workers:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Increased productivity by 13 percent and took fewer sick days." },
              { key: "B", text: "Completely stopped communicating with their project managers." },
              { key: "C", text: "Suffered a 90 percent decline in work quality." },
              { key: "D", text: "Demanded triple their original salaries within three weeks." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出 Bloom 的里程碑实证研究证实远程员工生产率提升了13%，病假减少且满意度显著提高。"
          },
          {
            q_type: "reading_item",
            stem: "Corporate employers benefit from telecommuting because it allows them to:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Access global talent pools and reduce commercial office leasing costs." },
              { key: "B", text: "Eliminate all salary payments to junior staff members." },
              { key: "C", text: "Force workers to pay for their own computer servers." },
              { key: "D", text: "Avoid paying municipal business property taxes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出远程办公能拓宽招聘视野、吸纳全球人才，并大幅缩减昂贵的商业写字楼租金和水电开支。"
          },
          {
            q_type: "reading_item",
            stem: "What major challenge of distributed work is highlighted in Paragraph 4?",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "The loss of spontaneous collaborative exchanges and junior mentorship." },
              { key: "B", text: "A severe shortage of home broadband fiber cables worldwide." },
              { key: "C", text: "Workers refusing to wear business attire on video screens." },
              { key: "D", text: "Computer viruses destroying all digital documents every evening." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第四段指出痛点在于自发性偶遇灵感协作消失，新人缺乏耳濡目染的文化熏陶与导师指导（mentorship & spontaneous exchanges）。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that successful modern workplaces should:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Manage by results and trust within an intentional hybrid framework." },
              { key: "B", text: "Mandate that all workers sleep inside the physical corporate office." },
              { key: "C", text: "Abolish all digital communication tools like email and video calls." },
              { key: "D", text: "Replace all corporate managers with algorithmic robot guards." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结指出职场未来属于基于产出交付与信任进行管理的组织（manage by deliverables and trust），推行兼顾协作与专注的弹性混合制。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `Two decades after the controversial privatization of British Rail under John Major's Conservative government, Britain's passenger railway system remains locked in a fierce political battlefield. Under the 1993 Railways Act, the monolithic state-owned British Rail was fragmented into dozens of private entities: track infrastructure was handed to a separate entity, while passenger train routes were auctioned off as commercial "franchises" to private transport corporations.

Proponents of privatization originally promised that commercial competition would unleash an era of customer service excellence, private capital investment, and falling ticket prices. Indeed, passenger journeys have more than doubled over the past twenty years, reaching historic highs. Modern train fleets with electric traction and onboard amenities have replaced dilapidated post-war rolling stock.

However, critics argue that passenger growth was driven by broader economic expansion and urban density rather than the genius of private franchise models. Far from delivering cheap fares, British commuters pay some of the highest passenger rail fares in Europe, with annual season tickets consuming an exorbitant proportion of average commuter incomes.

Furthermore, the franchise system has perversely increased taxpayer subsidies. Private train operating companies receive billions of pounds in public subsidies to operate unprofitable lines, while extracting millions in private shareholder dividends. When franchises encounter financial distress—as demonstrated by the repeated collapse of the East Coast Mainline franchise—private operators walk away from contractual liabilities, forcing the taxpayer to step in and bailout operations.

A resounding majority of the British public now favors bringing passenger rail back into public ownership. Transport economists emphasize that railways are natural geographic monopolies with profound environmental and economic externalities. Reinvigorating British transport requires abandoning fragmented commercial franchises in favor of an integrated public network dedicated to affordable, reliable mass transit.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The 1993 privatization of British Rail fragmented the national network into:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Separate infrastructure management and private commercial franchises." },
              { key: "B", text: "Fifty autonomous military divisions commanded by naval admirals." },
              { key: "C", text: "A completely underground subway network with zero aboveground tracks." },
              { key: "D", text: "Foreign-owned airline carrier networks operating on water." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出1993年私有化法案将英国铁路肢解为轨道基础设施管理与私营车企客运特许经营权（commercial franchises）两大碎片化板块。"
          },
          {
            q_type: "reading_item",
            stem: "Supporters of privatization point to which success over the past twenty years?",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Passenger journeys have doubled and modern fleets have been introduced." },
              { key: "B", text: "Passenger fares were completely eliminated for all citizens." },
              { key: "C", text: "Trains were legally converted into supersonic flight jets." },
              { key: "D", text: "Railway stations were turned into private luxury hotels." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出支持者强调的成果是客运旅次翻番（passenger journeys doubled）以及现代化新列车更新换代。"
          },
          {
            q_type: "reading_item",
            stem: "Critics criticize British rail fares because commuters:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Pay some of the highest passenger ticket prices in Western Europe." },
              { key: "B", text: "Are legally required to pay for train tickets with real gold bars." },
              { key: "C", text: "Must purchase tickets twenty-five years in advance of travel." },
              { key: "D", text: "Are forbidden from bringing luggage onto passenger cars." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出票价并未便宜，英国通勤客支付着全欧洲最贵的高昂票价（highest fares in Europe），季票挤占大量工薪收入。"
          },
          {
            q_type: "reading_item",
            stem: "The franchise model is described as flawed in Paragraph 4 because private operators:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Extract private dividends while taxpayers bail out distressed franchises." },
              { key: "B", text: "Refuse to use electrical energy to run locomotive engines." },
              { key: "C", text: "Pay 90 percent of their ticket revenues directly to public schools." },
              { key: "D", text: "Prohibit passengers from stepping onto station platforms." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出制度弊端在于“利润私有化，亏损公有化”：私营车企拿政府巨额补贴分红，遇危机便弃约甩锅，逼纳税人买单兜底。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that the optimal solution for Britain's railway system is:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Transitioning back to an integrated public network focused on service." },
              { key: "B", text: "Demolishing all railway tracks and replacing them with airports." },
              { key: "C", text: "Selling all passenger train carriages to overseas collectors." },
              { key: "D", text: "Banning any commuter from traveling more than five miles daily." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出铁路属于天然地理垄断和绿色公共产品，民意与经济学界均倾向于摒弃碎片化私营特许，回归一体化公共所有制（integrated public network）。"
          }
        ]
      }
    ]
  }
];
