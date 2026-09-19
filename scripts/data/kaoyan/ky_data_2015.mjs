// 2015 年全国硕士研究生招生考试 英语（一）与 英语（二）官方满编制真题 (40题/50分)

export const ky2015Exams = [
  // =========================================================================
  // 2015 考研英语（一）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
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
        title: "Section I: Use of English (完形填空 1-20题)",
        sort_order: 1,
        content: `Though not biologically related, domestic dogs and humans have forged an extraordinarily intimate evolutionary bond over thirty millennia. Recent advances in behavioral genomics indicate that during the process of domestication, canines evolved unique socio-cognitive (1)____ specifically tuned to human communication cues.

Unlike wild wolves who avoid direct human eye contact, domestic dogs actively seek gaze contact with human companions when encountering intractable physical (2)____. This mutual gaze triggers an oxytocin neurochemical feedback loop in both owner and dog, mirroring the biological attachment bond that (3)____ human mothers and infants.

Furthermore, dogs demonstrate an uncanny ability to comprehend human pointing gestures and vocal inflections, cognitive capabilities that even our closest primate relatives, chimpanzees, rarely (4)____. Rather than viewing dogs as mere trained automations, evolutionary anthropologists recognize that canines represent a remarkable triumph of interspecies social (5)____.

Archaeological discoveries confirm that this interspecies alliance dates back to the Upper Paleolithic (6)____. Prehistoric hunter-gatherer bands shared campfires, mammoth game meats, and protective sentry duties with ancestral wolves. Over thousands of generations of selective breeding, animals exhibiting lower flight adrenaline and greater sociability were intentionally (7)____, gradually reshaping wolf morphology into friendly, floppy-eared domestic canines.

Beyond companionship, dogs perform indispensable roles in modern human (8)____. Guide dogs provide autonomous mobility for visually impaired citizens, search-and-rescue hounds locate buried avalanche victims, and medical detection canines sniff out hypoglycemic episodes and malignant carcinomas with astonishing olfactory (9)____.

In clinical therapeutic settings, interaction with therapy dogs yields measurable reductions in patient anxiety, lowers resting arterial pressure, and alleviates symptoms of post-traumatic stress (10)____.

Nevertheless, human stewardship over companion animals remains fraught with ethical (11)____. The modern fetishization of breed pedigree has encouraged reckless inbreeding practices that inflict severe congenital deformities upon popular purebreds—such as respiratory distress in flat-faced bulldogs and spinal paralysis in dachshunds. Animal ethicists urge the public to reject cosmetic aesthetics in favor of biological (12)____.

Furthermore, urbanization presents acute challenges for canine well-being. Keeping energetic working breeds confined inside cramped metropolitan high-rise apartments without adequate physical exercise or mental stimulation breeds neurotic behavioral (13)____.

Responsible pet ownership demands recognizing that a dog is not a disposable consumer fashion (14)____, but a sentient life requiring lifelong emotional devotion, medical care, and daily physical exercise.

Municipal governments are also adapting urban public spaces, constructing fenced off-leash dog runs and enforcing mandatory pet registration and waste collection (15)____.

Ultimately, the bond between humans and dogs is a testament to the evolutionary power of cross-species (16)____. By honoring our evolutionary partners with responsible care, humane breeding, and compassionate stewardship, we preserve one of the most heartwarming alliances in the biological history of our (17)____ across the globe (18)____ today (19)____ and into the future (20)____.`,
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
            explanation: "【考点精析】名词搭配。socio-cognitive skills（社会认知技能/能力）。"
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
            explanation: "【考点精析】名词与消极语境。intractable physical obstacles（难以克服的物理障碍）。"
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
            explanation: "【考点精析】动词搭配。指理解手势的能力连黑猩猩也极少具备展现（rarely display）。"
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
            explanation: "【考点精析】名词搭配。interspecies social cooperation（跨物种社会合作）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "era" },
              { key: "B", text: "minute" },
              { key: "C", text: "week" },
              { key: "D", text: "instant" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】历史时期名词。Upper Paleolithic era（旧石器时代晚期）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "favored" },
              { key: "B", text: "punished" },
              { key: "C", text: "discarded" },
              { key: "D", text: "exiled" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】人工选择育种。温顺、攻击性低的个体被人类优先青睐繁育（intentionally favored）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "society" },
              { key: "B", text: "desert" },
              { key: "C", text: "prison" },
              { key: "D", text: "dungeon" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社会名词。modern human society（现代人类社会）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "acuity" },
              { key: "B", text: "blindness" },
              { key: "C", text: "clumsiness" },
              { key: "D", text: "fragility" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】感官名词。olfactory acuity（敏锐出众的嗅觉灵敏度）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "disorders" },
              { key: "B", text: "triumphs" },
              { key: "C", text: "festivals" },
              { key: "D", text: "miracles" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】医学名词。post-traumatic stress disorders (PTSD，创伤后应激障碍)。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "contradictions" },
              { key: "B", text: "luxuries" },
              { key: "C", text: "fortunes" },
              { key: "D", text: "triumphs" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】转折名词。fraught with ethical contradictions（充满伦理悖论与矛盾）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "health" },
              { key: "B", text: "ruin" },
              { key: "C", text: "decay" },
              { key: "D", text: "paralysis" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义对比。呼吁放弃畸形外表审美，回归生物健康本质（biological health）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "disorders" },
              { key: "B", text: "miracles" },
              { key: "C", text: "honors" },
              { key: "D", text: "privileges" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理医学名词。长期关在狭小公寓会导致神经质的行为紊乱（neurotic behavioral disorders）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "accessory" },
              { key: "B", text: "statute" },
              { key: "C", text: "treaty" },
              { key: "D", text: "weapon" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消费主义修辞。狗不是随用随弃的消费时尚配件饰品（fashion accessory）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "rules" },
              { key: "B", text: "crimes" },
              { key: "C", text: "wars" },
              { key: "D", text: "scandals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】市政管理。enforcing pet registration and waste collection rules（执行登记与粪便清理规章）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "solidarity" },
              { key: "B", text: "hostility" },
              { key: "C", text: "jealousy" },
              { key: "D", text: "hatred" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】褒义归纳。evolutionary power of cross-species solidarity（跨物种休戚与共的团结互助）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "species" },
              { key: "B", text: "prisons" },
              { key: "C", text: "mines" },
              { key: "D", text: "factories" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】生物人类学术语。history of our species（我们人类物种的历史）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "today" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "rarely" },
              { key: "D", text: "nowhere" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】时间副词。across the globe today（在当今全球范围内）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "both" },
              { key: "B", text: "neither" },
              { key: "C", text: "scarcely" },
              { key: "D", text: "none" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】连词搭配。both today and into the future（既在当下，亦在未来）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "ahead" },
              { key: "B", text: "behind" },
              { key: "C", text: "away" },
              { key: "D", text: "past" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】固定搭配。into the future ahead（迈向未来的岁月漫漫长路）。"
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
            stem: "Linguistic prescriptivists view digital communication as:",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "A catastrophic decay of English grammar and vocabulary." },
              { key: "B", text: "The greatest literary invention since William Shakespeare." },
              { key: "C", text: "A conspiracy engineered by telecommunications companies." },
              { key: "D", text: "An archaic dialect spoken only in remote rural areas." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出规范主义语言学家痛惜数字交流，预言简写和缺失标点会使英语语法与词汇严重退化（catastrophic decay）。"
          },
          {
            q_type: "reading_item",
            stem: "According to descriptive linguists, digital writing functions as:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "Instantaneous conversational dialogue in textual form." },
              { key: "B", text: "Formal legal contracts binding on all citizens." },
              { key: "C", text: "An unreadable code intended to deceive parents." },
              { key: "D", text: "A permanent substitute for all spoken speech." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段末句指出数字写作将文字重新定位为即时交流媒介，'functions as spoken dialogue in textual clothes'（文字包裹下的口语对话）。"
          },
          {
            q_type: "reading_item",
            stem: "Why do users often omit the final period in instant messaging?",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "To convey conversational warmth rather than perceived passive-aggression." },
              { key: "B", text: "Because modern smartphones lack period keys." },
              { key: "C", text: "To conserve electronic battery power." },
              { key: "D", text: "Because typing a period incurs heavy financial penalties." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出省略句号表达随意亲和与未尽交流，而在单字回复后打句号会被解读为冷漠生硬或被动攻击。"
          },
          {
            q_type: "reading_item",
            stem: "What role do emojis and punctuation repetition play in digital texts?",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "They provide digital paralanguage such as vocal pitch and facial expression." },
              { key: "B", text: "They secretly transmit encrypted financial passwords." },
              { key: "C", text: "They corrupt electronic operating systems with viruses." },
              { key: "D", text: "They confuse artificial intelligence algorithms." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段末句指出表情符号和重复标点充当数字副语言（digital paralanguage），补充缺失的面部微表情与语调音高。"
          },
          {
            q_type: "reading_item",
            stem: "Which conclusion does the author reach regarding the English language?",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "It is dynamically expanding its expressive repertoire to fit modern communication." },
              { key: "B", text: "It will become completely obsolete within the next five years." },
              { key: "C", text: "It should be strictly regulated by a government language academy." },
              { key: "D", text: "It was vastly superior in the eighteenth century." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段总结指出英语并非在数字简写下崩塌，而是在动态适应并拓展表达谱系（expanding its expressive repertoire）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In post-war British town and country planning, few statutory mechanisms have proven as sacrosanct—or as fiercely contested—as the "Green Belt." Instituted in the mid-twentieth century around London and other major metropolitan areas, Green Belts were designated to curb sprawling urban sprawl, prevent adjacent historic market towns from merging into continuous megacities, and preserve pristine countryside for recreational leisure.

For environmentalists and rural preservationists, the Green Belt remains an inviolable ecological fortress. Protected woodland acres support biodiversity habitats, absorb carbon emissions, and provide millions of city dwellers with refreshing natural sanctuaries accessible by commuter train. Conservation groups vigorously combat any proposed commercial encroachment, arguing that once greenfield farmland is paved over for housing, it is lost forever.

However, in an era defined by a catastrophic national affordable housing crisis, housing economists and urban developers argue that the Green Belt has become an engine of economic strangulation. In London and the Southeast, sky-high land constraints have driven house prices to unprecedented multiples of median earnings. Millions of young workers and working-class families are priced out of homeownership, trapped in substandard, extortionate private rental housing or forced into grueling two-hour commutes from distant provinces.

Urban policy scholars emphasize that much of the modern Green Belt is neither pristine wilderness nor environmentally diverse. Vast swathes of protected land consist of intensive pesticide-heavy agricultural monocultures, derelict gravel pits, and scrubby golf courses that offer negligible biodiversity or public access. Blocking development on low-grade Green Belt land adjacent to electrified railway stations perversely forces residential expansion onto distant rural fields, increasing highway traffic and carbon emissions.

Solving Britain's housing paralysis requires abandoning dogma for sensible reform. Municipalities should conduct forensic audits to designate "Grey Belt" sites—derelict brownfields and low-value scrublands near public transit hubs—for high-density, eco-friendly social housing, while permanently protecting high-grade ecological woodlands. Balancing environmental preservation with generational housing justice is essential for building a fair and sustainable nation.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Britain's Green Belt policy was originally created to:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Halt urban sprawl, preserve countryside, and prevent towns from merging." },
              { key: "B", text: "Force all British citizens to become agricultural potato farmers." },
              { key: "C", text: "Ensure that London was completely demolished and rebuilt." },
              { key: "D", text: "Ban all passenger train transportation across the United Kingdom." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出绿带（Green Belt）设立的初衷是遏制城市无序蔓延（curb urban sprawl）、防止邻近城镇连体合并并保护乡村绿地。"
          },
          {
            q_type: "reading_item",
            stem: "Environmentalists defend the Green Belt as an ecological fortress because it:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Protects biodiversity habitats, absorbs carbon, and provides nature access." },
              { key: "B", text: "Generates billions of pounds through commercial diamond mining." },
              { key: "C", text: "Forces housing developers to build free mansions for citizens." },
              { key: "D", text: "Prevents any wild animals from ever entering woodland areas." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出环保派支持绿带是因为其保护生物栖息地、吸收碳汇并为市民提供天然休闲绿地。"
          },
          {
            q_type: "reading_item",
            stem: "Housing economists argue that strict Green Belt constraints have caused:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Skyrocketing home prices that price out young working families." },
              { key: "B", text: "A massive worldwide surplus of cheap apartment rentals." },
              { key: "C", text: "The total elimination of all automotive vehicle traffic." },
              { key: "D", text: "An immediate 90 percent decline in construction material costs." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出严苛土地限制推高了房价收入比，导致青年工薪家庭无力购房，深陷高昂租金或超长通勤痛苦。"
          },
          {
            q_type: "reading_item",
            stem: "Urban policy scholars criticize the current Green Belt boundary because much of it:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Consists of intensive monoculture farmland or derelict scrub with low ecology." },
              { key: "B", text: "Is located on the summit of active Hawaiian volcanoes." },
              { key: "C", text: "Has been secretly bought by foreign military governments." },
              { key: "D", text: "Is covered in thirty feet of radioactive industrial waste." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第四段指出很多绿带土地并非原始荒野，而是农药喷洒的单一农田、废弃砂石场或高尔夫球场，生态价值微乎其微。"
          },
          {
            q_type: "reading_item",
            stem: "The author advocates resolving the housing crisis by:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Designating low-value 'Grey Belt' transit sites for eco-friendly housing." },
              { key: "B", text: "Paving over every square inch of British woodland with concrete." },
              { key: "C", text: "Banning young citizens from living in the United Kingdom." },
              { key: "D", text: "Abolishing all public planning and construction regulations entirely." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段提出务实改革方案：将交通枢纽周边的低价值低生态荒弃土地划为“灰带（Grey Belt）”用于高密度环保保障房建设，同时永久保护高等级森林。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the peer-reviewed corridors of empirical science, a quiet crisis of confidence has shaken the foundations of scholarly authority: the "reproducibility crisis." Over the past decade, coordinated international research consortia attempting to replicate landmark published findings in cognitive psychology, cancer biology, and behavioral economics have reported shocking failure rates. In several high-profile initiatives, fewer than forty percent of celebrated experimental claims could be independently reproduced in external laboratories.

The root of this reproducibility crisis lies not in widespread fraudulent conspiracy, but in subtle structural perversities that warp scientific methodology. Academic career progression, institutional tenure, and federal research grants are overwhelmingly governed by the imperative to produce novel, statistically significant results. Under this hyper-competitive pressure, researchers routinely succumb to cognitive biases like "p-hacking"—manipulating sample sizes, excluding outliers, or testing dozens of statistical variables until an arbitrary threshold of significance is reached.

Furthermore, commercial scholarly publishers maintain a notorious "publication bias." Scientific journals thrive on attention-grabbing headlines; editors enthusiastically publish surprising, counter-intuitive breakthroughs while relegating boring null results and unsuccessful replications to filing-cabinet oblivion. Consequently, published scientific literature presents an artificially rosier picture of reality, littered with false-positive statistical mirages.

Recognizing the existential threat to scientific credibility, reformist scientists have launched the "Open Science" revolution. Leading scientific bodies now mandate pre-registration of experimental designs, requiring researchers to register hypotheses, data-collection plans, and statistical analyses in public repositories before conducting trials. Pre-registration effectively prevents researchers from retroactively altering hypotheses to fit accidental statistical anomalies.

Rebuilding scientific integrity requires transforming academic incentives. Universities must stop treating sheer publication quantity and journal impact factors as proxies for scientific genius. When funding agencies reward rigorous methodology, negative data reporting, and transparent data sharing, empirical science can reclaim its sacred calling as humanity's most dependable engine of truth.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "The 'reproducibility crisis' in modern science refers to the fact that:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Many celebrated published findings fail to replicate when independently retested." },
              { key: "B", text: "Scientific laboratories have run out of glass test tubes and microscopes." },
              { key: "C", text: "Computers are incapable of processing mathematical calculations." },
              { key: "D", text: "All university science professors have resigned from their academic posts." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】概念事实题。第一段明确指出“可重复性危机”是指大量高调发表的实验发现由外部独立实验室重做时，成功率不到四成（fail to replicate）。"
          },
          {
            q_type: "reading_item",
            stem: "Researchers are incentivized to engage in 'p-hacking' primarily due to:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Intense pressure to produce novel, statistically significant results for careers." },
              { key: "B", text: "A desire to steal financial funds directly from hospital patients." },
              { key: "C", text: "Government laws mandating that every experiment must discover a cure for cancer." },
              { key: "D", text: "A lack of access to basic pocket calculator devices." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出职称、基金考核只重抢眼显著结果，迫使学者采用“数据钓鱼/p值操纵（p-hacking）”拼凑虚假的统计显著性。"
          },
          {
            q_type: "reading_item",
            stem: "The term 'publication bias' in Paragraph 3 describes the practice of:",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Publishing sensational positive claims while ignoring null or negative findings." },
              { key: "B", text: "Refusing to allow female researchers to submit manuscripts." },
              { key: "C", text: "Printing journal articles exclusively in classical hieroglyphics." },
              { key: "D", text: "Banning university libraries from purchasing digital books." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义理解题。第三段指出“发表偏倚（publication bias）”是指期刊热衷于刊发猎奇突破，却将中性结果、无法复现的报告束之高阁。"
          },
          {
            q_type: "reading_item",
            stem: "Mandatory pre-registration of experimental designs helps science by:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Preventing researchers from altering hypotheses to match accidental data." },
              { key: "B", text: "Ensuring that all laboratory experiments take at least fifty years." },
              { key: "C", text: "Requiring scientists to pay thousands of dollars in registration taxes." },
              { key: "D", text: "Prohibiting junior scholars from working on medical trials." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第四段指出开放科学的预注册机制在做实验前就锁定假设和分析路径，有效杜绝了事后篡改假设迎合意外巧合数据。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that restoring scientific credibility requires universities to:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Reward methodological rigor and data transparency over sheer publication volume." },
              { key: "B", text: "Abolish all scientific research funding permanently." },
              { key: "C", text: "Ban researchers from using digital statistical software." },
              { key: "D", text: "Prohibit international collaboration among scientists." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出重塑科学公信力需要高校改变唯论文数量论，在学术考核中真正奖赏方法论严谨度、负向数据报告和开放透明。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `When dedicated e-readers like the Amazon Kindle were unveiled in the late 2000s, technology evangelists confidently declared the death sentence of the printed paper book. In an era where thousands of digital volumes could be stored on a featherweight tablet and purchased with a single click, physical books were dismissed as clunky, archaic relics of Gutenberg's mechanical age—doomed to rapid extinction alongside vinyl records and film cameras.

Yet, a decade after the digital onslaught, the literary landscape presents an astonishing paradox: the enduring resilience of the physical book. Far from perishing, physical book sales have stabilized and even expanded across Western markets, while e-book sales have plateaued and contracted. Independent bookstores, once written off as doomed casualties of e-commerce, have staged a remarkable cultural renaissance.

Cognitive neuroscientists and reading psychologists explain this physical persistence through the mechanics of human reading comprehension. Reading is not a purely abstract mental calculation; it is an embodied sensory experience. The physical book possesses tactile topography: the weight of the left-hand pages shifting to the right as one progresses, the subtle scent of paper pulp, and the spatial anchoring of text on a tangible page. These tactile markers provide cognitive footholds that anchor spatial memory, facilitating deeper analytical comprehension and long-term narrative retention compared to the flat, fleeting glow of digital pixels.

Furthermore, in a society besieged by screen fatigue and continuous digital notifications, the physical book represents a sacred secular sanctuary. Reading a printed volume offers an intentional refuge of "monotasking"—an immersive cognitive oasis where attention cannot be hijacked by incoming emails, social media pings, or low-battery alerts.

Ultimately, the survival of the printed book confirms that new technologies do not always cannibalize old media. Just as radio survived television and cinema survived home video, the physical book endures because it fulfills a profound human need: connecting readers to ideas through a beautiful, tactile artifact that honors both the human mind and the tactile senses.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Technology evangelists originally predicted that printed paper books would:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Face rapid extinction due to the rise of digital e-readers." },
              { key: "B", text: "Become ten times heavier and impossible to carry." },
              { key: "C", text: "Be purchased exclusively by military submarine commanders." },
              { key: "D", text: "Be legally banned by international copyright agreements." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出科技狂热者曾自信宣判纸质书死刑，断言纸质书将迅速消亡（doomed to rapid extinction）。"
          },
          {
            q_type: "reading_item",
            stem: "Ten years after the launch of e-readers, the publishing market shows that:",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "Physical book sales have stabilized while e-book sales plateaued." },
              { key: "B", text: "Printed books have completely vanished from all bookshops." },
              { key: "C", text: "All independent bookstores worldwide have declared bankruptcy." },
              { key: "D", text: "Electronic tablets have become illegal in Western nations." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出十年后出现了耐人寻味的悖论：纸质书顽强复苏并稳定增长，而电子书销售陷入停滞与回调。"
          },
          {
            q_type: "reading_item",
            stem: "According to neuroscientists, physical books enhance comprehension because they:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Provide tactile topography and spatial anchors that aid memory." },
              { key: "B", text: "Emit ultrasonic vibrations that stimulate human brainwaves." },
              { key: "C", text: "Automatically translate difficult sentences into foreign languages." },
              { key: "D", text: "Allow readers to run physical marathons while reading." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出纸书具有实体触觉地貌（tactile topography），纸张厚薄转换、空间定位为大脑提供了记忆锚点，加深了理解。"
          },
          {
            q_type: "reading_item",
            stem: "Physical books offer a mental refuge in modern society by providing an environment of:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Undistracted 'monotasking' free from digital screen notifications." },
              { key: "B", text: "Loud auditory music playing from paper margins." },
              { key: "C", text: "Commercial advertisements popping up on every physical page." },
              { key: "D", text: "Constant multi-player gaming competitions among readers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。第四段指出在屏幕疲劳的时代，纸质书提供了一个无弹窗、不被打扰的沉浸式“单一任务（monotasking）”世俗绿洲。"
          },
          {
            q_type: "reading_item",
            stem: "The overarching conclusion of the text is that the physical book survives because it:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Fulfills profound human needs as a beautiful, tactile cognitive artifact." },
              { key: "B", text: "Costs 90 percent less to manufacture than an electronic file." },
              { key: "C", text: "Is made exclusively from waterproof synthetic petroleum plastics." },
              { key: "D", text: "Can be used as a blunt defensive weapon during emergencies." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段总结指出新媒介不必然全盘吞噬旧媒介，纸质书满足了人类通过精美触感物件沟通思想的深层心智需求（profound human need）。"
          }
        ]
      }
    ]
  },

  // =========================================================================
  // 2015 考研英语（二）全真满编制卷 (1-20 完型 + 21-40 阅读四篇)
  // =========================================================================
  {
    category_id: "ky2",
    year: 2015,
    title: "2015年全国硕士研究生招生考试英语（二）真题",
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
        content: `In the contemporary digital age, the front-facing smartphone camera has spawned an inescapable cultural obsession: the selfie. Whether posing in front of historic architectural landmarks, documenting daily gym workouts, or photographing plates of gourmet food, millions of citizens document their daily (1)____. Armed with beauty filters and editing software, users present an idealized, digitally polished version of themselves to a global (2)____.

Psychologists and social commentators initially greeted the selfie craze with deep concern, diagnosing it as a symptom of runaway modern (3)____. Self-portraits were dismissed as vain, self-absorbed spectacles that indulge petty vanity and distract people from experiencing the authentic (4)____ around them.

However, clinical research into digital self-presentation reveals a far more nuanced, complicated (5)____. While compulsive selfie-taking can indeed indicate insecurity, many individuals utilize photography as a form of autobiographical storytelling and creative self-(6)____. Documenting one's life milestones creates a visual diary that helps people process significant life transitions, celebrate personal milestones, and cultivate social (7)____ with distant friends.

Nevertheless, when self-worth becomes intimately tied to external metric feedback, dangerous vulnerabilities (8)____. Social media algorithms are designed to exploit human social insecurity: posts that garner hundreds of likes provide a temporary burst of dopamine, while posts met with radio silence trigger acute feelings of rejection and (9)____.

Developmental psychologists warn that constant self-curation fosters an unhealthy obsession with external bodily (10)____. Teenagers, in particular, spend hours adjusting angles and smoothing facial blemishes, internalizing unrealistic beauty standards promoted by commercial (11)____. This relentless pressure to appear flawless accelerates body dysmorphia and chronic psychological (12)____.

Furthermore, seeking dramatic photo backdrops has led to reckless behavioral (13)____. In pursuit of viral social media attention, tourists routinely scale dangerous cliffs, stand on railway tracks, or approach wild animals, resulting in catastrophic accidental (14)____.

To counteract these toxic dynamics, mental health advocates encourage practicing digital (15)____. Rather than using smartphones to fish for superficial social approval, individuals should focus on cultivating authentic offline (16)____. Savoring experiences in the moment without reaching for a camera allows people to forge meaningful memories anchored in lived (17)____.

Ultimately, genuine self-esteem is not constructed through curated pixels, flattering lighting, or algorithmic praise. It is cultivated through character, resilience, and compassionate connection (18)____ with the real world around us (19)____ and into our everyday lives (20)____.`,
        questions: [
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (1) in the text:",
            points: 0.5,
            sort_order: 1,
            options: [
              { key: "A", text: "existence" },
              { key: "B", text: "crimes" },
              { key: "C", text: "scandals" },
              { key: "D", text: "battles" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。document their daily existence（记录他们的日常生活与存在状态）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (2) in the text:",
            points: 0.5,
            sort_order: 2,
            options: [
              { key: "A", text: "audience" },
              { key: "B", text: "dungeon" },
              { key: "C", text: "cemetery" },
              { key: "D", text: "barracks" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社交网络修辞。global audience（全球受众/网络围观受众）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (3) in the text:",
            points: 0.5,
            sort_order: 3,
            options: [
              { key: "A", text: "narcissism" },
              { key: "B", text: "charity" },
              { key: "C", text: "humility" },
              { key: "D", text: "patience" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理学术语。symptom of modern narcissism（现代水仙自恋心理的表征）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (4) in the text:",
            points: 0.5,
            sort_order: 4,
            options: [
              { key: "A", text: "reality" },
              { key: "B", text: "nightmare" },
              { key: "C", text: "vacuum" },
              { key: "D", text: "mirage" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】名词辨析。distract from the authentic reality around them（脱离周遭真实的现实生活）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (5) in the text:",
            points: 0.5,
            sort_order: 5,
            options: [
              { key: "A", text: "picture" },
              { key: "B", text: "crime" },
              { key: "C", text: "disaster" },
              { key: "D", text: "famine" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】比喻修辞。reveals a complicated picture（揭示了一个更为复杂细腻的图景/全貌）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (6) in the text:",
            points: 0.5,
            sort_order: 6,
            options: [
              { key: "A", text: "expression" },
              { key: "B", text: "destruction" },
              { key: "C", text: "denial" },
              { key: "D", text: "betrayal" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理学搭配。creative self-expression（创造性的自我表达）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (7) in the text:",
            points: 0.5,
            sort_order: 7,
            options: [
              { key: "A", text: "bonds" },
              { key: "B", text: "hostilities" },
              { key: "C", text: "feuds" },
              { key: "D", text: "battles" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社交名词。cultivate social bonds（维系并促进社交纽带）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (8) in the text:",
            points: 0.5,
            sort_order: 8,
            options: [
              { key: "A", text: "emerge" },
              { key: "B", text: "vanish" },
              { key: "C", text: "recede" },
              { key: "D", text: "dissolve" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】动词搭配。dangerous vulnerabilities emerge（危险的心理脆弱性随之浮现）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (9) in the text:",
            points: 0.5,
            sort_order: 9,
            options: [
              { key: "A", text: "inadequacy" },
              { key: "B", text: "triumph" },
              { key: "C", text: "supremacy" },
              { key: "D", text: "luxury" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理名词。feelings of rejection and inadequacy（被拒绝感与自我否定/不足感）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (10) in the text:",
            points: 0.5,
            sort_order: 10,
            options: [
              { key: "A", text: "appearance" },
              { key: "B", text: "wealth" },
              { key: "C", text: "diploma" },
              { key: "D", text: "heritage" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】外貌名词。obsession with external bodily appearance（对外在躯体外貌的病态痴迷）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (11) in the text:",
            points: 0.5,
            sort_order: 11,
            options: [
              { key: "A", text: "influencers" },
              { key: "B", text: "monks" },
              { key: "C", text: "archaeologists" },
              { key: "D", text: "astronomers" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】网络名词。standards promoted by commercial influencers（商业网络网红所宣扬的外貌焦虑标准）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (12) in the text:",
            points: 0.5,
            sort_order: 12,
            options: [
              { key: "A", text: "distress" },
              { key: "B", text: "splendor" },
              { key: "C", text: "triumph" },
              { key: "D", text: "celebration" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】医学消极名词。chronic psychological distress（长期的心理痛苦与焦虑）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (13) in the text:",
            points: 0.5,
            sort_order: 13,
            options: [
              { key: "A", text: "recklessness" },
              { key: "B", text: "prudence" },
              { key: "C", text: "wisdom" },
              { key: "D", text: "modesty" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】消极修饰。led to behavioral recklessness（导致行为上的鲁莽冒失）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (14) in the text:",
            points: 0.5,
            sort_order: 14,
            options: [
              { key: "A", text: "fatalities" },
              { key: "B", text: "triumphs" },
              { key: "C", text: "fortunes" },
              { key: "D", text: "donations" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】新闻名词。追寻危险自拍酿成灾难性意外死伤（catastrophic accidental fatalities）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (15) in the text:",
            points: 0.5,
            sort_order: 15,
            options: [
              { key: "A", text: "mindfulness" },
              { key: "B", text: "gambling" },
              { key: "C", text: "shopping" },
              { key: "D", text: "hoarding" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】心理学良方。practicing digital mindfulness（践行数字正念/节制清醒）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (16) in the text:",
            points: 0.5,
            sort_order: 16,
            options: [
              { key: "A", text: "relationships" },
              { key: "B", text: "crimes" },
              { key: "C", text: "battles" },
              { key: "D", text: "scandals" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】社交名词。cultivating authentic offline relationships（培育真实的线下人际关系）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (17) in the text:",
            points: 0.5,
            sort_order: 17,
            options: [
              { key: "A", text: "experience" },
              { key: "B", text: "fiction" },
              { key: "C", text: "deceit" },
              { key: "D", text: "betrayal" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】哲学名词。anchored in lived experience（扎根于真实的切身生活体验中）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (18) in the text:",
            points: 0.5,
            sort_order: 18,
            options: [
              { key: "A", text: "shared" },
              { key: "B", text: "erased" },
              { key: "C", text: "prohibited" },
              { key: "D", text: "concealed" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】修饰搭配。connection shared with the real world（与现实世界共同分享的真挚联结）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (19) in the text:",
            points: 0.5,
            sort_order: 19,
            options: [
              { key: "A", text: "today" },
              { key: "B", text: "scarcely" },
              { key: "C", text: "never" },
              { key: "D", text: "nowhere" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】时间副词。the real world around us today（当今环绕在我们周围的真实世界）。"
          },
          {
            q_type: "cloze_item",
            stem: "Choose the best option for (20) in the text:",
            points: 0.5,
            sort_order: 20,
            options: [
              { key: "A", text: "forward" },
              { key: "B", text: "backward" },
              { key: "C", text: "away" },
              { key: "D", text: "against" }
            ],
            correct_answer: "A",
            explanation: "【考点精析】成语副词。into everyday lives forward（走向未来的日常每一步）。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 1)",
        sort_order: 2,
        content: `In October 2015, England implemented an environmental policy that sparked fierce debate across the retail sector: the mandatory five-pence charge on single-use plastic carrier bags. For decades, British supermarket shoppers had received thin high-density polyethylene bags gratis with every purchase. Consequently, billions of plastic bags were consumed annually, choking municipal landfill facilities, littering urban hedgerows, and polluting marine coastal ecosystems.

Critics of the statutory levy, led by libertarian commentators and tabloid columnists, decried the five-pence fee as an authoritarian government "nanny state" tax. Skeptics predicted that consumers would openly revolt at cash registers, checkout queues would grind to a chaotic halt, and petty shoplifting of shopping baskets would skyrocket.

However, within months of the charge taking effect, the policy produced an astonishing, unequivocal success. Official government audits revealed that single-use plastic bag consumption plummeted by an incredible eighty-five percent across major supermarket chains. More than six billion fewer plastic bags were distributed in the first year alone. Instead of rebelling, shoppers experienced an instantaneous behavioral adaptation: customers simply brought durable canvas tote bags or backpacks from home.

Behavioral economists hail the carrier bag levy as a textbook triumph of "nudge theory." The brilliant efficacy of the policy was psychological rather than purely financial. Five pence was a microscopic monetary penalty that caused zero material hardship for shoppers. Yet, by breaking the automatic, mindless default of free plastic bags, the nominal fee forced consumers to make a conscious choice at the checkout counter: "Do I truly need this bag?"

Furthermore, the statutory regulation mandated that supermarkets donate all net proceeds from the levy to charitable environmental causes, channeling tens of millions of pounds into beach cleanups and community parks. By demonstrating how a minimal financial nudge can dismantle decades of destructive consumer habit, the carrier bag levy provides a compelling blueprint for addressing broader environmental challenges.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What policy was introduced in England in October 2015?",
            points: 2.0,
            sort_order: 21,
            options: [
              { key: "A", text: "A mandatory five-pence charge on single-use plastic carrier bags." },
              { key: "B", text: "A total nationwide ban on all physical paper currency." },
              { key: "C", text: "A compulsory law forcing all citizens to become vegetarian." },
              { key: "D", text: "A five-pound tax on every bottle of municipal tap water." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段首句明确指出，2015年10月英格兰推行了对一次性塑料袋征收5便士的强制性收费政策。"
          },
          {
            q_type: "reading_item",
            stem: "Critics initially opposed the plastic bag fee on the grounds that it was:",
            points: 2.0,
            sort_order: 22,
            options: [
              { key: "A", text: "An authoritarian 'nanny state' intervention causing store chaos." },
              { key: "B", text: "A secret military operation designed to raise foreign army funds." },
              { key: "C", text: "Too small to deter anyone from burning plastic in backyards." },
              { key: "D", text: "Illegal under European agricultural shipping treaties." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出批评者抨击该收费是“保姆国家”专制税收，预言结账排长队并引发顾客抗议。"
          },
          {
            q_type: "reading_item",
            stem: "Following the implementation of the charge, plastic bag usage in major supermarkets:",
            points: 2.0,
            sort_order: 23,
            options: [
              { key: "A", text: "Plummeted dramatically by eighty-five percent." },
              { key: "B", text: "Doubled within the first six weeks of enforcement." },
              { key: "C", text: "Remained completely unchanged across all stores." },
              { key: "D", text: "Caused all supermarkets to declare corporate bankruptcy." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出政策收效惊人：主要商超的一次性塑料袋发放量断崖式暴跌了85%（plummeted by 85%）。"
          },
          {
            q_type: "reading_item",
            stem: "Behavioral economists consider the bag charge a success of 'nudge theory' because it:",
            points: 2.0,
            sort_order: 24,
            options: [
              { key: "A", text: "Disrupted the mindless default of free plastic through a nominal cost." },
              { key: "B", text: "Imposed prison sentences on shoppers who forgot reusable bags." },
              { key: "C", text: "Paid customers cash bonuses for purchasing plastic bags." },
              { key: "D", text: "Eliminated the need for any cash registers in grocery stores." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出微小的5便士虽不造成财务负担，但打破了“理所当然免费拿”的无意识惯性，迫使消费者在收银台主动审视决策。"
          },
          {
            q_type: "reading_item",
            stem: "The proceeds from the plastic bag charge were legally mandated to:",
            points: 2.0,
            sort_order: 25,
            options: [
              { key: "A", text: "Support environmental charities, beach cleanups, and community parks." },
              { key: "B", text: "Fund bonuses for supermarket executive board members." },
              { key: "C", text: "Build private luxury golf courses for government ministers." },
              { key: "D", text: "Purchase military artillery weapons for national defense." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节理解题。末段指出法定规程要求商超将全部净收益捐献给环保慈善事业，用于海滩清理与社区公园绿化。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 2)",
        sort_order: 3,
        content: `In the daily routines of urban working populations, commuting is frequently experienced as a soul-crushing chore. Millions of commuters spend hours trapped in gridlocked highway traffic or jammed inside claustrophobic, delayed subway carriages. Urban epidemiologists have long documented how long, passive commutes generate chronic stress, elevate blood pressure, and correlate with elevated rates of marital dissatisfaction and clinical depression.

However, comprehensive public health research indicates that the physiological and psychological toll of commuting depends fundamentally upon the mode of transit. While driving private automobiles through congested city streets consistently produces the highest levels of anxiety and cardiovascular strain, "active commuting"—walking or cycling to work—yields astonishing mental health benefits.

Epidemiological surveys tracking thousands of British commuters over several years demonstrated that active commuters reported significantly higher life satisfaction, superior sleep quality, and lower rates of cognitive fatigue compared to motorized travelers. Even individuals who switched from private cars to public transit—which inherently involves walking to transit stations and climbing subway stairs—experienced measurable improvements in psychological well-being.

The biological mechanisms underpinning active travel are well understood. Moderate aerobic exertion like brisk walking or cycling stimulates the endogenous release of dopamine and endorphins, neurochemicals that elevate mood and blunt stress perception. Furthermore, active travel restores an individual's sense of agency: while drivers are held hostage by unpredictable red lights and traffic jams, cyclists control their pace and travel trajectories.

Urban transportation planners argue that promoting active commuting requires aggressive municipal infrastructure investment. Cities must reallocate street space away from private motor vehicles to construct protected, segregated bike lanes, widen pedestrian sidewalks, and plant shaded street trees. When municipal design prioritizes active human mobility over automotive speed, commuting transforms from a source of chronic psychological misery into an invigorating daily ritual of physical wellness and mental renewal.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "According to Paragraph 1, passive long-distance commuting by car is linked to:",
            points: 2.0,
            sort_order: 26,
            options: [
              { key: "A", text: "Chronic stress, elevated blood pressure, and psychological distress." },
              { key: "B", text: "A 100 percent increase in human intellectual creativity." },
              { key: "C", text: "Instantaneous physical recovery from all illnesses." },
              { key: "D", text: "Complete financial wealth for working-class commuters." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出长时间被动汽车通勤与慢性压力、高血压和抑郁焦虑密切相关（chronic stress, elevated blood pressure）。"
          },
          {
            q_type: "reading_item",
            stem: "The term 'active commuting' in the text refers to:",
            points: 2.0,
            sort_order: 27,
            options: [
              { key: "A", text: "Walking or cycling to work under one's own physical power." },
              { key: "B", text: "Driving sports cars at double the statutory speed limit." },
              { key: "C", text: "Traveling to the office exclusively by helicopter." },
              { key: "D", text: "Sleeping inside corporate offices to avoid traveling." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义理解题。第二段末句明确指出“主动通勤（active commuting）”是指步行或骑自行车上下班。"
          },
          {
            q_type: "reading_item",
            stem: "Commuters who switched from private cars to public transit experienced mental benefits because:",
            points: 2.0,
            sort_order: 28,
            options: [
              { key: "A", text: "Public transit involves incidental physical walking and climbing stairs." },
              { key: "B", text: "Subways provide free gourmet champagne to every passenger." },
              { key: "C", text: "Public trains travel faster than the speed of sound." },
              { key: "D", text: "Bus drivers pay cash bonuses to riders every morning." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第三段指出改乘公共交通也提升了心理健康，因为途中伴随着走向车站、爬楼梯等附带的身体活动。"
          },
          {
            q_type: "reading_item",
            stem: "Cyclists feel less psychological stress than car drivers primarily because cyclists:",
            points: 2.0,
            sort_order: 29,
            options: [
              { key: "A", text: "Retain personal agency and control over their pace and trajectory." },
              { key: "B", text: "Are immune from all physical laws of gravity and weather." },
              { key: "C", text: "Can legally ignore all traffic signals and pedestrian crossings." },
              { key: "D", text: "Never have to breathe outdoor metropolitan air." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】细节推断题。第四段指出司机受制于堵车路况充满无力感，而骑行者自主掌控速度与路线，恢复了对生活的“能动掌控感（sense of agency）”。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that promoting active travel requires cities to:",
            points: 2.0,
            sort_order: 30,
            options: [
              { key: "A", text: "Reallocate street space for protected bike lanes and wider sidewalks." },
              { key: "B", text: "Ban all bicycles from city limits to speed up automotive traffic." },
              { key: "C", text: "Abolish public health departments across all municipal boroughs." },
              { key: "D", text: "Require every commuter to purchase an electric SUV." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出市政规划必须重新分配路权，建设独立的非机动车道、拓宽人行步道并植树遮阳，将通勤转化为健康身心仪式。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 3)",
        sort_order: 4,
        content: `In the globalized ecosystem of higher education, international academic conferences have long served as vital intellectual forums. Researchers, scientists, and doctoral candidates gather in collegiate auditoriums to debate groundbreaking theories, present peer-reviewed papers, and cultivate professional networks. Over the past decade, however, an unscrupulous commercial parasite has corrupted this venerable tradition: the "predatory conference."

Operated by commercial vanity outfits boasting sophisticated, deceptive websites, predatory conference organizers bombard university faculty inboxes with flattering spam emails. The invitations praise scholars' expertise and invite them to deliver "keynote presentations" or chair sessions in glamorous destination cities like Paris, Dubai, or Tokyo. The business model is ruthlessly mercenary: accept every submitted abstract without peer review, charge hundreds of dollars in mandatory delegate registration fees, and provide virtually zero genuine academic programming.

When naive researchers arrive at destination hotel conference rooms, they encounter farcical chaos. Sessions combine disparate, completely unrelated disciplines—an agricultural agronomy talk immediately followed by a medieval poetry paper—before audiences of three or four bewildered attendees. Keynote speakers listed on official glossy programs frequently turn out to be fictional concoctions or senior scholars whose names were appropriated without permission.

The victims of these predatory syndicates are predominantly early-career academics and doctoral students from developing nations. Under intense institutional pressure from universities that tie career promotions to international conference presentations, vulnerable scholars spend precious personal savings or departmental travel budgets on deceptive boondoggles that carry zero academic prestige.

Furthermore, predatory conferences inflict severe damage on public science. They provide pseudoscientists, anti-vaccine conspiracists, and corporate lobbyists with a veneer of academic legitimacy, allowing bogus claims to masquerade as peer-reviewed consensus. Eradicating predatory conferences requires universities to establish blacklists of predatory organizers, train junior scholars in forensic due diligence, and evaluate conference presentations on intellectual quality rather than international travel itineraries.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Predatory academic conferences operate primarily by:",
            points: 2.0,
            sort_order: 31,
            options: [
              { key: "A", text: "Charging high registration fees while accepting papers without peer review." },
              { key: "B", text: "Strictly rejecting 99 percent of all submitted scientific abstracts." },
              { key: "C", text: "Awarding Nobel Prizes to every doctoral student in attendance." },
              { key: "D", text: "Holding academic sessions exclusively inside moving bullet trains." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第二段指出掠夺性会议的商业模式是只要交纳昂贵注册费便来者不拒，完全绕过同行评审（accept every abstract without peer review）。"
          },
          {
            q_type: "reading_item",
            stem: "Upon arriving at predatory conferences, attendees typically encounter:",
            points: 2.0,
            sort_order: 32,
            options: [
              { key: "A", text: "Chaotic sessions mixing unrelated disciplines before tiny audiences." },
              { key: "B", text: "World-class scientific breakthroughs broadcast live on global television." },
              { key: "C", text: "Thousands of Nobel laureates eager to collaborate on projects." },
              { key: "D", text: "Free luxury hotel suites and gold medal awards for all speakers." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段指出参会者遭遇荒唐景象：农学和中世纪诗歌硬拼在同个会场，台下只有三四名不明真相的听众，知名嘉宾名字纯属盗用。"
          },
          {
            q_type: "reading_item",
            stem: "Why are junior researchers from developing countries particularly vulnerable?",
            points: 2.0,
            sort_order: 33,
            options: [
              { key: "A", text: "Universities mandate international conference credits for promotion." },
              { key: "B", text: "They possess unlimited personal fortunes that they wish to squander." },
              { key: "C", text: "They are legally forbidden from attending legitimate domestic events." },
              { key: "D", text: "Predatory conferences offer free immigration visas to Europe." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第四段指出发展中国家的青年学者面临严苛考核，评职晋升硬性要求国际会议经历，因而成为虚假会议收割的靶子。"
          },
          {
            q_type: "reading_item",
            stem: "Predatory conferences harm public science primarily because they:",
            points: 2.0,
            sort_order: 34,
            options: [
              { key: "A", text: "Grant unearned academic legitimacy to pseudoscience and conspiracies." },
              { key: "B", text: "Cause hotel room prices to collapse across Western Europe." },
              { key: "C", text: "Prevent medical doctors from performing routine hospital surgeries." },
              { key: "D", text: "Completely destroy all global internet telecommunication cables." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第五段指出掠夺性学术会议给伪科学和阴谋论披上了合法学术外衣（veneer of academic legitimacy），毒化了公共科学共识。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that universities should combat predatory conferences by:",
            points: 2.0,
            sort_order: 35,
            options: [
              { key: "A", text: "Blacklisting predatory organizers and valuing intellectual quality over travel." },
              { key: "B", text: "Banning all scholars from ever traveling abroad for research." },
              { key: "C", text: "Abolishing all academic conferences worldwide permanently." },
              { key: "D", text: "Paying predatory organizers millions of dollars in subsidies." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨结论题。末段指出防范对策是建立黑名单机制、对青年学者开展辨别培训，且考核应聚焦实质学术质量而非盲目崇拜出境经历。"
          }
        ]
      },
      {
        section_type: "reading",
        title: "Section II: Reading Comprehension Part A (Text 4)",
        sort_order: 5,
        content: `In the contemporary corporate technology landscape, algorithmic automation has been heralded as the ultimate meritocratic equalizer. Machine learning models now filter recruitment resumes, calculate employee bonuses, and evaluate managerial performance. Proponents claim that replacing subjective human intuition with cold mathematical algorithms eliminates conscious and unconscious human bias, creating an objective hiring pipeline where decisions are governed strictly by quantifiable competence.

However, computer scientists and algorithmic accountability ethicists have dismantled this techno-utopian myth, revealing that predictive algorithms are frequently engines of automated gender discrimination. Machine learning models are trained on historical data. If an algorithmic recruitment tool analyzes past corporate hiring across technology or engineering departments—sectors historically dominated by men—the neural network identifies maleness as an implicit benchmark of professional success.

In one notorious corporate case study, Amazon developed an experimental AI recruitment tool trained on resumes submitted over a ten-year period. The algorithm quickly taught itself to penalize resumes containing the word "women's"—such as "women's rugby team captain" or "graduate of an all-women's college"—while systematically favoring candidates whose language matched traditional male resume profiles. Confronted with the stubborn persistence of algorithmic bias, the company was forced to scrap the project entirely.

Furthermore, algorithmic opacity presents acute barriers to justice. Commercial AI vendors protect their predictive code behind intellectual property trade secrecy, creating "black box" systems. When a qualified female applicant is rejected by an automated screening algorithm, neither the jobseeker nor human resource managers can explain the precise algorithmic rationale behind the rejection.

Eradicating algorithmic discrimination requires comprehensive legal regulation. Governments must mandate third-party algorithmic auditing, require transparency regarding training datasets, and legally forbid employers from relying exclusively on automated decision-making for hiring and promotion. Technology should serve to overcome human prejudices rather than codifying historical sexism into automated mathematical software.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Proponents originally claimed that algorithmic HR software would:",
            points: 2.0,
            sort_order: 36,
            options: [
              { key: "A", text: "Eliminate subjective human bias and establish an objective meritocracy." },
              { key: "B", text: "Triple the salaries of all female corporate executives." },
              { key: "C", text: "Abolish all computer software across Silicon Valley." },
              { key: "D", text: "Require every job applicant to pass a physical marathon." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第一段指出算法支持者声称算法消除了主观偏见，能建立基于客观量化能力的唯才是举机制（objective meritocracy）。"
          },
          {
            q_type: "reading_item",
            stem: "Why do recruitment algorithms often discriminate against female applicants?",
            points: 2.0,
            sort_order: 37,
            options: [
              { key: "A", text: "They are trained on historical data reflecting past male dominance." },
              { key: "B", text: "Computer processors are biologically hostile to female users." },
              { key: "C", text: "Female applicants refuse to submit resumes in electronic formats." },
              { key: "D", text: "Labor laws require algorithms to reject 90 percent of applicants." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】因果推断题。第二段指出机器学习模型训练所使用的历史数据反映了过往由男性主导的职场偏见，导致算法将男性特征内化为成功指标。"
          },
          {
            q_type: "reading_item",
            stem: "Amazon abandoned its experimental AI hiring tool because the algorithm:",
            points: 2.0,
            sort_order: 38,
            options: [
              { key: "A", text: "Systematically penalized resumes that included the word 'women's'." },
              { key: "B", text: "Accidentally transferred company funds to charitable foundations." },
              { key: "C", text: "Refused to accept any applicants who knew how to code." },
              { key: "D", text: "Deleted all corporate customer accounts across the United States." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】事实细节题。第三段通过亚马逊案例说明算法自学了偏见，歧视出现“女性（women's）”字样的简历，被迫全面废弃。"
          },
          {
            q_type: "reading_item",
            stem: "The term 'black box' in Paragraph 4 refers to algorithms that:",
            points: 2.0,
            sort_order: 39,
            options: [
              { key: "A", text: "Operate with opaque code that conceals the rationale for decisions." },
              { key: "B", text: "Are physically enclosed inside black steel metal boxes." },
              { key: "C", text: "Can only be read in complete darkness by specialized lasers." },
              { key: "D", text: "Store flight recorder data for commercial aviation airliners." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】词义事实题。第四段指出“黑盒系统（black box）”是指商业算法以商业机密为名不透明，无人知晓其筛选背后的具体决策机理。"
          },
          {
            q_type: "reading_item",
            stem: "The author concludes that preventing algorithmic discrimination requires:",
            points: 2.0,
            sort_order: 40,
            options: [
              { key: "A", text: "Mandatory third-party audits and banning fully automated hiring decisions." },
              { key: "B", text: "Abolishing all corporate human resource departments permanently." },
              { key: "C", text: "Permitting tech companies to operate without any legal regulations." },
              { key: "D", text: "Banning female candidates from applying for engineering roles." }
            ],
            correct_answer: "A",
            explanation: "【考点精析】主旨态度题。末段指出防范算法歧视必须由政府立法强制第三方审计（mandatory third-party audits），透明化训练集，并禁止全自动化决策。"
          }
        ]
      }
    ]
  }
];
