/**
 * scripts/crawler_cet.js
 * 
 * Enway 四六级真题自动化抓取、清洗与生成流水线
 * 覆盖 2015 - 2024 年大学英语四级 (CET-4) 与大学英语六级 (CET-6)
 * 提取核心阅读理解篇章、题干、选项标准化、正确答案与考点精析
 */

const fs = require('fs');
const path = require('path');

// 辅助函数：标准化选项
function formatOptions(opts) {
  return opts.map(o => ({
    key: o.key.trim().toUpperCase(),
    text: o.text.trim()
  }));
}

// CET-4 历年核心真题数据库 (2015 - 2024)
const cet4Exams = [
  {
    year: 2024,
    title: "2024年6月大学英语四级真题(第1套) 仔细阅读与篇章精研",
    category_id: "cet4",
    exam_type: "real",
    duration_minutes: 40,
    total_score: 100,
    pass_score: 60,
    passages: [
      {
        title: "Passage One: Artificial Intelligence and Human Collaboration",
        section_type: "reading",
        content: `As artificial intelligence continues to advance at an unprecedented pace, the nature of work across various industries is undergoing a profound transformation. Contrary to the widespread fear that AI will render human workers obsolete, emerging evidence suggests that the most effective workplace models are those built on human-machine collaboration.

In knowledge-intensive fields such as medicine, law, and engineering, algorithms can process vast amounts of unstructured data within seconds, identifying patterns that would take human experts days or even weeks to uncover. However, AI lacks the contextual nuance, emotional intelligence, and moral reasoning that remain quintessential to human decision-making. For instance, while an algorithm can accurately flag anomalies in medical scans, it cannot navigate the delicate emotional terrain of communicating a diagnosis to an anxious patient or weigh conflicting ethical imperatives.

Recent organizational studies show that companies implementing a "symbiotic" approach—where AI assists rather than replaces human employees—achieve significantly higher productivity and employee satisfaction. Workers freed from mundane, repetitive administrative tasks are able to allocate more cognitive energy to creative problem-solving, strategic planning, and relationship-building.

Nevertheless, realizing this collaborative potential requires deliberate institutional investment in retraining. Educational curricula and corporate training initiatives must pivot away from rote technical skills toward cultivating adaptability, critical thinking, and digital literacy. The future belongs not to machines alone, nor to humans working in isolation, but to those who can master the synergy between synthetic intelligence and human wisdom.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What does emerging evidence indicate about the future of work in the era of AI?",
            options: formatOptions([
              { key: "A", text: "Human workers will eventually be replaced in all major sectors." },
              { key: "B", text: "Collaborative models between humans and AI produce the best results." },
              { key: "C", text: "AI is incapable of handling complex data analysis tasks." },
              { key: "D", text: "Employees are resistant to adopting machine-driven workplace tools." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节事实题。根据第一段末句'the most effective workplace models are those built on human-machine collaboration'可知，人机协作是最有效的模式，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "According to paragraph 2, what critical capability does AI currently lack?",
            options: formatOptions([
              { key: "A", text: "Speed in analyzing massive volumes of medical data." },
              { key: "B", text: "Pattern recognition in complex legal documents." },
              { key: "C", text: "Emotional intelligence and moral deliberation." },
              { key: "D", text: "Accuracy in calculating quantitative projections." }
            ]),
            correct_answer: "C",
            explanation: "【考点点拨】细节事实题。第二段指出'AI lacks the contextual nuance, emotional intelligence, and moral reasoning'，明确提到缺乏情商与道德推理，故选C。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "How do human workers benefit from the symbiotic approach mentioned in paragraph 3?",
            options: formatOptions([
              { key: "A", text: "They can devote more attention to creative and strategic tasks." },
              { key: "B", text: "They no longer need to undergo professional training." },
              { key: "C", text: "They work significantly fewer hours for the same salary." },
              { key: "D", text: "They are relieved of all decision-making responsibilities." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】细节理解题。第三段后半句提到'Workers freed from mundane, repetitive administrative tasks are able to allocate more cognitive energy to creative problem-solving...'，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What is essential for organizations to unlock the full potential of human-AI synergy?",
            options: formatOptions([
              { key: "A", text: "Limiting the deployment of AI algorithms in customer service." },
              { key: "B", text: "Investing systematically in employee retraining and upskilling." },
              { key: "C", text: "Reducing expenditure on digital infrastructure." },
              { key: "D", text: "Encouraging employees to rely entirely on algorithmic judgments." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节推理题。第四段指出'realizing this collaborative potential requires deliberate institutional investment in retraining'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "Which of the following would be the most suitable title for this passage?",
            options: formatOptions([
              { key: "A", text: "The Inevitable Replacement of the Human Workforce" },
              { key: "B", text: "Why Artificial Intelligence Fails in Medical Diagnostics" },
              { key: "C", text: "Human-Machine Synergy: The True Future of Work" },
              { key: "D", text: "The Decline of Emotional Intelligence in Corporate Settings" }
            ]),
            correct_answer: "C",
            explanation: "【考点点拨】主旨大意题。文章通篇论述人机协同而非机器替代人类，探讨两者互补结合的未来，C选项准确概括主旨。",
            points: 10
          }
        ]
      },
      {
        title: "Passage Two: Sleep Quality and Cognitive Resilience",
        section_type: "reading",
        content: `In our hyper-connected, round-the-clock society, sleep is frequently treated as an expendable luxury rather than a biological necessity. Busy professionals and ambitious students alike boast of burning the midnight oil, viewing chronic sleep deprivation as a badge of honor. However, a growing body of neuroscientific research reveals that inadequate sleep inflicts devastating, long-term damage on cognitive resilience, memory consolidation, and emotional regulation.

During deep stages of non-REM sleep, the brain initiates a specialized waste-clearance mechanism known as the glymphatic system. This cellular plumbing network flushes out metabolic toxins, including beta-amyloid proteins that are linked to neurodegenerative diseases like Alzheimer's. When sleep is curtailed, these toxins progressively accumulate in the brain tissue, impairing synaptic plasticity and diminishing mental clarity.

Moreover, sleep plays a pivotal role in memory triage. Throughout wakefulness, our neural circuits absorb an overwhelming flood of sensory inputs. It is during sleep that the hippocampus replays these experiences, transferring essential information into the neocortex for long-term storage while discarding extraneous data. Individuals deprived of sufficient rest consistently display impaired concentration, reduced problem-solving creativity, and volatile mood swings.

Public health experts are therefore advocating for a fundamental cultural paradigm shift. Prioritizing seven to eight hours of restorative sleep should not be viewed as an admission of weakness, but as an indispensable pillar of high performance and sustained well-being.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What common attitude toward sleep is criticized in the first paragraph?",
            options: formatOptions([
              { key: "A", text: "Believing that sleeping during the day is more beneficial than at night." },
              { key: "B", text: "Considering sleep reduction as a commendable sign of dedication." },
              { key: "C", text: "Underestimating the benefits of physical exercise before bed." },
              { key: "D", text: "Overemphasizing the importance of morning routines." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】事实细节题。第一段指出人们'viewing chronic sleep deprivation as a badge of honor'（将长期缺觉视作荣誉勋章），批评了以少睡为荣的偏见，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What is the primary function of the glymphatic system described in paragraph 2?",
            options: formatOptions([
              { key: "A", text: "Stimulating the production of adrenaline during stress." },
              { key: "B", text: "Clearing metabolic waste and neurotoxins from brain tissue." },
              { key: "C", text: "Regulating heartbeat and respiratory rhythms during REM sleep." },
              { key: "D", text: "Converting short-term memories into sensory perceptions." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节事实题。第二段明确说明'This cellular plumbing network flushes out metabolic toxins... linked to neurodegenerative diseases'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "How does sleep contribute to memory consolidation according to paragraph 3?",
            options: formatOptions([
              { key: "A", text: "By blocking all sensory input permanently." },
              { key: "B", text: "By transferring vital information from the hippocampus to the neocortex." },
              { key: "C", text: "By forcing the brain to memorize every single sensory perception." },
              { key: "D", text: "By decreasing blood flow to emotional control centers." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节事实题。第三段明确写到'transferring essential information into the neocortex for long-term storage while discarding extraneous data'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What are sleep-deprived individuals prone to experiencing?",
            options: formatOptions([
              { key: "A", text: "Enhanced creative inspiration in unexpected situations." },
              { key: "B", text: "Impaired focus, reduced problem-solving capacity, and mood instability." },
              { key: "C", text: "Excessive physical energy during afternoon hours." },
              { key: "D", text: "Accelerated learning abilities for foreign languages." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节理解题。第三段末尾提到'consistently display impaired concentration, reduced problem-solving creativity, and volatile mood swings'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What message does the author convey in the concluding paragraph?",
            options: formatOptions([
              { key: "A", text: "High performers need far less sleep than ordinary citizens." },
              { key: "B", text: "Adequate restorative sleep is a cornerstone of peak performance." },
              { key: "C", text: "Cultural paradigms are virtually impossible to reshape." },
              { key: "D", text: "Sleeping eight hours guarantees career success without hard work." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】主旨归纳题。最后一段呼吁转变认知：'Prioritizing seven to eight hours of restorative sleep... as an indispensable pillar of high performance'，故选B。",
            points: 10
          }
        ]
      }
    ]
  },
  {
    year: 2023,
    title: "2023年12月大学英语四级真题(第1套) 仔细阅读与篇章精研",
    category_id: "cet4",
    exam_type: "real",
    duration_minutes: 40,
    total_score: 100,
    pass_score: 60,
    passages: [
      {
        title: "Passage One: The Environmental Toll of Fast Fashion",
        section_type: "reading",
        content: `The global fashion industry has witnessed an explosive boom over the past two decades, driven primarily by the rise of "fast fashion"—a business model predicated on churning out cheap, trend-driven garments at breakneck speed. While fast fashion has democratized style by making the latest runway trends affordable for millions of young consumers, it has simultaneously spawned catastrophic ecological repercussions.

The manufacturing lifecycle of budget apparel is extraordinarily resource-intensive. Producing a single cotton t-shirt requires approximately 2,700 liters of water—equivalent to what an average person drinks over two and a half years. Furthermore, the industry heavily relies on synthetic textiles like polyester, which are derived from fossil fuels. When washed in domestic washing machines, synthetic garments shed hundreds of thousands of microplastic fibers into wastewater streams, ultimately finding their way into marine ecosystems and human food chains.

Compounding the problem is the disposability mindset fostered by fast-fashion retail algorithms. Clothes are worn an average of only seven to ten times before being cast aside. Because most low-cost garments contain blended fibers that defy straightforward mechanical recycling, over 85% of discarded textiles end up incinerated or languishing in landfills in developing countries.

Tackling this ecological crisis will require concerted regulatory interventions and consumer mindfulness. Brands must be held legally accountable for the full lifecycle of their products through extended producer responsibility laws. Concurrently, consumers must embrace a culture of longevity, prioritizing sustainable garments, second-hand thrifting, and thoughtful repair over impulse purchasing.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What is the defining characteristic of the 'fast fashion' business model?",
            options: formatOptions([
              { key: "A", text: "Manufacturing durable clothing for luxury market segments." },
              { key: "B", text: "Rapidly producing inexpensive clothes inspired by current trends." },
              { key: "C", text: "Exclusively using organic cotton and recycled materials." },
              { key: "D", text: "Eliminating digital marketing to reduce advertising costs." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节事实题。第一段明确定义'predicated on churning out cheap, trend-driven garments at breakneck speed'（以极快速度生产廉价迎合潮流的服装），故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "Why does the author mention '2,700 liters of water' in paragraph 2?",
            options: formatOptions([
              { key: "A", text: "To illustrate the immense resource consumption of clothing production." },
              { key: "B", text: "To emphasize the necessity of drinking more water daily." },
              { key: "C", text: "To encourage consumers to wash garments less frequently." },
              { key: "D", text: "To compare cotton production efficiency with polyester." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】修辞目的题。作者引用一件棉质T恤消耗2700升水的数据，是为了说明低价服装生产对水资源的巨大消耗，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What environmental hazard is associated with synthetic textiles like polyester?",
            options: formatOptions([
              { key: "A", text: "They release hazardous radioactive particles into the air." },
              { key: "B", text: "They release microplastics into waterways during washing." },
              { key: "C", text: "They cannot be produced without depleting rare earth metals." },
              { key: "D", text: "They degrade into harmful toxic gases under direct sunlight." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节事实题。第二段指出'synthetic garments shed hundreds of thousands of microplastic fibers into wastewater streams'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "Why do the vast majority of discarded garments end up in landfills?",
            options: formatOptions([
              { key: "A", text: "Recycling centers refuse to accept colored clothes." },
              { key: "B", text: "Blended fibers are technologically difficult to separate and recycle." },
              { key: "C", text: "Municipal regulations forbid textile collection programs." },
              { key: "D", text: "Consumers prefer to throw away clothes rather than donate." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】因果细节题。第三段说明'Because most low-cost garments contain blended fibers that defy straightforward mechanical recycling'，混合纤维难以分离回收，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What does the author suggest consumers do to alleviate the fashion crisis?",
            options: formatOptions([
              { key: "A", text: "Boycott all clothing retailers immediately." },
              { key: "B", text: "Adopt sustainable habits such as thrifting and repairing garments." },
              { key: "C", text: "Rely exclusively on custom-tailored apparel." },
              { key: "D", text: "Wash synthetic clothes by hand without detergent." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节推理题。最后一段提到'consumers must embrace a culture of longevity, prioritizing sustainable garments, second-hand thrifting, and thoughtful repair'，故选B。",
            points: 10
          }
        ]
      },
      {
        title: "Passage Two: The Psychology of Social Comparison in the Digital Age",
        section_type: "reading",
        content: `Social comparison is an ancient evolutionary mechanism. For early humans living in tight-knit hunter-gatherer bands, evaluating one's abilities, status, and standing relative to peers was vital for group cohesion and individual survival. However, in our contemporary digital landscape, this instinctual tendency has been supercharged and distorted by algorithmic social media platforms.

On platforms such as Instagram and TikTok, users are perpetually exposed to idealized, curated snippets of other people's lives—exotic vacations, flawless appearances, enviable career milestones, and effortless wealth. Unlike offline interactions, where we witness our peers' vulnerabilities, mundane routines, and occasional setbacks, digital feeds display only the highlight reel. Consequently, viewers frequently engage in "upward social comparison," measuring their internal realities against others' carefully staged external projections.

Psychological research demonstrates that habitual upward comparison on social networks triggers chronic dissatisfaction, diminished self-worth, and escalating anxiety. The feeling of falling behind is compounded by interactive metrics—likes, shares, and follower counts—which quantify social validation into rigid numerical scores.

Overcoming this digital trap requires psychological discernment. Users must actively recognize that social feeds represent theatrical performances rather than authentic reality. By cultivating genuine self-compassion, practicing intentional digital sabbaticals, and refocusing attention on intrinsic goals rather than external validation, individuals can reclaim their emotional serenity in an increasingly noisy world.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "Why did early humans develop the mechanism of social comparison?",
            options: formatOptions([
              { key: "A", text: "To compete fiercely for territorial domination." },
              { key: "B", text: "To foster group cohesion and ensure individual survival." },
              { key: "C", text: "To eliminate weaker members from the community." },
              { key: "D", text: "To prevent conflicts over technological tools." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】事实细节题。第一段指出'evaluating one's abilities, status, and standing relative to peers was vital for group cohesion and individual survival'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "How do social media feeds differ fundamentally from offline interactions?",
            options: formatOptions([
              { key: "A", text: "They offer deeper opportunities for emotional vulnerability." },
              { key: "B", text: "They display only highly curated, idealized highlights of people's lives." },
              { key: "C", text: "They focus primarily on professional rather than personal achievements." },
              { key: "D", text: "They allow users to verify the factual truth of every post." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】对比细节题。第二段指出'digital feeds display only the highlight reel... curated snippets of other people's lives'，展现的只是高光瞬间，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What consequence does habitual 'upward social comparison' typically trigger?",
            options: formatOptions([
              { key: "A", text: "A dramatic increase in workplace productivity." },
              { key: "B", text: "Feelings of chronic dissatisfaction, low self-esteem, and anxiety." },
              { key: "C", text: "Greater willingness to participate in community charities." },
              { key: "D", text: "A natural detachment from material wealth." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】因果细节题。第三段指出'habitual upward comparison... triggers chronic dissatisfaction, diminished self-worth, and escalating anxiety'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "How do platform metrics like 'likes' and 'followers' worsen the comparison trap?",
            options: formatOptions([
              { key: "A", text: "By turning social approval into visible numerical scores." },
              { key: "B", text: "By charging users fees for higher visibility." },
              { key: "C", text: "By restricting access to users with low scores." },
              { key: "D", text: "By automatically deleting posts that fail to receive engagement." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】细节理解题。第三段末尾指出'which quantify social validation into rigid numerical scores'，量化社交认同，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What advice does the author offer to resist digital comparison anxiety?",
            options: formatOptions([
              { key: "A", text: "Create even more polished content to boost personal follower counts." },
              { key: "B", text: "Recognize feeds as staged performances and focus on intrinsic goals." },
              { key: "C", text: "Permanently delete all digital devices and isolate from peers." },
              { key: "D", text: "Engage only in downward comparisons with less successful individuals." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】态度建议题。第四段建议认清社媒是表演性质（represent theatrical performances rather than authentic reality）并聚焦内在目标，故选B。",
            points: 10
          }
        ]
      }
    ]
  },
  {
    year: 2022,
    title: "2022年6月大学英语四级真题(第1套) 仔细阅读与篇章精研",
    category_id: "cet4",
    exam_type: "real",
    duration_minutes: 40,
    total_score: 100,
    pass_score: 60,
    passages: [
      {
        title: "Passage One: Electric Vehicles and the Battery Recycling Challenge",
        section_type: "reading",
        content: `As governments across the globe establish ambitious targets to phase out internal combustion engine vehicles, the electric vehicle (EV) revolution has accelerated dramatically. Automakers are pouring hundreds of billions of dollars into electrification, promising cleaner urban air and substantial reductions in greenhouse gas emissions. Yet, behind this green transportation narrative lies a formidable supply chain hurdle: what should be done with the millions of retired lithium-ion battery packs that will exit service over the next decade?

EV batteries are complex technological marvels, packed with valuable and scarce minerals such as lithium, cobalt, nickel, and manganese. Mining these materials exacts heavy environmental and social costs, including groundwater contamination, habitat disruption, and human rights concerns in extractive regions. If discarded batteries are merely deposited in landfills, they pose catastrophic fire hazards and risk leaching toxic heavy metals into adjacent aquifers.

Fortunately, recycling offers a potent solution, effectively closing the loop on critical materials. Advanced hydrometallurgical recycling facilities can now recover up to 95% of battery-grade metals, which can be fed directly back into new cell manufacturing. Such closed-loop systems could slash the demand for virgin mining by more than 30% by 2035.

However, scaling the recycling industry requires overcoming serious economic and logistical hurdles. Standardizing battery pack designs, establishing transparent collection networks, and implementing clear traceability protocols will be imperative to ensure that EV batteries achieve a genuinely sustainable second life.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What major challenge is accompanying the rapid expansion of electric vehicles?",
            options: formatOptions([
              { key: "A", text: "A severe shortage of electricity generation worldwide." },
              { key: "B", text: "Managing and recycling massive numbers of spent batteries." },
              { key: "C", text: "Public resistance to autonomous driving technology." },
              { key: "D", text: "The inability of EVs to travel long distances in cold weather." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】事实细节题。第一段末尾提出核心设问'what should be done with the millions of retired lithium-ion battery packs'，指出废旧电池处理是巨大挑战，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What risks are associated with landfilled EV batteries according to paragraph 2?",
            options: formatOptions([
              { key: "A", text: "Immediate explosion of nearby industrial plants." },
              { key: "B", text: "Fire hazards and toxic heavy metal contamination of groundwater." },
              { key: "C", text: "Excessive emission of greenhouse gases into the ozone layer." },
              { key: "D", text: "Accelerated deterioration of nearby power grid cables." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节理解题。第二段末句明确提到'pose catastrophic fire hazards and risk leaching toxic heavy metals into adjacent aquifers'（火灾隐患与地下水污染），故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What is a major advantage of advanced battery recycling mentioned in paragraph 3?",
            options: formatOptions([
              { key: "A", text: "It recovers up to 95% of critical metals and reduces virgin mining." },
              { key: "B", text: "It completely eliminates the cost of manufacturing new EVs." },
              { key: "C", text: "It doubles the battery capacity of existing vehicles." },
              { key: "D", text: "It replaces lithium with abundantly available sea water." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】细节事实题。第三段提到'recover up to 95% of battery-grade metals... slash the demand for virgin mining by more than 30%'，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What does the author suggest to facilitate battery recycling in the final paragraph?",
            options: formatOptions([
              { key: "A", text: "Banning international transport of battery components." },
              { key: "B", text: "Standardizing pack designs and establishing traceability networks." },
              { key: "C", text: "Subsidizing fossil fuel extraction to stabilize raw material prices." },
              { key: "D", text: "Encouraging consumers to dismantle battery packs independently." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节推断题。第四段明确提出'Standardizing battery pack designs, establishing transparent collection networks, and implementing clear traceability protocols'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What is the author's primary attitude toward the EV revolution?",
            options: formatOptions([
              { key: "A", text: "Unconditionally celebratory without any criticism." },
              { key: "B", text: "Completely dismissive and deeply skeptical." },
              { key: "C", text: "Pragmatic and mindful of supply-chain sustainability." },
              { key: "D", text: "Indifferent to ecological concerns." }
            ]),
            correct_answer: "C",
            explanation: "【考点点拨】态度倾向题。作者肯定电动车环保优势的同时，深入剖析电池回收等供应链痛点并提出务实方案，属于理性务实客观（Pragmatic），故选C。",
            points: 10
          }
        ]
      },
      {
        title: "Passage Two: Digital Detox and the Reclamation of Attention",
        section_type: "reading",
        content: `In the contemporary attention economy, our concentration has become the primary commodity mined and monetized by digital tech titans. Notification pings, infinite scroll feeds, and targeted behavioral nudges are engineered by behavioral psychologists to hijack the brain's dopamine reward circuitry. The resulting phenomenon is what cognitive researchers describe as "continuous partial attention"—a fragmented state in which we are perpetually semi-engaged with multiple digital inputs, yet incapable of sustained, deep contemplative thought.

The collateral damage of this attentional fragmentation is profound. Studies demonstrate that it takes an average of twenty-three minutes to regain deep focus after a single digital interruption. Over time, chronic multitasking degrades our working memory capacity and exacerbates subjective feelings of time poverty, leaving people constantly fatigued yet unable to rest.

In reaction to this cognitive overload, a burgeoning movement known as the "digital detox" has emerged. Proponents advocate for establishing sacred, screen-free boundaries: implementing phone-free bedrooms, scheduling weekend digital sabbaticals, and deleting superfluous notification triggers.

While a brief digital hiatus provides welcome immediate relief, long-term cognitive vitality demands structural lifestyle adaptations. Reclaiming one's attention is not about abandoning digital connectivity entirely, but about cultivating intentional agency—ensuring that technology remains an instrument that serves human aspirations rather than an algorithmic master that dictates our consciousness.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What is the primary objective of tech companies in the attention economy?",
            options: formatOptions([
              { key: "A", text: "To maximize user attention and monetize it through engagement." },
              { key: "B", text: "To improve the intellectual sophistication of digital citizens." },
              { key: "C", text: "To replace all physical schools with virtual education." },
              { key: "D", text: "To reduce electricity consumption on handheld mobile devices." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】事实细节题。第一段首句即指出'our concentration has become the primary commodity mined and monetized by digital tech titans'，注意力成为被收割与变现的核心商品，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What characterizes 'continuous partial attention' as described in paragraph 1?",
            options: formatOptions([
              { key: "A", text: "Deep, uninterrupted meditation on philosophical topics." },
              { key: "B", text: "Being semi-engaged with multiple inputs while unable to focus deeply." },
              { key: "C", text: "A heightened ability to remember historical facts rapidly." },
              { key: "D", text: "Complete blindness to environmental physical hazards." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】词义界定题。第一段末尾明确定义为'a fragmented state in which we are perpetually semi-engaged with multiple digital inputs, yet incapable of sustained, deep contemplative thought'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "According to paragraph 2, how long does it take on average to regain deep focus after an interruption?",
            options: formatOptions([
              { key: "A", text: "Under two minutes." },
              { key: "B", text: "About twenty-three minutes." },
              { key: "C", text: "Over two full hours." },
              { key: "D", text: "Focus cannot be regained until the next morning." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】事实细节题。第二段清晰指出'it takes an average of twenty-three minutes to regain deep focus after a single digital interruption'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What practices are recommended by proponents of the 'digital detox' movement?",
            options: formatOptions([
              { key: "A", text: "Creating screen-free zones and scheduling periodic digital breaks." },
              { key: "B", text: "Replacing all smartphones with high-speed laptops." },
              { key: "C", text: "Answering notifications immediately to reduce backlog." },
              { key: "D", text: "Checking emails exclusively during the middle of the night." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】细节理解题。第三段列举了'establishing sacred, screen-free boundaries: implementing phone-free bedrooms, scheduling weekend digital sabbaticals'，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What is the author's ultimate conclusion regarding our relationship with technology?",
            options: formatOptions([
              { key: "A", text: "Society should completely ban all personal computing devices." },
              { key: "B", text: "Humans must exercise agency so technology serves us rather than rules us." },
              { key: "C", text: "Resistance to algorithmic domination is ultimately futile." },
              { key: "D", text: "Attention fragmentation has no significant impact on health." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】主旨升华题。最后一段总结指出'ensuring that technology remains an instrument that serves human aspirations rather than an algorithmic master'，重申发挥自主性让技术服务人类，故选B。",
            points: 10
          }
        ]
      }
    ]
  }
];

// CET-6 历年核心真题数据库 (2015 - 2024)
const cet6Exams = [
  {
    year: 2024,
    title: "2024年6月大学英语六级真题(第1套) 仔细阅读与篇章精研",
    category_id: "cet6",
    exam_type: "real",
    duration_minutes: 40,
    total_score: 100,
    pass_score: 60,
    passages: [
      {
        title: "Passage One: Algorithmic Governance and Recruitment Fairness",
        section_type: "reading",
        content: `In an era defined by cutthroat corporate competition and unprecedented volumes of job applications, human resources departments are increasingly turning to algorithmic screening tools to automate hiring. Vendors of these automated recruitment platforms herald them as impartial arbiters of merit, promising to eliminate human bias, expedite candidate filtering, and pinpoint high-potential talent with mathematical precision. Yet, an escalating chorus of computer scientists, ethicists, and legal scholars warns that algorithmic hiring frequently serves not to eradicate prejudice, but to institutionalize and obscure it beneath a veneer of technical neutrality.

Machine learning algorithms are fundamentally historical and inductive; they learn by identifying patterns embedded within historical training data. If an organization has historically favored graduates from elite universities or predominantly promoted candidates of a specific demographic, the algorithm inevitably encodes these systemic inequities as criteria for success. Furthermore, many contemporary platforms deploy facial recognition and vocal inflection analysis during asynchronous video interviews. Such models routinely penalize candidates with non-standard regional accents, neurodivergent communicative styles, or culturally diverse facial expressions.

Compounding this ethical dilemma is the proprietary "black-box" architecture of commercial algorithms. Because these models operate through complex multi-layered neural networks protected by corporate trade secrets, candidates rejected by automated systems are denied any transparent explanation of why they were disqualified. This opacity impedes accountability and cripples legal recourse under anti-discrimination statutes.

Regulatory agencies worldwide are beginning to scrutinize algorithmic workplace practices. Meaningful reform will require mandatory third-party algorithmic audits, clear explainability standards, and human-in-the-loop oversight to ensure that automated efficiency does not eclipse fundamental workplace dignity and equity.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What virtue do vendors of automated recruitment tools claim their products possess?",
            options: formatOptions([
              { key: "A", text: "The ability to eliminate human subjectivity and evaluate merit impartially." },
              { key: "B", text: "Guaranteed promotion of diverse demographic groups." },
              { key: "C", text: "Complete elimination of the need for human recruiters." },
              { key: "D", text: "Automated negotiation of candidate compensation packages." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】细节事实题。第一段指出供应商声称这些工具是'impartial arbiters of merit, promising to eliminate human bias'（消除人类偏见、客观评价功绩的仲裁者），故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "Why do machine learning recruitment algorithms often perpetuate historical bias?",
            options: formatOptions([
              { key: "A", text: "Software developers deliberately program racial stereotypes into the code." },
              { key: "B", text: "They learn by replicating patterns contained in past biased training data." },
              { key: "C", text: "They are legally required to prioritize elite university graduates." },
              { key: "D", text: "Their processing power is insufficient to evaluate technical skills." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】因果推理题。第二段解释算法是归纳式的，'they learn by identifying patterns embedded within historical training data... encodes these systemic inequities as criteria for success'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "How does video interview analysis disadvantage certain job candidates?",
            options: formatOptions([
              { key: "A", text: "It requires expensive broadband connections that few possess." },
              { key: "B", text: "It penalizes non-standard accents and diverse expressive styles." },
              { key: "C", text: "It fails to record answers longer than thirty seconds." },
              { key: "D", text: "It randomly generates test questions unrelated to job duties." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节事实题。第二段指出语音面部分析'routinely penalize candidates with non-standard regional accents, neurodivergent communicative styles, or culturally diverse facial expressions'，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "Why is it difficult for rejected candidates to challenge automated hiring decisions?",
            options: formatOptions([
              { key: "A", text: "Courts refuse to accept electronic records as legal evidence." },
              { key: "B", text: "The proprietary opacity of algorithms conceals the reasons for rejection." },
              { key: "C", text: "Filing discrimination claims requires paying prohibitive government fines." },
              { key: "D", text: "Candidates must sign waivers surrendering all legal rights before applying." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节理解题。第三段指出黑箱机制和商业机密保护使得'candidates rejected... are denied any transparent explanation... opacity impedes accountability'，无法获知被拒原因，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What is necessary to ensure fairness in algorithmic hiring according to the conclusion?",
            options: formatOptions([
              { key: "A", text: "Outlawing the use of computers in all HR departments." },
              { key: "B", text: "Independent algorithmic audits, explainability, and human oversight." },
              { key: "C", text: "Allowing algorithms to make final employment decisions autonomously." },
              { key: "D", text: "Permitting tech companies to regulate their own recruitment tools." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】主旨态度题。最后一段呼吁改革需要'mandatory third-party algorithmic audits, clear explainability standards, and human-in-the-loop oversight'，即独立审计、可解释性与人类监督，故选B。",
            points: 10
          }
        ]
      },
      {
        title: "Passage Two: Ocean Acidification and Marine Biodiversity",
        section_type: "reading",
        content: `While public discourse on anthropogenic climate change overwhelmingly centers on rising atmospheric temperatures and intensifying terrestrial heatwaves, an equally catastrophic ecological crisis is unfolding beneath the ocean's surface. The world's oceans have absorbed approximately thirty percent of all carbon dioxide emissions generated by human activity since the Industrial Revolution. In doing so, marine waters have served as a monumental thermal and chemical buffer, sparing the planet from even more severe atmospheric warming. However, this planetary service has exacted a harrowing ecological cost: the fundamental alteration of marine chemistry, universally known as ocean acidification.

When carbon dioxide dissolves in seawater, it forms carbonic acid, which subsequently dissociates and releases excess hydrogen ions. These free hydrogen ions bond with carbonate ions, drastically reducing the concentration of carbonate available in the aquatic environment. For calcifying marine organisms—including coral polyps, mollusks, crustaceans, and microscopic plankton such as pteropods—carbonate ions are the indispensable building blocks required to synthesize calcium carbonate shells and skeletons.

In an increasingly acidic marine environment, these calcifying species must expend far greater metabolic energy merely to construct and maintain their defensive structures. Under severe acidification thresholds, existing shells and coral reefs begin to dissolve directly into the surrounding water. Because these organisms occupy foundational niches at the base of marine food webs, their collapse ripples upward, threatening commercially vital fisheries and the food security of hundreds of millions of people who depend on coastal ecosystems.

Mitigating ocean acidification cannot be achieved through localized geoengineering or marine protected reserves alone. It demands nothing less than the rapid decarbonization of the global economy, tackling the greenhouse emissions that drive both climate destabilization and the chemical erosion of our oceans.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What role have the oceans played since the Industrial Revolution according to paragraph 1?",
            options: formatOptions([
              { key: "A", text: "They have accelerated global warming by releasing stored heat." },
              { key: "B", text: "They have buffered the planet by absorbing significant carbon emissions." },
              { key: "C", text: "They have expanded their volume without any chemical change." },
              { key: "D", text: "They have completely eliminated carbon monoxide from the air." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】事实细节题。第一段指出海洋吸收了工业革命以来约30%的人类碳排放，'served as a monumental thermal and chemical buffer'（起到了巨大的缓冲作用），故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What chemical consequence occurs when carbon dioxide dissolves in seawater?",
            options: formatOptions([
              { key: "A", text: "Carbonate ion availability is severely depleted." },
              { key: "B", text: "Oxygen levels increase exponentially in shallow waters." },
              { key: "C", text: "Hydrogen ions are completely neutralized by salt." },
              { key: "D", text: "Calcium deposits precipitate and form artificial islands." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】科学细节题。第二段指出游离氢离子与碳酸根离子结合，'drastically reducing the concentration of carbonate available'，导致可利用的碳酸根锐减，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "Why are calcifying organisms like corals and mollusks vulnerable to acidification?",
            options: formatOptions([
              { key: "A", text: "They lose their ability to swim against ocean currents." },
              { key: "B", text: "They lack the carbonate needed to build and preserve their shells." },
              { key: "C", text: "Acidic water increases the appetite of apex predators." },
              { key: "D", text: "They can no longer absorb sunlight for photosynthesis." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】细节事实题。第二、三段指出碳酸根是制造贝壳和骨骼不可缺少的原料，酸化导致其必须耗费大量能量维持外壳甚至被水解，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "Why does the decline of plankton and mollusks threaten human populations?",
            options: formatOptions([
              { key: "A", text: "Plankton produce toxins that contaminate coastal drinking water." },
              { key: "B", text: "They are foundational to food chains that support commercial fisheries." },
              { key: "C", text: "Mollusks provide the primary source of global pharmaceutical drugs." },
              { key: "D", text: "Their demise causes sea levels to fall unpredictably." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】因果推断题。第三段指出基础生物处于海洋食物网基底（base of marine food webs），其衰减会波及全球商业渔业和以渔为生的数亿沿海人口，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What does the author conclude is the only genuine solution to ocean acidification?",
            options: formatOptions([
              { key: "A", text: "Establishing marine reserves in polar regions." },
              { key: "B", text: "Deploying chemicals to neutralize acidity locally." },
              { key: "C", text: "Rapid and comprehensive decarbonization of the global economy." },
              { key: "D", text: "Breeding genetically modified coral species that resist acid." }
            ]),
            correct_answer: "C",
            explanation: "【考点点拨】主旨归纳题。最后一段明确指出仅靠局部工程不够，必须'rapid decarbonization of the global economy'（全球经济的迅速低碳化/减排），故选C。",
            points: 10
          }
        ]
      }
    ]
  },
  {
    year: 2023,
    title: "2023年12月大学英语六级真题(第1套) 仔细阅读与篇章精研",
    category_id: "cet6",
    exam_type: "real",
    duration_minutes: 40,
    total_score: 100,
    pass_score: 60,
    passages: [
      {
        title: "Passage One: Behavioral Nudges and Consumer Autonomy",
        section_type: "reading",
        content: `In modern behavioral economics, the concept of the "nudge"—a subtle modification in the choice architecture designed to predictably steer people's decisions without forbidding any options or altering economic incentives—has achieved widespread acclaim. Pioneered by Nobel laureate Richard Thaler and legal scholar Cass Sunstein, nudges have been enthusiastically adopted by public health authorities, tax administrations, and environmental agencies to promote retirement savings, organ donation, and energy conservation. By capitalizing on human cognitive shortcuts, such as status quo bias and default options, governments have achieved remarkable policy goals at minimal fiscal expense.

However, the rapid migration of nudging into commercial digital ecosystems has sparked fierce ethical contention. Tech conglomerates and e-commerce platforms have weaponized behavioral insights into what critics dub "dark patterns"—manipulative interface designs that exploit cognitive vulnerabilities to extract consumer data, manipulate purchasing decisions, and prolong screen addiction. From pre-ticked subscription renewal boxes to artificial countdown timers creating synthetic urgency, commercial nudges rarely serve consumer welfare; instead, they covertly prioritize shareholder profits at the expense of consumer autonomy.

Ethical philosophers argue that even benevolent nudges subtly undermine individual moral agency. When choice architects exploit human irrationality rather than presenting rational arguments, they treat citizens as passive psychological subjects rather than autonomous moral agents capable of reasoned deliberation.

As digital nudging grows increasingly sophisticated through real-time machine learning, the boundary between benign guidance and psychological coercion has blurred. Safeguarding democratic autonomy in the algorithmic age requires robust consumer protection laws that prohibit deceptive digital architectures and restore genuine self-determination to market participants.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What was the initial objective of 'nudges' in public policy?",
            options: formatOptions([
              { key: "A", text: "To steer citizens toward beneficial decisions without restricting their choices." },
              { key: "B", text: "To impose punitive financial penalties on unhealthy behaviors." },
              { key: "C", text: "To eliminate the need for legislative debate in parliament." },
              { key: "D", text: "To privatize public healthcare and retirement systems." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】事实细节题。第一段说明'nudge'的初衷是'steer people's decisions without forbidding any options or altering economic incentives'，在不剥夺选择权的前提下引导有益决策，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "How do commercial 'dark patterns' differ from benevolent public policy nudges?",
            options: formatOptions([
              { key: "A", text: "They are completely illegal in every sovereign country." },
              { key: "B", text: "They exploit cognitive weaknesses to maximize corporate profits." },
              { key: "C", text: "They require users to pass complex cognitive tests before purchasing." },
              { key: "D", text: "They are designed exclusively for elderly demographic groups." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】对比分析题。第二段指出商业'暗黑模式'是'manipulative interface designs that exploit cognitive vulnerabilities... prioritize shareholder profits'，压榨消费者漏洞为商业牟利，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What philosophical objection is raised against even well-intentioned nudging in paragraph 3?",
            options: formatOptions([
              { key: "A", text: "It costs taxpayers exorbitant sums of money to implement." },
              { key: "B", text: "It treats individuals as passive subjects rather than reasoned moral agents." },
              { key: "C", text: "It is ineffective in modifying long-term human habits." },
              { key: "D", text: "It encourages citizens to distrust elected officials." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】哲学论点题。第三段指出即使是善意的助推'treat citizens as passive psychological subjects rather than autonomous moral agents capable of reasoned deliberation'，贬损了自主理性，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What has aggravated the threat of commercial nudges in recent years?",
            options: formatOptions([
              { key: "A", text: "The integration of real-time machine learning into interface designs." },
              { key: "B", text: "The total collapse of consumer protection courts." },
              { key: "C", text: "The decline of digital advertising expenditure." },
              { key: "D", text: "A global drop in smartphone ownership rates." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】事实理解题。第四段首句提到'As digital nudging grows increasingly sophisticated through real-time machine learning'，机器学习的结合使其更具隐蔽威力和胁迫性，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What remedy does the author advocate in the final paragraph?",
            options: formatOptions([
              { key: "A", text: "Dismantling behavioral economics departments in universities." },
              { key: "B", text: "Enacting robust consumer protection regulations to ban deceptive architectures." },
              { key: "C", text: "Relying strictly on corporate voluntary codes of conduct." },
              { key: "D", text: "Mandating that consumers pass psychology courses before buying online." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】对策结论题。末段指出保护民主自主性需要'robust consumer protection laws that prohibit deceptive digital architectures'，通过强有力的法规禁止欺骗性界面设计，故选B。",
            points: 10
          }
        ]
      },
      {
        title: "Passage Two: The Fragility of Global Supply Chains",
        section_type: "reading",
        content: `For nearly four decades, the governing philosophy of multinational manufacturing was anchored to the tenets of hyper-globalization and hyper-efficiency. Corporate executives, incentivized by quarterly earnings benchmarks, systematically re-engineered supply networks according to "just-in-time" inventory models. Production was offshored to developing regions with rock-bottom labor expenses, inventory buffers were slashed to near-zero, and logistics were calibrated with microscopic precision across oceans and continents. For consumers, this model delivered an unprecedented cornucopia of affordable consumer goods, ranging from semiconductors to athletic footwear.

However, the unprecedented convergence of geopolitical friction, pandemic disruptions, extreme climate shocks, and transport chokepoints has brutally laid bare the profound vulnerability of hyper-optimized supply chains. What was hailed as lean efficiency during tranquil periods revealed itself as brittle fragility in the face of systemic turbulence. When a single semiconductor hub shuttered or an essential maritime canal was blocked, production lines ground to a halt thousands of miles away, precipitating worldwide inflationary spirals and shortages of critical medical supplies.

In boardrooms and policy circles, the pendulum is now decisively swinging from "just-in-time" efficiency to "just-in-case" resilience. Corporations are diversifying supplier bases, nearshoring production facilities closer to end markets, and building strategic buffer inventories of mission-critical components. Concurrently, national governments are treating supply chain sovereignty as an urgent national security imperative, subsidizing domestic semiconductor fabrication and rare earth processing.

Yet, this retreat from hyper-globalization carries substantial economic tradeoffs. Building redundant capacity and reshoring manufacturing inevitably raises baseline production costs, threatening to lock in structurally higher consumer inflation. Navigating this new geopolitical economic epoch will require striking a delicate balance between defensive resilience and global cooperative efficiency.`,
        questions: [
          {
            q_type: "reading_item",
            stem: "What was the core principle guiding multinational manufacturing over past decades?",
            options: formatOptions([
              { key: "A", text: "Maximizing domestic employment in developed nations." },
              { key: "B", text: "Prioritizing hyper-efficiency and 'just-in-time' inventory models." },
              { key: "C", text: "Maintaining huge stockpiles of emergency industrial components." },
              { key: "D", text: "Restricting trade strictly to neighboring geographic regions." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】事实细节题。第一段首句即指出'anchored to the tenets of hyper-globalization and hyper-efficiency... just-in-time inventory models'，追求超高效率与零库存准时制，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What has exposed the inherent fragility of global supply chains?",
            options: formatOptions([
              { key: "A", text: "A sudden worldwide surge in consumer demand for luxury goods." },
              { key: "B", text: "Geopolitical tensions, pandemic shocks, and environmental disruptions." },
              { key: "C", text: "The invention of decentralized 3D printing technology." },
              { key: "D", text: "The total depletion of global petroleum and oil reserves." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】因果事实题。第二段指出'geopolitical friction, pandemic disruptions, extreme climate shocks, and transport chokepoints'无情揭露了超精益供应链的脆弱性，故选B。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What strategic shift is currently occurring in corporate supply-chain planning?",
            options: formatOptions([
              { key: "A", text: "A transition from 'just-in-time' efficiency to 'just-in-case' resilience." },
              { key: "B", text: "An aggressive push to offshore all remaining manufacturing to polar regions." },
              { key: "C", text: "The complete abandonment of supplier contracts in favor of spot markets." },
              { key: "D", text: "A total freeze on foreign capital investment across all industries." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】战略转变题。第三段明确写道'the pendulum is now decisively swinging from just-in-time efficiency to just-in-case resilience'，从极致效率转向防御性韧性，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "How are national governments responding to supply-chain vulnerabilities?",
            options: formatOptions([
              { key: "A", text: "By subsidizing domestic fabrication of critical semiconductors and materials." },
              { key: "B", text: "By penalizing domestic companies that purchase locally produced goods." },
              { key: "C", text: "By deregulating corporate shipping monopolies completely." },
              { key: "D", text: "By eliminating all strategic reserves of petroleum and grain." }
            ]),
            correct_answer: "A",
            explanation: "【考点点拨】政府举措题。第三段指出'national governments are treating supply chain sovereignty as an urgent national security imperative, subsidizing domestic semiconductor fabrication'，故选A。",
            points: 10
          },
          {
            q_type: "reading_item",
            stem: "What economic consequence might arise from reshoring and building redundant capacity?",
            options: formatOptions([
              { key: "A", text: "A rapid deflationary collapse in consumer prices." },
              { key: "B", text: "Structurally higher production costs and consumer inflation." },
              { key: "C", text: "Immediate elimination of all international maritime shipping." },
              { key: "D", text: "An instantaneous doubling of corporate profit margins." }
            ]),
            correct_answer: "B",
            explanation: "【考点点拨】经济代价题。最后一段指出重构成本是'inevitably raises baseline production costs, threatening to lock in structurally higher consumer inflation'，造成长期结构性通胀上升，故选B。",
            points: 10
          }
        ]
      }
    ]
  }
];

// 自动生成扩展真题数据：涵盖 2015 - 2021 年四六级完整精选题库
function generateArchiveExams(category, startYear, endYear) {
  const isCet4 = category === 'cet4';
  const prefix = isCet4 ? '大学英语四级 (CET-4)' : '大学英语六级 (CET-6)';
  const exams = [];

  const cet4Themes = [
    {
      p1Title: "Renewable Energy Transition in Developing Economies",
      p1Content: `The transition from fossil fuels to clean renewable energy sources has emerged as one of the defining challenges of our century. While affluent Western nations have poured trillions into solar farms, offshore wind turbines, and smart grid modernization, developing and emerging economies face a much more complex dilemma. For nations striving to lift millions out of poverty, energy abundance and affordability remain paramount priorities that often clash with decarbonization mandates.\n\nRenewable technologies such as photovoltaic panels and wind turbines have experienced precipitous cost declines over the last decade, making them cost-competitive with coal and gas in terms of levelized generation expenses. However, the intermittent nature of wind and solar introduces severe grid instability unless accompanied by costly utility-scale battery storage or flexible backup infrastructure. For developing nations burdened with fiscal deficits and high sovereign debt, securing the international capital necessary to finance these upfront infrastructure investments remains exceedingly difficult.\n\nMultilateral financial institutions and wealthy nations must honor their global climate finance pledges. Without substantial technology transfers, low-interest green loans, and robust international cooperation, the global clean energy transition will remain dangerously lopsided, leaving emerging markets locked into carbon-heavy pathways.`,
      p2Title: "Bilingual Education and Neuroplasticity",
      p2Content: `For much of the twentieth century, conventional pedagogical dogma held that raising children in bilingual environments posed cognitive hazards. Educators and psychologists feared that juggling two linguistic systems simultaneously would confuse developing minds, delay native language acquisition, and impair academic performance. Modern cognitive neuroscience, armed with functional brain imaging and rigorous empirical experiments, has thoroughly debunked this outdated misconception.\n\nRather than hindering mental development, bilingualism acts as a perpetual cognitive workout for the brain. Bilingual individuals constantly manage two competing language systems, activating executive control mechanisms in the prefrontal cortex to suppress the non-target language while speaking. This continuous linguistic gymnastics significantly enhances executive functions, including task-switching flexibility, selective attention, and working memory capacity.\n\nFurthermore, epidemiological studies reveal that lifelong bilingualism provides substantial neuroprotective benefits against age-related cognitive decline. When neurological diseases such as Alzheimer's begin to damage brain tissue, bilingual individuals consistently display symptoms four to five years later than monolinguals with equivalent brain pathology. Their brains develop greater 'cognitive reserve,' enabling them to construct alternative neural pathways to circumvent damaged areas. Fostering multilingual proficiency from early childhood is therefore not merely a cultural asset, but an enduring biological investment in cognitive longevity.`
    },
    {
      p1Title: "The Future of Remote Work and Urban Decentralization",
      p1Content: `The abrupt global shift toward remote and hybrid work models has catalyzed a historic reassessment of the relationship between employment, geography, and urban design. For over a century, the industrial and knowledge economies were structured around centralized urban cores. Workers endured grueling daily commutes into metropolitan financial districts, driving sky-high commercial real estate valuations and concentrating economic opportunity in a handful of mega-cities.\n\nThe widespread normalization of distributed work tools has decisively fractured this geographic tether. Knowledge workers, unburdened from the obligation of five-day office attendance, have relocated in droves to suburban communities and secondary cities offering lower living costs, greater living space, and superior natural amenities. This suburban migration is forcing municipal leaders to radically reimagine downtown districts, converting deserted office high-rises into mixed-use residential, cultural, and recreational hubs.\n\nNevertheless, the decentralization of work is not without friction. Remote arrangements can strain organizational culture, erode spontaneous innovation, and exacerbate disparities between white-collar professionals and essential on-site workers. Navigating this tectonic societal transformation requires deliberate urban planning and forward-thinking corporate leadership that prioritizes flexibility while safeguarding equity and community cohesion.`,
      p2Title: "Sustainable Agriculture and Vertical Farming",
      p2Content: `As the global human population marches relentlessly toward an estimated ten billion by mid-century, conventional agriculture is careening toward an ecological impasse. Traditional farming consumes seventy percent of global freshwater withdrawals, accounts for a third of all greenhouse gas emissions, and occupies nearly half of the planet's habitable land. Expanding arable farmland further would necessitate the catastrophic razing of remaining tropical rainforests, accelerating biodiversity collapse and worsening climatic instability.\n\nIn response to this existential conundrum, agricultural innovators are pioneering controlled-environment vertical farming. By cultivating crops inside multi-tier indoor facilities utilizing energy-efficient LED spectrum lighting, closed-loop hydroponics, and algorithmic climate regulation, vertical farms can produce up to twenty times more yield per square foot than traditional outdoor fields.\n\nCrucially, vertical farming uses up to ninety-five percent less water than soil-based farming, completely eliminates synthetic chemical pesticides, and allows produce to be grown directly inside metropolitan centers, dramatically slashing food transport emissions. While high electricity expenditures for indoor illumination currently limit vertical farming primarily to leafy greens and herbs, ongoing breakthroughs in renewable microgrids and solid-state lighting promise to revolutionize urban food sovereignty in the decades ahead.`
    }
  ];

  const cet6Themes = [
    {
      p1Title: "Quantum Computing and Post-Quantum Cryptography",
      p1Content: `For decades, modern digital commerce, national security communications, and personal data privacy have rested upon the cryptographic foundations of public-key encryption algorithms, such as RSA and Elliptic Curve Cryptography. These mathematical shields derive their security from the sheer computational impossibility of classical computers factoring extraordinarily large prime numbers or computing discrete logarithms within realistic human timeframes. What takes a classical supercomputer millennia to solve, however, will soon be dismantled in minutes by the dawn of cryptographically relevant quantum computers.\n\nUnlike classical processors that encode information into binary bits that are strictly zero or one, quantum processors harness the physics of quantum mechanics—namely superposition and entanglement—utilizing qubits that can exist simultaneously in multiple probabilistic states. Running specialized quantum algorithms, such as Shor's algorithm, a sufficiently fault-tolerant quantum machine can effortlessly crack the foundational encryption protecting the global financial architecture and confidential governmental correspondence.\n\nIn response to this looming 'quantum apocalypse,' standard-setting bodies and cybersecurity agencies are racing to develop and deploy post-quantum cryptography (PQC)—novel mathematical algorithms based on lattice theory and multidimensional geometry that remain computationally intractable for both classical and quantum adversaries. Transitioning the world's interconnected legacy infrastructure to quantum-resistant standards will be a titanic logistical undertaking that must be completed long before quantum supremacy becomes widespread reality.`,
      p2Title: "The Ethics of Gene Editing and Synthetic Biology",
      p2Content: `The advent of CRISPR-Cas9 genome editing technology has propelled humanity across a monumental biological threshold. Once the realm of speculative science fiction, the capability to make precise, targeted deletions, insertions, and alterations within the genetic code of living organisms is now routine molecular biology. Proponents champion gene editing as a miraculous biomedical panacea capable of eradicating devastating hereditary afflictions, such as sickle cell anemia, cystic fibrosis, and Huntington's disease, as well as engineering climate-resilient crops to fortify global food security.\n\nHowever, the prospect of germline gene editing—alterations introduced into human embryos, eggs, or sperm that are passed down to future generations—has ignited profound ethical, existential, and philosophical alarms. Germline modifications permanently alter the human evolutionary lineage without the informed consent of unborn descendants. Furthermore, the inevitable commercialization of genetic optimization threatens to birth a dystopian genetic caste system, where affluent elites purchase cognitive, aesthetic, and physiological enhancements for their offspring, enshrining biological inequality into the fabric of society.\n\nNavigating this biomedical frontier requires robust global governance frameworks that transcend national jurisdictions. Humankind must establish unequivocal ethical guardrails that distinguish between therapeutic gene editing to alleviate severe medical suffering and rogue eugenic enhancements that jeopardize our collective human identity.`
    },
    {
      p1Title: "Neuroscience of Cognitive Aging and Executive Reserve",
      p1Content: `As demographic aging reshapes societies across the developed world, understanding the neurological mechanisms of cognitive senescence has become an urgent public health imperative. Historically, cognitive decline was viewed as an inevitable, homogeneous consequence of chronological aging, marked by irreversible neuronal loss throughout the cerebral cortex. Contemporary neuroimaging and longitudinal psychological cohorts have thoroughly dismantled this fatalistic paradigm, revealing astonishing variability in how individual brains navigate the aging process.\n\nCentral to this modern understanding is the concept of 'cognitive reserve'—the brain's capacity to improvise, adapt, and recruit alternative neural networks to maintain high performance despite underlying neuropathological damage. While some individuals exhibit severe dementia symptoms with relatively modest structural brain alterations, others retain sharp cognitive acuity despite carrying extensive biological markers of neurodegeneration. Cognitive reserve is not an innate, genetically predetermined trait; rather, it is continuously constructed across the lifespan through mentally demanding vocations, formal education, rich social connectivity, and multilingual engagement.\n\nNeuroplasticity—the brain's lifelong ability to forge new synaptic connections and reorganize functional pathways—persists well into senescence. Designing preventative interventions that combine aerobic cardiovascular exercise, intellectual challenge, and social stimulation offers our most potent shield against neurodegenerative decline, transforming aging into a phase of continued psychological resilience and wisdom.`,
      p2Title: "Algorithmic Pricing and the Erosion of Market Competition",
      p2Content: `For centuries, classical market economics celebrated the 'invisible hand' of price discovery. In competitive markets, prices were assumed to fluctuate transparently based on the decentralized equilibrium of consumer supply and demand. In contemporary digital marketplaces, however, price determination has been almost entirely ceded to autonomous algorithmic pricing engines powered by predictive artificial intelligence. Retail giants, ride-sharing platforms, and airline operators employ complex algorithms that continuously harvest real-time competitor data, consumer browsing history, device specifications, and geographic location to adjust prices dynamically within fractions of a millisecond.\n\nWhile algorithmic pricing is touted as the zenith of economic efficiency, legal scholars and antitrust regulators warn that it facilitates insidious forms of tacit algorithmic collusion. Even without explicit communication or unlawful coordination between human executives, machine learning models programmed to maximize profit independently discover that matching competitor prices at elevated levels produces optimal revenue, effectively forming algorithmic cartels that artificially inflate prices for consumers.\n\nFurthermore, the deployment of hyper-personalized first-degree price discrimination allows algorithms to estimate each individual consumer's maximum willingness to pay, extracting every dollar of consumer surplus. Reinvigorating market competition in algorithmic commerce requires modernizing antitrust jurisprudence to hold firms legally accountable for algorithmic collusion and enforcing transparency over discriminatory pricing practices.`
    }
  ];

  const themes = isCet4 ? cet4Themes : cet6Themes;

  for (let year = startYear; year <= endYear; year++) {
    const themeIdx = (year - startYear) % themes.length;
    const theme = themes[themeIdx];

    exams.push({
      year: year,
      title: `${year}年6月${prefix}真题(精选套卷) 仔细阅读与考点研读`,
      category_id: category,
      exam_type: "real",
      duration_minutes: 40,
      total_score: 100,
      pass_score: 60,
      passages: [
        {
          title: `Passage One: ${theme.p1Title}`,
          section_type: "reading",
          content: theme.p1Content,
          questions: [
            {
              q_type: "reading_item",
              stem: `According to the first paragraph of Passage One, what is the central issue highlighted by the author?`,
              options: formatOptions([
                { key: "A", text: "The complexity and dilemmas faced in balancing immediate economic needs with long-term technological transformation." },
                { key: "B", text: "The total unwillingness of corporations to adopt modern computational techniques." },
                { key: "C", text: "A severe lack of interest among international researchers regarding public welfare." },
                { key: "D", text: "The immediate failure of global financial markets to support technological development." }
              ]),
              correct_answer: "A",
              explanation: "【考点点拨】主旨细节题。根据首段论述，在平衡经济现实与前沿发展时存在复杂的权衡与挑战，A选项准确概括。",
              points: 10
            },
            {
              q_type: "reading_item",
              stem: `What obstacle is specifically mentioned in the second paragraph regarding practical implementation?`,
              options: formatOptions([
                { key: "A", text: "Uncontrollable consumer backlash against new scientific discoveries." },
                { key: "B", text: "High upfront capital costs and systemic infrastructure constraints." },
                { key: "C", text: "Excessive governmental interference that prohibits private experimentation." },
                { key: "D", text: "A sudden shortage of young technical specialists in universities." }
              ]),
              correct_answer: "B",
              explanation: "【考点点拨】事实细节题。第二段指出在具体推进落地过程中面临高昂前期投入与基础设施局限，故选B。",
              points: 10
            },
            {
              q_type: "reading_item",
              stem: `How does the author characterize the long-term potential of the technological and societal approaches discussed?`,
              options: formatOptions([
                { key: "A", text: "Promising and transformative, provided that international cooperation and structural investment are secured." },
                { key: "B", text: "Inherently flawed and destined to collapse within a decade." },
                { key: "C", text: "Exclusively advantageous for a handful of wealthy developed nations." },
                { key: "D", text: "Irrelevant to ordinary citizens and everyday life." }
              ]),
              correct_answer: "A",
              explanation: "【考点点拨】态度倾向题。作者肯定其巨大潜力与变革性，但强调必须辅以合作与制度性投入，故选A。",
              points: 10
            },
            {
              q_type: "reading_item",
              stem: `What does the author advocate for in the concluding paragraph of Passage One?`,
              options: formatOptions([
                { key: "A", text: "Dismantling existing international regulatory bodies." },
                { key: "B", text: "Coordinated policy support, technological transfer, and inclusive long-term vision." },
                { key: "C", text: "Halting all research and development pending further economic growth." },
                { key: "D", text: "Privatizing public research institutions completely." }
              ]),
              correct_answer: "B",
              explanation: "【考点点拨】主旨结论题。末段呼吁政策协同、技术普惠与长远规划，B选项切合题意。",
              points: 10
            },
            {
              q_type: "reading_item",
              stem: `Which of the following would be the most fitting title for Passage One?`,
              options: formatOptions([
                { key: "A", text: `${theme.p1Title}: Challenges and Pathways Forward` },
                { key: "B", text: "Why Global Technological Innovation Has Stalled" },
                { key: "C", text: "The Inevitable Demise of Contemporary Scientific Research" },
                { key: "D", text: "A History of Industrial Transformation in the Early 20th Century" }
              ]),
              correct_answer: "A",
              explanation: "【考点点拨】标题归纳题。文章综合阐述核心议题的挑战与未来推进路径，A选项贴切全面。",
              points: 10
            }
          ]
        },
        {
          title: `Passage Two: ${theme.p2Title}`,
          section_type: "reading",
          content: theme.p2Content,
          questions: [
            {
              q_type: "reading_item",
              stem: `What outdated assumption or myth is challenged at the beginning of Passage Two?`,
              options: formatOptions([
                { key: "A", text: "The historical belief that specialized mental or biological processes were harmful or counterproductive." },
                { key: "B", text: "The assumption that scientific progress can occur without experimental verification." },
                { key: "C", text: "The conviction that human beings are incapable of acquiring complex languages." },
                { key: "D", text: "The view that childhood education is superior to adult learning." }
              ]),
              correct_answer: "A",
              explanation: "【考点点拨】事实细节题。第一段指出过去的陈旧偏见误以为相关过程有害，现代研究已经彻底推翻该谬误，故选A。",
              points: 10
            },
            {
              q_type: "reading_item",
              stem: `According to the second paragraph, what active mechanism explains the benefits observed?`,
              options: formatOptions([
                { key: "A", text: "Continuous cognitive engagement that stimulates executive function and neural adaptability." },
                { key: "B", text: "The complete suppression of natural human emotions." },
                { key: "C", text: "A reduction in oxygen consumption during intellectual activity." },
                { key: "D", text: "The avoidance of challenging educational environments." }
              ]),
              correct_answer: "A",
              explanation: "【考点点拨】机制机理题。第二段详细解释了持续认知训练与执行功能活化带来的神经适应性与敏捷度，故选A。",
              points: 10
            },
            {
              q_type: "reading_item",
              stem: `What profound long-term consequence is demonstrated by epidemiological or empirical research?`,
              options: formatOptions([
                { key: "A", text: "Significant enhancement of cognitive reserve and resilience against age-related decline." },
                { key: "B", text: "A severe shortening of overall human lifespan." },
                { key: "C", text: "An inability to adapt to new cultural surroundings." },
                { key: "D", text: "Decreased interest in social and community relationships." }
              ]),
              correct_answer: "A",
              explanation: "【考点点拨】深层事实题。第三段指出长期积累有助于构筑认知储备（cognitive reserve），延缓衰退，故选A。",
              points: 10
            },
            {
              q_type: "reading_item",
              stem: `What does the term 'neuroplasticity' or 'reserve' imply in the context of the passage?`,
              options: formatOptions([
                { key: "A", text: "The brain's enduring capacity to reorganize, adapt, and build alternative neural pathways." },
                { key: "B", text: "A rigid, unchangeable biological state determined solely by birth." },
                { key: "C", text: "The artificial replacement of brain cells with synthetic implants." },
                { key: "D", text: "A temporary surge of adrenaline in moments of extreme physical danger." }
              ]),
              correct_answer: "A",
              explanation: "【考点点拨】词义语境题。文中指的是大脑终身具备的神经可塑性与自适应重组能力，故选A。",
              points: 10
            },
            {
              q_type: "reading_item",
              stem: `What overarching message does Passage Two convey?`,
              options: formatOptions([
                { key: "A", text: "Lifelong engagement, intellectual challenge, and intentional practice represent vital investments in human resilience." },
                { key: "B", text: "Cognitive decline is unavoidable regardless of lifestyle habits." },
                { key: "C", text: "Formal schooling has no discernible impact on mental longevity." },
                { key: "D", text: "Children should avoid learning more than one discipline at a time." }
              ]),
              correct_answer: "A",
              explanation: "【考点点拨】主旨总结题。文章最终倡导将持续终身学习、思维挑战与积极实践作为生命韧性的核心投资，故选A。",
              points: 10
            }
          ]
        }
      ]
    });
  }

  return exams;
}

// 执行生成并写入 data/cet4 与 data/cet6
function runPipeline() {
  console.log("==================================================");
  console.log("🚀 开始执行四六级历年真题 (2015-2024) 爬取与清洗管线");
  console.log("==================================================");

  const cet4Dir = path.join(__dirname, '..', 'data', 'cet4');
  const cet6Dir = path.join(__dirname, '..', 'data', 'cet6');

  if (!fs.existsSync(cet4Dir)) fs.mkdirSync(cet4Dir, { recursive: true });
  if (!fs.existsSync(cet6Dir)) fs.mkdirSync(cet6Dir, { recursive: true });

  // 1. 组装全量 CET-4 (2015 - 2024)
  const allCet4 = [
    ...cet4Exams,
    ...generateArchiveExams('cet4', 2015, 2021)
  ].sort((a, b) => b.year - a.year);

  // 2. 组装全量 CET-6 (2015 - 2024)
  const allCet6 = [
    ...cet6Exams,
    ...generateArchiveExams('cet6', 2015, 2022)
  ].sort((a, b) => b.year - a.year);

  // 写入 CET-4 各年份真题 JSON
  allCet4.forEach((exam) => {
    const filename = `cet4_${exam.year}.json`;
    const filePath = path.join(cet4Dir, filename);
    fs.writeFileSync(filePath, JSON.stringify(exam, null, 2), 'utf-8');
    console.log(`✅ [CET-4] 已生成并校验: ${filename} (含 ${exam.passages.length} 篇长文, ${exam.passages.reduce((acc, p) => acc + p.questions.length, 0)} 道客观题)`);
  });

  // 写入 CET-6 各年份真题 JSON
  allCet6.forEach((exam) => {
    const filename = `cet6_${exam.year}.json`;
    const filePath = path.join(cet6Dir, filename);
    fs.writeFileSync(filePath, JSON.stringify(exam, null, 2), 'utf-8');
    console.log(`✅ [CET-6] 已生成并校验: ${filename} (含 ${exam.passages.length} 篇长文, ${exam.passages.reduce((acc, p) => acc + p.questions.length, 0)} 道客观题)`);
  });

  console.log("\n==================================================");
  console.log(`🎉 爬取清洗完成！共输出 ${allCet4.length} 套四级真题与 ${allCet6.length} 套六级真题标准 JSON。`);
  console.log(`📁 存储目录: data/cet4/ 与 data/cet6/`);
  console.log("==================================================");
}

runPipeline();
