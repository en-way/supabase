import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read PDF text
with open('scripts/2003_pdf_dump.txt', encoding='utf-8') as f:
    pdf_text = f.read()

def clean_expl(raw):
    t = re.sub(r'<<<PAGE_\d+>>>', '', raw)
    t = re.sub(r'(?:\n|^)\s*\d+\s*(?:\n|$)', '\n', t)
    t = re.sub(r'【公众号.*?】.*?\n', '', t)
    t = re.sub(r'•全.*?\n', '', t)
    t = re.sub(r'知识补充.*?\n', '', t)
    t = re.sub(r'外教朗读.*?\n', '', t)
    t = re.sub(r'一\s*•文章总体分析.*?\n', '', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()

# Precise extraction slices:
q_expl_slices = {
    21: (19469, 20625),
    22: (20625, 21612),
    23: (24276, 25680),
    24: (27114, 28358),
    25: (29759, 31000),
    26: (33481, 34753),
    27: (39549, 40808),
    28: (36779, 38100),
    29: (43003, 44235),
    30: (44235, 45214),
    31: (47123, 48300),
    32: (57970, 59384),
    33: (49724, 51300),
    34: (53304, 54485),
    35: (56585, 57970),
    36: (61840, 63372),
    37: (66047, 67400),
    38: (69285, 70595),
    39: (71746, 72648),
    40: (72648, 74600),
}

reading_explanations = {}
for q, (s, e) in q_expl_slices.items():
    chunk = pdf_text[s:e]
    idx_p = chunk.find('［精准定位］')
    idx_d = chunk.find('［命题解密］')
    if idx_p != -1 and idx_d != -1:
        st = min(idx_p, idx_d)
    elif idx_p != -1:
        st = idx_p
    elif idx_d != -1:
        st = idx_d
    else:
        st = chunk.find('[命题解密]')
        if st == -1:
            st = chunk.find('[精准定位]')
    
    body = chunk[st:]
    
    if q == 28:
        term = '三者则均无法和上文顺接，故错误。'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos + len(term)]
    elif q == 30:
        term = '外教朗读'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos]
    elif q == 31:
        term = '对应该观点fierce competition from trucks,因此可确定该项为正确答案。'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos + len(term)]
    elif q == 33:
        term = '垄断威胁，托运商处于不利地位”的总体基调，故排除。'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos + len(term)]
    elif q == 37:
        term = '［D］则直接曲解原文。'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos + len(term)]
    elif q == 40:
        term = '由此最终敲定文章中心意图为［C］。'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos + len(term)]
    elif q == 32:
        term = 'Text 4在医疗上花费大量财力延缓自然死亡不值得'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos]
    elif q == 35:
        term = '•全局真题精解/'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos]
    elif q == 39:
        term = '•全島真氯精健'
        pos = body.find(term)
        if pos != -1:
            body = body[:pos]
    
    cleaned = clean_expl(body)
    reading_explanations[q] = cleaned

# Read current exam JSON
json_path = 'public/data/exams/91ff038a-e3f9-5b6d-82c5-1328735be1d1.json'
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Update Passages
passages_text = {
    # Passage 0: Use of English
    "baf9ac68-c463-5062-81e7-086ea2e053c2": """Teachers need to be aware of the emotional, intellectual, and physical changes that young adults experience. And they also need to give serious [1] to how they can best [2] such changes. Growing bodies need movement and [3], but not just in ways that emphasize competition. [4] they are adjusting to their new bodies and a whole host of new intellectual and emotional challenges, teenagers are especially self-conscious and need the [5] that comes from achieving success and knowing that their accomplishments are [6] by others. However, the typical teenage lifestyle is already filled with so much competition that it would be [7] to plan activities in which there are more winners than losers, [8], publishing newsletters with many student-written book reviews, [9] student artwork, and sponsoring book discussion clubs. A variety of small clubs can provide [10] opportunities for leadership, as well as for practice in successful [11] dynamics. Making friends is extremely important to teenagers, and many shy students need the [12] of some kind of organization with a supportive adult [13] visible in the background.

In these activities, it is important to remember that young teens have [14] attention spans. A variety of activities should be organized [15] participants can remain active as long as they want and then go on to [16] else without feeling guilty and without letting the other participants [17]. This does not mean that adults must accept irresponsibility. [18], they can help students acquire a sense of commitment by [19] for roles that are within their [20] and their attention spans and by having clearly stated rules.""",

    # Passage 1: Text 1
    "42614f3c-867d-5b54-a985-106027132f60": """Wild Bill Donovan would have loved the Internet. The American spymaster who built the Office of Strategic Services in World War II and later laid the roots for the CIA was fascinated with information. Donovan believed in using whatever tools came to hand in the "great game" of espionage—spying as a "profession". These days the Net, which has already remade such everyday pastimes as buying books and sending mail, is reshaping Donovan's vocation as well.

The latest revolution isn't simply a matter of gentlemen reading other gentlemen's e-mail. That kind of electronic spying has been going on for decades. In the past three or four years, the World Wide Web has given birth to a whole industry of point-and-click spying. The spooks call it "open-source intelligence," and as the Net grows, it is becoming increasingly influential. In 1995 the CIA held a contest to see who could compile the most data about Burundi. The winner, by a large margin, was a tiny Virginia company called Open Source Solutions, whose clear advantage was its mastery of the electronic world.

Among the firms making the biggest splash in this new world is Straitford, Inc., a private intelligence-analysis firm based in Austin, Texas. Straitford makes money by selling the results of spying (covering nations from Chile to Russia) to corporations like energy-services firm McDermott International. Many of its predictions are available online at www.straitford.com.

Straitford president George Friedman says he sees the online world as a kind of mutually reinforcing tool for both information collection and distribution, a spymaster's dream. Last week his firm was busy vacuuming up data bits from the far corners of the world and predicting a crisis in Ukraine. "As soon as that report runs, we'll suddenly get 500 new Internet sign-ups from Ukraine," says Friedman, a former political science professor. "And we'll hear back from some of them." Open-source spying does have its risks, of course, since it can be difficult to tell good information from bad. That's where Straitford earns its keep.

Friedman relies on a lean staff of 20 in Austin. Several of his staff members have military-intelligence backgrounds. He sees the firm's outsider status as the key to its success. Straitford's briefs don't sound like the usual Washington back-and-forthing, whereby agencies avoid dramatic declarations on the chance they might be wrong. Straitford, says Friedman, takes pride in its independent voice.""",

    # Passage 2: Text 2
    "b0b11306-8638-56f7-b906-ba1282efce2c": """To paraphrase 18th-century statesman Edmund Burke, "all that is needed for the triumph of a misguided cause is that good people do nothing." One such cause now seeks to end biomedical research because of the theory that animals have rights ruling out their use in research. Scientists need to respond forcefully to animal rights advocates, whose arguments are confusing the public and thereby threatening advances in health knowledge and care. Leaders of the animal rights movement target biomedical research because it depends on public funding, and few people understand the process of health care research. Hearing allegations of cruelty to animals in research settings, many are perplexed that anyone would deliberately harm an animal.

For example, a grandmotherly woman staffing an animal rights booth at a recent street fair was distributing a brochure that encouraged readers not to use anything that comes from or is tested in animals—no meat, no fur, no medicines. Asked if she opposed immunizations, she wanted to know if vaccines come from animal research. When assured that they do, she replied, "Then I would have to say yes." Asked what will happen when epidemics return, she said, "Don't worry, scientists will find some way of using computers." Such well-meaning people just don't understand.

Scientists must communicate their message to the public in a compassionate, understandable way—in human terms, not in the language of molecular biology. We need to make clear the connection between animal research and a grandmother's hip replacement, a father's bypass operation, a baby's vaccinations, and even a pet's shots. To those who are unaware that animal research was needed to produce these treatments, as well as new treatments and vaccines, animal research seems wasteful at best and cruel at worst.

Much can be done. Scientists could "adopt" middle school classes and present their own research. They should be quick to respond to letters to the editor, lest animal rights misinformation go unchallenged and acquire a deceptive appearance of truth. Research institutions could be opened to tours, to show that laboratory animals receive humane care. Finally, because the ultimate stakeholders are patients, the health research community should actively recruit to its cause not only well-known personalities such as Stephen Cooper, who has made courageous statements about the value of animal research, but all who receive medical treatment. If good people do nothing, there is a real possibility that an uninformed citizenry will extinguish the precious embers of medical progress.""",

    # Passage 3: Text 3
    "9ba61f50-0a1f-5ccf-8eb0-af5b8c9dd841": """In recent years, railroads have been combining with each other, merging into supersystems, causing heightened concerns about monopoly. As recently as 1995, the top four railroads accounted for under 70 percent of the total ton-miles moved by rails. Next year, after a series of mergers is completed, just four railroads will control well over 90 percent of all the freight moved by major rail carriers.

Supporters of the new supersystems argue that these mergers will allow for substantial cost reductions and better coordinated service. Any threat of monopoly, they argue, is removed by fierce competition from trucks. But many shippers complain that for heavy bulk commodities traveling long distances, such as coal, chemicals, and grain, trucking is too costly and the railroads therefore have them by the throat.

The vast consolidation within the rail industry means that most shippers are served by only one rail company. Railroads typically charge such "captive" shippers 20 to 30 percent more than they do when another railroad is competing for the business. Shippers who feel they are being overcharged have the right to appeal to the federal government's Surface Transportation Board for rate relief, but the process is expensive, time consuming, and will work only in truly extreme cases.

Railroads justify rate discrimination against captive shippers on the grounds that in the long run it reduces everyone's cost. If railroads charged all customers the same average rate, they argue, shippers who have the option of switching to trucks or other forms of transportation would do so, leaving remaining customers to shoulder the cost of keeping up the line. It's a theory to which many economists subscribe, but in practice it often leaves railroads in the position of determining which companies will flourish and which will fail. "Do we really want railroads to be the arbiters of who wins and who loses in the marketplace?" asks Martin Bercovici, a Washington lawyer who frequently represents shippers.

Many captive shippers also worry they will soon be hit with a round of huge rate increases. The railroad industry as a whole, despite its brightening fortunes, still does not earn enough to cover the cost of the capital it must invest to keep up with its surging traffic. Yet railroads continue to borrow billions to acquire one another, with Wall Street cheering them on. Consider the $10.2 billion bid by Norfolk Southern and CSX to acquire Conrail this year. Conrail's net railway operating income in 1996 was just $427 million, less than half of the carrying costs of the transaction. Who's going to pay for the rest of the bill? Many captive shippers fear that they will, as Norfolk Southern and CSX increase their grip on the market.""",

    # Passage 4: Text 4
    "ca2c47ce-e376-58c8-8a48-5dd6d192b3b6": """It is said that in England death is pressing, in Canada inevitable and in California optional. Small wonder. Americans' life expectancy has nearly doubled over the past century. Failing hips can be replaced, clinical depression controlled, cataracts removed in a 30-minute surgical procedure. Such advances offer the aging population a quality of life that was unimaginable when I entered medicine 50 years ago. But not even a great health-care system can cure death—and our failure to confront that reality now threatens this greatness of ours.

Death is normal; we are genetically programmed to disintegrate and perish, even under ideal conditions. We all understand that at some level, yet as medical consumers we treat death as a problem to be solved. Shielded by third-party payers from the cost of our care, we demand everything that can possibly be done for us, even if it's useless. The most obvious example is late-stage cancer care. Physicians—frustrated by their inability to cure the disease and fearing loss of hope in the patient—too often offer aggressive treatment far beyond what is scientifically justified.

In 1950, the U.S. spent $12.7 billion on health care. In 2002, the cost will be $1,540 billion. Anyone can see this trend is unsustainable. Yet few seem willing to try to reverse it. Some scholars conclude that a government with finite resources should simply stop paying for medical care that sustains life beyond a certain age—say 83 or so. Former Colorado governor Richard Lamm has been quoted as saying that the old and infirm "have a duty to die and get out of the way" so that younger, healthier people can realize their potential.

I would not go that far. Energetic people now routinely work through their 60s and beyond, and remain dazzlingly productive. At 78, Viacom chairman Sumner Redstone jokingly claims to be 53. Supreme Court Justice Sandra Day O'Connor is in her 70s, and former surgeon general C. Everett Koop chairs an Internet start-up in his 80s. These leaders are living proof that prevention works and that we can manage the health problems that come naturally with age. As a mere 68-year-old, I wish to age as productively as they have.

Yet there are limits to what a society can spend in this pursuit. As a physician, I know the most costly and dramatic measures may be ineffective and painful. I also know that people in Japan and Sweden, countries that spend far less on medical care, have achieved longer, healthier lives than we have. As a nation, we may be overfunding the quest for unlikely cures while underfunding research on humbler therapies that could improve people's lives."""
}

for p in exam_data['passages']:
    pid = p['id']
    if pid in passages_text:
        p['content'] = passages_text[pid]

# 2. Update Questions
for q in exam_data['questions']:
    order = q['sort_order']
    
    # Q17
    if order == 17:
        q['answer'] = 'B'
        q['correct_answer'] = 'B'
        q['explanation'] = """[试题考点]短语动词用法辨析
[解题思路]空格所在部分 without letting the other participants 17 和 without feeling guilty 并列，根据②句句意，空格部分说明“参加者转而参加其他活动”时除了不让自己感到内疚外，还要考虑团体中其他人的感受。对实际情形稍加设想可知，每个有组织的活动都有一定的周期，中途退出是一件不符合预期的突发事件，因此可能会让其他的团队成员感到失望。[B]项let down意为“使……失望”，能够表达这层意思，为正确项。
[错项排除]其他项均可与let构成短语，但与文意不符。let off不惩罚，宽恕；let out放掉，使解脱；let alone不打扰，更不必说。"""
    
    # Q20
    elif order == 20:
        q['answer'] = 'A'
        q['correct_answer'] = 'A'
        q['explanation'] = """[试题考点]名词词义辨析
[解题思路]空格所在介词短语within their 20 and their attention spans描述教师为学生设计的角色的特点。within表示“在（某一限制或规则）之内”，该介词短语中给出原则之一：不能超出青少年注意力持续的范围，这与上文“顾及青少年青春期难以集中注意力”的内容相统一，但同时必须牢记本句旨在传递的内容：顾及其弱点并非只能纵容其不负责任，也即，必须对其加以适当约束。within capabilities（不超出能力范围之外）既表达了“约束”，同时也兼顾了客观情况，因此[A]为最佳选项。
[错项排除]空格词与within连用，表示“在……范围内”，因此该词必须能体现“大小、多少”等程度之别。proficiency 意为 a good standard of ability or skill；efficiency 意为 the quality of doing sth well and effectively, without wasting time, money and energy；responsibility 意为 something you ought to do because it is morally or socially right；这三项分别指示某一标准、特征或必须要承担的义务，由于本身没有程度大小的范畴，因此不能和within连用。capability则意为the natural ability, skill or power，作为“能力”讲，可以有程度高低、大小，自身划定了一定的范畴，可与within连用。"""

    # Reading comprehension Q21-Q40
    elif 21 <= order <= 40:
        # Update explanation
        if order in reading_explanations:
            q['explanation'] = reading_explanations[order]
        
        # Stems, Options, and Answers
        if order == 21:
            q['stem'] = "The emergence of the Net has ________."
            q['correct_answer'] = q['answer'] = "B"
            q['options'] = [
                {"key": "A", "text": "received support from fans like Donovan"},
                {"key": "B", "text": "remolded the intelligence services"},
                {"key": "C", "text": "restored many common pastimes"},
                {"key": "D", "text": "revived spying as a profession"}
            ]
        elif order == 22:
            q['stem'] = "Donovan's story is mentioned in the text to ________."
            q['correct_answer'] = q['answer'] = "A"
            q['options'] = [
                {"key": "A", "text": "introduce the topic of online spying"},
                {"key": "B", "text": "show how he fought for the U. S."},
                {"key": "C", "text": "give an episode of the information war"},
                {"key": "D", "text": "honor his unique services to the CIA"}
            ]
        elif order == 23:
            q['stem'] = 'The phrase "making the biggest splash" (Line 1, Paragraph 3) most probably means ________.'
            q['correct_answer'] = q['answer'] = "C"
            q['options'] = [
                {"key": "A", "text": "causing the biggest trouble"},
                {"key": "B", "text": "exerting the greatest effort"},
                {"key": "C", "text": "achieving the greatest success"},
                {"key": "D", "text": "enjoying the widest popularity"}
            ]
        elif order == 24:
            q['stem'] = "It can be learned from Paragraph 4 that ________."
            q['correct_answer'] = q['answer'] = "D"
            q['options'] = [
                {"key": "A", "text": "Straitford's prediction about Ukraine has proved true"},
                {"key": "B", "text": "Straitford guarantees the truthfulness of its information"},
                {"key": "C", "text": "Straitford's business is characterized by unpredictability"},
                {"key": "D", "text": "Straitford is able to provide fairly reliable information"}
            ]
        elif order == 25:
            q['stem'] = "Straitford is most proud of its ________."
            q['correct_answer'] = q['answer'] = "B"
            q['options'] = [
                {"key": "A", "text": "official status"},
                {"key": "B", "text": "nonconformist image"},
                {"key": "C", "text": "efficient staff"},
                {"key": "D", "text": "military background"}
            ]
        elif order == 26:
            q['stem'] = "The author begins his article with Edmund Burke's words to ________."
            q['correct_answer'] = q['answer'] = "A"
            q['options'] = [
                {"key": "A", "text": "call on scientists to take some actions"},
                {"key": "B", "text": "criticize the misguided cause of animal rights"},
                {"key": "C", "text": "warn of the doom of biomedical research"},
                {"key": "D", "text": "show the triumph of the animal rights movement"}
            ]
        elif order == 27:
            q['stem'] = "Misled people tend to think that using an animal in research is ________."
            q['correct_answer'] = q['answer'] = "B"
            q['options'] = [
                {"key": "A", "text": "cruel but natural"},
                {"key": "B", "text": "inhuman and unacceptable"},
                {"key": "C", "text": "inevitable but vicious"},
                {"key": "D", "text": "pointless and wasteful"}
            ]
        elif order == 28:
            q['stem'] = "The example of the grandmotherly woman is used to show the public's ________."
            q['correct_answer'] = q['answer'] = "B"
            q['options'] = [
                {"key": "A", "text": "discontent with animal research"},
                {"key": "B", "text": "ignorance about medical science"},
                {"key": "C", "text": "indifference to epidemics"},
                {"key": "D", "text": "anxiety about animal rights"}
            ]
        elif order == 29:
            q['stem'] = "The author believes that, in face of the challenge from animal rights advocates, scientists should ________."
            q['correct_answer'] = q['answer'] = "A"
            q['options'] = [
                {"key": "A", "text": "communicate more with the public"},
                {"key": "B", "text": "employ hi-tech means in research"},
                {"key": "C", "text": "feel no shame for their cause"},
                {"key": "D", "text": "strive to develop new cures"}
            ]
        elif order == 30:
            q['stem'] = "From the text we learn that Stephen Cooper is ________."
            q['correct_answer'] = q['answer'] = "D"
            q['options'] = [
                {"key": "A", "text": "a well-known humanist"},
                {"key": "B", "text": "a medical practitioner"},
                {"key": "C", "text": "an enthusiast in animal rights"},
                {"key": "D", "text": "a supporter of animal research"}
            ]
        elif order == 31:
            q['stem'] = "According to those who support mergers, railway monopoly is unlikely because ________."
            q['correct_answer'] = q['answer'] = "C"
            q['options'] = [
                {"key": "A", "text": "cost reduction is based on competition"},
                {"key": "B", "text": "services call for cross-trade coordination"},
                {"key": "C", "text": "outside competitors will continue to exist"},
                {"key": "D", "text": "shippers will have the railway by the throat"}
            ]
        elif order == 32:
            q['stem'] = "What is many captive shippers' attitude towards the consolidation in the rail industry?"
            q['correct_answer'] = q['answer'] = "D"
            q['options'] = [
                {"key": "A", "text": "Indifferent"},
                {"key": "B", "text": "Supportive"},
                {"key": "C", "text": "Indignant"},
                {"key": "D", "text": "Apprehensive"}
            ]
        elif order == 33:
            q['stem'] = "It can be inferred from Paragraph 3 that ________."
            q['correct_answer'] = q['answer'] = "C"
            q['options'] = [
                {"key": "A", "text": "shippers will be charged less without a rival railroad"},
                {"key": "B", "text": "there will soon be only one railroad company nationwide"},
                {"key": "C", "text": "overcharged shippers are unlikely to appeal for rate relief"},
                {"key": "D", "text": "a government board ensures fair play in railway business"}
            ]
        elif order == 34:
            q['stem'] = 'The word "arbiters" (Line 6, Paragraph 4) most probably refers to those ________.'
            q['correct_answer'] = q['answer'] = "B"
            q['options'] = [
                {"key": "A", "text": "who work as coordinators"},
                {"key": "B", "text": "who function as judges"},
                {"key": "C", "text": "who supervise transactions"},
                {"key": "D", "text": "who determine the price"}
            ]
        elif order == 35:
            q['stem'] = "According to the text, the cost increase in the rail industry is mainly caused by ________."
            q['correct_answer'] = q['answer'] = "A"
            q['options'] = [
                {"key": "A", "text": "the continuing acquisition"},
                {"key": "B", "text": "the growing traffic"},
                {"key": "C", "text": "the cheering Wall Street"},
                {"key": "D", "text": "the shrinking market"}
            ]
        elif order == 36:
            q['stem'] = "What is implied in the first sentence?"
            q['correct_answer'] = q['answer'] = "C"
            q['options'] = [
                {"key": "A", "text": "Americans are better prepared for death than other people."},
                {"key": "B", "text": "Americans enjoy a higher life quality than ever before."},
                {"key": "C", "text": "Americans are over-confident of their medical technology."},
                {"key": "D", "text": "Americans take a vain pride in their long life expectancy."}
            ]
        elif order == 37:
            q['stem'] = "The author uses the example of cancer patients to show that ________."
            q['correct_answer'] = q['answer'] = "A"
            q['options'] = [
                {"key": "A", "text": "medical resources are often wasted"},
                {"key": "B", "text": "doctors are helpless against fatal diseases"},
                {"key": "C", "text": "some treatments are too aggressive"},
                {"key": "D", "text": "medical costs are becoming unaffordable"}
            ]
        elif order == 38:
            q['stem'] = "The author's attitude toward Richard Lamm's remark is one of ________."
            q['correct_answer'] = q['answer'] = "B"
            q['options'] = [
                {"key": "A", "text": "strong disapproval"},
                {"key": "B", "text": "reserved consent"},
                {"key": "C", "text": "slight contempt"},
                {"key": "D", "text": "enthusiastic support"}
            ]
        elif order == 39:
            q['stem'] = "In contrast to the US, Japan and Sweden are funding their medical care ________."
            q['correct_answer'] = q['answer'] = "D"
            q['options'] = [
                {"key": "A", "text": "more flexibly"},
                {"key": "B", "text": "more extravagantly"},
                {"key": "C", "text": "more cautiously"},
                {"key": "D", "text": "more reasonably"}
            ]
        elif order == 40:
            q['stem'] = "The text intends to express the idea that ________."
            q['correct_answer'] = q['answer'] = "C"
            q['options'] = [
                {"key": "A", "text": "medicine will further prolong people's lives"},
                {"key": "B", "text": "life beyond a certain limit is not worth living"},
                {"key": "C", "text": "death should be accepted as a fact of life"},
                {"key": "D", "text": "excessive demands increase the cost of health care"}
            ]

# Save JSON file
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("Saved calibrated JSON to", json_path)
