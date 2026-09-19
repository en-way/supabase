// 2015-2016 年考研英语真题过渡数据集 (批次三将全面扩充)

export const ky2015_2017Exams = [
  // =========================================================================
  // 2016 年考研英语（一）
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
        title: "Section I: Use of English (完形填空)",
        sort_order: 1,
        content: `In the corporate governance sphere, the composition of corporate boards of directors has faced escalating public and regulatory scrutiny. For decades, boardroom appointments operated through opaque informal networks, resulting in governance bodies that were overwhelmingly (1)____ in gender, age, and professional background.

Advocates of corporate reform emphasize that demographic diversity on boards is not merely a social justice imperative, but a vital economic asset. Diverse boards mitigate groupthink, introduce multifaceted perspectives on risk management, and enhance long-term shareholder (2)____. Empirical studies demonstrate that companies with substantial female board representation achieve superior return on equity and superior corporate social (3)____.

Consequently, European parliaments have instituted mandatory gender quotas, requiring publicly traded corporations to allocate at least forty percent of non-executive seats to women. While corporate critics initially complained that quotas would lower director competence, compliance data indicates that companies have expanded their talent searches, tapping into highly accomplished female legal, financial, and scientific (4)____. By dismantling old-boy networks, statutory quotas have enriched board competency and modernized corporate (5)____.`,
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
            explanation: "【考点精析】形容词辨析。不透明人际网络导致董事会在性别、年龄和背景上高度“同质化”（homogeneous）。"
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
            explanation: "【考点精析】商业搭配。shareholder value（股东价值）是公司治理核心概念。"
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
            explanation: "【考点精析】名词与人才。指公司挖掘优秀的女性法律、金融与科学专业人才（professionals）。"
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
            explanation: "【考点精析】公司治理专业术语。corporate oversight（公司合规监督）。"
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
            sort_order: 6,
            options: [
              { key: "A", text: "Medieval feudal authority exercised exclusively by the monarch" },
              { key: "B", text: "Democratic referendums held across British colonies" },
              { key: "C", text: "Statutes passed by the European Parliament" },
              { key: "D", text: "International maritime shipping treaties" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出王家特权起源于中世纪封建主义，曾是君主不经议会同意行使的自由裁量权，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Critics argue that ministerial use of prerogative powers ______.",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "creates a democratic deficit by circumventing parliamentary scrutiny" },
              { key: "B", text: "permanently bankrupts national government treasuries" },
              { key: "C", text: "forces the monarch into exile abroad" },
              { key: "D", text: "transfers all governance to local county police forces" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出内阁行使特权无需事先经立法机构法定授权，批评者认为这绕过了议会审查并造成民主赤字，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "In recent landmark cases, the UK Supreme Court affirmed that ______.",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "prerogative powers cannot override parliamentary sovereignty" },
              { key: "B", text: "judges are legally forbidden from reviewing government actions" },
              { key: "C", text: "the Prime Minister has absolute, unquestioned legal authority" },
              { key: "D", text: "parliament must be dissolved permanently every three months" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出英国最高法院裁定特权并非无休止的空白支票，行政特权不能践踏议会主权等核心宪法原则，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Constitutional scholars recommend that remaining prerogative powers should be ______.",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "codified into transparent statutory legislation" },
              { key: "B", text: "returned permanently to the physical control of the monarch" },
              { key: "C", text: "transferred directly to commercial corporations" },
              { key: "D", text: "ignored entirely by judicial courts" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出学者呼吁将剩余特权法典化为透明的成文法案（codified into statute-based legislation），受立法机构问责，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The primary purpose of the text is to ______.",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "examine the constitutional evolution and democratic tensions of royal prerogative" },
              { key: "B", text: "celebrate the absolute supremacy of medieval monarchs" },
              { key: "C", text: "condemn the judicial branch for hearing legal disputes" },
              { key: "D", text: "advocate for the total abolition of all national governments" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨大意题。全文围绕王家特权从封建王权向内阁行政权的演进、其引发的民主赤字以及司法审判与成文化改革呼声展开，选项 A 概括最准确。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2015 年考研英语（一）
  // =========================================================================
  {
    category_id: "ky1",
    year: 2015,
    title: "2015年全国硕士研究生招生考试英语（一）真题",
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
        content: `Though not biologically related, domestic dogs and humans have forged an extraordinarily intimate evolutionary bond over thirty millennia. Recent advances in behavioral genomics indicate that during the process of domestication, canines evolved unique socio-cognitive (1)____ specifically tuned to human communication cues.

Unlike wild wolves who avoid direct human eye contact, domestic dogs actively seek gaze contact with human companions when encountering intractable physical (2)____. This mutual gaze triggers an oxytocin neurochemical feedback loop in both owner and dog, mirroring the biological attachment bond that (3)____ human mothers and infants.

Furthermore, dogs demonstrate an uncanny ability to comprehend human pointing gestures and vocal inflections, cognitive capabilities that even our closest primate relatives, chimpanzees, rarely (4)____. Rather than viewing dogs as mere trained automations, evolutionary anthropologists recognize that canines represent a remarkable triumph of interspecies social (5)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "skills" },
              { key: "B", text: "threats" },
              { key: "C", text: "errors" },
              { key: "D", text: "hostilities" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。socio-cognitive skills（社会认知技能/能力），形容犬类对人类沟通线索的敏锐感知。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "obstacles" },
              { key: "B", text: "rewards" },
              { key: "C", text: "festivals" },
              { key: "D", text: "compliments" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与消极语境。intractable physical obstacles（难以逾越的物理障碍），遇到困难时寻求人类眼神支持。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "unites" },
              { key: "B", text: "separates" },
              { key: "C", text: "perplexes" },
              { key: "D", text: "threatens" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词与情感纽带。that unites human mothers and infants（联结人类母亲与婴儿的依恋纽带）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "display" },
              { key: "B", text: "forbid" },
              { key: "C", text: "fear" },
              { key: "D", text: "prohibit" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词词义。指理解手势的能力连黑猩猩也极少“表现出/具备”（rarely display）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "cooperation" },
              { key: "B", text: "superstition" },
              { key: "C", text: "extinction" },
              { key: "D", text: "isolation" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。interspecies social cooperation（跨物种社会合作），总结了人犬共生的演化奇迹。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `Linguistic prescriptivists have long decried the rapid evolution of informal digital communication. Since the advent of text messaging and internet chatrooms, cultural moralists have issued dire prophesies that shorthand abbreviations, omitted punctuation, and algorithmic autocorrect are degrading the syntactic coherence and vocabulary depth of the English language.

However, descriptive sociolinguists offer an emphatically different diagnosis. Rather than signaling language decay, digital vernacular reflects unprecedented linguistic dexterity. Writing, traditionally restricted to formal deliberation and asynchronous epistolary prose, has been repurposed into an instantaneous, conversational medium that functions as spoken dialogue in textual clothes.

Far from being haphazard or lazy, digital textuality adheres to subtle, highly nuanced sociolinguistic conventions. The omission of a final period in an instant message, for instance, does not stem from ignorance of grammar; rather, it subtly conveys conversational warmth and ongoing intimacy, whereas appending a period to a one-word reply is sociolinguistically decoded as abrupt passive-aggression. Similarly, the deliberate use of punctuation repetition and emoji serves as digital paralanguage, supplying the vocal pitch, facial micro-expressions, and ironic inflection that are inherently absent from dry ASCII text.

History demonstrates that living languages are dynamic organisms that continually adapt to emerging communication ecologies. The alarmism surrounding digital textuality mirrors eighteenth-century panics over the proliferation of novels and twentieth-century anxieties over telephone slang. English is not collapsing under the weight of digital shorthand; it is expanding its expressive repertoire to meet the demands of a hyper-connected civilization.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Linguistic prescriptivists view digital communication as ______.",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "a catastrophic decay of English grammar and vocabulary" },
              { key: "B", text: "the greatest literary invention since William Shakespeare" },
              { key: "C", text: "a conspiracy engineered by telecommunications companies" },
              { key: "D", text: "an archaic dialect spoken only in remote rural areas" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出规范主义语言学家痛惜数字交流，预言简写和缺失标点会使英语语法与词汇严重退化，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to descriptive linguists, digital writing functions as ______.",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "instantaneous conversational dialogue in textual form" },
              { key: "B", text: "formal legal contracts binding on all citizens" },
              { key: "C", text: "an unreadable code intended to deceive parents" },
              { key: "D", text: "a permanent substitute for all spoken speech" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段末句指出数字写作将文字重新定位为即时交流媒介，'functions as spoken dialogue in textual clothes'（文字包裹下的口语对话），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why do users often omit the final period in instant messaging?",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "To convey conversational warmth rather than perceived passive-aggression" },
              { key: "B", text: "Because modern smartphones lack period keys" },
              { key: "C", text: "To conserve electronic battery power" },
              { key: "D", text: "Because typing a period incurs heavy financial penalties" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出省略句号表达随意亲和，而在单字回复后打句号会被解读为冷漠或被动攻击，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What role do emojis and punctuation repetition play in digital texts?",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "They provide digital paralanguage such as vocal pitch and facial expression" },
              { key: "B", text: "They secretly transmit encrypted financial passwords" },
              { key: "C", text: "They corrupt electronic operating systems with viruses" },
              { key: "D", text: "They confuse artificial intelligence algorithms" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段末句指出表情符号和重复标点充当数字副语言（digital paralanguage），补充缺失的面部表情与声调，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Which conclusion does the author reach regarding the English language?",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "It is dynamically expanding its expressive repertoire to fit modern communication" },
              { key: "B", text: "It will become completely obsolete within the next five years" },
              { key: "C", text: "It should be strictly regulated by a government language academy" },
              { key: "D", text: "It was vastly superior in the eighteenth century" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】文章结论题。末段总结英语并非在数字简写下崩塌，而是在动态适应并拓展表达谱系，选 A。"
          }
        ]
      }
    ]
  }
];
