# -*- coding: utf-8 -*-
import json
import os

EXAM_ID = "1ac5713f-fb5d-560f-a22a-3c5c3431d03f"

PASSAGES = [
    # Passage 0: Section I Cloze (ID: b599cacf-7052-514f-8446-7e74e5f4358d)
    {
        "id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "exam_id": EXAM_ID,
        "category_id": "ky2",
        "section_type": "cloze",
        "title": "Section I: Use of English",
        "sort_order": 1,
        "text": """Given the advantages of electronic money, you might think that we would move quickly to the cashless society in which all payments are made electronically. [1], a true cashless society is probably not around the corner. Indeed, predictions have been [2] for two decades but have not yet come to fruition. For example, Business Week predicted in 1975 that electronic means of payment would soon "revolutionize the very [3] of money itself," only to [4] itself several years later. Why has the movement to a cashless society been so [5] in coming?

Although electronic means of payment may be more efficient than a payments system based on paper, several factors work [6] the disappearance of the paper system. First, it is very [7] to set up the computer, card reader, and telecommunications networks necessary to make electronic money the [8] form of payment. Second, paper checks have the advantage that they [9] receipts, something that many consumers are unwilling to [10]. Third, the use of paper checks gives consumers several days of "float" — it takes several days [11] a check is cashed and funds are [12] from the issuer's account, which means that the writer of the check can earn interest on the funds in the meantime. [13] electronic payments are immediate, they eliminate the float for the consumer.

Fourth, electronic means of payment may [14] security and privacy concerns. We often hear media reports that an unauthorized hacker has been able to access a computer database and to alter information [15] there. The fact that this is not an [16] occurrence means that dishonest persons might be able to access bank accounts in electronic payments systems and [17] from someone else's accounts. The [18] of this type of fraud is no easy task, and a new field of computer science is developing to [19] security issues.

A further concern is that the use of electronic means of payment leaves an electronic [20] that contains a large amount of personal data. There are concerns that government, employers, and marketers might be able to access these data, thereby violating our privacy."""
    },
    # Passage 1: Text 1 (ID: 33384f03-2864-5122-bc64-fb03a46b5193)
    {
        "id": "33384f03-2864-5122-bc64-fb03a46b5193",
        "exam_id": EXAM_ID,
        "category_id": "ky2",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part A - Text 1",
        "sort_order": 2,
        "text": """Davidson relates a joke from cotton country about just how much a modern textile mill has been automated: The average mill has only two employees today, "a man and a dog. The man is there to feed the dog, and the dog is there to keep the man away from the machines."

Davidson's article is one of a number of pieces that have recently appeared making the point that the reason we have such stubbornly high unemployment and declining middle-class incomes today is largely because of the big drop in demand because of the Great Recession, but it is also because of the advances in both globalization and the information technology revolution, which are more rapidly than ever replacing labor with machines or foreign workers.

In the past, workers with average skills, doing an average job, could earn an average lifestyle. But, today, average is officially over. Being average just won't earn you what it used to. It can't when so many more employers have so much more access to so much more above average cheap foreign labor, cheap robotics, cheap software, cheap automation and cheap genius. Therefore, everyone needs to find their extra — their unique value contribution that makes them stand out in whatever is their field of employment.

Yes, new technology has been eating jobs forever, and always will. But there's been an acceleration. As Davidson notes, "In the 10 years ending in 2009, [U.S.] factories shed workers so fast that they erased almost all the gains of the previous 70 years; roughly one out of every three manufacturing jobs — about 6 million in total — disappeared."

There will always be change — new jobs, new products, new services. But the one thing we know for sure is that with each advance in globalization and the I.T. revolution, the best jobs will require workers to have more and better education to make themselves above average.

In a world where average is officially over, there are many things we need to do to support employment, but nothing would be more important than passing some kind of G.I. Bill for the 21st century that ensures that every American has access to post-high school education."""
    },
    # Passage 2: Text 2 (ID: 4f5f933e-cdec-519e-a0eb-fd81bdbbb1bc)
    {
        "id": "4f5f933e-cdec-519e-a0eb-fd81bdbbb1bc",
        "exam_id": EXAM_ID,
        "category_id": "ky2",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part A - Text 2",
        "sort_order": 3,
        "text": """A century ago, the immigrants from across the Atlantic included settlers and sojourners. Along with the many folks looking to make a permanent home in the United States came those who had no intention to stay, and who would make some money and then go home. Between 1908 and 1915, about 7 million people arrived while about 2 million departed. About a quarter of all Italian immigrants, for example, eventually returned to Italy for good. They even had an affectionate nickname, "uccelli di passaggio," birds of passage.

Today, we are much more rigid about immigrants. We divide newcomers into two categories: legal or illegal, good or bad. We hail them as Americans in the making, or brand them as aliens to be kicked out. That framework has contributed to a broken immigration system and the long political paralysis over how to fix it. We don't need more categories, but we need to change the way we think about categories. We need to look beyond strict definitions of legal and illegal. To start, we can recognize the new birds of passage, those living and thriving in the gray areas. We might then begin to solve our immigration challenges.

Crop pickers, violinists, construction workers, entrepreneurs, engineers, home health-care aides and physicists are among today's birds of passage. They are energetic participants in a global economy driven by the flow of work, money and ideas. They prefer to come and go as opportunity calls them. They can manage to have a job in one place and a family in another.

With or without permission, they straddle laws, jurisdictions and identities with ease. We need them to imagine the United States as a place where they can be productive for a while without committing themselves to staying forever. We need them to feel that home can be both here and there and that they can belong to two nations honorably.

Accommodating this new world of people in motion will require new attitudes on both sides of the immigration battle. Looking beyond the culture war logic of right or wrong means opening up the middle ground and understanding that managing immigration today requires multiple paths and multiple outcomes, including the chance to move back and forth. That is what the new birds of passage already do with quiet resourcefulness, even if it is not yet what the law today requires to accomplish legally in the existing system."""
    },
    # Passage 3: Text 3 (ID: eeb57e8b-8d72-5b6f-9ed4-0f411236e54e)
    {
        "id": "eeb57e8b-8d72-5b6f-9ed4-0f411236e54e",
        "exam_id": EXAM_ID,
        "category_id": "ky2",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part A - Text 3",
        "sort_order": 4,
        "text": """Scientists have found that although we are prone to snap overreactions, if we take a moment and think about how we are likely to react, we can reduce or even eliminate the negative effects of our quick, hard-wired responses.

Snap decisions can be important defense mechanisms; if we are judging whether someone is dangerous, our brains and bodies are hard-wired to react very quickly, within milliseconds. But we need more time to assess other factors. To accurately tell whether someone is sociable, studies show, we need at least a minute, preferably five. It takes a while to judge complex aspects of personality, like neuroticism or open-mindedness.

But snap decisions in reaction to rapid stimuli aren't exclusive to the interpersonal realm. Psychologists at the University of Toronto found that viewing a fast-food logo for just a few milliseconds primes us to read 20 percent faster, even though reading has little to do with eating. We unconsciously associate fast food with speed and impatience and carry those impulses into whatever else we're doing. Subjects exposed to fast-food flashes also tend to think a musical piece lasts too long.

Yet we can reverse such influences. If we know we will overreact to consumer products or housing options when we see a happy face (one reason good sales representatives and real estate agents are always smiling), we can take a moment before buying. If we know female job screeners are more likely to reject attractive female applicants, we can help screeners understand their biases — or hire outside screeners.

John Gottman, the marriage expert, explains that we quickly "thin slice" information reliably only after we ground such snap reactions in "thick sliced" long-term study. When Dr. Gottman really wants to assess whether a couple will stay together, he invites them to his island retreat for a much longer evaluation: two days, not two seconds.

Our ability to mute our hard-wired reactions by pausing is what differentiates us from animals: dogs can think about the future only intermittently or for a few minutes. But historically we have spent about 12 percent of our days contemplating the longer term. Although technology might change the way we react, it hasn't changed our nature. We still have the imaginative capacity to rise above temptation and reverse the high-speed trend."""
    },
    # Passage 4: Text 4 (ID: 379cc8f6-b46e-5027-a791-b9c7fe18bc3a)
    {
        "id": "379cc8f6-b46e-5027-a791-b9c7fe18bc3a",
        "exam_id": EXAM_ID,
        "category_id": "ky2",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part A - Text 4",
        "sort_order": 5,
        "text": """Europe is not a gender-equality heaven. In particular, the corporate workplace will never be completely family-friendly until women are part of senior management decisions, and Europe's top corporate-governance positions remain overwhelmingly male. Indeed, women hold only 14 per cent of positions on European corporate boards.

The European Union is now considering legislation to compel corporate boards to maintain a certain proportion of women — up to 60 per cent. This proposed mandate was born of frustration. Last year, European Commission Vice President Viviane Reding issued a call to voluntary action. Reding invited corporations to sign up for gender balance goals of 40 per cent female board membership. But her appeal was considered a failure: only 24 companies took it up.

Do we need quotas to ensure that women can continue to climb the corporate ladder fairly as they balance work and family?

"Personally, I don't like quotas," Reding said recently. "But I like the results." Quotas get action: they "open the way to equality and they break through the glass ceiling," according to Reding, a result seen in France and other countries with legally binding provisions on placing women in top business positions.

I understand Reding's reluctance — and her frustration. I don't like quotas either; they run counter to my belief in meritocracy, governance by the capable. But, when one considers the obstacles to achieving the meritocratic ideal, it does look as if a fairer world must be temporarily ordered.

After all, four decades of evidence has now shown that corporations in Europe as well as the US are evading the meritocratic hiring and promotion of women to top positions — no matter how much "soft pressure" is put upon them. When women do break through to the summit of corporate power — as, for example, Sheryl Sandberg recently did at Facebook — they attract massive attention precisely because they remain the exception to the rule.

If appropriate public policies were in place to help all women whether CEOs or their children's caregivers — and all families, Sandberg would be no more newsworthy than any other highly capable person living in a more just society."""
    },
    # Passage 5: Part B (ID: 41ab5bb2-e0e5-59a0-8a10-90ef85d959e7)
    {
        "id": "41ab5bb2-e0e5-59a0-8a10-90ef85d959e7",
        "exam_id": EXAM_ID,
        "category_id": "ky2",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part B",
        "sort_order": 6,
        "text": """The hugely popular blog the Skint Foodie chronicles how Tony balances his love of good food with living on benefits. After bills, Tony has £60 a week to spend, £40 of which goes on food, but 10 years ago he was earning £130,000 a year working in corporate communications and eating at London's best restaurants at least twice a week. Then his marriage failed, his career burned out and his drinking became serious. "The community mental health team saved my life. And I felt like that again, to a certain degree, when people responded to the blog and gave me the validation and confidence that I'd lost. But it's still a day-by-day thing." Now he's living in a council flat and fielding offers from literary agents. He's feeling positive, but he'll carry on writing the blog, which he describes as "my search for a middle way between returning to my former life and being skint, but not unhappy: a chronicling of what happens when you're in this state, with barely any money to spend on food" — but eating well on a budget. Here's his advice for economical foodies.

[41]
Impulsive spending isn't an option, so plan your week's menu in advance, making shopping lists for your ingredients in their exact quantities. I have an Excel template for a week of breakfast, lunch and dinner. Stop laughing: it's not just cost effective but helps you balance your diet. It's also a good idea to shop daily instead of weekly, because, being human, you'll sometimes change your mind about what you fancy.

[42]
This is where supermarkets and their anonymity come in handy. With them, there's not the same embarrassment as when buying one carrot in a little greengrocer. And if you plan properly, you'll know that you only need, say, 350g of shin of beef and six rashers of bacon, not whatever weight is pre-packed in the supermarket chiller.

[43]
You may proudly claim to only have frozen peas in the freezer — that's not good enough. Mine is filled with leftovers, bread, stock, meat and fish. Planning ahead should eliminate wastage, but if you have keys and bits of herbs and carrots, don't throw them away: everything will be cooked or juiced.

[44]
Everyone says this, but it really is a top tip for frugal eaters. Shop at butchers, delis and fish-sellers regularly, even for small things, and be super friendly. Soon you'll feel comfortable asking if they've any knuckles of ham for soups and stews, or beef bones, chicken carcasses and fish heads for stock which, more often than not, they'll let you have for free.

[45]
You won't be eating out a lot, but save your pennies and once every few months treat yourself to a set lunch at a good restaurant — £1.75 a week for three months gives you £21 — more than enough for a three-course lunch at Michelin-starred Arbutus. It's £16.95 there — or £12.99 for a large pizza from Domino's: I know which I'd rather eat."""
    }
]

print("Passages definition complete.")

QUESTIONS = [
    # Q1
    {
        "sort_order": 1,
        "question_number": 1,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [1] in the passage:",
        "options": {
            "A": "Moreover",
            "B": "However",
            "C": "Therefore",
            "D": "Otherwise"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】空格位于首段第二句句首。首句指出电子货币具有诸多优势，人们本以为会迅速走向无现金社会；第二句则转折指出真正的无现金社会可能并不会很快到来（a true cashless society is probably not around the corner）。\n【命题解密】上下文构成鲜明的逻辑转折对比关系。However（然而，但是）符合语境转折关系。\n【错项排除】[A] Moreover 表示顺承递进；[C] Therefore 表示因果推论；[D] Otherwise 表示否则，均与转折语境不符。"
    },
    # Q2
    {
        "sort_order": 2,
        "question_number": 2,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [2] in the passage:",
        "options": {
            "A": "off",
            "B": "back",
            "C": "over",
            "D": "around"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】空格位于首段第三句：Indeed, predictions have been [2] for two decades but have not yet come to fruition.\n【命题解密】考查副词搭配与语境含义。around 与 be 动词连用构成 be around，意为“存在、流行、在周围”，表示“关于无现金社会的各种预测已经存在了二十年，但至今仍未实现”。\n【错项排除】[A] be off 意为“离开、取消”；[B] be back 意为“返回”；[C] be over 意为“结束”，均无法与 for two decades 连用表示预测流传已久。"
    },
    # Q3
    {
        "sort_order": 3,
        "question_number": 3,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [3] in the passage:",
        "options": {
            "A": "power",
            "B": "concept",
            "C": "history",
            "D": "role"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】空格位于首段第四句：...electronic means of payment would soon 'revolutionize the very [3] of money itself,' only to...\n【命题解密】考查名词辨析。the very concept of money itself 意为“货币本身的概念”。1975年《商业周刊》预测电子支付将彻底颠覆并革新“货币的概念本身”，与常识和文意高度吻合。\n【错项排除】[A] power（力量、权力）；[C] history（历史）；[D] role（角色、作用），均无法与 the very concept of money itself 所表达的根本性定义变革相符。"
    },
    # Q4
    {
        "sort_order": 4,
        "question_number": 4,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [4] in the passage:",
        "options": {
            "A": "reverse",
            "B": "resist",
            "C": "resume",
            "D": "reward"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】空格位于首段第四句末尾：...only to [4] itself several years later.\n【命题解密】only to do 表示令人意外或失望的结果。此处指《商业周刊》在1975年做出激进预测后，仅仅几年后就自己推翻/逆转了自己的预测（reverse itself）。\n【错项排除】[B] resist（抵抗、抵制），感情色彩过强且无法作推翻预测讲；[C] resume（重新开始、恢复）；[D] reward（奖励、奖赏），均脱离语境。"
    },
    # Q5
    {
        "sort_order": 5,
        "question_number": 5,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [5] in the passage:",
        "options": {
            "A": "silent",
            "B": "sudden",
            "C": "slow",
            "D": "steady"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】空格位于首段末句设问：Why has the movement to a cashless society been so [5] in coming?\n【命题解密】呼应前文“走向无现金社会的步伐并没有预期那么快”，be slow in coming 是固定表达，意为“迟迟不来、进展缓慢”。\n【错项排除】[A] silent（无声的、沉默的）；[B] sudden（突然的）；[D] steady（稳定的），与前文呼应“迟缓到来”的核心语义相悖。"
    },
    # Q6
    {
        "sort_order": 6,
        "question_number": 6,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [6] in the passage:",
        "options": {
            "A": "for",
            "B": "against",
            "C": "with",
            "D": "on"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】空格位于第二段首句：Although electronic means of payment may be more efficient... several factors work [6] the disappearance of the paper system.\n【命题解密】work against 意为“阻碍、违背、对……产生不利影响”。文中阐述尽管电子支付效率高，但若干客观因素在阻碍纸币系统的消失。\n【错项排除】[A] work for 表示“为……效力、有利于”；[C] work with 表示“与……合作”；[D] work on 表示“从事于、对……起作用”，均无法体现阻碍消亡的负向对立阻力。"
    },
    # Q7
    {
        "sort_order": 7,
        "question_number": 7,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [7] in the passage:",
        "options": {
            "A": "expensive",
            "B": "imaginative",
            "C": "sensitive",
            "D": "productive"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】空格位于第二段第二句：First, it is very [7] to set up the computer, card reader, and telecommunications networks necessary to...\n【命题解密】此处列举阻碍无现金社会的第一个具体因素：建立遍布全社会的计算机、读卡器和通信网络成本极高、极其昂贵（expensive）。\n【错项排除】[B] imaginative（富有想象力的）；[C] sensitive（敏感的）；[D] productive（多产的、富有成效的），均非阻碍普及的经济成本属性。"
    },
    # Q8
    {
        "sort_order": 8,
        "question_number": 8,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [8] in the passage:",
        "options": {
            "A": "similar",
            "B": "original",
            "C": "temporary",
            "D": "dominant"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】空格位于第二段第二句末尾：...necessary to make electronic money the [8] form of payment.\n【命题解密】考查形容词辨析。dominant form of payment 意为“主导支付形式/主要支付方式”，即取代纸币成为市场主流。\n【错项排除】[A] similar（相似的）；[B] original（最初的、原始的）；[C] temporary（暂时的），均不符合成为主导支付形态的语义。"
    },
    # Q9
    {
        "sort_order": 9,
        "question_number": 9,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [9] in the passage:",
        "options": {
            "A": "collect",
            "B": "copy",
            "C": "provide",
            "D": "print"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】空格位于第二段第三句：Second, paper checks have the advantage that they [9] receipts, something that...\n【命题解密】provide receipts 意为“提供收据/凭证”。纸质支票具备的一个天然优势就是能够为交易双方提供实体凭据。\n【错项排除】[A] collect（收集）；[B] copy（复制）；[D] print（打印，支票本身作为凭证而非机器打印），provide 最为自然准确。"
    },
    # Q10
    {
        "sort_order": 10,
        "question_number": 10,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [10] in the passage:",
        "options": {
            "A": "give up",
            "B": "take over",
            "C": "bring back",
            "D": "pass down"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】空格位于第二段第三句末：...something that many consumers are unwilling to [10].\n【命题解密】give up 意为“放弃”。许多消费者不愿意放弃纸质收据带来的安全感与确定性。\n【错项排除】[B] take over（接管）；[C] bring back（带回、恢复）；[D] pass down（传承、流传），均与上下文不符。"
    },
    # Q11
    {
        "sort_order": 11,
        "question_number": 11,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [11] in the passage:",
        "options": {
            "A": "before",
            "B": "after",
            "C": "since",
            "D": "when"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】空格位于第二段第四句：Third, the use of paper checks gives consumers several days of 'float' — it takes several days [11] a check is cashed...\n【命题解密】it takes some time before... 属于经典时间状语句型，意为“需要花费几天时间……才会发生”。此处指支票开出后需要好几天才能兑现并扣款。\n【错项排除】[B] after（在……之后）；[C] since（自从）；[D] when（当……时），均不能表达“经过若干时间之后才……”的延迟机制。"
    },
    # Q12
    {
        "sort_order": 12,
        "question_number": 12,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [12] in the passage:",
        "options": {
            "A": "kept",
            "B": "borrowed",
            "C": "withdrawn",
            "D": "released"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】空格位于第二段第四句中：...and funds are [12] from the issuer's account...\n【命题解密】withdraw funds from an account 意为“从账户中扣除/提取资金”，是标准的银行金融业务术语。\n【错项排除】[A] kept（保留）；[B] borrowed（借入）；[D] released（释放、发行），均非支票结算扣款的标准动词。"
    },
    # Q13
    {
        "sort_order": 13,
        "question_number": 13,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [13] in the passage:",
        "options": {
            "A": "Unless",
            "B": "Because",
            "C": "Until",
            "D": "Though"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】空格位于第二段末句句首：[13] electronic payments are immediate, they eliminate the float for the consumer.\n【命题解密】前后分句存在明确的因果关系：正因为电子支付是即时完成的（immediate），所以它消除了消费者的资金浮动期（float）。Because 引出原因状语从句。\n【错项排除】[A] Unless（除非）；[C] Until（直到）；[D] Though（尽管），逻辑关系均不符。"
    },
    # Q14
    {
        "sort_order": 14,
        "question_number": 14,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [14] in the passage:",
        "options": {
            "A": "hide",
            "B": "express",
            "C": "ease",
            "D": "raise"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】空格位于第三段首句：Fourth, electronic means of payment may [14] security and privacy concerns.\n【命题解密】raise concerns 意为“引起/引发担忧”，是高频动宾搭配。电子支付方式引发了人们对安全与隐私的严重担忧。\n【错项排除】[A] hide（隐瞒）；[B] express（表达）；[C] ease（缓解、减轻），与下文详述黑客攻击和隐私侵犯的负面事实恰恰相反。"
    },
    # Q15
    {
        "sort_order": 15,
        "question_number": 15,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [15] in the passage:",
        "options": {
            "A": "analyzed",
            "B": "shared",
            "C": "stored",
            "D": "displayed"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】空格位于第三段第二句：...access a computer database and to alter information [15] there.\n【命题解密】information stored there 意为“存储在数据库中的信息”。过去分词短语作后置定语修饰 information。\n【错项排除】[A] analyzed（被分析的）；[B] shared（被分享的）；[D] displayed（被展示的），均不如 stored 符合数据库的核心技术功能。"
    },
    # Q16
    {
        "sort_order": 16,
        "question_number": 16,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [16] in the passage:",
        "options": {
            "A": "unsafe",
            "B": "unnatural",
            "C": "unclear",
            "D": "uncommon"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】空格位于第三段第三句：The fact that this is not an [16] occurrence means that...\n【命题解密】not an uncommon occurrence 双重否定表肯定，意为“屡见不鲜、并非罕见的事情”，呼应前句 often hear media reports。\n【错项排除】[A] unsafe（不安全的）；[B] unnatural（不自然的）；[C] unclear（不清楚的），均不能与 not 搭配表示“频繁发生”。"
    },
    # Q17
    {
        "sort_order": 17,
        "question_number": 17,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [17] in the passage:",
        "options": {
            "A": "steal",
            "B": "choose",
            "C": "benefit",
            "D": "return"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】空格位于第三段第三句后半句：...access bank accounts in electronic payments systems and [17] from someone else's accounts.\n【命题解密】steal from someone else's accounts 意为“从他人的银行账户中盗取资金”，与前面的 dishonest persons 形成动作呼应。\n【错项排除】[B] choose（选择）；[C] benefit（获益）；[D] return（归还），无法准确刻画黑客不法分子的盗窃犯罪行为。"
    },
    # Q18
    {
        "sort_order": 18,
        "question_number": 18,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [18] in the passage:",
        "options": {
            "A": "consideration",
            "B": "prevention",
            "C": "manipulation",
            "D": "justification"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】空格位于第三段第四句首：The [18] of this type of fraud is no easy task, and a new field...\n【命题解密】prevention of this type of fraud 意为“对此类金融欺诈行为的预防与防范”。下文提到发展新计算机科学技术正是为了应对和解决这些安全隐患。\n【错项排除】[A] consideration（考虑）；[C] manipulation（操纵、摆布）；[D] justification（正当理由），均脱离防范金融犯罪的技术主旨。"
    },
    # Q19
    {
        "sort_order": 19,
        "question_number": 19,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [19] in the passage:",
        "options": {
            "A": "call for",
            "B": "fight against",
            "C": "adapt to",
            "D": "cope with"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】空格位于第三段第四句末：...a new field of computer science is developing to [19] security issues.\n【命题解密】cope with security issues 意为“应对、处理安全问题”，是常见动宾搭配。\n【错项排除】[A] call for（呼吁、需要）；[B] fight against（与……战斗，对象通常是人或敌人，非 security issues）；[C] adapt to（适应），均不如 cope with 贴切。"
    },
    # Q20
    {
        "sort_order": 20,
        "question_number": 20,
        "passage_id": "b599cacf-7052-514f-8446-7e74e5f4358d",
        "question_type": "multiple_choice",
        "points": 0.5,
        "stem": "Choose the best option for blank [20] in the passage:",
        "options": {
            "A": "chunk",
            "B": "chip",
            "C": "trail",
            "D": "path"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】空格位于末段首句：A further concern is that the use of electronic means of payment leaves an electronic [20] that contains a large amount of personal data.\n【命题解密】an electronic trail 意为“电子踪迹、数字痕迹”，暗含可被追踪和留存的属性，准确对应其包含大量个人隐私数据这一特征。\n【错项排除】[A] chunk（大块）；[B] chip（芯片）；[D] path（路径、通道），均无法形成“留存电子踪迹引致隐私泄露”的专用隐喻表达。"
    },
    # Q21
    {
        "sort_order": 21,
        "question_number": 21,
        "passage_id": "33384f03-2864-5122-bc64-fb03a46b5193",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "The joke in Paragraph 1 is used to illustrate",
        "options": {
            "A": "the impact of technological advances",
            "B": "the alleviation of job pressure",
            "C": "the shrinkage of textile mills",
            "D": "the decline of middle-class incomes"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】由题干关键词 The joke in Paragraph 1 定位至第一段。首段引述现代纺织厂只有一人一狗的笑话，狗的作用是防止人触碰机器。\n【命题解密】第二段紧接着解释该笑话的含义：技术进步和自动化正在前所未有地用机器取代劳动力（advances in both globalization and the information technology revolution... replacing labor with machines）。因此笑话是为了说明技术进步给劳动力市场带来的深远冲击，A项 the impact of technological advances 正确。\n【错项排除】[B] 工作压力的缓解，与文意相反；[C] 纺织厂的萎缩属于字面表面现象；[D] 中产阶级收入下降是后果之一，而非该笑话直接隐喻的核心。"
    },
    # Q22
    {
        "sort_order": 22,
        "question_number": 22,
        "passage_id": "33384f03-2864-5122-bc64-fb03a46b5193",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "According to Paragraph 3, to be a successful employee, one has to",
        "options": {
            "A": "work on cheap software",
            "B": "ask for a moderate salary",
            "C": "adopt an average lifestyle",
            "D": "contribute something unique"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】由题干定位至第三段末句：Therefore, everyone needs to find their extra — their unique value contribution that makes them stand out in whatever is their field of employment.\n【命题解密】第三段指出“平庸的时代已经结束”，要想脱颖而出，必须找到自己的附加值，即“独特的价值贡献”（their unique value contribution）。D项 contribute something unique 是原文的同义替换。\n【错项排除】[A] 使用廉价软件是雇主的手段而非成功员工的要素；[B] 要求中等薪水与文意相悖；[C] 接受普通生活方式与成为成功员工的目标相反。"
    },
    # Q23
    {
        "sort_order": 23,
        "question_number": 23,
        "passage_id": "33384f03-2864-5122-bc64-fb03a46b5193",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "The quotation in Paragraph 4 explains that",
        "options": {
            "A": "gains of technology have been erased",
            "B": "job opportunities are disappearing at a high speed",
            "C": "factories are making much less money than before",
            "D": "new jobs and services have been offered"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】定位至第四段引语：As Davidson notes, 'In the 10 years ending in 2009, [U.S.] factories shed workers so fast that they erased almost all the gains of the previous 70 years; roughly one out of every three manufacturing jobs... disappeared.'\n【命题解密】该引语用 factories shed workers so fast 和 about 6 million in total disappeared 说明工作机会正在以惊人的速度消失。B项 job opportunities are disappearing at a high speed 为精准概括。\n【错项排除】[A] 技术收益被抹去曲解了原文“前70年就业增长被抹去”；[C] 工厂赚钱减少文中未提；[D] 新工作和服务出现在第五段，非第四段引语内容。"
    },
    # Q24
    {
        "sort_order": 24,
        "question_number": 24,
        "passage_id": "33384f03-2864-5122-bc64-fb03a46b5193",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "According to the author, to reduce unemployment, the most important is",
        "options": {
            "A": "to accelerate the I.T. revolution",
            "B": "to ensure more education for people",
            "C": "to advance economic globalization",
            "D": "to pass more bills in the 21st century"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】定位至末段核心句：...nothing would be more important than passing some kind of G.I. Bill for the 21st century that ensures that every American has access to post-high school education.\n【命题解密】作者明确指出没有什么比确保每个美国人都能获得高中后教育更重要了。B项 to ensure more education for people 是该句的直接同义归纳。\n【错项排除】[A] 加速IT革命和[C] 推进全球化是造成劳动力被取代的客观背景而非解决方案；[D] 在21世纪通过更多法案过度泛化，忽略了“教育法案”的核心限定。"
    },
    # Q25
    {
        "sort_order": 25,
        "question_number": 25,
        "passage_id": "33384f03-2864-5122-bc64-fb03a46b5193",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "Which of the following would be the most appropriate title for the text?",
        "options": {
            "A": "New Law Takes Effect.",
            "B": "Technology Goes Cheap.",
            "C": "Average Is Over.",
            "D": "Recession Is Bad."
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】全文围绕第三段和第六段反复强调的核心命题 Average is officially over（平庸的时代结束了）展开论述。\n【命题解密】作者论述在自动化和全球化背景下，普通技能已无法立足，个人必须具备独特价值，社会必须提供更高水平教育。因此 C项 Average Is Over. 是最具统摄性的最佳标题。\n【错项排除】[A] 新法律生效将建议误作为既成事实；[B] 科技变便宜仅是原因之一；[D] 经济衰退是影响因素之一，均无法涵盖全文主旨。"
    },
    # Q26
    {
        "sort_order": 26,
        "question_number": 26,
        "passage_id": "4f5f933e-cdec-519e-a0eb-fd81bdbbb1bc",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "\"Birds of passage\" refers to those who",
        "options": {
            "A": "stay in a foreign country temporarily",
            "B": "leave their home countries for good",
            "C": "immigrate across the Atlantic",
            "D": "find permanent jobs overseas"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】定位至首段：...those who had no intention to stay, and who would make some money and then go home... They even had an affectionate nickname, 'uccelli di passaggio,' birds of passage.\n【命题解密】首段清晰界定了 birds of passage（候鸟）的定义：那些无意永久居留、赚了钱就返回家乡的暂居劳工。A项 stay in a foreign country temporarily（在外国临时居留）与文意完全契合。\n【错项排除】[B] 永久离开祖国与赚了钱就回国相悖；[C] 跨越大西洋只是百年前移民的地理路径，非群体本质定义；[D] 寻找永久性海外工作与暂留赚钱相反。"
    },
    # Q27
    {
        "sort_order": 27,
        "question_number": 27,
        "passage_id": "4f5f933e-cdec-519e-a0eb-fd81bdbbb1bc",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "It is implied in Paragraph 2 that the current immigration system in the US",
        "options": {
            "A": "needs new immigrant categories",
            "B": "has loosened control over immigrants",
            "C": "should be adapted to meet challenges",
            "D": "has been fixed via political means"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】定位至第二段：That framework has contributed to a broken immigration system and the long political paralysis over how to fix it... We might then begin to solve our immigration challenges.\n【命题解密】作者指出当前将移民简单非黑即白地二元划分导致了移民体系瘫痪破败，呼吁超越合法与非法的刻板定义，通过顺应新流动趋势来化解移民挑战。C项 should be adapted to meet challenges 为合理推断。\n【错项排除】[A] 原文明确说 We don't need more categories；[B] 放宽对移民管控与文首 we are much more rigid 相悖；[D] 已通过政治手段修复与 long political paralysis（长期政治瘫痪）相悖。"
    },
    # Q28
    {
        "sort_order": 28,
        "question_number": 28,
        "passage_id": "4f5f933e-cdec-519e-a0eb-fd81bdbbb1bc",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "According to the author, today's birds of passage want",
        "options": {
            "A": "financial incentives",
            "B": "a global recognition",
            "C": "the freedom to stay and leave",
            "D": "opportunities to get regular jobs"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】定位至第三段末句：They prefer to come and go as opportunity calls them. They can manage to have a job in one place and a family in another.\n【命题解密】come and go as opportunity calls them 表明候鸟型劳工希望根据工作机会随时自由来去，即享有在两国之间居留与离开的自由。C项 the freedom to stay and leave 契合文意。\n【错项排除】[A] 经济激励；[B] 全球认可；[D] 获得固定常规工作的机会，均偏离原文随时来去、兼顾两地家庭与工作的流动诉求。"
    },
    # Q29
    {
        "sort_order": 29,
        "question_number": 29,
        "passage_id": "4f5f933e-cdec-519e-a0eb-fd81bdbbb1bc",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "The author suggests that the birds of passage today should be treated",
        "options": {
            "A": "as faithful partners",
            "B": "with legal tolerance",
            "C": "with economic favors",
            "D": "as mighty rivals"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】定位至第四、五段：With or without permission, they straddle laws... opening up the middle ground and understanding that managing immigration today requires multiple paths and multiple outcomes...\n【命题解密】作者主张不能简单以非法定义惩处他们，应当在法律框架中开辟中间地带，给予其合法的制度包容与多重出入境许可。B项 with legal tolerance（在法律层面予以包容与宽容）是作者的核心建言。\n【错项排除】[A] 当作忠诚伙伴；[C] 给予经济恩惠；[D] 视为强大对手，均非法律制度层面的应对主张。"
    },
    # Q30
    {
        "sort_order": 30,
        "question_number": 30,
        "passage_id": "4f5f933e-cdec-519e-a0eb-fd81bdbbb1bc",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "The most appropriate title for this text would be",
        "options": {
            "A": "Come and Go: Big Mistake",
            "B": "Living and Thriving: Great Risk",
            "C": "With or Without: Great Risk",
            "D": "Legal or Illegal: Big Mistake"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】全文主旨围绕批评现行“非合法即非法”的粗暴移民分类展开。\n【命题解密】作者在第二段和末段重点论述：将所有移民标签化为 legal or illegal 是现行体制的最大弊端，必须摒弃二元对立、认同灰色地带的候鸟人群。因此 D项 Legal or Illegal: Big Mistake 最精准概括了全文批驳核心（文章来源即《华盛顿邮报》评论：We See All Immigrants as Legal or Illegal. Big Mistake）。\n【错项排除】[A] 来来往往是大错特错与作者鼓励候鸟流动背道而驰；[B] 和 [C] 均将焦点误置于风险，脱离了反思制度分类的主题。"
    },
    # Q31
    {
        "sort_order": 31,
        "question_number": 31,
        "passage_id": "eeb57e8b-8d72-5b6f-9ed4-0f411236e54e",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "The time needed in making decisions may",
        "options": {
            "A": "predetermine the accuracy of our judgment",
            "B": "prove the complexity of our brain reaction",
            "C": "depend on the importance of the assessment",
            "D": "vary according to the urgency of the situation"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】定位至第二段：...if we are judging whether someone is dangerous, our brains and bodies are hard-wired to react very quickly, within milliseconds. But we need more time to assess other factors.\n【命题解密】当面临危险时，我们需要在毫秒间迅速决策；而在评估他人复杂性格时，则需要几分钟甚至更久。这说明决策所需的时间因情境的紧急程度而异。D项 vary according to the urgency of the situation 契合文意。\n【错项排除】[A] 预先决定判断的准确性与后文审慎思考能提高准确性矛盾；[B] 证明大脑反应复杂性非文意焦点；[C] 取决于评估的重要性不如依据情境紧迫性准确。"
    },
    # Q32
    {
        "sort_order": 32,
        "question_number": 32,
        "passage_id": "eeb57e8b-8d72-5b6f-9ed4-0f411236e54e",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "Our reaction to a fast-food logo shows that snap decisions",
        "options": {
            "A": "can be associative",
            "B": "are not unconscious",
            "C": "can be dangerous",
            "D": "are not impulsive"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】定位至第三段：Psychologists... found that viewing a fast-food logo... primes us to read 20 percent faster... We unconsciously associate fast food with speed and impatience...\n【命题解密】文中明确指出我们无意识地将快餐与速度和急躁产生联想（associate），并在做其他事情时受到传导。A项 can be associative（具有联想性/关联性）为原文原词同义转述。\n【错项排除】[B] 并非无意识与原文 We unconsciously associate 相悖；[C] 快餐标识让人阅读变快并不能得出具有危险性；[D] 并非冲动与 carry those impulses 矛盾。"
    },
    # Q33
    {
        "sort_order": 33,
        "question_number": 33,
        "passage_id": "eeb57e8b-8d72-5b6f-9ed4-0f411236e54e",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "To reverse the negative influences of snap decisions, we should",
        "options": {
            "A": "trust our first impression",
            "B": "think before we act",
            "C": "do as people usually do",
            "D": "ask for expert advice"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】定位至首段和第四段：...if we take a moment and think about how we are likely to react, we can reduce or even eliminate the negative effects... we can take a moment before buying.\n【命题解密】作者在首段和第四段反复建议：行动或购买前花一点时间冷静思考（take a moment and think）。B项 think before we act（三思而后行）是对这一解决之道的经典提炼。\n【错项排除】[A] 相信第一印象属于盲目跟随快速反应；[C] 照常人行事与抵御本能冲动无关；[D] 寻求专家建议文中未提及。"
    },
    # Q34
    {
        "sort_order": 34,
        "question_number": 34,
        "passage_id": "eeb57e8b-8d72-5b6f-9ed4-0f411236e54e",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "John Gottman says that reliable snap reactions are based on",
        "options": {
            "A": "critical assessment",
            "B": "\"thin sliced\" study",
            "C": "adequate information",
            "D": "sensible explanation"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】定位至第五段首句：John Gottman, the marriage expert, explains that we quickly 'thin slice' information reliably only after we ground such snap reactions in 'thick sliced' long-term study.\n【命题解密】戈特曼指出，只有把快速反应建立在大量长期的研究与充足信息基础之上（thick sliced long-term study），快速决断才是可靠的。C项 adequate information（充足的信息）是对 thick sliced study 的准确诠释。\n【错项排除】[A] 批判性评估；[B] thin sliced study 是戈特曼批评的片面薄层切片，需要 thick sliced 补充；[D] 合理解释脱离文意。"
    },
    # Q35
    {
        "sort_order": 35,
        "question_number": 35,
        "passage_id": "eeb57e8b-8d72-5b6f-9ed4-0f411236e54e",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "The author's attitude toward reversing the high-speed trend is",
        "options": {
            "A": "tolerant",
            "B": "optimistic",
            "C": "uncertain",
            "D": "doubtful"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】定位至末段结尾：We still have the imaginative capacity to rise above temptation and reverse the high-speed trend.\n【命题解密】作者在末段强调人类区别于动物的关键在于暂停本能反应的能力，并充满信心地指出我们依然具备战胜诱惑、扭转快速决策倾向的想象与控制能力。态度是乐观的（optimistic）。\n【错项排除】[A] 容忍的；[C] 不确定的；[D] 怀疑的，均与作者结尾积极坚定的肯定基调不符。"
    },
    # Q36
    {
        "sort_order": 36,
        "question_number": 36,
        "passage_id": "379cc8f6-b46e-5027-a791-b9c7fe18bc3a",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "In the European corporate workplace, generally",
        "options": {
            "A": "women take the lead",
            "B": "men have the final say",
            "C": "corporate governance is overwhelmed",
            "D": "senior management is family-friendly"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】定位至首段：...Europe's top corporate-governance positions remain overwhelmingly male. Indeed, women hold only 14 per cent of positions on European corporate boards.\n【命题解密】首段指出欧洲最高企业治理层依然由男性占据绝对压倒性优势，女性仅占董事会席位的14%，说明男性掌握决定权。B项 men have the final say（男性拥有最终决定权）是 overwhelmingly male 的同义转述。\n【错项排除】[A] 女性占主导与事实完全颠倒；[C] 企业治理不堪重负属于对 overwhelmed 词义的曲解；[D] 高管层对家庭友好与 will never be completely family-friendly 相悖。"
    },
    # Q37
    {
        "sort_order": 37,
        "question_number": 37,
        "passage_id": "379cc8f6-b46e-5027-a791-b9c7fe18bc3a",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "The European Union's intended legislation is",
        "options": {
            "A": "a reflection of gender balance",
            "B": "a response to Reding's call",
            "C": "a reluctant choice",
            "D": "a voluntary action"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】定位至第二段：The European Union is now considering legislation to compel corporate boards... This proposed mandate was born of frustration... only 24 companies took it up.\n【命题解密】第二段表明欧盟起初只是呼吁企业自愿行动，但由于应者寥寥、行动遭遇挫折失败（born of frustration），才不得不考虑立法强制推行配额。C项 a reluctant choice（无奈/勉强的选择）准确概括了这一因自愿行动受挫而被迫采取的强制之举。\n【错项排除】[A] 反映性别平衡颠倒了因果，立法是为了解决缺乏平衡的问题；[B] 欧盟立法是雷丁本人在自愿行动失败后推动的，非仅仅回应其呼吁；[D] 自愿行动是之前的号召，而非当前的强制立法。"
    },
    # Q38
    {
        "sort_order": 38,
        "question_number": 38,
        "passage_id": "379cc8f6-b46e-5027-a791-b9c7fe18bc3a",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "According to Reding, quotas may help women",
        "options": {
            "A": "get top business positions",
            "B": "see through the glass ceiling",
            "C": "balance work and family",
            "D": "anticipate legal results"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】定位至第四段：Quotas get action: they 'open the way to equality and they break through the glass ceiling,' according to Reding, a result seen in France and other countries with legally binding provisions on placing women in top business positions.\n【命题解密】雷丁指出配额能够见效，打破玻璃天花板，帮助女性获得顶层商业管理职位（placing women in top business positions）。A项 get top business positions 正确。\n【错项排除】[B] 看透玻璃天花板曲解了打破（break through）；[C] 平衡工作和家庭并非配额的直接职场功能；[D] 预测法律结果偏离文意。"
    },
    # Q39
    {
        "sort_order": 39,
        "question_number": 39,
        "passage_id": "379cc8f6-b46e-5027-a791-b9c7fe18bc3a",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "The author's attitude toward Reding's appeal is one of",
        "options": {
            "A": "skepticism",
            "B": "objectiveness",
            "C": "indifference",
            "D": "approval"
        },
        "answer": "D",
        "correct_answer": "D",
        "explanation": "【精准定位】定位至第五段：I understand Reding's reluctance — and her frustration... when one considers the obstacles... it does look as if a fairer world must be temporarily ordered.\n【命题解密】作者在第五段阐明虽然自己崇尚精英任用，但面对企业四十年来的回避现实，强制设定配额以实现更公平的世界是必要且暂时的手段。因此对雷丁推动配额的做法持赞同与认可态度（approval）。\n【错项排除】[A] 怀疑；[B] 客观；[C] 漠不关心，均与文中明确的理解与支持立场不符。"
    },
    # Q40
    {
        "sort_order": 40,
        "question_number": 40,
        "passage_id": "379cc8f6-b46e-5027-a791-b9c7fe18bc3a",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "Women entering top management become headlines due to the lack of",
        "options": {
            "A": "more social justice",
            "B": "massive media attention",
            "C": "suitable public policies",
            "D": "greater \"soft pressure\""
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】定位至第六段末句与第七段：...they attract massive attention precisely because they remain the exception to the rule. If appropriate public policies were in place to help all women... Sandberg would be no more newsworthy...\n【命题解密】作者指出女性进入高管成为新闻轰动是因为她们仍然是特例，如果出台了合适的公共政策来帮助所有女性，高管女性就不会再成为轰动新闻。因此成为头条是因为缺乏合适的公共政策保障。C项 suitable public policies（对应 appropriate public policies）正确。\n【错项排除】[A] 社会正义概念过宽；[B] 大众媒体关注是现状本身而非原因；[D] 更大的软性压力与第六段所述软性压力毫无成效相悖。"
    },
    # Q41
    {
        "sort_order": 41,
        "question_number": 41,
        "passage_id": "41ab5bb2-e0e5-59a0-8a10-90ef85d959e7",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "Choose the most suitable subheading from A-G for section [41]:",
        "options": {
            "A": "Shopkeepers are your friends",
            "B": "Remember to treat yourself",
            "C": "Stick to what you need",
            "D": "Live like a peasant",
            "E": "Balance your diet",
            "F": "Planning is everything",
            "G": "Waste not, want not"
        },
        "answer": "F",
        "correct_answer": "F",
        "explanation": "【精准定位】定位至 [41] 段落首句与次句：Impulsive spending isn't an option, so plan your week's menu in advance, making shopping lists for your ingredients in their exact quantities. I have an Excel template for a week...\n【命题解密】该段核心主旨为杜绝冲动消费，提前规划一周菜单，列出所需食材清单，并用 Excel 模板规划三餐。F项 Planning is everything（计划决定一切）完美契合段落主旨。\n【错项排除】[E] Balance your diet 虽在段中出现，但只是提前计划带来的附带益处之一，并非全段主旨；其余选项均与提前做购物计划无直接关联。"
    },
    # Q42
    {
        "sort_order": 42,
        "question_number": 42,
        "passage_id": "41ab5bb2-e0e5-59a0-8a10-90ef85d959e7",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "Choose the most suitable subheading from A-G for section [42]:",
        "options": {
            "A": "Shopkeepers are your friends",
            "B": "Remember to treat yourself",
            "C": "Stick to what you need",
            "D": "Live like a peasant",
            "E": "Balance your diet",
            "F": "Planning is everything",
            "G": "Waste not, want not"
        },
        "answer": "C",
        "correct_answer": "C",
        "explanation": "【精准定位】定位至 [42] 段落：This is where supermarkets and their anonymity come in handy... there's not the same embarrassment as when buying one carrot... you only need, say, 350g of shin of beef and six rashers of bacon, not whatever weight is pre-packed...\n【命题解密】段落指出在超市购物利用其不具名性，可以避免只买一根胡萝卜的尴尬，坚持按自己实际所需的分量购买，不买多余的预包装食品。C项 Stick to what you need（坚持只买所需）为精准概括。\n【错项排除】[A] 段落是在对比超市与小菜店，未提及与店主交朋友；[D] 像农民一样生活未在文中出现；其余选项均无法体现按需购买的核心语义。"
    },
    # Q43
    {
        "sort_order": 43,
        "question_number": 43,
        "passage_id": "41ab5bb2-e0e5-59a0-8a10-90ef85d959e7",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "Choose the most suitable subheading from A-G for section [43]:",
        "options": {
            "A": "Shopkeepers are your friends",
            "B": "Remember to treat yourself",
            "C": "Stick to what you need",
            "D": "Live like a peasant",
            "E": "Balance your diet",
            "F": "Planning is everything",
            "G": "Waste not, want not"
        },
        "answer": "G",
        "correct_answer": "G",
        "explanation": "【精准定位】定位至 [43] 段落：...Mine is filled with leftovers, bread, stock, meat and fish. Planning ahead should eliminate wastage, but if you have keys and bits of herbs and carrots, don't throw them away: everything will be cooked or juiced.\n【命题解密】段落强调冰箱里装满了剩饭菜、面包和高汤，剩菜不要扔掉，都可以拿来做汤或榨汁，核心在于消除浪费（eliminate wastage）。G项 Waste not, want not（不浪费则不匮乏/俭以防匮）是绝佳对应。\n【错项排除】[E] 均衡膳食与剩饭菜利用无关；其余选项均脱离防范食物浪费的主题。"
    },
    # Q44
    {
        "sort_order": 44,
        "question_number": 44,
        "passage_id": "41ab5bb2-e0e5-59a0-8a10-90ef85d959e7",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "Choose the most suitable subheading from A-G for section [44]:",
        "options": {
            "A": "Shopkeepers are your friends",
            "B": "Remember to treat yourself",
            "C": "Stick to what you need",
            "D": "Live like a peasant",
            "E": "Balance your diet",
            "F": "Planning is everything",
            "G": "Waste not, want not"
        },
        "answer": "A",
        "correct_answer": "A",
        "explanation": "【精准定位】定位至 [44] 段落：Shop at butchers, delis and fish-sellers regularly, even for small things, and be super friendly. Soon you'll feel comfortable asking if they've any knuckles of ham for soups... they'll let you have for free.\n【命题解密】段落建议经常去肉铺、熟食店和鱼贩那里购物，保持极为友善的态度，与店主搞好关系可以免费拿到骨头和鱼头熬汤。A项 Shopkeepers are your friends（店主是你的朋友）直接契合与店主建立友谊的主题。\n【错项排除】[C] Stick to what you need 属于上一段；[D] 像农民一样生活脱离文意；其余选项无关联。"
    },
    # Q45
    {
        "sort_order": 45,
        "question_number": 45,
        "passage_id": "41ab5bb2-e0e5-59a0-8a10-90ef85d959e7",
        "question_type": "multiple_choice",
        "points": 2.0,
        "stem": "Choose the most suitable subheading from A-G for section [45]:",
        "options": {
            "A": "Shopkeepers are your friends",
            "B": "Remember to treat yourself",
            "C": "Stick to what you need",
            "D": "Live like a peasant",
            "E": "Balance your diet",
            "F": "Planning is everything",
            "G": "Waste not, want not"
        },
        "answer": "B",
        "correct_answer": "B",
        "explanation": "【精准定位】定位至 [45] 段落：You won't be eating out a lot, but save your pennies and once every few months treat yourself to a set lunch at a good restaurant... Michelin-starred Arbutus... I know which I'd rather eat.\n【命题解密】段落指出平时虽然很少下馆子，但可以把积攒的零钱存起来，每隔几个月犒劳自己去米其林餐厅吃一顿优质平价套餐。B项 Remember to treat yourself（记得犒劳自己）是原文 treat yourself 的原词对应。\n【错项排除】[D] Live like a peasant 与去米其林餐厅享用大餐完全相反；其余选项均无法概括犒劳自己的主旨。"
    }
]

def main():
    json_path = 'public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update Exam Metadata
    data['exam']['title'] = "2013年全国硕士研究生入学统一考试英语（二）真题"
    data['exam']['total_score'] = 60.0

    # 2. Update Passages
    data['passages'] = PASSAGES

    # 3. Update Questions
    data['questions'] = QUESTIONS

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("Successfully built 2013 ky2 Golden Engine to public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json!")

if __name__ == '__main__':
    main()
