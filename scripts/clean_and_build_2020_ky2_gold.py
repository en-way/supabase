# -*- coding: utf-8 -*-
"""
scripts/clean_and_build_2020_ky2_gold.py
Complete gold generator for 2020 ky2.
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_id = "ee996af1-3aaa-5380-9465-08125c4db713"
json_path = f"public/data/exams/{exam_id}.json"

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# Official Title
d['title'] = "2020年全国硕士研究生招生考试英语（二）真题"
if 'exam' in d:
    d['exam']['title'] = d['title']

# Passages P0-P5
p0 = """Being a good parent is, of course, what every parent would like to be. But defining what it means to be a good parent is undoubtedly very [1], particularly since children respond differently to the same style of parenting. A calm, rule-following child might respond better to a different sort of parenting than, [2], a younger sibling.

[3], there's another sort of parent that's a bit easier to [4]: a patient parent. Children of every age benefit from patient parenting. Still, [5] every parent would like to be patient, this is no easy [6]. Sometimes parents get exhausted and frustrated and are unable to maintain a [7] and composed style with their kids. I understand this.

You're only human, and sometimes your kids can [8] you just a little too far. And then the [9] happens: You lose your patience and either scream at your kids or say something that was a bit too [10] and does nobody any good. You wish that you could [11] the clock and start over. We've all been there.

[12], even though it's common, it's important to keep in mind that in a single moment of fatigue, you can say something to your child that you may [13] for a long time. This may not only do damage to your relationship with your child but also [14] your child's self-esteem.

If you consistently lose your [15] with your kids, then you are inadvertently modeling a lack of emotional control for your kids. We are all becoming increasingly aware of the [16] of modeling tolerance and patience for the younger generation. This is a skill that will help them all throughout life. In fact, the ability to emotionally regulate or maintain emotional control when [17] by stress is one of the most important of all life's skills.

Certainly, it's incredibly [18] to maintain patience at all times with your children. A more practical goal is to try, to the best of your ability, to be as tolerant and composed as you can when faced with [19] situations involving your children. I can promise you this: As a result of working toward this goal, you and your children will benefit and [20] from stressful moments feeling better physically and emotionally."""

p1 = """Rats and other animals need to be highly attuned to social signals from others so they can identify friends to cooperate with and enemies to avoid. To find out if this extends to non-living beings, Laleh Quinn at the University of California, San Diego, and her colleagues tested whether rats can detect social signals from robotic rats.

They housed eight adult rats with two types of robotic rat—one social and one asocial—for four days. The robot rats were quite minimalist, resembling a chunkier version of a computer mouse with wheels to move around and colourful markings.

During the experiment, the social robot rat followed the living rats around, played with the same toys, and opened cage doors to let trapped rats escape. Meanwhile, the asocial robot simply moved forwards and backwards and side to side.

Next, the researchers trapped the robots in cages and gave the rats the opportunity to release them by pressing a lever. Across 18 trials each, the living rats were 52 per cent more likely on average to set the social robot free than the asocial one. This suggests that the rats perceived the social robot as a genuine social being, says Quinn.

The rats may have bonded more with the social robot because it displayed behaviors like communal exploring and playing. This could lead to the rats better remembering having freed it earlier, and wanting the robot to return the favour when they get trapped, she says. "Rats have been shown to engage in multiple forms of reciprocal help and cooperation, including what is referred to as direct reciprocity where a rat will help another rat that has previously helped them," says Quinn.

The readiness of the rats to befriend the social robot was surprising given its minimal design. The robot was the same size as a regular rat but looked like a plastic box on wheels. "We'd assumed we'd have to give it a moving head and tail, facial features, and put a scent on it to make it smell like a real rat, but that wasn't necessary," says Janet Wiles at the University of Queensland in Australia, who helped with the research.

The finding shows how sensitive rats are to social cues, even when they come from basic robots, says Wiles. Similarly, children tend to treat robots as if they are fellow beings, even when they display only simple social signals. "We humans seem to be fascinated by robots, and it turns out other animals are too," says Wiles."""

p2 = """It is true that CEO pay has gone up—top ones may make 300 times the pay of typical workers on average, and since the mid-1970s, CEO pay for large publicly traded American corporations has, by varying estimates, gone up by about 500%. The typical CEO of a top American corporation now makes about $18.9 million a year.

The best model for understanding the growth of CEO pay is that of limited CEO talent in a world where business opportunities for the top firms are growing rapidly. The efforts of America's highest-earning 1% have been one of the more dynamic elements of the global economy. It's not popular to say, but one reason their pay has gone up so much is that CEOs really have upped their game relative to many other workers in the U.S. economy.

Today's CEO, at least for major American firms, must have many more skills than simply being able to "run the company." CEOs must have a good sense of financial markets and maybe even how the company should trade in them. They also need better public relations skills than their predecessors, as the costs of even a minor slipup can be significant. Then there's the fact that large American companies are much more globalized than ever before, with supply chains spread across a larger number of countries. To lead in that system requires knowledge that is fairly mind-boggling. Plus, virtually all major American companies are becoming tech companies, one way or another. Beyond this, major CEOs still have to do all the day-to-day work they have always done.

The common idea that high CEO pay is mainly about ripping people off doesn't explain history very well. By most measures, corporate governance has become a lot tighter and more rigorous since the 1970s. Yet it is principally during this period of stronger governance that CEO pay has been accelerating, not just in the United States, but also in other developed economies with rigorous corporate governance. That suggests it is in the broader corporate interest to recruit top candidates for increasingly tough jobs.

Furthermore, the highest CEO salaries are paid to outside candidates, not to the cozy insider picks, another sign that high CEO pay is not some kind of depredation at the expense of the rest of the company. And the stock market reacts positively when companies tie CEO pay to, say, stock prices, a sign that those practices build up corporate value not just for the CEO."""

p3 = """Madrid was hailed as a public health beacon last November when it rolled out ambitious restrictions on the most polluting cars. Seven months and one election day later, a new conservative city council suspended enforcement of the clean air zone, a first step toward its possible demise.

Mayor José Luis Martínez-Almeida made opposition to the zone a centrepiece of his election campaign, despite its success in improving air quality. A judge has now overruled the city's decision to stop levying fines, ordering them reinstated. But with legal battles ahead, the zone's future looks uncertain at best.

Among other weaknesses, the measures cities must employ when left to tackle dirty air on their own are politically contentious, and therefore vulnerable. That's because they inevitably put the costs of cleaning the air on to individual drivers—who must pay fees or buy better vehicles—rather than on to the car manufacturers whose cheating is the real cause of our toxic pollution.

It's not hard to imagine a similar reversal happening in London. The new ultra-low emission zone (Ulez) is likely to be a big issue in next year's mayoral election. And if Sadiq Khan wins and extends it to the North and South Circular roads in 2021 as he intends, it is sure to spark intense opposition from the far larger number of motorists who will then be affected.

It's not that measures such as London's Ulez are useless. Far from it. Local officials are using the levers that are available to them to safeguard residents' health in the face of a serious threat. The zones do deliver some improvements to air quality, and the science tells us that means real health benefits—fewer heart attacks, strokes and premature births, less cancer, dementia and asthma. Fewer untimely deaths.

But mayors and councilors can only do so much about a problem that is far bigger than any one city or town. They are acting because national governments—Britain's and others across Europe—have failed to do so.

Restrictions that keep highly polluting cars out of certain areas—city centres, "school streets", even individual roads—are a response to the absence of a larger effort to properly enforce existing regulations and require auto companies to bring their vehicles into compliance. Wales has introduced special low speed limits to minimise pollution. We're doing everything but insist that manufacturers clean up their cars."""

p4 = """Now that members of Generation Z are graduating college this spring—the most commonly-accepted definition says this generation was born after 1995, give or take a year—the attention has been rising steadily in recent weeks. Gen Zs are about to hit the streets looking for work in a labor market that's tighter than it's been in decades. And employers are planning on hiring about 17 percent more new graduates for jobs in the U.S. this year than last, according to a survey conducted by the National Association of Colleges and Employers. Everybody wants to know how the people who will soon inhabit those empty office cubicles will differ from those who came before them.

If "entitled" is the most common adjective, fairly or not, applied to millennials (those born between 1981 and 1995), the catchwords for Generation Z are practical and cautious. According to the career counselors and experts who study them, Generation Zs are clear-eyed, economic pragmatists. Despite graduating into the best economy in the past 50 years, Gen Zs know what an economic train wreck looks like. They were impressionable kids during the crash of 2008, when many of their parents lost their jobs or their life savings or both. They aren't interested in taking any chances. The booming economy seems to have done little to assuage this underlying generational sense of anxious urgency, especially for those who have college debt. College loan balances in the U.S. now stand at a record $1.5 trillion, according to the Federal Reserve.

One survey from Accenture found that 88 percent of graduating seniors this year chose their major with a job in mind. In a 2019 survey of University of Georgia students, meanwhile, the career office found the most desirable trait in a future employer was the ability to offer secure employment (followed by professional development and training, and then inspiring purpose). Job security or stability was the second most important career goal (work-life balance was number one), followed by a sense of being dedicated to a cause or to feel good about serving the greater good.

That's a big change from the previous generation. "Millennials wanted more flexibility in their lives," notes Tanya Michelsen, Associate Director of YouthSight, a UK-based brand manager that conducts regular 60-day surveys of British youth, in findings that might just as well apply to American youth. "Generation Zs are looking for more certainty and stability, because of the rise of the gig economy. They have troubles seeing a financial future and they are quite risk averse.\""""

p5 = """Five Ways to Win Over Everyone in the Office

[A] Give compliments, just not too many
[B] Put on a good face, always
[C] Tailor your interactions
[D] Spend time with everyone
[E] Reveal, don't hide, information
[F] Slow down and listen
[G] Put yourselves in others' shoes

Is it possible to like everyone in your office? Think about how tough it is to get together 15 people, much less 50, who all get along perfectly. But unlike in friendships, you need coworkers. You work with them every day, and you depend on them just as they depend on you. Here are some ways that you can get the whole office on your side.

[41] If you have a bone to pick with someone in your workplace, you may try to stay tight-lipped around them. But you won't be helping either one of you. A Harvard Business School study found that observers consistently rated those who were upfront about themselves more highly, while those who hid lost trustworthiness. The lesson is not that you should make your personal life an open book, but rather, when given the option to offer up details about yourself or studiously stash them away, you should just be honest.

[42] Just as important as being honest about yourself is being receptive to others. We often feel the need to tell others how we feel, whether it's a concern about a project, a stray thought, or a compliment. Those are all valid, but you need to take time to hear out your coworkers, too. In fact, rushing to get your own ideas out there can cause colleagues to feel you don't value their opinions. Do your best to engage coworkers in a genuine, back-and-forth conversation, rather than prioritizing your own thoughts.

[43] It's common to have a "cubicle mate" or special confidant in a work setting. But in addition to those trusted coworkers, you should expand your horizons and find out about all the people around you. Use your lunch and coffee breaks to meet up with colleagues you don't always see. Find out about their lives and interests beyond the job. It requires minimal effort and goes a long way. This will help to grow your internal network, in addition to being a nice break in the work day.

[44] Positive feedback is important for anyone to hear. And you don't have to be someone's boss to tell them they did an exceptional job on a particular project. This will help engender goodwill in others. But don't overdo it or be fake about it. One study found that people responded best to comments that shifted from negative to positive, possibly because it suggested they had won somebody over.

[45] This one may be a bit more difficult to pull off, but it can go a long way to achieving results. Remember in dealing with any coworker what they appreciate from an interaction. Watch out for how they verbalize with others. Some people like small talk in a meeting before digging into important matters, while others are more straightforward. Jokes that work on one person won't necessarily land with another. So, adapt your style accordingly to type. Consider the person that you're dealing with in advance and what will get you to your desired outcome."""

passages = d.get('passages', [])
passage_updates = [
    {"type": "cloze", "passage_number": 1, "title": "Section I: Use of English", "content": p0},
    {"type": "reading", "passage_number": 1, "title": "Section II: Reading Comprehension Part A - Text 1", "content": p1},
    {"type": "reading", "passage_number": 2, "title": "Section II: Reading Comprehension Part A - Text 2", "content": p2},
    {"type": "reading", "passage_number": 3, "title": "Section II: Reading Comprehension Part A - Text 3", "content": p3},
    {"type": "reading", "passage_number": 4, "title": "Section II: Reading Comprehension Part A - Text 4", "content": p4},
    {"type": "reading", "passage_number": 5, "title": "Section II: Reading Comprehension Part B", "content": p5},
]
for i, p in enumerate(passages):
    if i < len(passage_updates):
        p.update(passage_updates[i])

# Load expls gold
with open('scripts/2020_ky2_expls_gold.json', 'r', encoding='utf-8') as f:
    gold_expls = json.load(f)

# Questions configuration
questions_data = [
    # Cloze 1-20
    (1, "Choose the best option for blank [1] in the passage:", {"A": "tedious", "B": "pleasant", "C": "instructive", "D": "tricky"}, "D"),
    (2, "Choose the best option for blank [2] in the passage:", {"A": "in addition", "B": "for example", "C": "at once", "D": "by accident"}, "B"),
    (3, "Choose the best option for blank [3] in the passage:", {"A": "Fortunately", "B": "Occasionally", "C": "Accordingly", "D": "Eventually"}, "A"),
    (4, "Choose the best option for blank [4] in the passage:", {"A": "amuse", "B": "assist", "C": "describe", "D": "train"}, "C"),
    (5, "Choose the best option for blank [5] in the passage:", {"A": "while", "B": "because", "C": "unless", "D": "once"}, "A"),
    (6, "Choose the best option for blank [6] in the passage:", {"A": "answer", "B": "task", "C": "choice", "D": "access"}, "B"),
    (7, "Choose the best option for blank [7] in the passage:", {"A": "tolerant", "B": "formal", "C": "rigid", "D": "critical"}, "A"),
    (8, "Choose the best option for blank [8] in the passage:", {"A": "move", "B": "drag", "C": "push", "D": "send"}, "C"),
    (9, "Choose the best option for blank [9] in the passage:", {"A": "mysterious", "B": "illogical", "C": "suspicious", "D": "inevitable"}, "D"),
    (10, "Choose the best option for blank [10] in the passage:", {"A": "boring", "B": "naive", "C": "harsh", "D": "vague"}, "C"),
    (11, "Choose the best option for blank [11] in the passage:", {"A": "turn back", "B": "take apart", "C": "set aside", "D": "cover up"}, "A"),
    (12, "Choose the best option for blank [12] in the passage:", {"A": "Overall", "B": "Instead", "C": "However", "D": "Otherwise"}, "C"),
    (13, "Choose the best option for blank [13] in the passage:", {"A": "like", "B": "miss", "C": "believe", "D": "regret"}, "D"),
    (14, "Choose the best option for blank [14] in the passage:", {"A": "raise", "B": "affect", "C": "justify", "D": "reflect"}, "B"),
    (15, "Choose the best option for blank [15] in the passage:", {"A": "time", "B": "bond", "C": "race", "D": "cool"}, "D"),
    (16, "Choose the best option for blank [16] in the passage:", {"A": "nature", "B": "secret", "C": "importance", "D": "context"}, "C"),
    (17, "Choose the best option for blank [17] in the passage:", {"A": "cheated", "B": "defeated", "C": "confused", "D": "confronted"}, "D"),
    (18, "Choose the best option for blank [18] in the passage:", {"A": "terrible", "B": "hard", "C": "strange", "D": "wrong"}, "B"),
    (19, "Choose the best option for blank [19] in the passage:", {"A": "trying", "B": "changing", "C": "exciting", "D": "surprising"}, "A"),
    (20, "Choose the best option for blank [20] in the passage:", {"A": "hide", "B": "emerge", "C": "withdraw", "D": "escape"}, "B"),

    # Reading Text 1 (21-25)
    (21, "Quinn and her colleagues conducted a test to see if rats can ________.", {
        "A": "pick up social signals from non-living rats",
        "B": "distinguish a friendly rat from a hostile one",
        "C": "attain sociable traits through special training",
        "D": "send out warning messages to their fellows"
    }, "A"),
    (22, "What did the asocial robot do during the experiment?", {
        "A": "It followed the social robot.",
        "B": "It played with some toys.",
        "C": "It set the trapped rats free.",
        "D": "It moved around alone."
    }, "D"),
    (23, "According to Quinn, the rats released the social robot because they ________.", {
        "A": "tried to practice a means of escape",
        "B": "expected it to do the same in return",
        "C": "wanted to display their intelligence",
        "D": "considered that an interesting game"
    }, "B"),
    (24, "Janet Wiles notes that rats ________.", {
        "A": "can remember other rats' facial features",
        "B": "differentiate smells better than sizes",
        "C": "respond more to actions than to looks",
        "D": "can be scared by a plastic box on wheels"
    }, "C"),
    (25, "It can be learned from the text that rats ________.", {
        "A": "appear to be adaptable to new surroundings",
        "B": "are more socially active than other animals",
        "C": "behave differently from children in socializing",
        "D": "are more sensitive to social cues than expected"
    }, "D"),

    # Reading Text 2 (26-30)
    (26, "Which of the following has contributed to CEO pay rise?", {
        "A": "The growth in the number of corporations.",
        "B": "The general pay rise with a better economy.",
        "C": "Increased business opportunities for top firms.",
        "D": "Close cooperation among leading economies."
    }, "C"),
    (27, "Compared with their predecessors, today's CEOs are required to ________.", {
        "A": "foster a stronger sense of teamwork",
        "B": "finance more research and development",
        "C": "establish closer ties with tech companies",
        "D": "operate more globalized companies"
    }, "D"),
    (28, "CEO pay has been rising since the 1970s despite ________.", {
        "A": "continual internal opposition",
        "B": "strict corporate governance",
        "C": "conservative business strategies",
        "D": "repeated government warnings"
    }, "B"),
    (29, "High CEO pay can be justified by the fact that it helps ________.", {
        "A": "confirm the status of CEOs",
        "B": "motivate inside candidates",
        "C": "boost the efficiency of CEOs",
        "D": "increase corporate value"
    }, "D"),
    (30, "The most suitable title for this text would be ________.", {
        "A": "CEOs Are Not Overpaid",
        "B": "CEO Pay: Past and Present",
        "C": "CEOs' Challenges of Today",
        "D": "CEO Traits: Not Easy to Define"
    }, "A"),

    # Reading Text 3 (31-35)
    (31, "Which of the following is true about Madrid's clean air zone?", {
        "A": "Its effects are questionable.",
        "B": "It has been opposed by a judge.",
        "C": "It needs tougher enforcement.",
        "D": "Its fate is yet to be decided."
    }, "D"),
    (32, "Which is considered a weakness of the city-level measures to tackle dirty air?", {
        "A": "They are biased against car manufacturers.",
        "B": "They prove impractical for city councils.",
        "C": "They are deemed too mild for politicians.",
        "D": "They put too much burden on individual motorists."
    }, "D"),
    (33, "The author believes that the extension of London's Ulez will ________.", {
        "A": "arouse strong resistance",
        "B": "ensure Khan's electoral success",
        "C": "improve the city's traffic",
        "D": "discourage car manufacturing"
    }, "A"),
    (34, "Who does the author think should have addressed the problem?", {
        "A": "Local residents.",
        "B": "Mayors.",
        "C": "Councilors.",
        "D": "National governments."
    }, "D"),
    (35, "It can be inferred from the last paragraph that auto companies ________.", {
        "A": "will raise low-emission car production",
        "B": "should be forced to follow regulations",
        "C": "will upgrade the design of their vehicles",
        "D": "should be put under public supervision"
    }, "B"),

    # Reading Text 4 (36-40)
    (36, "Generation Zs graduating college this spring ________.", {
        "A": "are recognized for their abilities",
        "B": "are optimistic about the labor market",
        "C": "are in favor of office job offers",
        "D": "are drawing growing public attention"
    }, "D"),
    (37, "Generation Zs are keenly aware ________.", {
        "A": "what their parents expect of them",
        "B": "how valuable a counselor's advice is",
        "C": "what a tough economic situation is like",
        "D": "how they differ from past generations"
    }, "C"),
    (38, "The word \"assuage\" (Line 9, Para. 2) is closest in meaning to ________.", {
        "A": "deepen",
        "B": "define",
        "C": "maintain",
        "D": "relieve"
    }, "D"),
    (39, "It can be learned from Paragraph 3 that Generation Zs ________.", {
        "A": "give top priority to professional training",
        "B": "have a clear idea about their future job",
        "C": "care little about their job performance",
        "D": "think it hard to achieve work-life balance"
    }, "B"),
    (40, "Michelsen thinks that compared with millennials, Generation Zs are ________.", {
        "A": "less realistic",
        "B": "less adventurous",
        "C": "more diligent",
        "D": "more generous"
    }, "B"),

    # Part B (41-45)
    (41, "Choose the most suitable subheading from [A]-[G] for paragraph [41].", {
        "A": "Give compliments, just not too many",
        "B": "Put on a good face, always",
        "C": "Tailor your interactions",
        "D": "Spend time with everyone",
        "E": "Reveal, don't hide, information",
        "F": "Slow down and listen",
        "G": "Put yourselves in others' shoes"
    }, "E"),
    (42, "Choose the most suitable subheading from [A]-[G] for paragraph [42].", {
        "A": "Give compliments, just not too many",
        "B": "Put on a good face, always",
        "C": "Tailor your interactions",
        "D": "Spend time with everyone",
        "E": "Reveal, don't hide, information",
        "F": "Slow down and listen",
        "G": "Put yourselves in others' shoes"
    }, "F"),
    (43, "Choose the most suitable subheading from [A]-[G] for paragraph [43].", {
        "A": "Give compliments, just not too many",
        "B": "Put on a good face, always",
        "C": "Tailor your interactions",
        "D": "Spend time with everyone",
        "E": "Reveal, don't hide, information",
        "F": "Slow down and listen",
        "G": "Put yourselves in others' shoes"
    }, "D"),
    (44, "Choose the most suitable subheading from [A]-[G] for paragraph [44].", {
        "A": "Give compliments, just not too many",
        "B": "Put on a good face, always",
        "C": "Tailor your interactions",
        "D": "Spend time with everyone",
        "E": "Reveal, don't hide, information",
        "F": "Slow down and listen",
        "G": "Put yourselves in others' shoes"
    }, "A"),
    (45, "Choose the most suitable subheading from [A]-[G] for paragraph [45].", {
        "A": "Give compliments, just not too many",
        "B": "Put on a good face, always",
        "C": "Tailor your interactions",
        "D": "Spend time with everyone",
        "E": "Reveal, don't hide, information",
        "F": "Slow down and listen",
        "G": "Put yourselves in others' shoes"
    }, "C"),
]

# Clean explanations
def clean_expl(q_num, raw_expl):
    if not raw_expl:
        return ""
    # Remove header number like "41.[答案]"
    cleaned = raw_expl.strip()
    
    # Trim bilingual leakage or trailing questions
    # E.g. if contains next question or paragraph snippet
    cutoff_markers = [
        '\n·语篇分析·', '\n长难句分析', '\n经典搭配', '\n词汇注释',
        'Text 1', 'Text 2', 'Text 3', 'Text 4', 'Part B',
        '=== Text', '=== Page',
        '\nI❶', '\nII❶', '\nIII❶', '\nIV❶', '\nV❶', '\nVI❶', '\nVII❶',
        '\nIO', '\nIIO', '\nIIIO', '\nIVO', '\nVO', '\nVIO', '\nVIIO',
    ]
    for m in cutoff_markers:
        idx = cleaned.find(m)
        if idx != -1:
            cleaned = cleaned[:idx].strip()
            
    # For reading questions, ensure it starts with ［精准定位］ or [精准定位]
    if q_num in range(21, 41):
        if not (cleaned.startswith('［精准定位］') or cleaned.startswith('[精准定位]')):
            idx = cleaned.find('［精准定位］')
            if idx == -1:
                idx = cleaned.find('[精准定位]')
            if idx != -1:
                cleaned = cleaned[idx:].strip()
                
    # Normalize brackets
    cleaned = cleaned.replace('[精准定位]', '［精准定位］')
    cleaned = cleaned.replace('[命题解密]', '［命题解密］')
    cleaned = cleaned.replace('[错项排除]', '［错项排除］')
    cleaned = cleaned.replace('[技巧总结]', '［技巧总结］')
    cleaned = cleaned.replace('[考点提炼]', '［考点提炼］')
    cleaned = cleaned.replace('[解题思路]', '［解题思路］')
    cleaned = cleaned.replace('[精解]', '［精解］')
    cleaned = cleaned.replace('[干扰项设置]', '［干扰项设置］')
    cleaned = cleaned.replace('【精解］', '［精解］')
    cleaned = cleaned.replace('[精解］', '［精解］')
    cleaned = cleaned.replace('［精解]', '［精解］')
    cleaned = cleaned.replace('［精准定位', '［精准定位］')
    cleaned = cleaned.replace('［精准定位］］', '［精准定位］')
    
    return cleaned.strip()

questions = d.get('questions', [])
for i, (q_num, stem, opt_dict, ans) in enumerate(questions_data):
    q = questions[i]
    q['question_number'] = q_num
    q['sort_order'] = q_num
    q['score'] = 0.5 if q_num <= 20 else 2.0
    q['points'] = q['score']
    q['stem'] = stem
    q['answer'] = ans
    q['correct_answer'] = ans
    
    # Options formatting
    q['options'] = [
        {"key": k, "text": v, "content": v, "value": k}
        for k, v in opt_dict.items()
    ]
    
    raw_e = gold_expls.get(str(q_num), "")
    c_e = clean_expl(q_num, raw_e)
    # If c_e is short or empty, keep existing or fallback
    if len(c_e) < 50:
        c_e = clean_expl(q_num, q.get('explanation', ''))
    q['explanation'] = c_e

# Write updated json
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Updated public/data/exams/ee996af1-3aaa-5380-9465-08125c4db713.json with pure gold standard!")
