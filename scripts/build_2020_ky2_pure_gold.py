# -*- coding: utf-8 -*-
"""
build_2020_ky2_pure_gold.py
Forensic Calibration & Full Golden Reconstruction for 2020 ky2
Exam UUID: ee996af1-3aaa-5380-9465-08125c4db713
"""

import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_id = "ee996af1-3aaa-5380-9465-08125c4db713"
json_path = f"public/data/exams/{exam_id}.json"

with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Official Title
official_title = "2020年全国硕士研究生招生考试英语（二）真题"
exam_data['title'] = official_title
if 'exam' in exam_data:
    exam_data['exam']['title'] = official_title

# 2. Golden Passages P0-P5
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

passages = exam_data.get('passages', [])
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

print("Passages P0-P5 calibrated successfully!")
