# -*- coding: utf-8 -*-
"""
Round 68: 2018 ky1 Gold Calibration Engine
Exam: 2018年全国硕士研究生招生考试英语（一）真题 (UUID: e95fe05a-07f4-53d1-a11f-9b636acc6469)
Authoritative Source: 2018黄皮书真题解析（英语一）.pdf
"""

import json
import re
import sys
import fitz

sys.stdout.reconfigure(encoding='utf-8')

PDF_PATH = r'c:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2018黄皮书真题解析（英语一）.pdf'
JSON_PATH = r'public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json'

print("=== Building 2018 ky1 Gold Calibration Engine ===")

# 1. Load authoritative PDF text
doc = fitz.open(PDF_PATH)
full_pages = [doc[i].get_text() for i in range(57)]

# --- Authoritative Passages ---
passages_text = [
    # Passage 0: Section I: Use of English (Cloze)
    """Trust is a tricky business. On the one hand, it's a necessary condition [1] many worthwhile things: child care, friendships, etc. On the other hand, putting your [2] in the wrong place often carries a high [3].

[4], why do we trust at all? Well, because it feels good. [5] people place their trust in an individual or an institution, their brains release oxytocin, a hormone that [6] pleasurable feelings and triggers the herding instinct that prompts humans to [7] with one another. Scientists have found that exposure [8] this hormone puts us in a trusting [9]. In a Swiss study, researchers sprayed oxytocin into the noses of half the subjects; those subjects were ready to lend significantly higher amounts of money to strangers than were their [10] who inhaled something else.

[11] for us, we also have a sixth sense for dishonesty that may [12] us. A Canadian study found that children as young as 14 months can differentiate [13] a credible person and a dishonest one. Sixty toddlers were each [14] to an adult tester holding a plastic container. The tester would ask, "What's in here?" before looking into the container, smiling, and exclaiming, "Wow!" Each subject was then invited to look [15]. Half of them found a toy; the other half [16] the container was empty — and realized the tester had [17] them.

Among the children who had not been tricked, the majority were [18] to cooperate with the tester in learning a new skill, demonstrating that they trusted his leadership. [19], only five of the 30 children paired with the "[20]" tester participated in a follow-up activity.""",

    # Passage 1: Section II: Reading Comprehension Part A - Text 1
    """Among the annoying challenges facing the middle class is one that will probably go unmentioned in the next presidential campaign: What happens when the robots come for their jobs?

Don't dismiss that possibility entirely. About half of U. S. jobs are at high risk of being automated, according to a University of Oxford study, with the middle class disproportionately squeezed. Lower-income jobs like gardening or day care don't appeal to robots. But many middle-class occupations — trucking, financial advice, software engineering — have aroused their interest, or soon will. The rich own the robots, so they will be fine.

This isn't to be alarmist. Optimists point out that technological upheaval has benefited workers in the past. The Industrial Revolution didn't go so well for Luddites whose jobs were displaced by mechanized looms, but it eventually raised living standards and created more jobs than it destroyed. Likewise, automation should eventually boost productivity, stimulate demand by driving down prices, and free workers from hard, boring work. But in the medium term, middle-class workers may need a lot of help adjusting.

The first step, as Erik Brynjolfsson and Andrew McAfee argue in The Second Machine Age, should be rethinking education and job training. Curriculums — from grammar school to college — should evolve to focus less on memorizing facts and more on creativity and complex communication. Vocational schools should do a better job of fostering problem-solving skills and helping students work alongside robots. Online education can supplement the traditional kind. It could make extra training and instruction affordable. Professionals trying to acquire new skills will be able to do so without going into debt.

The challenge of coping with automation underlines the need for the U. S. to revive its fading business dynamism: Starting new companies must be made easier. In previous eras of drastic technological change, entrepreneurs smoothed the transition by dreaming up ways to combine labor and machines. The best uses of 3D printers and virtual reality haven't been invented yet. The U. S. needs the new companies that will invent them.

Finally, because automation threatens to widen the gap between capital income and labor income, taxes and the safety net will have to be rethought. Taxes on low-wage labor need to be cut, and wage subsidies such as the earned income tax credit should be expanded: This would boost incomes, encourage work, reward companies for job creation, and reduce inequality.

Technology will improve society in ways big and small over the next few years, yet this will be little comfort to those who find their lives and careers upended by automation. Destroying the machines that are coming for our jobs would be nuts. But policies to help workers adapt will be indispensable.""",

    # Passage 2: Section II: Reading Comprehension Part A - Text 2
    """A new survey by Harvard University finds more than two-thirds of young Americans disapprove of President Trump's use of Twitter. The implication is that Millennials prefer news from the White House to be filtered through other sources, not a president's social media platform.

Most Americans rely on social media to check daily headlines. Yet as distrust has risen toward all media, people may be starting to beef up their media literacy skills. Such a trend is badly needed. During the 2016 presidential campaign, nearly a quarter of web content shared by Twitter users in the politically critical state of Michigan was fake news, according to the University of Oxford. And a survey conducted for BuzzFeed News found 44 percent of Facebook users rarely or never trust news from the media giant.

Young people who are digital natives are indeed becoming more skillful at separating fact from fiction in cyberspace. A Knight Foundation focus-group survey of young people between ages 14 and 24 found they use "distributed trust" to verify stories. They cross-check sources and prefer news from different perspectives — especially those that are open about any bias. "Many young people assume a great deal of personal responsibility for educating themselves and actively seeking out opposing viewpoints," the survey concluded.

Such active research can have another effect. A 2014 survey conducted in Australia, Britain, and the United States by the University of Wisconsin-Madison found that young people's reliance on social media led to greater political engagement.

Social media allows users to experience news events more intimately and immediately while also permitting them to re-share news as a projection of their values and interests. This forces users to be more conscious of their role in passing along information. A survey by Barna research group found the top reason given by Americans for the fake news phenomenon is "reader error," more so than made-up stories or factual mistakes in reporting. About a third say the problem of fake news lies in "misinterpretation or exaggeration of actual news" via social media. In other words, the choice to share news on social media may be the heart of the issue. "This indicates there is a real personal responsibility in counteracting this problem," says Roxanne Stone, editor in chief at Barna Group.

So when young people are critical of an over-tweeting president, they reveal a mental discipline in thinking skills — and in their choices on when to share on social media.""",

    # Passage 3: Section II: Reading Comprehension Part A - Text 3
    """Any fair-minded assessment of the dangers of the deal between Britain's National Health Service (NHS) and DeepMind must start by acknowledging that both sides mean well. DeepMind is one of the leading artificial intelligence (AI) companies in the world. The potential of this work applied to healthcare is very great, but it could also lead to further concentration of power in the tech giants. It is against that background that the information commissioner, Elizabeth Denham, has issued her damning verdict against the Royal Free hospital trust under the NHS, which handed over to DeepMind the records of 1.6 million patients in 2015 on the basis of a vague agreement which took far too little account of the patients' rights and their expectations of privacy.

DeepMind has almost apologized. The NHS trust has mended its ways. Further arrangements — and there may be many — between the NHS and DeepMind will be carefully scrutinised to ensure that all necessary permissions have been asked of patients and all unnecessary data has been cleaned. There are lessons about informed patient consent to learn. But privacy is not the only angle in this case and not even the most important. Ms Denham chose to concentrate the blame on the NHS trust, since under existing law it "controlled" the data and DeepMind merely "processed" it. But this distinction misses the point that it is processing and aggregation, not the mere possession of bits, that gives the data value.

The great question is who should benefit from the analysis of all the data that our lives now generate. Privacy law builds on the concept of damage to an individual from identifiable knowledge about them. That misses the way the surveillance economy works. The data of an individual there gains its value only when it is compared with the data of countless millions more.

The use of privacy law to curb the tech giants in this instance feels slightly maladapted. This practice does not address the real worry. It is not enough to say that the algorithms DeepMind develops will benefit patients and save lives. What matters is that they will belong to a private monopoly which developed them using public resources. If software promises to save lives on the scale that drugs now can, big data may be expected to behave as a big pharma has done. We are still at the beginning of this revolution and small choices now may turn out to have gigantic consequences later. A long struggle will be needed to avoid a future of digital feudalism. Ms Denham's report is a welcome start.""",

    # Passage 4: Section II: Reading Comprehension Part A - Text 4
    """The U. S. Postal Service (USPS) continues to bleed red ink. It reported a net loss of $5.6 billion for fiscal 2016, the 10th straight year its expenses have exceeded revenue. Meanwhile, it has more than $120 billion in unfunded liabilities, mostly for employee health and retirement costs. There are many reasons this formerly stable federal institution finds itself at the brink of bankruptcy. Fundamentally, the USPS is in a historic squeeze between technological change that has permanently decreased demand for its bread-and-butter product, first-class mail, and a regulatory structure that denies management the flexibility to adjust its operations to the new reality.

And interest groups ranging from postal unions to greeting-card makers exert self-interested pressure on the USPS's ultimate overseer — Congress — insisting that whatever else happens to the Postal Service, aspects of the status quo they depend on get protected. This is why repeated attempts at reform legislation have failed in recent years, leaving the Postal Service unable to pay its bills except by deferring vital modernization.

Now comes word that everyone involved — Democrats, Republicans, the Postal Service, the unions and the system's heaviest users — has finally agreed on a plan to fix the system. Legislation is moving through the House that would save USPS an estimated $28.6 billion over five years, which could help pay for new vehicles, among other survival measures. Most of the money would come from a penny-per-letter permanent rate increase and from shifting postal retirees into Medicare. The latter step would largely offset the financial burden of annually pre-funding retiree health care, thus addressing a long-standing complaint by the USPS and its unions.

If it clears the House, this measure would still have to get through the Senate — where someone is bound to point out that it amounts to the bare, bare minimum necessary to keep the Postal Service afloat, not comprehensive reform. There's no change to collective bargaining at the USPS, a major omission considering that personnel accounts for 80 percent of the agency's costs. Also missing is any discussion of eliminating Saturday letter delivery. That common-sense change enjoys wide public support and would save the USPS $2 billion per year. But postal special-interest groups seem to have killed it, at least in the House. The emerging consensus around the bill is a sign that legislators are getting frightened about a politically embarrassing short-term collapse at the USPS. It is not, however, a sign that they're getting serious about transforming the postal service.""",

    # Passage 5: Section II: Reading Comprehension Part B
    """[A] In December of 1869, Congress appointed a commission to select a site and prepare plans and cost estimates for a new State Department Building. The commission was also to consider possible arrangements for the War and Navy Departments. To the horror of some who expected a Greek Revival twin of the Treasury Building to be erected on the other side of the White House, the elaborate French Second Empire style design by Alfred Mullett was selected, and construction of the State Department began in June of 1871.

[B] Completed in 1875, the State Department's south wing was the first to be occupied, with its elegant four-story library (completed in 1876), Diplomatic Reception Room, and Secretary's office decorated with carved wood, Oriental rugs, and stenciled wall patterns. The Navy Department moved into the east wing in 1879, where elaborate wall and ceiling stenciling and thoughtful design features were also incorporated, including the great floor-to-ceiling skylight over the central stairwell and masonry fireplace mantels.

[C] The State, War, and Navy Building, as it was originally known, housed the three Executive Branch Departments most intimately associated with formulating and conducting the nation's foreign policy in the last quarter of the nineteenth century and the first quarter of the twentieth century — the period when the United States emerged as an international power. The building has housed some of the nation's most important diplomatic agreements, and many memorable events have taken place within its walls.

[D] Many of the most celebrated national figures have participated in historical events that have taken place within the EEOB's granite walls. Theodore and Franklin D. Roosevelt, William Howard Taft, Dwight D. Eisenhower, Lyndon B. Johnson, Gerald Ford, and George H. W. Bush all had offices in this building before becoming president. It has housed 16 Secretaries of the Navy, 21 Secretaries of War, and 24 Secretaries of State. Winston Churchill once walked its corridors and Japanese emissaries met here with Secretary of State Cordell Hull after the bombing of Pearl Harbor.

[E] The Eisenhower Executive Office Building (EEOB) commands a unique position in both the national history and the architectural heritage of the United States. Designed by Supervising Architect of the Treasury, Alfred B. Mullett, it was built from 1871 to 1888 to house the growing staffs of the State, War, and Navy Departments, and is considered one of the best examples of French Second Empire architecture in the country.

[F] Construction took 17 years as the building slowly rose wing by wing. When the EEOB was finished, it was the largest office building in Washington, with nearly 2 miles of black and white tiled corridors. Almost all of the interior detail is of cast iron or plaster; the use of wood was minimized to insure fire safety. Eight monumental curving staircases of granite with over 4,000 individually cast bronze balusters are capped by four skylight domes and two stained glass rotundas.

[G] The history of the EEOB began long before its foundations were laid. The first executive offices were constructed between 1799 and 1820. A series of fires (including those set by the British in 1814) and overcrowded conditions led to the construction of the existing Treasury Building. In 1866, the construction of the North Wing of the Treasury Building necessitated the demolition of the State Department building."""
]

# Official answers
official_answers = {
    1: 'C', 2: 'A', 3: 'D', 4: 'B', 5: 'D', 6: 'B', 7: 'C', 8: 'D', 9: 'B', 10: 'A',
    11: 'B', 12: 'B', 13: 'A', 14: 'C', 15: 'D', 16: 'A', 17: 'C', 18: 'B', 19: 'A', 20: 'C',
    21: 'D', 22: 'C', 23: 'A', 24: 'D', 25: 'B', 26: 'D', 27: 'A', 28: 'B', 29: 'C', 30: 'A',
    31: 'B', 32: 'C', 33: 'D', 34: 'D', 35: 'B', 36: 'B', 37: 'A', 38: 'A', 39: 'C', 40: 'D',
    41: 'E', 42: 'G', 43: 'A', 44: 'B', 45: 'D'
}

# Part B options mapping (authentic EEOB paragraphs)
part_b_opts = [
    {'key': 'A', 'text': '[A] In December of 1869, Congress appointed a commission to select a site and prepare plans and cost estimates for a new State Department Building...', 'value': 'A'},
    {'key': 'B', 'text': "[B] Completed in 1875, the State Department's south wing was the first to be occupied, with its elegant four-story library (completed in 1876)...", 'value': 'B'},
    {'key': 'C', 'text': "[C] The State, War, and Navy Building, as it was originally known, housed the three Executive Branch Departments most intimately associated with formulating and conducting the nation's foreign policy...", 'value': 'C'},
    {'key': 'D', 'text': "[D] Many of the most celebrated national figures have participated in historical events that have taken place within the EEOB's granite walls...", 'value': 'D'},
    {'key': 'E', 'text': '[E] The Eisenhower Executive Office Building (EEOB) commands a unique position in both the national history and the architectural heritage of the United States...', 'value': 'E'},
    {'key': 'F', 'text': '[F] Construction took 17 years as the building slowly rose wing by wing. When the EEOB was finished, it was the largest office building in Washington...', 'value': 'F'},
    {'key': 'G', 'text': '[G] The history of the EEOB began long before its foundations were laid. The first executive offices were constructed between 1799 and 1820...', 'value': 'G'}
]

# Read local JSON
with open(JSON_PATH, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Calibrate Exam Metadata
exam = exam_data['exam']
exam['title'] = '2018年全国硕士研究生招生考试英语（一）真题'
exam['category_id'] = 'ky1'
exam['year'] = 2018
exam['exam_type'] = 'real'
exam['total_score'] = 60.0
exam['pass_score'] = 36.0
exam['duration_minutes'] = 180
exam['approval_status'] = 'approved'

# 2. Calibrate Passages
titles = [
    'Section I: Use of English',
    'Section II: Reading Comprehension Part A - Text 1',
    'Section II: Reading Comprehension Part A - Text 2',
    'Section II: Reading Comprehension Part A - Text 3',
    'Section II: Reading Comprehension Part A - Text 4',
    'Section II: Reading Comprehension Part B'
]

for idx, p in enumerate(exam_data['passages']):
    p['title'] = titles[idx]
    p['content'] = passages_text[idx]

# 3. Calibrate Questions
for idx, q in enumerate(exam_data['questions']):
    q_num = idx + 1
    q['question_number'] = q_num
    q['sort_order'] = q_num
    
    ans = official_answers[q_num]
    q['answer'] = ans
    q['correct_answer'] = ans
    
    if q_num <= 20:
        q['score'] = 0.5
        q['points'] = 0.5
        q['question_type'] = 'cloze_item'
        q['q_type'] = 'cloze_item'
        q['stem'] = f'Choose the best option for blank [{q_num}] in the passage:'
    else:
        q['score'] = 2.0
        q['points'] = 2.0
        q['question_type'] = 'reading_item'
        q['q_type'] = 'reading_item'
        
    if 41 <= q_num <= 45:
        q['options'] = part_b_opts
        q['stem'] = f'Choose the correct paragraph [A]-[G] for position ({q_num}):'

# Save updated JSON
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("Saved preliminary gold JSON. Now extracting and injecting pure UTF-8 explanations...")
