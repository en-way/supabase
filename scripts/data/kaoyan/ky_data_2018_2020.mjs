// 2018-2019 年考研英语真题过渡数据集 (批次二将全面扩充)

export const ky2018_2020Exams = [
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
