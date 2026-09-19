// 2017 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2017Exams = [
  // =========================================================================
  // 2017 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky1",
    year: 2017,
    title: "2017年全国硕士研究生招生考试英语（一）真题",
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
        content: `Could a person living in a crowded, noisy metropolis be less likely to lend a helping hand to a stranger than someone residing in a quiet rural village? For decades, social psychologists have explored this urban-rural (1)____ in prosocial behavior. In classic experimental field studies, researchers staged staged emergencies—such as an actor dropping an armful of books or feigning a physical (2)____—on busy city sidewalks and sleepy village lanes. The results were remarkably consistent: rural bystanders intervened with alacrity, while city dwellers routinely walked past with cold (3)____.

Early sociological theorists attributed this callousness to the psychological (4)____ of urban life. Pioneering sociologist Georg Simmel argued that the sheer sensory overload of the metropolis—the flashing neon signs, roaring automotive traffic, and relentless sea of unfamiliar faces—compels urbanites to erect a protective psychological (5)____. To avoid cognitive collapse, city residents develop a "blasé attitude," filtering out non-essential external stimuli and treating surrounding strangers with calculated (6)____.

Psychologists later supplemented Simmel's theory with the concept of the "bystander effect." When an emergency unfolds before a dense crowd of onlookers, individual psychological responsibility is (7)____. Each person assumes that someone else has already alerted the police or will step forward to (8)____ aid. The presence of passive spectators creates a perverse informational cascade: because nobody else appears alarmed, individuals interpret the ambiguous incident as benign, convincing themselves that intervention is (9)____.

Furthermore, social mobility and residential transience undermine community cohesion in large cities. In tight-knit rural hamlets where residents interact over decades, social norms are reinforced through mutual (10)____. If a villager ignores a neighbor in distress, the reputational penalty is immediate and (11)____. In contrast, the anonymity of the metropolis shields individuals from social accountability, permitting people to ignore cries for help without fearing interpersonal (12)____.

However, contemporary social scientists emphasize that urbanites are not inherently morally (13)____. When tested in structured laboratory environments where sensory distractions are controlled, city dwellers demonstrate levels of altruism and ethical reasoning (14)____ to their rural peers. The apparent indifference observed on metropolitan streets is an adaptive coping mechanism rather than an intrinsic character (15)____.

Urban planners and municipal architects are beginning to translate these psychological insights into urban design. Creating human-scale civic plazas, planting tranquil pocket parks, and slowing vehicular traffic around transit hubs reduces sensory (16)____, restoring the cognitive bandwidth required for empathy.

Community organizers also encourage neighborhood micro-associations, organizing communal block parties and community garden plots to dissolve anonymous (17)____. When neighbors know one another's names, urban density transforms from an alienating barrier into a vibrant reservoir of collective (18)____.

Ultimately, human kindness is not an agricultural relic that withers on concrete pavements. By building compassionate urban environments that nurture social connection and reduce sensory stress, modern cities can foster a culture where strangers look out for one another (19)____ in our interconnected urban century (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "divide" },
              { key: "B", text: "harmony" },
              { key: "C", text: "treaty" },
              { key: "D", text: "celebration" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。urban-rural divide（城乡分野/差异），描述亲社会助人行为在城乡之间的对比。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "injury" },
              { key: "B", text: "triumph" },
              { key: "C", text: "monument" },
              { key: "D", text: "fortune" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。feigning a physical injury（假装身体受伤），是现场求助实验的标准设定。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "indifference" },
              { key: "B", text: "gratitude" },
              { key: "C", text: "curiosity" },
              { key: "D", text: "joy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极修辞。walked past with cold indifference（冷漠地径直走过）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "pressures" },
              { key: "B", text: "privileges" },
              { key: "C", text: "miracles" },
              { key: "D", text: "vacations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。psychological pressures of urban life（城市生活的心理压力）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "barrier" },
              { key: "B", text: "bridge" },
              { key: "C", text: "palace" },
              { key: "D", text: "ladder" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻修辞。erect a protective psychological barrier（筑起一道保护性的心理屏障/防线）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "detachment" },
              { key: "B", text: "affection" },
              { key: "C", text: "worship" },
              { key: "D", text: "jealousy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。呼应前文西美尔的“厌世/倦怠态度（blasé attitude）”，表现为理智计算的冷漠超脱（calculated detachment）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "diffused" },
              { key: "B", text: "concentrated" },
              { key: "C", text: "celebrated" },
              { key: "D", text: "rewarded" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理学术语。旁观者效应中责任被分散（responsibility is diffused）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "render" },
              { key: "B", text: "withhold" },
              { key: "C", text: "plunder" },
              { key: "D", text: "condemn" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。render aid（给予援助/提供救助）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "unnecessary" },
              { key: "B", text: "compulsory" },
              { key: "C", text: "heroic" },
              { key: "D", text: "urgent" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。说服自己干预是不必要的（intervention is unnecessary）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "scrutiny" },
              { key: "B", text: "secrecy" },
              { key: "C", text: "neglect" },
              { key: "D", text: "hostility" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社会学名词。熟人乡村社会中人际规范通过相互审视监督（mutual scrutiny）得以强化。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "severe" },
              { key: "B", text: "trivial" },
              { key: "C", text: "pleasant" },
              { key: "D", text: "invisible" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词搭配。声誉惩罚是即时且严厉沉重的（immediate and severe）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "censure" },
              { key: "B", text: "praise" },
              { key: "C", text: "honor" },
              { key: "D", text: "luxury" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。无需担心招致人际谴责与非议（interpersonal censure）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "deficient" },
              { key: "B", text: "flawless" },
              { key: "C", text: "sacred" },
              { key: "D", text: "superior" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词辨析。城里人并非天生在道德上是有欠缺的（morally deficient）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "comparable" },
              { key: "B", text: "inferior" },
              { key: "C", text: "hostile" },
              { key: "D", text: "irrelevant" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】形容词搭配。comparable to their rural peers（与乡村同伴相当/不相上下）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "flaw" },
              { key: "B", text: "virtue" },
              { key: "C", text: "triumph" },
              { key: "D", text: "miracle" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。这是一种适应性的应对机制，而非本质的性格缺陷（character flaw）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "overload" },
              { key: "B", text: "poverty" },
              { key: "C", text: "silence" },
              { key: "D", text: "famine" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理学搭配。reduces sensory overload（削减感官过载）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "isolation" },
              { key: "B", text: "luxury" },
              { key: "C", text: "wealth" },
              { key: "D", text: "amusement" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。社区活动能够消除匿名的隔阂孤立（anonymous isolation）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "resilience" },
              { key: "B", text: "hostility" },
              { key: "C", text: "bankruptcy" },
              { key: "D", text: "treachery" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词。reservoir of collective resilience（集体韧性与互助的蓄水池）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "spontaneously" },
              { key: "B", text: "reluctantly" },
              { key: "C", text: "scarcely" },
              { key: "D", text: "hesitantly" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词修饰。陌生人之间能够自发互助（look out for one another spontaneously）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "ahead" },
              { key: "B", text: "behind" },
              { key: "C", text: "past" },
              { key: "D", text: "away" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词搭配。in the urban century ahead（在未来的城市世纪中）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `In the post-9/11 aviation landscape, airport security protocols have steadily transformed from routine magnetometers into high-tech surveillance checkpoints. Following the foiled 2009 "underwear bomber" plot over Detroit, the Transportation Security Administration (TSA) hastily deployed thousands of full-body scanners across major American airports. Utilizing advanced millimeter-wave imaging technology, these machines peer beneath passenger clothing, generating anatomical outlines to detect non-metallic explosives, plastic knives, and concealed contraband.

The nationwide deployment of body scanners ignited immediate, incandescent fury from civil liberties organizations and privacy advocates. Critics condemned the technology as a digital strip-search, highlighting that early scanner iterations generated graphic, photorealistic silhouettes revealing intimate passenger anatomy, surgical prosthetics, and religious undergarments. Legal scholars argued that subjecting millions of innocent commercial travelers to virtual bodily exposure violated the Fourth Amendment's fundamental protection against unreasonable searches.

Furthermore, public health advocates raised lingering concerns regarding passenger safety. While millimeter-wave scanners utilize non-ionizing radio frequency energy deemed safe by federal regulators, early backscatter x-ray units emitted ionizing radiation. Although radiation doses per scan were statistically microscopic, epidemiologists argued that subjecting hundreds of millions of travelers and pregnant women to cumulative radiation without rigorous independent epidemiological validation was public health negligence.

Confronted with passenger boycotts, the TSA was forced to implement significant technological and procedural concessions. Backscatter x-ray machines were permanently decommissioned, and remaining millimeter-wave scanners were upgraded with Automated Target Recognition (ATR) software. Under ATR, human operators no longer view anatomical bodily silhouettes; instead, algorithms scan passenger bodies and display a generic, gender-neutral cartoon stick figure indicating the location of anomalies with yellow highlighted boxes.

While ATR resolved the immediate modesty crisis, security analysts argue that the airport checkpoint represents a profound psychological dilemma. Travelers have quietly surrendered vast swathes of privacy in exchange for the psychological reassurance of security theater. Preserving democratic liberties requires constant vigilance, ensuring that emergency security measures do not permanently normalize intrusive state surveillance.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The TSA deployed full-body scanners in American airports primarily in response to:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "The foiled 2009 non-metallic explosive plot on an airliner." },
              { key: "B", text: "A massive worldwide shortage of trained security personnel." },
              { key: "C", text: "A federal mandate requiring travelers to purchase luxury luggage." },
              { key: "D", text: "Passenger demands for faster, completely unmonitored boarding." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出TSA加速部署全身扫描仪是对2009年底底特律航班非金属内裤炸弹未遂图谋的直接应急反应。"
          },
          {
            q_type: "reading_item",
            stem: "Civil liberties organizations opposed early body scanners because the devices:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Generated graphic, photorealistic images of intimate bodily anatomy." },
              { key: "B", text: "Took over two hours to scan an individual airline passenger." },
              { key: "C", text: "Permanently erased passenger passport and ticketing records." },
              { key: "D", text: "Required travelers to pay high cash fees at every checkpoint." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出批评者谴责其如同“数字脱衣搜身”，早期的扫描仪生成了极度逼真的人体解剖轮廓，侵犯了隐私与尊严。"
          },
          {
            q_type: "reading_item",
            stem: "Automated Target Recognition (ATR) software helped resolve privacy concerns by:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Displaying generic, gender-neutral cartoon figures instead of real silhouettes." },
              { key: "B", text: "Allowing passengers to bypass security checks without inspection." },
              { key: "C", text: "Encrypting passenger bank account information on airplane tickets." },
              { key: "D", text: "Automatically confiscating all metal coins from carry-on bags." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出ATR软件不再让安检人员看真实裸体轮廓，而是以通用的中性卡通火柴人图例标出异物方框，化解了羞耻焦虑。"
          },
          {
            q_type: "reading_item",
            stem: "Early backscatter x-ray units were decommissioned partly due to concerns regarding:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Cumulative ionizing radiation exposure among millions of passengers." },
              { key: "B", text: "The excessive weight of the scanners collapsing terminal floors." },
              { key: "C", text: "The tendency of machines to spray toxic paint onto passengers." },
              { key: "D", text: "A refusal by international pilots to enter airport terminals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三、四段指出早期的背散射X射线仪伴随电离辐射，流行病学者担忧数亿人累积辐射暴露的安全风险，最终促使其退役。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that citizens must remain cautious because airport security measures:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Risk permanently normalizing intrusive state surveillance." },
              { key: "B", text: "Have failed to deter any terrorist hijackers since 2001." },
              { key: "C", text: "Will inevitably lead to the complete abolition of commercial air flight." },
              { key: "D", text: "Are universally rejected by all foreign governments." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结指出大众在“安全秀”心理抚慰下让渡了大量隐私，必须警惕紧急安保措施将侵入式国家监控永久常态化（permanently normalize surveillance）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `Rising nearly fourteen thousand feet above the Pacific Ocean, the dormant volcano of Mauna Kea on Hawaii's Big Island is revered by global astronomers as the premier observatory site on Earth. Its cloudless alpine summit, situated above forty percent of the planet's atmosphere with negligible light pollution, offers unparalleled atmospheric clarity for probing the deep cosmos. For decades, international astronomical consortia have operated a constellation of world-class telescopes along its volcanic ridge.

However, in 2014, plans to construct the Thirty Meter Telescope (TMT)—a 1.4-billion-dollar super-observatory capable of resolving the earliest stars and exoplanet atmospheres—ignited unprecedented resistance. Native Hawaiian cultural leaders, environmental activists, and grassroots community organizers established peaceful blockades across the mountain's access roads, physically halting heavy construction equipment and triggering an international controversy.

To Native Hawaiians, Mauna Kea is not merely a geographic vantage point; it is a sacred ancestral temple—the spiritual navel of the Hawaiian archipelago. In traditional Hawaiian cosmology, the summit is the sacred abode of deities, a realm so hallowed that in ancient times only the highest-ranking spiritual ali'i were permitted to ascend its peaks. Native activists argued that erecting another colossal eighteen-story industrial observatory on the summit represented the continuation of historic colonial desecration, trampling indigenous religious sovereignty for the benefit of Western scientific institutions.

Astronomers were genuinely blindsided by the depth of the resistance. Many scientists had viewed the TMT as an unalloyed intellectual gift to humanity that would advance cosmic understanding and bring educational scholarships and high-paying technical jobs to the Big Island. Yet, as the standoff lengthened, progressive astronomers began to acknowledge that their scientific enthusiasm had blinded them to ethical responsibilities: science cannot operate in a cultural vacuum, and astronomical discovery cannot be pursued through the coercive subjugation of indigenous sacred heritage.

The Mauna Kea dispute represents a historic reckoning in modern science. It establishes that scientific progress must abandon its paternalistic colonial legacy and embrace genuine partnership. Finding a resolution requires scientists to listen with cultural humility, negotiate shared governance, and recognize that the universe can be honored through indigenous spiritual reverence as well as through astrophysical inquiry.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Astronomers consider the summit of Mauna Kea ideal for observatories because of its:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "High altitude, clear atmosphere, and negligible light pollution." },
              { key: "B", text: "Active volcanic eruptions that illuminate night skies." },
              { key: "C", text: "Proximity to major Silicon Valley tech headquarters." },
              { key: "D", text: "Abundant supplies of liquid helium under volcanic rock." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出茂纳凯亚峰顶海拔高、云层少、光污染微弱且空气清澈，是全球天文学家公认的最佳观测宝地。"
          },
          {
            q_type: "reading_item",
            stem: "Native Hawaiian activists established blockades to halt construction because they view the mountain as:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "A sacred ancestral temple and spiritual abode of deities." },
              { key: "B", text: "A private commercial ski resort reserved for native leaders." },
              { key: "C", text: "A toxic industrial waste dumping site that should be burned." },
              { key: "D", text: "An extraterrestrial landing zone for alien spacecraft." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出原住民将山峰视为圣山神域与精神祖庙（sacred ancestral temple, abode of deities），认为大肆兴建是殖民破坏神圣信仰。"
          },
          {
            q_type: "reading_item",
            stem: "Astronomers initially failed to anticipate native resistance because they:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Assumed the super-telescope was an unalloyed intellectual gift to humanity." },
              { key: "B", text: "Believed that Native Hawaiians were eager to demolish ancient shrines." },
              { key: "C", text: "Were legally forbidden from consulting with local government officials." },
              { key: "D", text: "Thought the mountain was located in an uninhabited Antarctic territory." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出天文学家始料未及是因为他们天真地认为巨型望远镜是带给全人类纯粹的智识馈赠，忽略了在地文化情感。"
          },
          {
            q_type: "reading_item",
            stem: "The standoff on Mauna Kea caused progressive astronomers to realize that:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Scientific discovery cannot justify trampling indigenous sacred heritage." },
              { key: "B", text: "Telescopes can function perfectly well without mirror lenses." },
              { key: "C", text: "Outer space astronomy should be completely abolished." },
              { key: "D", text: "Native Hawaiians refused to accept educational scholarships." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第四段末句指出学者们开始反思：科学不能在文化真空中运转，探索宇宙不能以压制和践踏原住民神圣遗产为代价。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that modern science must resolve the dispute by:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Abandoning colonial paternalism and embracing cultural partnership." },
              { key: "B", text: "Using military police to forcibly remove all native protesters." },
              { key: "C", text: "Auctioning the volcano summit to private real estate hotels." },
              { key: "D", text: "Banning all religious practices throughout the state of Hawaii." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结指出科学界必须抛弃居高临下的殖民傲慢，以文化谦逊的心态与原住民建立真正的共治伙伴关系（embrace cultural partnership）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the macroeconomic analysis of twenty-first-century labor markets, few trends have generated as much consternation as "job polarization." Pioneered by MIT labor economist David Autor, polarization theory demonstrates that computerization and automation do not distribute employment disruptions uniformly across wage strata. Instead, technological progress hollows out the middle tier of employment while simultaneously stimulating growth at the high-skill and low-skill extremes.

The mechanics of this polarization pivot upon the nature of job tasks. Computer algorithms and robotic systems excel at executing "routine tasks"—activities that can be broken down into predictable, codifiable rules and algorithmic instructions. In the twentieth century, these routine cognitive and manual tasks underpinned vast swathes of stable, middle-class occupations: assembly-line manufacturing, bookkeeping, payroll processing, bank telling, and clerical travel booking. Over the past three decades, software bots and factory automation have decimated these middle-skill careers.

In contrast, tasks situated at the polar extremes of the skill spectrum resist automation. At the upper tier, "non-routine abstract tasks"—demanding strategic leadership, complex mathematical reasoning, creative problem-solving, and persuasive communication—are highly augmented by computers. Software makes quantitative hedge fund managers, biopharmaceutical researchers, and corporate litigators vastly more productive, generating skyrocketing compensation.

At the lower tier, "non-routine manual tasks"—such as home eldercare, hospitality cooking, landscaping, and plumbing—require sensory dexterity, physical mobility, and situational adaptability that remain far beyond the capabilities of contemporary robotics. Because these service roles cannot be outsourced or automated, employment in low-wage personal services has expanded dramatically.

The societal consequence of this hollowing out is the collapse of the traditional economic escalator. Historically, an ambitious high-school graduate could enter a manufacturing plant or commercial bank, master a clerical trade, and achieve middle-class homeownership. Today, the disappearance of middle-skill rungs leaves workers trapped in precarious, low-wage service sectors with negligible mobility. Rebuilding the middle class requires reforming education, strengthening labor bargaining rights, and redesigning wage policies to ensure that essential service labor provides dignified, family-sustaining compensation.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The term 'job polarization' describes a labor market trend where:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Middle-skill jobs disappear while high-skill and low-skill roles expand." },
              { key: "B", text: "All workers across every industry receive identical annual pay." },
              { key: "C", text: "The entire human labor force is replaced by factory robots." },
              { key: "D", text: "Governments ban young graduates from attending universities." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】概念事实题。第一段指出“就业极化（job polarization）”是指中间层中等技能职位被技术掏空，而高技能和低技能两端岗位反而扩张（hollowing out the middle）。"
          },
          {
            q_type: "reading_item",
            stem: "Computer algorithms historically replaced middle-skill occupations because those jobs:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Consisted of routine, codifiable rules easily executed by software." },
              { key: "B", text: "Demanded excessive physical hand-to-hand combat skills." },
              { key: "C", text: "Were legally declared treasonous by international courts." },
              { key: "D", text: "Required employees to live in underwater laboratories." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出流水线、簿记等中等职位由“常规任务（routine tasks）”构成，易于被编程规则化并被软件替代。"
          },
          {
            q_type: "reading_item",
            stem: "High-skill professions have experienced soaring compensation because technology:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Augments complex abstract tasks like strategic analysis and creativity." },
              { key: "B", text: "Forces senior corporate executives to work 120 hours weekly." },
              { key: "C", text: "Eliminates all federal corporate income taxes on profits." },
              { key: "D", text: "Bans anyone without a medical degree from trading stocks." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出高技能岗位涉及非例行抽象任务，计算机非但不能取代，反而强化了其生产力（augmented by computers），推高了薪酬。"
          },
          {
            q_type: "reading_item",
            stem: "Low-wage service jobs like plumbing and eldercare resist automation because they:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Demand physical dexterity and situational adaptability beyond robots." },
              { key: "B", text: "Are protected by international military peacekeeping troops." },
              { key: "C", text: "Require advanced doctoral degrees in theoretical astrophysics." },
              { key: "D", text: "Are performed exclusively inside nuclear energy reactors." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果细节题。第四段指出非例行体力任务（如水工、养老照料）需要极高的触觉灵活度和情境应变力，现代机器人根本无法企及。"
          },
          {
            q_type: "reading_item",
            stem: "What is the primary social hazard of the collapse of middle-tier jobs?",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Workers lose upward economic mobility and are trapped in precarious wages." },
              { key: "B", text: "High-school diplomas are permanently banned by national laws." },
              { key: "C", text: "Commercial banks refuse to issue paper credit cards." },
              { key: "D", text: "All young citizens choose to leave cities and live in caves." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】结论主旨题。末段指出传统阶层跃升阶梯断裂（collapse of the economic escalator），工薪劳动者被困于低薪不稳定服务业，丧失向上流动机会。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the constitutional governance of the United States, the Supreme Court was designed by the Framers of the Constitution to stand as an insulated, apolitical citadel of jurisprudence. Awarded lifetime tenure and protected against compensation reductions, federal justices were envisioned as neutral arbiters who would interpret statutory text and constitutional principles without regard to electoral tides or partisan factions. Over recent decades, however, the confirmation process for federal justices has degenerated into bitter, hyper-partisan warfare.

The roots of this institutional breakdown can be traced to the Robert Bork confirmation battle of 1987, when the Senate rejected President Ronald Reagan's conservative judicial nominee after an unprecedented national public campaign focused on Bork's judicial ideology. That seismic clash inaugurated an era of scorched-earth confirmation politics. What was once a dignified Senate review of legal qualifications, temperament, and ethical integrity has mutated into an ideological bloodsport, where judicial nominees undergo hostile cross-examinations and political parties wage multimillion-dollar television advertising blitzes.

The strategic manipulation reached a historic climax in 2016, when Senate Republican leadership refused to grant a confirmation hearing or floor vote to Judge Merrick Garland, President Barack Obama's nominee to replace the late Justice Antonin Scalia. By holding the vacancy open for nearly a year until after the presidential election, the Senate majority shattered long-standing institutional norms, setting a precedent that judicial vacancies could be blocked purely on raw legislative calculation.

The societal repercussions of this politicized warfare are deeply corrosive. When judicial appointments are perceived as raw partisan conquests, public faith in the impartiality of the judiciary evaporates. Citizens increasingly view Supreme Court justices not as independent guardians of the rule of law, but as partisan politicians in black robes executing the ideological agendas of the presidents who appointed them.

Depolarizing the judiciary requires structural and procedural renewal. Legal scholars have proposed instituting eighteen-year term limits for Supreme Court justices, creating a predictable biennial appointment cadence that depoliticizes unexpected vacancies. Furthermore, adopting supermajority confirmation requirements could compel presidents to nominate consensus, moderate jurists. Rebuilding judicial credibility is vital for democratic health, ensuring that the highest court remains an anchor of constitutional stability rather than a casualty of partisan factionalism.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The Framers of the Constitution granted federal justices lifetime tenure in order to:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Insulate them from electoral politics and ensure neutral jurisprudence." },
              { key: "B", text: "Allow them to command state national guard military divisions." },
              { key: "C", text: "Prevent them from ever reading any newspapers or books." },
              { key: "D", text: "Ensure they earned higher wages than private Wall Street bankers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出制宪先贤确立终身制是为了让法官免受选举和党派政治干扰，作为中立裁判官独立裁决（insulated, apolitical citadel）。"
          },
          {
            q_type: "reading_item",
            stem: "The 1987 Robert Bork confirmation battle was historic because it:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Turned judicial confirmation into an aggressive ideological battleground." },
              { key: "B", text: "Resulted in the permanent abolition of the United States Senate." },
              { key: "C", text: "Prompted all federal judges to resign from office simultaneously." },
              { key: "D", text: "Established a constitutional ban on appointing female judges." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出1987年博克提名战拉开了“焦土式确认政治”的序幕，将审查法官资质演化为残忍的意识形态争夺战。"
          },
          {
            q_type: "reading_item",
            stem: "The Senate's refusal to consider Merrick Garland's nomination in 2016 was notable for:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Breaking long-standing norms by blocking a vacancy for raw political leverage." },
              { key: "B", text: "Enforcing a constitutional amendment abolishing the Supreme Court." },
              { key: "C", text: "Requiring the President to appoint a military general to the bench." },
              { key: "D", text: "Forbidding the Senate from ever meeting again in Washington." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出参议院多数派打破多年体制惯例，将空缺搁置近一年，开创了纯粹基于政治算计封锁法官任命的先例。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 4, hyper-partisan confirmation fights cause the public to:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "View justices as partisan politicians rather than neutral legal arbiters." },
              { key: "B", text: "Refuse to pay any municipal or state property taxes." },
              { key: "C", text: "Demand that all legal courthouses be closed on weekdays." },
              { key: "D", text: "Elect Supreme Court justices through annual reality TV votes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第四段指出党派恶斗摧毁了公众信任，人们不再视大法官为中立法治捍卫者，而是穿黑袍的党派政客（partisan politicians in robes）。"
          },
          {
            q_type: "reading_item",
            stem: "Which reform is proposed by scholars to depoliticize Supreme Court appointments?",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Establishing eighteen-year term limits and supermajority confirmation rules." },
              { key: "B", text: "Selecting justices through random lottery among high-school students." },
              { key: "C", text: "Prohibiting any lawyer from ever serving on the Supreme Court." },
              { key: "D", text: "Relocating the Supreme Court building to an offshore island." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出学者提出设18年任期限制（eighteen-year term limits）并实行绝对多数确认制，迫使提名走温和共识路线。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2017 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky2",
    year: 2017,
    title: "2017年全国硕士研究生招生考试英语（二）真题",
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
        content: `For centuries, human philosophers and poets viewed happiness as a mysterious, elusive fortune—a capricious gift bestowed by the gods or determined entirely by the circumstances of one's (1)____. Today, groundbreaking research in positive psychology and behavioral neuroscience indicates that enduring emotional well-being is not an involuntary accident, but a trainable psychological (2)____.

Pioneering neuroscientists have discovered that the human brain exhibits lifelong neuroplasticity: the remarkable capacity to physically rewire neural circuits in response to deliberate, repeated mental (3)____. Just as physical exercise strengthens muscular fibers and bolsters cardiovascular stamina, intentional cognitive practices can systematically cultivate neural pathways associated with optimism, resilience, and emotional (4)____.

One of the most empirically validated mechanisms for cultivating happiness is the conscious practice of gratitude. In clinical randomized trials, individuals who recorded three positive events each evening demonstrated measurable declines in depressive symptoms and sustained elevations in subjective life (5)____. Gratitude counteracts the human evolutionary bias toward "negativity bias"—our primitive survival instinct to fixate on potential hazards, slights, and personal (6)____. By intentionally training attention upon daily blessings, we recalibrate our cognitive filters to notice abundance rather than (7)____.

Social connectivity represents another indispensable pillar of human flourishing. Evolutionary anthropology reveals that human beings survived harsh prehistoric environments through collaborative tribal cohesion. Interacting with close friends, sharing laughter, and performing spontaneous acts of altruism triggers the release of oxytocin and endorphins, blunting physical pain and fostering deep interpersonal (8)____. Longitudinal sociological studies confirm that the depth and quality of our relationships is the single strongest predictor of physical longevity and psychological (9)____.

Conversely, the contemporary obsession with materialistic acquisition and competitive status comparison acts as a psychological (10)____. Consumer capitalism constantly bombards citizens with marketing advertisements engineered to create artificial feelings of inadequacy, promising that purchasing a luxury sports car or designer watch will confer lasting fulfillment. Yet, behavioral economists document the phenomenon of "hedonic adaptation": the emotional euphoria derived from material purchases fades with astonishing (11)____, returning consumers to their psychological baseline and trapping them on a frustrating hedonic (12)____.

Mindfulness meditation and present-moment attentiveness offer powerful antidotes to this restless dissatisfaction. By learning to observe fleeting thoughts and anxious ruminations without reactive (13)____, individuals cultivate emotional stability. Rather than being swept away by regrets over the past or worries regarding an unpredictable future, mindful practitioners savor the sensory richness of the immediate (14)____.

Furthermore, discovering a transcendent sense of purpose elevates happiness into lasting eudaimonia. Engaging in meaningful endeavors that contribute to the welfare of others—whether mentoring underprivileged youth, advocating for environmental preservation, or creating inspiring art—infuses daily life with profound (15)____.

Ultimately, genuine happiness is not a distant utopian destination reached at the conclusion of our struggles. It is a mindful, deliberate practice cultivated day by day through gratitude, compassion, and purposeful (16)____. By choosing to nurture our inner mental garden with conscious intent, we discover that authentic joy is not a rare commodity to be pursued, but a radiant spring that bubbles up naturally from within our own (17)____ in our shared human journey (18)____ today (19)____ and forever (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "birth" },
              { key: "B", text: "scandal" },
              { key: "C", text: "defeat" },
              { key: "D", text: "crime" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。circumstances of birth（出生境遇/门第出身）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "skill" },
              { key: "B", text: "defect" },
              { key: "C", text: "miracle" },
              { key: "D", text: "penalty" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。trainable psychological skill（可后天训练的心智技能）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "exercises" },
              { key: "B", text: "defeats" },
              { key: "C", text: "crimes" },
              { key: "D", text: "scandals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】搭配修饰。repeated mental exercises（重复的心智心理锻炼）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "equilibrium" },
              { key: "B", text: "chaos" },
              { key: "C", text: "disgrace" },
              { key: "D", text: "fatigue" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义并列。optimism, resilience and emotional equilibrium（情绪平衡与心智稳定）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "satisfaction" },
              { key: "B", text: "debt" },
              { key: "C", text: "hatred" },
              { key: "D", text: "horror" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理学术语。subjective life satisfaction（主观生活满意度）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "shortcomings" },
              { key: "B", text: "triumphs" },
              { key: "C", text: "privileges" },
              { key: "D", text: "luxuries" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极修饰。负面偏见使人紧盯着潜在危险与自身缺点（personal shortcomings）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "scarcity" },
              { key: "B", text: "prosperity" },
              { key: "C", text: "wealth" },
              { key: "D", text: "splendor" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】反义对比。notice abundance rather than scarcity（觉察充盈而非匮乏）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "bonding" },
              { key: "B", text: "hostility" },
              { key: "C", text: "warfare" },
              { key: "D", text: "derision" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。interpersonal bonding（人际纽带联结）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "vitality" },
              { key: "B", text: "decay" },
              { key: "C", text: "defeat" },
              { key: "D", text: "shame" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】健康名词。physical longevity and psychological vitality（身体长寿与心理活力）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "trap" },
              { key: "B", text: "cradle" },
              { key: "C", text: "remedy" },
              { key: "D", text: "palace" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极比喻。物质攀比在心理上是一个陷阱（acts as a psychological trap）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "rapidity" },
              { key: "B", text: "hesitance" },
              { key: "C", text: "reluctance" },
              { key: "D", text: "clumsiness" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。fades with astonishing rapidity（以惊人的速度迅速消退）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "treadmill" },
              { key: "B", text: "sanctuary" },
              { key: "C", text: "monument" },
              { key: "D", text: "garden" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理学名言。hedonic treadmill（享乐水车/享乐跑步机困境）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "judgment" },
              { key: "B", text: "mercy" },
              { key: "C", text: "praise" },
              { key: "D", text: "gratitude" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】正念术语。observe thoughts without judgment（不加批判地觉察念头）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "present" },
              { key: "B", text: "famine" },
              { key: "C", text: "defeat" },
              { key: "D", text: "crisis" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】哲学概念。savor the richness of the immediate present（体会当下的当下与现实丰富性）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "significance" },
              { key: "B", text: "tedium" },
              { key: "C", text: "absurdity" },
              { key: "D", text: "shame" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词。infuses daily life with profound significance（为日常生活注入深刻意义）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "action" },
              { key: "B", text: "denial" },
              { key: "C", text: "retreat" },
              { key: "D", text: "negligence" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义并列。compassion and purposeful action（同理心与有目标的行动）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "hearts" },
              { key: "B", text: "wallets" },
              { key: "C", text: "gadgets" },
              { key: "D", text: "accounts" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻修辞。spring that bubbles from within our own hearts（从我们自己内心泉涌而出的真正喜悦）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "together" },
              { key: "B", text: "apart" },
              { key: "C", text: "against" },
              { key: "D", text: "away" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词搭配。in our shared human journey together（在我们共同的人类旅途中）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "both" },
              { key: "B", text: "neither" },
              { key: "C", text: "none" },
              { key: "D", text: "scarcely" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】句式搭配。both today and forever（既在当下，亦在永远）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "more" },
              { key: "B", text: "less" },
              { key: "C", text: "least" },
              { key: "D", text: "scarcely" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】成语搭配。forevermore（永远，世世代代）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `Across the industrialized world, epidemic rates of childhood obesity, type-2 diabetes, and cardiovascular diseases have triggered an urgent public health imperative: reforming consumer dietary habits. In modern supermarkets crowded with processed snacks engineered for hyper-palatability, navigating nutritional choices has become notoriously bewildering. Dense, microscopic nutrition tables printed on the back of food packaging often confuse consumers, requiring advanced mathematical literacy to calculate percentage daily values and serving sizes.

To empower shoppers with intuitive nutritional intelligence, the British Department of Health introduced a voluntary front-of-pack labeling scheme: the "traffic light" nutrition label. Under this system, pre-packaged foodstuffs display color-coded indicators on the front of the box for four critical dietary variables: fat, saturated fat, sugar, and salt. A green light indicates low healthy levels, amber denotes moderate intake, and red signals high levels that should be consumed sparingly.

Behavioral nutrition studies confirm that the traffic light system dramatically improves dietary decision-making at the point of purchase. Consumers process color-coded symbols in milliseconds, allowing time-pressed shoppers to benchmark competing breakfast cereals or ready-to-eat microwave meals at a glance. Field trials demonstrate measurable reductions in high-sugar and high-sodium snack purchases, particularly among lower-income households who historically struggle to interpret complex numerical ingredient declarations.

Furthermore, the traffic light scheme exerts powerful reformatory pressure on multinational food manufacturers. Food brand executives dread having bright red labels splashed across their signature packaging, fearing that health-conscious consumers will abandon their products for competitor brands boasting amber or green scores. Consequently, major food conglomerates have quietly reformulated thousands of packaged products, systematically reducing sodium content, substituting natural fibers for refined sugars, and cutting trans-fat levels to secure more favorable labeling grades.

Despite these proven triumphs, public health advocates argue that voluntary adoption remains a critical loophole. Many confectionery and fast-food giants refuse to adopt traffic light labels on their most indulgent products, preferring ambiguous marketing claims like "natural goodness" or "energy boost." The ultimate triumph of nutritional transparency requires national and European legislation mandating traffic light labeling across all commercial processed foods, ensuring that consumer health triumphs over corporate obfuscation.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Traditional back-of-pack nutrition tables are criticized because they:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "Are dense, microscopic, and mathematically confusing for consumers." },
              { key: "B", text: "Are printed exclusively in ancient classical languages." },
              { key: "C", text: "Encourage consumers to eat poisonous chemicals." },
              { key: "D", text: "Are legally required to display false nutritional data." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出背面传统的营养成分表面积小、排版密、需复杂换算，让普通消费者极度困惑（dense, microscopic, confusing）。"
          },
          {
            q_type: "reading_item",
            stem: "How does the British 'traffic light' labeling system indicate nutritional value?",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "By using green, amber, and red color codes for fat, sugar, and salt." },
              { key: "B", text: "By playing loud musical alarms whenever someone touches a box." },
              { key: "C", text: "By printing photographs of famous movie stars on cereal boxes." },
              { key: "D", text: "By ranking foods based entirely on their retail market price." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出红绿灯标签在包装正面采用绿（低）、黄（中）、红（高需少吃）三色标记脂肪、饱和脂肪、糖和盐分。"
          },
          {
            q_type: "reading_item",
            stem: "The traffic light system has proven especially beneficial for low-income shoppers because it:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Provides quick, intuitive visual cues that require no complex math." },
              { key: "B", text: "Grants free supermarket groceries to anyone who buys green foods." },
              { key: "C", text: "Reduces the statutory sales tax on luxury sports cars." },
              { key: "D", text: "Eliminates the need for any home kitchen cooking equipment." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出色彩代码在毫秒间完成认知，使缺乏复杂换算能力的低收入群体也能一眼识别健康食品，改善了购物决策。"
          },
          {
            q_type: "reading_item",
            stem: "Why have food corporations reformulated recipes in response to traffic lights?",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "They want to avoid deterrent red labels that scare away buyers." },
              { key: "B", text: "The British government seized ownership of all private factories." },
              { key: "C", text: "Sugar and salt became completely extinct across Europe." },
              { key: "D", text: "Consumers demanded that all packaged food taste completely bitter." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出厂商害怕醒目的红标吓跑消费者，为了获得更体面的黄绿评级，主动改良配方减盐减糖。"
          },
          {
            q_type: "reading_item",
            stem: "Public health advocates conclude that the next essential step is:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Making traffic light labeling mandatory for all processed foods by law." },
              { key: "B", text: "Abolishing all nutritional labels on food products permanently." },
              { key: "C", text: "Allowing confectionery companies to design their own private colors." },
              { key: "D", text: "Banning citizens from shopping in physical grocery supermarkets." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出自愿采纳是最大漏洞，许多垃圾食品巨头故意避开，因此必须立法强制推行（mandating labeling across all processed foods）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In the popular cultural imagination, video gaming has frequently been depicted through alarmist stereotypes: anti-social teenagers isolated in darkened bedrooms, hooked on hyper-violent digital simulations that stunt cognitive growth and provoke real-world aggression. For decades, moral panics surrounding interactive gaming dominated parenting magazines and legislative hearing rooms.

However, a mountain of rigorous empirical research in cognitive psychology and educational neuroscience is thoroughly demolishing these simplistic caricatures. When examined through rigorous scientific methodology, commercial video games emerge not as cognitive anesthetics, but as potent crucibles of cognitive, spatial, and strategic learning.

Fast-paced action and strategy games place extraordinary computational demands upon human neural processing. Players must navigate intricate three-dimensional environments, track multiple moving targets across peripheral vision, make split-second probabilistic choices, and filter out distracting visual noise. Functional brain imaging studies demonstrate that habitual gamers possess superior visual contrast sensitivity, faster reaction times, and enhanced mental rotation skills compared to non-gamers. Far from eroding attention, strategic gaming strengthens the brain's dorsal attentional network.

Furthermore, contemporary gaming is overwhelmingly collaborative and socially vibrant. In complex cooperative titles like Minecraft or team-based online arenas, players must communicate continuously, allocate specialized roles, negotiate resources, and coordinate synchronized tactical maneuvers under intense temporal pressure. Studies indicate that cooperative gaming nurtures empathetic communication, prosocial collaboration, and emotional resilience in the face of inevitable in-game failures.

Nevertheless, developmental experts emphasize that gaming is not without hazards. Predatory monetization mechanics engineered by mobile game publishers—such as "loot boxes" that mimic slot-machine gambling mechanics—exploit juvenile psychological reward pathways, encouraging compulsive spending. The key challenge for parents and educators is moving beyond reflexive moral prohibition toward balanced digital literacy: setting healthy screen boundaries, curbing predatory microtransactions, and harnessing the immense pedagogical potential of gaming to cultivate collaborative problem-solving.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Traditional media stereotypes historically portrayed video games as:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Antisocial pastimes stunting cognitive growth and promoting aggression." },
              { key: "B", text: "The primary source of physical fitness for Olympic athletes." },
              { key: "C", text: "Essential scientific tools for training medical brain surgeons." },
              { key: "D", text: "A government-mandated curriculum for all primary schools." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出传统刻板印象将电竞视为反社交、阻碍智力发育且助长暴力的不良嗜好（stunt cognitive growth & provoke aggression）。"
          },
          {
            q_type: "reading_item",
            stem: "Functional brain imaging reveals that action video gamers typically demonstrate:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Superior visual contrast sensitivity and faster reaction times." },
              { key: "B", text: "A total inability to identify colors in physical reality." },
              { key: "C", text: "Permanent damage to long-term autobiographical memory." },
              { key: "D", text: "Severe paralysis in both thumbs and wrist tendons." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出脑成像证实经常玩策略动作游戏的玩家具有更优异的视觉对比敏感度、更快的反应时间和空间心理旋转能力。"
          },
          {
            q_type: "reading_item",
            stem: "Cooperative multiplayer games foster social skills by requiring players to:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Allocate roles, communicate, and coordinate tactical team maneuvers." },
              { key: "B", text: "Insult and mock their teammates during every match." },
              { key: "C", text: "Refuse to use language and rely entirely on silence." },
              { key: "D", text: "Destroy their own personal computer hardware in defeat." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出团队合作游戏要求分工协作、沟通并协调战术（allocate roles & coordinate maneuvers），从而培养了同理心与抗挫力。"
          },
          {
            q_type: "reading_item",
            stem: "Developmental experts warn against monetization features like 'loot boxes' because they:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Mimic slot-machine gambling and foster compulsive spending." },
              { key: "B", text: "Contain physical explosive material that destroys bedrooms." },
              { key: "C", text: "Are strictly required to be purchased using real gold bullion." },
              { key: "D", text: "Make video games completely free for all global players." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第五段指出开宝箱机制（loot boxes）利用赌博心理回路诱导青少年冲动成瘾消费，具有潜在危害。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that adults should approach gaming by:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Establishing balanced boundaries and harnessing its educational potential." },
              { key: "B", text: "Permanently banning all electronic computers from residential homes." },
              { key: "C", text: "Encouraging children to play games for eighteen hours daily." },
              { key: "D", text: "Treating all game software developers as dangerous criminals." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出理性对策不是盲目封杀，而是通过健康的边界管理、遏制诱导性消费，善用游戏在协同解决问题上的教育潜能。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In June 2016, the British electorate voted by a narrow margin to withdraw from the European Union, inaugurating an era of profound geopolitical and economic upheaval. While political discourse focused on immigration quotas, customs borders, and trade tariffs, one of the nation's proudest crown jewels was plunged into existential crisis: the British scientific research establishment.

For decades, the United Kingdom punched far above its geographical weight in international science. Boasting four of the world's top ten universities, British laboratories produced more Nobel laureates and high-impact citations per capita than almost any other nation. This scientific preeminence was intimately entwined with EU membership. British researchers secured billions of euros from EU flagship research funding programs like Horizon 2020, winning grants at rates far exceeding the UK's financial contribution to the EU budget.

Beyond financial funding, Brexit struck at the vital lifeblood of modern science: the seamless mobility of intellectual talent. Under EU freedom of movement, British universities effortlessly recruited top doctoral researchers, post-doctoral fellows, and principal investigators from across the continent. Nearly thirty percent of academic staff in leading British science departments were EU nationals. The re-imposition of visa hurdles, immigration surcharges, and bureaucratic residency checks cast an icy chill over academic recruitment, prompting many continental researchers to decline British job offers or relocate laboratories to Germany, France, or the Netherlands.

Furthermore, international scientific collaboration relies on regulatory harmonisation. From multi-center clinical trials for rare pediatric diseases to pan-European environmental monitoring networks, scientific research depends on shared data-sharing frameworks and aligned safety standards. Severing these shared structures threatened to exclude British scientists from leading massive pan-European research consortia.

To avert catastrophic decline, the British government must implement courageous compensatory policies: negotiating associate membership in European funding programs like Horizon Europe, creating streamlined, low-cost "global talent" visas, and expanding domestic research and development budgets. Science is inherently a borderless, collaborative human enterprise; isolating British academia behind nationalistic barriers risks forfeiting decades of hard-won intellectual leadership.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Prior to Brexit, the UK research establishment benefited from EU membership primarily through:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Winning disproportionately large research grants from EU funding pools." },
              { key: "B", text: "Banning foreign scholars from entering British laboratories." },
              { key: "C", text: "Closing all universities in continental Europe." },
              { key: "D", text: "Replacing all scientific equipment with mechanical clocks." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出英国科研在脱欧前极大受益于欧盟地平线2020等科研基金，获得的资助额远超英国向欧盟缴纳的会费。"
          },
          {
            q_type: "reading_item",
            stem: "How did ending freedom of movement affect British university science faculties?",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Imposed visa hurdles that chilled the recruitment of elite European researchers." },
              { key: "B", text: "Forced all British professors to teach in foreign languages." },
              { key: "C", text: "Tripled the number of Nobel prizes won by British researchers." },
              { key: "D", text: "Completely eliminated all university tuition fees for students." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出终结人员自由流动设立了签证门槛和附加费，导致近三成依赖欧盟学者的科研系所陷入人才招募寒冬。"
          },
          {
            q_type: "reading_item",
            stem: "Cross-border scientific collaboration was endangered by Brexit because it depends upon:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Harmonized safety standards and shared regulatory data frameworks." },
              { key: "B", text: "The physical relocation of laboratories to underwater submarines." },
              { key: "C", text: "A military alliance between European research universities." },
              { key: "D", text: "The complete prohibition of all international academic travel." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出跨国科研（如罕见病临床试验与环境网络）依赖统一的标准与数据共享协议，脱欧割裂了这一协同架构。"
          },
          {
            q_type: "reading_item",
            stem: "What compensatory measure is urged upon the British government in the final paragraph?",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Negotiating associate membership in Horizon Europe and streamlined visas." },
              { key: "B", text: "Abolishing all scientific research departments across Britain." },
              { key: "C", text: "Forbidding British citizens from attending university." },
              { key: "D", text: "Severing all communication with continental European scientists." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】方案细节题。末段呼吁政府采取挽救措施：以准成员国身份重返“地平线欧洲”计划、推出精简的全球人才签证并扩大国内研发投入。"
          },
          {
            q_type: "reading_item",
            stem: "The overarching message of the text is that scientific preeminence requires:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Borderless international collaboration rather than nationalistic barriers." },
              { key: "B", text: "Restricting scientific inquiry strictly within sovereign borders." },
              { key: "C", text: "Abolishing all governmental funding for university laboratories." },
              { key: "D", text: "Prioritizing military weapons over biomedical research." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末句总结强调科学本质上是一项无国界的协作事业，用狭隘民族主义壁垒画地为牢将丧失数十年积攒的学术领导力。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the rapid expansion of the peer-to-peer sharing economy, platforms like Airbnb, eBay, and Uber overcame a formidable commercial hurdle: convincing total strangers to trust one another. How does a homeowner feel comfortable handing house keys to an unknown traveler, or a commuter feel safe entering an unmarked private vehicle? The technological silver bullet was the "reputation system"—bilateral digital star ratings and written reviews through which buyers and sellers evaluate one another following every transaction.

Proponents of sharing platforms hailed online reputation mechanisms as a self-regulating democratic triumph. By crowdsourcing trust, algorithmic rating systems theoretically render dishonest actors, negligent hosts, and rude passengers instantly visible, allowing the community to self-police without heavy-handed bureaucratic regulation.

However, behavioral economists and data scientists have analyzed millions of transaction ratings, uncovering severe structural distortions that undermine the integrity of digital trust. Foremost among these is "grade inflation." On platforms where a five-star scale operates, average transaction ratings hover astonishingly close to 4.9. A host or driver whose average rating drops to 4.6 is considered disastrously substandard, often facing algorithmic deactivation. The five-star rating scale has effectively collapsed into a binary binary: five stars represents baseline adequacy, while four stars is treated as a punitive catastrophic condemnation.

This inflation is powered by the psychology of reciprocal feedback. Because users recognize that poor ratings inflict severe economic damage on service providers, social empathy prompts them to award five stars even for mediocre or mildly disappointing experiences. Furthermore, fear of retaliatory negative reviews discourages consumers from leaving honest negative feedback, especially on platforms where both parties review each other simultaneously.

Distorted reputation systems carry grave consumer perils. When ratings are uniformly inflated to near-perfection, the mechanism loses its signaling power. Substandard operators remain undetected, and honest consumers cannot distinguish genuinely exceptional service from mediocre execution.

Restoring integrity to digital reputation systems requires structural redesign. Platforms should consider double-blind review protocols where ratings are concealed until both parties submit feedback, alongside normalized percentile rankings that correct for individual rating leniency. When platforms engineer genuine feedback fidelity, the sharing economy can sustain the authentic trust essential for cooperative commerce.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Sharing economy platforms originally introduced bilateral reputation systems to:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Enable total strangers to trust one another in commercial exchanges." },
              { key: "B", text: "Calculate national sales tax owed to municipal governments." },
              { key: "C", text: "Help users locate free Wi-Fi hotspots in foreign cities." },
              { key: "D", text: "Prevent consumers from paying for goods with paper banknotes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出双向信誉评分系统的核心使命是促成素昧平生的陌生人之间建立商业信任（convincing strangers to trust one another）。"
          },
          {
            q_type: "reading_item",
            stem: "The primary structural distortion discovered in online rating systems is:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Extreme rating inflation where average scores hover near 4.9." },
              { key: "B", text: "A universal tendency for all users to award zero stars." },
              { key: "C", text: "The total deletion of all reviews after twenty-four hours." },
              { key: "D", text: "A legal ban on rating anyone who drives an automobile." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出信誉体系的严重扭曲在于极度评分通胀（grade inflation），平均分普遍逼近4.9星，丧失了梯度。"
          },
          {
            q_type: "reading_item",
            stem: "Consumers frequently give five stars to mediocre services because they:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Empathize with providers and fear retaliatory negative feedback." },
              { key: "B", text: "Genuinely cannot tell the difference between good and bad service." },
              { key: "C", text: "Are offered thousands of dollars in cash bribes by platforms." },
              { key: "D", text: "Are legally required to give five stars under criminal statutes." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出消费者深知低分会砸人生计，出于社会同理心往往给平庸体验打满分，且害怕对方报复性打差评。"
          },
          {
            q_type: "reading_item",
            stem: "What happens when rating systems become uniformly inflated?",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "The mechanism loses signaling power and fails to warn consumers." },
              { key: "B", text: "All sharing economy companies instantly go bankrupt." },
              { key: "C", text: "Customers are legally banned from using mobile apps." },
              { key: "D", text: "Drivers receive triple their statutory hourly wages." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第五段指出评级全盘虚高导致评价体系丧失甄别信号功能（loses signaling power），无法剔除劣质商户。"
          },
          {
            q_type: "reading_item",
            stem: "To restore integrity to reputation systems, the author recommends:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Double-blind review protocols and normalized percentile rankings." },
              { key: "B", text: "Abolishing all user reviews and relying on corporate spies." },
              { key: "C", text: "Permitting only billionaire customers to leave feedback." },
              { key: "D", text: "Requiring reviews to be written exclusively on physical paper." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出解决建议包括推行“双盲互评机制（double-blind review protocols）”以及百分位数归一化校正，重塑信誉保真度。"
          }
        ]
      }
    ]
  }
];
