import json
import re

exam_file = 'public/data/exams/c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json'

with open(exam_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Clean Passages
p0_content = """The homeless make up a growing percentage of America's population. [1], homelessness has reached such proportions that local governments can't possibly [2]. To help homeless people [3] independence, the federal government must support job training programs, [4] the minimum wage, and fund more low-cost housing.

[5] everyone agrees on the number of Americans who are homeless. [6] anywhere from 600,000 to 3 million. [7] the figure may vary, analysts do agree on another matter: that the number of the homeless is [8]. One of the federal government's studies [9] that the number of the homeless will reach nearly 19 million by the end of this decade.

Finding ways to [10] this growing homeless population has become increasingly difficult. [11] when homeless individuals manage to find a [12] that will give them three meals a day and a place to sleep at night, a good number still spend the bulk of each day [13] the street.

Part of the problem is that many homeless adults are addicted to alcohol or drugs. And a significant number of the homeless have serious mental disorders. Many others, [14] not addicted or mentally ill, simply lack the everyday [15] skills needed to turn their lives [16]. Boston Globe reporter Chris Reidy notes that the situation will improve only when there are [17] programs that address the many needs of the homeless. [18] Edward Zlotkowski, director of community service at Bentley College in Massachusetts, [19] it, “There has to be [20] of programs. What's needed is a package deal.”"""

p1_content = """In spite of "endless talk of difference," American society is an amazing machine for homogenizing people. There is "democratizing uniformity of dress and discourse, and the casualness and absence of deference" characteristic of popular culture. People are absorbed into "a culture of consumption" launched by the 19th-century department stores that offered "vast arrays of goods in an elegant atmosphere." Instead of intimate shops catering to a knowledgeable elite, these were stores "anyone could enter, regardless of class or background. This turned shopping into a public and democratic act." The mass media, advertising and sports are other forces for homogenization.

Immigrants are quickly fitting into this common culture, which may not be altogether elevating but is hardly poisonous. Writing for the National Immigration Forum, Gregory Rodriguez reports that today's immigration is neither at unprecedented levels nor resistant to assimilation. In 1998 immigrants were 9.8 percent of the population; in 1900, 13.6 percent. In the 10 years prior to 1990, 3.1 immigrants arrived for every 1,000 residents; in the 10 years prior to 1890, 9.2 for every 1,000. Now, consider three indices of assimilation—language, home ownership and intermarriage.

The 1990 Census revealed that "a majority of immigrants from each of the fifteen most common countries of origin spoke English 'well' or 'very well' after ten years of residence." The children of immigrants tend to be bilingual and proficient in English. "By the third generation, the original language is lost in the majority of immigrant families." Hence the description of America as a "graveyard" for languages. By 1996 foreign-born immigrants who had arrived before 1970 had a home ownership rate of 75.6 percent, higher than the 69.8 percent rate among native-born Americans.

Foreign-born Asians and Hispanics "have higher rates of intermarriage than do U.S.-born whites and blacks." By the third generation, one-third of Hispanic women are married to non-Hispanics, and 41 percent of Asian-American women are married to non-Asians.

Rodriguez notes that children in remote villages around the world are fans of superstars like Arnold Schwarzenegger and Garth Brooks, yet "some Americans fear that immigrants living within the United States remain somehow immune to the nation's assimilative power."

Are there divisive issues and pockets of seething anger in America? Indeed. It is big enough to have a bit of everything. But particularly when viewed against America's turbulent past, today's social indices hardly suggest a dark and deteriorating social environment."""

p2_content = """Stratford-on-Avon, as we all know, has only one industry—William Shakespeare—but there are two distinctly separate and increasingly hostile branches. There is the Royal Shakespeare Company (RSC), which presents superb productions of the plays at the Shakespeare Memorial Theatre on the Avon. And there are the townsfolk who largely live off the tourists who come, not to see the plays, but to look at Anne Hathaway's Cottage, Shakespeare's birthplace and the other sights.

The worthy residents of Stratford doubt that the theatre adds a penny to their revenue. They frankly dislike the RSC's actors, them with their long hair and beards and sandals and noisiness. It's all deliciously ironic when you consider that Shakespeare, who earns their living, was himself an actor (with a beard) and did his share of noise-making.

The tourist streams are not entirely separate. The sightseers who come by bus—and often take in Warwick Castle and Blenheim Palace on the side—don't usually see the plays, and some of them are even surprised to find a theatre in Stratford. However, the playgoers do manage a little sight-seeing along with their playgoing. It is the playgoers, the RSC contends, who bring in much of the town's revenue because they spend the night (some of them four or five nights) pouring cash into the hotels and restaurants. The sightseers can take in everything and get out of town by nightfall.

The townsfolk don't see it this way and the local council does not contribute directly to the subsidy of the Royal Shakespeare Company. Stratford cries poor traditionally. Nevertheless every hotel in town seems to be adding a new wing or cocktail lounge. Hilton is building its own hotel there, which you may be sure will be decorated with Hamlet Hamburger Bars, the Lear Lounge, the Banquo Banqueting Room, and so forth, and will be very expensive.

Anyway, the townsfolk can't understand why the Royal Shakespeare Company needs a subsidy. (The theatre has broken attendance records for three years in a row. Last year its 1,431 seats were 94 per cent occupied all year long and this year they'll do better.) The reason, of course, is that costs have rocketed and ticket prices have stayed low.

It would be a shame to raise prices too much because it would drive away the young people who are Stratford's most attractive clientele. They come entirely for the plays, not the sights. They all seem to look alike (though they come from all over)—lean, pointed, dedicated faces, wearing jeans and sandals, eating their buns and bedding down for the night on the flagstones outside the theatre to buy the 20 seats and 80 standing-room tickets held for the sleepers and sold to them when the box office opens at 10:30 a.m."""

p3_content = """When prehistoric man arrived in new parts of the world, something strange happened to the large animals: they suddenly became extinct. Smaller species survived. The large, slow-growing animals were easy game, and were quickly hunted to extinction. Now something similar could be happening in the oceans.

That the seas are being overfished has been known for years. What researchers such as Ransom Myers and Boris Worm have shown is just how fast things are changing. They have looked at half a century of data from fisheries around the world. Their methods do not attempt to estimate the actual biomass (the amount of living biological matter) of fish species in particular parts of the ocean, but rather changes in that biomass over time. According to their latest paper published in Nature, the biomass of large predators (animals that kill and eat other animals) in a new fishery is reduced on average by 80% within 15 years of the start of exploitation. In some long-fished areas, it has halved again since then.

Dr. Worm acknowledges that these figures are conservative. One reason for this is that fishing technology has improved. Today's vessels can find their prey using satellites and sonar, which were not available 50 years ago. That means a higher proportion of what is in the sea is being caught, so the real difference between present and past is likely to be worse than the one recorded by changes in catch sizes. In the early days, too, longlines would have been more saturated with fish. Some individuals would therefore not have been caught, since no baited hooks would have been available to trap them, leading to an underestimate of fish stocks in the past. Furthermore, in the early days of longline fishing, a lot of fish were lost to sharks after they had been hooked. That is no longer a problem, because there are fewer sharks around now.

Dr. Myers and Dr. Worm argue that their work gives a correct baseline, which future management efforts must take into account. That matters because theory suggests that the maximum sustainable yield that can be cropped from a fishery comes when the biomass of a target species is about 50% of its original levels. Most fisheries are well below that, which is a bad way to do business."""

p4_content = """Many things make people think artists are weird. But the weirdest may be this: artists' only job is to explore emotions, and yet they choose to focus on the ones that feel bad.

This wasn't always so. The earliest forms of art, like painting and music, are those best suited for expressing joy. But somewhere from the 19th century onward, more artists began seeing happiness as meaningless, phony or, worst of all, boring, as we went from Wordsworth’s daffodils to Baudelaire’s flowers of evil.

You could argue that art became more skeptical of happiness because modern times have seen so much misery. But it’s not as if earlier times didn't know perpetual war, disaster and the massacre of innocents. The reason, in fact, may be just the opposite: there is too much damn happiness in the world today.

After all, what is the one modern form of expression almost completely dedicated to depicting happiness? Advertising. The rise of anti-happy art almost exactly tracks the emergence of mass media, and with it, a commercial culture in which happiness is not just an ideal but an ideology.

People in earlier eras were surrounded by reminders of misery. They worked until exhausted, lived with few protections and died young. In the West, before mass communication and literacy, the most powerful mass medium was the church, which reminded worshippers that their souls were in danger and that they would someday be meat for worms. Given all this, they did not exactly need their art to be a bummer too.

Today the messages the average Westerner is surrounded with are not religious but commercial, and forever happy. Fast-food eaters, news anchors, text messengers, all smiling, smiling, smiling. Our magazines feature beaming celebrities and happy families in perfect homes. And since these messages have an agenda—to lure us to open our wallets—they make the very idea of happiness seem unreliable. “Celebrate!” commanded the ads for the arthritis drug Celebrex, before we found out it could increase the risk of heart attacks.

But what we forget—what our economy depends on us forgetting—is that happiness is more than pleasure without pain. The things that bring the greatest joy carry the greatest potential for loss and disappointment. Today, surrounded by promises of easy happiness, we need art to tell us, as religion once did, Memento mori: remember that you will die, that everything ends, and that happiness comes not in denying this but in living with it. It’s a message even more bitter than a clove cigarette, yet, somehow, a breath of fresh air."""

# Update Passages in data
data['passages'][0]['content'] = p0_content
data['passages'][0]['type'] = 'cloze'
data['passages'][0]['passage_number'] = 1

data['passages'][1]['content'] = p1_content
data['passages'][1]['type'] = 'reading'
data['passages'][1]['passage_number'] = 1

data['passages'][2]['content'] = p2_content
data['passages'][2]['type'] = 'reading'
data['passages'][2]['passage_number'] = 2

data['passages'][3]['content'] = p3_content
data['passages'][3]['type'] = 'reading'
data['passages'][3]['passage_number'] = 3

data['passages'][4]['content'] = p4_content
data['passages'][4]['type'] = 'reading'
data['passages'][4]['passage_number'] = 4

data['passages'][5]['type'] = 'reading_part_b'
data['passages'][5]['passage_number'] = 5

# 2. Clean Questions
q35_gold_expl = """［精准定位］第一段指出海洋生物濒临灭绝的现状；第二、三段借一项研究具体说明海洋生物量的急剧减少；第四段建议渔场在正确基线的指导下，合理安排捕捞量，维持一定的生物量水平以确保可持续发展。可见，［B］“生物量水平”是作者始终关注的对象。
［命题解密］正确项［B］为全文的论述对象，biomass 及同义表达 changes in that biomass、the biomass of large predators、real difference (in biomass) between present and past、fish stocks、the massive changes、the biomass of a target species 等多次复现贯穿全文。
［错项排除］［A］干扰源于末段首句 management efforts（管理活动），但这仅涉及研究意义，无法涵盖全篇。［C］利用文中复现词汇 catch-size 设置干扰，具有一定迷惑性，但“捕捞量”仅仅是影响“生物量变化”的一个因素，不是文章中心话题。［D］干扰源于第三段②句的 fishing technology，“技术应用”是解释“实际生物量遭受更大损失”的原因之一，不是全篇中心。
［技巧总结］本题以“中心关注点”的形式考查考生对文章的宏观把握。考生解题的关键在于分清主次：微观层面上，要对每个段落进行句意梳理、大意总结，再抠出段落关键词；宏观层面上，根据每个段落大意，找到或者提炼出能够将各段落意义联系起来的枢纽语段或中心词。正确项应该是贯穿全文的主线、中心词，而错误项则不一定会体现在所有段落中。
本文第一段指出海洋生物濒临灭绝（数量剧减）的现状；第二段借研究指出过度捕捞导致“海洋生物量的剧减（changes in biomass）”；第三段指出生物量实际变化其实很可能更为严重；第四段则指出正确的基线应该准确反映生物量的变化，渔场应在此基础上合理安排捕捞，维持一定的生物量水平，实现可持续发展。可见各段落按照“概括指出海洋生物量锐减——以研究发现说明海洋生物量变化之快——进一步指出研究还可能低估了海洋实际生物量的变化——建议维持一定生物量水平以谋求可持续发展”的逻辑展开，“生物量水平”贯彻始终。［B］选项正确。"""

q39_gold_expl = """［精准定位］末段③句指出：我们需要艺术来告诉我们“你终将死亡，万事皆会结束，幸福的到来不在于否认这一点而在于与之共生”；④句进而指出：（艺术告诉我们的）这个信息比丁香烟还要苦涩却带来一缕清新空气。由此可知，作者认为反幸福艺术令人不悦却使人头脑清醒，［B］正确。
［命题解密］正确项［B］是对末段③④句内容的高度概括，其中 distasteful 对应 you will die, that everything ends、bitter 等；refreshing 对应 we need art to tell us、a breath of fresh air 等。
［错项排除］［A］将②句 carry the greatest potential for loss and disappointment（幸福之中暗藏痛苦的可能）曲解为“幸福以悲伤告终”。［C］将③句中 living with it（应该忍受痛苦）偷换成“应该享受痛苦”。［D］将①句中 our economy depends on us forgetting that happiness is more than pleasure without pain（我们的经济依赖于盲目的幸福）曲解为“反幸福艺术随经济的兴盛而繁荣”。
［技巧总结］作者于末段提出自己观点并升华主题，命题人于此考查考生总结段落信息的能力，侧面考查考生对全篇主旨的把握。解题的关键是结合本段乃至全文信息理解段末比喻修辞。
具体解题思路为：首先可从两个层面理解末段前三句信息：我们生活中充斥着幸福的承诺（surrounded by），我们忘记了幸福并非是没有痛苦的快乐（we forget...），基于这一情形，我们需要艺术来提醒我们痛苦的存在以及学会忍受（we need art to tell us...）。借此可理解段末比喻内涵：现代的（反幸福）艺术虽然苦涩却令人清醒，初步判定［B］正确。［D］中言及反幸福艺术与经济的关系，并非文章讨论重点，且违背①句所述关系。［A］、［C］则分别篡改②、③句信息，最终敲定［B］为答案。"""

for q in data['questions']:
    so = q['sort_order']
    stem = q.get('stem', '')
    opts = q.get('options', [])
    expl = q.get('explanation', '') or ''
    
    # Q14
    if so == 14:
        for o in opts:
            if o['key'] == 'D' and o['text'] == 'wher eas':
                o['text'] = 'whereas'
                
    # Q15
    elif so == 15:
        for o in opts:
            if o['key'] == 'C' and o['text'] == 'survi val':
                o['text'] = 'survival'
                
    # Q16
    elif so == 16:
        for o in opts:
            if o['key'] == 'A': o['text'] = 'around'
            elif o['key'] == 'B': o['text'] = 'over'
            elif o['key'] == 'C': o['text'] = 'on'
            elif o['key'] == 'D': o['text'] = 'up'
            
    # Q21
    elif so == 21:
        q['stem'] = 'The word "homogenizing" (Line 2, Paragraph 1) most probably means ________.'
        
    # Q22
    elif so == 22:
        q['stem'] = 'According to the author, the department stores of the 19th century ________.'
        
    # Q27
    elif so == 27:
        q['stem'] = 'It can be inferred from Paragraph 3 that ________.'
        
    # Q30
    elif so == 30:
        q['stem'] = 'From the text we can conclude that the author ________.'
        for o in opts:
            if o['key'] == 'B':
                o['text'] = "favors the townsfolk's view"
            elif o['key'] == 'C':
                o['text'] = "takes a detached attitude"
                
    # Q31
    elif so == 31:
        q['stem'] = 'The extinction of large prehistoric animals is noted to suggest that ________.'
        for o in opts:
            if o['key'] == 'A':
                o['text'] = 'large animals were vulnerable to the changing environment'
                
    # Q32
    elif so == 32:
        q['stem'] = "We can infer from Dr. Myers and Dr. Worm's paper that ________."
        
    # Q35
    elif so == 35:
        q['explanation'] = q35_gold_expl
        
    # Q36
    elif so == 36:
        q['stem'] = 'By citing the examples of poets Wordsworth and Baudelaire, the author intends to show that ________.'
        
    # Q38
    elif so == 38:
        q['stem'] = "In the author's opinion, advertising ________."
        
    # Q39
    elif so == 39:
        q['stem'] = 'We can learn from the last paragraph that the author believes ________.'
        q['explanation'] = q39_gold_expl
        
    # Clean explanation head leaks for Q26-Q38
    if 26 <= so <= 38 and so not in [35, 39]:
        pos = expl.find('［精准定位］')
        if pos == -1:
            pos = expl.find('【精准定位】')
        if pos != -1 and pos > 0:
            q['explanation'] = expl[pos:].strip()

with open(exam_file, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("2006 exam JSON successfully calibrated with full Q35 & Q39 explanations!")
