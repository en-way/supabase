import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

exam_file = 'public/data/exams/e1b9d134-9546-55ab-9a60-c7e5b04046a3.json'
with open(exam_file, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Calibrate Passages
# Passage 0: Section I Use of English (ID: 8b7dec36-0057-5b3e-8d45-b736f5b913e2)
p0_content = """Comparisons were drawn between the development of television in the 20th century and the diffusion of printing in the 15th and 16th centuries. Yet much had happened [1]. As was discussed before, it was not [2] the 19th century that the newspaper became the dominant pre-electronic [3], following in the wake of the pamphlet and the book and in the [4] of the periodical. It was during the same time that the communications revolution [5] up, beginning with transport, the railway, and leading [6] through the telegraph, the telephone, radio, and motion pictures [7] the 20th-century world of the motor car and the airplane. Not everyone sees that process in [8]. It is important to do so.

It is generally recognized, [9], that the introduction of the computer in the early 20th century, [10] by the invention of the integrated circuit during the 1960s, radically changed the process, [11] its impact on the media was not immediately [12]. As time went by, computers became smaller and more powerful, and they became "personal" too, as well as [13], with display becoming sharper and storage [14] increasing. They were thought of, like people, [15] generations, with the distance between generations much [16].

It was within the computer age that the term "information society" began to be widely used to describe the [17] within which we now live. The communications revolution has [18] both work and leisure and how we think and feel both about place and time, but there have been [19] views about its economic, political, social and cultural implications. "Benefits" have been weighed [20] "harmful" outcomes. And generalizations have proved difficult."""

# Passage 1: Section II Text 1 (ID: c82eb2c3-d5f7-58fa-981e-0806ff32c124)
p1_content = """If you intend using humor in your talk to make people smile, you must know how to identify shared experiences and problems. Your humor must be relevant to the audience and should help to show them that you are one of them or that you understand their situation and are in sympathy with their point of view. Depending on whom you are addressing, the problems will be different. If you are talking to a group of managers, you may refer to the disorganized methods of their secretaries; alternatively if you are addressing secretaries, you may want to comment on their disorganized bosses.

Here is an example, which I heard at a nurses' convention, of a story which works well because the audience all shared the same view of doctors. A man arrives in heaven and is being shown around by St. Peter. He sees wonderful accommodations, beautiful gardens, sunny weather, and so on. Everyone is very peaceful, polite and friendly until, waiting in a line for lunch, the new arrival is suddenly pushed aside by a man in a white coat, who rushes to the head of the line, grabs his food and stomps over to a table by himself. "Who is that?" the new arrival asked St. Peter. "Oh, that's God," came the reply, "but sometimes he thinks he's a doctor."

If you are part of the group which you are addressing, you will be in a position to know the experiences and problems which are common to all of you and it'll be appropriate for you to make a passing remark about the inedible canteen food or the chairman's notorious bad taste in ties. With other audiences you mustn't attempt to cut in with humor as they will resent an outsider making disparaging remarks about their canteen or their chairman. You will be on safer ground if you stick to scapegoats like the Post Office or the telephone system.

If you feel awkward being humorous, you must practice so that it becomes more natural. Include a few casual and apparently off-the-cuff remarks which you can deliver in a relaxed and unforced manner. Often it's the delivery which causes the audience to smile, so speak slowly and remember that a raised eyebrow or an unbelieving look may help to show that you are making a light-hearted remark.

Look for the humor. It often comes from the unexpected. A twist on a familiar quote "If at first you don't succeed, give up" or a play on words or on a situation. Search for exaggeration and understatements. Look at your talk and pick out a few words or sentences which you can turn about and inject with humor."""

# Passage 2: Section II Text 2 (ID: e105b25c-a6ec-502d-b204-11a9c304d4fe)
p2_content = """Since the dawn of human ingenuity, people have devised ever more cunning tools to cope with work that is dangerous, boring, burdensome, or just plain nasty. That compulsion has resulted in robotics—the science of conferring various human capabilities on machines. And if scientists have yet to create the mechanical version of science fiction, they have begun to come close.

As a result, the modern world is increasingly populated by intelligent gizmos whose presence we barely notice but whose universal existence has removed much human labor. Our factories hum to the rhythm of robot assembly arms. Our banking is done at automated teller terminals that thank us with mechanical politeness for the transaction. Our subway trains are controlled by relentless robo-drivers. And thanks to the continual miniaturization of electronics and micro-mechanics, there are already robot systems that can perform some kind of brain and bone surgery with submillimeter accuracy—far greater precision than highly skilled physicians can achieve with their hands alone.

But if robots are to reach the next stage of laborsaving utility, they will have to operate with less human supervision and be able to make at least a few decisions for themselves—goals that pose a real challenge. "While we know how to tell a robot to handle a specific error," says Dave Lavery, manager of a robotics program at NASA, "we can't yet give a robot enough 'common sense' to reliably interact with a dynamic world."

Indeed the quest for true artificial intelligence has produced very mixed results. Despite a spell of initial optimism in the 1960s and 1970s when it appeared that transistor circuits and microprocessors might be able to copy the action of the human brain by the year 2010, researchers lately have begun to extend that forecast by decades if not centuries.

What they found, in attempting to model thought, is that the human brain's roughly one hundred billion nerve cells are much more talented—and human perception far more complicated—than previously imagined. They have built robots that can recognize the error of a machine panel by a fraction of a millimeter in a controlled factory environment. But the human mind can glimpse a rapidly changing scene and immediately disregard the 98 percent that is irrelevant, instantaneously focusing on the monkey at the side of a winding forest road or the single suspicious face in a big crowd. The most advanced computer systems on Earth can't approach that kind of ability, neuroscientists think, and they'll be hard pressed to do so in the next couple of decades. "There is a kind of perception which is very easy for human beings to do," says Michael Sipser, a mathematician at the Massachusetts Institute of Technology. "Robots can't do it at all and we don't know quite how we do it.\""""

# Passage 3: Section II Text 3 (ID: 53474821-9120-5962-acc2-5c36455d7aeb)
p3_content = """Could the bad old days of economic decline be about to return? Since OPEC agreed to supply-cuts in March, the price of crude oil has jumped to almost $26 a barrel, up from less than $10 last December. This near-tripling of oil prices calls up scary memories of the 1973 oil shock, when prices quadrupled, and 1979-1980, when they also almost tripled. Both previous shocks resulted in double-digit inflation and global economic decline. So where are the headlines warning of gloom and doom this time?

The oil price was given another push up this week when Iraq suspended oil exports. Strengthening economic growth, at the same time as winter grips the northern hemisphere, could push the price higher still in the short term.

Yet there are good reasons to expect the economic consequences now to be less severe than in the 1970s. In most countries the cost of crude oil now accounts for a smaller share of the price of petrol than it did in the 1970s. In Europe, taxes account for up to four-fifths of the retail price, so even quite big changes in the price of crude have a more muted effect on pump prices than in the past.

Rich economies are also less dependent on oil than they were, and so less sensitive to swings in the oil price. Energy conservation, a shift to other fuels and a decline in the importance of heavy, energy-intensive industries have reduced oil consumption. Software, consultancy and mobile telephones use far less oil than steel or car production. For each dollar of GDP (in constant prices) rich economies now use nearly 50% less oil than in 1973. The OECD estimates in its latest Economic Outlook that, if oil prices averaged $22 a barrel for a full year, compared with $13 in 1998, this would increase the oil import bill in rich economies by only 0.25%-0.5% of GDP. That is less than one-quarter of the income loss in 1974 or 1980. On the other hand, oil-importing emerging economies—to which heavy industry has shifted—have become more energy-intensive, and so could be more seriously squeezed.

One more reason not to lose sleep over the rise in oil prices is that, unlike the rises in the 1970s, it has not occurred against the background of general commodity-price inflation and global excess demand. A sizable portion of the world is only just emerging from economic decline. The Economist's commodity price index is broadly unchanging from a year ago. In 1973 commodity prices jumped by 70%, and in 1979 by almost 30%."""

# Passage 4: Section II Text 4 (ID: f0cbd337-0bdf-58e8-8723-cf2c30aa0d62)
p4_content = """The Supreme Court's decisions on physician-assisted suicide carry important implications for how medicine seeks to relieve dying patients of pain and suffering.

Although it ruled that there is no constitutional right to physician-assisted suicide, the Court in effect supported the medical principle of "double effect," a centuries-old moral principle holding that an action having two effects—a good one that is intended and a harmful one that is foreseen—is permissible if the actor intends only the good effect.

Doctors have used that principle in recent years to justify using high doses of morphine to control terminally ill patients' pain, even though increasing dosages will eventually kill the patient.

Nancy Dubler, director of Montefiore Medical Center, contends that the principle will shield doctors who "until now have very, very strongly insisted that they could not give patients sufficient medication to control their pain if that might hasten death."

George Annas, chair of the health law department at Boston University, maintains that, as long as a doctor prescribes a drug for a legitimate medical purpose, the doctor has done nothing illegal even if the patient uses the drug to hasten death. "It's like surgery," he says. "We don't call those deaths homicides because the doctors didn't intend to kill their patients, although they risked their death. If you're a physician, you can risk your patient's suicide as long as you don't intend their suicide."

On another level, many in the medical community acknowledge that the assisted-suicide debate has been fueled in part by the despair of patients for whom modern medicine has prolonged the physical agony of dying.

Just three weeks before the Court's ruling on physician-assisted suicide, the National Academy of Science (NAS) released a two-volume report, Approaching Death: Improving Care at the End of Life. It identifies the undertreatment of pain and the aggressive use of "ineffectual and forced medical procedures that may prolong and even dishonor the period of dying" as the twin problems of end-of-life care.

The profession is taking steps to require young doctors to train in hospices, to test knowledge of aggressive pain management therapies, to develop a Medicare billing code for hospital-based care, and to develop new standards for assessing and treating pain at the end of life.

Annas says lawyers can play a key role in insisting that these well-meaning medical initiatives translate into better care. "Large numbers of physicians seem unconcerned with the pain their patients are needlessly and predictably suffering, to the extent that it constitutes 'systematic patient abuse'." He says medical licensing boards "must make it clear... that painful deaths are presumptively ones that are incompetently managed and should result in license suspension.\""""

passage_map = {
    '8b7dec36-0057-5b3e-8d45-b736f5b913e2': p0_content,
    'c82eb2c3-d5f7-58fa-981e-0806ff32c124': p1_content,
    'e105b25c-a6ec-502d-b204-11a9c304d4fe': p2_content,
    '53474821-9120-5962-acc2-5c36455d7aeb': p3_content,
    'f0cbd337-0bdf-58e8-8723-cf2c30aa0d62': p4_content
}

for p in exam_data.get('passages', []):
    pid = p.get('id')
    if pid in passage_map:
        p['content'] = passage_map[pid]
        print(f"Updated passage {pid}: {len(p['content'].split())} words, {len(p['content'].splitlines())} lines")

# Load verified full explanations from PDF
with open('scripts/2002_pdf_dump.txt', encoding='utf-8') as f:
    pdf_full = f.read()

# Helper to extract clean explanation block
def get_clean_exp(qnum, default_exp):
    # Search in pdf_full
    p_q = pdf_full.find(f'\n{qnum}.\n')
    if p_q == -1:
        p_q = pdf_full.find(f'\n{qnum}. ')
    if p_q == -1:
        p_q = pdf_full.find(f'\n{qnum} •')
    if p_q == -1:
        p_q = pdf_full.find(f'\n{qnum}•')
    if p_q == -1:
        return default_exp
        
    nxt_pos = pdf_full.find(f'\n{qnum+1}.', p_q + 5) if qnum < 40 else pdf_full.find('Part B', p_q)
    if nxt_pos == -1 and qnum == 40:
        nxt_pos = pdf_full.find('<<<PAGE_39>>>', p_q)
    if nxt_pos == -1:
        nxt_pos = p_q + 3000
    chunk = pdf_full[p_q:nxt_pos]
    
    # Locate anchor
    anchors = ['［精准定位］', '[精准定位]', '［试题考点］', '[试题考点]', '［命题解密］', '[命题解密]', '［解题思路］', '[解题思路]']
    found_idx = -1
    for a in anchors:
        idx = chunk.find(a)
        if idx != -1:
            if found_idx == -1 or idx < found_idx:
                found_idx = idx
    if found_idx != -1:
        clean = chunk[found_idx:].strip()
        # Cut trailing page numbers or next section markers if any
        clean = re.sub(r'<<<PAGE_\d+>>>.*', '', clean, flags=re.DOTALL).strip()
        clean = re.sub(r'\n\d+\s*$', '', clean).strip()
        if len(clean) >= 100:
            return clean
            
    # If chunk extraction was too short or didn't find anchor, fallback to cleaning default_exp
    clean_def = default_exp
    for a in anchors:
        idx = clean_def.find(a)
        if idx != -1:
            clean_def = clean_def[idx:].strip()
            break
    return clean_def

# Specific Question Updates (stems, options, answers)
q_updates = {
    # Q5: ans -> B
    5: {
        'answer': 'B',
        'correct_answer': 'B',
    },
    # Q14: ans -> C
    14: {
        'answer': 'C',
        'correct_answer': 'C',
    },
    # Q19: ans -> B
    19: {
        'answer': 'B',
        'correct_answer': 'B',
    },
    # Q21: stem typo vour -> your, underline
    21: {
        'stem': 'To make your humor work, you should ________.',
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q22: ans C -> B!
    22: {
        'stem': 'The joke about doctors implies that, in the eyes of nurses, they are ________.',
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q23: opt D text -> have often been the laughing stock
    23: {
        'stem': 'It can be inferred from the text that public services ________.',
        'options': [
            {'key': 'A', 'text': 'have benefited many people', 'value': 'A'},
            {'key': 'B', 'text': 'are the focus of public attention', 'value': 'B'},
            {'key': 'C', 'text': 'are an inappropriate subject for humor', 'value': 'C'},
            {'key': 'D', 'text': 'have often been the laughing stock', 'value': 'D'}
        ],
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q24: stem underline
    24: {
        'stem': 'To achieve the desired result, humorous stories should be delivered ________.',
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q25: stem underline
    25: {
        'stem': 'The best title for the text may be ________.',
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q26: stem underline
    26: {
        'stem': 'Human ingenuity was initially demonstrated in ________.',
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q27: stem underline
    27: {
        'stem': 'The word "gizmos" (line 1, paragraph 2) most probably means ________.',
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q28: stem underline, opt A
    28: {
        'stem': "According to the text, what is beyond man's ability now is to design robots that can ________.",
        'options': [
            {'key': 'A', 'text': 'fulfill delicate tasks like performing brain surgery', 'value': 'A'},
            {'key': 'B', 'text': 'interact with human beings verbally', 'value': 'B'},
            {'key': 'C', 'text': 'have a little common sense', 'value': 'C'},
            {'key': 'D', 'text': 'respond independently to a changing world', 'value': 'D'}
        ],
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q29: opt D cultivate human creativity
    29: {
        'stem': 'Besides reducing human labor, robots can also ________.',
        'options': [
            {'key': 'A', 'text': 'make a few decisions for themselves', 'value': 'A'},
            {'key': 'B', 'text': 'deal with some errors with human intervention', 'value': 'B'},
            {'key': 'C', 'text': 'improve factory environments', 'value': 'C'},
            {'key': 'D', 'text': 'cultivate human creativity', 'value': 'D'}
        ],
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q30: stem underline
    30: {
        'stem': 'The author uses the example of a monkey to argue that robots are ________.',
        'options': [
            {'key': 'A', 'text': 'expected to copy human brain in internal structure', 'value': 'A'},
            {'key': 'B', 'text': 'able to perceive abnormalities in a dynamic environment', 'value': 'B'},
            {'key': 'C', 'text': 'far less able than human brain in focusing on relevant information', 'value': 'C'},
            {'key': 'D', 'text': 'best used in a controlled factory environment', 'value': 'D'}
        ],
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q31: stem underline, opt C
    31: {
        'stem': 'The main reason for the latest rise of oil price is ________.',
        'options': [
            {'key': 'A', 'text': 'global inflation', 'value': 'A'},
            {'key': 'B', 'text': 'reduction in supply', 'value': 'B'},
            {'key': 'C', 'text': 'fast growth in world economy', 'value': 'C'},
            {'key': 'D', 'text': "Iraq's suspension of oil exports", 'value': 'D'}
        ],
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q32: stem full
    32: {
        'stem': 'It can be inferred from the text that the retail price of petrol will go up for even a small change in crude oil prices if ________.',
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q33: stem underline
    33: {
        'stem': 'The estimates in Economic Outlook show that in rich countries ________.',
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q34: stem underline, opt A
    34: {
        'stem': 'We can draw a conclusion from the text that ________.',
        'options': [
            {'key': 'A', 'text': 'oil price shocks are less shocking now', 'value': 'A'},
            {'key': 'B', 'text': 'inflation seems irrelevant to oil-price shocks', 'value': 'B'},
            {'key': 'C', 'text': 'energy conservation can keep down the oil prices', 'value': 'C'},
            {'key': 'D', 'text': 'the price rise of crude leads to the shrinking of heavy industry', 'value': 'D'}
        ],
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q35: stem underline
    35: {
        'stem': 'From the text we can see that the writer seems ________.',
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q36: stem underline, opts A, B, C full
    36: {
        'stem': 'From the first three paragraphs, we learn that ________.',
        'options': [
            {'key': 'A', 'text': "doctors used to increase drug dosages to control their patients' pain", 'value': 'A'},
            {'key': 'B', 'text': 'it is still illegal for doctors to help the dying end their lives', 'value': 'B'},
            {'key': 'C', 'text': 'the Supreme Court strongly opposes physician-assisted suicide', 'value': 'C'},
            {'key': 'D', 'text': 'patients have no constitutional right to commit suicide', 'value': 'D'}
        ],
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q38: stem underline
    38: {
        'stem': "According to the NAS's report, one of the problems in end-of-life care is ________.",
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q39: ans D -> A! (Bold)
    39: {
        'stem': 'Which of the following best defines the word "aggressive" (line 3, paragraph 7)?',
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q40: stem full
    40: {
        'stem': 'George Annas would probably agree that doctors should be punished if they ________.',
        'options': [
            {'key': 'A', 'text': 'manage their patients incompetently', 'value': 'A'},
            {'key': 'B', 'text': 'give patients more medicine than needed', 'value': 'B'},
            {'key': 'C', 'text': 'reduce drug dosages for their patients', 'value': 'C'},
            {'key': 'D', 'text': 'prolong the needless suffering of the patients', 'value': 'D'}
        ],
        'answer': 'D',
        'correct_answer': 'D'
    }
}

for q in exam_data.get('questions', []):
    qnum = q.get('sort_order')
    # Update stem, options, answers if in q_updates
    if qnum in q_updates:
        for k, v in q_updates[qnum].items():
            q[k] = v
            
    # Clean explanation
    old_exp = q.get('explanation', '')
    clean_exp = get_clean_exp(qnum, old_exp)
    q['explanation'] = clean_exp

# Save updated exam json
with open(exam_file, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"Successfully calibrated 2002 exam JSON to {exam_file}!")
