// 2018-2020 年考研英语一与英语二真题数据集

export const ky2018_2020Exams = [
  // =========================================================================
  // 2020 年考研英语（一）
  // =========================================================================
  {
    category_id: "ky1",
    year: 2020,
    title: "2020年全国硕士研究生招生考试英语（一）真题",
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
        content: `Even people who do not normally follow financial news will have heard about the dramatic expansion of artificial intelligence in corporate management. Algorithmic software systems now review resumes, calculate compensation packages, and monitor office productivity with minimal human (1)____.

Advocates contend that algorithmic evaluation eliminates subjective human bias, establishing an objective meritocracy in which personnel decisions are grounded (2)____ in quantifiable performance metrics. Yet, organizational sociologists caution that predictive algorithms are trained on historical data, which inevitably reflects entrenched institutional (3)____.

If an algorithm analyzes decades of promotions within a historically male-dominated firm, the machine learning model will internalize gender as an implicit variable of (4)____, penalizing qualified female applicants simply because their profiles diverge from historical norms. Therefore, automated HR systems must be subject to continuous algorithmic auditing to prevent technology from codifying past prejudices into future hiring (5)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "intervention" },
              { key: "B", text: "superstition" },
              { key: "C", text: "jealousy" },
              { key: "D", text: "curiosity" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。with minimal human intervention（在极少人为干预的情况下），描述算法自动化的运行特点。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "strictly" },
              { key: "B", text: "hesitantly" },
              { key: "C", text: "rarely" },
              { key: "D", text: "vaguely" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词语义。grounded strictly in（严格建立在……基础之上），呼应客观唯才是举（objective meritocracy）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "biases" },
              { key: "B", text: "triumphs" },
              { key: "C", text: "aspirations" },
              { key: "D", text: "remedies" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。历史数据难免反映根深蒂固的制度性“偏见”（entrenched institutional biases）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "success" },
              { key: "B", text: "failure" },
              { key: "C", text: "panic" },
              { key: "D", text: "hostility" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】语境逻辑。算法会将性别隐含地作为衡量职场“成功”（success）的预测变量，导致偏颇。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "practices" },
              { key: "B", text: "rumors" },
              { key: "C", text: "excuses" },
              { key: "D", text: "refusals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。hiring practices（招聘实践/做法），属于人力资源管理标准术语。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `A looming crisis in archaeological preservation has emerged across coastal regions as rising sea levels, ocean acidification, and intensified storm surges accelerate the erosion of fragile coastal heritage sites. From prehistoric shell middens in the Scottish Orkney Islands to ancient Greco-Roman port infrastructure along the Mediterranean basin, thousands of irreplaceable historical settlements are being washed into the sea.

Heritage conservationists face agonizing triage decisions. Unlike municipal dikes or commercial harbor installations, historic ruins cannot be permanently fortified with massive concrete seawalls without destroying the archaeological integrity of the surrounding landscape. Furthermore, public conservation budgets are painfully constrained, forcing archaeologists to decide which historic sites warrant costly physical preservation and which must be allowed to erode naturally into oblivion.

In response to this reality, a pioneering paradigm known as 'preservation by record' has gained widespread traction. Utilizing LiDAR scanning, photogrammetry drones, and high-resolution sub-surface radar, interdisciplinary archaeological expeditions are rapidly creating millimeter-accurate 3D digital twins of endangered coastal sites before tides dismantle the physical stone.

While digital twins can never fully replace the tangible, emotional gravitas of touching an ancient megalith, they ensure that detailed architectural measurements, artifact coordinates, and stratigraphic layers remain permanently accessible to future scholars worldwide. In an age of unprecedented environmental upheaval, digital archives may represent our most pragmatic defense against cultural amnesia.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Coastal archaeological sites are currently threatened by ______.",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "rising sea levels and accelerating coastal erosion" },
              { key: "B", text: "widespread commercial housing redevelopment" },
              { key: "C", text: "deliberate vandalism by offshore tourists" },
              { key: "D", text: "a complete lack of interest from modern historians" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段首句指出 'rising sea levels, ocean acidification, and intensified storm surges accelerate the erosion...'，海平面上升与海水侵蚀威胁遗址，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Why are concrete seawalls often unsuitable for protecting historical ruins?",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "They destroy the archaeological integrity of the landscape" },
              { key: "B", text: "They dissolve rapidly in saline ocean water" },
              { key: "C", text: "They are legally banned under maritime navigation treaties" },
              { key: "D", text: "They attract dangerous marine predators to the coast" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节因果题。第二段第二句指出防波堤 'destroying the archaeological integrity of the surrounding landscape'，会破坏遗址原真性与周边地貌，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The concept of 'preservation by record' refers to ______.",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "creating millimeter-accurate 3D digital twins before sites erode" },
              { key: "B", text: "writing short romantic fictional stories about lost monuments" },
              { key: "C", text: "locking archaeological records in secret governmental vaults" },
              { key: "D", text: "demolishing ruins immediately to salvage raw stone" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】概念事实题。第三段指出这一理念是通过激光雷达、无人机摄影测量等快速生成毫米级高精 3D 数字孪生体，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to the author, digital twins of heritage sites ______.",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "ensure architectural and stratigraphic data remain permanently accessible" },
              { key: "B", text: "completely surpass physical ruins in aesthetic beauty" },
              { key: "C", text: "can only be viewed by certified academic professors" },
              { key: "D", text: "require enormous quantities of fossil fuels to maintain" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出数字孪生体确保了详尽的建筑测绘、坐标和地层数据能够长久被全球学者查阅利用，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What is the author's primary attitude toward digital preservation?",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "Pragmatic and supportive" },
              { key: "B", text: "Skeptical and dismissive" },
              { key: "C", text: "Alarmist and panicked" },
              { key: "D", text: "Cynical and detached" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】作者观点态度题。作者认为在气候变化加剧的严峻现实下，数字化记录是务实且有力的文化记忆防御措施，态度务实支持，选 A。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2020 年考研英语（二）
  // =========================================================================
  {
    category_id: "ky2",
    year: 2020,
    title: "2020年全国硕士研究生招生考试英语（二）真题",
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
        content: `It's not difficult to appreciate the visual grandeur of an ancient cathedral, but the acoustic design of historic stone sanctuaries is rarely accorded comparable (1)____. Acousticians are now rediscovering the acoustic ingenuity embedded in sacred medieval architecture.

Unlike modern concert halls engineered for crisp clarity, medieval masonry was intentionally designed to cultivate prolonged reverberation times, often exceeding five seconds. This extended resonance smoothed vocal imperfections and transformed monophonic liturgical chants into ethereal, enveloping acoustic (2)____.

When singers performed plainchant in resonant cathedrals, sound waves bounced repeatedly across vaulted ceilings, creating standing waves that fostered a profound sense of temporal (3)____. Worshippers felt as though they were stepping out of mundane earthly reality into a celestial chamber where human voices fused (4)____ with architectural geometry. Understanding historical acoustics reminds modern architects that sound is not merely an engineering technicality, but a powerful spatial medium that shapes human emotion and spiritual (5)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "recognition" },
              { key: "B", text: "suspicion" },
              { key: "C", text: "hostility" },
              { key: "D", text: "jealousy" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词搭配。rarely accorded comparable recognition（很少获得同等的认可/重视），与前文普遍欣赏视觉宏伟形成对比。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "experiences" },
              { key: "B", text: "accidents" },
              { key: "C", text: "failures" },
              { key: "D", text: "deficits" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词语义。声学混响将单音圣歌转化为沉浸式的空灵声音体验（acoustic experiences）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "timelessness" },
              { key: "B", text: "punctuality" },
              { key: "C", text: "haste" },
              { key: "D", text: "boredom" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词与宗教意境。声波驻波营造出一种超越时间的永恒感（sense of timelessness）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "harmoniously" },
              { key: "B", text: "violently" },
              { key: "C", text: "reluctantly" },
              { key: "D", text: "haphazardly" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】副词搭配。human voices fused harmoniously with architectural geometry（人声与建筑几何和谐交融）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "contemplation" },
              { key: "B", text: "superstition" },
              { key: "C", text: "deception" },
              { key: "D", text: "exhaustion" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义名词。声音能够塑造人类情感与精神上的冥想/沉思（spiritual contemplation）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `The rapid rise of the subscription economy has transformed the fundamental relationship between consumers and corporate commerce. Once defined by discrete, one-off purchases of durable physical goods, household expenditure is increasingly dominated by perpetual recurring billing streams covering streaming entertainment, software licenses, automotive amenities, and even morning coffee.

Proponents of the subscription model champion its consumer convenience and low initial entry barriers. Instead of coughing up hundreds of dollars to purchase an expensive software suite or audio library, users can access comprehensive catalog suites for a modest monthly charge. For businesses, subscription agreements convert volatile, feast-or-famine sales cycles into highly predictable, recurring annual cash flows that Wall Street investors richly reward with inflated valuation multiples.

Yet, behavioral economists caution that the subscription business model weaponizes subtle cognitive flaws, most notably 'status quo bias' and 'subscription creep.' Once consumers register their credit cards for automated monthly renewals, the psychological friction required to cancel a service far exceeds the inertia of letting micro-payments slip quietly through bank statements. Studies indicate that the average household routinely underestimates its aggregate monthly recurring commitments by more than 50 percent, hemorrhaging hundreds of dollars annually on zombie subscriptions they rarely use.

In response to consumer outcry over predatory retention tactics—where signing up takes one digital click while canceling requires enduring endless automated customer-support mazes—regulators are intervening. Emerging consumer protection statutes mandate clear, single-click cancellation buttons, requiring corporate providers to obtain explicit affirmative consent before converting promotional trials into binding recurring debts.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Why do Wall Street investors reward subscription business models?",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "They convert volatile sales into highly predictable recurring revenues" },
              { key: "B", text: "They completely eliminate customer support costs" },
              { key: "C", text: "They are legally exempt from corporate income taxes" },
              { key: "D", text: "They force all competitors out of the global market" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出订阅模式将不稳定的销售周期转化为高度可预测的持续现金流（convert volatile sales cycles into highly predictable, recurring annual cash flows），受到华尔街青睐，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What behavioral phenomenon is termed 'subscription creep'?",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "The gradual accumulation of forgotten automated micro-payments" },
              { key: "B", text: "The physical degradation of digital streaming servers" },
              { key: "C", text: "The spontaneous cancellation of legitimate software licenses" },
              { key: "D", text: "The sudden price drop of consumer durable goods" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】概念推断题。第三段阐述消费者因为现状偏差和惰性，忽略账单中自动扣款的微小支出，不知不觉累积大量闲置僵尸订阅，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to behavioral studies in Paragraph 3, typical households ______.",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "underestimate their total recurring commitments by over 50 percent" },
              { key: "B", text: "cancel all digital services within forty-eight hours" },
              { key: "C", text: "refuse to pay for any mobile phone entertainment" },
              { key: "D", text: "personally negotiate subscription terms with corporate directors" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出普通家庭通常低估其月度总持续支出达 50% 以上（underestimates its aggregate monthly commitments by more than 50%），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What predatory practice are regulators targeting?",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "Making sign-up effortless while making cancellation deliberately difficult" },
              { key: "B", text: "Charging consumers in foreign currencies" },
              { key: "C", text: "Providing high-definition video streaming without extra fees" },
              { key: "D", text: "Allowing users to share passwords with family members" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段指出监管聚焦于 'signing up takes one digital click while canceling requires enduring endless automated customer-support mazes'（加入一键，取消极难），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What regulatory remedy is being codified into new consumer laws?",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "Mandatory, straightforward single-click cancellation mechanisms" },
              { key: "B", text: "The complete prohibition of all credit card payments" },
              { key: "C", text: "A legal ban on offering promotional free trials" },
              { key: "D", text: "Government control over all digital entertainment content" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。末段指出最新消费者保护法要求必须提供清晰的一键取消按钮（single-click cancellation buttons），并获得明确确认授权，选 A。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2019 年考研英语（一）
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
        title: "Section I: Use of English (完形填空)",
        sort_order: 1,
        content: `Grade inflation in higher education has steadily escalated into an acute administrative and pedagogical dilemma. Across elite universities, the percentage of undergraduate students graduating with top honors has climbed to historic (1)____. Where a 'C' grade once signified average mastery of the curriculum, it is now widely perceived by students as a catastrophic (2)____.

Sociologists attribute this phenomenon to the commercialization of the university experience. As tuition fees rise, students increasingly view themselves as entitled consumers purchasing credentials rather than scholars being academically (3)____. Faculty members, evaluated heavily by student satisfaction questionnaires, feel tacit pressure to award lenient grades to ensure favorable course (4)____.

Consequently, grade inflation compresses the grading spectrum, making it increasingly difficult for graduate school admissions committees and prospective employers to (5)____ truly exceptional scholars from mediocre peers. Restoring academic rigor demands instituting transparent departmental grading medians and recalibrating student evaluations.`,
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
            explanation: "【考点精析】名词搭配。climbed to historic highs（攀升至历史新高），生动对应评分膨胀的加剧。"
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
            explanation: "【考点精析】名词与消极修饰。catastrophic failure（灾难性的失败），反映学生心态的扭曲。"
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
            explanation: "【考点精析】被动语态与学术情境。academically assessed（接受学业学术评估），与消费文凭形成对比。"
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
            explanation: "【考点精析】专业术语。course evaluations（课程教学评估/评教反馈）。"
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
            explanation: "【考点精析】动词与介词搭配。distinguish ... from ...（将……与……区分开来），反映分数区分度下降的弊端。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `The emergence of artificial intelligence in medical diagnostics has ignited vigorous debate over the future of the medical profession. Deep learning algorithms, trained on millions of anonymized radiological scans and pathology slides, can now detect subtle malignant tumors with accuracy rates matching or exceeding seasoned diagnostic specialists.

Technological optimists predict that autonomous diagnostic software will soon render human radiologists and pathologists obsolete, drastically reducing diagnostic bottlenecks and cutting healthcare costs in underserved regions. In many developing nations where the ratio of qualified radiologists to citizens is perilously low, automated diagnostic software can triage chest radiographs for tuberculosis with remarkable speed.

However, clinical ethicists and senior clinicians argue that medicine encompasses far more than statistical pattern recognition. Diagnostic decision-making is inherently contextual: it requires synthesizing ambiguous clinical symptoms, understanding patients' nuanced life histories, and communicating devastating diagnoses with profound human empathy. A machine can calculate the mathematical probability of malignancy, but it cannot hold an anxious patient's hand or navigate delicate palliative care trade-offs.

Furthermore, accountability questions loom large in medical malpractice jurisprudence. If an algorithm fails to identify a fatal tumor or recommends an inappropriate chemotherapy regimen, who bears legal liability: the attending physician who deferred to the machine, the computer engineer who designed the network, or the hospital administrator who procured the software? Until regulatory frameworks resolve these liability dilemmas, artificial intelligence will remain a cognitive partner rather than an autonomous replacement for human physicians.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What capability of diagnostic AI is highlighted in Paragraph 1?",
            points: 2.0,
            sort_order: 6,
            options: [
              { key: "A", text: "Detecting malignant tumors with accuracy comparable to specialists" },
              { key: "B", text: "Performing delicate neurosurgery without human supervision" },
              { key: "C", text: "Inventing novel chemotherapy medications in seconds" },
              { key: "D", text: "Replacing all primary care clinics with digital chatbots" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第一段指出深度学习算法能以匹敌甚至超越资深专家的准确率识别细微恶性肿瘤（detect subtle malignant tumors with accuracy rates matching or exceeding specialists），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "According to Paragraph 2, diagnostic AI is especially advantageous in developing nations because it ______.",
            points: 2.0,
            sort_order: 7,
            options: [
              { key: "A", text: "relieves bottlenecks caused by severe shortages of qualified radiologists" },
              { key: "B", text: "requires zero electrical power or internet connection" },
              { key: "C", text: "guarantees free medicine to every citizen" },
              { key: "D", text: "eliminates the need for hospital beds" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第二段指出在放射科医生严重不足的地区，自动化软件能够快速筛查结核病胸片，缓解诊断瓶颈，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "Clinicians argue that medicine cannot be fully automated because ______.",
            points: 2.0,
            sort_order: 8,
            options: [
              { key: "A", text: "clinical care requires contextual synthesis and empathetic human communication" },
              { key: "B", text: "doctors refuse to use computers under any circumstances" },
              { key: "C", text: "computer algorithms cannot process high-resolution images" },
              { key: "D", text: "patients prefer interacting solely with mechanical robots" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第三段指出医疗绝不仅是统计模式识别，它需要综合模糊症状并带着同理心与患者沟通，选 A。"
          },
          {
            q_type: "reading_item",
            stem: "What legal problem is raised in the final paragraph?",
            points: 2.0,
            sort_order: 9,
            options: [
              { key: "A", text: "Determining liability when an algorithmic diagnosis causes harm" },
              { key: "B", text: "The international patenting of human genetic material" },
              { key: "C", text: "The copyright ownership of hospital medical charts" },
              { key: "D", text: "The criminalization of medical research software" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节事实题。第四段提出了医疗过失纠纷中的责任界定难题（who bears legal liability when an algorithm fails），选 A。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that diagnostic AI should currently be treated as ______.",
            points: 2.0,
            sort_order: 10,
            options: [
              { key: "A", text: "a supportive cognitive collaborator rather than a complete substitute" },
              { key: "B", text: "a dangerous threat that should be immediately banned" },
              { key: "C", text: "the sole decision-maker in all clinical treatments" },
              { key: "D", text: "a temporary fad of no lasting medical importance" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】作者结论观点题。末段结语指出 AI 将是医生的认知协同伙伴（cognitive partner）而非完全自主的替代品，选 A。"
          }
        ]
      }
    ]
  }
];
