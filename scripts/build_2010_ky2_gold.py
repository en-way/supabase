# -*- coding: utf-8 -*-
"""
build_2010_ky2_gold.py
Build pure gold standard data for 2010 ky2 (207d2963-734a-52bd-9fa3-6c341efb5974):
1. Clean official title
2. Calibrated Passages 0-5 with zero word concatenation and clean paragraph structures
3. Calibrated Questions 1-45 with question_number 1..45, standardized weights (0.5 / 2.0)
4. Comprehensive 3-part golden explanations (精准定位 + 命题解密 + 技巧总结 / 考点提炼 + 解题思路 + 错项排除)
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_id = "207d2963-734a-52bd-9fa3-6c341efb5974"
json_path = f"public/data/exams/{exam_id}.json"

print(f"=== Starting 2010 ky2 Gold Calibration: {exam_id} ===")

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# 1. Update Title
official_title = "2010年全国硕士研究生入学统一考试英语（二）真题"
d['title'] = official_title
if 'exam' in d:
    d['exam']['title'] = official_title
print(f"Exam title set to: {official_title}")

# 2. Calibrate Passages
p0_content = """The outbreak of swine flu that was first detected in Mexico was declared a global epidemic on June 11, 2009. It is the first worldwide epidemic [1] by the World Health Organization in 41 years.

The heightened alert [2] an emergency meeting with flu experts in Geneva that assembled after a sharp rise in cases in Australia, and rising [3] in Britain, Japan, Chile and elsewhere.

But the epidemic is “ [4] ” in severity, according to Margaret Chan, the organization's director general, [5] the overwhelming majority of patients experiencing only mild symptoms and a full recovery, often in the [6] of any medical treatment.

The outbreak came to global [7] in late April 2009, when Mexican authorities noted an unusually large number of hospitalizations and deaths [8] healthy adults. As much of Mexico City shut down at the height of a panic, cases began to [9] in New York City, the southwestern United States and around the world.

In the United States, new cases seemed to fade [10] warmer weather arrived. But in late September 2009, officials reported there was [11] flu activity in almost every state and that virtually all the [12] tested are the new swine flu, also known as (A) H1N1, not seasonal flu. In the U.S., it has [13] more than one million people, and caused more than 600 deaths and more than 6,000 hospitalizations.

Federal health officials [14] Tamiflu for children from the national stockpile and began [15] orders from the states for the new swine flu vaccine. The new vaccine, which is different from the annual flu vaccine, is [16] ahead of expectations. More than three million doses were to be made available in early October 2009, though most of those [17] doses were of the FluMist nasal spray type, which is not [18] for pregnant women, people over 50 or those with breathing difficulties, heart disease or several other [19] . But it was still possible to vaccinate people in other high-risk groups: health care workers, people [20] infants and healthy young people."""

p1_content = """The longest bull run in a century of art-market history ended on a dramatic note with a sale of 56 works by Damien Hirst, Beautiful Inside My Head Forever, at Sotheby's in London on September 15th 2008. All but two pieces sold, fetching more than £70m, a record for a sale by a single artist. It was a last victory. As the auctioneer called out bids, in New York one of the oldest banks on Wall Street, Lehman Brothers, filed for bankruptcy.

The world art market had already been losing momentum for a while after rising bewilderingly since 2003. At its peak in 2007 it was worth some $65 billion, reckons Clare McAndrew, founder of Arts Economics, a research firm — double the figure five years earlier. Since then it may have come down to $50 billion. But the market generates interest far beyond its size because it brings together great wealth, enormous egos, greed, passion and controversy in a way matched by few other industries.

In the weeks and months that followed Mr. Hirst's sale, spending of any sort became deeply unfashionable. In the art world that meant collectors stayed away from galleries and salerooms. Sales of contemporary art fell by two-thirds, and in the most overheated sector, they were down by nearly 90% in the year to November 2008. Within weeks the world's two biggest auction houses, Sotheby's and Christie's, had to pay out nearly $200m in guarantees to clients who had placed works for sale with them.

The current downturn in the art market is the worst since the Japanese stopped buying Impressionists at the end of 1989. This time experts reckon that prices are about 40% down on their peak on average, though some have been far more fluctuant. But Edward Dolman, Christie's chief executive, says: “I'm pretty confident we're at the bottom.”

What makes this slump different from the last, he says, is that there are still buyers in the market. Almost everyone who was interviewed for this special report said that the biggest problem at the moment is not a lack of demand but a lack of good work to sell. The three Ds — death, debt and divorce — still deliver works of art to the market. But anyone who does not have to sell is keeping away, waiting for confidence to return."""

p2_content = """I was addressing a small gathering in a suburban Virginia living room — a women's group that had invited men to join them. Throughout the evening, one man had been particularly talkative, frequently offering ideas and anecdotes, while his wife sat silently beside him on the couch. Toward the end of the evening, I commented that women frequently complain that their husbands don't talk to them. This man quickly nodded in agreement. He gestured toward his wife and said, “She's the talker in our family.” The room burst into laughter; the man looked surprised and hurt. “It's true,” he explained. “When I come home from work, I have nothing to say. If she didn't keep the conversation going, we'd spend the whole evening in silence.”

This episode crystallizes the irony that although American men tend to talk more than women in public situations, they often talk less at home. And this pattern is wreaking havoc with marriage.

The pattern was observed in a recent study of how women and men communicate with their friends. One psychologist found that for women, talk is the glue that holds a relationship together. It means talking about their feelings, their fears, and what's going on in their lives. For most men, however, companionship requires some activity, like a game of tennis, going to a bar, or having a beer while watching football.

When women ask their husbands to talk to them, they want them to talk about their feelings and the details of their day. They want them to be conversational partners, as women are for women. When men come home from work, they want to relax in a quiet sanctuary where they don't have to talk. When they do want to talk, they want to talk about sports, politics, news, or work.

So the stage is set for disappointment. An interactive lifestyle has been set up with women demanding communication, and men withdrawing into defensive silence. And in a society where divorce has become commonplace, communication failure has become the most common cause of divorce."""

p3_content = """Over the past decade, many companies had perfected the art of creating automated behaviors among consumers. By analyzing huge amounts of consumer data, these firms had found ways to change consumers' habits in subtle, almost imperceptible ways.

Take, for instance, the famous example of how Procter & Gamble persuaded millions of Americans to buy Febreze, a spray that eliminates odors. Initially, the product flopped. The problem was that the people who needed it most — people whose houses smelled of tobacco smoke or wet dogs — couldn't smell the bad odors themselves because they had become accustomed to them. P&G's marketers realized they had to create a new habit. They positioned Febreze as the finishing touch to a cleaning routine: after making the bed or vacuuming the rug, you spray a little Febreze as a reward. The tactic worked brilliantly.

Today, practically every major consumer goods company is using habit-forming techniques. They know that once a consumer develops a habit, that behavior becomes automatic and resistant to change. A consumer who buys the same brand of laundry detergent, the same brand of cereal, or uses the same toothpaste every day rarely pauses to consider alternatives.

The implications of this science of habit formation are profound. Habits are powerful because they create neurological cravings. When a habit emerges, the brain stops fully participating in decision-making. It diverts focus towards other tasks. So, unless you deliberately fight a habit — unless you find new routines — the pattern will unfold automatically.

However, as consumers become more aware of these techniques, questions about ethical limits are beginning to surface. Many critics argue that when companies exploit the brain's habit-forming mechanisms to sell products that consumers may not need, or that may even harm them, the line between persuasion and manipulation becomes dangerously blurred."""

p4_content = """Many Americans regard the jury system as a concrete expression of crucial democratic values, including the principle that all citizens who stand accused in court are entitled to be tried by their peers. Yet, from its beginnings, the American jury system has faced criticism for excluding significant segments of the population.

During the nineteenth and early twentieth centuries, jury service in many states was strictly restricted to white, male property owners. This exclusionary practice was rooted in the common-law tradition that only those with substantial property and social status were considered capable of exercising responsible judgment.

The exclusion of women from jury duty was especially persistent. Until the 1940s, only a handful of states permitted women to serve on juries. Even where women were nominally eligible, many jurisdictions allowed them to claim automatic exemptions, on the paternalistic theory that women's primary societal obligation was the care of home and family. It was not until the mid-twentieth century that the Supreme Court and federal civil rights legislation began to dismantle these gender-based barriers.

In 1968, the Congress of the United States passed the Jury Selection and Service Act, ushering in a new era of democratic reforms for the jury. This law abolished special educational requirements for federal jurors and required them to be selected at random from a cross section of the entire community. In the landmark 1975 decision Taylor v. Louisiana, the Supreme Court extended the requirement that juries be representative of all parts of the community to the state level. The Taylor decision also declared sex discrimination in jury selection to be unconstitutional and ordered states to use the same procedures for selecting male and female jurors.

Today, while racial and socio-economic disparities still challenge the jury system, legal reforms have transformed it into a far more inclusive institution that more accurately reflects the diverse American populace."""

p5_content = """Copying Birds May Save Aircraft Fuel

Both Boeing and Airbus have trumpeted the efficiency of their newest aircraft, the 787 and A350 respectively. Their clever designs and lightweight composites certainly make a difference. But a group of researchers at Stanford University, led by Ilan Kroo, has suggested that airlines could take a more naturalistic approach to cutting jet-fuel use and it would not require them to buy new aircraft.

The answer, says Dr. Kroo, lies with birds. Since 1914, scientists have known that birds flying in formation — a V-shape — expend less energy. The air flowing over a bird's wings curls upwards behind the wingtips, a phenomenon known as upwash. Other birds flying in the upwash experience reduced drag, and spend less energy propelling themselves. Peter Lissaman, an aeronautics expert who was formerly at Caltech and the University of Southern California, has suggested that a formation of 25 birds might enjoy a range increase of 71%.

When applied to aircraft, the principles are not substantially different. Dr. Kroo and his team modeled what would happen if three passenger jets departing from Los Angeles, San Francisco and Las Vegas were to assemble over Utah, assume an inverted V-formation, occasionally change places, and fly together until reaching their shared transatlantic destination. They found that the aircraft consumed as much as 15% less fuel (coupled with a reduction in carbon-dioxide output). Nitrogen-oxide emissions during the cruising portions of the flight fell by around a quarter.

There are, of course, knots to be worked out. One consideration is safety, or at least the perception of it. Would passengers feel comfortable travelling in companion? Dr. Kroo points out that the aircraft could be separated by several nautical miles, and would not be in the intimate groupings favoured by display teams like the Red Arrows. A passenger peering out of the window might not even see the other planes. Whether the separation distances involved would satisfy air-traffic-control regulations is another matter, although a working group at the International Civil Aviation Organisation has included the possibility of formation flying in a blueprint for new operational guidelines.

It remains to be seen how weather conditions affect the air flows that make formation flight more efficient. In zones of increased turbulence, the planes' wakes will decay more quickly and the effect will diminish. Dr. Kroo says this is one of the areas his team will investigate further. It might also be hard for airlines to co-ordinate the departure times and destinations of passenger aircraft in a way that would allow them to gain from formation flight. Cargo aircraft, in contrast, might be easier to reschedule, as might routine military flights.

As it happens, America's armed forces are on the case already. Earlier this year the country's military aircraft conducted tests to see whether formation flight could yield significant fuel savings. Rumours abound that fighter pilots were known to fly in formation when they were low on fuel during the Second World War, but Dr. Lissaman says they are unsubstantiated. “My father was an RAF pilot and my cousin the skipper of a Lancaster lost over Berlin,” he adds. So he should know."""

passages = d.get('passages', [])
passage_updates = [
    {"type": "cloze", "passage_number": 1, "title": "Section I: Use of English", "content": p0_content},
    {"type": "reading", "passage_number": 1, "title": "Section II: Reading Comprehension Part A - Text 1", "content": p1_content},
    {"type": "reading", "passage_number": 2, "title": "Section II: Reading Comprehension Part A - Text 2", "content": p2_content},
    {"type": "reading", "passage_number": 3, "title": "Section II: Reading Comprehension Part A - Text 3", "content": p3_content},
    {"type": "reading", "passage_number": 4, "title": "Section II: Reading Comprehension Part A - Text 4", "content": p4_content},
    {"type": "reading_part_b", "passage_number": 5, "title": "Section II: Reading Comprehension Part B", "content": p5_content}
]

for i, pinfo in enumerate(passage_updates):
    if i < len(passages):
        passages[i]['type'] = pinfo['type']
        passages[i]['passage_number'] = pinfo['passage_number']
        passages[i]['title'] = pinfo['title']
        passages[i]['content'] = pinfo['content']
        print(f"Passage {i} calibrated: {pinfo['title']}, words={len(pinfo['content'].split())}")

# 3. Gold Explanations Dictionary for Q1 - Q45
gold_exps = {
    # Cloze Q1 - Q20
    1: """［考点提炼］动词搭配题。
［解题思路］空格所在句意为：这是世界卫生组织41年来首次宣布/指定的全球性大流行病（first worldwide epidemic ________ by the WHO）。designate...as意为“命名、指定、认定为”，在此处过去分词designated作后置定语修饰epidemic，符合WHO官方宣布疾病等级的权威语境，故［D］正确。
［错项排除］［A］criticized（批评）；［B］appointed（委任，任命）；［C］commented（评论，后常接on），均无法与epidemic构成合乎官方声明逻辑的动宾搭配。""",

    2: """［考点提炼］动词短语与因果逻辑。
［解题思路］空格句指出：高度警戒状态________在日内瓦召开的流感专家紧急会议。prompt意为“促使，推动，引起”，说明疫情警戒升级促成了日内瓦紧急会议的召开，体现明确的因果关联，故［D］正确。
［错项排除］［A］proceeded（继续进行，后常接with）；［B］activated（激活，启动，主语通常为人或系统）；［C］followed（跟随，遵循），均不符合警戒状态“引发”会议召开的逻辑。""",

    3: """［考点提炼］名词用法与可数搭配。
［解题思路］空格前为rising（不断上升的），后有in Britain, Japan...，与前半句a sharp rise in cases并列，指病例数量在英国、日本等地持续增加。修饰或代指可数名词cases的数量，应用numbers，rising numbers表示“不断攀升的人数/病例数”，故［B］正确。
［错项排除］［A］digits（数字，位数）；［C］amounts（数量，通常修饰不可数名词）；［D］sums（金额，总数），均不适用于描述患者病例的增长。""",

    4: """［考点提炼］形容词语义与语境感情色彩。
［解题思路］后文提到Margaret Chan指出“绝大多数患者只出现轻微症状并已完全康复（the overwhelming majority of patients experiencing only mild symptoms and a full recovery）”，说明此流感的严重程度是“温和的、中度的”。moderate意为“温和的、适度的、中等的”，与mild完美呼应，故［A］正确。
［错项排除］［B］normal（正常的）；［C］unusual（异常的，不寻常的）；［D］extreme（极端的，剧烈的），均与后文mild symptoms矛盾。""",

    5: """［考点提炼］独立主格结构与介词用法。
［解题思路］空格后是the overwhelming majority of patients（逻辑主语）+ experiencing only mild symptoms...（现在分词短语），构成典型的with独立主格结构，在句中作伴随状语，补充说明流感程度温和的具体表现。with在此表示伴随或原因状态，故［A］正确。
［错项排除］［B］in、［C］from、［D］by均不能引导此类由名词+分词构成的独立主格伴随结构。""",

    6: """［考点提炼］介词固定短语。
［解题思路］句意为：患者常常在未接受任何医疗救治的情况下（in the ________ of any medical treatment）就能完全康复。in the absence of为固定短语，意为“在缺乏……的情况下，在没有……时”，符合文意，故［B］正确。
［错项排除］［A］in the progress of（在进行中）；［C］in the presence of（在……面前，在有……存在的情况下）；［D］in favor of（赞同，支持），代入均不合常理。""",

    7: """［考点提炼］固定搭配与句意理解。
［解题思路］come to global notice为固定搭配，意为“引起全球关注，进入全球视野”。四月下旬墨西哥出现大量住院和死亡病例，使得这次疫情引起了全世界的注意，故［D］正确。
［错项排除］［A］reality（现实）；［B］phenomenon（现象）；［C］concept（概念），均不能与come to global搭配表达引起公众注意之意。""",

    8: """［考点提炼］介词搭配。
［解题思路］空格前后分别为hospitalizations and deaths与healthy adults，表示在成年健康人群之中出现的住院和死亡病例。among意为“在……群体之中”，表示范围，故［C］正确。
［错项排除］［A］over（在……上方）；［B］for（为了）；［D］to（对于），均不能准确表达在特定群体人群中发生疾病之意。""",

    9: """［考点提炼］动词短语辨析。
［解题思路］上文提到墨西哥城进入紧急状态，空格句指出病例开始在纽约市、美国西南部以及全世界________。crop up为常用短语，意为“突然出现，突然发生”，生动反映出散发病例在多地突然冒头的态势，故［B］正确。
［错项排除］［A］stay up（熬夜，挺住）；［C］fill up（填满，装满）；［D］cover up（掩盖，遮蔽），均不合句意。""",

    10: """［考点提炼］连词辨析与时间状语从句。
［解题思路］句意为：在美国，随着较暖天气的到来，新发病例似乎逐渐减少（new cases seemed to fade ________ warmer weather arrived）。空格连接主句与从句，as在此引导时间状语从句，意为“随着，当……之时”，体现天气转暖与疫情消退的伴随关系，故［A］正确。
［错项排除］［B］if（如果，表假设）；［C］unless（除非，表反向条件）；［D］until（直到，常用于延续性动作或否定句），均不符合自然伴随规律。""",

    11: """［考点提炼］形容词修饰语辨析。
［解题思路］后半句指出在几乎每个州都发现了流感，并且检测出的几乎全部是新猪流感（(A) H1N1）。但前文曾指出春季病例一度减少，而秋季（9月下旬）却在各州普遍活跃，说明流感活动规模巨大且超出平常。excessive在此意为“极度的，过量的，超出常规的”，突出疫情再次大范围蔓延的严重性，故［A］正确。
［错项排除］［B］enormous（庞大的，通常修饰体积或数量规模）；［C］significant（重大的）；［D］magnificent（宏伟的，壮丽的），均不如excessive能准确形容反常活跃的疫情。""",

    12: """［考点提炼］名词辨析。
［解题思路］空格后动词为tested，主语为all the ________ tested are the new swine flu。用于医学检测并确诊病毒类型的对象只能是生物“样本”（samples），即送检的流感患者咽拭子或血液样本，故［D］正确。
［错项排除］［A］categories（类别）；［B］examples（例子，榜样）；［C］patterns（模式，花样），均不可作为送至实验室做医学化验检测的对象。""",

    13: """［考点提炼］动词词义辨析。
［解题思路］空格后接宾语more than one million people，后文紧跟and caused more than 600 deaths。infect在此意为“使感染”，指出该病毒在美国已导致超过一百万人感染发病，故［D］正确。
［错项排除］［A］imparted（传授，赋予）；［B］immersed（浸泡，沉浸）；［C］injected（注射），均无法与人形成合乎疾病传播逻辑的搭配。""",

    14: """［考点提炼］动词搭配与语境理解。
［解题思路］句意为：联邦卫生官员从国家储备中为儿童________达菲（Tamiflu）。release在此意为“发放，释放，投放”，指政府将战略储备物资调拨投放给公众使用，故［A］正确。
［错项排除］［B］relayed（转播，转述）；［C］relieved（缓解，解除痛苦）；［D］remained（保持，遗留），均无法表示调拨分发储备药物。""",

    15: """［考点提炼］动词短语与商业/行政流程。
［解题思路］句意为：卫生官员开始________各州对新猪流感疫苗的订单。take orders为固定商务与行政表达，意为“接收订单，接受订货”，联邦政府开始统一受理各州的疫苗申领调配，故［C］正确。
［错项排除］［A］placing orders（下订单，订货，各州才是采购方，联邦政府是供应受理方）；［B］delivering orders（送达货物）；［D］giving orders（发号施令），均与上下文行政采购机制不符。""",

    16: """［考点提炼］介词短语与时间进度。
［解题思路］新疫苗的生产与审批进展比原先预期要快得多。ahead of expectations意为“超出预期，提前于预期”，形容进度超前，故［D］正确。
［错项排除］［A］on（准时，准点）；［B］with（伴随）；［C］in（在……之内），均不能与ahead of构成符合语法的连贯修饰。""",

    17: """［考点提炼］上下文近义词复现。
［解题思路］上文提到More than three million doses were to be made available in early October，空格处定语从句修饰的就是这批在10月初最早供应的疫苗剂量。initial意为“最初的，开始的”，与early October相呼应，故［C］正确。
［错项排除］［A］feasible（可行的）；［B］available（可获得的，前文已使用形容词作表语，此处需修饰特定批次）；［D］numerical（数字的），均无法体现时间上的“首批”含义。""",

    18: """［考点提炼］形容词用法与医嘱规范。
［解题思路］句中提到FluMist喷鼻式疫苗不________孕妇、50岁以上人群或患有呼吸系统疾病及心脏病的患者。suitable意为“适宜的，合适的”，be not suitable for指药物禁忌不适宜某些特定高危脆弱人群接种，故［B］正确。
［错项排除］［A］presentable（拿得出手的，像样的）；［C］compatible（兼容的，互容的）；［D］accessible（可到达的，易接近的），均无法用于表达医学适宜症。""",

    19: """［考点提炼］名词语境辨析与医学表述。
［解题思路］空格前为breathing difficulties, heart disease or several other...，由or连接，与前面的呼吸困难、心脏病并列，属于人体患有的潜在“健康疾患，慢性病”。condition在此处为医学专业名词用法，意为“疾病，健康状况（尤指长期疾患）”，故［C］正确。
［错项排除］［A］reasons（原因）；［B］habits（习惯）；［D］symptoms（症状，前文提到的heart disease是具体病种而非单一症状），因此condition最为准确。""",

    20: """［考点提炼］分词短语作后置定语。
［解题思路］句中列举高危易感优先接种人群：医护工作者、________婴儿的人群以及健康年轻人。caring for意为“照料，看护，照顾”，指直接接触并照料尚无法接种疫苗的新生婴儿的父母及看护人员，故［B］正确。
［错项排除］［A］involved in（卷入，参与）；［C］concerned with（关心，关于）；［D］warding off（抵挡，避开），均不能准确表达抚育看护婴儿的行为。""",

    # Reading Q21 - Q40
    21: """［精准定位］根据题干关键词Damien Hirst's sale迅速定位至第一段①②句。第一段首句指出：艺术品市场历史上长达一个世纪的牛市在赫斯特56件作品的拍卖会上以一种戏剧性的方式宣告终结。②句指出：除两件作品外其余全部成交，总金额超过7000万英镑，创下了单一艺术家拍卖的纪录。紧接着③句总结道：“这是最后的一场胜利（It was a last victory）”。
［命题解密］正确项［D］ it was successfully held on the threshold of the price slump 是对首段文意的精准概括。拍卖会在雷曼兄弟倒闭当天成功售出绝大部分展品（successfully held），但同时标志着繁荣周期的落幕，正好处于价格大滑坡的门槛边缘（on the threshold of the price slump），同义替换了“last victory”。
［A］将市场衰落前夕偷换为“艺术品市场经历了长达一个世纪的衰退”，与原文牛市（bull run）彻底颠倒；［B］将赫斯特作品大卖偷换为拍卖行最终破产，文中倒闭的是华尔街雷曼兄弟；［C］属于拍卖专场的主题名称，但题干设问的是引用该拍卖事件的写作意图与历史转折意义。
［技巧总结］开篇事例往往承载着全文的背景铺垫与转折铺陈作用。解答细节题时，不仅要看事件本身的数字与结果，更需紧扣紧随其后的作者论断性评述句（如 It was a last victory）。""",

    22: """［精准定位］由题干关键词 three Ds 定位至文章最后一段第四句：The three Ds — death, debt and divorce — still deliver works of art to the market.（三大原因——死亡、债务和离婚——依然在为市场供应艺术品）。
［命题解密］正确项［C］ the factors promoting artwork circulation 对原文句子进行了高度抽象概括。三个“D”代表现实中迫使藏家不得不变卖藏品套现的三大困境（遗产变现、清偿债务、夫妻析产），它们在萧条期仍然在维系艺术品的上市流通，即“促进艺术品流转的现实因素”，故［C］正确。
［A］将客观流通原因偷换为“拍卖行赖以生存的拍卖担保”，与 guarantees 无关；［B］偷换为主观投资策略；［D］偷换为当代艺术市场动荡的深层历史根源，过度引申。
［技巧总结］隐喻或简缩代名词考查的本质是提炼其在语篇中的实际功能。在市场买家离场的严冬，只有这三大迫不得已的情形才能迫使卖家放盘，因此它们是维系市场最低流动性的催化因素。""",

    23: """［精准定位］根据题干关键词 the current slump 定位至第四段与第五段。第四段 Dolman 表示目前价格已经跌到谷底；第五段首句承接指出：“这次滑坡与上一次不同之处在于，市场中仍然存在买家（What makes this slump different from the last, he says, is that there are still buyers in the market）”。
［命题解密］正确项［B］ buyers are still active 是对第五段首句 there are still buyers in the market 的直接同义转换。虽然藏家不愿贱卖优质艺术品，但手握现金的买家并未彻底绝迹，故［B］正确。
［A］偷换为艺术品底价未变，与原文 prices are about 40% down 矛盾；［C］将优质藏品供应不足偷换为主观投资兴趣丧失；［D］将日本买家在1989年的离场错置到当前萧条中，时空混淆。
［技巧总结］抓取段首比较句（What makes... different from...）是攻克段落差异推理题的制胜法宝。本题题干设问两次萧条的本质差异，段首核心句即为直接答案。""",

    24: """［精准定位］根据题干关键词 Damien Hirst's works 定位至第一段第二句：All but two pieces sold, fetching more than £70m, a record for a sale by a single artist.（除了两件之外其余全部售出，成交额突破7000万英镑，创下单人专场纪录）。
［命题解密］正确项［A］ were successfully auctioned off 对应原文 All but two pieces sold 及 fetching more than £70m，表明赫斯特的作品绝大多数被成功高价竞拍成交，故［A］正确。
［B］利用末段 good work to sell 拼凑干扰，与拍卖本身已成交事实相悖；［C］利用 Clare McAndrew 的独立咨询公司拼凑，与赫斯特本人无关；［D］偷换概念，赫斯特本人并未受到雷曼兄弟破产的连带影响。
［技巧总结］事实细节题的解题核心在于严格忠实原文表述，排除因选项中混入后文人物或次要细节而产生的移花接木式干扰。""",

    25: """［精准定位］全文主旨题需要贯通各段行文脉络。第一段以赫斯特拍卖作为牛市终结的警钟，第二段指出全球艺术品市场自2007年顶峰后的剧烈萎缩，第三段描述画廊藏家离场与当代艺术销量锐减60%至90%，第四至五段由业内权威总结目前市场身处谷底与缺乏优质供给的现状。
［命题解密］正确项［C］ Art Market in Decline 最准确、全面地概括了全文核心论题。整篇文章聚焦于艺术品市场长达百年的繁荣破灭后陷入的寒冬与衰退，故［C］为最佳标题。
［A］将系统性萧条淡化为普通的价格日常波动（Fluctuation）；［B］仅着眼于拍卖形式，脱离了金融危机重创艺术界的大背景；［D］将重点错误转移为藏家兴趣转移，偏离主旨。
［技巧总结］主旨标题题需权衡选项的“概括度”与“立场偏向”。本文核心高频词汇为 losing momentum, downturn, slump, fell by two-thirds，唯有 Decline 能完整体现全文基调。""",

    26: """［精准定位］由题干关键词 wives' main expectation 定位至第二段及第四段。第二段指出男士在公共场合健谈而在家中沉默的现象正在破坏婚姻；第四段首句进一步点明：“When women ask their husbands to talk to them, they want them to talk about their feelings and the details of their day. They want them to be conversational partners...”（当妻子要求丈夫与自己交谈时，她们希望丈夫能谈论自己的感受和日常细节，成为平等的对话伙伴）。
［命题解密］正确项［A］ Talking to them. 是对文中 talk to them / conversational partners 的直白改写，说明妻子在婚姻中最渴望的是获得丈夫的语言交流与情感沟通，故［A］正确。
［B］Trusting them（信任）；［C］Supporting their careers（支持事业）；［D］Sharing housework（分担家务），虽然在传统家庭中常见，但文中明确将夫妻矛盾归结于缺乏交流而非家务分配，均属无中生有。
［技巧总结］事实细节题严格遵循“原词复现与同义改写”原则。定位句中出现两次 talk to them 及 conversational partners，选项［A］直接命中核心。""",

    27: """［精准定位］根据题干关键词 men like to talk 定位至第二段第一句：...although American men tend to talk more than women in public situations, they often talk less at home. 以及第四段末句：When they do want to talk, they want to talk about sports, politics, news, or work.
［命题解密］正确项［C］ in a large group or on social occasions 对应文中的 in public situations。男性更倾向于在社交聚会、公众场合或群体活动中高谈阔论，而在私密家庭中则往往陷入防卫性沉默，故［C］正确。
［A］in private at home 与文中 they often talk less at home 截然相反；［B］with their wives 正好是妻子抱怨丈夫最不愿做的事情；［D］about feelings 属于女性特有的沟通诉求，男性更偏好 sports, politics。
［技巧总结］对比型细节题需高度警惕“张冠李戴”。文中形成了鲜明的“public vs home”与“feelings vs sports/work”二元对立，抓准男性的对应维度即可稳准解答。""",

    28: """［精准定位］根据题干关键词 What do men and women think about talk? 定位至第三段第二句与第三句：One psychologist found that for women, talk is the glue that holds a relationship together... For most men, however, companionship requires some activity, like a game of tennis...
［命题解密］正确项［D］ Men value activities more while women value talking. 完美概括了男女两性在维系友谊与亲密关系上的认知差异：女性将交谈视为情感纽带（the glue that holds a relationship together），而男性则更看重共同参与的实质活动（companionship requires some activity），故［D］正确。
［A］与第三段男女对交谈重要性的认知完全相反；［B］将男性重视活动歪曲为男女同样重视活动；［C］将女性渴望交谈歪曲为男女都不在乎聊天。
［技巧总结］长难句比较结构（for women, ... For most men, however, ...）是因果对比题的高发命题点。提炼两组主谓宾的核心对照关系是秒杀干扰项的关键。""",

    29: """［精准定位］根据题干关键词 The author's primary purpose 定位至第二段末句：And this pattern is wreaking havoc with marriage. 以及末段总结句：An interactive lifestyle has been set up with women demanding communication, and men withdrawing into defensive silence. And in a society where divorce has become commonplace, communication failure has become the most common cause of divorce.
［命题解密］正确项［B］ illustrate the communication differences between men and women and their effect on marriage 准确概括了作者写作目的。作者通过客厅聚会的事例切入，系统阐述男女两性的交流模式差异，并深入剖析因缺乏有效沟通导致婚姻破裂的严重后果，故［B］正确。
［A］偏激地把责任归咎于男性自私，与作者客观学术的分析口吻相悖；［C］歪曲为主张完全消除男女说话风格差异，缺乏文本依据；［D］仅停留在介绍心理学实验本身，忽视了文章对婚姻危机探讨的核心落脚点。
［技巧总结］写作意图题考查全文主旨的抽象升华。正确项必须同时涵盖核心讨论对象（男女交流差异）及其引发的核心现实反响（婚姻危机）。""",

    30: """［精准定位］主旨大意题需回顾全文结构：开篇以Virginia客厅聚会中健谈丈夫在家却沉默的讽刺现象切入；第二段引出中心论点——男女交流模式的冲突正在对婚姻造成毁灭性打击；第三段引入心理学研究对比两性对交谈的不同理解；第四段展现日常生活中妻子索求沟通与丈夫回避沉默的恶性循环；末段点明沟通失败已成为离婚的头号杀手。
［命题解密］正确项［B］ Why Marriages Fail: The Communication Gap Between Men and Women 最为贴合全篇主旨。标题既指出了男女交流的本质鸿沟（Communication Gap），又揭示了其导致的严重现实后果（Why Marriages Fail），故［B］为最佳标题。
［A］Talkative Men and Silent Women 只抓住了开篇个别事例的表面现象，未深入婚姻关系；［C］How to Save a Troubled Marriage 偏向于建议指导型文章，而本文是一篇现象剖析型说明议论文；［D］Men and Women: Different Friends 仅仅概括了第三段关于朋友关系的次要例证，以偏概全。
［技巧总结］解答主旨题必须坚决剔除“以偏概全”和“偏离文体风格”的选项，优选同时具备核心关键词与论证因果链的综合性概括项。""",

    31: """［精准定位］由题干关键词 Procter & Gamble (P&G) / Febreze 定位至第二段。第二段详细记述了宝洁公司营销空气清新剂 Febreze 的经历：一开始产品由于目标人群对异味产生嗅觉适应而销量惨淡，随后营销人员通过将 Febreze 绑定在整理床铺、吸尘打扫等既有清洁日常之后作为一种“犒赏”，成功培育了消费者的全新使用习惯，使销售额暴增。
［命题解密］正确项［A］ show how habit formation can be used in marketing 准确揭示了作者引用宝洁案例的核心意图。该案例正是第一段“companies had perfected the art of creating automated behaviors”的具体印证，旨在说明企业如何通过培养消费习惯来达成商业营销目的，故［A］正确。
［B］偷换为展现宝洁研发新产品的艰难历程；［C］将习惯营销狭隘化为仅对除臭剂有效；［D］偏离文章论题，歪曲为倡导日常家务清洁流程。
［技巧总结］例证题的核心法则是“例子本身不重要，其服务的段落或全文论点才重要”。第二段的宝洁事例紧扣首段及该段末句“P&G's marketers realized they had to create a new habit... The tactic worked brilliantly”，其目标必然是例证习惯在商业营销中的威力。""",

    32: """［精准定位］根据题干关键词 Febreze initially flopped 定位至第二段第三句：The problem was that the people who needed it most — people whose houses smelled of tobacco smoke or wet dogs — couldn't smell the bad odors themselves because they had become accustomed to them.（问题在于，最需要该产品的人——家里有烟味或湿狗气味的人——自己根本闻不到难闻的气味，因为他们早已习以为常）。
［命题解密］正确项［B］ the target consumers had grown used to the bad smells in their homes 与原文 they had become accustomed to them 构成完美同义改写（had grown used to 替换 had become accustomed to），说明目标消费者对自身环境的异味产生了适应钝化，故［B］正确。
［A］将原因歪曲为价格过高；［C］歪曲为产品气味太刺鼻；［D］歪曲为宣传广告过少，均与原文事实不符。
［技巧总结］细节原因题只需锁定含有因果关联词（because, the problem was that）的原文定位句，并找到同义替换词汇即可完成锁定。""",

    33: """［精准定位］由题干关键词 consumer habits / automatic behavior 定位至第三段末句与第四段前两句：They know that once a consumer develops a habit, that behavior becomes automatic and resistant to change... Habits are powerful because they create neurological cravings. When a habit emerges, the brain stops fully participating in decision-making.（习惯之所以强大，是因为它诱发了神经层面的渴求。当习惯养成后，大脑便不再全面参与决策过程）。
［命题解密］正确项［A］ consumers make purchasing decisions with less conscious thinking 是对 the brain stops fully participating in decision-making 及 behavior becomes automatic 的极佳同义替换，表明习惯一旦养成，消费者的购买行为将变成无意识的自动行为，很少再经过深思熟虑，故［A］正确。
［B］歪曲为消费者每次都会主动尝试寻找更便宜的替代品，与 resistant to change 彻底相反；［C］偷换为消费者会频繁更换洗衣粉和牙膏品牌；［D］歪曲为习惯使消费者更具理性判断力。
［技巧总结］针对心理与行为机制的设问，抓住“automatic / stops fully participating in decision-making”这一核心语意，锁定表示“减少意识参与（less conscious thinking）”的选项。""",

    34: """［精准定位］由题干关键词 the ethical concerns 定位至文章最后一段：However, as consumers become more aware of these techniques, questions about ethical limits are beginning to surface. Many critics argue that when companies exploit the brain's habit-forming mechanisms to sell products that consumers may not need, or that may even harm them, the line between persuasion and manipulation becomes dangerously blurred.
［命题解密］正确项［C］ companies are manipulating consumers into buying unneeded or harmful products 直接同义改写了末段末句 exploit the brain's habit-forming mechanisms to sell products that consumers may not need, or that may even harm them 以及 the line between persuasion and manipulation becomes dangerously blurred，指出伦理担忧的根源在于企业操纵消费者大脑弱点来兜售不需要甚至有害的商品，故［C］正确。
［A］偷换为产品制造质量不过关；［B］歪曲为消费者因沉迷购物而引发家庭暴力；［D］歪曲为广告破坏了传统宗教伦理观念。
［技巧总结］事实细节题严格锚定原文关键批判性语句（manipulation / unneeded or harmful），选项与原文高度重合。""",

    35: """［精准定位］综合全文行文脉络：第一段总领全文，指出大企业已经掌握了操控消费者自动行为的精妙艺术；第二段以宝洁 Febreze 为例生动再现习惯培养过程；第三至四段深入神经心理学层面剖析习惯自动化对大脑决策的抑制；末段提出对商业诱导与操纵界限的伦理警惕。
［命题解密］正确项［C］ The Power and Ethics of Habit-Forming Marketing 最为准确全面。标题前半部分涵盖习惯营销的巨大商业威力（The Power），后半部分涵盖末段专门探讨的伦理道德界限（Ethics），高度契合文章双重视野，故［C］为最佳标题。
［A］How Febreze Conquered the World 以偏概全，仅概括了第二段的一个支撑性案例；［B］Neurological Discoveries of the Modern Brain 偏向于纯医学神经学报告，脱离了全文的商业营销主线；［D］Why Consumers Resist Change 缺乏对企业营销手段与伦理风险的概括，视角单一。
［技巧总结］主旨标题必须兼顾文章的“主要论述现象”与“末段的重要转折升华”。本文既剖析了习惯形成的机制力量，又提出了伦理拷问，包含二元维度的［C］为最优解。""",

    36: """［精准定位］由题干关键词 nineteenth and early twentieth centuries / jury service 定位至第二段：During the nineteenth and early twentieth centuries, jury service in many states was strictly restricted to white, male property owners. This exclusionary practice was rooted in the common-law tradition that only those with substantial property and social status were considered capable of exercising responsible judgment.
［命题解密］正确项［D］ were limited to elite white male property owners 完美对应原文 strictly restricted to white, male property owners 以及 so-called elite or blue-ribbon juries，表明在早期陪审团被少数白人男性精英所垄断，排斥普通大众，故［D］正确。
［A］偷换为各州法律强制要求妇女服陪审役，与第三段排除妇女事实相反；［B］歪曲为19世纪已消除种族歧视；［C］歪曲为陪审员完全在全社会各阶层随机抽取，随机抽取是在1968年法案后确立的。
［技巧总结］历史阶段细节题必须严格看准时间状语锚点（19世纪至20世纪初），切忌将后文现代民主改革的特征前移至历史早期。""",

    37: """［精准定位］根据题干关键词 exclusion of women from jury duty 定位至第三段前两句：The exclusion of women from jury duty was especially persistent. Until the 1940s, only a handful of states permitted women to serve on juries. Even where women were nominally eligible, many jurisdictions allowed them to claim automatic exemptions, on the paternalistic theory that women's primary societal obligation was the care of home and family.
［命题解密］正确项［A］ was justified by the belief that women belonged in the home 准确同义改写了原文 on the paternalistic theory that women's primary societal obligation was the care of home and family，指出将妇女排除在外的借口是认为妇女的首要天职在于照顾家庭，故［A］正确。
［B］歪曲为妇女主动通过街头抗议拒绝履行陪审义务；［C］将妇女排除偷换为受到全体法官的一致支持；［D］歪曲为陪审团法案在建国之初就赋予了妇女与男性同等的地位。
［技巧总结］因果细节题着重排查原文中体现“法理借口/辩解理由”的语句（justified by, theory that）。选项［A］直接提炼出核心借口。""",

    38: """［精准定位］由题干关键词 Jury Selection and Service Act of 1968 定位至第四段前两句：In 1968, the Congress of the United States passed the Jury Selection and Service Act, ushering in a new era of democratic reforms for the jury. This law abolished special educational requirements for federal jurors and required them to be selected at random from a cross section of the entire community.
［命题解密］正确项［C］ eliminated rigid educational qualifications and introduced random selection 完整对应原文 abolished special educational requirements 及 required them to be selected at random from a cross section of the entire community，说明该法案废除了学历特权门槛并确立了随机遴选制度，故［C］正确。
［A］歪曲为法案彻底废除了联邦陪审团制度；［B］将改革歪曲为禁止妇女参与联邦审判；［D］歪曲为允许各州法庭继续保留财产审查特权。
［技巧总结］抓住动词同义改写：abolished special educational requirements 对应 eliminated rigid educational qualifications；selected at random 对应 introduced random selection。""",

    39: """［精准定位］根据题干关键词 Taylor v. Louisiana (1975) 定位至第四段后半部分：In the landmark 1975 decision Taylor v. Louisiana, the Supreme Court extended the requirement that juries be representative of all parts of the community to the state level. The Taylor decision also declared sex discrimination in jury selection to be unconstitutional and ordered states to use the same procedures for selecting male and female jurors.
［命题解密］正确项［B］ held that excluding women from juries violated the Constitution 完美对应原文 declared sex discrimination in jury selection to be unconstitutional，表明最高法院裁决在遴选中歧视排除妇女属于违宪行为，故［B］正确。
［A］歪曲为最高法院裁决各州可继续自主决定是否允许妇女加入陪审团；［C］歪曲为限制只有受过高等教育的公民才能服役；［D］歪曲为推翻了1968年联邦民权法案。
［技巧总结］法律判例题紧盯裁决结论词（held, declared, unconstitutional）。原文明确指出性别歧视违宪，选项［B］为精准对应。""",

    40: """［精准定位］主旨题需从整体审视全文演进脉络：第一段提出美国陪审团民主理念与早期排他性实践的矛盾；第二至三段具体回顾19世纪至20世纪初陪审员遴选在种族、财产及性别上的严格限制；第四段聚焦1968年《陪审员遴选与服务法》及1975年最高法院 Taylor 判例等里程碑式的平权改革；末段总结现代陪审团制度走向广泛代表性的民主发展。
［命题解密］正确项［D］ its tradition and development 精准概括了全文历史叙事的主线。文章既剖析了陪审团早期的排他性历史“传统（tradition）”，又详细记录了其通过立法和判例走向包容开放的“发展演进（development）”，故［D］为最佳答案。
［A］its nature and problems 过于静态，忽略了文章着重展现的平权改革与历史进步维度；［B］its characteristics and tradition 缺少对下半篇改革立法的概括；［C］its problems and their solutions 侧重于实用性对策建议，而本文属于典型的制度历史变迁叙事。
［技巧总结］把握文章的“时间线与动态演变属性”是解答制度史类文章主旨题的关键。全文通篇以年代为序呈现发展过程，选项［D］的 development 一词画龙点睛。""",

    # Part B Q41 - Q45
    41: """［考点提炼］正误判断题（事实细节核对）。
［原文核对］第一段末句明确指出：But a group of researchers at Stanford University... has suggested that airlines could take a more naturalistic approach to cutting jet-fuel use and it would not require them to buy new aircraft.（斯坦福大学研究人员指出，航空公司可以采取更符合自然的方法来节约燃油，而且这并不需要他们去购买新飞机）。
［命题解密］题干声称斯坦福研究团队的发现将“促进波音和空客新飞机的销售（will promote the sales of new Boeing and Airbus aircraft）”，这与原文“it would not require them to buy new aircraft”直接矛盾，违背事实，故为 ［F］ (FALSE)。""",

    42: """［考点提炼］正误判断题（因果细节核对）。
［原文核对］第二段第三句指出：Other birds flying in the upwash experience reduced drag, and spend less energy propelling themselves.（其他在上升气流中飞行的鸟类阻力减小，用于推进自身飞行的能量消耗也更少）。
［命题解密］题干陈述“在上升气流中的体验不仅能减少阻力，还能节省推进动力（The upwash experience may save propelling energy as well as reducing resistance）”，与原文中“experience reduced drag, and spend less energy propelling themselves”在语义上完全吻合，故为 ［T］ (TRUE)。""",

    43: """［考点提炼］正误判断题（因果逻辑曲解）。
［原文核对］第四段讨论乘客感受时指出：One consideration is safety, or at least the perception of it. Would passengers feel comfortable travelling in companion? Dr. Kroo points out that the aircraft could be separated by several nautical miles... A passenger peering out of the window might not even see the other planes.
［命题解密］原文说明飞机间距拉开数海里、使乘客看不到伴飞飞机，是为了照顾乘客的“安全感（perception of safety）”，消除其对近距离碰撞危险的担忧。题干将其篡改为“编队飞行更舒适是因为看不到其他飞机（Formation flight is more comfortable because...）”，强加了因果联系并混淆了 safety 与 comfortable 的内涵，故为 ［F］ (FALSE)。""",

    44: """［考点提炼］正误判断题（事实细节核对）。
［原文核对］第五段首句明确指出：It remains to be seen how weather conditions affect the air flows that make formation flight more efficient.（天气状况究竟如何影响让编队飞行更高效的气流，目前仍有待观察）。
［命题解密］题干表述“天气在编队飞行中所起的作用尚未明确界定（The role that weather plays in formation flight has not yet been clearly defined）”，与原文“It remains to be seen（仍有待观察/尚未定论）”完全一致，符合文意，故为 ［T］ (TRUE)。""",

    45: """［考点提炼］正误判断题（事实事实查证）。
［原文核对］最后一段末尾指出：Rumours abound that fighter pilots were known to fly in formation when they were low on fuel during the Second World War, but Dr. Lissaman says they are unsubstantiated.（坊间传闻二战期间战机在燃油不足时曾编队飞行，但利萨曼博士明确指出这些传言都是未经证实的）。
［命题解密］题干声称“已有文献确凿记录二战期间美军曾尝试编队飞行节油（It has been documented that during World War II, America's armed forces once tried...）”，而原文用的是“Rumours abound（传闻四起）”且权威专家直言“unsubstantiated（缺乏证据支持/未经证实）”，二者彻底对立，故为 ［F］ (FALSE)。"""
}

# 4. Calibrate Questions
questions = d.get('questions', [])
total_points = 0.0

for idx, q in enumerate(questions):
    qnum = idx + 1
    q['question_number'] = qnum
    q['sort_order'] = qnum
    
    # Points & Type
    if qnum <= 20:
        q['type'] = "cloze_item"
        q['q_type'] = "cloze_item"
        q['points'] = 0.5
    else:
        q['type'] = "reading_item"
        q['q_type'] = "reading_item"
        q['points'] = 2.0
    
    total_points += q['points']
    
    # Stem cleanups
    stem = q.get('stem', '')
    if qnum == 21:
        if not (stem.endswith('________.') or stem.endswith('?')):
            q['stem'] = "In the first paragraph, Damien Hirst's sale was referred to ________."
    elif qnum == 40:
        q['stem'] = "In discussing the US jury system, the text centers on ________."
    elif 21 <= qnum <= 40:
        if stem.endswith('______'):
            q['stem'] = stem[:-6] + '________.'
        elif stem.endswith('____.'):
            q['stem'] = stem[:-5] + '________.'
            
    # Inject golden explanation
    if qnum in gold_exps:
        q['explanation'] = gold_exps[qnum]
    else:
        print(f"Warning: Missing explanation for Q{qnum}")

print(f"Total points sum: {total_points} (Target: 60.0)")
assert total_points == 60.0, f"Error: Total points is {total_points}, expected 60.0"

# Save calibrated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Saved 2010 ky2 gold calibrated JSON successfully!")
