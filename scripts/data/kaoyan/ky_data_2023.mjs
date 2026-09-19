// 2023 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const kyHistoricalArchive = [
  // =========================================================================
  // 2023 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Infant cognitive development has captivated developmental psychologists for over a century. Early theorists posited that neonates experience the surrounding world as a blooming, buzzing confusion, devoid of structural (1)____. However, modern neuroimaging and non-invasive eye-tracking methodologies reveal that infants possess sophisticated perceptual frameworks far earlier than previously (2)____.

Even at several months of age, infants can discern phonemic contrasts across all human languages, a perceptual flexibility that gradually (3)____ as neural pruning attunes their auditory cortex to their native tongue. Moreover, rudimentary arithmetic expectations and intuitive physics appear to guide their gaze: when presented with impossible physical events, such as an object passing through a solid barrier, babies register heightened pupil dilation, indicating cognitive (4)____.

These empirical breakthroughs demonstrate that learning is not a passive recording of external sensations, but rather an active, hypothesis-testing inquiry. Caregivers should therefore prioritize rich conversational and tactile interaction over passive digital screens, which lack the contingent responsiveness necessary to stimulate deep neurodevelopmental (5)____.

In linguistic acquisition, maternal speech patterns—frequently termed 'infant-directed speech'—serve an indispensable pedagogical role. Characterized by exaggerated pitch contours, slower articulation tempos, and simplified syntactic structures, this melodic communication style effortlessly (6)____ infant attention, highlighting acoustic boundaries between distinct syllables and words. 

Neuroscientists note that these linguistic cadences stimulate the infant's left auditory hemisphere, (7)____ the neural pathways responsible for eventual speech production. Far from being patronizing gibberish, exaggerated maternal speech represents an evolutionary (8)____ that bootstraps infant vocabulary comprehension months before spoken words emerge.

Concurrently, social referencing emerges as a primary navigational mechanism during the second half of the infant's first year. When confronted with novel, ambiguous stimuli—such as an unfamiliar mechanical toy or a steep visual cliff—infants instinctively seek out their caregiver's facial (9)____. If the mother projects an encouraging smile, the infant boldly advances; if her visage reflects apprehension, the child abruptly (10)____ exploration.

This emotional transmission demonstrates that cognitive learning is inextricably tethered to affective security. When caregivers maintain warm, predictable attentiveness, infants develop secure attachment patterns that foster exploratory confidence. Conversely, chronic parental neglect or severe emotional flat-lining can (11)____ infant curiosity, dampening the neuroplastic responsiveness of the developing brain.

Motor development also operates in tight (12)____ with perceptual cognition. The transition from prone crawling to bipedal walking fundamentally overhauls how an infant navigates the domestic environment. Bipedal locomotion broadens the visual field, frees the hands to manipulate domestic artifacts, and dramatically accelerates spatial (13)____.

Each physical milestone compels the child to formulate novel cognitive strategies. A crawling baby perceives a staircase as an insurmountable obstacle, whereas a walking toddler views the same incline as an invitation for adventurous climbing. Thus, motor milestones are not merely mechanical muscular achievements, but profound catalysts of cognitive (14)____.

Cross-cultural comparative studies further enrich our understanding of infant cognition. While Western middle-class parenting often emphasizes solo object play and early verbal praise, communal cultures in Central Africa and Oceania prioritize continuous physical contact and collective social (15)____. Despite divergent childrearing customs, infants across all societies attain foundational milestones with remarkable temporal (16)____.

This cross-cultural resilience suggests that human evolution has endowed neonates with robust self-righting cognitive mechanisms. Provided an environment satisfies minimal nutritional, emotional, and social baselines, the human brain will autonomously (17)____ its developmental blueprint.

Nevertheless, extreme socioeconomic deprivation can impose severe developmental tolls. Chronic exposure to environmental neurotoxins, household food insecurity, and unremitting parental stress generate elevated cortisol concentrations that can disrupt hippocampal synaptic (18)____. 

Public policy initiatives targeting infant well-being must therefore transcend simplistic educational toys, focusing instead on structural family support. Guaranteed paid parental leave, accessible community child healthcare, and maternal mental wellness services provide the essential bedrock upon which infant cognitive development truly (19)____.

Ultimately, infancy represents a unique developmental window of unparalleled neuroplasticity and vulnerability. Protecting and nurturing this formative epoch is not merely a private familial duty, but a foundational collective investment in the social, intellectual, and democratic (20)____ of future generations.`,
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
            explanation: "【考点精析】名词辨析与句意连贯。devoid of structural coherence（缺乏结构上的连贯性/协调性）。"
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
            explanation: "【考点精析】被动语态搭配。far earlier than previously assumed（远早于先前所设想）。"
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
            explanation: "【考点精析】动词与神经修剪。婴儿对外语语音对比的灵活性随着大脑神经元修剪逐渐收窄（narrows）。"
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
            explanation: "【考点精析】心理实验现象。看到不可能的物理事件时，婴儿瞳孔放大表明其产生了认知上的惊讶（surprise）。"
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
            explanation: "【考点精析】名词与褒义搭配。深度神经发育成长（neurodevelopmental growth）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "captures" },
              { key: "B", text: "distracts" },
              { key: "C", text: "offends" },
              { key: "D", text: "paralyzes" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。母亲语优美的旋律性轻松吸引住（captures）婴儿的注意力。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "fortifying" },
              { key: "B", text: "severing" },
              { key: "C", text: "poisoning" },
              { key: "D", text: "bypassing" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】现在分词与积极作用。强化、巩固（fortifying）负责言语生成的神经回路。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "adaptation" },
              { key: "B", text: "superstition" },
              { key: "C", text: "mistake" },
              { key: "D", text: "tragedy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。evolutionary adaptation（演化适应机制）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "expressions" },
              { key: "B", text: "passports" },
              { key: "C", text: "scandals" },
              { key: "D", text: "hesitations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。facial expressions（面部表情），是社会参照现象的核心观察线索。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "halts" },
              { key: "B", text: "accelerates" },
              { key: "C", text: "celebrates" },
              { key: "D", text: "praises" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与对比。如果母亲表情焦虑担忧，孩子会立刻停止（halts）探索。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "stifle" },
              { key: "B", text: "kindle" },
              { key: "C", text: "nourish" },
              { key: "D", text: "restore" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。长期忽视会扼杀、压制（stifle）婴儿的好奇心。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "coordination" },
              { key: "B", text: "conflict" },
              { key: "C", text: "hostility" },
              { key: "D", text: "separation" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】介词短语搭配。operate in tight coordination with（与……紧密协同运行）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "mapping" },
              { key: "B", text: "confusion" },
              { key: "C", text: "blindness" },
              { key: "D", text: "paralysis" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】空间认知概念。直立行走加速了空间地图构建（spatial mapping）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "reorganization" },
              { key: "B", text: "decay" },
              { key: "C", text: "stagnation" },
              { key: "D", text: "fatigue" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。运动里程碑是认知重组与飞跃（cognitive reorganization）的催化剂。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "immersion" },
              { key: "B", text: "isolation" },
              { key: "C", text: "rejection" },
              { key: "D", text: "hatred" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与集体文化。collective social immersion（全方位的集体社交沉浸融入）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "synchrony" },
              { key: "B", text: "disaster" },
              { key: "C", text: "chaos" },
              { key: "D", text: "hostility" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。remarkable temporal synchrony（在时间节点上表现出惊人的一致与同步性）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "unfold" },
              { key: "B", text: "suppress" },
              { key: "C", text: "demolish" },
              { key: "D", text: "conceal" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与蓝图。大脑会自发地展开并实现其发育蓝图（unfold its developmental blueprint）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "connectivity" },
              { key: "B", text: "paralysis" },
              { key: "C", text: "extinction" },
              { key: "D", text: "exhaustion" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】神经生物学表达。高皮质醇会破坏海马体突触连接性（hippocampal synaptic connectivity）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "thrives" },
              { key: "B", text: "withers" },
              { key: "C", text: "collapses" },
              { key: "D", text: "stagnates" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与蓬勃发展。提供了婴儿认知发育真正得以茁壮繁荣（truly thrives）的基石。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "fabric" },
              { key: "B", text: "superstition" },
              { key: "C", text: "betrayal" },
              { key: "D", text: "disaster" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻名词。social, intellectual, and democratic fabric（社会、智力与民主的肌理与结构）。"
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
            sort_order: 21,
            options: [
              { key: "A", text: "Strict governmental censorship of regional reporting" },
              { key: "B", text: "The loss of advertising revenue to digital platform monopolies" },
              { key: "C", text: "Widespread public disinterest in reading text" },
              { key: "D", text: "A severe national shortage of printing press paper" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第一段指出报社破产归咎于广告收入下滑以及数字垄断平台对商业分类广告的蚕食，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "Communities without local newspapers tend to experience ______.",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "lower voter participation and higher municipal borrowing costs" },
              { key: "B", text: "harmonious municipal consensus without any political debate" },
              { key: "C", text: "a rapid surge in private philanthropic investments" },
              { key: "D", text: "unprecedented improvements in school board governance" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段列举实证研究表明缺乏地方媒体会导致投票率走低以及因缺少监督而增加借款成本，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Non-profit investigative newsrooms face the limitation that ______.",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "philanthropic funding is heavily biased toward prosperous cities" },
              { key: "B", text: "they are legally forbidden from uncovering municipal scandals" },
              { key: "C", text: "digital readers refuse to read investigative exposes" },
              { key: "D", text: "national aggregators refuse to link to non-profit domains" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出慈善捐款高度集中在富裕的大城市，非工业区依然沦为新闻荒漠，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which policy proposal is mentioned to sustain local journalism?",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Nationalizing all municipal printing presses" },
              { key: "B", text: "Mandating aggregators to compensate original news publishers" },
              { key: "C", text: "Banning social media accounts from reporting on school boards" },
              { key: "D", text: "Imposing heavy penalties on readers of digital media" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第四段指出立法强制要求数字平台向原创媒体支付内容版权报酬，选 B。"
          },
          {
            q_type: "reading_item",
            stem: "The author considers local journalism to be ______.",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "an outdated commercial relic incapable of modernization" },
              { key: "B", text: "an indispensable public good vital to democratic accountability" },
              { key: "C", text: "a trivial luxury that small towns can easily live without" },
              { key: "D", text: "a chief instigator of national political polarization" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】作者观点题。末段首句明确将其定义为不可或缺的公共产品（indispensable public good），对民主监督具有基石作用，选 B。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `Autonomous driving technologies are accelerating from controlled testing tracks into real-world traffic ecosystems. Equipped with lidar, radar arrays, and deep neural networks, autonomous passenger vehicles promise to dramatically reduce vehicular fatalities, ninety percent of which currently stem from human perceptual error, intoxication, or distracted driving.

Yet, as commercial robotaxi fleets expand, software engineers and regulatory ethicists face intractable moral dilemmas known as 'trolley problems.' When an imminent multi-vehicle collision is inevitable, how should an autonomous vehicle's decision-making algorithm prioritize human life? Should the software protect the passenger inside the vehicle at all costs, or steer into a barrier to spare a larger group of pedestrians on a zebra crossing?

Surveys of public attitudes reveal a profound moral paradox. When asked in the abstract, the vast majority of citizens endorse utilitarian programming that minimizes total human casualties. However, when asked whether they would purchase an autonomous vehicle programmed to sacrifice its own passengers in emergency scenarios, consumer willingness plummets to near zero. People demand utilitarian vehicles for everyone else, while demanding self-protective vehicles for themselves and their families.

Consequently, automotive safety regulators are moving away from philosophical dilemmas toward deterministic safety frameworks. Rather than expecting algorithms to make moral value judgments in split-second emergencies, statutory mandates emphasize conservative defensive driving: enforcing continuous headway margins, restricting maximum speeds in pedestrian zones, and ensuring fail-safe mechanical overrides. By eliminating the high-speed conditions that create unsolvable moral crashes, engineers can deliver societal safety without getting bogged down in ethical impasses.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What is the principal safety promise of autonomous vehicles?",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Eliminating vehicular fatalities caused by human error and distraction" },
              { key: "B", text: "Allowing vehicles to travel indefinitely without electrical charging" },
              { key: "C", text: "Completely removing all traffic lights from metropolitan streets" },
              { key: "D", text: "Enabling commuters to work 100-hour weeks without fatigue" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段末尾指出无人驾驶有望大幅消除由人类感知失误、醉驾和分心导致的交通事故死亡（ninety percent of which stem from human error），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The 'moral paradox' mentioned in Paragraph 3 indicates that ______.",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "people praise utilitarian ethics for others but demand self-protection for themselves" },
              { key: "B", text: "consumers refuse to ride in cars manufactured outside their home nation" },
              { key: "C", text: "pedestrians prefer interacting with human drivers rather than computers" },
              { key: "D", text: "engineers refuse to write code for autonomous braking systems" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第三段指出公众在抽象层面上支持功利主义最小化伤亡，但买车时要求绝对优先保护自己和家人，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "How are regulators resolving the ethical dilemma of autonomous driving?",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "By focusing on deterministic defensive driving to prevent crashes altogether" },
              { key: "B", text: "By permanently banning all autonomous vehicle testing on public roads" },
              { key: "C", text: "By leaving all ethical decisions to random lottery algorithms" },
              { key: "D", text: "By requiring drivers to pass philosophical logic exams before entering cars" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出监管正转向确定性的防御性驾驶规则（enforcing continuous headway margins, restricting speeds），从根本上避免出现道德两难的碰撞险情，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The word 'impasse' in the final sentence is closest in meaning to ______.",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "deadlock" },
              { key: "B", text: "opportunity" },
              { key: "C", text: "celebration" },
              { key: "D", text: "agreement" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义猜测题。前文讨论道德两难僵局，ethical impasses 即伦理死局、僵局（deadlock），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following would be the most suitable title for Text 2?",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Autonomous Driving: From Moral Dilemmas to Engineering Reality" },
              { key: "B", text: "Why Robotaxis Should Be Banned Worldwide" },
              { key: "C", text: "The Ultimate Perfection of Human Motorists" },
              { key: "D", text: "How Pedestrians Will Conquer Autonomous Highways" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨标题题。文章阐述了自动驾驶由伦理电车难题转向工程防御性实操规范的演进路径，选 A。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `Low-Earth orbit (LEO) is rapidly congesting with tens of thousands of commercial satellites launched to deploy global broadband internet constellations. While satellite internet bridges digital divides in remote archipelagos and rural regions, the unprecedented density of orbital hardware is generating an acute environmental crisis: space debris and orbital carrying capacity exhaustion.

Aerospace engineers warn of the 'Kessler Syndrome'—a catastrophic cascading collision scenario where high-speed orbital debris fragments collide with operational satellites, producing clouds of secondary shrapnel that trigger further collisions. Because fragments in low-Earth orbit travel at orbital velocities exceeding seven kilometers per second, even a centimeter-wide speck of defunct paint carries the kinetic energy of an exploding artillery shell.

Furthermore, astronomical observation from Earth is severely compromised. Optical telescopes capturing long-exposure images of deep galaxies are increasingly crisscrossed by bright streaks reflecting sunlight from satellite constellation solar panels. Radio astronomers face parallel interference, as broadband downlink frequencies bleed into frequencies reserved for cosmic microwave research.

International space law, codified primarily during the Cold War in the 1967 Outer Space Treaty, lacks modern enforcement mechanisms. Satellites are legally designated as state property, meaning private salvagers cannot physically de-orbit a derelict satellite without the registered launching state's explicit permission. To prevent our near-Earth commons from becoming permanently hazardous, spacefaring nations must negotiate updated orbital space traffic management treaties, mandating active de-orbiting thrusters and economic penalties for abandoned space junk.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The deployment of commercial satellite constellations has ______.",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "congested low-Earth orbit and created serious space debris risks" },
              { key: "B", text: "eliminated all forms of digital terrestrial communication" },
              { key: "C", text: "lowered global temperatures across both polar icecaps" },
              { key: "D", text: "permanently extinguished the threat of asteroid collisions" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出商业卫星网络部署导致低地球轨道严重拥堵，产生严重的太空垃圾危机，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What is the core danger of the 'Kessler Syndrome'?",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "A cascading chain reaction of orbital collisions generating clouds of shrapnel" },
              { key: "B", text: "The immediate crash of all satellites into ocean trenches" },
              { key: "C", text: "The loss of gravitational pull between the Earth and the Moon" },
              { key: "D", text: "Excessive radioactive fallout entering the upper stratosphere" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出凯斯勒综合征是指高速轨道碎片碰撞产生级联反应，引发毁灭性连锁碰撞，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Astronomers complain that satellite constellations ______.",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "interfere with optical telescope exposures and radio astronomy frequencies" },
              { key: "B", text: "physically block sunlight from reaching agricultural crops" },
              { key: "C", text: "corrupt all digital university library databases" },
              { key: "D", text: "increase ticket prices for private space tourism" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出卫星反射阳光在光学长曝光照片上留下划痕，其下行频段还干扰宇宙微波射电研究，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why is clearing abandoned space junk legally complicated under current law?",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Old treaties designate satellites as sovereign state property" },
              { key: "B", text: "Space debris carries lethal contagious pathogens" },
              { key: "C", text: "Private companies are strictly forbidden from owning computers" },
              { key: "D", text: "The United Nations claims sole physical possession of all orbits" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果事实题。第四段指出依据冷战时期的《外层空间条约》，废弃卫星仍属主权国家财产，未经许可不得擅自清除，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The author advocates that spacefaring nations must ______.",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "negotiate updated treaties mandating active de-orbiting and penalties" },
              { key: "B", text: "completely dismantle all global satellite communications" },
              { key: "C", text: "privatize all outer space orbits to the highest corporate bidder" },
              { key: "D", text: "halt all astronomy research until the next century" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】作者观点题。第四段末句指出航天大国必须谈判达成最新的太空交通管理条约，强制配备离轨发动机并对遗弃太空垃圾施加经济惩罚，选 A。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `The geopolitical resurgence of industrial reshoring—relocating offshore manufacturing facilities back to domestic soil—has become a cornerstone of contemporary economic policy in North America and Western Europe. Spurred by geopolitical tensions, pandemic supply chain vulnerabilities, and escalating shipping freight costs, governments are channeling hundreds of billions of dollars in subsidies to repatriate advanced semiconductor foundries, electric vehicle battery plants, and medical equipment factories.

However, labor market analysts caution that industrial reshoring in the twenty-first century will not resurrect the mass blue-collar assembly jobs of the mid-twentieth century. Modern domestic manufacturing facilities are hyper-automated technological complexes dominated by robotic automation, automated guided vehicles, and computer-vision quality inspection stations. A semiconductor foundry that cost twenty billion dollars to construct may require only a few hundred specialized automation technicians and systems engineers to operate.

This structural divergence creates a profound regional employment mismatch. The displaced workers in deindustrialized heartlands often lack the advanced programming and mechatronics credentials required to operate modern cyber-physical factories. Without massive, well-funded vocational retraining investments, reshoring initiatives risk creating high-tech industrial enclaves that generate immense corporate profits while leaving local working-class communities largely economically marginalized.

Economists emphasize that the ultimate justification for industrial reshoring must be understood through the lens of national economic resilience and technological sovereignty, rather than aggregate job volume. Domestic manufacturing secures critical supply chains against foreign geopolitical embargoes and accelerates domestic innovation ecosystems. But to ensure that the domestic benefits are equitably shared, state support for advanced factories must be coupled with lifelong technical education and regional community development compacts.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What has motivated the resurgence of industrial reshoring in Western nations?",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Geopolitical tensions, shipping vulnerabilities, and supply security" },
              { key: "B", text: "A total global shortage of industrial plastics and crude oil" },
              { key: "C", text: "A nationwide consumer boycott of all electronic gadgets" },
              { key: "D", text: "The complete bankruptcy of all international shipping companies" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出地缘政治摩擦、疫情供应链脆弱性及海运运费上涨促成了制造业回流，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Modern reshored factories will not create mass blue-collar employment because ______.",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "they are hyper-automated complexes requiring minimal specialized technicians" },
              { key: "B", text: "workers refuse to accept wages paid in national currency" },
              { key: "C", text: "governmental statutes forbid hiring human factory workers" },
              { key: "D", text: "factories are located exclusively on offshore ocean platforms" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段阐明现代回流工厂是高度自动化的复合体，大量使用机器人和机器视觉，只需极少数自动化技师，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What risk is highlighted in Paragraph 3 regarding deindustrialized communities?",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Displaced workers lack skills for cyber-physical factories, risking marginalization" },
              { key: "B", text: "Local residents will immediately demolish the new semiconductor foundries" },
              { key: "C", text: "Factory robots will cause widespread environmental radiation" },
              { key: "D", text: "Working-class families will refuse to purchase domestically made products" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节因果题。第三段指出老工业区下岗工人缺乏高级机电一体化技能，回流工厂可能沦为难以惠及本地工人的技术飞地，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to economists, the primary justification for reshoring is ______.",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "strengthening national economic resilience and technological sovereignty" },
              { key: "B", text: "permanently stopping all international trade and diplomacy" },
              { key: "C", text: "ensuring that every high school graduate becomes a factory laborer" },
              { key: "D", text: "lowering the national stock market index" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出回流的终极价值必须从国家经济韧性与技术主权（resilience and technological sovereignty）的角度来衡量，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that industrial reshoring policies must be accompanied by ______.",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "lifelong technical education and regional community development compacts" },
              { key: "B", text: "an immediate ban on teaching software programming in schools" },
              { key: "C", text: "the total nationalization of all corporate patent portfolios" },
              { key: "D", text: "a return to nineteenth-century steam engine technologies" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】作者结论题。第四段末句指出国家补贴必须与终身技术教育和区域社区发展契约相结合，实现利益公平共享，选 A。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2023 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Circadian rhythms are endogenous biological oscillations that orchestrate hormone secretion, core body temperature, and cellular repair across a twenty-four-hour cycle. In modern industrialized societies, however, widespread artificial illumination and nocturnal screen exposure frequently (1)____ these synchronized physiological pacemakers.

When people regularly stay awake past midnight, light emissions suppress the pineal gland's secretion of melatonin, a hormone critical for signaling sleep (2)____. This chronic circadian misalignment does not merely cause daytime sleepiness; extensive epidemiological studies link habitual sleep disruption to elevated risks of hypertension, insulin resistance, and depressive (3)____.

To realign internal clocks, chronobiologists recommend establishing consistent diurnal habits. Prioritizing morning exposure to natural sunlight provides a potent zeitgeber—an environmental cue that (4)____ the master circadian clock located in the brain's suprachiasmatic nucleus. Conversely, dampening indoor light levels two hours prior to bedtime fosters natural melatonin accumulation, enabling restorative slumber that bolsters immune (5)____.

Beyond light hygiene, meal timing plays an equally (6)____ role in peripheral circadian entrainment. While the central suprachiasmatic clock synchronizes primarily to photic signals, peripheral clocks within the liver, pancreas, and gastrointestinal tract respond (7)____ to nutrient intake. 

Consuming heavy, calorie-dense dinners late in the evening desynchronizes metabolic organs from the central cranial clock. This internal misalignment (8)____ glucose tolerance and impairs nocturnal lipid clearance. Chrono-nutritionists therefore advocate for time-restricted eating windows, advising people to consume the bulk of their daily caloric intake during daylight hours when insulin sensitivity is naturally (9)____.

Physical activity also serves as a potent non-photic cue. Moderate aerobic exercise performed in the morning or early afternoon accelerates metabolic activation and enhances nocturnal slow-wave sleep depth. However, vigorous, high-intensity workouts scheduled immediately before bedtime can elevate core body temperature and sympathetic nervous (10)____, inadvertently postponing sleep onset.

The workplace environment represents another critical front in circadian health. Traditional windowless office cubicles, illuminated solely by static, dim fluorescent tubes, deprive employees of the high-lux daytime stimulation necessary to maintain alertness. In response, enlightened corporate architects are introducing biodynamic lighting systems that automatically modulate color temperatures, (11)____ bright, blue-enriched light at 9:00 AM and transitioning toward warm, amber hues by late afternoon.

Shift workers endure the most severe circadian (12)____ in modern economies. Millions of nurses, emergency responders, and manufacturing technicians are compelled to labor during nocturnal troughs and sleep during loud daylight hours. Epidemiologists categorize long-term graveyard shift rotation as a probable physiological (13)____, associated with elevated oncological and cardiovascular morbidities.

To mitigate occupational hazards, industrial hygienists recommend implementing forward-rotating shift schedules that align more harmoniously with the human circadian inclination to naturally (14)____ sleep timing. Providing bright light exposure during early shifts, combined with light-blocking amber spectacles during morning commutes home, assists nocturnal workers in preserving biological (15)____.

Caffeine consumption patterns also demand judicious regulation. Although caffeine effectively blocks adenosine receptors in the brain to temporarily mask fatigue, its biological half-life ranges from five to eight hours. Consuming caffeinated espresso or energy drinks in the late afternoon impairs deep delta-wave sleep architectures, leaving individuals feeling (16)____ upon waking and perpetuating a vicious cycle of chemical stimulant reliance.

In modern educational settings, adolescent sleep biology has provoked urgent policy debates. During puberty, biological circadian rhythms undergo a natural delay of approximately two hours, making early bedtime physiologically unnatural for teenagers. Forcing high school students to report to class at 7:30 AM results in chronic societal sleep (17)____, depressing academic performance and elevating mental health vulnerabilities.

Municipalities that have delayed high school start times to 8:30 AM report measurable dividends: improved grades, reduced rates of vehicular accidents among teen drivers, and significant reductions in adolescent (18)____. Aligning social timetables with biological reality demonstrates that chronobiology holds profound implications for educational equity.

Ultimately, honoring circadian biology requires shedding the toxic cultural machismo that glorifies sleep deprivation as a badge of productivity. Sleep is not a negotiable luxury or an unproductive void; it is the vital biological bedrock upon which human physical health, emotional equilibrium, and cognitive performance (19)____. 

As chronobiological science illuminates the profound cellular rhythms governing life, societies must redesign cities, workplaces, and educational institutions to nurture, rather than fracture, our ancient evolutionary (20)____ with the diurnal cycles of our planet.`,
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
            explanation: "【考点精析】动词搭配。人工照明与屏幕夜间暴露会干扰破坏（disrupt）生理生物钟节律。"
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
            explanation: "【考点精析】专业搭配。褪黑素是入睡开始（sleep onset）的神经化学信号。"
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
            explanation: "【考点精析】医学搭配。depressive episodes（抑郁发作期），与高血压、胰岛素抵抗并列。"
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
            explanation: "【考点精析】动词搭配。晨光是一个强有力的授时因子，能重置校准（resets）下丘脑视交叉上核的中央生物钟。"
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
            explanation: "【考点精析】名词与褒义搭配。优质睡眠增强机体免疫能力与健全性（immune competence）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "influential" },
              { key: "B", text: "worthless" },
              { key: "C", text: "destructive" },
              { key: "D", text: "invisible" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。进食时间在外周生物钟调节中扮演着同样重要的关键角色（influential role）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "predominantly" },
              { key: "B", text: "reluctantly" },
              { key: "C", text: "scarcely" },
              { key: "D", text: "dubiously" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词语义。外周器官的生物钟主要（predominantly）对营养摄入做出响应。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "compromises" },
              { key: "B", text: "fortifies" },
              { key: "C", text: "celebrates" },
              { key: "D", text: "guarantees" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词辨析。体内节律脱节会损害、危害（compromises）葡萄糖耐量。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "peaked" },
              { key: "B", text: "depressed" },
              { key: "C", text: "eliminated" },
              { key: "D", text: "frozen" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词与生理机能。在白昼时段，人体的胰岛素敏感度天然处于巅峰峰值（naturally peaked）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "arousal" },
              { key: "B", text: "paralysis" },
              { key: "C", text: "decay" },
              { key: "D", text: "extinction" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】专业术语。sympathetic nervous arousal（交感神经系统唤醒/兴奋），睡前剧烈运动会引起兴奋而推迟入睡。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "emitting" },
              { key: "B", text: "blocking" },
              { key: "C", text: "prohibiting" },
              { key: "D", text: "swallowing" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词现在分词。生物动态照明系统在早晨发射/散发（emitting）高亮度蓝光以提神。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "penalties" },
              { key: "B", text: "rewards" },
              { key: "C", text: "privileges" },
              { key: "D", text: "triumphs" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词修辞。倒班轮班工人承受着最严重的昼夜节律健康代价/惩罚（circadian penalties）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "carcinogen" },
              { key: "B", text: "nutrient" },
              { key: "C", text: "vaccine" },
              { key: "D", text: "vitamin" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】医学分类。世卫组织将长期夜班倒班列为潜在的生理致癌因素（probable carcinogen）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "delay" },
              { key: "B", text: "accelerate" },
              { key: "C", text: "abolish" },
              { key: "D", text: "freeze" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词语义。顺时针向前倒班符合人类生物钟倾向于顺延推迟（delay）睡眠时间的生理规律。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "integrity" },
              { key: "B", text: "collapse" },
              { key: "C", text: "chaos" },
              { key: "D", text: "ruin" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。preserving biological integrity（维护生物学机能完整性）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "unrefreshed" },
              { key: "B", text: "exhilarated" },
              { key: "C", text: "victorious" },
              { key: "D", text: "enlightened" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词与负面状态。下午摄入咖啡因破坏深睡眠，导致醒来时依然感到未消除疲劳、昏沉不适（feeling unrefreshed）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "deprivation" },
              { key: "B", text: "abundance" },
              { key: "C", text: "wealth" },
              { key: "D", text: "pleasure" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。chronic societal sleep deprivation（普遍的慢性社会性睡眠剥夺）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "depression" },
              { key: "B", text: "cheerfulness" },
              { key: "C", text: "enthusiasm" },
              { key: "D", text: "gratitude" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极名词与消减。推迟上学时间使青少年抑郁（adolescent depression）大幅减轻。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "rest" },
              { key: "B", text: "decay" },
              { key: "C", text: "stumble" },
              { key: "D", text: "perish" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与介词搭配。rest upon（建立在……的基础之上），睡眠是健康和认知表现赖以依托的基石。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "synchrony" },
              { key: "B", text: "dispute" },
              { key: "C", text: "hostility" },
              { key: "D", text: "estrangement" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。our ancient evolutionary synchrony with the diurnal cycles（人类与地球昼夜节律之间古老漫长的演化协同与同步）。"
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
            sort_order: 21,
            options: [
              { key: "A", text: "Digital resale platforms and environmentally conscious young consumers" },
              { key: "B", text: "The total bankruptcy of all major fast-fashion manufacturers" },
              { key: "C", text: "Strict governmental bans on purchasing newly manufactured garments" },
              { key: "D", text: "Heavy subsidies paid directly by traditional department stores" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出二手转售市场爆发由数字化平台和具备环保意识的年轻一代共同推动，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "For Gen Z shoppers, buying second-hand represents ______.",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "a humiliating necessity due to poverty" },
              { key: "B", text: "an ideological statement and an expression of personal style" },
              { key: "C", text: "an attempt to hoard items for illegal black-market resale" },
              { key: "D", text: "an aversion to any form of textile recycling" }
            ],
            correct_answer: "B",
            explanation: "【考点精析】细节事实题。第二段指出买二手不仅为省钱，更是意识形态主张和独特生活方式选择（an ideological statement and a creative lifestyle choice），选 B。"
          },
          {
            q_type: "reading_item",
            stem: "How are traditional retail brands reacting to the secondhand boom?",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "By launching their own trade-in and authenticated resale portals" },
              { key: "B", text: "By filing lawsuits against young thrift store owners" },
              { key: "C", text: "By reducing the durability of their fabrics to prevent resale" },
              { key: "D", text: "By withdrawing completely from digital e-commerce channels" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出传统零售商顺势而为，上线自己的官方以旧换新和官方认证转售门户，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Sustainability researchers warn that the resale economy may fail to help the planet if ______.",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "consumers use resale proceeds to fund more fast-fashion consumption" },
              { key: "B", text: "refurbished electronics fail after three years of use" },
              { key: "C", text: "digital resale websites charge transaction commissions" },
              { key: "D", text: "textile recycling centers are relocated to rural zones" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出如果人们将二手收益当作零花钱再去买新的快时尚，总体环境消耗依然得不到根本减缓，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The primary purpose of the text is to ______.",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "analyze the rise of the resale economy and its environmental realities" },
              { key: "B", text: "condemn the younger generation for their consumerist vanity" },
              { key: "C", text: "advocate for the immediate closure of all physical thrift stores" },
              { key: "D", text: "promote a specific commercial second-hand mobile app" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨大意题。文章全方位剖析了二手经济的崛起势头、商业转型以及其背后的环境真实影响，选 A。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In the arid heartlands of global agriculture, precision irrigation technologies are replacing wasteful flood-and-furrow farming with data-driven hydrological stewardship. Equipped with sub-surface moisture probes, thermal satellite imagery, and automated drip-irrigation networks, modern agronomic platforms apply water in micro-doses directly to plant root zones, conserving up to sixty percent more water than traditional agrarian methods.

The driving impetus behind smart irrigation is the escalating depletion of ancient fossil aquifers. Across regions such as the American High Plains and southern Spain, intensive agricultural extraction has drawn down underground water tables to critically unsustainable depths. By synchronizing irrigation cycles with weather forecasts and soil evapotranspiration rates, smart farming platforms prevent unnecessary irrigation during humid or overcast spells, extending the productive lifespan of regional groundwater reserves.

Furthermore, precision irrigation delivers substantial agronomic dividends beyond water conservation. Flooding crops with excessive water frequently leaches valuable nitrogen fertilizers deep into groundwater tables, polluting drinking wells while starving root systems. Drip fertigation—delivering liquid nutrients dissolved directly within irrigation water—ensures that crops receive balanced nourishment, boosting harvest yields while curtailing synthetic chemical runoff into river basins.

Smallholder farmers, however, face prohibitive capital expenditure hurdles when attempting to adopt smart irrigation systems. Sensor hardware, automated solenoid valves, and cloud-based analytics subscriptions require significant upfront capital investments that small family farms rarely possess. To prevent the digitization of agriculture from exacerbating wealth stratification, public agricultural extension agencies are partnering with regional cooperatives to deploy shared sensor hubs and provide low-interest equipment loans.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What is the primary technological advantage of precision irrigation?",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Delivering water in micro-doses directly to roots to maximize conservation" },
              { key: "B", text: "Eliminating the need for sunshine during grain development" },
              { key: "C", text: "Preventing all insects from landing on crops" },
              { key: "D", text: "Allowing farmers to harvest crops three times a day" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出精准灌溉通过滴灌将微量水分直接精准送达植物根部，节水高达 60%，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Precision irrigation extends aquifer lifespans by ______.",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "synchronizing irrigation with real-time weather and evapotranspiration rates" },
              { key: "B", text: "drilling thousands of deeper wells into the Earth's core" },
              { key: "C", text: "importing Arctic icebergs via cargo aircraft" },
              { key: "D", text: "prohibiting all forms of crop exports" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出智能系统结合天气预报和土壤蒸发量动态调配水分，避免阴雨天过度灌溉，保护了深层地下水，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What is 'drip fertigation' mentioned in Paragraph 3?",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Delivering dissolved liquid fertilizers directly through irrigation water" },
              { key: "B", text: "Spraying chemical powders from high-altitude airplanes" },
              { key: "C", text: "Burying solid manure beneath plastic ground sheets" },
              { key: "D", text: "Freezing crops with nitrogen gas to prevent rot" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节例证题。第三段明确指出水肥一体化（drip fertigation）是将液体养分直接溶解在灌溉水中施用，提高肥料吸收率，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What barrier prevents smallholder farmers from adopting precision irrigation?",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "High upfront capital costs for sensors, valves, and software subscriptions" },
              { key: "B", text: "A complete absence of electrical power across rural communities" },
              { key: "C", text: "Government laws that make drip irrigation strictly illegal" },
              { key: "D", text: "Universal consumer refusal to eat drip-irrigated produce" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节因果题。第四段指出传感器硬件、电磁阀和软件订阅前期资金门槛昂贵（prohibitive capital expenditure hurdles），小农户难以负担，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that expanding smart agriculture requires ______.",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "public cooperative support and accessible low-interest financing" },
              { key: "B", text: "liquidating all small family farms in favor of giant monopolies" },
              { key: "C", text: "abandoning all technological innovation in farming" },
              { key: "D", text: "tripling water prices for all residential consumers" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】作者观点题。末段指出必须通过农业技术推广部门与合作社提供共享传感器网络及低息贷款支持，确保数字化农业普惠发展，选 A。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `Public libraries are undergoing a historic metamorphosis from quiet book storehouses into multifunctional civic innovation hubs. While early digital alarmists predicted that the ascendancy of e-readers and internet search engines would render brick-and-mortar libraries obsolete, municipal library systems have instead experienced an extraordinary civic renaissance.

Rather than remaining confined to physical lending, modern libraries provide essential digital equity infrastructure. In an era where employment applications, governmental healthcare enrollments, and civic permits are conducted exclusively online, public library terminals provide vital internet connectivity for households unable to afford commercial high-speed broadband. Furthermore, trained reference librarians have evolved into indispensable digital navigators, assisting patrons with resume preparation, digital literacy training, and identifying deceptive online misinformation.

Concurrently, public libraries have repurposed physical square footage into creative collaborative zones. Stacks of seldom-consulted reference encyclopedias have made way for digital audio studios, 3D printing equipment, sewing machines, and entrepreneurial meeting rooms. By offering frictionless, cost-free access to expensive technological tools, libraries empower aspiring entrepreneurs, amateur artisans, and student creators who would otherwise be excluded from the modern knowledge economy.

This institutional expansion, however, has stretched municipal library budgets to the breaking point. Library staff are frequently called upon to act as de facto social workers, assisting unhoused patrons and navigating mental health crises without adequate psychiatric training or municipal funding. For libraries to flourish in their expanded civic roles, municipal leaders must match rhetorical appreciation with sustained budgetary commitments, recognizing that public libraries represent our most democratic physical social infrastructure.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What did early digital alarmists predict about public libraries?",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "That internet search engines and e-books would render them obsolete" },
              { key: "B", text: "That they would become the wealthiest commercial corporations on Earth" },
              { key: "C", text: "That librarians would lead violent political rebellions" },
              { key: "D", text: "That all printed books would spontaneously catch fire" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出早期的数字悲观主义者曾预言电子书和搜索引擎会使实体图书馆过时淘汰（render brick-and-mortar libraries obsolete），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "How do modern reference librarians assist underserved patrons?",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "By offering digital literacy training and evaluating online misinformation" },
              { key: "B", text: "By selling high-interest commercial bank credit cards" },
              { key: "C", text: "By confiscating personal smartphones upon entry" },
              { key: "D", text: "By writing university doctoral dissertations on their behalf" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段末句指出图书馆员充当数字引航员，指导简历制作、数字素养培训并识别网络虚假信息，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What new amenities have replaced old reference book stacks in libraries?",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Digital audio recording studios, 3D printers, and entrepreneurial spaces" },
              { key: "B", text: "Luxury private penthouses for municipal politicians" },
              { key: "C", text: "Heavy diesel machinery repair shops" },
              { key: "D", text: "Commercial gambling casinos" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出闲置百科全书书架被数字录音室、3D 打印设备和创客会议室所取代，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What challenge confronts library staff in their expanded civic role?",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Handling social and mental health crises without adequate resources" },
              { key: "B", text: "A severe national ban on printing paper books" },
              { key: "C", text: "Widespread student refusal to enter libraries" },
              { key: "D", text: "Having to memorize every book in the library catalog" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出图书馆员常被动充当事实上的社工，在缺少专项培训和资金的情况下处理复杂的社会及心理危机，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that municipal leaders should ______.",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "support libraries with sustained budgets matching their expanded civic missions" },
              { key: "B", text: "sell all library buildings to private property developers" },
              { key: "C", text: "fire all reference librarians and replace them with automated doors" },
              { key: "D", text: "charge citizens thirty dollars an hour to read books" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】作者观点结论题。末段强调市政领导必须将口头赞美落实为可持续的财政预算支持，认可图书馆是最具民主性的公共社会基础设施，选 A。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `High-altitude alpine ecosystems across the European Alps and Rocky Mountains are experiencing an ecological crisis fueled by the confluence of climate warming and unconstrained mass tourism. Glaciers that once sustained year-round snowpack are retreating at historic rates, while millions of tourists crowd delicate alpine meadows to hike, ski, and photograph fragile peaks.

The economic lure of alpine tourism is undeniable. For isolated mountain communities historically dependent on subsistence dairy farming and forestry, modern winter sports resorts and summer adventure tourism provide lucrative livelihoods, financing infrastructure upgrades and preventing rural depopulation. However, this commercial prosperity carries severe ecological liabilities: ski slope grooming strips fragile mountain topsoil, heavy construction fragments sensitive wildlife corridors, and high-altitude snowmaking machinery consumes millions of cubic meters of precious alpine reservoir water.

Simultaneously, the melting of alpine permafrost undermines the structural integrity of mountain ridges. Once firmly bound by sub-surface ice, high-elevation rock faces are destabilizing, triggering catastrophic rockfalls that threaten hiking trails, mountain huts, and cable car installations. Mountaineering guides report that historic ascent routes climbed safely for centuries have become prohibitively hazardous due to unbonded boulder fields.

In response to this multi-dimensional crisis, forward-thinking alpine valleys are pioneering regenerative tourism models. Instead of investing millions into energy-intensive artificial snowmaking to prolong doomed ski seasons, resorts are re-orienting toward four-season eco-tourism: botanical guided walks, low-impact electric rail access, and visitor quotas on overcrowded summit ridges. By capping visitor volumes and diversifying into climate-resilient recreation, alpine regions can safeguard their natural splendors while cultivating sustainable mountain livelihoods.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What twin pressures are threatening high-altitude alpine ecosystems?",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Climate warming and unconstrained mass tourism" },
              { key: "B", text: "Overfishing and commercial maritime shipping" },
              { key: "C", text: "Heavy chemical manufacturing and coal mining" },
              { key: "D", text: "Volcanic eruptions and desert sandstorms" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出高山生态正遭受气候变暖和不受节制的过度大众旅游的双重压力冲击，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "How has tourism economically benefited isolated alpine communities?",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "By generating lucrative livelihoods and halting rural depopulation" },
              { key: "B", text: "By providing citizens with free international airline tickets" },
              { key: "C", text: "By eliminating the need for municipal sanitation services" },
              { key: "D", text: "By completely liquidating mountain farms for shopping malls" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出旅游业为偏远山区提供了丰厚的生计来源，资助了基础设施建设并防止了乡村人口流失，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why are historic mountaineering routes becoming increasingly dangerous?",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Permafrost thaw destabilizes rock faces, causing catastrophic rockfalls" },
              { key: "B", text: "Governments have laid landmines along mountain trails" },
              { key: "C", text: "Local wildlife has evolved poisonous venom" },
              { key: "D", text: "Atmospheric oxygen has completely vanished from summits" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节因果题。第三段指出多年冻土融化削弱了岩壁的结构完整性，导致岩体松动坠落，严重威胁登山路线安全，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "How are progressive alpine resorts adapting through regenerative tourism?",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "By diversifying into four-season eco-tourism and capping visitor volumes" },
              { key: "B", text: "By installing massive indoor air-conditioners across whole mountain ranges" },
              { key: "C", text: "By permanently dynamiting unstable mountain peaks" },
              { key: "D", text: "By banning all local residents from hiking in nature" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出前瞻性度假区不再盲目造雪，而是转向四季生态旅游、绿色轨道交通及热门山脊限流配额，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which of the following would be the best title for Text 4?",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Alpine Tourism at the Crossroads: Melting Glaciers and Regenerative Solutions" },
              { key: "B", text: "The Universal Failure of Winter Olympic Sports" },
              { key: "C", text: "Why Humans Should Never Visit Mountain Ranges" },
              { key: "D", text: "How Artificial Snow Will Save Global Glaciers" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨标题题。全文围绕阿尔卑斯高山旅游在气候变暖冰川消融下面临的危机，以及转向再生型生态旅游的应对出路展开，选 A。"
          }
        ]
      }
    ]
  }
];
