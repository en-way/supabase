# -*- coding: utf-8 -*-
"""
Round 64: 2016 ky1 Gold Engine
Performs forensic reconstruction of 2016 English (One) exam [UUID: 666cdb4e-7fd3-53c2-8c91-a12fa3160c09]:
- Exam metadata normalization: title = '2016年全国硕士研究生招生考试英语（一）真题', total_score = 60.0, pass_score = 36.0
- Passages 0-5 gold reconstruction:
  - Passage 0: 3 paragraphs (Courtship, Marriage, Divorce), clean gap formatting [1]..[20]
  - Passage 1 (Text 1): 7 paragraphs (restore missing Para 7: 'Relying on ethical persuasion...', fix 'France, which prides itself...', restore lost 1st sentence of Para 3, strip leaked Q22 stem, strip duplicated 'a couple of uplifting motiveso', capitalize 'In contrast')
  - Passage 2 (Text 2): 6 paragraphs (restore obliterated sentences in Para 3, strip leaked Q27 stem, clean 'showT', fix corrupted quotes 'housing crisis' & 'concreted meadows', capitalize 'Development')
  - Passage 3 (Text 3): 6 paragraphs (clean initial quote, strip duplicated 'causes it helps.', remove duplicate ':Companies did not receive lower fines.', restore full quote in Para 5 and strip 'We estimate < record in CSRO')
  - Passage 4 (Text 4): 7 paragraphs (pristine sentences from Yellow Book)
  - Passage 5 (Part B): 8 paragraphs (strip Directions and options [A]-[G] from content, retain 5 clean gaps [41]-[45])
- Questions 1-45 gold reconstruction:
  - question_number = 1..45 (0 None)
  - sort_order = 1..45
  - score = points = 0.5 (cloze) / 2.0 (reading)
  - question_type = q_type = 'cloze_item' / 'reading_item'
  - Cloze stem format: 'Choose the best option for blank [{qnum}] in the passage:'
  - Cloze answers calibrated to official key: 1:A, 2:D, 3:C, 4:A, 5:C, 6:B, 7:D, 8:B, 9:D, 10:A, 11:D, 12:C, 13:B, 14:B, 15:C, 16:A, 17:B, 18:D, 19:B, 20:A
  - Fix Q20 option B from 'once.... ...' to 'once'
  - Reading answers calibrated: 21:A, 22:D, 23:D, 24:C, 25:D, 26:A, 27:D, 28:C, 29:A, 30:C, 31:B, 32:C, 33:D, 34:A, 35:B, 36:A, 37:B, 38:B, 39:C, 40:B, 41:C, 42:F, 43:D, 44:E, 45:G
  - Fix Q24 fabricated options to real official exam options
  - Complete three-tier golden explanations for all 45 questions
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import json

EXAM_PATH = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\666cdb4e-7fd3-53c2-8c91-a12fa3160c09.json"

with open(EXAM_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# 1. Update Exam Metadata
exam = data["exam"]
exam["title"] = "2016年全国硕士研究生招生考试英语（一）真题"
exam["total_score"] = 60.0
exam["pass_score"] = 36.0

# 2. Reconstruct Passages
passages = data["passages"]

p0_content = """In Cambodia, the choice of a spouse is a complex one for the young male. It may involve not only his parents and his friends, [1] those of the young woman, but also a matchmaker. A young man can [2] a likely spouse on his own and then ask his parents to [3] the marriage negotiations, or the young man's parents may make the choice of a spouse, giving the child little to say in the selection. [4], a girl may veto the spouse her parents have chosen. [5] a spouse has been selected, each family investigates the other to make sure its child is marrying [6] a good family.

The traditional wedding is a long and colorful affair. Formerly it lasted three days, [7] by the 1980s it more commonly lasted a day and a half. Buddhist priests offer a short sermon and [8] prayers of blessing. Parts of the ceremony involve ritual hair cutting, [9] cotton threads soaked in holy water around the bride's and groom's wrists, and [10] a candle around a circle of happily married and respected couples to bless the [11]. Newlyweds traditionally move in with the wife's parents and may [12] with them up to a year, [13] they can build a new house nearby.

Divorce is legal and easy to [14], but not common. Divorced persons are [15] with some disapproval. Each spouse retains [16] property he or she [17] into the marriage, and jointly-acquired property is [18] equally. Divorced persons may remarry, but a gender prejudice [19] up: The divorced male doesn't have a waiting period before he can remarry [20] the woman must wait ten months."""

p1_content = """France, which prides itself as the global innovator of fashion, has decided its fashion industry has lost an absolute right to define physical beauty for women. Its lawmakers gave preliminary approval last week to a law that would make it a crime to employ ultra-thin models on runways. The parliament also agreed to ban websites that "incite excessive thinness" by promoting extreme dieting.

Such measures have a couple of uplifting motives. They suggest beauty should not be defined by looks that end up impinging on health. That's a start. And the ban on ultra-thin models seems to go beyond protecting models from starving themselves to death - as some have done. It tells the fashion industry that it must take responsibility for the signal it sends women, especially teenage girls, about the social tape-measure they must use to determine their individual worth.

The bans, if fully enforced, would suggest to women (and many men) that they should not let others be arbiters of their beauty. And perhaps faintly, they hint that people should look to intangible qualities like character and intellect rather than dieting their way to size zero or wasp-waist physiques.

The French measures, however, rely too much on severe punishment to change a culture that still regards beauty as skin-deep-and bone-showing. Under the law, using a fashion model that does not meet a government-defined index of body mass could result in a $85,000 fine and six months in prison.

The fashion industry knows it has an inherent problem in focusing on material adornment and idealized body types. In Denmark, the United States, and a few other countries, it is trying to set voluntary standards for models and fashion images that rely more on peer pressure for enforcement.

In contrast to France's actions, Denmark's fashion industry agreed last month on rules and sanctions regarding the age, health, and other characteristics of models. The newly revised Danish Fashion Ethical Charter clearly states: "We are aware of and take responsibility for the impact the fashion industry has on body ideals, especially on young people." The charter's main tool of enforcement is to deny access for designers and modeling agencies to Copenhagen Fashion Week (CFW), which is run by the Danish Fashion Institute. But in general it relies on a name-and-shame method of compliance.

Relying on ethical persuasion rather than law to address the misuse of body ideals may be the best step. Even better would be to help elevate notions of beauty beyond the material standards of a particular industry."""

p2_content = """For the first time in history more people live in towns than in the country. In Britain this has had a curious result. While polls show Britons rate "the countryside" alongside the royal family, Shakespeare and the National Health Service (NHS) as what makes them proudest of their country, this has limited political support.

A century ago Octavia Hill launched the National Trust not to rescue stylish houses but to save "the beauty of natural places for everyone forever." It was specifically to provide city dwellers with spaces for leisure where they could experience "a refreshing air." Hill's pressure later led to the creation of national parks and green belts. They don't make countryside any less a charity for the public good. It is endangered by annual increments of development, in particular the spread of suburban sprawl and what is called "infill" - the filling in of urban green space. And the country's population continues to grow. As every town expands and consumes more of it, it needs constant guardianship.

At the next election none of the big parties seem likely to endorse this sentiment. The Conservatives' planning reform explicitly gives rural development priority over conservation, even authorizing "off-plan" building where local people might object. The concept of sustainable development has been defined as profitable. Labour likewise wants to discontinue local planning where councils oppose development. The Liberal Democrats are silent. Only Ukip, sensing its chance, has sided with those pleading for a more considered approach to using green land. Its Campaign to Protect Rural England struck terror into many local Conservative parties.

The sensible place to build new houses, factories and offices is where people are, in cities and towns where infrastructure is in place. The London agents Stirling Ackroyd recently identified enough sites for half a million houses in the London area alone, with no intrusion on green belt. What is true of London is even truer of the provinces.

The idea that "housing crisis" equals "concreted meadows" is pure lobby talk. The issue is not the need for more houses but, as always, where to put them. Under lobby pressure, George Osborne favours rural new-build against urban renovation and renewal. He favours out-of-town shopping sites against high streets. This is not a free market but a biased one. Rural towns and villages have grown and will always grow. They do so best where building sticks to their edges and respects their character. We do not need to ruin urban conservation areas. Why ruin rural ones?

Development should be planned, not let rip. After the Netherlands, Britain is Europe's most crowded country. Half a century of town and country planning has enabled it to retain an enviable rural coherence, while still permitting low-density urban living. There is no doubt of the alternative - the ribbon development and fragmented sprawl of the 1930s. The countryside had to be defended then. It must be defended now, if only for the great and growing numbers who love it so that it is considered a national treasure. It should unite the left and right of the political spectrum."""

p3_content = """"There is one and only one social responsibility of business," wrote Milton Friedman, a Nobel Prize-winning economist, "that is, to use its resources and engage in activities designed to increase its profits." But even if you accept Friedman's premise and regard corporate social responsibility (CSR) policies as a waste of shareholders' money, things may not be absolutely clear-cut. New research suggests that CSR may create monetary value for companies - at least when they are prosecuted for corruption.

The largest firms in America and Britain together spend more than $15 billion a year on CSR, according to an estimate by EPG, a consulting firm. This could add value to their businesses in three ways. First, consumers may take CSR spending as a "signal" that a company's products are of high quality. Second, customers may be willing to buy a company's products as an indirect way to donate to the good causes it helps. And third, through a more diffuse "halo effect," CSR may earn a company greater respect from both consumers and others.

Previous studies on CSR have had trouble differentiating these effects because consumers can be affected by all three. A recent study attempts to separate them by looking at bribery prosecutions under America's Foreign Corrupt Practices Act (FCPA).

The study found that, among prosecuted firms, those with the most comprehensive CSR programmes tended to get more lenient penalties. Their analysis ruled out the possibility that it was firms' political influence, rather than their CSR stand, that accounted for the leniency: Companies that contributed more to political campaigns did not receive lower fines.

In all, the study concludes that whereas prosecutors should only evaluate a case based on its merits, they do seem to be influenced by a company's record in CSR. "We estimate that either eliminating a substantial labour-rights concern, such as child labour, or increasing corporate giving by about 20% results in fines that generally are 40% lower than the typical punishment for bribing foreign officials," says one researcher.

Researchers admit that their study does not answer the question of how much businesses ought to spend on CSR. Nor does it reveal how much companies are banking on the halo effect, rather than the other possible benefits, when they decide their CSR budgets. What it does show is that online reputation management may not be enough: When companies get into serious legal trouble, having built up a reservoir of good character can win them a less costly punishment."""

p4_content = """There will eventually come a day when The New York Times ceases to publish stories on newsprint. Exactly when that day will be is a matter of debate. "Sometime in the future," the paper's publisher said back in 2010.

Nostalgia for ink on paper and the rustle of pages aside, there's plenty of incentive to ditch print. The infrastructure required to make a physical newspaper - printing presses, delivery trucks - isn't just expensive; it's excessive at a time when online-only competitors don't have the same set of financial constraints. Readers are migrating away from print anyway. And though print ad sales continue to dwarf their online and mobile counterparts, revenue from print is still declining.

Overhead may be high and circulation lower, but rushing to eliminate its print edition would be a mistake, says BuzzFeed CEO Jonah Peretti.

Peretti says the Times shouldn't waste time getting out of the print business, but only if they go about doing it the right way. "Figuring out a way to accelerate that transition would make sense for them," he said, "but if you discontinue it, you're going to have your most loyal customers really upset with you."

Sometimes that's worth making a change anyway. Peretti gives the example of Netflix moving away from DVDs in favor of streaming, which was seen as a blunder at the time but turned out to be foresighted. But Netflix was offering a better alternative and can't be compared to what when the Times discontinue print. "You can't do that with the Times, but you can raise prices and make it into more of a legacy product."

The most loyal customers would still get the product they favor, the idea goes, and they'd feel like they were helping sustain the quality of something they believe in. "So if you're overpaying for print, you could feel like you were helping," Peretti said. "Then increase it at a higher rate each year and essentially make it generate more revenue." In other words, look at print as a luxury, and make it for the people who are already obsessed with it. Which may be what the Times is doing, given that a home-delivery subscription was recently bumped to $8.60 a week, or more than twice as much as a digital-only subscription.

"It's a really hard thing to do and it's a tremendous luxury that BuzzFeed doesn't have a legacy business," Peretti remarked. "But we're going to have questions like that where we have things we're doing that don't make sense when the market changes and the world changes. In those situations, it's better to be more aggressive than less aggressive.\""""

p5_content = """No matter how formal or informal the work environment, the way you present yourself has an impact. This is especially true in first impressions. According to research from Princeton University, people assess your competence, trustworthiness, and likeability in just a tenth of a second, solely based on the way you look.

The difference between today's workplace and the "dress for success" era is that the range of options is so much broader. Norms have evolved and fragmented. In some settings, red sneakers or dress T-shirts can convey status; in others not so much. Plus, whatever image we present is magnified by social-media services like LinkedIn. Chances are, your headshots are seen much more often now than a decade or two ago. Millennials, it seems, face the paradox of being the least formal generation yet the most conscious of style and personal branding. It can be confusing.

So how do we navigate this? How do we know when to invest in an upgrade? And what's the best way to pull off one that enhances our goals? Here are some tips:

[41] _________________________________
As an executive coach, I've seen image upgrades be make-or-break over the years. But they don't make sense in every situation. If you're doing it simply because you're bored or you've decided to be more "stylish," that's probably not a good enough reason to spend time and money on clothes. On the other hand, if you're in a period of transition - say, you've taken a new job or you're preparing for a promotion - it can be a good time to reassess your image. If it's working for you, maybe there's no need for an upgrade and that's OK.

[42] _________________________________
Get clear on what impact you're trying to achieve. Do you need to appear more authoritative, or more approachable? Does your work require you to convey confidence and competence, or creativity and innovation? As image consultant Sarah Jane Sloane puts it, you want to figure out whether you're trying to look like "a sleek executive or a colorful bohemian or something in between." Once you know your goal, it's easier to create a look that aligns with it. (It's OK to use characterizations like that.)

[43] _________________________________
Look at your work environment like an anthropologist. What are the norms of your industry and company? What are senior leaders wearing? Are there specific pieces or styles that communicate credibility? A three-piece suit might make you look like a leader in one company, but alienate you in another. The better you understand your context, the more control you can have over your impact.

[44] _________________________________
Enlist the support of professionals. You don't need a whole glam squad, but consider hiring a stylist for a couple of hours or consulting a knowledgeable salesperson or friend. It's not as expensive as you might think.

[45] _________________________________
The point of a style upgrade isn't to become more vain, or to spend more time fussing with your clothes. It's to make getting dressed easy and give you more time and mental energy for what matters. Edit down your options. Buy all your clothes at once with a stylist instead of shopping alone, one article of clothing at a time."""

passages[0]["content"] = p0_content
passages[0]["passage_type"] = "cloze"
passages[0]["order_index"] = 0

passages[1]["content"] = p1_content
passages[1]["passage_type"] = "reading"
passages[1]["order_index"] = 1

passages[2]["content"] = p2_content
passages[2]["passage_type"] = "reading"
passages[2]["order_index"] = 2

passages[3]["content"] = p3_content
passages[3]["passage_type"] = "reading"
passages[3]["order_index"] = 3

passages[4]["content"] = p4_content
passages[4]["passage_type"] = "reading"
passages[4]["order_index"] = 4

passages[5]["content"] = p5_content
passages[5]["passage_type"] = "reading"
passages[5]["order_index"] = 5

# 3. Gold Question Reconstructions
gold_cloze = {
    1: {
        "opts": [("A", "as well as"), ("B", "by way of"), ("C", "on behalf of"), ("D", "with regard to")],
        "ans": "A",
        "expl": "［考点提炼］句内并列逻辑与介词短语辨析。\n［精准定位］空格所在句：It may involve not only his parents and his friends, [1] those of the young woman, but also a matchmaker.\n［解题思路］句中出现 not only... but also... 结构，空格前后连接并列人物名词 his parents and his friends 与 those of the young woman（指代女方的父母朋友）。[A] as well as 意为“以及，除……之外也”，与 not only 构成自然补充并列，符合文意。\n［错项排除］[B] by way of 意为“经由，作为”；[C] on behalf of 意为“代表”；[D] with regard to 意为“关于”，均无法表示并列关系。"
    },
    2: {
        "opts": [("A", "adapt to"), ("B", "provide for"), ("C", "compete with"), ("D", "decide on")],
        "ans": "D",
        "expl": "［考点提炼］动词短语语义辨析与上下文线索。\n［精准定位］空格所在句：A young man can [2] a likely spouse on his own and then ask his parents to [3] the marriage negotiations, or the young man's parents may make the choice of a spouse...\n［解题思路］or 后面并列分句表示父母替孩子做选择（make the choice of a spouse），与前面分句年轻男子自己（on his own）选择配偶形成并列对应，[D] decide on 意为“选定，决定”，与 make the choice 语义契合。\n［错项排除］[A] adapt to 意为“适应”；[B] provide for 意为“抚养，供养”；[C] compete with 意为“与……竞争”，均不符合语境。"
    },
    3: {
        "opts": [("A", "renew"), ("B", "close"), ("C", "arrange"), ("D", "postpone")],
        "ans": "C",
        "expl": "［考点提炼］句内动作顺承与动词辨析。\n［精准定位］空格所在句：...and then ask his parents to [3] the marriage negotiations...\n［解题思路］and then 表示动作承接。年轻男子自己选定意中人之后，请求父母“安排/筹办”提亲议婚事宜。[C] arrange 意为“安排，筹划”，完全符合婚礼礼仪流程。\n［错项排除］[A] renew 意为“重新开始”；[B] close 意为“结束”；[D] postpone 意为“推迟”，均与求婚提亲的语境相悖。"
    },
    4: {
        "opts": [("A", "In theory"), ("B", "In time"), ("C", "Above all"), ("D", "For example")],
        "ans": "A",
        "expl": "［考点提炼］句际逻辑关系与状语短语辨析。\n［精准定位］空格所在句：[4], a girl may veto the spouse her parents have chosen.\n［解题思路］上句指出如果父母作主，孩子几乎毫无发言权（giving the child little to say in the selection）。本句指出女孩可以否决父母选定的配偶。[A] In theory 意为“理论上”，表明这只存在于理论条文中，实践中往往难以违抗父母之命，与上下文形成精准逻辑对比。\n［错项排除］[B] In time 意为“及时，终究”；[C] Above all 意为“最重要的是”；[D] For example 意为“例如”，均不符合反差对比逻辑。"
    },
    5: {
        "opts": [("A", "Although"), ("B", "Lest"), ("C", "After"), ("D", "Unless")],
        "ans": "C",
        "expl": "［考点提炼］时间顺序与从属连词辨析。\n［精准定位］空格所在句：[5] a spouse has been selected, each family investigates the other to make sure its child is marrying [6] a good family.\n［解题思路］从时态 has been selected（现在完成时）到 investigates（一般现在时），体现程序上的先后承接关系：配偶选定之后，双方家庭展开背景调查。[C] After 意为“在……之后”，逻辑严丝合缝。\n［错项排除］[A] Although 表让步；[B] Lest 表唯恐、以免；[D] Unless 表除非，均违背顺承程序逻辑。"
    },
    6: {
        "opts": [("A", "within"), ("B", "into"), ("C", "from"), ("D", "through")],
        "ans": "B",
        "expl": "［考点提炼］介词固定搭配。\n［精准定位］空格所在句：...to make sure its child is marrying [6] a good family.\n［解题思路］marry into a family 为地道英文固定搭配，意为“通过婚姻嫁入/入赘到……家庭”。此处表示确保孩子能与一个门当户对的好人家联姻，[B] into 完全正确。\n［错项排除］[A] within 表示在某范围内部；[C] from 表示来自；[D] through 表示通过、穿过，均不能与 marry 构成此特定婚姻搭配。"
    },
    7: {
        "opts": [("A", "since"), ("B", "or"), ("C", "so"), ("D", "but")],
        "ans": "D",
        "expl": "［考点提炼］分句转折对比与连词辨析。\n［精准定位］空格所在句：Formerly it lasted three days, [7] by the 1980s it more commonly lasted a day and a half.\n［解题思路］Formerly（从前，三天）与 by the 1980s（20世纪80年代，一天半）形成鲜明的时间与习俗演化对比，[D] but 表并列转折对比，语义通顺。\n［错项排除］[A] since 表自从或因为；[B] or 表选择；[C] so 表因果，均无法表达前后时间长度的反差对比。"
    },
    8: {
        "opts": [("A", "test"), ("B", "recite"), ("C", "copy"), ("D", "create")],
        "ans": "B",
        "expl": "［考点提炼］动词语义搭配与宗教仪式语境。\n［精准定位］空格所在句：Buddhist priests offer a short sermon and [8] prayers of blessing.\n［解题思路］and 连接僧侣主持仪式的两个动作：布道（offer a short sermon）与吟诵祈福祝祷词（recite prayers of blessing）。[B] recite 意为“朗诵，吟诵”，是宗教祈祷的固定搭配。\n［错项排除］[A] test 意为“测试”；[C] copy 意为“抄写，复制”；[D] create 意为“创造”，在现场婚礼仪式中僧侣不可能“测试”或“抄写/创造”祈福词。"
    },
    9: {
        "opts": [("A", "folding"), ("B", "piling"), ("C", "wrapping"), ("D", "tying")],
        "ans": "D",
        "expl": "［考点提炼］动词与宾语介词搭配。\n［精准定位］空格所在句：...[9] cotton threads soaked in holy water around the bride's and groom's wrists...\n［解题思路］tie... around... 为固定搭配，意为“把……系/缠在……周围”。此处指柬埔寨传统仪式中把圣水浸泡过的棉线系在新郎新娘手腕上象征永结同心，[D] tying 正确。\n［错项排除］[A] folding 意为“折叠”；[B] piling 意为“堆积”；[C] wrapping 意为“包裹”，棉线无法 folding 或 piling，且 tie around 最为贴切精准。"
    },
    10: {
        "opts": [("A", "passing"), ("B", "lighting"), ("C", "hiding"), ("D", "serving")],
        "ans": "A",
        "expl": "［考点提炼］动词搭配与仪式场景。\n［精准定位］空格所在句：...and [10] a candle around a circle of happily married and respected couples to bless the [11].\n［解题思路］pass a candle around a circle 表示在围成一圈的人群中依次“传递”点燃的蜡烛，将幸福美满的婚姻祝福传递下去，[A] passing 符合民俗语境。\n［错项排除］[B] lighting 意为“点燃”，虽然蜡烛可以 light，但不能说“在一圈人中点燃蜡烛并传递祝福”；[C] hiding 意为“隐藏”；[D] serving 意为“端上，服务”，均不符合语境。"
    },
    11: {
        "opts": [("A", "association"), ("B", "meeting"), ("C", "collection"), ("D", "union")],
        "ans": "D",
        "expl": "［考点提炼］熟词僻义与名词辨析。\n［精准定位］空格所在句：...to bless the [11].\n［解题思路］前文描述全套婚礼仪式，目的自然是祝福新人喜结连理，即祝福这段新结合的婚姻。[D] union 可指“婚姻，结合”（a marriage/matrimonial union），完全吻合文意。\n［错项排除］[A] association 意为“协会，联系”；[B] meeting 意为“会议”；[C] collection 意为“收藏品，收集”，均不能指代新人神圣的婚姻结合。"
    },
    12: {
        "opts": [("A", "grow"), ("B", "part"), ("C", "live"), ("D", "deal")],
        "ans": "C",
        "expl": "［考点提炼］动词短语语义顺承。\n［精准定位］空格所在句：Newlyweds traditionally move in with the wife's parents and may [12] with them up to a year...\n［解题思路］前文 move in with the wife's parents（搬来与女方父母同住），由 and 连接，顺承说明“可以和他们生活/居住至多一年”，[C] live (with) 意为“同住，共同生活”，与文意高度自洽。\n［错项排除］[A] grow with 意为“与……一同成长”；[B] part with 意为“舍弃，与……分离”；[D] deal with 意为“应付，处理”，均违背居住语境。"
    },
    13: {
        "opts": [("A", "whereas"), ("B", "until"), ("C", "for"), ("D", "if")],
        "ans": "B",
        "expl": "［考点提炼］时间连词辨析。\n［精准定位］空格所在句：...may live with them up to a year, [13] they can build a new house nearby.\n［解题思路］新婚夫妇与女方父母居住长达一年，“直到”他们能在附近建好自己的新房为止，[B] until 表时间终点，逻辑顺畅。\n［错项排除］[A] whereas 表对比转折；[C] for 表因为；[D] if 表如果，均不符合时间期限与居住过渡逻辑。"
    },
    14: {
        "opts": [("A", "follow"), ("B", "obtain"), ("C", "challenge"), ("D", "avoid")],
        "ans": "B",
        "expl": "［考点提炼］动宾搭配与上下文对比。\n［精准定位］空格所在句：Divorce is legal and easy to [14], but not common.\n［解题思路］空格与 legal 构成并列同向表达，主语为 Divorce。离婚合法且容易“办理/取得”（obtain a divorce 为地道用法），但并不常见，[B] obtain 正确。\n［错项排除］[A] follow 意为“遵循，理解”；[C] challenge 意为“质疑，挑战”；[D] avoid 意为“避免”，均无法表达依法办理取得离婚资格。"
    },
    15: {
        "opts": [("A", "isolated"), ("B", "persuaded"), ("C", "viewed"), ("D", "exposed")],
        "ans": "C",
        "expl": "［考点提炼］动词与介词 with 搭配。\n［精准定位］空格所在句：Divorced persons are [15] with some disapproval.\n［解题思路］view... with disapproval 意为“带着某种不赞成/非议的眼光看待某人”。离婚者会受到一定程度的非议，[C] viewed 正确。\n［错项排除］[A] isolated 搭配 from；[B] persuaded 意为“被说服”；[D] exposed 搭配 to，均不能与 with some disapproval 构成自然搭配。"
    },
    16: {
        "opts": [("A", "whatever"), ("B", "however"), ("C", "whenever"), ("D", "wherever")],
        "ans": "A",
        "expl": "［考点提炼］连接代词引导名词性从句。\n［精准定位］空格所在句：Each spouse retains [16] property he or she brought into the marriage...\n［解题思路］retains 之后需要接宾语从句修饰名词 property，[A] whatever 充当限制性定语修饰 property，引导宾语从句，意为“无论何种财产”，语义完整。\n［错项排除］[B] however、[C] whenever、[D] wherever 均为副词，分别引导方式、时间、地点状语，不能作定语修饰 property。"
    },
    17: {
        "opts": [("A", "changed"), ("B", "brought"), ("C", "shaped"), ("D", "pushed")],
        "ans": "B",
        "expl": "［考点提炼］动词搭配与婚前财产语境。\n［精准定位］空格所在句：...property he or she [17] into the marriage...\n［解题思路］bring into the marriage 为婚产分割法律术语，意为“带入婚姻的财产”，即婚前财产。[B] brought 正确。\n［错项排除］[A] changed into 意为“转变成”；[C] shaped into 意为“塑造成”；[D] pushed into 意为“推入”，均不符合婚姻财产法理常识。"
    },
    18: {
        "opts": [("A", "withdrawn"), ("B", "invested"), ("C", "donated"), ("D", "divided")],
        "ans": "D",
        "expl": "［考点提炼］动词与副词 equally 搭配。\n［精准定位］空格所在句：...and jointly-acquired property is [18] equally.\n［解题思路］jointly-acquired property 指夫妻婚后共同财产。既然婚前财产各自保留，共同财产自然是“均分”，divide equally 意为“平均分割”，[D] divided 正确。\n［错项排除］[A] withdrawn 意为“提现，撤回”；[B] invested 意为“投资”；[C] donated 意为“捐赠”，均不合平分家产语境。"
    },
    19: {
        "opts": [("A", "clears"), ("B", "shows"), ("C", "warms"), ("D", "breaks")],
        "ans": "B",
        "expl": "［考点提炼］动词短语辨析。\n［精准定位］空格所在句：Divorced persons may remarry, but a gender prejudice [19] up: The divorced male doesn't have a waiting period...\n［解题思路］冒号后面具体指出离异男性再婚无等待期，而女性必须等待十个月，显而易见存在性别偏见。show up 意为“显露，显现”，[B] shows 正确。\n［错项排除］[A] clear up 意为“清理，天气放晴”；[C] warm up 意为“活跃，热身”；[D] break up 意为“破碎，结束”，均无法表示偏见显露。"
    },
    20: {
        "opts": [("A", "while"), ("B", "once"), ("C", "so that"), ("D", "in that")],
        "ans": "A",
        "expl": "［考点提炼］句内逻辑。\n\n［解题思路］空格前分句“离异男性再婚之前没有等待期”与空格后分句“女性必须要等待十个月”存在语义对比（离异男性VS女性、无等待期VS等待十个月），故空格处应体现对比逻辑。［A］ while 用于对比两件事物，符合文意。\n\n［错项排除］［B］ once 作连词时意为 as soon as，表条件；［C］ so that 或引出结果，或表示目的；［D］ in that 表示因果关系，但“离异女性必须等待十个月”并非“离异男性再婚之前无等待期”的条件、结果、目的或原因，故排除此三项。"
    }
}

gold_reading = {
    21: {
        "stem": "According to the first paragraph, what would happen in France?",
        "opts": [("A", "Physical beauty would be redefined."), ("B", "New runways would be constructed."), ("C", "Websites about dieting would thrive."), ("D", "The fashion industry would decline.")],
        "ans": "A",
        "expl": "［考点提炼］事实细节题。\n［精准定位］第一段①句指出，法国裁定其时尚业不再享有界定女性形体美的绝对权（its fashion industry has lost an absolute right to define physical beauty for women），②③句进一步阐述禁止极瘦模特走秀、取缔极端节食网站的法案。\n［命题解密］题干与正确项 [A] Physical beauty would be redefined是对第一段主旨的概括提炼：极瘦不再是唯一的美，形体美将被重新定义。\n［错项排除］[B]项曲解法规对T台模特的限制；[C]项颠倒黑白，法案意在取缔（ban）此类网站而非让其蓬勃发展（thrive）；[D]项过度推断，法规旨在规范模特健康，并非导致整个时尚行业衰退。"
    },
    22: {
        "stem": "The phrase \"impinging on\" (Line 2, Para. 2) is closest in meaning to ________.",
        "opts": [("A", "indicating the state of"), ("B", "heightening the value of"), ("C", "losing faith in"), ("D", "doing harm to")],
        "ans": "D",
        "expl": "［考点提炼］词义推断题。\n［精准定位］第二段②句指出：They suggest beauty should not be defined by looks that end up impinging on health.\n［解题思路］上文提到模特因过度节食而饿死（starving themselves to death），法令明确反对以牺牲健康为代价的瘦削，因此美不应由最终“危害/损害”健康的容貌来界定。[D] doing harm to 意为“对……造成损害”，与 impinging on 含义最为接近。\n［错项排除］[A] indicating the state of（表明……的状态）；[B] heightening the value of（提高……的价值）；[C] losing faith in（对……失去信心），均脱离损害健康的语境。"
    },
    23: {
        "stem": "Which of the following is true of the fashion industry?",
        "opts": [("A", "The French measures have already failed."), ("B", "Its inherent problems are getting worse."), ("C", "Models are no longer under peer pressure."), ("D", "New standards are being set in Denmark.")],
        "ans": "D",
        "expl": "［考点提炼］事实细节正误判断题。\n［精准定位］第五段②句指出：In Denmark, the United States, and a few other countries, it is trying to set voluntary standards for models and fashion images... 第六段详细介绍了丹麦时尚界达成的行业自愿新标准。\n［命题解密］正确项 [D] New standards are being set in Denmark 是对五、六两段关于丹麦时尚伦理宪章事实的同义转述。\n［错项排除］[A]项无中生有，法案刚获初步批准，谈不上已经失败；[B]项中 are getting worse 原文未提及；[C]项与文意相反，丹麦等国的自愿标准恰恰更多依赖同侪压力（rely more on peer pressure）来执行。"
    },
    24: {
        "stem": "A designer is most likely to be rejected by CFW for ________.",
        "opts": [("A", "pursuing perfect physical conditions"), ("B", "caring too much about models' character"), ("C", "showing little concern for health factors"), ("D", "setting a high age threshold for models")],
        "ans": "C",
        "expl": "［考点提炼］事实推断与因果细节题。\n［精准定位］第六段①句提到丹麦达成关于模特年龄、健康及其它特征的规范与处罚（rules and sanctions regarding the age, health...），③句指出主要强制手段为拒绝违规设计师参加哥本哈根时装周（to deny access for designers and modeling agencies to CFW）。\n［命题解密］结合宪章强调对模特健康负责可知，如果设计师不顾及模特健康因素，极易被CFW拒之门外，[C] showing little concern for health factors 符合题意。\n［错项排除］[A]项追求完美体魄并非受罚理由；[B]项注重模特品格符合文章提倡方向；[D]项设定高年龄门槛与保护未成年模特的初衷背道而驰。"
    },
    25: {
        "stem": "Which of the following may be the best title of the text?",
        "opts": [("A", "The Great Threats to the Fashion Industry"), ("B", "Just Another Round of Struggle for Beauty"), ("C", "A Dilemma for the Starving Models in France"), ("D", "A Challenge to the Fashion Industry's Body Ideals")],
        "ans": "D",
        "expl": "［考点提炼］全文主旨大意题。\n［精准定位］全文围绕法国立法禁止超瘦模特以及丹麦等国推行行业健康自愿标准展开，核心议题在于挑战并纠正时尚界长期奉行的病态身材标准（misuse of body ideals）。\n［命题解密］[D] A Challenge to the Fashion Industry's Body Ideals（对时尚业身材典范的挑战）精准涵盖全文中心论题，且态度鲜明中肯。\n［错项排除］[A]项夸大事实，文章并非讨论时尚业的灭顶之灾；[B]项泛泛而谈，偏离法律与行业规范的主旨；[C]项局限于法国模特的困境，忽视了国际反思与伦理标准的主线。"
    },
    26: {
        "stem": "Britain's public sentiment about the countryside ________.",
        "opts": [("A", "is not well reflected in politics"), ("B", "is fully backed by the royal family"), ("C", "didn't start till the Shakespearean age"), ("D", "has brought much benefit to the NHS")],
        "ans": "A",
        "expl": "［精准定位］第一段③句明确指出：英国人很重视乡村，认为“乡村”与王室、莎士比亚、NHS 一样，令他们引以为傲，但是这种民意得到的政治支持却非常有限。换言之，英国民众对乡村的观点没有在政治中得到很好的体现。［A］正确。\n\n［命题解密］正确项［A］是对第一段③句has limited political support的合理解读。\n\n［B］利用③句royal family、support等词捏造出“受到王室的全面支持”，但文中并未介绍王室的态度。［C］利用③句Shakespeare捏造关联，但文中用其旨在体现“人们对countryside的重视：将其与Shakespeare相提并论”，并未介绍英国民众乡村观的起始时间。［D］利用③句NHS捏造关联，由makes them proudest捏造出“带给NHS许多好处”，但同样文中提到NHS旨在突出人们对乡村的重视（将其与NHS等并列，视为“国之四宝”），二者并无直接关联。\n\n［技巧总结］本题直接考点为第一段③句（长难句），实际全面考查对第一段信息的分析能力。正确解答此类试题需要考生：1）会读题，抓住各选项关键信息，锁定答题范围；2）细读文，借助语法知识理清句子结构，由逻辑关联词确定各语义成分功能，明确句子语义重点以及各提及对象之间关系。\n具体来看，首先读题：根据四个选项关键词politics、royal family、Shakespearean age、NHS可锁定本题答题范围在③句。随后梳理理清句子结构：While构成句内转折，语义重点在后：转折之前Britons rate the countryside alongside... as...（人们认为乡村与 一样，都是 ）为题干所述内容（即民众对乡村的看法），其中the countryside与the royal family、Shakespeare、NHS为并列平行结构，四者之间并无直接语义逻辑关联；this（指代前半句）has limited political support为语义重点。最后于语义重点中比对选项：唯有［A］体现作者强调内容，故正确；［B］、［C］、［D］均以并列平行结构the royal family、Shakespeare、NHS强生关联，故错误。"
    },
    27: {
        "stem": "According to Paragraph 2, the achievements of the National Trust are now being ________.",
        "opts": [("A", "largely overshadowed"), ("B", "properly protected"), ("C", "effectively reinforced"), ("D", "gradually destroyed")],
        "ans": "D",
        "expl": "［精准定位］第二段④句指出：现在他们（即英国当局）不仅不再建设乡村，甚至逐年用混凝土（即城市建设）吞噬乡村（土地）。这很明显与①②句所述国民托管组织宗旨（永葆自然美之地）背道而驰，损坏了③句所述该组织所取得的成果（使得国家公园和绿化带得以创建）。故［D］正确。\n\n［命题解密］正确项［D］是对④句中第二分句的同义概括，其中gradually对应every year, destroyed对应consumes。\n\n［A］因④句They don't make countryside any more and... consumes more of it 而来，但句中They 实指英国当局，而非组织本身，组织所取得的成就是“被破坏，逐渐消失”而非“被蒙上阴影，黯然失色”。［B］根据⑤句constant guardianship（持续保护）制造出properly protected（恰当保护），却将文意“作者建议乡村需要持续保护”篡改为“作者描述组织目前的成果维护情况”。［C］源自④句concrete一词，但此处该词为名词“混凝土”（混凝土吞噬了该组织的成果），并非动词“巩固，加强”（该组织的成果正被加强）。\n\n［技巧总结］本题就涉及今昔变化以及多个提及对象的段落（第二段）命制事实概括题。解答此类题时需要考生：1）根据原文时态或时间标记词（no more, not any more, no longer）等理解事实细节、概括得出今昔变化；2）借助作者评论性话语把握整体趋势。\n如本题，首先了解事实细节：根据A century ago可推知国民托管组织的创建初衷“旨在永葆自然美之地”，根据later可推知该组织的成就“使得诸多国家公园和绿化带得以创建”，根据一般现在时态及every year可推知英国住建当局不再建设乡村，相反每年混凝土还吞噬乡村。随后概括今昔对比得出：国民托管组织的成果正逐年被破坏。最后结合末句作者评注（呼吁）“乡村需要持续保护”，可确定［D］为答案。"
    },
    28: {
        "stem": "Which of the following can be inferred from Paragraph 3?",
        "opts": [("A", "Labour is under attack for opposing development."), ("B", "The Conservatives may abandon \"off-plan\" building."), ("C", "Ukip may gain from its support for rural conservation."), ("D", "The Liberal Democrats are losing political influence.")],
        "ans": "C",
        "expl": "［精准定位］根据第三段⑥⑦句可知，Ukip是下一届选举中唯一支持乡村保护的政党，且⑥句中“嗅到了机会”暗示UKip将从中获利，⑦句中其发起的运动使得许多地方保守党胆战心惊（证明其已然获利），故［C］正确。\n\n［命题解密］根据本段各句主语可知，作者按“三大党派（保守党、工党、自由民主党）VS独立党（UKip）”的逻辑行文，通过介绍各党派对于“乡村开发还是保护”的态度（即对于民意的支持与否），反衬出唯一支持民意的独立党（UKip）的举动以及可能由此带来的影响（获利）。［C］为根据该信息做出的合理推断。\n\n［A］从④句中得出，但句中指出“地方议会反对乡村开发”，而不是工党；工党“反对地方规划”，故错误。［B］根据②句off-plan building得出，但该句指出保守党“支持乡村开发优先于乡村保护，甚至批准'计划外'建设”，由此并不能推知保守党将“放弃计划外建设”，故错误。［D］根据⑤句得出，但由The Liberal Democrats are silent 只能推知自民党未就“乡村保护”表态，losing political influence从⑤句中难以推断，证实［C］正确。"
    },
    29: {
        "stem": "The author holds that George Osborne's preference ________.",
        "opts": [("A", "shows his disregard for the character of rural areas"), ("B", "stresses the necessity of easing the housing crisis"), ("C", "highlights his firm stand against lobby pressure"), ("D", "reveals a strong prejudice against urban areas")],
        "ans": "A",
        "expl": "［精准定位］第五段⑥⑦句指出：乡村得到了发展且将一直发展下去，而在村镇边缘建设并尊重其特征的做法最为可取。而③④句指出：在游说团体的压力下，Osborne支持乡村新建，支持城外购物场所建设。言外之意为：Osborne的做法与这种可取的做法背道而驰，不尊重乡村的特征。［A］正确。\n\n［命题解密］正确项［A］由第三四句Osborne的做法以及第六七句作者所建议的做法对比推断得出。\n\n［B］利用①②句中housing crisis, need for more houses干扰，文中指出“住房危机等同于将草地变成混凝土建筑纯粹是游说之词，问题不是需要更多房屋而是建在哪里”，可见作者意在强调“住房危机并非需要在乡村建房的合理借口”，由此并不能推知Osborne强调缓解住房危机。［C］与③句Under lobby pressure...（在游说团体的压力下……）文意相悖。［D］与③句against urban renovation and renewal（反对城市改造更新）相悖，Osborne反对城市更新并非出于“对城市的偏见”，而是出于“对游说团体的顺从”。\n\n［技巧总结］本题就作者对George Osborne的观点态度进行考查。通常作者态度往往体现在字里行间的用词色彩上（褒义、贬义、中性）；在涉及对比的语段中，往往体现在作者对不同立场的取舍上。本题中，首先由Under lobby pressure（迫于游说团体的压力）以及a biased one（有偏见/不公允的市场）可知作者对Osborne持批评态度，进而排除［B］与［C］（均含肯定色彩）；再结合后文作者对乡村建设的建议（building sticks to their edges and respects their character）对比Osborne的实际做法，即可得知唯有［A］跟countryside搭边，且指出了 Osborne对乡村的忽视，故正确。"
    },
    30: {
        "stem": "In the last paragraph, the author shows his appreciation of ________.",
        "opts": [("A", "the size of population in Britain"), ("B", "the enviable urban lifestyle in Britain"), ("C", "the town-and-country planning in Britain"), ("D", "the political life in today's Britain")],
        "ans": "C",
        "expl": "［精准定位］第六段③句指岀半个世纪的城乡规划使得拥挤度位居欧洲第二的英国拥有令人艳羡的乡村协调性以及低密度城市居住条件，很明显作者对英国城乡规划表示欣赏。［C］正确。\n\n［命题解密］题干 + 正确项［C］是对第六段③句 town and country planning has enabled... enviable rural coherence... low-density urban living的合理解读，其中 appreciation 对应原文 enviable。\n\n［A］源自②句Europe's most crowded country,但文中意在说明英国拥挤程度之高（反衬城乡规划的重要作用），而非欣赏英国的人口规模。［B］根据③句enviable, urban living捏造出“令人羡慕的城市生活”，但文中enviable修饰的是rural coherence（乡村和谐协调），而非urban living。［D］为全文的引申信息，但纵观全文，作者一直强调“政党不支持乡村保护”，故作者不可能对其表示欣赏。\n\n［技巧总结］题干问及“作者对……的欣赏”，结合选项内容可知，本题考查考生对第六段具体细节的理解。本题解答可借助褒义词enviable迅速反推答案：纵观第六段，唯有③句中使用了具有明显褒贬色彩的形容词enviable（令人羡慕的），从而确定答题范围为③句；随后细读该句：Half a century of town and country planning has enabled it to retain an enviable rural coherence, while still permitting low-density urban living（半个世纪的城乡规划使得拥挤度位居欧洲第二的英国拥有令人艳羡的乡村协调性，同时还允许低密度的城市生活），由主语Half a century of town and country planning以及谓语动词has enabled可知，英国之所以拥有令人艳羡的乡村协调性（enviable rural coherence），以及低密度的城市生活（low-density urban living)，体现出作者的赏识，故［C］正确。"
    },
    31: {
        "stem": "The author views Milton Friedman's statement about CSR with ________.",
        "opts": [("A", "tolerance"), ("B", "skepticism"), ("C", "approval"), ("D", "uncertainty")],
        "ans": "B",
        "expl": "［精准定位］首段①句先介绍Friedman观点，②句则转折指出“即便认同其前提假设，……，事实可能也非绝对分明”，③句则指出新研究表明CSR能够给企业带来货币价值。由此可推知，作者对于Friedman的言论持怀疑态度，［B］正确。\n\n［命题解密］由①句wrote Milton Friedman, a Nobel Prize-winning economist可知作者对Friedman的身份给予了客观介绍；紧接着在②句以But even if you accept Friedman's premise...引出自己的看法，其中premise说明Friedman言论仅仅是一家之言（属于未经验证的前提假设），things may not be absolutely clear-cut则直接针对Friedman言论提出质疑；最后在③句借New research（新研究发现）直接驳斥Friedman观点，由此可知作者对Friedman言论持怀疑态度，即［B］正确。\n\n［A］“宽容”、［C］“认可”与文意相悖；［D］“不确定”，纵观全文，作者态度十分明确（借助研究结论肯定CSR的积极价值，反驳Friedman言论），而非不确定。\n\n［技巧总结］作者观点态度题的解答关键在于：1）把握文章主旨大意；2）理清各观点持有者之间的逻辑关系；3）关注带有褒贬色彩的词汇或特殊句式。一般而言，转折连词（如本题中的But）、作者对论据（或某一观点）的评价性话语（如本题中的things may not be absolutely clear-cut）、以及具有公信力的新近事实（如本题中借引的新研究发现）往往和作者观点一致；让步假设、虚拟语气等的真实语义和表面含义通常相反。"
    },
    32: {
        "stem": "According to Paragraph 2, CSR helps a company by ________.",
        "opts": [("A", "guarding it against malpractices"), ("B", "protecting it from being defamed"), ("C", "winning trust from consumers"), ("D", "raising the quality of its products")],
        "ans": "C",
        "expl": "［精准定位］第二段介绍了 CSR使企业增值的三种方式：一、消费者将CSR看作是企业产品质量高的标志；二、消费者出于间接捐助慈善事业的心理愿意购买产品；三、CSR使消费者及他人对企业更加关注并认可。可见这三种方式共同之处在于“为企业赢得来自消费者的信任”，［C］正确。\n\n［命题解密］［C］抓住了③④⑤句核心关键人物consumers/customers,并概括提炼出内容背后信息：无论是第一种方式中所提及的“将CSR视作企业产品质量高的标志(take... as a signal that...)”，还是第二种方式中所提及的“出于间接捐助慈善事业的心理愿意购买产品(willing to buy... as an indirect way to donate...)”，亦或是第三种方式中所提及的“赢得来自消费者及他人的尊重(earn greater respect from both consumers and others)”，均与“赢得消费者信任(winning trust from consumers)”密切相关。\n\n［A］利用第二段末句halo effect（光环效应）设置干扰，将第三段首句消费者可能受到所有三种效应的影响、以及行贿诉讼偷换概念为防范企业做出不法行为。［B］将文意偷换为保护企业名誉免遭诋毁。［D］对第一种方式断章取义，由consumers may take CSR spending as a signal that a company's products are of high quality（消费者可能会将企业在CSR上的花销看作是企业产品高质量的标志）捏造出“提高企业产品质量”，但实际上这只是消费者的主观认知而非客观事实。\n\n［技巧总结］由题目设问方式According to Paragraph 2, CSR helps a company by可知本题既可是考查第二段主旨，也可能是事实细节考查。浏览第二段可知，该段论述了CSR使企业增值的三种方式，且各方式均与消费者对于企业的信任度相关，可初步推知［C］正确；而［A］与［B］与该部分信息无直接关联，可排除。"
    },
    33: {
        "stem": "The expression \"more lenient\" (Para. 4) is closest in meaning to ________.",
        "opts": [("A", "less controversial"), ("B", "more effective"), ("C", "more lasting"), ("D", "less severe")],
        "ans": "D",
        "expl": "［精准定位］第四段①句（考查词所在句）指出：研究发现CSR计划最全面的企业往往会受到更宽大的处罚。②句随即解释该现象，指出原因在于企业在CSR方面的立场（CSR stand），并于冒号后对该立场进行说明：政治竞选捐款较多的企业并未获得较低罚款。由解释说明逻辑可知，lower fines与more lenient penalties语义同向，故判断出［D］正确。\n\n［命题解密］题干more lenient与正确项［D］less severe同义。从语法结构上来看，题干所在句与下文解释说明部分构成取舍关系，通过排除政治捐款的影响，突显CSR对减轻企业处罚的重要作用。\n\n［A］利用第四段中ruled out the possibility设置干扰，臆断出受到的处罚“争议较小”，偏离文意。［B］“更有效”和［C］“更持久”均无法与句中penalties形成合理搭配。\n\n［技巧总结］词义推断题的解题关键在于：在明确代入该词的句子信息的基础上，结合上下文语境（尤其是相邻句之间的逻辑关系：如因果、解释说明、并列或对比等），寻找同义复现或反义线索，以确保段落间建立起顺滑一致的逻辑关系。如本题的解答，通过判断第四段①②句间为补充解释关系，得知leniency与lower fines同义，基本确定［D］正确。再结合研究目的（区分CSR的三种效应、验证光环效应的影响）、研究方式（研究美国的行贿诉讼案例）以及第一段便已经明确的研究结论（CSR的光环效应能使企业在被诉时受益），可推知研究发现（考查词所在句内容）：CSR计划最全面的企业在被诉时受罚较轻，确定［D］为答案。而其他三项则无法在其间建立顺滑的逻辑关系，故排除。"
    },
    34: {
        "stem": "When prosecutors evaluate a case, a company's CSR record ________.",
        "opts": [("A", "has an impact on their decision"), ("B", "comes across as reliable evidence"), ("C", "increases the chance of being penalized"), ("D", "constitutes part of the investigation")],
        "ans": "A",
        "expl": "［精准定位］根据题干直接定位至第五段。该段首句指出，检察官原本应该只是基于案情本身进行评判，但实际上他们确实会受到公司CSR记录的影响，可见［A］符合文义。\n\n［命题解密］正确项［A］ has an impact 是对原文 they do seem to be influenced by a company's record in CSR的同义改写。\n\n［B］将检察官“基于案情本身判案，但难免受公司CSR记录的影响(seem to be influenced by)”夸大为“将公司CSR记录视为判案可靠证据(reliable evidence)”。［C］对②句increasing... by about 20% result in fines断章取义，从而将文中完整信息“企业捐赠提高20%/即CSR记录佳，则罚款会降低40%”改为“CSR记录会使得公司受罚可能性增加”。［D］对“检察官判案受企业CSR记录影响”过度推断出“企业CSR记录是检察官调查的一部分(constitutes part of the investigation)”，但由第三段可知，这种影响并非来自“调查”，而是来自“光环效应”。\n\n［技巧总结］本题就第五段所述的“研究结论”命制事实细节题。对于该类题型，需从两个角度加以考虑：①遵循事实细节题正确项的一般原则“题干+正确项=//~原文某句”；②注意“研究是为了论证文章主旨，研究结论体现的便是文章主旨”，故题干+正确项应与文章主旨高度契合。如本题题干+正确项 ［A］ When prosecutors evaluate a case, a company's CSR record has an impact on their decision 对应①句主要内容 they/prosecutors do seem to be influenced by a company's record in CSR，又体现了文章主旨，企业CSR会在其被诉时创造货币价值。"
    },
    35: {
        "stem": "Which of the following is true of CSR, according to the last paragraph?",
        "opts": [("A", "Its negative effects on businesses are often overlooked."), ("B", "The necessary amount of companies' spending on it is unknown."), ("C", "Companies' financial capacity for it has been overestimated."), ("D", "It has brought much benefit to the banking industry.")],
        "ans": "B",
        "expl": "［精准定位］末段首句指出，研究未能回答“企业应该在CSR上投入多少”这一问题，也即企业在CSR上具体的必要花费数额尚不得而知，［B］正确。\n\n［命题解密］正确项［B］是对末段首句their study does not answer the question of how much businesses ought to spend on CSR 的同义改写。\n\n［A］误认为末段③句get into trouble with the law... costly punishment 是在介绍“CSR 被人们所忽视的负面影响”，而实际上该句是在说明CSR最起码的积极作用。［C］将末段①句信息“研究未能解答企业应该在CSR上投入多少”曲解为“研究高估了企业的CSR支出能力/CSR财政能力”。［D］根据末段②句词汇banking望文生义、捏造出“CSR能为银行业带来很多收益”，而实际上banking on意为“指望”，和“银行业”无关。\n\n［技巧总结］从原文来看，命题的陷阱在于取舍结构、倒装句、否定句等特殊句式。从选项来看，命题人通常会采用望文生义（文中取某词僻义或特殊用法，选项却用其常见含义）、断章取义（不是整体理解句子信息，而是将个别词汇糅杂到一起形成完整的语句）等方式形成干扰。本题中，根据［A］negative effect、［B］spending on、［C］financial capacity、［D］banking industry 不难分别定位至③句、①句、①句、②句，但需要借助语法知识、语义逻辑、以及文章主题等才能理解到［C］曲解文意、［A］断章取义、［D］望文生义，只有［B］是对①句主要内容的同义表达。"
    },
    36: {
        "stem": "The New York Times is considering ending its print edition partly due to ________.",
        "opts": [("A", "the high cost of operation"), ("B", "the increasing online ad sales"), ("C", "the pressure from its investors"), ("D", "the complaints from its readers")],
        "ans": "A",
        "expl": "［考点提炼］因果事实细节题。\n［精准定位］第二段①②句指出报纸放弃印刷版的充足动力：The infrastructure required to make a physical newspaper - printing presses, delivery trucks - isn't just expensive; it's excessive at a time when online-only competitors don't have the same set of financial constraints.\n［命题解密］维持实体印刷版的印刷机、送货车等基础设施造价高昂，甚至在网络竞争对手面前显得过于昂贵，即高昂的运营维护成本，[A] the high cost of operation 正确对应 expensive 和 excessive。\n［错项排除］[B]项与第四句 print ad sales continue to dwarf their online... 形成的反差不符；[C]项投资者施压与[D]项读者投诉在文中均未提及。"
    },
    37: {
        "stem": "Peretti suggests that, in face of the present situation, the Times should ________.",
        "opts": [("A", "end the print edition for good"), ("B", "make strategic adjustments"), ("C", "seek new sources of readership"), ("D", "aim for efficient management")],
        "ans": "B",
        "expl": "［考点提炼］人物观点理解题。\n［精准定位］第三段至第五段Peretti指出：急于淘汰纸质版是个错误（rushing to eliminate... would be a mistake），不应彻底放弃忠实读者，而是可以通过提高售价将其转变为传承奢侈品（raise prices and make it into more of a legacy product）。\n［命题解密］Peretti建议不要一刀切停印，而是因势利导改变定位与定价策略，[B] make strategic adjustments（做出战略性调整）高度概括其策略主张。\n［错项排除］[A]项永久停印恰恰是Peretti明确反对的愚蠢做法；[C]项寻找新读者与关注忠实拥趸（most loyal customers）相悖；[D]项以高效管理为目标偏离文章产品转型的重心。"
    },
    38: {
        "stem": "It can be inferred from Paragraphs 5 and 6 that a \"legacy product\" ________.",
        "opts": [("A", "helps restore the glory of former times"), ("B", "is meant for the most loyal customers"), ("C", "will have the cost of printing reduced"), ("D", "expands the popularity of the paper")],
        "ans": "B",
        "expl": "［考点提炼］段落推理判断题。\n［精准定位］第六段①④句：The most loyal customers would still get the product they favor... In other words, look at print as a luxury, and make it for the people who are already obsessed with it.\n［命题解密］所谓传承产品（legacy product）就是将纸质报纸作为一种奢侈品，专供那些对其深深入迷、甚至心甘情愿支付高溢价的最忠实客户，[B] is meant for the most loyal customers 是最核心的本质特征。\n［错项排除］[A]项恢复往昔辉煌脱离实际；[C]项并未减少印刷成本；[D]项扩大知名度与定位小众忠实读者群体的策略完全相反。"
    },
    39: {
        "stem": "Peretti believes that, in a changing world, ________.",
        "opts": [("A", "traditional luxuries can stay unaffected"), ("B", "cautiousness facilitates problem-solving"), ("C", "aggressiveness better meets challenges"), ("D", "legacy businesses are becoming outdated")],
        "ans": "C",
        "expl": "［考点提炼］人物观点态度题。\n［精准定位］第七段末句Peretti总结道：In those situations, it's better to be more aggressive than less aggressive.\n［命题解密］当市场与世界发生巨变、过去的做法不再奏效时，更加积极进取比谨小慎微更能从容应对挑战，[C] aggressiveness better meets challenges 与原文原词精妙吻合。\n［错项排除］[A]项传统奢侈品不受影响与全文求变理念不符；[B]项主张谨慎行事与原文 more aggressive 正好相反；[D]项断言传承业务彻底过时过于武断绝对。"
    },
    40: {
        "stem": "Which of the following would be the best title of the text?",
        "opts": [("A", "Shift to Online Newspapers All at Once"), ("B", "Make Your Print Newspaper a Luxury Good"), ("C", "Keep Your Newspapers Forever in Fashion"), ("D", "Cherish the Newspaper Still in Your Hand")],
        "ans": "B",
        "expl": "［考点提炼］文章标题归纳题。\n［精准定位］全文开篇陈述纸质《纽约时报》终将走向终结的行业困局，随后借BuzzFeed CEO Peretti的建言，深入论证传统报业不应仓促关停纸质版，而应提价并将其打造成供忠实受众享用的传承奢侈品（look at print as a luxury）。\n［命题解密］[B] Make Your Print Newspaper a Luxury Good（让你的纸版报纸成为奢侈品）契合原刊标题（Make Them a Luxury Good），精准概括全文核心破局方案。\n［错项排除］[A]项一蹴而就转入网络正是文中反对的鲁莽行为；[C]项让报纸永远保持流行脱离现实；[D]项珍惜手中报纸流于感性怀旧，偏离商业战略调整的主题。"
    },
    41: {
        "stem": "Choose the best heading [A]-[G] for paragraph (41).",
        "opts": [("A", "Create a new image of yourself"), ("B", "Have confidence in yourself"), ("C", "Decide if the time is right"), ("D", "Understand the context"), ("E", "Work with professionals"), ("F", "Know your goals"), ("G", "Make it efficient")],
        "ans": "C",
        "expl": "［考点提炼］小标题匹配题。\n［精准定位］第四段讨论何时应该进行形象升级：指出形象升级并不能适用于每种情况，但在职业过渡期（in a period of transition）则是重新评估形象的合适时机（a good time to reassess your image）。\n［命题解密］全段关键词围绕 a good time 和是否需要升级展开，[C] Decide if the time is right（判断时机是否合适）准确概括本段中心论点。\n［错项排除］[A] Create a new image of yourself 过于宽泛，无法体现本段对时机的权衡考量。"
    },
    42: {
        "stem": "Choose the best heading [A]-[G] for paragraph (42).",
        "opts": [("A", "Create a new image of yourself"), ("B", "Have confidence in yourself"), ("C", "Decide if the time is right"), ("D", "Understand the context"), ("E", "Work with professionals"), ("F", "Know your goals"), ("G", "Make it efficient")],
        "ans": "F",
        "expl": "［考点提炼］小标题匹配题。\n［精准定位］第五段首句总领：Get clear on what impact you're trying to achieve. 末尾明确指出：Once you know your goal, it's easier to create a look that aligns with it.\n［命题解密］全段强调明确自己想通过外在形象达到的目标与影响力，[F] Know your goals（明确你的目标）为原文 your goal 的直接对应。\n［错项排除］其他选项均未涉及目标（goals）与预期成效的设定。"
    },
    43: {
        "stem": "Choose the best heading [A]-[G] for paragraph (43).",
        "opts": [("A", "Create a new image of yourself"), ("B", "Have confidence in yourself"), ("C", "Decide if the time is right"), ("D", "Understand the context"), ("E", "Work with professionals"), ("F", "Know your goals"), ("G", "Make it efficient")],
        "ans": "D",
        "expl": "［考点提炼］小标题匹配题。\n［精准定位］第六段建议像人类学家一样审视工作环境：Look at your work environment like an anthropologist. 段末总结：The better you understand your context, the more control you can have over your impact.\n［命题解密］全段剖析所处行业与公司的风气与环境脉络，[D] Understand the context（了解你所处的环境/语境）与段末原词完美呼应。\n［错项排除］其他选项均脱离了对工作环境与背景规范的考察。"
    },
    44: {
        "stem": "Choose the best heading [A]-[G] for paragraph (44).",
        "opts": [("A", "Create a new image of yourself"), ("B", "Have confidence in yourself"), ("C", "Decide if the time is right"), ("D", "Understand the context"), ("E", "Work with professionals"), ("F", "Know your goals"), ("G", "Make it efficient")],
        "ans": "E",
        "expl": "［考点提炼］小标题匹配题。\n［精准定位］第七段首句开门见山：Enlist the support of professionals. 接着具体建议雇佣形象造型师（hiring a stylist）或向懂行的销售人员请教。\n［命题解密］[E] Work with professionals（与专业人士合作）与段首首句及 hiring a stylist 形成直接呼应。\n［错项排除］其他选项均未涉及寻求外部专业人员支持这一核心行动。"
    },
    45: {
        "stem": "Choose the best heading [A]-[G] for paragraph (45).",
        "opts": [("A", "Create a new image of yourself"), ("B", "Have confidence in yourself"), ("C", "Decide if the time is right"), ("D", "Understand the context"), ("E", "Work with professionals"), ("F", "Know your goals"), ("G", "Make it efficient")],
        "ans": "G",
        "expl": "45. 【答案】G 【精解】第八段首两句通过正反对比指出：提升形象不是为了变得更自负或花费更多时间考虑穿衣打扮，而是为了减少决策疲劳，提高效率；后文进一步介绍正确做法，即如何高效地提升形象。选项[G] Make it efficient 为对本段主要观点的概括，efficient 与段末两句的具体做法一致。\n【干扰项设置】根据首句的 become more vain（变得更加虚荣、自负），可能会将包含 confidence（信心）的[B] Have confidence in yourself 当作正确项。但首先 vain 与 confidence 语义及褒贬色彩不同，vain 强调“爱慕虚荣”，为贬义，confidence 为褒义；其次，文中针对 become more vain 予以否定，与[B]的肯定态度不符；再次，继续阅读本段可知后文主要针对如何提高效率提出建议，并非“要有自信”，故排除[B]选项。"
    }
}

# 4. Update Questions in Exam Data
questions = data["questions"]

for idx, q in enumerate(questions):
    qnum = idx + 1
    q["question_number"] = qnum
    q["sort_order"] = qnum
    
    if qnum <= 20:
        q["score"] = 0.5
        q["points"] = 0.5
        q["question_type"] = "cloze_item"
        q["q_type"] = "cloze_item"
        q["passage_id"] = passages[0]["id"]
        cfg = gold_cloze[qnum]
        q["stem"] = f"Choose the best option for blank [{qnum}] in the passage:"
        q["answer"] = cfg["ans"]
        q["correct_answer"] = cfg["ans"]
        q["options"] = [{"key": k, "text": t, "value": k} for k, t in cfg["opts"]]
        q["explanation"] = cfg["expl"]
    elif qnum <= 25:
        q["score"] = 2.0
        q["points"] = 2.0
        q["question_type"] = "reading_item"
        q["q_type"] = "reading_item"
        q["passage_id"] = passages[1]["id"]
        cfg = gold_reading[qnum]
        q["stem"] = cfg["stem"]
        q["answer"] = cfg["ans"]
        q["correct_answer"] = cfg["ans"]
        q["options"] = [{"key": k, "text": t, "value": k} for k, t in cfg["opts"]]
        q["explanation"] = cfg["expl"]
    elif qnum <= 30:
        q["score"] = 2.0
        q["points"] = 2.0
        q["question_type"] = "reading_item"
        q["q_type"] = "reading_item"
        q["passage_id"] = passages[2]["id"]
        cfg = gold_reading[qnum]
        q["stem"] = cfg["stem"]
        q["answer"] = cfg["ans"]
        q["correct_answer"] = cfg["ans"]
        q["options"] = [{"key": k, "text": t, "value": k} for k, t in cfg["opts"]]
        q["explanation"] = cfg["expl"]
    elif qnum <= 35:
        q["score"] = 2.0
        q["points"] = 2.0
        q["question_type"] = "reading_item"
        q["q_type"] = "reading_item"
        q["passage_id"] = passages[3]["id"]
        cfg = gold_reading[qnum]
        q["stem"] = cfg["stem"]
        q["answer"] = cfg["ans"]
        q["correct_answer"] = cfg["ans"]
        q["options"] = [{"key": k, "text": t, "value": k} for k, t in cfg["opts"]]
        q["explanation"] = cfg["expl"]
    elif qnum <= 40:
        q["score"] = 2.0
        q["points"] = 2.0
        q["question_type"] = "reading_item"
        q["q_type"] = "reading_item"
        q["passage_id"] = passages[4]["id"]
        cfg = gold_reading[qnum]
        q["stem"] = cfg["stem"]
        q["answer"] = cfg["ans"]
        q["correct_answer"] = cfg["ans"]
        q["options"] = [{"key": k, "text": t, "value": k} for k, t in cfg["opts"]]
        q["explanation"] = cfg["expl"]
    else:
        q["score"] = 2.0
        q["points"] = 2.0
        q["question_type"] = "reading_item"
        q["q_type"] = "reading_item"
        q["passage_id"] = passages[5]["id"]
        cfg = gold_reading[qnum]
        q["stem"] = cfg["stem"]
        q["answer"] = cfg["ans"]
        q["correct_answer"] = cfg["ans"]
        q["options"] = [{"key": k, "text": t, "value": k} for k, t in cfg["opts"]]
        q["explanation"] = cfg["expl"]

# Save reconstructed JSON
with open(EXAM_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Round 64: 2016 ky1 gold JSON successfully written to", EXAM_PATH)
