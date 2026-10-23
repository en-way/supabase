# -*- coding: utf-8 -*-
"""
Round 62: 2015 ky1 Gold Engine
Performs forensic reconstruction of 2015 English (One) exam:
- Exam metadata normalization (title, total_score)
- Passages 0-5 gold reconstruction (clean structure, restored sentences, no OCR footnotes, no directions in text)
- Questions 1-45 gold reconstruction (question_number 1..45, points 0.5/2.0, q_type, options, answers, cleaned explanations)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
import re

EXAM_PATH = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\865e5af8-24a4-58e1-bc9e-640f32d8e946.json"

with open(EXAM_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. Update Exam Metadata
exam = data["exam"]
exam["title"] = "2015年全国硕士研究生招生考试英语（一）真题"
exam["total_score"] = 60.0

# 2. Reconstruct Passages
passages = data["passages"]

p0_content = """Though not biologically related, friends are as "related" as fourth cousins, sharing about 1% of genes. That is [1] a study, published from the University of California and Yale University in the Proceedings of the National Academy of Sciences, has [2].

The study is a genome-wide analysis [3] 1,932 unique subjects which [4] pairs of unrelated friends and pairs of unrelated strangers. The same type of data was used for [5]. While 1% may seem [6], to geneticists it is a significant number. Most people do not even [7] their fourth cousins but somehow choose to [8] who they are related to.

The study [9] found that the genes for smell were something shared in friends but not genes for immunity. Why this is, is not understood. [10], it could be that smell draws us towards similar environments, but there is more [11] it than that. It could be that people are drawn to each other through many mechanisms that [12] us to choose friends with similar genes, [13] "functional kinship" of being friends with [14].

One of the remarkable findings of the study was that the similar genes seem to be evolving [15] than other genes. Studying this could help [16] why human evolution picked pace in the last 30,000 years, with social environment being a major [17] factor.

The findings do not simply explain people's [18] to befriend those of similar [19] backgrounds, say the researchers. Though all the subjects were drawn from a population of European extraction, care was taken to [20] that all subjects, friends and strangers were taken from the same population."""

p1_content = """King Juan Carlos of Spain once insisted that "kings don't abdicate, they die in their sleep." But embarrassing scandals and the popularity of the republican left in the recent Euro-elections have forced him to eat his words and stand down. So does the Spanish crisis suggest that monarchy is seeing its last days? Does that mean the writing is on the wall for all European royals, with their magnificent palaces and majestic pageants?

The Spanish case provides arguments both for and against monarchy. When public opinion is particularly polarized, as it was following the end of the Franco regime, monarchs can rise above "mere" politics and "embody" a spirit of national unity.

It is this apparent transcendence of politics that explains monarchs' continuing popularity as heads of state. And so, the Middle East excepted, Europe is the most monarch-infested region in the world, with 10 kingdoms (not counting Vatican city and Andorra). But unlike their absolutist counterparts in the Gulf and Asia, most royal families have survived because they allow voters to avoid the difficult search for a non-controversial but respected public figure.

Even so, kings and queens undoubtedly have a downside. Symbolic of national unity as they claim to be, their very history—and sometimes the way they behave today—embodies outdated and indefensible privileges and inequalities. At a time when Thomas Piketty and other economists are warning of rising inequality and the increasing power of inherited wealth, it is bizarre that wealthy aristocratic families should still be the symbolic heart of modern democratic states.

The most successful monarchies strive to abandon or hide their old aristocratic ways. They have day-jobs, ride bicycles, not horses (or helicopters). Even so, keeping a monarchical show on the road is becoming increasingly difficult in the era of rolling news and social media.

While Europe's monarchies will no doubt be smart enough to survive for some time to come, it is the British royals who have most to fear from the Spanish example.

It is only the Queen who has preserved the monarchy's reputation with her rather ordinary (if well-heeled) granny style. The danger will come with Charles, who has both an expensive taste of lifestyle and a pretty hierarchical view of the world. He has failed to understand that monarchies have largely survived because they provide a service—as non-controversial and non-political heads of state. Charles ought to know that as English history shows, it is kings, not republicans, who are the monarchy's worst enemies."""

p2_content = """Just how much does the Constitution protect your digital data? The Supreme Court will now consider whether police can search the contents of a mobile phone without a warrant if the phone is on or around a person during an arrest.

California has asked the justices to refrain from a sweeping ruling, particularly one that upsets the old assumption that authorities may search through the possessions of suspects at the time of their arrest. It is hard, the state argues, for judges to assess the implications of new and rapidly changing technologies.

The court would be recklessly modest if it followed California's advice. Enough of the implications are discernable, even obvious, so that the justices can and should provide updated guidelines to police, lawyers and defendants.

They should start by discarding California's lame argument that exploring the contents of a smartphone—a vast storehouse of digital information—is similar to, say, going through a suspect's purse. The court has ruled that police don't violate the Fourth Amendment when they go through the wallet or pocketbook of an arrestee without a warrant. But exploring one's smartphone is more like entering his or her home. A smartphone may contain an arrestee's reading history, financial history, medical history and comprehensive records of recent correspondence. The development of "cloud computing", meanwhile, has made that exploration so much the easier.

Americans should take steps to protect their digital privacy. But keeping sensitive information on these devices is increasingly a requirement of normal life. Citizens still have a right to expect private documents to remain private and protected by the Constitution's prohibition on unreasonable searches.

As so often is the case, stating that principle doesn't ease the challenge of line-drawing. In many cases, it would not be overly burdensome for authorities to obtain a warrant to search through phone contents. They could still invalidate Fourth Amendment protections when facing severe, urgent circumstances, and they could take reasonable measures to ensure that phone data are not erased or altered while waiting for a warrant. The court, though, may want to allow room for police to cite situations where they are entitled to more freedom.

But the justices should not swallow California's argument whole. New, disruptive technology sometimes demands novel applications of the Constitution's protections. Orin Kerr, a law professor, compares the explosion and accessibility of digital information in the 21st century with the establishment of automobile use as a virtual necessity of life in the 20th: The justices had to specify novel rules for the new personal domain of the passenger car then; they must sort out how the Fourth Amendment applies to digital information now."""

p3_content = """The journal Science is adding an extra round of statistical checks to its peer-review process, editor-in-chief Marcia McNutt announced today. The policy follows similar efforts from other journals, after widespread concern that basic mistakes in data analysis are contributing to the irreproducibility of many published research findings.

"Readers must have confidence in the conclusions published in our journal," writes McNutt in an editorial. Working with the American Statistical Association, the journal has appointed seven experts to a statistics board of reviewing editors (SBoRE). Manuscripts will be flagged up for additional scrutiny by the journal's internal editors, or by its existing Board of Reviewing Editors or by outside peer reviewers. The SBoRE panel will then find external statisticians to review these manuscripts.

Asked whether any particular papers had impelled the change, McNutt said: "The creation of the 'statistics board' was motivated by concerns broadly with the application of statistics and data analysis in scientific research and is part of Science's overall drive to increase reproducibility in the research we publish."

Giovanni Parmigiani, a biostatistician at the Harvard School of Public Health, a member of the SBoRE group, says he expects the board to "play primarily an advisory role." He considers the "need for and foresight behind the establishment of the SBoRE to be novelty," adding that the board's "major impact will not only be through the publications in Science itself, but hopefully through a larger group of publishing places that may want to model their approach after Science."

John Ioannidis, a physician who studies research methodology, says that the policy is "a most welcome step forward" and "long overdue." "Most journals are weak in statistical review, and this damages the quality of what they publish. I think that, for the majority of scientific papers nowadays, statistical review is more essential than expert review," he says. But he noted that biomedical journals such as Annals of Internal Medicine, the Journal of the American Medical Association and The Lancet pay strong attention to statistical review.

Professional scientists are expected to know how to analyse data, but statistical errors are alarmingly common in published research, according to David Vaux, a cell biologist at the Walter and Eliza Hall Institute of Medical Research in Parkville, Australia. Researchers should improve standards, he wrote in 2012, but journals should also take a tougher line, "engaging reviewers who are statistically literate and editors who can verify the process." Vaux says that Science's idea to pass some papers to statisticians "has some merit, but a weakness is that it relies on the board of reviewing editors to identify the papers that need scrutiny in the first place.\""""

p4_content = """Two years ago, Rupert Murdoch's daughter, Elisabeth, spoke of the "unsettling dearth of integrity across so many of our institutions." Integrity had collapsed, she argued, because of a collective acceptance that the only "sorting mechanism" in society should be profit and the market. But "it's us, human beings, we the people who create the society we want, not profit."

Driving her point home, she continued: "It's increasingly apparent that the absence of purpose, of a moral language within government, media or business could become one of the most dangerous goals for capitalism and freedom." This same absence of moral purpose was wounding companies such as News International, she thought, making it more likely that it would lose its way as it had with widespread illegal telephone hacking.

As the hacking trial concludes—finding guilty one ex-editor of the News of the World, Andy Coulson, for conspiring to hack phones, and finding his predecessor, Rebekah Brooks, innocent of the same charge—the wider issue of dearth of integrity still stands. Journalists are known to have hacked the phones of up to 5,500 people. This is hacking on an industrial scale, as was acknowledged by Glenn Mulcaire, the man hired by the News of the World in 2001 to be the point person for phone hacking. Others await trial. This long story still unfolds.

In many respects, the dearth of moral purpose frames not only the fact of such widespread phone hacking but the terms on which the trial took place. One of the astonishing revelations was how little Rebekah Brooks knew of what went on in her newsroom, how little she thought to ask and the fact that she never inquired how the stories arrived. The core of her successful defence was that she knew nothing.

In today's world, it has become normal that well-paid executives should not be accountable for what happens in the organisations that they run. Perhaps we should not be so surprised. For a generation, the collective doctrine has been that the sorting mechanism of society should be profit. The words that have mattered are efficiency, flexibility, shareholder value, business-friendly, wealth generation, sales, impact and, in newspapers, circulation. Words degraded to the margin have been justice, fairness, tolerance, proportionality and accountability.

The purpose of editing the News of the World was not to promote reader understanding, to be fair in what was written or to betray any common humanity. It was to ruin lives in the quest for circulation and impact. Ms Brooks may or may not have had suspicions about how her journalists got their stories, but she asked no questions, gave no instructions nor received traceable, recorded answers."""

p5_content = """How does your reading proceed? Clearly you try to comprehend, in the sense of identifying meanings for individual words and working out relationships between them, drawing on your implicit knowledge of English grammar. (41) _______________________ You begin to infer a context for the text, for instance by taking decisions about what kind of speech event it is: who is speaking, to whom, about what, where, and for what purpose.

The ways of reading indicated here are without doubt kinds of comprehension. But they show comprehension to consist not just of passive assimilation but of active engagement in inference and problem-solving. You infer information you feel the writer has invited you to grasp by presenting you with specific evidence and clues; (42) _______________________

Conceived in this way, comprehension will not follow exactly the same track for each reader. What is in question is not the retrieval of an absolute, fixed or 'true' meaning that can be read off and checked for accuracy, or some timeless relation of the text to the world. (43) _______________________

Such background material inevitably reflects who we are. (44) _______________________ This does not, however, make interpretation merely relative or arbitrary. Precisely because the same words on the page produce different but overlapping readings, debates about texts can play an important role in social discussion of beliefs and values.

How we read a given text also depends to some extent on our particular interest in reading it. (45) _______________________ Such dimensions of reading suggest—as others introduced later in the book will also do—that we bring an implicit (often unacknowledged) agenda to any act of reading. It doesn't then necessarily follow that one kind of reading is fuller, more advanced and more worthwhile than another. Ideally, different kinds of reading inform each other, and act as useful reference points for and counterbalances to one another. Together, they make up the reading component of your overall literacy, or relationship to your surrounding textual environment."""

passages[0]["content"] = p0_content
passages[0]["type"] = "cloze"
passages[0]["passage_number"] = 1
passages[0]["title"] = "Section I: Use of English"

passages[1]["content"] = p1_content
passages[1]["type"] = "reading"
passages[1]["passage_number"] = 2
passages[1]["title"] = "Section II: Reading Comprehension Part A - Text 1"

passages[2]["content"] = p2_content
passages[2]["type"] = "reading"
passages[2]["passage_number"] = 3
passages[2]["title"] = "Section II: Reading Comprehension Part A - Text 2"

passages[3]["content"] = p3_content
passages[3]["type"] = "reading"
passages[3]["passage_number"] = 4
passages[3]["title"] = "Section II: Reading Comprehension Part A - Text 3"

passages[4]["content"] = p4_content
passages[4]["type"] = "reading"
passages[4]["passage_number"] = 5
passages[4]["title"] = "Section II: Reading Comprehension Part A - Text 4"

passages[5]["content"] = p5_content
passages[5]["type"] = "new_type"
passages[5]["passage_number"] = 6
passages[5]["title"] = "Section II: Reading Comprehension Part B"

# 3. Clean and calibrate Questions
questions = data["questions"]

def make_opts(d):
    return [{"key": k, "text": v, "value": k} for k, v in d.items()]

GOLD_QUESTIONS_DATA = {
    # Cloze (Q1-20)
    1: {
        "stem": "Choose the best option for blank [1] in the passage:",
        "opts": {"A": "when", "B": "why", "C": "how", "D": "what"},
        "ans": "D"
    },
    2: {
        "stem": "Choose the best option for blank [2] in the passage:",
        "opts": {"A": "defended", "B": "concluded", "C": "withdrawn", "D": "advised"},
        "ans": "B"
    },
    3: {
        "stem": "Choose the best option for blank [3] in the passage:",
        "opts": {"A": "for", "B": "with", "C": "on", "D": "by"},
        "ans": "C"
    },
    4: {
        "stem": "Choose the best option for blank [4] in the passage:",
        "opts": {"A": "compared", "B": "sought", "C": "separated", "D": "connected"},
        "ans": "A"
    },
    5: {
        "stem": "Choose the best option for blank [5] in the passage:",
        "opts": {"A": "tests", "B": "objects", "C": "samples", "D": "examples"},
        "ans": "C"
    },
    6: {
        "stem": "Choose the best option for blank [6] in the passage:",
        "opts": {"A": "insignificant", "B": "unexpected", "C": "unreliable", "D": "incredible"},
        "ans": "A"
    },
    7: {
        "stem": "Choose the best option for blank [7] in the passage:",
        "opts": {"A": "visit", "B": "miss", "C": "seek", "D": "know"},
        "ans": "D"
    },
    8: {
        "stem": "Choose the best option for blank [8] in the passage:",
        "opts": {"A": "resemble", "B": "influence", "C": "favor", "D": "surpass"},
        "ans": "A"
    },
    9: {
        "stem": "Choose the best option for blank [9] in the passage:",
        "opts": {"A": "again", "B": "also", "C": "instead", "D": "thus"},
        "ans": "B"
    },
    10: {
        "stem": "Choose the best option for blank [10] in the passage:",
        "opts": {"A": "Meanwhile", "B": "Furthermore", "C": "Likewise", "D": "Perhaps"},
        "ans": "D"
    },
    11: {
        "stem": "Choose the best option for blank [11] in the passage:",
        "opts": {"A": "about", "B": "to", "C": "from", "D": "like"},
        "ans": "B"
    },
    12: {
        "stem": "Choose the best option for blank [12] in the passage:",
        "opts": {"A": "drive", "B": "observe", "C": "confuse", "D": "limit"},
        "ans": "A"
    },
    13: {
        "stem": "Choose the best option for blank [13] in the passage:",
        "opts": {"A": "according to", "B": "rather than", "C": "regardless of", "D": "along with"},
        "ans": "B"
    },
    14: {
        "stem": "Choose the best option for blank [14] in the passage:",
        "opts": {"A": "chances", "B": "responses", "C": "missions", "D": "benefits"},
        "ans": "D"
    },
    15: {
        "stem": "Choose the best option for blank [15] in the passage:",
        "opts": {"A": "later", "B": "slower", "C": "faster", "D": "earlier"},
        "ans": "C"
    },
    16: {
        "stem": "Choose the best option for blank [16] in the passage:",
        "opts": {"A": "forecast", "B": "remember", "C": "understand", "D": "express"},
        "ans": "C"
    },
    17: {
        "stem": "Choose the best option for blank [17] in the passage:",
        "opts": {"A": "unpredictable", "B": "contributory", "C": "controllable", "D": "disruptive"},
        "ans": "B"
    },
    18: {
        "stem": "Choose the best option for blank [18] in the passage:",
        "opts": {"A": "endeavor", "B": "decision", "C": "arrangement", "D": "tendency"},
        "ans": "D"
    },
    19: {
        "stem": "Choose the best option for blank [19] in the passage:",
        "opts": {"A": "political", "B": "religious", "C": "ethnic", "D": "economic"},
        "ans": "C"
    },
    20: {
        "stem": "Choose the best option for blank [20] in the passage:",
        "opts": {"A": "see", "B": "show", "C": "prove", "D": "tell"},
        "ans": "A"
    },
    
    # Text 1 (Q21-25)
    21: {
        "stem": "According to the first two paragraphs, king Juan Carlos of Spain ________.",
        "opts": {
            "A": "eased his relationship with his rivals",
            "B": "used to enjoy high public support",
            "C": "was unpopular among European royals",
            "D": "ended his reign in embarrassment"
        },
        "ans": "D"
    },
    22: {
        "stem": "Monarchs are kept as heads of state in Europe mostly ________.",
        "opts": {
            "A": "to give voters more public figures to look up to",
            "B": "to achieve a balance between tradition and reality",
            "C": "owing to their undoubted and respectable status",
            "D": "due to their everlasting political embodiment"
        },
        "ans": "C"
    },
    23: {
        "stem": "Which of the following is shown to be odd, according to the fourth paragraph?",
        "opts": {
            "A": "Aristocrats' excessive reliance on inherited wealth.",
            "B": "The role of the nobility in modern democracies.",
            "C": "The simple lifestyle of the aristocratic families.",
            "D": "The nobility's adherence to their privileges."
        },
        "ans": "B"
    },
    24: {
        "stem": "The British royals \"have most to fear\" because Charles ________.",
        "opts": {
            "A": "fails to adapt himself to his future role",
            "B": "fails to change his lifestyle as advised",
            "C": "takes republicans as his potential allies",
            "D": "takes a tough line on political issues"
        },
        "ans": "A"
    },
    25: {
        "stem": "Which of the following is the best title of the text?",
        "opts": {
            "A": "Carlos, Glory and Disgrace Combined",
            "B": "Charles, Anxious to Succeed to the Throne",
            "C": "Carlos, a Lesson for All European Monarchs",
            "D": "Charles, Slow to React to the Coming Threats"
        },
        "ans": "C"
    },
    
    # Text 2 (Q26-30)
    26: {
        "stem": "The Supreme Court will work out whether, during an arrest, it is legitimate to ________.",
        "opts": {
            "A": "prevent suspects from deleting their phone contents",
            "B": "search for suspects' mobile phones without a warrant",
            "C": "check suspects' phone contents without being authorized",
            "D": "prohibit suspects from using their mobile phones"
        },
        "ans": "C"
    },
    27: {
        "stem": "The author's attitude toward California's argument is one of ________.",
        "opts": {
            "A": "disapproval",
            "B": "indifference",
            "C": "tolerance",
            "D": "cautiousness"
        },
        "ans": "A"
    },
    28: {
        "stem": "The author believes that exploring one's phone contents is comparable to ________.",
        "opts": {
            "A": "going through one's wallet",
            "B": "handling one's historical records",
            "C": "scanning one's correspondences",
            "D": "getting into one's residence"
        },
        "ans": "D"
    },
    29: {
        "stem": "In Paragraphs 5 and 6, the author shows his concern that ________.",
        "opts": {
            "A": "principles are hard to be clearly expressed",
            "B": "the court is giving police less room for action",
            "C": "phones are used to store sensitive information",
            "D": "citizens' privacy is not effectively protected"
        },
        "ans": "D"
    },
    30: {
        "stem": "Orin Kerr's comparison is quoted to indicate that ________.",
        "opts": {
            "A": "the Constitution should be implemented flexibly",
            "B": "principles of the Constitution should never be altered",
            "C": "California's argument violates principles of the Constitution",
            "D": "new technology requires reinterpretation of the Constitution"
        },
        "ans": "D"
    },
    
    # Text 3 (Q31-35)
    31: {
        "stem": "It can be learned from Paragraph 1 that ________.",
        "opts": {
            "A": "Science intends to simplify its peer-review process",
            "B": "journals are strengthening their statistical checks",
            "C": "few journals are blamed for mistakes in data analysis",
            "D": "lack of data analysis is common in research projects"
        },
        "ans": "B"
    },
    32: {
        "stem": "The phrase \"flagged up\" (Para. 2) is the closest in meaning to ________.",
        "opts": {
            "A": "found",
            "B": "revised",
            "C": "marked",
            "D": "stored"
        },
        "ans": "C"
    },
    33: {
        "stem": "Giovanni Parmigiani believes that the establishment of the SBoRE may ________.",
        "opts": {
            "A": "pose a threat to all its peers",
            "B": "meet with strong opposition",
            "C": "increase Science's circulation",
            "D": "set an example for other journals"
        },
        "ans": "D"
    },
    34: {
        "stem": "David Vaux holds that what Science is doing now ________.",
        "opts": {
            "A": "adds to researchers' workload",
            "B": "diminishes the role of reviewers",
            "C": "has room for further improvement",
            "D": "is to fail in the foreseeable future"
        },
        "ans": "C"
    },
    35: {
        "stem": "Which of the following is the best title of the text?",
        "opts": {
            "A": "Science Joins Push to Screen Statistics in Papers",
            "B": "Professional Statisticians Deserve More Respect",
            "C": "Data Analysis Finds Its Way onto Editors' Desks",
            "D": "Statisticians Are Coming Back with Science"
        },
        "ans": "A"
    },
    
    # Text 4 (Q36-40)
    36: {
        "stem": "According to the first two paragraphs, Elisabeth was upset by ________.",
        "opts": {
            "A": "the consequences of the current sorting mechanism",
            "B": "companies' financial loss due to immoral practices",
            "C": "governmental ineffectiveness on moral issues",
            "D": "the wide misuse of integrity among institutions"
        },
        "ans": "A"
    },
    37: {
        "stem": "It can be inferred from Paragraph 3 that ________.",
        "opts": {
            "A": "Glenn Mulcaire may deny phone hacking as a crime",
            "B": "more journalists may be found guilty of phone hacking",
            "C": "Andy Coulson should be held innocent of the charge",
            "D": "phone hacking will be accepted on certain occasions"
        },
        "ans": "B"
    },
    38: {
        "stem": "The author believes that Rebekah Brooks's defence ________.",
        "opts": {
            "A": "was hardly convincing",
            "B": "centered on trivial issues",
            "C": "revealed a cunning personality",
            "D": "was part of a conspiracy"
        },
        "ans": "A"
    },
    39: {
        "stem": "The author holds that the current collective doctrine shows ________.",
        "opts": {
            "A": "a marginalized lifestyle",
            "B": "unfair wealth distribution",
            "C": "generally distorted values",
            "D": "a rigid moral code"
        },
        "ans": "C"
    },
    40: {
        "stem": "Which of the following is suggested in the last paragraph?",
        "opts": {
            "A": "The quality of writings is of primary importance.",
            "B": "Moral awareness matters in editing a newspaper.",
            "C": "Common humanity is central to news reporting.",
            "D": "Journalists need stricter industrial regulations."
        },
        "ans": "B"
    },
    
    # Part B (Q41-45)
    41: {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (41):",
        "ans": "C"
    },
    42: {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (42):",
        "ans": "E"
    },
    43: {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (43):",
        "ans": "G"
    },
    44: {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (44):",
        "ans": "B"
    },
    45: {
        "stem": "Choose the best paragraph [A]-[G] that fits into gap (45):",
        "ans": "A"
    }
}

PART_B_OPTS = {
    "A": "Are we studying that text and trying to respond in a way that fulfils the requirement of a given course? Reading it simply for pleasure? Skimming it for information? Ways of reading on a train or in bed are likely to differ considerably from reading in a seminar room.",
    "B": "Factors such as the place and period in which we are reading, our gender, ethnicity, age and education will also affect the interpretation we arrive at.",
    "C": "If you are unfamiliar with words or idioms, you guess at their meaning, using clues from them or the context, or look them up in a dictionary. As you read on, you may make inferences about the characters and about their relationship to each other. You also make more general inferences about the world that the text constructs.",
    "D": "In effect, you try to reconstruct the likely meanings or intentions of that author, through your interaction with the text, but you cannot be certain of them.",
    "E": "You make further inferences, for instance, about how the text might be meant to affect the reader, what it might be making the reader feel: surprise, suspense, amusement, disgust, indignation. You also infer information you feel the writer has intentionally left out.",
    "F": "In plays, novels and narrative poems, characters speak and act within a fictional world, but in poetry and prose the world is also spoken by a voice: a narrator or persona.",
    "G": "Rather, we ascribe meanings to texts on the basis of interaction between what we already know, what we believe, and what we read."
}

EXPLICIT_EXPLANATIONS = {
    22: """［精准定位］第三段首句指出君主作为国家元首受到持续欢迎是因为其应然的政治超越性；末句进一步指出大多数欧洲王室为何存留至今是因为他们为选民提供了一位无可争议且备受尊敬的公众人物。由此可知，欧洲君主作为国家元首被保留重点是因为他们无可争辩且受人尊重的地位，［C］正确。

［命题解密］题干+正确项是对第三段首末句间因果逻辑链接的概括与改写，正确项完全对应末句中 a non-controversial but respected public figure。

［错项排除］［A］将第三段③句 a non-controversial but respected public figure 改为 more public figures to look up to，既改变“人物数量（一个→多个）”又遗漏关键信息（无争议、受尊重）；［B］首先根据事实信息“欧洲王室留存至今”合理延伸出“欧洲王室跨越传统与现实”，但却由此捏造出“达成传统与现实的平衡”并将其视为欧洲保留君主的目的所在；［D］将第三段①句君主得以保留的原因“政治超越性/非政治性”改为与之相反的“政治象征性”。

［技巧总结］纵观选项可知本题实为因果细节题：题干为果，选项为因。典型解答思路为“根据题干定位，于定位处搜索因果关联词，再于关联词前后搜查原因/目的”。如本题，首先根据题干与①句 explains monarchs' continuing popularity as heads of state 和③句 royal families have survived because... 的近义关系，将解题线索集中到第三段①句 this apparent transcendence of politics 和③句 a non-controversial but respected public figure；然后结合第二段末句 rise above "mere" politics and "embody" a spirit of national unity，即可得出正确答案。""",

    23: """［精准定位］第四段末句指出：在经济学家就“日益加深的不平等和世袭财富权力”发出警告的今日，富有的贵族世家竟然还是现代民主国家的核心象征，这非常怪异。由此可知［B］入选。

［命题解密］题干和正确项［B］所做问答共同构成对③句的同义改写：题干 odd 对应 bizarre，选项 the role of the nobility 对应 wealthy aristocratic families should still be the symbolic heart of modern democratic states。

［错项排除］［A］利用第四段③句 warning of rising inequality and the increasing power of inherited wealth 制造干扰，但这是托马斯·皮凯蒂等经济学家的警告内容，并非作者所指的“奇怪现象”；［C］与第五段所述王室尽管努力展现平民化生活方式但实质未变的事实相反，且文中并未提及贵族生活方式“简朴”；［D］虽然贵族特权不可辩护，但题目问的是“何种现象在现代民主国家显得奇怪”，核心在于“古老贵族在现代民主政体中所扮演的角色”，故［B］为最佳选项。""",

    26: """［精准定位］第一段②句指出，最高法院即将讨论在逮捕过程中，警方可否无证搜查嫌疑人的手机内容。即，最高法院将要解决的问题是“逮捕过程中，未经授权搜查嫌疑人手机内容是否合法”，［C］正确。

［命题解密］题干+正确项［C］构成对首段②句的同义改写：题干中 work out 对应文中 consider；is legitimate to 对应 can；正确项中 check 对应 search；without being authorized 对应 without a warrant。

［错项排除］［A］利用背景信息“警察会阻止嫌疑人删除手机内容”过度推导：最高法院针对的是“（警察）搜查手机内容”，未涉及“（嫌疑人）删除手机内容”。［B］将②句 search the contents of a mobile phone（搜查手机内容［以求找到想要信息］）偷换为与之形近意远的 search for mobile phones（搜索［某一范围］以求找到手机）。［D］将首段②句 the phone is on or around a person 断章取义为“不准嫌疑人携带/使用手机”。

［技巧总结］本题就长难句命制事实信息题。解题时可采用思路：首先提取句子针对主体（主语）、行为（谓语）、具体情形（时间、条件、地点等），并与选项对比、初步判定正误；随后借助上下文检验。""",

    30: """［精准定位］根据 Orin Kerr's comparison 定位至末段③句，该句类比指出：当初汽车成为生活必需品时，法官们不得不为其确立新规，同理，如今数字信息成为人类日常生活一部分，法官也应为该新兴领域明令新规。再根据“所举事例旨在为观点服务”原则，可将类比意图追溯到②句：新的颠覆性技术有时需要对宪法保护条例有新的运用。可见，作者类比意图在于说明新技术需要宪法新解释，［D］正确。

［命题解密］正确项［D］是对末段③句类比的概括，又是对②句观点的改写，其中 requires 对应 demands；reinterpretation of the Constitution 对应 novel applications of the Constitution's protections。

［错项排除］［A］貌似与②句 novel applications of the Constitution's protections（宪法保护条例的新运用）及③句 specify novel rules（明确新的规则）同义，因此干扰性极大，但实际上文章讨论的是“宪法保护范围的新运用”并非“宪法本身的灵活实施”。［B］利用常识“宪法原则/精神不变”捏造干扰，但与文意相差甚远。［C］对①句 the justices should not swallow California's argument whole（法官们不应该全盘接受加州观点）过度推导，得出“加州观点”违反了“宪法原则”，而实际上两者并非对立。""",

    35: """［精准定位］文首段引入话题，概述《科学》新举措“增加额外统计审查”及其成因；第二三段阐释该举措具体内容及背景原因；第四至六段引三位专家之言对该举措予以评价。由此可知，“《科学》对其发表的论文增加统计审查”为全文论述主题，［A］为最佳题目。

［命题解密］正确项是对文首段话题的完美契合，其中 screen“筛查，审查”对应 checks，joins push 对应 follow similar efforts from other journals；并且准确概括了文章的中心内容。

［错项排除］［B］利用第六段①句 professional 以及文中反复提及的 statisticians 干扰，但选项侧重点为“专业统计学家未受到足够重视”，偏离文章论述中心；［C］强调的是“编辑担起新职责——数据分析”，但文章重心在于“统计审查”；［D］言外之意即“以往统计学家不受期刊重视，如今正找回其地位”，但文中重在探讨“对论文质量的把关”，“统计学家”是作为重要把关者而出现的，并非全文关注的焦点。

［技巧总结］标题题干扰项的典型特点是：涉及文中关键词却重心偏离。本文首段首句（主题句）引入《科学》的一项新举措，后文均围绕此举措展开论述，故该举措是本文话题，［A］是对首段新举措 Science is adding an extra round of statistical checks to its peer-review process 的同义改写。"""
}

def clean_explanation(q_num, expl):
    if q_num in EXPLICIT_EXPLANATIONS:
        return EXPLICIT_EXPLANATIONS[q_num]
    if not expl:
        return ""
    
    # Strip any top junk before standard headers
    markers = [
        "［考点提炼］", "[考点提炼]", "【考点提炼】",
        "［精准定位］", "[精准定位]", "【精准定位】",
        "［解题思路］", "[解题思路]", "【解题思路】",
        "［命题解密］", "[命题解密]", "【命题解密】",
        "［本题考核知识点］", "[本题考核知识点]", "【本题考核知识点】",
        "41.本题考核", "42. 本题考核", "43. 本题考核", "44. 本题考核", "45.本题考核"
    ]
    
    first_idx = len(expl)
    for m in markers:
        idx = expl.find(m)
        if idx != -1 and idx < first_idx:
            first_idx = idx
            
    if first_idx < len(expl):
        cleaned = expl[first_idx:].strip()
        return cleaned
        
    return expl.strip()

for i, q in enumerate(questions, 1):
    q["question_number"] = i
    q["sort_order"] = i
    
    gold_data = GOLD_QUESTIONS_DATA.get(i, {})
    if "stem" in gold_data:
        q["stem"] = gold_data["stem"]
    if "ans" in gold_data:
        q["answer"] = gold_data["ans"]
        q["correct_answer"] = gold_data["ans"]
    
    if i <= 20:
        q["points"] = 0.5
        q["q_type"] = "cloze_item"
        q["passage_id"] = passages[0]["id"]
        q["options"] = make_opts(gold_data["opts"])
    elif 21 <= i <= 40:
        q["points"] = 2.0
        q["q_type"] = "reading_item"
        p_idx = 1 + (i - 21) // 5
        q["passage_id"] = passages[p_idx]["id"]
        q["options"] = make_opts(gold_data["opts"])
    else: # 41 <= i <= 45
        q["points"] = 2.0
        q["q_type"] = "reading_item"
        q["passage_id"] = passages[5]["id"]
        q["options"] = make_opts(PART_B_OPTS)

    q["explanation"] = clean_explanation(i, q.get("explanation", ""))

# Save calibrated json
with open(EXAM_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("SUCCESS: 2015 ky1 exam calibrated and saved to", EXAM_PATH)
