# -*- coding: utf-8 -*-
"""
build_2020_ky1_gold_engine.py
Constructs the 100% authentic golden JSON for 2020 ky1:
- Exam metadata normalized: 60.0 score, 36.0 pass_score, 180 min, approved, published.
- 6 Passages (P0-P5) completely reconstructed:
  * P0: Cloze (4 paragraphs, 275 words)
  * P1: Text 1 (4 paragraphs, 435 words, clean of Text 2 pollution)
  * P2: Text 2 (7 paragraphs, 447 words)
  * P3: Text 3 (10 paragraphs, 380 words, clean of question pollution)
  * P4: Text 4 (6 paragraphs, 436 words, complete with paragraph VI)
  * P5: Part B (6 paragraphs, 540 words, eye contact research)
- 45 Questions (Q1-Q45):
  * question_number: 1..45
  * sort_order: 1..45
  * score / points: 0.5 for Q1-Q20, 2.0 for Q21-Q45
  * question_type: 'cloze_item' / 'reading_item'
  * answer == correct_answer == official answer key
  * options complete with keys and authentic text
  * three-tier explanations formatted in clean Markdown
"""

import re
import sys
import json
import os

sys.stdout.reconfigure(encoding='utf-8')

# 1. Load existing JSON to preserve IDs
json_path = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\f56943c1-0ba8-58fe-b7d3-061352345067.json"
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

exam_id = "f56943c1-0ba8-58fe-b7d3-061352345067"

# 2. Reconstruct Passages
passages_p0 = """Even if families don't sit down to eat together as frequently as before, millions of Britons will nonetheless have got a share this weekend of one of the nation's great traditions: the Sunday roast. [1] a cold winter's day, few culinary pleasures can [2] it. Yet as we report now, the food police are determined that this [3] should be rendered yet another guilty pleasure [4] to damage our health.

The Food Standards Authority (FSA) has [5] a public warning about the risks of a compound called acrylamide that forms in some foods cooked [6] high temperatures. This means that people should [7] crisping their roast potatoes, reject thin-crust pizzas and only [8] toast their bread. But where is the evidence to support such alarmist advice? [9] studies have shown that acrylamide can cause neurological damage in mice, there is no [10] evidence that it causes cancer in humans.

Scientists say the compound is [11] to cause cancer but have no hard scientific proof. [12] the precautionary principle, it could be argued that it is [13] to follow the FSA advice. [14], it was rumoured that smoking caused cancer for years before the evidence was found to prove a [15].

Doubtless a piece of boiled beef can always be [16] up on Sunday alongside some steamed vegetables, without the Yorkshire pudding and no wine. But would life be worth living? [17], the FSA says it is not telling people to cut out roast foods [18], but to reduce their lifetime intake. However, their [19] risks coming across as being pushy and overprotective. Constant health scares just [20] with no one listening."""

passages_p1 = """A group of Labour MPs, among them Yvette Cooper, are bringing in the new year with a call to institute a UK "town of culture" award. The proposal is that it should sit alongside the existing city of culture title, which was held by Hull in 2017, and has been awarded to Coventry for 2021. Cooper and her colleagues argue that the success of the crown for Hull, where it brought in £220m of investment and an avalanche of arts, ought not to be confined to cities. Britain's towns, it is true, are not prevented from applying, but they generally lack the resources to put together a bid to beat their bigger competitors. A town of culture award could, it is argued, become an annual event, attracting funding and creating jobs.

Some might see the proposal as a booby prize for the fact that Britain is no longer able to apply for the much more prestigious title of European capital of culture, a sought-after award bagged by Glasgow in 1990 and Liverpool in 2008. A cynic might speculate that the UK is on the verge of disappearing into an endless fever of self-celebration in its desperation to reinvent itself for the post-Brexit world: after town of culture, who knows what will follow—village of culture? Suburb of culture? Hamlet of culture?

It is also wise to recall that such titles are not a cure-all. A badly run "year of culture" washes in and washes out of a place like the tide, bringing prominence for a spell but leaving no lasting benefits to the community. The really successful holders of such titles are those that do a great deal more than fill hotel bedrooms and bring in high-profile arts events and good press for a year. They transform the aspirations of the people who live there; they nudge the self-image of the city into a bolder and more optimistic light. It is hard to get right, and requires a remarkable degree of vision, as well as cooperation between city authorities, the private sector, community groups and cultural organisations. But it can be done: Glasgow's year as European capital of culture can certainly be seen as one of a complex series of factors that have turned the city into the powerhouse of art, music and theatre that it remains today.

A "town of culture" could be not just about the arts but about honouring a town's peculiarities—helping sustain its high street, supporting local facilities and above all celebrating its people. Jeremy Wright, the culture secretary, should welcome this positive, hope-filled proposal, and turn it into action."""

passages_p2 = """Scientific publishing has long been a licence to print money. Scientists need journals in which to publish their research, so they will supply the articles without monetary reward. Other scientists perform the specialised work of peer review also for free, because it is a central element in the acquisition of status and the production of scientific knowledge.

With the content of papers secured for free, the publisher needs only find a market for its journal. Until this century, university libraries were not very price sensitive. Scientific publishers routinely report profit margins approaching 40% on their operations, at a time when the rest of the publishing industry is in an existential crisis.

The Dutch giant Elsevier, which claims to publish 25% of the scientific papers produced in the world, made profits of more than £900m last year, while UK universities alone spent more than £210m in 2016 to enable researchers to access their own publicly funded research; both figures seem to rise unstoppably despite increasingly desperate efforts to change them.

The most drastic, and thoroughly illegal, reaction has been the emergence of Sci-Hub, a kind of global photocopier for scientific papers, set up in 2012, which now claims to offer access to every paywalled article published since 2015. The success of Sci-Hub, which relies on researchers passing on copies they have themselves legally accessed, shows the legal ecosystem has lost legitimacy among its users and must be transformed so that it works for all participants.

In Britain the move towards open access publishing has been driven by funding bodies. In some ways it has been very successful. More than half of all British scientific research is now published under open access terms: either freely available from the moment of publication, or paywalled for a year or more so that the publishers can make a profit before being placed on general release.

Yet the new system has not yet worked out any cheaper for the universities. Publishers have responded to the demand that they make their product free to readers by charging their writers fees to cover the costs of preparing an article. These range from around £500 to $5,000, and apparently the work gets more expensive the more that publishers do it. A report last year pointed out that the costs both of subscriptions and of these "article preparation costs" had been steadily rising at a rate above inflation.

In some ways the scientific publishing model resembles the economy of the social internet: labour is provided free in exchange for the hope of status, while huge profits are made by a few big firms who run the market places. In both cases, we need a rebalancing of power."""

passages_p3 = """Progressives often support diversity mandates as a path to equality and a way to level the playing field. But all too often such policies are an insincere form of virtue-signaling that benefits only the most privileged and does little to help average people.

A pair of bills sponsored by Massachusetts state Senator Jason Lewis and House Speaker Pro Tempore Patricia Haddad, to ensure "gender parity" on boards and commissions, provide a case in point.

Haddad and Lewis are concerned that more than half the state-government boards are less than 40 percent female. In order to ensure that elite women have more such opportunities, they have proposed imposing government quotas. If the bills become law, state boards and commissions will be required to set aside 50 percent of board seats for women by 2022.

The bills are similar to a measure recently adopted in California, which last year became the first state to require gender quotas for private companies. In signing the measure, California Governor Jerry Brown admitted that the law, which expressly classifies people on the basis of sex, is probably unconstitutional.

The US Supreme Court frowns on sex-based classifications unless they are designed to address an "important" policy interest. Because the California law applies to all boards, even where there is no history of prior discrimination, courts are likely to rule that the law violates the constitutional guarantee of "equal protection".

But are such government mandates even necessary? Female participation on corporate boards may not currently mirror the percentage of women in the general population, but so what?

The number of women on corporate boards has been steadily increasing without government interference. According to a study by Catalyst, between 2010 and 2015 the share of women on the boards of global corporations increased by 54 percent.

Requiring companies to make gender the primary qualification for board membership will inevitably lead to less experienced private sector boards. That is exactly what happened when Norway adopted a nationwide corporate gender quota.

Writing in The New Republic, Alice Lee notes that increasing the number of opportunities for board membership without increasing the pool of qualified women to serve on such boards has led to a "golden skirt" phenomenon, where the same elite women scoop up multiple seats on a variety of boards.

Next time somebody pushes corporate quotas as a way to promote gender equity, remember that such policies are largely self-serving measures that make their sponsors feel good but do little to help average women."""

passages_p4 = """Last Thursday, the French Senate passed a digital services tax, which would impose an entirely new tax on large multinationals that provide digital services to consumers or users in France. Digital services include everything from providing a platform for selling goods and services online to targeting advertising based on user data, and the tax applies to gross revenue from such services. Many French politicians and media outlets have referred to this as a "GAFA tax," meaning that it is designed to apply primarily to companies such as Google, Apple, Facebook and Amazon—in other words, multinational tech companies based in the United States.

The digital services tax now awaits the signature of President Emmanuel Macron, who has expressed support for the measure, and it could go into effect within the next few weeks. But it has already sparked significant controversy, with the United States trade representative opening an investigation into whether the tax discriminates against American companies, which in turn could lead to trade sanctions against France.

The French tax is not just a unilateral move by one country in need of revenue. Instead, the digital services tax is part of a much larger trend, with countries over the past few years proposing or putting in place an alphabet soup of new international tax provisions. They have included Britain's DPT (diverted profits tax), Australia's MAAL (multinational anti-avoidance law), and India's SEP (significant economic presence) test, to name but a few. At the same time, the European Union, Spain, Britain and several other countries have all seriously contemplated digital services taxes.

These unilateral developments differ in their specifics, but they are all designed to tax multinationals on income and revenue that countries believe they should have a right to tax, even if international tax rules do not grant them that right. In other words, they all share a view that the international tax system has failed to keep up with the current economy.

In response to these many unilateral measures, the Organization for Economic Cooperation and Development (OECD) is currently working with 131 countries to reach a consensus by the end of 2020 on an international solution. Both France and the United States are involved in the organization's work, but France's digital services tax and the American response raise questions about what the future holds for the international tax system.

France's planned tax is a clear warning: Unless a broad consensus can be reached on reforming the international tax system, other nations are likely to follow suit, and American companies will face a cascade of different taxes from dozens of nations that will prove burdensome and costly."""

passages_p5 = """In a social situation, eye contact with another person can show that you are paying attention in a friendly way. But it can also be antagonistic, such as when a political candidate turns toward their competitor during a debate and makes eye contact that signals hostility. Here's what hard science reveals about eye contact:

[41] ____________________
We know that a typical infant will instinctively gaze into its mother's eyes, and she will look back. This mutual gaze is a major part of the attachment between mother and child. In adulthood, looking at someone else in a pleasant way can be a complimentary sign of paying attention. It can catch someone's attention in a crowded room. "Eye contact and smile" can signal availability and confidence, a common-sense notion supported in studies by psychologist Monica Moore.

[42] ____________________
Neuroscientist Bonnie Auyeung found that the hormone oxytocin increased the amount of eye contact from men toward the interviewer during a brief interview when the direction of their gaze was recorded. This was also found in high-functioning men with some autistic spectrum symptoms, who may tend to avoid eye contact. Specific brain regions that respond during direct gaze are being explored by other researchers, using advanced methods of brain scanning.

[43] ____________________
With the use of eye-tracking technology, Julia Minson of the Harvard Kennedy School of Government concluded that eye contact can signal very different kinds of messages, depending on the situation. While eye contact may be a sign of connection or trust in friendly situations, it's more likely to be associated with dominance or intimidation in adversarial situations. "Whether you're a politician or a parent, it might be helpful to keep in mind that trying to maintain eye contact may backfire if you're trying to convince someone who has a different set of beliefs than you," said Minson.

[44] ____________________
When we look at a face or a picture, our eyes pause on one spot at a time, often on the eyes or mouth. These pauses typically occur at about three per second, and the eyes then jump to another spot, until several important points in the image are registered like a series of snapshots. How the whole image is then assembled and perceived is still a mystery although it is the subject of current research.

[45] ____________________
In people who score high in a test of neuroticism, a personality dimension associated with self-consciousness and anxiety, eye contact triggered more activity associated with avoidance, according to the Finnish researcher Jari Hietanen and colleagues. "Our findings indicate that people do not only feel different when they are the centre of attention but that their brain reactions also differ." A more direct finding is that people who scored highly for negative emotions like anxiety looked at others for shorter periods of time and reported more comfortable feelings when others did not look directly at them."""

passage_contents = [passages_p0, passages_p1, passages_p2, passages_p3, passages_p4, passages_p5]
passage_titles = [
    "Section I: Use of English",
    "Section II: Reading Comprehension Part A - Text 1",
    "Section II: Reading Comprehension Part A - Text 2",
    "Section II: Reading Comprehension Part A - Text 3",
    "Section II: Reading Comprehension Part A - Text 4",
    "Section II: Reading Comprehension Part B"
]
passage_types = ["use_of_english", "reading", "reading", "reading", "reading", "reading"]

for i, p in enumerate(exam_data['passages']):
    p['title'] = passage_titles[i]
    p['content'] = passage_contents[i]
    p['text'] = passage_contents[i]
    p['sort_order'] = i + 1
    p['passage_type'] = passage_types[i]
    p['section_type'] = 'cloze' if i == 0 else 'reading'

# 3. Read dump text for explanations
with open(r"d:\A16pro\Aing\antigravity\supabase\scripts\2020_ky1_dump.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Font & typo replacements
raw_text = re.sub(r'---\s*PAGE\s*\d+\s*---', '', raw_text)
raw_text = re.sub(r'(?:^|\n)\s*&\s*\[A\]', '\n8. [A]', raw_text)
raw_text = re.sub(r'(?:^|\n)\s*11\.\s*EA\]', '\n11. [A]', raw_text)
raw_text = re.sub(r'(?:^|\n)\s*1&\s*［A］', '\n18. ［A］', raw_text)
raw_text = re.sub(r'21\s*・\s*Cooper and her colleagues argue that a 41 town of\s*culture" award could\s*・',
                  '21. Cooper and her colleagues argue that a "town of culture" award could _______.', raw_text)
raw_text = re.sub(r'2&\s*How does', '28. How does', raw_text)
raw_text = re.sub(r'36\.\s*The French Senate has passed a hill to\s*・',
                  '36. The French Senate has passed a bill to _______.', raw_text)

def clean_section(text):
    text = re.sub(r'•词汇注释.*', '', text, flags=re.DOTALL)
    text = re.sub(r'•语篇分析.*', '', text, flags=re.DOTALL)
    text = re.sub(r'三、语篇分析.*', '', text, flags=re.DOTALL)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# Format explanation
def format_expl(raw_expl):
    # Standardize tags
    raw_expl = re.sub(r'[\[［]考点提炼[\]］]', '\n\n### ［考点提炼］\n', raw_expl)
    raw_expl = re.sub(r'[\[［]解题思路[\]］]', '\n\n### ［解题思路］\n', raw_expl)
    raw_expl = re.sub(r'[\[［]精准定位[\]］]', '\n\n### ［精准定位］\n', raw_expl)
    raw_expl = re.sub(r'[\[［]命题解密[\]］]', '\n\n### ［命题解密］\n', raw_expl)
    raw_expl = re.sub(r'[\[［]错项排除[\]］]', '\n\n### ［错项排除］\n', raw_expl)
    raw_expl = re.sub(r'[\[［]技巧总结[\]］]', '\n\n### ［技巧总结］\n', raw_expl)
    raw_expl = re.sub(r'[\[［]精解[\]］]', '\n\n### ［精解］\n', raw_expl)
    raw_expl = re.sub(r'[\[［]干扰项设置[\]］]', '\n\n### ［干扰项设置］\n', raw_expl)
    raw_expl = re.sub(r'•词汇注释与难句分析.*', '', raw_expl, flags=re.DOTALL)
    raw_expl = re.sub(r'•语篇分析.*', '', raw_expl, flags=re.DOTALL)
    raw_expl = re.sub(r'三、语篇分析.*', '', raw_expl, flags=re.DOTALL)
    raw_expl = re.sub(r'二、语篇分析.*', '', raw_expl, flags=re.DOTALL)
    raw_expl = re.sub(r'\n{3,}', '\n\n', raw_expl)
    return raw_expl.strip()

# Cloze answers & options
cloze_data = [
    ("C", [("A", "In"), ("B", "Towards"), ("C", "On"), ("D", "Till")]),
    ("A", [("A", "match"), ("B", "express"), ("C", "satisfy"), ("D", "influence")]),
    ("B", [("A", "patience"), ("B", "enjoyment"), ("C", "surprise"), ("D", "concern")]),
    ("D", [("A", "intensified"), ("B", "privileged"), ("C", "compelled"), ("D", "guaranteed")]),
    ("A", [("A", "issued"), ("B", "received"), ("C", "ignored"), ("D", "cancelled")]),
    ("B", [("A", "under"), ("B", "at"), ("C", "for"), ("D", "by")]),
    ("D", [("A", "forget"), ("B", "regret"), ("C", "finish"), ("D", "avoid")]),
    ("A", [("A", "partially"), ("B", "regularly"), ("C", "easily"), ("D", "initially")]),
    ("D", [("A", "Unless"), ("B", "Since"), ("C", "If"), ("D", "While")]),
    ("C", [("A", "secondary"), ("B", "external"), ("C", "conclusive"), ("D", "negative")]),
    ("C", [("A", "insufficient"), ("B", "bound"), ("C", "likely"), ("D", "slow")]),
    ("A", [("A", "On the basis of"), ("B", "At the cost of"), ("C", "In addition to"), ("D", "In contrast to")]),
    ("B", [("A", "interesting"), ("B", "advisable"), ("C", "urgent"), ("D", "fortunate")]),
    ("D", [("A", "As usual"), ("B", "In particular"), ("C", "By definition"), ("D", "After all")]),
    ("C", [("A", "resemblance"), ("B", "combination"), ("C", "connection"), ("D", "pattern")]),
    ("B", [("A", "made"), ("B", "served"), ("C", "saved"), ("D", "used")]),
    ("A", [("A", "To be fair"), ("B", "For instance"), ("C", "To be brief"), ("D", "In general")]),
    ("B", [("A", "reluctantly"), ("B", "entirely"), ("C", "gradually"), ("D", "carefully")]),
    ("C", [("A", "promise"), ("B", "experience"), ("C", "campaign"), ("D", "competition")]),
    ("D", [("A", "follow up"), ("B", "pick up"), ("C", "open up"), ("D", "end up")])
]

# Extract Cloze explanations
cloze_expls = {}
for q in range(1, 21):
    m = re.search(rf'(?:^|\n)\s*{q}\.\s*(?:\[A\]|［A］).*?(?=(?:^|\n)\s*(?:{q+1}\.|\bII\b|\b111\b|\bIV\b|•词汇注释|•语篇分析|Part A|$))', raw_text, re.DOTALL)
    if m:
        block = m.group(0).strip()
        expl_idx = block.find('[考点提炼]')
        if expl_idx == -1: expl_idx = block.find('［考点提炼］')
        expl = block[expl_idx:].strip() if expl_idx != -1 else ""
        cloze_expls[q] = format_expl(expl)
    else:
        cloze_expls[q] = ""

# Reading Q21-Q40 definitions
from verify_reading_definitions import questions_21_40

reading_expls = {}
for item in questions_21_40:
    q = item['qnum']
    if q == 31:
        # Special case for Q31 due to PDF block layout
        q31_text = """### ［精准定位］
本题考查作者对两项麻州法案的看法，可定位至第二、三段，发现两项法案意在确保各委员会中的“性别平等”（即：减少性别偏见）。而两项法案为对首段②句作者观点“此类政策往往是一种虚伪的道德信号，仅有利于最有特权者，却无益于普通人”的例证。可见作者认为，法案并不能如发起人所言减少性别偏见，［A］正确。

### ［命题解密］
正确项［A］契合首段作者对此类政策的评价：虽宣称可实现平等、促进公平竞争（a path to equality and a way to level the playing field），实则仅有利于最有特权者，却无助于普通人（benefits only the most privileged and does little to help average people）。

### ［错项排除］
［B］从第二段“法案旨在确保性别平等”和第三段①句“州政府委员会中女性成员明显少于男性”主观推出“法案对州政府构成威胁”，但文中并未提及此因果关联。
［C］基于惯性思维，由第三段③句所述法案内容“要求州内各类委员会留出50%的席位给女性”过度推断出女性在政界的地位将会提高。
［D］将第三段②句ensure that elite women have more such opportunities（确保精英女性有更多机会进入政府委员会）曲解为“大大拓宽了人们的职业选择”。

### ［技巧总结］
本题明为考查作者观点，暗中考查例证关系。解题关键在于意识到第二、三段事例是对第一段观点的例证，并厘清第一段中的作者观点：先由第二段A pair of bills... provide a case in point可知例证关系，判断正确项应体现第一段作者主要观点。再根据第一段Progressives often support... But all too often such policies...明确作者态度：此类政策并不能实现平等，反而强化特权。"""
        reading_expls[31] = q31_text.strip()
        continue

    m = re.search(rf'(?:^|\n)\s*{q}\.\s*([A-Z].*?)(?=(?:^|\n)\s*(?:{q+1}\.|\bText\s+\d|\bPart\s+B|•词汇注释|三、语篇分析|•语篇分析|$))', raw_text, re.DOTALL)
    if m:
        block = m.group(0).strip()
        expl_idx = -1
        for kw in ['［精准定位］', '[精准定位]', '［命题解密］', '[命题解密]']:
            pos = block.find(kw)
            if pos != -1 and (expl_idx == -1 or pos < expl_idx):
                expl_idx = pos
        expl = block[expl_idx:].strip() if expl_idx != -1 else ""
        reading_expls[q] = format_expl(expl)
    else:
        reading_expls[q] = ""

# Part B Q41-Q45
partb_opts = [
    {"key": "A", "content": "Eye fixations are brief"},
    {"key": "B", "content": "Too much eye contact is instinctively felt to be rude"},
    {"key": "C", "content": "Eye contact can be a friendly social signal"},
    {"key": "D", "content": "Personality can affect how a person reacts to eye contact"},
    {"key": "E", "content": "Biological factors behind eye contact are being investigated"},
    {"key": "F", "content": "Most people are not comfortable holding eye contact with strangers"},
    {"key": "G", "content": "Eye contact can also be aggressive"}
]

partb_answers = {41: "C", 42: "E", 43: "G", 44: "A", 45: "D"}
partb_expls = {}
for q in range(41, 46):
    m = re.search(rf'{q}\.\s*［答案］([A-G])\s*［精解］(.*?)(?=(?:\d+\.\s*［答案］|$))', raw_text, re.DOTALL)
    if m:
        expl_body = m.group(2).strip()
        partb_expls[q] = format_expl("［精解］" + expl_body)
    else:
        partb_expls[q] = ""

# Now build the 45 questions
questions = exam_data['questions']
assert len(questions) == 45, f"Expected 45 questions, got {len(questions)}"

# Assign passage_id mapping
p_map = {
    0: exam_data['passages'][0]['id'], # Cloze Q1-Q20
    1: exam_data['passages'][1]['id'], # Text 1 Q21-Q25
    2: exam_data['passages'][2]['id'], # Text 2 Q26-Q30
    3: exam_data['passages'][3]['id'], # Text 3 Q31-Q35
    4: exam_data['passages'][4]['id'], # Text 4 Q36-Q40
    5: exam_data['passages'][5]['id'], # Part B Q41-Q45
}

# Update Q1-Q20 (Cloze)
for i in range(20):
    q = questions[i]
    qnum = i + 1
    ans, opts = cloze_data[i]
    q['question_number'] = qnum
    q['sort_order'] = qnum
    q['score'] = 0.5
    q['points'] = 0.5
    q['question_type'] = 'cloze_item'
    q['q_type'] = 'cloze_item'
    q['passage_id'] = p_map[0]
    q['stem'] = f"Choose the best option for blank [{qnum}] in the passage:"
    q['answer'] = ans
    q['correct_answer'] = ans
    q['options'] = [{"key": k, "content": c} for k, c in opts]
    q['explanation'] = cloze_expls[qnum]

# Update Q21-Q40 (Reading Comprehension Part A)
for i in range(20):
    idx = 20 + i
    q = questions[idx]
    item = questions_21_40[i]
    qnum = item['qnum']
    passage_idx = 1 + (i // 5)
    
    q['question_number'] = qnum
    q['sort_order'] = qnum
    q['score'] = 2.0
    q['points'] = 2.0
    q['question_type'] = 'reading_item'
    q['q_type'] = 'reading_item'
    q['passage_id'] = p_map[passage_idx]
    q['stem'] = item['stem']
    q['answer'] = item['answer']
    q['correct_answer'] = item['answer']
    q['options'] = item['options']
    q['explanation'] = reading_expls[qnum]

# Update Q41-Q45 (Part B)
for i in range(5):
    idx = 40 + i
    q = questions[idx]
    qnum = 41 + i
    
    q['question_number'] = qnum
    q['sort_order'] = qnum
    q['score'] = 2.0
    q['points'] = 2.0
    q['question_type'] = 'reading_item'
    q['q_type'] = 'reading_item'
    q['passage_id'] = p_map[5]
    q['stem'] = f"Choose the best heading [A]-[G] for Paragraph {i+2} [{qnum}]:"
    q['answer'] = partb_answers[qnum]
    q['correct_answer'] = partb_answers[qnum]
    q['options'] = [dict(opt) for opt in partb_opts]
    q['explanation'] = partb_expls[qnum]

# Exam metadata normalization
exam_data['title'] = "2020年全国硕士研究生招生考试英语（一）真题"
exam_data['category_id'] = "ky1"
exam_data['year'] = 2020
exam_data['exam_type'] = "real"
exam_data['total_score'] = 60.0
exam_data['pass_score'] = 36.0
exam_data['duration_minutes'] = 180
exam_data['approval_status'] = "approved"
exam_data['is_published'] = True

if 'exam' in exam_data:
    exam_data['exam']['title'] = exam_data['title']
    exam_data['exam']['category_id'] = "ky1"
    exam_data['exam']['year'] = 2020
    exam_data['exam']['exam_type'] = "real"
    exam_data['exam']['total_score'] = 60.0
    exam_data['exam']['pass_score'] = 36.0
    exam_data['exam']['duration_minutes'] = 180
    exam_data['exam']['approval_status'] = "approved"
    exam_data['exam']['is_published'] = True

# Write out the calibrated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("Successfully wrote calibrated 2020 ky1 JSON to:", json_path)
