import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

exam_file = 'public/data/exams/2c892204-071f-5943-86be-d49bca93fe71.json'
with open(exam_file, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Gold Passages Content
# Passage 0: Section I Use of English (ID: 4f5df10d-1837-59f4-98d4-6588100bcaec)
p0_content = """The government is to ban payments to witnesses by newspapers seeking to buy up people involved in prominent cases [1] the trial of Rosemary West.

In a significant [2] of legal controls over the press, Lord Irvine, the Lord Chancellor, will introduce a [3] bill that will propose making payments to witnesses [4] and will strictly control the amount of [5] that can be given to a case [6] a trial begins.

In a letter to Gerald Kaufman, chairman of the House of Commons media select committee, Lord Irvine said he [7] with a committee report this year which said that self-regulation did not [8] sufficient control.

[9] of the letter came two days after Lord Irvine caused a [10] of media protest when he said the [11] of privacy controls contained in European legislation would be left to judges [12] to Parliament.

The Lord Chancellor said introduction of the Human Rights Bill, which [13] the European Convention on Human Rights legally [14] in Britain, laid down that everybody was [15] to privacy and that public figures could go to court to protect themselves and their families.

"Press freedoms will be in safe hands [16] our British judges," he said.

Witness payments became an [17] after West was sentenced to 10 life sentences in 1995. Up to 19 witnesses were [18] to have received payments for telling their stories to newspapers. Concerns were raised [19] witnesses might be encouraged to exaggerate their stories in court to [20] guilty verdicts."""

# Passage 1: Section II Text 1 (ID: 4e851c3e-3768-52a5-b959-5e5b308906c9)
p1_content = """Specialisation can be seen as a response to the problem of an increasing accumulation of scientific knowledge. By splitting up the subject matter into smaller units, one man could continue to handle the information and use it as the basis for further research. But specialisation was only one of a series of related developments in science affecting the process of communication. Another was the growing professionalisation of scientific activity.

No clear-cut distinction can be drawn between professionals and amateurs in science: exceptions can be found to any rule. Nevertheless, the word "amateur" does carry a connotation that the person concerned is not fully integrated into the scientific community and, in particular, may not fully share its values. The growth of specialisation in the nineteenth century, with its consequent requirement of a longer, more complex training, implied greater problems for amateur participation in science. The trend was naturally most obvious in those areas of science based especially on a mathematical or laboratory training, and can be illustrated in terms of the development of geology in the United Kingdom.

A comparison of British geological publications over the last century and a half reveals not simply an increasing emphasis on the primacy of research, but also a changing definition of what constitutes an acceptable research paper. Thus, in the nineteenth century, local geological studies represented worthwhile research in their own right; but, in the twentieth century, local studies have increasingly become acceptable to professionals only if they incorporate, and reflect on, the wider geological picture. Amateurs, on the other hand, have continued to pursue local studies in the old way. The overall result has been to make entrance to professional geological journals harder for amateurs, a result that has been reinforced by the widespread introduction of refereeing, first by national journals in the nineteenth century and then by several local geological journals in the twentieth century. As a logical consequence of this development, separate journals have now appeared aimed mainly towards either professional or amateur readership. A rather similar process of differentiation has led to professional geologists coming together nationally within one or two specific societies, whereas the amateurs have tended either to remain in local societies or to come together nationally in a different way.

Although the process of professionalisation and specialisation was already well under way in British geology during the nineteenth century, its full consequences were thus delayed until the twentieth century. In science generally, however, the nineteenth century must be reckoned as the crucial period for this change in the structure of science."""

# Passage 2: Section II Text 2 (ID: dea76b45-8738-5e7c-b1ed-77d39cdd1f55)
p2_content = """A great deal of attention is being paid today to the so-called digital divide—the division of the world into the info (information) rich and the info poor. And that divide does exist today. My wife and I lectured about this impending doom 20 years ago. What the scholars and policy makers who worry about this divide forget is that the digital divide was not created by the Internet, but by an obvious quirk of distribution that has faced each new invention in history.

There are technological reasons to hope the digital divide will narrow. As the Internet becomes more and more commercialized, it is in the interest of business to universalize access—after all, the more people online, the more potential customers there are. More and more governments, afraid their countries will be left behind, want to spread Internet access. Within the next decade or two, one to two billion people on the planet will be netted together. As a result, I now believe the digital divide will narrow rather than widen in the years ahead. And that is very good news because the Internet may well be the most powerful tool for combating world poverty that we've ever had.

Of course, the use of the Internet isn't the only way to defeat poverty. And the Internet is not the only tool we have. But it has enormous potential.

To take advantage of this tool, some impoverished countries will have to get over their outdated anti-colonial prejudices with respect to foreign investment. Countries that still think foreign investment is an invasion of their sovereignty might well study the history of infrastructure (the basic structural foundations of a society) in the United States. When the United States built its industrial infrastructure, it didn't have the capital to do so. And that is why America's Second Wave infrastructure—including roads, harbors, highways, ports and so on—were built with foreign investment. The English, the Germans, the Dutch and the French were investing in Britain's former colony. They financed them. Immigrant Americans built them. Guess who owns them now? The Americans. I believe the same thing would be true in underdeveloped countries, which is why the more capital that comes in helping them build their Third Wave infrastructure, the better off they're going to be, which will also narrow the digital divide."""

# Passage 3: Section II Text 3 (ID: 9f04a599-cbe5-5da4-bc20-f5f23621332c)
p3_content = """Why do so many Americans distrust what they read in their newspapers? The American Society of Newspaper Editors is trying to answer this question. The organization is deep into a long self-analysis called the journalism credibility project.

Sad to say, this project has turned out to be mostly low-level findings about factual errors and spelling and grammar failures. These are important, but they have been known to anyone who ever worked in a newsroom, and the problems are not difficult to fix.

But the sources of distrust go way deeper. Most journalists learn to see the world through a set of standard templates (patterns) into which they plug each day's events. In other words, there is a conventional story line in the newsroom culture that provides a backbone and a justification for all they do.

There exists a social and cultural disconnect between journalists and their readers, which helps explain why the "standard templates" of the newsroom seem alien to many readers. In a recent survey, questionnaires were sent to 1,000 journalists and 1,000 members of the public.

Replies show that compared with other Americans, journalists are more likely to be up-scale, better educated, and less religious. The result is that they see the world differently from readers and are often out of touch with the communities they serve.

Reporters tend to be part of a broadly defined social and cultural elite, so their work tends to reflect the conventional values of this elite. The world according to the standard templates may seem quite normal and natural to them, but at the same time, it can seem bizarre to someone with a very different view of the world.

This is an explosive situation for any industry, particularly a declining one. Here is a troubled business that keeps hiring employees whose views are at odds with those of its customers. You have to squint mightily to see the journalism credibility project doing anything about that. The project may eventually get around to noticing the actual problem, but for now it seems to be taking the usual unavailing methods: focusing on the parts of the problem that are most easy to address or looking for reporters who differ broadly by outlook, values, education, and class."""

# Passage 4: Section II Text 4 (ID: d5d601b7-32a5-5781-b39c-8f71911c8a8e)
p4_content = """The world is going through the biggest wave of mergers and acquisitions ever witnessed. The process sweeps from hyperactive America to Europe and reaches the shores of Japan. In the first eight months of this year, the value of all the deals was already greater than that of the whole year of 1997.

There's no question that the big are getting bigger and more powerful. Multinational corporations accounted for less than 20% of international trade in 1982. Today the figure is more than 33% and rising. The world's top 200 firms now account for more than a quarter of world economic activity. In telecommunications, media and entertainment, energy and finance, the top firms have been rapidly gaining market share through mergers.

I believe that the most important forces behind the massive M&A wave are the same that underpin the globalization process: falling transportation and communication costs, lower trade and investment barriers and enlarged markets that require firms to expand in order to stay competitive. In short, the globalization of world markets is pushing companies towards greater scale.

Examples of benefits or costs of the current concentration wave are scanty. Yet it is hard to imagine that the merger of a few oil firms today could re-create the same kind of monopoly that Standard Oil achieved a century ago. The world economy is more competitive today with more competitors from more regions than it was then. In addition, the speed of technological changes will accelerate the emergence of outside competitors to any mega-merger.

Yet the fact remains that the merger movement must be watched. A few weeks ago, Alan Greenspan, the Federal Reserve chairman, warned against "the dangers of mega-banks, who have no other alternative than to operate as lender of last resort." The big banks are so large that their failure could pull down the whole financial system. Who is going to supervise, regulate and operate as lender of last resort for the mega-banks that are being created? Won't they be beyond the control of any single nation? And what about the traditional "anti-trust" on issues that affect many other nations, as in the U.S. vs. Microsoft case?"""

# Passage 5: Section II Text 5 (ID: e1a90001-2001-4000-8000-000000000006)
p5_content = """When I decided to quit my full-time employment it never occurred to me that I might become a part of a new international trend. A lateral move that hurt my pride and blocked my professional progress prompted me to abandon my relatively high-profile career although, I covered my exit in the manner of a disgraced government minister by claiming "I wanted to spend more time with my family".

Curiously, some two-and-a-half years and two novels later, my experiment in what the Americans term "downshifting" has turned my tired excuse into an absolute reality. I have been transformed from a passionate advocate of the philosophy of "having it all", preached by Linda Kelsey for the past seven years in the pages of She magazine, into a woman who is happy to settle for a bit of everything.

I have discovered, as perhaps Kelsey will after her much-publicized resignation from the editorship of She after a build-up of stress, that abandoning the doctrine of "juggling your life", and making the alternative move into "downshifting" brings with it far greater rewards than financial success and social status. Nothing can strike your fancy as much as the simple pleasures of life: 12-hour working days, pressured deadlines, the fearful strain of office politics, and the limitations of being a parent on "quality time" are gone.

In America, the move away from juggling to a simpler, less materialistic lifestyle is a well-established trend. Downshifting—also known in America as "voluntary simplicity"—has, ironically, even bred a new area of what might be termed "anti-consumerism". There are a number of bestselling downshifting self-help books for people who want to simplify their lives; there are newsletters, such as The Tightwad Gazette, that give hundreds of thousands of Americans useful tips on anything from recycling their cling-film to making their own soap; there are even support groups for those who want to achieve the mid-'90s equivalent of dropping out.

While in America the trend started as a reaction to the economic decline—after the mass redundancies caused by downsizing in the late '80s—and is still linked to the politics of thrift, in Britain, at least among the middle-class downshifters of my acquaintance, we have different reasons for seeking to simplify our lives.

For the women of my generation who were urged to keep juggling through the '80s, downshifting in the mid-'90s is not so much a search for the mythical good life—growing your own organic vegetables, and risking turning into one—as a personal recognition of your limitations."""

passage_map = {
    '4f5df10d-1837-59f4-98d4-6588100bcaec': (p0_content, 'cloze', 1),
    '4e851c3e-3768-52a5-b959-5e5b308906c9': (p1_content, 'reading', 1),
    'dea76b45-8738-5e7c-b1ed-77d39cdd1f55': (p2_content, 'reading', 2),
    '9f04a599-cbe5-5da4-bc20-f5f23621332c': (p3_content, 'reading', 3),
    'd5d601b7-32a5-5781-b39c-8f71911c8a8e': (p4_content, 'reading', 4),
    'e1a90001-2001-4000-8000-000000000006': (p5_content, 'reading', 5)
}

for p in exam_data.get('passages', []):
    pid = p.get('id')
    if pid in passage_map:
        content, ptype, pnum = passage_map[pid]
        p['content'] = content
        p['type'] = ptype
        p['passage_number'] = pnum
        print(f"Updated passage {pid}: type={ptype}, num={pnum}, {len(content.split())} words, {len(content.splitlines())} lines")

# Load verified explanations from PDF
with open('scripts/2001_pdf_dump.txt', encoding='utf-8') as f:
    pdf_full = f.read()

def get_clean_exp(qnum, default_exp):
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
        nxt_pos = pdf_full.find('<<<PAGE_41>>>', p_q)
    if nxt_pos == -1:
        nxt_pos = p_q + 3000
    chunk = pdf_full[p_q:nxt_pos]
    
    anchors = ['［精准定位］', '[精准定位]', '［试题考点］', '[试题考点]', '［命题解密］', '[命题解密]', '［解题思路］', '[解题思路]']
    found_idx = -1
    for a in anchors:
        idx = chunk.find(a)
        if idx != -1:
            if found_idx == -1 or idx < found_idx:
                found_idx = idx
    if found_idx != -1:
        clean = chunk[found_idx:].strip()
        clean = re.sub(r'<<<PAGE_\d+>>>.*', '', clean, flags=re.DOTALL).strip()
        clean = re.sub(r'\n\d+\s*$', '', clean).strip()
        if len(clean) >= 100:
            return clean
            
    clean_def = default_exp
    for a in anchors:
        idx = clean_def.find(a)
        if idx != -1:
            clean_def = clean_def[idx:].strip()
            break
    return clean_def

# Question Updates
q_updates = {
    # Q12: ans B -> C! (rather than)
    12: {
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q13: ans A -> B! (makes)
    13: {
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q21: stem underline
    21: {
        'stem': 'The growth of specialisation in the 19th century might be more clearly seen in sciences such as ________.',
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q22: stem underline
    22: {
        'stem': 'We can infer from the passage that ________.',
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q23: stem underline
    23: {
        'stem': 'The author writes of the development of geology to demonstrate ________.',
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q24: stem underline
    24: {
        'stem': 'The direct reason for specialisation is ________.',
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q25: stem underline
    25: {
        'stem': 'Digital divide is something ________.',
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q26: stem underline
    26: {
        'stem': 'Governments attach importance to the Internet because it ________.',
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q27: stem underline
    27: {
        'stem': 'The writer mentioned the case of the United States to justify the policy of ________.',
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q28: stem underline
    28: {
        'stem': "It seems that now a country's economy depends much on ________.",
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q30: stem underline
    30: {
        'stem': 'The results of the journalism credibility project turned out to be ________.',
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q31: stem underline
    31: {
        'stem': 'The basic problem of journalists as pointed out by the writer lies in their ________.',
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q32: stem underline
    32: {
        'stem': 'Despite its efforts, the newspaper industry still cannot satisfy the readers owing to its ________.',
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q34: stem underline
    34: {
        'stem': 'According to the author, one of the driving forces behind M&A wave is ________.',
        'answer': 'A',
        'correct_answer': 'A'
    },
    # Q35: stem underline
    35: {
        'stem': 'From Paragraph 4 we can infer that ________.',
        'answer': 'D',
        'correct_answer': 'D'
    },
    # Q36: stem underline
    36: {
        'stem': "Toward the new business wave, the writer's attitude can be said to be ________.",
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q38: stem underline
    38: {
        'stem': "The writer's experiment shows that downshifting ________.",
        'answer': 'B',
        'correct_answer': 'B'
    },
    # Q39: stem underline
    39: {
        'stem': '"Juggling one\'s life" probably means living a life characterized by ________.',
        'answer': 'C',
        'correct_answer': 'C'
    },
    # Q40: stem underline
    40: {
        'stem': 'According to the passage, downshifting emerged in the US as a result of ________.',
        'answer': 'D',
        'correct_answer': 'D'
    }
}

for q in exam_data.get('questions', []):
    qnum = q.get('sort_order')
    if qnum in q_updates:
        for k, v in q_updates[qnum].items():
            q[k] = v
            
    old_exp = q.get('explanation', '')
    clean_exp = get_clean_exp(qnum, old_exp)
    q['explanation'] = clean_exp

# Save updated exam JSON
with open(exam_file, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"Successfully calibrated 2001 exam JSON to {exam_file}!")
