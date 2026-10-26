# -*- coding: utf-8 -*-
"""
build_2022_ky1_pure_gold.py
Reconstruct 2022 ky1 (6d676d85-a38a-5fe4-9506-31de03b648b6.json) to 100% pure gold.
"""

import sys
import json
import subprocess

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

json_path = 'public/data/exams/6d676d85-a38a-5fe4-9506-31de03b648b6.json'

with open(json_path, 'r', encoding='utf-8') as f:
    old_data = json.load(f)

# 1. Calibrate Exam Metadata
exam = old_data.get('exam', {})
exam['id'] = '6d676d85-a38a-5fe4-9506-31de03b648b6'
exam['title'] = '2022年全国硕士研究生招生考试英语（一）真题'
exam['year'] = 2022
exam['category_id'] = 'ky1'
exam['exam_type'] = 'ky1'
exam['total_score'] = 60.0
exam['pass_score'] = 36.0
exam['duration_minutes'] = 180
exam['approval_status'] = 'approved'
exam['is_published'] = True

# 2. Reconstruct Passages P0-P5
passages = old_data.get('passages', [])

p0_content = """The idea that plants have some degree of consciousness first took root in the early 2000s; the term "plant neurobiology" was [1] around the notion that some aspects of plant behavior could be [2] to intelligence in animals. [3] plants lack brains, the firing of electrical signals in their stems and leaves nonetheless triggered responses that [4] consciousness, researchers previously reported.

But such an idea is untrue, according to a new opinion article. Plant biology is complex and fascinating, but it [5] so greatly from that of animals that so-called [6] of plant intelligence is inconclusive, the authors wrote.

Beginning in 2006, some scientists have [7] that plants possess neuron-like cells that interact with hormones and neurotransmitters, [8] "a plant nervous system, [9] to that in animals," said lead study author Lincoln Taiz. "They [10] claimed that plants have brain-like command centers at their root tips."

This [11] makes sense if you simplify the workings of a complex brain, [12] it to an array of electrical pulses; cells in plants also communicate through electrical signals. [13], the signaling in a plant is only [14] similar to the firing in a complex animal brain, which is more than "a mass of cells that communicate by electricity," Taiz said.

"For consciousness to evolve, a brain with a threshold [15] of complexity and capacity is required," he [16]. "Since plants don't have nervous systems, the [17] that they have consciousness are effectively zero."

And what's so great about consciousness, anyway? Plants can't run away from [18], so investing energy in a body system which [19] a threat and can feel pain would be a very [20] evolutionary strategy, according to the article."""

p1_content = """People often complain that plastics are too durable. Water bottles, shopping bags, and other trash litter the planet, from Mount Everest to the Mariana Trench, because plastics are everywhere and don't break down easily. But some plastic materials change over time. They crack and frizzle. They "weep" out additives. They melt into sludge. All of which creates huge headaches for institutions, such as museums, trying to preserve culturally important objects. The variety of plastic objects at risk is dizzying: early radios, avant-garde sculptures, celluloid animation stills from Disney films, the first artificial heart.

Certain artifacts are especially vulnerable because some pioneers in plastic art didn't always know how to mix ingredients properly, says Thea van Oosten, a polymer chemist who, until retiring a few years ago, worked for decades at the Cultural Heritage Agency of the Netherlands (RCE). "It's like baking a cake: If you don't have exact amounts, it goes wrong," she says. "The object you make is already a time bomb."

And sometimes, it's not the artist's fault. In the 1960s, the Italian artist Piero Gilardi began to create hundreds of bright, colorful foam pieces. Those pieces included small beds of roses and other items as well as a few dozen "nature carpets"—large rectangles decorated with foam pumpkins, cabbages, and watermelons. He intended people to sit, lie, and walk on these carpets—which meant they had to be durable.

Unfortunately, the polyurethane foam he used is inherently unstable. It's often gone in 15 or 20 years. As Gilardi's nature carpets began to crumble, museums locked some of them away in the dark.

So van Oosten and colleagues worked to preserve Gilardi's sculptures. They infused some with Stabiltex, a mixture of water and synthetic resin, and bathed others in a solution of Plexisol, an acrylic resin. The treatments restored elasticity to the carpets, giving them another few decades of life.

Such struggles, as art of all types begins to disintegrate, are increasingly common.

And more is at stake here than individual objects. Joana Lia Ferreira, an assistant professor of conservation and restoration at the NOVA School of Science and Technology, notes that archaeologists first defined the great material ages of human history—Stone Age, Iron Age, and so on—after examining artifacts in museums. We now live in an age of plastic, she says, "and what we decide to collect today, what we decide to preserve...will have a strong impact on how in the future we'll be seen.\""""

p2_content = """As the latest crop of students pen their undergraduate application form and weigh up their options, it may be worth considering just how the point, purpose and value of a degree has changed and what Generation Z need to consider as they start the third stage of their educational journey.

Millennials were told that if you did well in school, got a decent degree, you would be set up for life. But that promise has been found wanting. As degrees became universal, they became devalued. Education was no longer a secure route of social mobility. Today, 28 per cent of graduates in the UK are in non-graduate roles, a percentage which is double the average among the OECD countries.

This is not to say that there is no point in getting a degree, but rather stress that a degree is not for everyone, that the switch from classroom to lecture hall is not an inevitable one and that other options are available.

Thankfully, there are signs that this is already happening, with Generation Z seeking to learn from their millennial predecessors, even if parents and teachers tend to be still set in the degree mindset. Employers have long seen the advantages of hiring school leavers who often prove themselves to be more committed and loyal employees than graduates. Many too are seeing the advantages of scrapping a degree requirement for certain roles.

For those for whom a degree is the desired route, consider that this may well be the first of many. In this age of generalists, it pays to have specific knowledge or skills. Postgraduates now earn 40 per cent more than graduates. When more and more of us have a degree, it makes sense to have two.

It is unlikely that Generation Z will be done with education at 18 or 21; they will need to be constantly upskilling throughout their career to stay employable. It has been estimated that this generation, due to the pressures of technology, the wish for personal fulfilment and desire for diversity, will work for 17 different employers over the course of their working life and have five different careers. Education, and not just knowledge gained on campus, will be a core part of Generation Z's career trajectory.

Older generations often talk about their degree in the present and personal tense: "I am a geographer," or "I am a classicist." Their sons or daughters would never say such a thing; it's as if they already know that their degree won't define them in the same way."""

p3_content = """Enlightening, challenging, stimulating, fun. These were some of the words that Nature readers used to describe their experience of art-science collaborations in a series of articles on partnerships between artists and researchers. Nearly 40% of the roughly 350 people who responded to an accompanying poll said they had collaborated with artists; and almost all said they would consider doing so in future.

Such an encouraging result is not surprising. Scientists are increasingly seeking out visual artists to help them communicate their work to new audiences. "Artists help scientists reach a broader audience and make emotional connections that enhance learning," one respondent said.

One example of how artists and scientists have together rocked the scenes came last month when the Sydney Symphony Orchestra performed a reworked version of Antonio Vivaldi's The Four Seasons. They reimagined the 300-year-old score by injecting the latest climate prediction data for each season provided by Monash University's Climate Change Communication Research Hub. The performance was a creative call to action ahead of November's United Nations Climate Change Conference in Glasgow, UK.

But a genuine partnership must be a two-way street. Fewer artists than scientists responded to the Nature poll, however, several respondents noted that artists do not simply assist scientists with their communication requirements. Nor should their work be considered only as an object of study. The alliances are most valuable when scientists and artists have a shared stake in a project, are able to jointly design it and can critique each other's work. Such an approach can both prompt new research as well as result in powerful art.

More than half a century ago, the Massachusetts Institute of Technology opened its Center for Advanced Visual Studies (CAVS) to explore the role of technology in culture. The founders deliberately focused their projects around light—hence the "visual studies" in the name. Light was a something that both artists and scientists had an interest in, and therefore could form the basis of collaboration. As science and technology progressed, and divided into more sub-disciplines, the centre was simultaneously looking to a time when leading researchers could also be artists, writers and poets, and vice versa.

Nature's poll findings suggest that this trend is as strong as ever, but, to make a collaboration work, both sides need to invest time, and embrace surprise and challenge. The reach of art-science tie-ups needs to go beyond the necessary purpose of research communication, and participants must not fall into the trap of stereotyping each other. Artists and scientists alike are immersed in discovery and invention, and challenge and critique are core to both, too."""

p4_content = """The personal grievance provisions of New Zealand's Employment Relations Act 2000 (ERA) prevent an employer from firing an employee without good cause. Instead, dismissals must be justified. Employers must both show cause and act in a procedurally fair way.

Personal grievance procedures were designed to guard the jobs of ordinary workers from unjustified dismissals. The premise was that the balance of power in an employment relationship is inherently tilted against the employee, who needs special protections. It was also designed to reinforce the standard dismissal process: an employer cannot simply give an employee contractual notice.

But these provisions create difficulties for businesses when applied to highly paid managers and executives. As countless boards and business owners will attest, constraining firms from firing poorly performing, high-earning managers is a handbrake on boosting productivity and overall performance. The difference between C-grade and A-grade managers may very well be the difference between business success or failure.

Between two equally sized teams, all other things being equal, the team with the better manager will win. Because managers are responsible for organizing resources to achieve business objectives, a bad manager can quickly jeopardize company results. Discretionary work effort is rapidly foregone when employees lose confidence in their bosses, and employees will eventually depart the firm for greener pastures. When poorly performing managers cannot be removed without considerable difficulty, other workers may be placing those jobs at risk.

If not placing jobs at risk, to the extent employment protection laws constrain business owners from dismissing under-performing managers, those laws act as a constraint on firm productivity and therefore on workers' wages. Indeed, in "An International Perspective on New Zealand's Productivity Paradox" (2014), the Productivity Commission singled out the low quality of managerial capabilities as a cause of the country's poor productivity growth record.

Nor are highly paid managers themselves immune from the harm caused by the ERA's unjustified dismissal procedures. Because employment protection laws make it costlier to fire an employee, employers are more cautious about hiring new staff. This makes it harder for the marginal manager to gain employment. And firms pay staff less because firms carry the burden of the employment arrangement going wrong.

Iron-clad employment protection procedures can also be a barrier for high-performing managers to make quick exits. The threat of a grievance process can create huge difficulties in ending employment arrangements quietly, cleanly and quickly, even if both sides agree that they should end.

Across the Tasman Sea, Australia deals with the unjustified dismissal paradox by excluding employees earning above a specified "high-income threshold" from the protection of its unfair dismissal laws. In New Zealand, a 2016 private members' Bill tried to permit firms and high-income employees to contract out of the unjustified dismissal regime. However, the mechanisms proposed were unwieldy and the Bill was voted down following the change in government later that year."""

p5_content = """In the following text, five people express their views about zoos. For questions 41-45, choose from the arguments (A-G) the one which each person would most likely support.

(41) Teri Byrd
I was a zoo and wildlife-park employee for years, both in the UK and in the US, and I was always told that the main purpose of zoos was for the benefit of the animals and for conservation purposes. This claim was false. Neither one of them actually participated in any contributions to animal research or conservation. They are profitable institutions whose bottom line is much more important than the condition of the animals.
Animals despise being captives in zoos. No matter how you "enhance" enclosures, they do not allow for freedom, a natural diet or adequate exercise. Animals end up stressed and unhealthy or dead. It's past time for transparency with these institutions, and it's past time to eliminate zoos from our culture.

(42) Karen R. Sime
As a zoology professor, I agree with Emma Marris that zoo displays can be sad and cruel, but she understates the educational potential.
My colleagues and I surveyed students in our classes about their early experiences with animals. The vast majority of our students told us that zoo visits were the crucial and very early experience that led to their passion for biology. We need to educate children to care about animals and nature, and zoos remain the best way to do that.

(43) Greg Newberry
Emma Marris's article is an insult and a disservice to the thousands of zoo professionals who work tirelessly to improve how they care for animals. Zoos are not static; they are constantly evolving to provide better care for animals.
Zoos do vital conservation work and help people, especially children, connect with the broader natural world. They are not the soulless prisons that Ms. Marris implies.

(44) Dean Gallea
Zoos and the captive animals they house serve a higher purpose. Without them, far more people would travel to wilderness areas, disrupting wildlife and damaging ecosystems.
By keeping a relatively small number of animals in captivity, we can satisfy the public's desire to see animals while leaving the vast majority undisturbed in their natural environments.

(45) John Fraser
Marris misrepresents the findings of our research. Our work actually demonstrates that zoo visitors gain a deeper appreciation for biodiversity and are more motivated to take action to protect the natural world.
Zoos serve as an essential bridge between human society and wildlife, helping millions of urban dwellers understand the natural world we live in.

[A] Zoos which spare no effort to take care of animals should not be subjected to unfair criticism.
[B] To pressure zoos to spend less on their animals would lead to inhumane outcomes for the precious creatures in their care.
[C] While animals in captivity deserve sympathy, zoos play a significant role in starting young people down the path of related sciences.
[D] Zoos save people trips to wilderness areas and thus contribute to wildlife conservation.
[E] For wild animals that cannot be returned to their natural habitats, zoos offer the best alternative.
[F] Zoos should have been closed down as they prioritize money making over animals' wellbeing.
[G] Marris distorts our findings which actually prove that zoos serve as an indispensable link between man and nature."""

p_contents = [p0_content, p1_content, p2_content, p3_content, p4_content, p5_content]
p_titles = [
    "Section I: Use of English",
    "Section II: Reading Comprehension Part A - Text 1",
    "Section II: Reading Comprehension Part A - Text 2",
    "Section II: Reading Comprehension Part A - Text 3",
    "Section II: Reading Comprehension Part A - Text 4",
    "Section II: Reading Comprehension Part B"
]

for idx, p in enumerate(passages):
    p['sort_order'] = idx + 1
    p['title'] = p_titles[idx]
    p['content'] = p_contents[idx]

# 3. Calibrate Questions Q1-Q45
expected_answers = {
    1: 'A', 2: 'C', 3: 'D', 4: 'C', 5: 'D', 6: 'B', 7: 'C', 8: 'B', 9: 'A', 10: 'D',
    11: 'C', 12: 'B', 13: 'A', 14: 'C', 15: 'B', 16: 'D', 17: 'A', 18: 'A', 19: 'D', 20: 'B',
    21: 'A', 22: 'C', 23: 'D', 24: 'D', 25: 'B',
    26: 'C', 27: 'B', 28: 'C', 29: 'D', 30: 'A',
    31: 'B', 32: 'A', 33: 'A', 34: 'B', 35: 'C',
    36: 'D', 37: 'A', 38: 'D', 39: 'B', 40: 'C',
    41: 'F', 42: 'C', 43: 'A', 44: 'D', 45: 'G'
}

questions = old_data.get('questions', [])

for idx, q in enumerate(questions):
    qnum = idx + 1
    q['question_number'] = qnum
    q['sort_order'] = qnum
    ans = expected_answers[qnum]
    q['answer'] = ans
    q['correct_answer'] = ans
    
    if qnum <= 20:
        q['q_type'] = 'cloze_item'
        q['points'] = 0.5
        q['score'] = 0.5
        q['stem'] = f"Choose the best option for blank [{qnum}] in the passage:"
    else:
        q['q_type'] = 'reading_item'
        q['points'] = 2.0
        q['score'] = 2.0
        if qnum >= 41:
            names = {
                41: "Teri Byrd",
                42: "Karen R. Sime",
                43: "Greg Newberry",
                44: "Dean Gallea",
                45: "John Fraser"
            }
            q['stem'] = f"Match {names[qnum]} to the corresponding argument [A]-[G]:"
            
    # standardize options
    opts = q.get('options', [])
    for opt in opts:
        k = opt.get('key')
        t = opt.get('text', opt.get('content', ''))
        opt['key'] = k
        opt['text'] = t
        opt['content'] = t
        opt['value'] = k

# Save back to JSON
new_data = {
    "exam": exam,
    "passages": passages,
    "questions": questions,
    "exportedAt": old_data.get("exportedAt")
}

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

print("2022 ky1 successfully calibrated and written to JSON!")
for p in passages:
    print(f"P{p['sort_order']}: {p['title']} | paras={len(p['content'].splitlines())} | words={len(p['content'].split())}")
