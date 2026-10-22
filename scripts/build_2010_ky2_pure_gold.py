# -*- coding: utf-8 -*-
"""
build_2010_ky2_pure_gold.py
Construct 100% Golden Standard Data for 2010 KY2 Exam (UUID: 207d2963-734a-52bd-9fa3-6c341efb5974):
- Title: 2010年全国硕士研究生入学统一考试英语（二）真题
- Passages 0-5: Pure paragraphs, zero concatenation, authentic full-length texts
- Questions 1-45:
  * Q1-Q20: Cloze (0.5 pts each, Total 10.0 pts)
  * Q21-Q40: Reading Part A (2.0 pts each, Total 40.0 pts)
  * Q41-Q45: Reading Part B True/False (2.0 pts each, Total 10.0 pts)
- Full Parity with Master Exam Bank & Supabase Production Schema
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_id = "207d2963-734a-52bd-9fa3-6c341efb5974"
json_path = f"public/data/exams/{exam_id}.json"

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

# 1. Title
official_title = "2010年全国硕士研究生入学统一考试英语（二）真题"
d['title'] = official_title
if 'exam' in d:
    d['exam']['title'] = official_title

# 2. Passages
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

p2_content = """I was addressing a small gathering in a suburban Virginia living room — a women's group that had invited men to join them. Throughout the evening, one man had been particularly talkative, frequently offering ideas and anecdotes, while his wife sat silently beside him on the couch. Toward the end of the evening, I commented that women frequently complain that their husbands don't talk to them. This man quickly nodded in agreement. He gestured toward his wife and said, “She's the talker in our family.” The room burst into laughter; the man looked surprised and hurt. “It's true,” he explained. “When I come home from work I have nothing to say. If she didn't keep the conversation going, we'd spend the whole evening in silence.”

This episode crystallizes the irony that although American men tend to talk more than women in public situations, they often talk less at home. And this pattern is wreaking havoc with marriage.

The pattern was observed by political scientist Andrew Hacker in the late 1970s. Sociologist Catherine Kohler Riessman reports in her new book Divorce Talk that most of the women she interviewed — but only a few of the men — gave lack of communication as the reason for their divorces. Given the current divorce rate of nearly 50 percent, that amounts to millions of cases in the United States every year — a virtual epidemic of failed conversation.

In my own research, complaints from women about their husbands most often focused not on tangible inequities such as having badges of power or doing far more than their share of daily life-support work like cleaning, cooking and social arrangements. Instead, they focused on communication: “He doesn't listen to me.” “He doesn't talk to me.” I found, as Hacker observed years before, that most wives want their husbands to be, first and foremost, conversational partners, but few husbands share this expectation of their wives.

In short, the image that best represents the current crisis is the stereotypical cartoon scene of a man sitting at the breakfast table with a newspaper held up in front of his face, while a woman glares at the back of it, wanting to talk."""

p3_content = """Over the past decade, many companies had perfected the art of creating automatic behaviors — habits — among consumers. These habits have helped companies earn billions of dollars when customers eat snacks or wipe counters almost without thinking, often in response to a carefully designed set of daily cues.

“There are fundamental public health problems, like dirty hands instead of a soap habit, that remain killers only because we can't figure out how to change people's habits,” said Dr. Curtis, the director of the Hygiene Center at the London School of Hygiene & Tropical Medicine. “We wanted to learn from industry how to create new behaviors that happen automatically.”

The companies that Dr. Curtis turned to — Procter & Gamble, Colgate-Palmolive and Unilever — had invested hundreds of millions of dollars finding the subtle cues in consumers' lives that corporations could use to introduce new routines.

If you look hard enough, you'll find that many of the products we use every day — chewing gums, skin moisturizers, disinfecting wipes, air fresheners, water purifiers, health snacks, teeth whiteners, fabric softeners, vitamins — are results of manufactured habits. A century ago, few people regularly brushed their teeth multiple times a day. Today, because of shrewd advertising and public health campaigns, many Americans habitually give their pearly whites a cavity-preventing scrub twice a day, often with Colgate, Crest or one of the other brands.

A few decades ago, many people didn't drink water outside of a tap. Then beverage companies started bottling water from far-off springs, and now office workers unthinkingly sip bottled water all day long. Chewing gum, once bought primarily by adolescent boys, is now featured in commercials as a breath freshener and teeth cleanser for use after a meal. Skin moisturizers are advertised as part of morning beauty rituals, slipped in between hair brushing and putting on makeup.

“Our products succeed when they become part of daily or weekly patterns,” said Carol Berning, a consumer psychologist who recently retired from Procter & Gamble, the company that sold $76 billion of Tide, Crest and other products last year. “Creating positive habits is a huge part of improving our consumers' lives, and it's essential to making new products commercially viable.”

Through experiments and observation, social scientists like Dr. Berning have learned that there is power in tying certain behaviors to habitual cues through ruthless advertising. As this new science of habit has emerged, controversies have erupted when the tactics have been used to sell questionable beauty creams or unhealthy foods."""

p4_content = """Many Americans regard the jury system as a concrete expression of crucial democratic values, including the principles that all citizens who meet minimal qualifications of age and literacy are equally competent to serve on juries; that jurors should be selected randomly from a representative cross section of the community; that no citizen should be denied the right to serve on a jury on account of race, religion, sex, or national origin; that defendants are entitled to trial by their peers; and that verdicts should represent the conscience of the community and not just the letter of the law. The jury is also said to be the best surviving example of direct rather than representative democracy. In a direct democracy, citizens take turns governing themselves, rather than electing representatives to govern for them.

But as recently as in 1968, jury selection procedures conflicted with these democratic ideals. In some states, for example, jury duty was limited to persons of supposedly superior intelligence, education, and moral character. Although the Supreme Court of the United States had prohibited intentional racial discrimination in jury selection as early as the 1880 case of Strauder v. West Virginia, the practice of selecting so-called elite or blue-ribbon juries provided a convenient way around this and other antidiscrimination laws.

The system also failed to regularly include women on juries until the mid-20th century. Although women first served on state juries in Utah in 1898, it was not until the 1940s that a majority of states made women eligible for jury duty. Even then several states automatically exempted women from jury duty unless they personally asked to have their names included on the jury list. This practice was justified by the claim that women were needed at home, and it kept juries unrepresentative of women through the 1960s.

In 1968, the Congress of the United States passed the Jury Selection and Service Act, ushering in a new era of democratic reforms for the jury. This law abolished special educational requirements for federal jurors and required them to be selected at random from a cross section of the entire community. In the landmark 1975 decision Taylor v. Louisiana, the Supreme Court extended the requirement that juries be representative of all parts of the community to the state level. The Taylor decision also declared sex discrimination in jury selection to be unconstitutional and ordered states to use the same procedures for selecting male and female jurors."""

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
        print(f"Passage {i} updated: {pinfo['title']}, words={len(pinfo['content'].split())}")

# 3. Gold Questions Data (Stems, Options, Answers, Scores, Explanations)
# Standard Answers:
# 1-5: D, C, B, A, A
# 6-10: B, D, C, B, A
# 11-15: C, D, D, A, C
# 16-20: B, D, C, A, B
# 21-25: D, A, B, C, C
# 26-30: A, C, B, D, C
# 31-35: A, A, D, C, B
# 36-40: D, A, C, B, D
# 41-45: F, T, F, T, F

gold_q_data = {
    # Cloze Q1 - Q20
    1: {
        "stem": "It is the first worldwide epidemic [1] by the World Health Organization in 41 years.",
        "options": [{"key": "A", "value": "criticized"}, {"key": "B", "value": "appointed"}, {"key": "C", "value": "commented"}, {"key": "D", "value": "designated"}],
        "correct_answer": "D",
        "score": 0.5,
        "explanation": """［考点提炼］动词搭配题。
［解题思路］空格所在句意为：这是世界卫生组织41年来首次宣布/指定的全球性大流行病（first worldwide epidemic ________ by the WHO）。designate...as意为“命名、指定、认定为”，在此处过去分词designated作后置定语修饰epidemic，符合WHO官方宣布疾病等级的权威语境，故［D］正确。
［错项排除］［A］criticized（批评）；［B］appointed（委任，任命）；［C］commented（评论，后常接on），均无法与epidemic构成合乎官方声明逻辑的动宾搭配。"""
    },
    2: {
        "stem": "The heightened alert [2] an emergency meeting with flu experts in Geneva...",
        "options": [{"key": "A", "value": "proceeded"}, {"key": "B", "value": "activated"}, {"key": "C", "value": "followed"}, {"key": "D", "value": "prompted"}],
        "correct_answer": "C",
        "score": 0.5,
        "explanation": """［考点提炼］动词语义与时间逻辑。
［解题思路］空格句主语为The heightened alert（警戒级别的提升），宾语为an emergency meeting（紧急会议）。后文that assembled after a sharp rise...说明专家们在病例激增后先于日内瓦召开会议，随后世卫组织据此正式拉响了全球警戒警报。follow表示“在……之后发生/跟进”，即警报的升级是在日内瓦紧急会议召开之后紧接着做出的决定，符合事实时间先后链条，故［C］正确。
［错项排除］［A］proceeded（进行，不及物动词后需接with）；［B］activated（激活，通常以人为主语启动设备或系统）；［D］prompted（促使，主客体时间颠倒，警报是会议的结果而非起因）。"""
    },
    3: {
        "stem": "...and rising [3] in Britain, Japan, Chile and elsewhere.",
        "options": [{"key": "A", "value": "digits"}, {"key": "B", "value": "numbers"}, {"key": "C", "value": "amounts"}, {"key": "D", "value": "sums"}],
        "correct_answer": "B",
        "score": 0.5,
        "explanation": """［考点提炼］名词用法与可数搭配。
［解题思路］空格前为rising（不断上升的），后有in Britain, Japan...，与前半句a sharp rise in cases并列，指患病人数或病例数在多国持续攀升。修饰或代指可数人群、病例的数量，应用numbers，rising numbers表示“不断增加的病例数/发病人数”，故［B］正确。
［错项排除］［A］digits（数字，位数）；［C］amounts（数量，通常修饰不可数名词）；［D］sums（金额，总数），均不适用于描述患者病例的增长。"""
    },
    4: {
        "stem": "But the epidemic is “ [4] ” in severity, according to Margaret Chan...",
        "options": [{"key": "A", "value": "moderate"}, {"key": "B", "value": "normal"}, {"key": "C", "value": "unusual"}, {"key": "D", "value": "extreme"}],
        "correct_answer": "A",
        "score": 0.5,
        "explanation": """［考点提炼］形容词语义与语境感情色彩。
［解题思路］下文陈冯富珍总干事进一步解释道：“绝大多数患者只出现轻微症状并已完全康复（the overwhelming majority of patients experiencing only mild symptoms and a full recovery）”，说明此流感的严重程度并不剧烈，属于中等温和程度。moderate意为“温和的、适度的、中等的”，与后文mild完美呼应，故［A］正确。
［错项排除］［B］normal（正常的，流行病暴发不能称为normal）；［C］unusual（异常的）；［D］extreme（极端的，剧烈的），均与后文mild symptoms矛盾。"""
    },
    5: {
        "stem": "...[5] the overwhelming majority of patients experiencing only mild symptoms...",
        "options": [{"key": "A", "value": "with"}, {"key": "B", "value": "in"}, {"key": "C", "value": "from"}, {"key": "D", "value": "by"}],
        "correct_answer": "A",
        "score": 0.5,
        "explanation": """［考点提炼］独立主格结构与介词用法。
［解题思路］空格后紧跟the overwhelming majority of patients（逻辑主语）+ experiencing only mild symptoms...（现在分词短语），构成典型的with复合独立主格结构，在句中作伴随状语，补充说明疫情程度温和的具体临床特征。with在此表示伴随或解释状态，故［A］正确。
［错项排除］［B］in、［C］from、［D］by均无法引导由“名词+分词短语”构成的独立伴随状语结构。"""
    },
    6: {
        "stem": "...often in the [6] of any medical treatment.",
        "options": [{"key": "A", "value": "progress"}, {"key": "B", "value": "absence"}, {"key": "C", "value": "presence"}, {"key": "D", "value": "favor"}],
        "correct_answer": "B",
        "score": 0.5,
        "explanation": """［考点提炼］介词固定短语。
［解题思路］句意为：绝大多数患者在未接受任何医疗救治的情况下（in the ________ of any medical treatment）就能自行完全康复。in the absence of为英语经典固定短语，意为“在缺乏……的情况下，在没有……时”，生动印证了前文所述轻症患者无需就医即可痊愈的事实，故［B］正确。
［错项排除］［A］in the progress of（在……的进程中）；［C］in the presence of（在……面前，在有……存在时）；［D］in favor of（赞同，支持），代入后语义完全反常。"""
    },
    7: {
        "stem": "The outbreak came to global [7] in late April 2009...",
        "options": [{"key": "A", "value": "reality"}, {"key": "B", "value": "phenomenon"}, {"key": "C", "value": "concept"}, {"key": "D", "value": "notice"}],
        "correct_answer": "D",
        "score": 0.5,
        "explanation": """［考点提炼］固定搭配与语境理解。
［解题思路］come to global notice为固定搭配，意为“引起全球关注，进入全球视野”。4月下旬墨西哥出现大量住院和死亡病例，使此次疫情首次引起了全世界的广泛关注，故［D］正确。
［错项排除］［A］reality（现实）；［B］phenomenon（现象）；［C］concept（概念），均无法与come to global搭配表达引起公众注意之意。"""
    },
    8: {
        "stem": "...hospitalizations and deaths [8] healthy adults.",
        "options": [{"key": "A", "value": "over"}, {"key": "B", "value": "for"}, {"key": "C", "value": "among"}, {"key": "D", "value": "to"}],
        "correct_answer": "C",
        "score": 0.5,
        "explanation": """［考点提炼］介词搭配。
［解题思路］空格前后分别为hospitalizations and deaths与healthy adults，表示在成年健康人群之中出现的住院和死亡病例。among意为“在……群体之中”，表示特定范围，故［C］正确。
［错项排除］［A］over（在……上方）；［B］for（为了）；［D］to（对于），均不能准确表达在特定人群范围中发生疾病之意。"""
    },
    9: {
        "stem": "...cases began to [9] in New York City, the southwestern United States and around the world.",
        "options": [{"key": "A", "value": "stay up"}, {"key": "B", "value": "crop up"}, {"key": "C", "value": "fill up"}, {"key": "D", "value": "cover up"}],
        "correct_answer": "B",
        "score": 0.5,
        "explanation": """［考点提炼］动词短语辨析。
［解题思路］上文提到墨西哥城陷入恐慌关闭公共场所，空格句指出新病例开始在纽约市、美国西南部以及全世界多地________。crop up为常用短语，意为“突然出现，突然冒出”，形象地描述了散发病例在多地相继冒头的态势，故［B］正确。
［错项排除］［A］stay up（熬夜，挺立）；［C］fill up（填满，装满）；［D］cover up（掩盖，遮蔽），均不合句意。"""
    },
    10: {
        "stem": "In the United States, new cases seemed to fade [10] warmer weather arrived.",
        "options": [{"key": "A", "value": "as"}, {"key": "B", "value": "if"}, {"key": "C", "value": "unless"}, {"key": "D", "value": "until"}],
        "correct_answer": "A",
        "score": 0.5,
        "explanation": """［考点提炼］连词辨析与时间状语从句。
［解题思路］句意为：在美国，随着较暖天气的到来，新发病例似乎逐渐减少（new cases seemed to fade ________ warmer weather arrived）。空格连接主句与从句，as在此引导时间状语从句，意为“随着，当……之时”，体现出天气变暖与流感减少之间的伴随发展关系，故［A］正确。
［错项排除］［B］if（如果，表假设）；［C］unless（除非，表反向条件）；［D］until（直到……为止），均无法表达自然的伴随过程。"""
    },
    11: {
        "stem": "...officials reported there was [11] flu activity in almost every state...",
        "options": [{"key": "A", "value": "excessive"}, {"key": "B", "value": "enormous"}, {"key": "C", "value": "significant"}, {"key": "D", "value": "magnificent"}],
        "correct_answer": "C",
        "score": 0.5,
        "explanation": """［考点提炼］形容词修饰语与疾控公文规范。
［解题思路］后半句指出在几乎每个州都发现了流感，并且检测出的几乎全部是新猪流感（(A) H1N1）。CDC公共卫生报告中形容流感传播的专业标准表述为significant flu activity，意为“显著的、大范围活跃的流感活动”，准确客观地传达了疫情反弹的态势，故［C］正确。
［错项排除］［A］excessive（过度的，含有贬义主观情绪）；［B］enormous（庞大的，通常修饰体积尺寸）；［D］magnificent（宏伟的，华丽的），均不符合疾病监控的严谨科学公文语境。"""
    },
    12: {
        "stem": "...virtually all the [12] tested are the new swine flu...",
        "options": [{"key": "A", "value": "categories"}, {"key": "B", "value": "examples"}, {"key": "C", "value": "patterns"}, {"key": "D", "value": "samples"}],
        "correct_answer": "D",
        "score": 0.5,
        "explanation": """［考点提炼］名词词义辨析与医学化验语境。
［解题思路］空格后动词为tested（送检，检测），主语为all the ________ tested are the new swine flu。送往实验室进行病毒核酸或血清检测的对象只能是医学“样本”（samples），即咽拭子或血清标本，故［D］正确。
［错项排除］［A］categories（类别）；［B］examples（例子，榜样）；［C］patterns（模式，样式），均不可作为送进实验室做化学/生物检测的对象。"""
    },
    13: {
        "stem": "In the U.S., it has [13] more than one million people...",
        "options": [{"key": "A", "value": "imparted"}, {"key": "B", "value": "immersed"}, {"key": "C", "value": "injected"}, {"key": "D", "value": "infected"}],
        "correct_answer": "D",
        "score": 0.5,
        "explanation": """［考点提炼］动词词义辨析。
［解题思路］空格后接宾语more than one million people，后文紧跟and caused more than 600 deaths。infect在此意为“使感染”，指该病毒在美国已导致超过一百万人感染发病，故［D］正确。
［错项排除］［A］imparted（传授，赋予）；［B］immersed（浸泡，沉浸）；［C］injected（注射），均无法与人群形成合乎病毒传染逻辑的动宾搭配。"""
    },
    14: {
        "stem": "Federal health officials [14] Tamiflu for children from the national stockpile...",
        "options": [{"key": "A", "value": "released"}, {"key": "B", "value": "relayed"}, {"key": "C", "value": "relieved"}, {"key": "D", "value": "remained"}],
        "correct_answer": "A",
        "score": 0.5,
        "explanation": """［考点提炼］动词搭配与行政调配流程。
［解题思路］句意为：联邦卫生官员从国家应急储备中为儿童________达菲（Tamiflu）。release在此处意为“投放，调拨，发放”，指政府将战略储备物资紧急调配并投向市场或医疗机构供公众使用，故［A］正确。
［错项排除］［B］relayed（转播，转述）；［C］relieved（缓解，减轻）；［D］remained（保持，逗留），均无法表示调拨国家储备药品。"""
    },
    15: {
        "stem": "...and began [15] orders from the states for the new swine flu vaccine.",
        "options": [{"key": "A", "value": "placing"}, {"key": "B", "value": "delivering"}, {"key": "C", "value": "taking"}, {"key": "D", "value": "giving"}],
        "correct_answer": "C",
        "score": 0.5,
        "explanation": """［考点提炼］动词短语与商业/申领流程。
［解题思路］句意为：联邦官员开始________各州关于新猪流感疫苗的订单/申领要求。take orders在此为固定商业行政表达，意为“接受订单，受理订货”，各州是订购申领方，联邦卫生机构是受理调拨方，故［C］正确。
［错项排除］［A］placing orders（下单采购，属于各州的行为而非联邦官员的动作）；［B］delivering orders（递送货物）；［D］giving orders（发号施令），均不符合统筹调配订单的流程。"""
    },
    16: {
        "stem": "The new vaccine, which is different from the annual flu vaccine, is [16] ahead of expectations.",
        "options": [{"key": "A", "value": "feasible"}, {"key": "B", "value": "available"}, {"key": "C", "value": "reliable"}, {"key": "D", "value": "applicable"}],
        "correct_answer": "B",
        "score": 0.5,
        "explanation": """［考点提炼］形容词语义辨析。
［解题思路］后句紧承指出More than three million doses were to be made available in early October...，说明新疫苗供应上市的时间表比预想的要快。is available ahead of expectations表示新疫苗的供应“比预期更早可供使用/面市”，与后文made available形成直接词汇呼应，故［B］正确。
［错项排除］［A］feasible（可行的）；［C］reliable（可靠的）；［D］applicable（适用的），均无法与ahead of expectations呼应体现提前投放市场供人接种的状态。"""
    },
    17: {
        "stem": "...though most of those [17] doses were of the FluMist nasal spray type...",
        "options": [{"key": "A", "value": "prevalent"}, {"key": "B", "value": "principal"}, {"key": "C", "value": "innovative"}, {"key": "D", "value": "initial"}],
        "correct_answer": "D",
        "score": 0.5,
        "explanation": """［考点提炼］上下文近义词复现与时间修饰。
［解题思路］上文提到More than three million doses were to be made available in early October，空格处定语从句修饰的正是在10月初最早供应投放的这批剂量。initial意为“最初的，首批的”，those initial doses指“最初投放的那批疫苗”，精准呼应early October，故［D］正确。
［错项排除］［A］prevalent（普遍流行的）；［B］principal（主要的）；［C］innovative（创新的），均无法在时间维度上指代最早投放的一期疫苗。"""
    },
    18: {
        "stem": "...which is not [18] for pregnant women, people over 50...",
        "options": [{"key": "A", "value": "presented"}, {"key": "B", "value": "restricted"}, {"key": "C", "value": "recommended"}, {"key": "D", "value": "introduced"}],
        "correct_answer": "C",
        "score": 0.5,
        "explanation": """［考点提炼］动词用法与医疗接种指南。
［解题思路］文中指出FluMist鼻喷减毒活疫苗不________孕妇、50岁以上老人或患有呼吸道和心脏疾病的患者。be recommended for为疫苗接种指南中的标准禁忌表达，not recommended for表示“不推荐给……人群接种”，符合医学用语，故［C］正确。
［错项排除］［A］presented（展示，提出）；［B］restricted（受限制的，若用restricted则搭配to或介词短语不同）；［D］introduced（介绍，引进），均不符合医嘱指南规范。"""
    },
    19: {
        "stem": "...heart disease or several other [19] .",
        "options": [{"key": "A", "value": "problems"}, {"key": "B", "value": "issues"}, {"key": "C", "value": "agonies"}, {"key": "D", "value": "sufferings"}],
        "correct_answer": "A",
        "score": 0.5,
        "explanation": """［考点提炼］名词语境辨析与医学健康搭配。
［解题思路］空格前为breathing difficulties, heart disease or several other...，由or连接，与前面的呼吸困难、心脏病并列，属于人体患有的潜在健康疾患。health problems为极高频的地道搭配，problems代指各种慢性身体健康疾患，故［A］正确。
［错项排除］［B］issues（社会议题、争论焦点）；［C］agonies（极度痛苦）；［D］sufferings（受难，折磨），均无法与具体的生理疾病（heart disease）并列。"""
    },
    20: {
        "stem": "...health care workers, people [20] infants and healthy young people.",
        "options": [{"key": "A", "value": "involved in"}, {"key": "B", "value": "caring for"}, {"key": "C", "value": "concerned with"}, {"key": "D", "value": "warding off"}],
        "correct_answer": "B",
        "score": 0.5,
        "explanation": """［考点提炼］现在分词短语作后置定语。
［解题思路］句中列举流感易感与优先接种保护人群：医护工作者、________婴儿的人群以及健康年轻人。care for意为“照料，照顾”，指直接看护和抚育尚不能接种疫苗的婴幼儿的家长和保育人员，接种可防止将病毒传染给婴儿，故［B］正确。
［错项排除］［A］involved in（卷入，参与）；［C］concerned with（关心，关于）；［D］warding off（避开，挡开），均无法准确表达抚育看护婴儿的行为。"""
    },

    # Reading Q21 - Q25 (Text 1)
    21: {
        "stem": "In the first paragraph, Damien Hirst's sale was referred to as “a last victory” because",
        "options": [
            {"key": "A", "value": "the art market had witnessed a succession of victories"},
            {"key": "B", "value": "the auctioneer finally got the two pieces at the highest bids"},
            {"key": "C", "value": "Beautiful Inside My Head Forever won over all masterpieces"},
            {"key": "D", "value": "it was successfully made just before the world financial crisis"}
        ],
        "correct_answer": "D",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词Damien Hirst's sale及a last victory迅速定位至第一段。首句指出：艺术品市场历史上长达一个世纪的牛市在达米恩·赫斯特作品专场拍卖会上以一种戏剧性的方式落幕。②句指出：除两件作品外全部成交，创下单人专场纪录。紧接着③④句点明：“这是最后的一场胜利。当拍卖师叫价之时，华尔街最古老的投行之一雷曼兄弟在纽约申请破产（As the auctioneer called out bids, in New York one of the oldest banks on Wall Street, Lehman Brothers, filed for bankruptcy）”。
［命题解密］正确项［D］ it was successfully made just before the world financial crisis 是对原文事实的精准提纯。赫斯特的拍卖专场在金融风暴（雷曼兄弟破产）全面席卷全球的转折关头抢先完成了巨额套现（successfully made just before），因而成为百年大牛市终结前的“最后一次胜利”，故［D］正确。
［错项排除］［A］将大萧条前的个案偷换为“艺术品市场见证了一连串的胜利”，与牛市终结相悖；［B］将两件未成交的流拍作品颠倒为“拍卖师最终以最高价买下该两件作品”；［C］属于拍卖主题的字面拼凑，偷换为战胜了所有名家杰作，偏离主旨。
［技巧总结］解答观点例证题时，不仅要看事件本身的成交数字，更需紧盯作者在紧邻句中给出的时代背景参照物（Lehman Brothers filed for bankruptcy）。抓住标志性历史事件是锁定正确同义转述的关键。"""
    },
    22: {
        "stem": "By saying “spending of any sort became deeply unfashionable” (Line 1-2, Para. 3), the author suggests that",
        "options": [
            {"key": "A", "value": "collectors were no longer actively involved in art-market auctions"},
            {"key": "B", "value": "people stopped every kind of spending and stayed away from galleries"},
            {"key": "C", "value": "art collection as a fashion had lost its appeal to a great extent"},
            {"key": "D", "value": "works of art in general had gone out of fashion so they were not worth buying"}
        ],
        "correct_answer": "A",
        "score": 2.0,
        "explanation": """［精准定位］根据题干引语定位至第三段第一、二句：In the weeks and months that followed Mr. Hirst's sale, spending of any sort became deeply unfashionable. In the art world that meant collectors stayed away from galleries and salerooms.（在赫斯特拍卖会后的数周和数月里，任何形式的消费都变得极不合时宜。在艺术界，这意味着藏家们远离了画廊和拍卖大厅）。
［命题解密］正确项［A］ collectors were no longer actively involved in art-market auctions 直接同义改写了第二句对引语的具象阐释（collectors stayed away from galleries and salerooms），表明收藏家不再积极参与艺术品拍卖市场，故［A］正确。
［错项排除］［B］对原文any sort进行了绝对化、字面化的误读，偷换为全社会所有人停止了所有开销；［C］将经济寒冬导致的购买行为收缩偷换为“艺术品收藏作为一种时尚彻底失去了吸引力”；［D］偷换为艺术品本身过时导致不值一文。
［技巧总结］代词及引语推断题遵循“就近释义”原则。破折号或紧随其后的解释性句式（In the art world that meant...）往往直接提供标准答案的同义对应。"""
    },
    23: {
        "stem": "Which of the following statements is NOT true?",
        "options": [
            {"key": "A", "value": "Sales of contemporary art fell dramatically from 2007 to 2008."},
            {"key": "B", "value": "The art market surpassed many other industries in momentum."},
            {"key": "C", "value": "The art market generally went downward in various ways."},
            {"key": "D", "value": "Some art dealers were awaiting better chances to come."}
        ],
        "correct_answer": "B",
        "score": 2.0,
        "explanation": """［精准定位］逆向是非判断题需全面扫描各选项与原文的对应细节。
［命题解密］正确项［B］ The art market surpassed many other industries in momentum 与原文第二段末句截然相悖。第二段末句原文为：...because it brings together great wealth, enormous egos, greed, passion and controversy in a way matched by few other industries.（它汇聚了巨大的财富、膨胀的自我、贪婪、激情与争议，很少有其他行业能在这几点上与之比拟）。原文比拼的是“汇聚财富、贪婪与争议的程度”，而非选项所说的“市场发展动量（momentum）超越了许多其他行业”，属于典型的张冠李戴，故［B］为符合题干设问的反向真实项。
［错项排除］［A］对应第三段Sales of contemporary art fell by two-thirds... down by nearly 90%，属于原文真实表述；［C］对应全文关于艺术品价格下跌40%、画廊交易冰封的总体描述，符合事实；［D］对应末段末句waiting for confidence to return，符合事实。
［技巧总结］排查NOT true题时，务必警惕“高频热词错配”。原文虽然在前文提到过 momentum，但在末句进行跨行业对比时指的却是 great wealth, egos, greed and controversy，偷梁换柱是命题专家设置干扰的典型手法。"""
    },
    24: {
        "stem": "The three Ds mentioned in the last paragraph are",
        "options": [
            {"key": "A", "value": "auction houses' favorites"},
            {"key": "B", "value": "contemporary trends"},
            {"key": "C", "value": "factors promoting artwork circulation"},
            {"key": "D", "value": "styles representing Impressionists"}
        ],
        "correct_answer": "C",
        "score": 2.0,
        "explanation": """［精准定位］由题干关键词The three Ds定位至最后一段第四句：The three Ds — death, debt and divorce — still deliver works of art to the market.（三大原因——死亡、债务和离婚——依然在为市场供应艺术品）。
［命题解密］正确项［C］ factors promoting artwork circulation 是对原文deliver works of art to the market的高度抽象概括。在买家和藏家均持币观望的萧条严冬，唯有遗产变现、清偿债务和夫妻分产这三大现实困境能够迫使持有者出让藏品，从而维持了艺术品在市场上的最低限度流转，故［C］正确。
［错项排除］［A］偷换为拍卖行最喜欢的偏好；［B］偷换为当代的普遍社会潮流；［D］将现实生活危机移花接木为代表印象派的艺术风格。
［技巧总结］代词与暗喻考查的是考生在语境中的提纯能力。抓取谓语动词 deliver works of art to the market，直接与 circulation（流通）形成同义映射。"""
    },
    25: {
        "stem": "The most appropriate title for this text could be",
        "options": [
            {"key": "A", "value": "Fluctuation of Art Prices"},
            {"key": "B", "value": "Up-to-date Art Auctions"},
            {"key": "C", "value": "Art Market in Decline"},
            {"key": "D", "value": "Shifted Interest in Arts"}
        ],
        "correct_answer": "C",
        "score": 2.0,
        "explanation": """［精准定位］全文主旨标题题需统揽全篇核心脉络。第一段以赫斯特拍卖作为牛市终结的戏剧性警钟；第二段指出全球艺术品市场由650亿美元顶峰滑落；第三段描述藏家远离画廊导致当代艺术销量暴跌三分之二至90%；第四至五段由业内领袖总结市场身处谷底、供给枯竭的萧条现状。
［命题解密］正确项［C］ Art Market in Decline（艺术品市场走向衰落）完美提炼了贯穿全篇的下行基调。全文通篇围绕 losing momentum, downturn, slump, fell by nearly 90% 展开，唯有［C］最全面精准地概括了主旨，故［C］为最佳标题。
［错项排除］［A］将系统性的暴跌衰退弱化为普通的价格日常波动（Fluctuation）；［B］仅着眼于拍卖形式本身，忽视了全行业遭遇重创的宏观背景；［D］偷换为大众艺术兴趣的转移，脱离主旨。
［技巧总结］主旨标题题应紧扣作者的感情色彩与宏观论述走向。全篇无一不在展现繁荣幻灭与市场冷寂，用词 Decline 兼具概括性与准确性。"""
    },

    # Reading Q26 - Q30 (Text 2)
    26: {
        "stem": "What is most wives' main expectation of their husbands?",
        "options": [
            {"key": "A", "value": "Talking to them."},
            {"key": "B", "value": "Trusting them."},
            {"key": "C", "value": "Supporting their careers."},
            {"key": "D", "value": "Sharing housework."}
        ],
        "correct_answer": "A",
        "score": 2.0,
        "explanation": """［精准定位］由题干关键词most wives' main expectation定位至第四段末句：I found, as Hacker observed years before, that most wives want their husbands to be, first and foremost, conversational partners, but few husbands share this expectation of their wives.（我发现，正如哈克多年前观察到的那样，绝大多数妻子首要期望丈夫能成为交谈的伙伴，但很少有丈夫对妻子抱有同样的期待）。
［命题解密］正确项［A］ Talking to them. 是对文中 conversational partners 的直白改写与意译。妻子期望丈夫成为倾听并回应自己的对话伙伴，即“与自己交谈”，故［A］正确。
［错项排除］［B］Trusting them（信任彼此）；［C］Supporting their careers（支持事业）；［D］Sharing housework（分担家务），虽然在第四段首句提到 cleaning, cooking 等家务，但作者明确强调妻子抱怨的核心在于 communication 而非 tangible inequities，故［D］属于反向干扰项。
［技巧总结］细节题抓住最高级或优先级标志词（first and foremost）。原文中 first and foremost conversational partners 直指妻子最核心的期盼，选项［A］直接命中。"""
    },
    27: {
        "stem": "Judging from the context, the phrase “wreaking havoc” (Line 3, Para. 2) most probably means",
        "options": [
            {"key": "A", "value": "generating motivation"},
            {"key": "B", "value": "exerting influence"},
            {"key": "C", "value": "causing damage"},
            {"key": "D", "value": "creating pressure"}
        ],
        "correct_answer": "C",
        "score": 2.0,
        "explanation": """［精准定位］根据题干词汇定位至第二段末句：And this pattern is wreaking havoc with marriage.（而这种模式正在对婚姻……）。
［命题解密］正确项［C］ causing damage（造成破坏/伤害）是 wreaking havoc 的精确词义。后文第三段紧接着引入社会学家的统计数据：近50%的高离婚率中绝大多数女性将“缺乏沟通”视为离婚的主因，末段也指出“沟通失败是离婚的最普遍诱因”，证明男女沟通障碍正在对婚姻关系造成巨大的撕裂与破坏，故［C］正确。
［错项排除］［A］generating motivation（产生动力）；［B］exerting influence（施加影响，中性词，未能体现严重破坏性）；［D］creating pressure（制造压力，破坏力程度不足且词义偏离）。
［技巧总结］词义推断题必须结合“逻辑下文”印证感情色彩。后文围绕 divorce（离婚危机）层层展开，说明该短语必然是严重的负面破坏词，锁定 causing damage。"""
    },
    28: {
        "stem": "All of the following are true EXCEPT",
        "options": [
            {"key": "A", "value": "men tend to talk more in public than women"},
            {"key": "B", "value": "nearly 50 percent of recent divorces are caused by failed conversation"},
            {"key": "C", "value": "women attach much importance to communication between couples"},
            {"key": "D", "value": "a female tends to be more talkative at home than her spouse"}
        ],
        "correct_answer": "B",
        "score": 2.0,
        "explanation": """［精准定位］逆向是非题逐一排查四个选项。
［命题解密］正确项［B］ nearly 50 percent of recent divorces are caused by failed conversation 犯了典型的“数字与因果偷换”逻辑错误。原文第三段第三句为：Given the current divorce rate of nearly 50 percent, that amounts to millions of cases in the United States every year... 原文的意思是“鉴于当前全美总体离婚率接近50%”，而受访女性中绝大多数以缺乏沟通为由离婚。这绝不等于“近50%的离婚案件都是由沟通失败所导致的”，选项歪曲了统计基数与条件从属关系，故［B］为符合题意的反向项。
［错项排除］［A］对应第二段首句American men tend to talk more than women in public situations，符合事实；［C］对应第四段Instead, they focused on communication，符合事实；［D］对应第二段首句they often talk less at home，说明妻子在家里比丈夫更爱说话，符合事实。
［技巧总结］数字细节题是考研出题人的“高频陷阱区”。区分“总体的客观发生率（divorce rate of nearly 50%）”与“特定原因在案件中的占比”，避免概念偷换。"""
    },
    29: {
        "stem": "Which of the following can best summarize the main idea of this text?",
        "options": [
            {"key": "A", "value": "The moral decaying deserves more research by sociologists."},
            {"key": "B", "value": "Marriage break-up stems from sex inequalities."},
            {"key": "C", "value": "Husband and wife have different expectations from their marriage."},
            {"key": "D", "value": "Conversational patterns between man and wife are different."}
        ],
        "correct_answer": "D",
        "score": 2.0,
        "explanation": """［精准定位］主旨概括题需贯通全文论证主线：第一段以弗吉尼亚客厅聚会中的健谈男子在家沉默为引子；第二段点明核心命题——男女说话模式存在巨大反差并破坏婚姻；第三段引入社会学与心理学调查证实男女对交谈功能的认知差异；第四段深入剖析妻子索求对话与丈夫抗拒沉默的冲突；末段以报纸遮面的讽刺漫画形象定格夫妻沟通断层。
［命题解密］正确项［D］ Conversational patterns between man and wife are different. 最直接全面地统摄了全文的主线。整篇文章自始至终围绕“夫妻两性对话模式的不同（Conversational patterns are different）”展开深度阐述，故［D］正确。
［错项排除］［A］偷换为道德败坏（moral decaying），脱离语篇；［B］将沟通问题歪曲为两性不平等（sex inequalities），第四段已明确澄清不满并非源于不平等；［C］将交流模式狭隘化为主观期待差异，概括范围不如［D］精准。
［技巧总结］主旨题优选“核心概念复现最高且直击要害”的选项。本文从头到尾都在讨论 talk, communication, conversational partners，核心即为 conversational patterns。"""
    },
    30: {
        "stem": "In the following part immediately after this text, the author will most probably focus on ________.",
        "options": [
            {"key": "A", "value": "a vivid account of the new book Divorce Talk"},
            {"key": "B", "value": "a detailed description of the stereotypical cartoon"},
            {"key": "C", "value": "other possible reasons for a high divorce rate in the U.S."},
            {"key": "D", "value": "a brief introduction to the political scientist Andrew Hacker"}
        ],
        "correct_answer": "C",
        "score": 2.0,
        "explanation": """［精准定位］后文推断题依据文章结尾段落的逻辑收束点。第四段和第五段系统完成了对“沟通失败（communication failure）作为离婚头号诱因”的深入论述，并以“报纸挡脸”的经典漫画形象对这一现象作了概括总结（In short, the image that best represents the current crisis...）。
［命题解密］正确项［C］ other possible reasons for a high divorce rate in the U.S. 顺理成章地承接了全文对美国离婚危机的学术探讨。作者在详尽剖析了首要原因（沟通失败）之后，下一章节最自然、最具逻辑深度的行文发展方向必然是转向探讨导致美国高离婚率的“其他潜在诱因”，故［C］为最佳合理推断。
［错项排除］［A］Divorce Talk 一书已在第三段完成引用，无需在文末重新叙述；［B］漫画形象在末段已作为总结阐述完毕，属于已知信息；［D］政治学家哈克已在第三、四段完成引证，不会作为独立章节来介绍。
［技巧总结］后文推断题的解题秘诀在于“宏观视野下的行文逻辑推进”。在完成一个主要矛盾维度的全方位剖析后，学术型论述文通常会横向拓展至其他相关影响因素（other possible reasons）。"""
    },

    # Reading Q31 - Q35 (Text 3)
    31: {
        "stem": "According to Dr. Curtis, habits like hand washing with soap ________.",
        "options": [
            {"key": "A", "value": "should be further cultivated"},
            {"key": "B", "value": "should be changed gradually"},
            {"key": "C", "value": "are deeply rooted in history"},
            {"key": "D", "value": "are basically private concerns"}
        ],
        "correct_answer": "A",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词Dr. Curtis及hand washing with soap定位至第二段：...fundamental public health problems, like dirty hands instead of a soap habit, that remain killers only because we can't figure out how to change people's habits... We wanted to learn from industry how to create new behaviors that happen automatically.（像不用肥皂洗手这样的根本公共卫生问题依然是致命杀手，仅仅是因为我们尚未弄清如何改变人们的习惯……我们希望向工业界学习如何创造出自动发生的全新行为）。
［命题解密］正确项［A］ should be further cultivated 准确同义转述了柯蒂斯博士的核心诉求。博士指出缺乏用肥皂洗手的习惯导致疾病蔓延，因此公共卫生界必须向企业取经，努力培养和巩固这一习惯（create new behaviors / should be further cultivated），故［A］正确。
［错项排除］［B］将培养好习惯歪曲为“应当逐渐改变肥皂洗手习惯”；［C］歪曲为这一习惯根植于历史，与原文缺乏该习惯的现状相反；［D］歪曲为纯粹的私人问题，原文明确强调这是 fundamental public health problems。
［技巧总结］细节题需看清作者与引述人物的立场动机。柯蒂斯博士呼吁解决“dirty hands instead of soap”，其目标自然是培养（cultivate）用肥皂洗手的健康习惯。"""
    },
    32: {
        "stem": "Bottled water, chewing gum and skin moisturizers are mentioned in Paragraph 5 so as to ________.",
        "options": [
            {"key": "A", "value": "reveal their impact on people's habits"},
            {"key": "B", "value": "show the urgent need of daily necessities"},
            {"key": "C", "value": "indicate their effect on people's buying power"},
            {"key": "D", "value": "manifest the significant role of good habits"}
        ],
        "correct_answer": "A",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词定位至第四段末与第五段。第四段首句提出论点：...many of the products we use every day — chewing gums, skin moisturizers... are results of manufactured habits. 第五段紧接着具体列举瓶装水、口香糖和润肤霜等日用品如何通过商业广告塑造了大众全新的日常使用习惯。
［命题解密］正确项［A］ reveal their impact on people's habits 完美对应上下文的核心论题。列举这些日常消费品是为了向读者揭示现代商业产品如何深刻重塑并主导了人们的日常生活行为习惯（results of manufactured habits），故［A］正确。
［错项排除］［B］歪曲为说明日常必需品的紧迫需求；［C］偷换为展现产品对人们购买力的影响；［D］偏离商业营销主线，歪曲为弘扬好习惯的意义。
［技巧总结］例证题恪守“例子支撑其所在段落核心论点”原则。段落核心是 manufactured habits（被制造出来的习惯），举例即为说明产品对消费习惯的巨大塑造影响。"""
    },
    33: {
        "stem": "Which of the following does NOT belong to products that help create people's habits?",
        "options": [
            {"key": "A", "value": "Tide."},
            {"key": "B", "value": "Crest."},
            {"key": "C", "value": "Colgate."},
            {"key": "D", "value": "Unilever."}
        ],
        "correct_answer": "D",
        "score": 2.0,
        "explanation": """［精准定位］逆向考查对文中企业与产品/品牌概念的辨析。第三段提到：The companies that Dr. Curtis turned to — Procter & Gamble, Colgate-Palmolive and Unilever...；第六段提到：...sold $76 billion of Tide, Crest and other products last year.
［命题解密］正确项［D］ Unilever 属于公司企业名称（联合利华），而非单一的具体产品或消费品品牌。题干明确设问“Which does NOT belong to products...”，［A］Tide（汰渍洗衣粉）、［B］Crest（佳洁士牙膏）、［C］Colgate（高露洁牙膏）均为用于改变消费者日常习惯的知名产品/品牌，唯有联合利华是企业法人，故［D］为符合要求的正确答案。
［错项排除］［A］、［B］、［C］在文中均明确作为日用消费品产品品牌出现，不符合NOT设问。
［技巧总结］考研英语常在细微的“概念范畴（企业 Company vs. 产品 Product）”上设伏。细读第三段 companies 和第四、六段 products 的不同表述即可精准识别。"""
    },
    34: {
        "stem": "From the text we know that some of consumers' habits are developed due to ________.",
        "options": [
            {"key": "A", "value": "perfected art of products"},
            {"key": "B", "value": "automatic behavior creation"},
            {"key": "C", "value": "commercial promotions"},
            {"key": "D", "value": "scientific experiments"}
        ],
        "correct_answer": "C",
        "score": 2.0,
        "explanation": """［精准定位］由题干关键词consumers' habits are developed due to定位至第四段第二句：Today, because of shrewd advertising and public health campaigns, many Americans habitually give their pearly whites a cavity-preventing scrub... 以及末段首句：...tying certain behaviors to habitual cues through ruthless advertising.
［命题解密］正确项［C］ commercial promotions（商业推广/广告营销）准确概括了文中的 shrewd advertising 和 ruthless advertising。正是日用品巨头长年累月铺天盖地的商业广告和促销活动，才促成了大众诸如每天刷牙两次、饭后嚼口香糖等消费习惯的养成，故［C］正确。
［错项排除］［A］将原因歪曲为产品制造技术完美无瑕；［B］automatic behavior creation 本身就是习惯的表现形式，而非其背后的外部驱动因；［D］科学实验只是学者观察总结的工具，并非促使大众养成习惯的原因。
［技巧总结］因果推断题抓准原文中的驱动动因（because of shrewd advertising / through advertising）。广告推广（advertising）的标准高级同义替换即为 commercial promotions。"""
    },
    35: {
        "stem": "The author's attitude toward the influence of advertisement on people's habits is ________.",
        "options": [
            {"key": "A", "value": "indifferent"},
            {"key": "B", "value": "negative"},
            {"key": "C", "value": "positive"},
            {"key": "D", "value": "biased"}
        ],
        "correct_answer": "B",
        "score": 2.0,
        "explanation": """［精准定位］情感态度题需重点考察文章末尾作者对广告影响的价值评述。文章最后一段指出：...tying certain behaviors to habitual cues through ruthless advertising. As this new science of habit has emerged, controversies have erupted when the tactics have been used to sell questionable beauty creams or unhealthy foods.（通过冷酷无情的广告将特定行为与习惯提示绑定……随着这一习惯新科学的出现，当这些策略被用来兜售可疑的美容霜或不健康的垃圾食品时，争议便爆发了）。
［命题解密］正确项［B］ negative（消极的，负面的，批判的）准确捕捉了作者在末段的鲜明倾向。作者使用了 ruthless（无情的）、controversies（争议）、questionable（可疑的）、unhealthy（不健康的）等一系列强烈的贬义词汇，揭露企业利用心理操控兜售有害产品的恶劣影响，态度明显偏向负面批判，故［B］正确。
［错项排除］［A］indifferent（漠不关心的）；［C］positive（积极支持的）；［D］biased（有偏见的，态度题通常不选极端贬义的人格缺陷词）。
［技巧总结］攻克态度题的关键在于提炼末段的“修饰性形容词和副词”。ruthless advertising 和 questionable/unhealthy foods 明确表达了作者对广告操纵心智的批判与担忧立场。"""
    },

    # Reading Q36 - Q40 (Text 4)
    36: {
        "stem": "From the principles of the US jury system, we learn that ________.",
        "options": [
            {"key": "A", "value": "both literate and illiterate people can serve on juries"},
            {"key": "B", "value": "defendants are immune from trial by their peers"},
            {"key": "C", "value": "no age limit should be imposed for jury service"},
            {"key": "D", "value": "judgment should consider the opinion of the public"}
        ],
        "correct_answer": "D",
        "score": 2.0,
        "explanation": """［精准定位］由题干关键词principles of the US jury system定位至第一段长难句：...and that verdicts should represent the conscience of the community and not just the letter of the law.（并且裁决应当代表社会的良知，而不仅仅是法律的字面条文）。
［命题解密］正确项［D］ judgment should consider the opinion of the public 是对 verdicts should represent the conscience of the community 的精妙同义转述。judgment 替换 verdicts（判决/裁决），opinion of the public 替换 conscience of the community（公众舆论/公众良知），说明审判应当倾听并反映社会公众的意愿，故［D］正确。
［错项排除］［A］与原文who meet minimal qualifications of age and literacy（符合最低识字率与年龄标准）矛盾，文盲不能服役；［B］与原文defendants are entitled to trial by their peers（被告有权接受同侪审判）彻底反向；［C］与原文age minimal qualifications（存在最低年龄门槛）矛盾。
［技巧总结］长难句平行排比结构中，末尾的核心结论句往往是命题点所在。verdicts 与 judgment，community conscience 与 public opinion 的对应展现了高阶同义转换。"""
    },
    37: {
        "stem": "The practice of selecting so-called elite jurors prior to 1968 showed ________.",
        "options": [
            {"key": "A", "value": "the inadequacy of antidiscrimination laws"},
            {"key": "B", "value": "the prevalent discrimination against certain races"},
            {"key": "C", "value": "the conflicting ideals in jury selection procedures"},
            {"key": "D", "value": "the arrogance common among the Supreme Court judges"}
        ],
        "correct_answer": "A",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词selecting so-called elite jurors prior to 1968定位至第二段后半部分：Although the Supreme Court of the United States had prohibited intentional racial discrimination in jury selection as early as the 1880 case of Strauder v. West Virginia, the practice of selecting so-called elite or blue-ribbon juries provided a convenient way around this and other antidiscrimination laws.
［命题解密］正确项［A］ the inadequacy of antidiscrimination laws 直接印证了原文 provided a convenient way around this and other antidiscrimination laws。尽管最高法院早在1880年就禁止种族歧视，但各地法庭却通过遴选所谓的“精英或蓝带陪审团”轻而易举地规避了反歧视法规，这恰恰暴露了既有反歧视法律在执行与覆盖层面的严重不足与缺陷（inadequacy），故［A］正确。
［错项排除］［B］只看到了种族表象，未触及精英陪审制度打擦边球规避法律的制度漏洞核心；［C］将法律规避歪曲为程序上的理想冲突；［D］无端攻击最高法院法官傲慢，原文无中生有。
［技巧总结］抓住转折让步关系（Although... had prohibited... the practice provided a way around...）。既然禁令被轻易绕过（way around），必然说明现有法规存在漏洞与不健全（inadequacy）。"""
    },
    38: {
        "stem": "Even in the 1960s, women were seldom on the jury list in some states because ________.",
        "options": [
            {"key": "A", "value": "they were automatically banned by state laws"},
            {"key": "B", "value": "they fell far short of the required qualifications"},
            {"key": "C", "value": "they were supposed to perform domestic duties"},
            {"key": "D", "value": "they tended to evade public engagement"}
        ],
        "correct_answer": "C",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词women were seldom on the jury list / in the 1960s定位至第三段末尾两句：Even then several states automatically exempted women from jury duty unless they personally asked to have their names included on the jury list. This practice was justified by the claim that women were needed at home, and it kept juries unrepresentative of women through the 1960s.
［命题解密］正确项［C］ they were supposed to perform domestic duties 完美同义改写了原文 women were needed at home。当时社会普遍抱持家长式偏见，认为女性的首要天职是操持家务与相夫教子（perform domestic duties），因此以家庭需要为由免除其陪审义务，导致60年代女性在陪审员名单中极少出现，故［C］正确。
［错项排除］［A］将自动免除义务（automatically exempted）歪曲为法律强制禁止（banned）；［B］歪曲为女性达不到服役资历要求；［D］歪曲为女性主动逃避公共参与。
［技巧总结］原因解释题精准比对原文中的借口声明（justified by the claim that...）。needed at home 与 domestic duties 是考研词汇中最经典的互释对。"""
    },
    39: {
        "stem": "After the Jury Selection and Service Act was passed, ________.",
        "options": [
            {"key": "A", "value": "sex discrimination in jury selection was unconstitutional and had to be abolished"},
            {"key": "B", "value": "educational requirements became less rigid in the selection of federal jurors"},
            {"key": "C", "value": "jurors at the state level ought to be representative of the entire community"},
            {"key": "D", "value": "states ought to conform to the federal court in reforming the jury system"}
        ],
        "correct_answer": "B",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词Jury Selection and Service Act定位至第四段第一、二句：In 1968, the Congress of the United States passed the Jury Selection and Service Act, ushering in a new era of democratic reforms for the jury. This law abolished special educational requirements for federal jurors and required them to be selected at random from a cross section of the entire community.
［命题解密］正确项［B］ educational requirements became less rigid in the selection of federal jurors 精准同义转述了 This law abolished special educational requirements for federal jurors。法案废除了专门针对联邦陪审员设立的特殊严苛学历门槛，使得学历要求变得不再僵化严苛（became less rigid），故［B］正确。
［错项排除］［A］将1975年最高法院 Taylor 判例的结论错置到1968年国会法案之中；［C］同样属于1975年 Taylor 案将社区代表性原则推广至“州级别法院”的后续成果；［D］无中生有，文中未提及州法庭必须顺从联邦法庭。
［技巧总结］法律与历史法案题必须严守“时间与实施主体界限”。1968年法案针对的是 federal jurors，其核心举措是 abolished special educational requirements，对应 became less rigid。"""
    },
    40: {
        "stem": "In discussing the US jury system, the text centers on ________.",
        "options": [
            {"key": "A", "value": "its nature and problems"},
            {"key": "B", "value": "its characteristics and tradition"},
            {"key": "C", "value": "its problems and their solutions"},
            {"key": "D", "value": "its tradition and development"}
        ],
        "correct_answer": "D",
        "score": 2.0,
        "explanation": """［精准定位］全文主旨大意题需纵览全篇的叙事结构演进：第一段阐述美国陪审团植根于宪政历史的崇高民主理念与直接民主传统；第二、三段展现历史上在遴选中排斥少数族裔与女性的保守传统实践；第四段聚焦1968年国会法案与1975年最高法院具有分水岭意义的平权立法与司法裁决，展现制度向包容与平等方向的发展演变。
［命题解密］正确项［D］ its tradition and development 精准提炼了文章“传统根基（tradition）”与“历史演进发展（development）”的双重轴线，既囊括了早期的排他性历史，又概括了现当代走向代表性的改革步伐，故［D］为最佳概括。
［错项排除］［A］its nature and problems 过于静态负面，割裂了后半篇显著的法治进步；［B］缺少对下半篇改革立法与发展的提炼；［C］侧重于实用性政策解决方案，与本文客观严肃的法制制度史风格不符。
［技巧总结］制度史类文章主旨题关注“动态时间线”。通篇由 1880 -> 1940s -> 1968 -> 1975 串联，选项中的 development 画龙点睛。"""
    },

    # Reading Part B Q41 - Q45
    41: {
        "stem": "Findings of the Stanford University researchers will promote the sales of new Boeing and Airbus aircraft.",
        "options": [{"key": "T", "value": "True"}, {"key": "F", "value": "False"}],
        "correct_answer": "F",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词Stanford University researchers及sales of new Boeing and Airbus aircraft定位至第一段末句：But a group of researchers at Stanford University, led by Ilan Kroo, has suggested that airlines could take a more naturalistic approach to cutting jet-fuel use and it would not require them to buy new aircraft.（但是由伊兰·克鲁领导的斯坦福大学研究小组提出，航空公司可以采取一种更天然的方式来降低航油消耗，而且这种方法并不需要航空公司购买新客机）。
［命题解密］原文明确强调该研究方案的核心优势就在于“it would not require them to buy new aircraft（不需要购买新客机）”，这与题干声称的“将促进波音和空客新客机的销售（promote the sales of new Boeing and Airbus aircraft）”在逻辑上截然相反，陈述明显不符合原文事实，故判断为［False］。"""
    },
    42: {
        "stem": "The upwash experience may save propelling energy as well as reducing resistance.",
        "options": [{"key": "T", "value": "True"}, {"key": "F", "value": "False"}],
        "correct_answer": "T",
        "score": 2.0,
        "explanation": """［精准定位］由题干关键词upwash experience, propelling energy, reducing resistance定位至第二段第三、四句：The air flowing over a bird's wings curls upwards behind the wingtips, a phenomenon known as upwash. Other birds flying in the upwash experience reduced drag, and spend less energy propelling themselves.（流经鸟类翅膀的气流在翼尖后方向上卷起，这种现象被称为上升气流。在上升气流中飞行的其他鸟类受到的阻力减小，并且用于向前推进自身所消耗的能量也更少）。
［命题解密］题干中的 reducing resistance 对应原文中的 reduced drag（阻力减小），save propelling energy 对应原文中的 spend less energy propelling themselves（推进能耗降低）。题干陈述与原文叙述完全吻合，故判断为［True］。"""
    },
    43: {
        "stem": "Formation flight is more comfortable because passengers can not see the other planes.",
        "options": [{"key": "T", "value": "True"}, {"key": "F", "value": "False"}],
        "correct_answer": "F",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词comfortable及passengers can not see the other planes定位至第四段第二至五句：One consideration is safety, or at least the perception of it. Would passengers feel comfortable travelling in companion? Dr. Kroo points out that the aircraft could be separated by several nautical miles... A passenger peering out of the window might not even see the other planes.
［命题解密］原文指出编队飞行的一大顾虑是乘客的安全感（Would passengers feel comfortable...?），克鲁博士解释说飞机间距可达数海里，望向窗外的乘客甚至看不到其他飞机。这一解释仅是为了打消乘客对于飞机靠得太近的安全恐惧与心理焦虑，文章并未得出“因为看不到其他飞机，编队飞行就会‘更加舒适（is more comfortable）’”这一荒谬因果推论，强加因果且夸大事实，故判断为［False］。"""
    },
    44: {
        "stem": "The role that weather plays in formation flight has not yet been clearly defined.",
        "options": [{"key": "T", "value": "True"}, {"key": "F", "value": "False"}],
        "correct_answer": "T",
        "score": 2.0,
        "explanation": """［精准定位］由题干关键词weather及clearly defined定位至第五段第一至三句：It remains to be seen how weather conditions affect the air flows that make formation flight more efficient. In zones of increased turbulence, the planes' wakes will decay more quickly and the effect will diminish. Dr. Kroo says this is one of the areas his team will investigate further.（天气状况如何影响使编队飞行更加高效的气流，目前仍有待观察……克鲁博士表示这是其团队将进一步深入调研的领域之一）。
［命题解密］原文明确使用了 It remains to be seen（尚待观察）以及 investigate further（有待进一步研究），直接证明天气在编队飞行中的具体影响与作用机制目前尚未被完全明确地界定与证实，题干陈述 has not yet been clearly defined 与原文事实高度一致，故判断为［True］。"""
    },
    45: {
        "stem": "It has been documented that during World War II, America's armed forces once tried formation flight to save fuel.",
        "options": [{"key": "T", "value": "True"}, {"key": "F", "value": "False"}],
        "correct_answer": "F",
        "score": 2.0,
        "explanation": """［精准定位］根据题干关键词documented, World War II, America's armed forces定位至文章最后一段后半部分：Rumours abound that fighter pilots were known to fly in formation when they were low on fuel during the Second World War, but Dr. Lissaman says they are unsubstantiated.（流传甚广的传言称，二战期间战斗机飞行员在燃油不足时曾进行编队飞行，但利萨曼博士表示这些传言都是未经证实的）。
［命题解密］原文明确将二战期间低油量编队飞行的说法定性为 Rumours（民间传言）并且已被航空专家判定为 unsubstantiated（未经证实的，缺乏事实根据的）。题干却声称“It has been documented（已被文献/官方档案所证实记载）”，与原文“传闻且查无实据”彻底颠倒矛盾，故判断为［False］。"""
    }
}

# Update Questions
questions = d.get('questions', [])
print(f"Total existing questions in json: {len(questions)}")

for i in range(1, 46):
    idx = i - 1
    if idx < len(questions):
        q = questions[idx]
        gdata = gold_q_data[i]
        q['question_number'] = i
        q['sort_order'] = i
        q['stem'] = f'Choose the best option for blank [{i}] in the passage:' if i <= 20 else gdata['stem']
        q['options'] = [{'key': opt['key'], 'text': opt.get('text') or opt.get('value'), 'value': opt.get('value') or opt.get('text')} for opt in gdata['options']]
        q['correct_answer'] = gdata['correct_answer']
        q['answer'] = gdata['correct_answer']
        q['score'] = gdata['score']
        q['points'] = gdata['score']
        q['explanation'] = gdata['explanation']

# Save calibrated json
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("=== Successfully calibrated 2010 ky2 pure gold data ===")
