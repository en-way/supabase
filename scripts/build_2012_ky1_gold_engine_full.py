# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Writing build_2012_ky1_gold_engine_full.py...")

# We will read existing json to get IDs
json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\baa66182-74ec-5a78-b2d2-077ffdcad9dc.json'
with open(json_path, encoding='utf-8') as f:
    old_data = json.load(f)

exam_id = "baa66182-74ec-5a78-b2d2-077ffdcad9dc"
exam_title = "2012年全国硕士研究生入学统一考试英语（一）真题"

# Passages
p0_content = (
    "The ethical judgments of the Supreme Court justices have become an important issue recently. "
    "The court cannot [1] its legitimacy as guardian of the rule of law [2] justices behave like politicians. "
    "Yet, in several instances, justices acted in ways that [3] the court's reputation for being independent and impartial.\n\n"
    "Justice Antonin Scalia, for example, appeared at political events. That kind of activity makes it less likely "
    "that the court's decisions will be [4] as impartial judgments. Part of the problem is that the justices are "
    "not [5] by an ethics code. At the very least, the court should make itself [6] to the code of conduct that "
    "[7] to the rest of the federal judiciary.\n\n"
    "This and other similar cases [8] the question of whether there is still a [9] between the court and politics.\n\n"
    "The framers of the Constitution envisioned law [10] having authority apart from politics. They gave justices "
    "permanent positions [11] they would be free to [12] those in power and have no need to [13] political support. "
    "Our legal system was designed on the assumption that continued tying of law to politics would be dangerous. "
    "It was designed [14] to separate the two.\n\n"
    "Constitutional law is political because it results from choices between different [15] of liberty and property. "
    "But the court's decisions ought to be made according to principle, not based on politics. When the court departs "
    "from that rule, and allows politics to [16] its judgment, it loses its authority apart from politics. That makes "
    "it easier for decisions with which people disagree to be [17] as political rather than judicial.\n\n"
    "The justices must [18] doubts about the court's legitimacy by making themselves [19] to the code of conduct. "
    "That would make it more likely that the court's decisions will be seen as separate from politics and, [20], "
    "convincing as law."
)

p1_content = (
    "Come on — everybody's doing it. That whispered message, half invitation and half forcing, is what most of us "
    "think of when we hear the words peer pressure. It usually leads to no good — drinking, drugs and casual sex. "
    "But in her new book Join the Club, Tina Rosenberg contends that peer pressure can also be a positive force "
    "through what she calls the social cure, in which organizations and officials use the power of group dynamics "
    "to help individuals improve their lives and possibly the world.\n\n"
    "Rosenberg, the recipient of a Pulitzer Prize, offers a host of examples of the social cure in action: In South "
    "Carolina, a state-sponsored antismoking program called Rage Against the Haze sets out to make cigarettes uncool. "
    "In South Africa, an HIV-prevention initiative known as loveLife recruits young people to promote safe sex among their peers.\n\n"
    "The idea seems promising, and Rosenberg is a perceptive observer. Her critique of the lameness of many public-health "
    "campaigns is spot-on: they fail to mobilize peer pressure for healthy habits, and they demonstrate a seriously "
    "flawed understanding of psychology. \"Dare to be different, please don't smoke!\" pleads one billboard campaign "
    "aimed at reducing smoking among teenagers — teenagers who desire nothing more than fitting in. Rosenberg argues "
    "convincingly that public-health advocates ought to take a page from advertisers, so skilled at applying peer pressure.\n\n"
    "But on the general effectiveness of the social cure, Rosenberg is less persuasive. Join the Club is filled with "
    "too much irrelevant detail and not enough exploration of the social and biological mechanisms that make peer pressure "
    "so powerful. Now and again, the author glimpses the truth: that the flaw of the social cure is that it cannot provide "
    "a long-lasting cure. It doesn't work very well for very long. The trouble with Rage Against the Haze is that the "
    "funded billboard campaigns and events will not be sustained forever; indeed, in South Carolina, the number of young "
    "smokers rebounded after state funding was cut. Meanwhile, in South Africa, evidence that loveLife produces lasting "
    "changes is limited and mixed.\n\n"
    "There's no doubt that our peer groups exert enormous influence on our behavior. An emerging body of research shows "
    "that positive health habits — as well as negative ones — spread through networks of friends via social communication. "
    "This is a subtle form of peer pressure: we unconsciously imitate the behavior we see every day.\n\n"
    "Far less certain, however, is how successfully experts and bureaucrats can select our peer groups and steer their "
    "activities in virtuous directions. It's like the teacher who breaks up the troublemakers in the back row by pairing "
    "them with better-behaved classmates. The tactic never really works. And that's the problem with a social cure "
    "engineered from the outside: in the real world, as in school, we insist on choosing our own friends."
)

p2_content = (
    "A deal is a deal — except, apparently, when Entergy is involved. The company, a major energy supplier in New England, "
    "provoked justified outrage in Vermont last week when it announced it was reneging on a longstanding commitment to abide "
    "by the state's strict nuclear regulations.\n\n"
    "Instead, the company has done precisely what it had long promised it would not: challenge the constitutionality of "
    "Vermont's rules in the federal court, as part of a desperate effort to keep its Vermont Yankee nuclear power plant "
    "running. It's a stunning move.\n\n"
    "The conflict has been surfacing since 2002, when the corporation bought Vermont Yankee and negotiated an agreement with "
    "state regulators to keep the products moving. The plant was scheduled to open up in 2012, and Entergy offered to apply "
    "for state permission if it wished to keep the plant open longer. But Entergy went further: Entergy agreed that it would "
    "need the legislature's approval. Then, too, the company went along.\n\n"
    "Either Entergy never really intended to live by those commitments, or it underestimated the Vermont public's resistance "
    "to nuclear power. A string of accidents, including a partial collapse of a cooling tower in 2007 and the discovery of "
    "underground tritium leakage in 2010, raised serious questions about the plant's safety and Entergy's management. "
    "The Senate in Vermont voted 26 to 4 last year against allowing an extension.\n\n"
    "Now the company is suddenly claiming that the 2002 agreement is invalid because of the 2006 legislation, and that "
    "only the federal Nuclear Regulatory Commission (NRC) has the authority to determine whether the plant is safe enough "
    "to operate and whether its license should be extended. But if the company had kept its word, that debate would be "
    "beside the point.\n\n"
    "The company seems to have concluded that its reputation in Vermont is already so damaged that it has nothing left "
    "to lose: By suing the state, it has admitted that it would rather take its chances with a federal judge than with "
    "the state's regulators, but it has also lost any claim to being an honest broker in Vermont. As Entergy sells its "
    "nuclear power across New England, it will likely find that Vermont is not the only state that will keep in mind "
    "what promises from Entergy are worth."
)

p3_content = (
    "In the idealized version of how science is done, facts about the world are waiting to be observed and collected "
    "by the objective researcher using the scientific method to carry out work. But in the everyday practice of science, "
    "discovery frequently follows an ambiguous and complicated route. We aim to be objective, but we can never completely "
    "escape the context of our unique life experience. Prior knowledge and interests influence what we experience, what "
    "we think our experiences mean, and the actions we take, so that the opportunities for misinterpretation, error, "
    "and self-deception abound.\n\n"
    "Consequently, discovery claims should be thought of as protoscience. Similar to newly staked mining claims, they "
    "are full of potential. But it takes collective scrutiny and acceptance to transform a discovery claim into a mature "
    "discovery. This is the credibility process, through which the individual researcher's me, here, now becomes the "
    "community's anyone, anywhere, anytime. Objective knowledge is the goal, not the starting point.\n\n"
    "Once a discovery claim becomes public, the discoverer receives intellectual credit for having made it. But the "
    "claim does not get accepted as fact until it gets confirmed. Usually this requires that other researchers try to "
    "duplicate the findings and that subsequent research cannot be made until the findings are confirmed. In the process, "
    "the original claim gets modified, broadened, and made more specific, as other researchers adapt it to their own "
    "purposes and contexts. In other words, a discovery claim works its way through the community, the idea is revised, "
    "its value tested, and its boundaries defined.\n\n"
    "Two paradoxes exist throughout this credibility process. First, scientific work tends to see itself as a solitary "
    "pursuit, but discovery is essentially a collective act. Second, the very nature of science is to doubt, yet discovery "
    "requires belief. For a discovery claim to be accepted, other scientists must believe in the honesty and competence "
    "of the discoverer, while simultaneously remaining skeptical of the claim itself.\n\n"
    "In the end, credibility \"happens\" to a discovery claim — a process which can take weeks, months, or even years. "
    "Annette Baier has described this process as \"the creation of trust between strangers who share a common commitment "
    "to the truth.\" As Albert Szent-Gyorgyi put it: \"Discovery consists of seeing what everybody has seen and thinking "
    "what nobody has thought.\" Through this collaborative crucible, provisional claims are transformed into established knowledge."
)

p4_content = (
    "If the trade unionist Jimmy Hoffa were alive today, he would probably represent civil servants. When Hoffa's "
    "Teamsters were in their prime in 1960, only one in ten American government workers belonged to a union; now 36% do. "
    "In 2009 the number of unionists in America's public sector passed that of their fellow members in the private sector. "
    "In Britain, more than half of public-sector workers but only about 15% of private-sector ones are unionized.\n\n"
    "There are three reasons for the public-sector unions' thriving. First, they can shut things down without suffering "
    "much in the way of consequences. Second, they are mostly bright and well-educated. A quarter of America's public-sector "
    "workers have a university degree. Third, they now dominate left-of-centre politics. Some of their ties go back a "
    "long way. Britain's Labor Party, as its name implies, has long been associated with trade unionism. Its current "
    "leader, Ed Miliband, owes his position to votes from public-sector unions.\n\n"
    "At the state level their influence can be even more fearsome. Mark Baldassare of the Public Policy Institute of "
    "California points out that much of the state's budget is patrolled by unions. The teachers' unions keep an eye on "
    "schools, the CCPOA on prisons and a variety of labor groups on health care.\n\n"
    "In many rich countries average wages in the state sector are higher than in the private one. But the real gains "
    "come in benefits and work practices. Politicians have repeatedly \"backloaded\" public-sector pay deals, keeping "
    "the pay increases modest but adding to holidays and especially pensions that are already generous.\n\n"
    "Reform has been vigorously opposed, perhaps most notoriously in education, where charter schools, academies and "
    "merit pay all faced drawn-out battles. Even though there is plenty of evidence that the quality of the teachers "
    "is the most important variable, teachers' unions have fought against getting rid of bad ones and promoting good ones.\n\n"
    "As the cost to everyone else has become clearer, politicians have begun to clamp down. In Wisconsin the unions "
    "have rallied thousands of supporters against Scott Walker, the hardline Republican governor. But many within the "
    "public sector suffer under the current system, too.\n\n"
    "John Donahue at Harvard's Kennedy School points out that the norms of culture in Western civil services suit those "
    "who want to stay put but is bad for high achievers. The only American public-sector workers who earn well above "
    "$250,000 a year are university sports coaches and the president of the United States. Bankers' fat pay packets "
    "have attracted much criticism, but a public-sector system that does not reward high achievers may be a much bigger "
    "problem for America."
)

p5_content = (
    "Think of those fleeting moments when you look out of an aeroplane window and realize that once, not so long ago, "
    "to look in this way was the province of only the gods and the birds. But having been thrilled by the astonishing "
    "sense of flight on our early journeys around the world, we now seem to treat it as entirely ordinary: an annoyance "
    "that takes up time, rather than an event that opens the mind.\n\n"
    "The second half of the 20th century saw a collection of geniuses, warriors, entrepreneurs and visionaries labour "
    "to create a fabulous machine that could function as a typewriter and printing press, studio and theatre, paintbrush "
    "and gallery, piano and radio, the mail as well as the mail carrier. [41] ________\n\n"
    "Anyone who has ever worked at an office desktop or curled up with a laptop in bed might be forgiven for thinking "
    "that the computer has finally fulfilled that promise. But the true significance of the computer is still emerging. [42] ________\n\n"
    "But for all the reasons there are to celebrate the computer, we must also be on our guard. Today, we are in danger "
    "of being seduced into a culture of consumption rather than production: of downloading other people's culture "
    "rather than creating our own.\n\n"
    "All animals download, but only a few upload. Beavers build dams and birds make nests. Yet for all the reasons "
    "there are to celebrate the computer, only humans make culture: they do so by translating their experiences into "
    "music, paintings, books and other creations, and then sharing them with others. [43] ________\n\n"
    "Yet for all the possibilities of our new culture machines, most people are still stuck in download mode. Even after "
    "the advent of widespread social media, a pyramid of production remains, with a small number of people uploading "
    "material, a slightly larger group commenting on or modifying that content, and a huge percentage remaining content "
    "to just consume. [44] ________\n\n"
    "For all the possibilities of our new culture machine, television is still the medium that shapes the world's "
    "culture. Television is a one-way tap: you open the valve and information flows out. [45] ________\n\n"
    "What counts as meaningful uploading? My definition revolves around the concept of \"stickiness\" — creations "
    "and experiences to which others adhere, which make a lasting impression on other people's minds and give them "
    "reason to think, feel or create something of their own.\n\n"
    "[A] Of course, it is precisely these superfluous things that define human culture and ultimately what it is to be "
    "human. Downloading and consuming culture requires great skills, but failing to move beyond downloading is to strip "
    "oneself of a defining constituent of humanity.\n\n"
    "[B] Applications like tumblr. com, which allow users to combine pictures, words and other media in creative ways "
    "and then share them, have the potential to add stickiness by amusing, entertaining and enlightening others.\n\n"
    "[C] Not only did they develop such a device but by the turn of the millennium they had also managed to embed it "
    "in a worldwide system accessed by billions of people every day.\n\n"
    "[D] This is because the networked computer has sparked a secret war between downloading and uploading — between "
    "passive consumption and active creation — whose outcome will shape our collective future in ways we can only begin "
    "to imagine.\n\n"
    "[E] The challenge the computer mounts to television thus bears little similarity to one format being replaced by "
    "another in the manner of record players being replaced by CD players.\n\n"
    "[F] One reason for the persistence of this pyramid of production is that for the past half-century, much of the "
    "world's media culture has been defined by a single medium — television — and television is defined by downloading.\n\n"
    "[G] The networked computer offers the first chance in 50 years to reverse that flow, to encourage thoughtful downloading "
    "and, even more importantly, meaningful uploading."
)

passages = [
    {
        "id": "482c849e-0293-5209-b118-0cd4c91aadb6",
        "exam_id": exam_id,
        "title": "Section I: Use of English",
        "type": "cloze",
        "passage_number": None,
        "content": p0_content
    },
    {
        "id": "dc3497d7-d11a-5683-85b6-cc12f1b7eba3",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part A - Text 1",
        "type": "reading",
        "passage_number": 1,
        "content": p1_content
    },
    {
        "id": "d2419589-e83f-5a1b-b3d0-3a82d1263fc4",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part A - Text 2",
        "type": "reading",
        "passage_number": 2,
        "content": p2_content
    },
    {
        "id": "eed30545-c966-5cf7-96bc-731f2ab56649",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part A - Text 3",
        "type": "reading",
        "passage_number": 3,
        "content": p3_content
    },
    {
        "id": "c6027e7b-c31e-5cc7-82a0-d71ff57c6931",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part A - Text 4",
        "type": "reading",
        "passage_number": 4,
        "content": p4_content
    },
    {
        "id": "06091d69-1e9a-56f8-9520-8ebd89db8bbd",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part B",
        "type": "reading_part_b",
        "passage_number": 5,
        "content": p5_content
    }
]

print("Passages structured successfully.")
