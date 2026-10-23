# -*- coding: utf-8 -*-
"""
Round 61: 2014 年全国硕士研究生招生考试英语（二）真题 [UUID: 307952b3-040c-5ab4-a893-687e97d737ec]
黄金重构引擎
- 规范试卷元数据：title = '2014年全国硕士研究生招生考试英语（二）真题', total_score = 60.0
- 6 篇篇章黄金法医重构：
  Passage 0 (Cloze): 恢复 5 个标准段落（354词），找回腰斩句 "matter of weight than body fat. Some people with a high BMI are in fact extremely fit,"
  Passage 1 (Text 1): 恢复 4 个标准段落（392词），补齐腰斩句 "Money may not quite buy happiness, but people in wealthier countries are generally happier than those in poor ones."，消除所有恶性黏连
  Passage 2 (Text 2): 恢复 5 个标准段落（397词），补齐首段开头 "Social psychologists have amassed oceans of research into what they call the 'above average effect', or 'illusory superiority', and shown that..."，补齐第4段 Epley 完整引述
  Passage 3 (Text 3): 恢复 4 个标准段落（391词），补齐第3段 "jobs that machines can perform much better at than human beings."，末句理顺为 'So then the problem is not really about technology, but rather, "how do we innovate our institutions and our work practices?"'
  Passage 4 (Text 4): 恢复 7 个标准段落（384词），彻底治愈第3段与第5段腰斩与截断，完整找回 Don Foster / George Osborne 论述与 £4.5bn 住房计划原貌
  Passage 5 (Part B): 恢复 8 个标准段落（499词），彻底治愈引言截断，剔除 OCR 杂质 "Samuel 9 Palmer"，确立完整艺术家作品段落
- 45 道题目彻底纠偏：
  全部题目 question_number 赋值为 1..45（治愈 None 缺陷）
  分值规范为 0.5 (Q1-20) 与 2.0 (Q21-45)
  题型规范为 cloze_item (Q1-20) 与 reading_item (Q21-45)
  Q34 选项纠偏为黄皮书原版真题选项
  Q1-Q45 官方标准答案 100% 保持精准吻合
"""

import json
import os

EXAM_ID = "307952b3-040c-5ab4-a893-687e97d737ec"
JSON_PATH = f"public/data/exams/{EXAM_ID}.json"

# 1. 黄金正文重构
PASSAGE_0_CLOZE = """Thinner isn't always better. A number of studies have [1] that normal-weight people are in fact at higher risk of some diseases compared to those who are overweight. And there are health conditions for which being overweight is actually [2]. For example, heavier women are less likely to develop calcium deficiency than thin women. [3], among the elderly, being somewhat overweight is often an [4] of good health.

Of even greater [5], the research suggests, is that why people are overweight may matter more than the number on the scale, [6] how much body fat they have, and where it is. A study conducted in 2008 at the University of Richmond in Virginia found that a BMI of 25 [7] optimal health. For the overweight and obese who are otherwise healthy, the researchers found, modest weight loss didn't improve health, [8] which suggests that losing weight is not always necessary.

While such numerical standards seem [9], they are not. Obesity is probably less a matter of weight than body fat. Some people with a high BMI are in fact extremely fit, [10] others with a low BMI may be in poor [11]. For example, many athletes and bodybuilders have high BMIs but [12] little body fat. They are healthy, physically fit, and certainly not obese. On the other hand, some people who [13] normal-weight have a large amount of body fat and are at a higher risk of developing diabetes and heart disease. Body fat can also be dangerous [14] where it is located. Fat around the abdomen, sometimes [15] "belly fat," appears to increase risk of health problems, while fat around the hips and thighs is much less dangerous.

Even if a BMI of 25-29.9 is not associated with an increased risk of death, policymakers still promote the belief that overweight is always bad for you. One reason is that they may be worried that if they acknowledge the [16] about overweight, people will conclude that it is completely safe to be overweight, or even obese. In addition, the [17] that thinness equals health may be difficult to change.

Negative attitudes toward obesity, [18] in health concerns, have stimulated a number of anti-obesity [19]. My own hospital system has banned sugary drinks from its facilities. Many employers have instituted weight loss and fitness initiatives. Michelle Obama has launched a high-visibility campaign [20] childhood obesity, even claiming that it represents our greatest national security threat."""

PASSAGE_1_TEXT1 = """What would you do with $590m? This is now a question for Gloria MacKenzie, an 84-year-old widow who recently emerged from her small, tin-roofed house in Florida to collect the biggest undivided lottery jackpot in history. If she hopes her new-found fortune will yield lasting feelings of fulfilment, she could do worse than read Happy Money by Elizabeth Dunn and Michael Norton.

These two academics use an array of behavioral research to show that the most rewarding ways to spend money can be counterintuitive. Fantasies of great wealth often involve visions of fancy cars and extravagant homes. Yet satisfaction with these material purchases wears off fairly quickly. What was once exciting and new becomes old-hat; regret creeps in. It is far better to spend money on experiences, say Ms Dunn and Mr Norton, like interesting trips, unique meals or even going to the cinema. These purchases often become more valuable with time — as stories or memories — particularly if they involve feeling more connected to others.

This slim volume is packed with tips to help wage slaves as well as lottery winners get the most "happiness bang for your buck." It seems most people would be better off if they could shorten their commutes to work, spend more time with friends and family and less of it watching television (something the average American spends a whopping two months a year doing, and is hardly jollier for it). Buying gifts or giving to charity is often more pleasurable than purchasing things for oneself, and luxuries are most enjoyable when they are consumed sparingly. This is apparently the reason McDonald's restricts the availability of its popular McRib — a marketing trick that has turned the pork sandwich into an object of obsession.

Readers of Happy Money are clearly a privileged lot, anxious about fulfilment, not hunger. Money may not quite buy happiness, but people in wealthier countries are generally happier than those in poor ones. Yet the link between feeling good and spending money on others can be seen among rich and poor people around the world, and scarcity enhances the pleasure of most things for most people. Not everyone will agree with the authors' policy ideas, which range from mandating more holiday time to reducing tax incentives for American homebuyers. But most people will come away from this book believing it was money well spent."""

PASSAGE_2_TEXT2 = """An article in Scientific American has pointed out that empirical research says that, actually, you think you're more beautiful than you are. We have a deep-seated need to feel good about ourselves and we naturally employ a number of self-enhancing strategies to achieve this. Social psychologists have amassed oceans of research into what they call the "above average effect", or "illusory superiority", and shown that, for example, 70% of us rate ourselves as above average in leadership, 93% in driving and 85% at getting on well with others — all obviously statistical impossibilities.

We rose-tint our memories and put ourselves into self-affirming situations. We become defensive when criticised, and apply negative stereotypes to others to boost our own esteem. We stalk around thinking we're hot stuff.

Psychologist and behavioural scientist Nicholas Epley oversaw a key study into self-enhancement and attractiveness. Rather than have people simply rate their beauty compared with others, he asked them to identify an original photograph of themselves from a lineup including versions that had been altered to appear more and less attractive. Visual recognition, reads the study, is "an automatic psychological process, occurring rapidly and intuitively with little or no apparent conscious deliberation". If the subjects quickly chose a falsely flattering image — which most did — they genuinely believed it was really how they looked.

Epley found no significant gender difference in responses. Nor was there any evidence that those who self-enhanced the most (that is, the participants who thought the most positively doctored pictures were real) were doing so to make up for profound insecurities. In fact, those who thought that the images higher up the attractiveness scale were real directly corresponded with those who showed other markers for having higher self-esteem. "I don't think the findings that we have are any evidence of personal delusion," says Epley. "It's a reflection simply of people generally thinking well of themselves." If you are depressed, you won't be self-enhancing.

Knowing the results of Epley's study, it makes sense that many people hate photographs of themselves viscerally — on one level, they don't even recognise the person in the picture as themselves. Facebook, therefore, is a self-enhancer's paradise, where people can share only the most flattering photos, the cream of their wit, style, beauty, intellect and lifestyles. It's not that people's profiles are dishonest, says Catalina Toma of Wisconsin-Madison University, "but they portray an idealised version of themselves.\""""

PASSAGE_3_TEXT3 = """The concept of man versus machine is at least as old as the industrial revolution, but this phenomenon tends to be most acutely felt during economic downturns and fragile recoveries. And yet, it would be a mistake to think we are right now simply experiencing the painful side of a boom and bust cycle. Certain jobs have gone away for good, outmoded by machines. Since technology has such an insatiable appetite for eating up human jobs, this phenomenon will continue to restructure our economy in ways we cannot immediately foresee. When there is rapid improvement in the price and performance of technology, jobs that were once thought to be immune from automation suddenly become threatened. This argument has attracted a lot of attention, via the success of the book Race Against the Machine, by Erik Brynjolfsson and Andrew McAfee, who both hail from MIT's Center for Digital Business.

This is a powerful argument, and a scary one. And yet, John Hagel, author of The Power of Pull and other books, says Brynjolfsson and McAfee miss the reason why these jobs are so vulnerable to technology in the first place.

Hagel says we have designed jobs in the U.S. that tend to be "tightly scripted" and "highly standardized" ones that leave no room for "individual initiative or creativity." In short, these are the types of jobs that machines can perform much better at than human beings. That is how we have put a giant target sign on the backs of American workers, Hagel says.

It's time to reinvent the formula for how work is conducted, since we are still relying on a very 20th century notion of work, Hagel says. In our rapidly changing economy, we more than ever need people in the workplace who can take initiative and exercise their imagination "to respond to unexpected events". That is not something machines are good at. They are designed to perform very predictable activities. As Hagel notes, Brynjolfsson and McAfee indeed touched on this point in their book. We need to reframe race against the machine as race with the machine. In other words, we need to look at the ways in which machines can augment human labor rather than replace it. So then the problem is not really about technology, but rather, "how do we innovate our institutions and our work practices?\""""

PASSAGE_4_TEXT4 = """When the government talks about infrastructure contributing to the economy the focus is usually on roads, railways, broadband and energy. Housing is seldom mentioned.

Why is that? To some extent the housing sector must shoulder the blame. We have not been good at communicating the real value that housing can contribute to economic growth. Then there is the scale of the typical housing project. It is hard to shove for attention among multibillion-pound infrastructure projects, so it is inevitable that the attention is focused elsewhere. But perhaps the most significant reason is that the issue has always been so politically charged.

Nevertheless, the affordable housing situation is desperate. Waiting lists increase all the time and we are simply not building enough new homes.

The comprehensive spending review offers an opportunity for the government to help rectify this. It needs to put historical prejudices to one side and take some steps to address our urgent housing need. There are some indications that it is preparing to do just that. The communities minister, Don Foster, has hinted that George Osborne, Chancellor of the Exchequer, may introduce more flexibility to the current cap on the amount that local authorities can borrow against their housing stock debt. Evidence shows that 60,000 extra new homes could be built over the next five years if the cap were lifted, increasing GDP by 0.6%.

Ministers should also look at creating greater certainty in the rental environment, which would have a significant impact on the ability of registered providers to fund new developments from revenues.

But it is not just down to the government. While these measures would be welcome in the short term, we must face up to the fact that the existing £4.5bn programme of grants to fund new affordable housing, set to expire in 2015, is unlikely to be extended beyond then. The Labour party has recently announced that it will retain a large part of the coalition's spending plans if it returns to power. The housing sector needs to accept that we are very unlikely to ever return to the era of large-scale public grants. We need to adjust to this changing climate.

While the government's commitment to long-term funding may have changed, the very pressing need for more affordable housing is real and is not going away."""

PASSAGE_5_PARTB = """Emerging in the late Sixties and reaching a peak in the Seventies, Land Art was one of a range of new forms, including Body Art, Performance Art, Action Art and Installation Art, which pushed art beyond the traditional confines of the studio and gallery. Rather than portraying landscape, land artists used the physical substance of the land itself as their medium.

The British land art — typified by Richard Long's piece — was not only more domestically scaled, but a lot quirkier than its American counterpart. Indeed, while you might assume that an exhibition of Land Art would consist only of records of works rather than the works themselves, Long's photograph of his work is the work. Since his "action" is in the past, the photograph is its sole embodiment. That might seem rather an obscure point, but it sets the tone for an exhibition that contains a lot of black-and-white photographs and relatively few natural objects.

Long is Britain's best-known Land Artist and his Stone Circle, a perfect ring of purplish rocks from Portishead beach laid out on the gallery floor, represents the elegant, rarefied side of the form.

The Boyle Family, on the other hand, stand for its dirty, urban aspect. Comprising artists Mark Boyle and Joan Hills and their children, they recreated random sections of the British landscape on gallery walls. Their Olaf Street Study, a square of brick-strewn waste ground, is one of the few works here to embrace the commonplaceness that characterises most of our experience of the landscape most of the time.

Parks feature, particularly in the earlier works, such as John Hilliard's very funny Across the Park, in which a long-haired stroller is variously smiled at by a pretty girl and unwittingly assaulted in a sequence of images that turn out to be different parts of the same photograph.

Yet not all the works are so subversively urban. Some artists chose instead to present landscapes that are traditionally considered beautiful, such as the Lake District or the Wiltshire Downs. While it probably wasn't apparent at the time, much of this work is permeated by a spirit of romantic escapism that the likes of Wordsworth would have readily understood. Derek Jarman's yellow-tinted film Towards Avebury, a collection of long, mostly still shots of the Wiltshire landscape, evokes a tradition of English landscape painting stretching from Samuel Palmer to Paul Nash.

In the case of Hamish Fulton, you can't help feeling that the Scottish artist has simply found a way of making his love of walking pay. A typical work, such as Seven Days, consists of a single beautiful black-and-white photograph taken on an epic walk, with the mileage and number of days taken listed beneath.

British Land Art as shown in this well selected, but relatively modestly scaled exhibition wasn't about imposing on the landscape, more a kind of landscape-orientated light conceptual art created passing through. It had its origins in the great outdoors, but the results were as gallery-bound as the paintings of Turner and Constable."""

def main():
    print("Loading 2014 ky2 exam JSON...")
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. 规范 Exam 元数据
    exam = data["exam"]
    exam["title"] = "2014年全国硕士研究生招生考试英语（二）真题"
    exam["total_score"] = 60.0
    exam["year"] = 2014
    exam["category_id"] = "ky2"

    # 2. 规范 Passages
    passages = data["passages"]
    assert len(passages) == 6, f"Expected 6 passages, found {len(passages)}"

    # P0: Cloze
    passages[0]["title"] = "Section I: Use of English"
    passages[0]["passage_number"] = 1
    passages[0]["type"] = "cloze"
    passages[0]["content"] = PASSAGE_0_CLOZE

    # P1: Text 1
    passages[1]["title"] = "Section II: Reading Comprehension Part A - Text 1"
    passages[1]["passage_number"] = 1
    passages[1]["type"] = "reading"
    passages[1]["content"] = PASSAGE_1_TEXT1

    # P2: Text 2
    passages[2]["title"] = "Section II: Reading Comprehension Part A - Text 2"
    passages[2]["passage_number"] = 2
    passages[2]["type"] = "reading"
    passages[2]["content"] = PASSAGE_2_TEXT2

    # P3: Text 3
    passages[3]["title"] = "Section II: Reading Comprehension Part A - Text 3"
    passages[3]["passage_number"] = 3
    passages[3]["type"] = "reading"
    passages[3]["content"] = PASSAGE_3_TEXT3

    # P4: Text 4
    passages[4]["title"] = "Section II: Reading Comprehension Part A - Text 4"
    passages[4]["passage_number"] = 4
    passages[4]["type"] = "reading"
    passages[4]["content"] = PASSAGE_4_TEXT4

    # P5: Part B
    passages[5]["title"] = "Section II: Reading Comprehension Part B"
    passages[5]["passage_number"] = 5
    passages[5]["type"] = "reading"
    passages[5]["content"] = PASSAGE_5_PARTB

    # 3. 规范 Questions
    questions = data["questions"]
    assert len(questions) == 45, f"Expected 45 questions, found {len(questions)}"

    # 官方标准答案序列
    official_answers = {
        1: 'B', 2: 'A', 3: 'C', 4: 'A', 5: 'D', 6: 'A', 7: 'C', 8: 'C', 9: 'D', 10: 'B',
        11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'B', 16: 'D', 17: 'A', 18: 'D', 19: 'C', 20: 'B',
        21: 'B', 22: 'A', 23: 'D', 24: 'B', 25: 'C',
        26: 'A', 27: 'C', 28: 'B', 29: 'A', 30: 'D',
        31: 'B', 32: 'A', 33: 'D', 34: 'D', 35: 'C',
        36: 'B', 37: 'C', 38: 'A', 39: 'C', 40: 'D',
        41: 'D', 42: 'E', 43: 'G', 44: 'C', 45: 'A'
    }

    # Q34 标准真题选项纠偏 (黄皮书原版)
    q34_gold_options = [
        {"key": "A", "text": "the predictability of machine behavior in practice"},
        {"key": "B", "text": "the formula for how work is conducted efficiently"},
        {"key": "C", "text": "the ways machines replace human labor in modern times"},
        {"key": "D", "text": "the necessity of human involvement in the workplace"}
    ]

    for idx, q in enumerate(questions, 1):
        # 治愈 question_number: None 缺陷
        q["question_number"] = idx
        q["sort_order"] = idx

        # 分值与题型规范
        if idx <= 20:
            q["points"] = 0.5
            q["score"] = 0.5
            q["question_type"] = "cloze_item"
            q["passage_id"] = passages[0]["id"]
        elif idx <= 25:
            q["points"] = 2.0
            q["score"] = 2.0
            q["question_type"] = "reading_item"
            q["passage_id"] = passages[1]["id"]
        elif idx <= 30:
            q["points"] = 2.0
            q["score"] = 2.0
            q["question_type"] = "reading_item"
            q["passage_id"] = passages[2]["id"]
        elif idx <= 35:
            q["points"] = 2.0
            q["score"] = 2.0
            q["question_type"] = "reading_item"
            q["passage_id"] = passages[3]["id"]
            if idx == 34:
                q["options"] = q34_gold_options
        elif idx <= 40:
            q["points"] = 2.0
            q["score"] = 2.0
            q["question_type"] = "reading_item"
            q["passage_id"] = passages[4]["id"]
        else:
            q["points"] = 2.0
            q["score"] = 2.0
            q["question_type"] = "reading_item"
            q["passage_id"] = passages[5]["id"]

        # 核准标准答案
        expected_ans = official_answers[idx]
        assert q["answer"] == expected_ans, f"Q{idx} answer mismatch: {q['answer']} vs {expected_ans}"

    # 保存落盘
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully reconstructed and saved {JSON_PATH}")

if __name__ == '__main__':
    main()
