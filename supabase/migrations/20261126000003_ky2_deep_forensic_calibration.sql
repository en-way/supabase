-- Deep forensic calibration for KY2 (11 PDF paragraph restorations + citation/glued-token/zero-AI-fabrication fixes)
BEGIN;
-- 2013 Q27
UPDATE public.questions SET explanation = '【精准定位】定位至第二段：That framework has contributed mightily to our broken immigration system and the long political paralysis over how to fix it... We might then begin to solve our immigration challenges.
【命题解密】作者指出当前将移民简单非黑即白地二元划分导致了移民体系瘫痪破败，呼吁超越合法与非法的刻板定义，通过顺应新流动趋势来化解移民挑战。C项 should be adapted to meet challenges 为合理推断。
【错项排除】[A] 原文明确说 We don''t need more categories；[B] 放宽对移民管控与文首 we are much more rigid 相悖；[D] 已通过政治手段修复与 long political paralysis（长期政治瘫痪）相悖。' WHERE id = '1eb69108-28b3-50b0-b8d9-6c7117259e20';
-- 2013 Q33
UPDATE public.questions SET explanation = '【精准定位】定位至首段（if we take a moment and think about how we are likely to react, we can reduce or even eliminate the negative effects）与第四段（we can take a moment before buying）。
【命题解密】作者在首段提出“行动前先思考（take a moment and think）”，第四段又呼应建议“购买前稍作停顿（take a moment before buying）”。B项 think before we act（三思而后行）是对这一解决之道的经典提炼。
【错项排除】[A] 相信第一印象属于盲目跟随快速反应；[C] 照常人行事与抵御本能冲动无关；[D] 寻求专家建议文中未提及。' WHERE id = '8e7daad5-e8cd-5ba2-9f7a-b20bd45cceb3';
-- 2014 passage[3] (reading)
UPDATE public.passages SET content = 'The concept of man versus machine is at least as old as the industrial revolution, but this phenomenon tends to be most acutely felt during economic downturns and fragile recoveries. And yet, it would be a mistake to think we are right now simply experiencing the painful side of a boom and bust cycle. Certain jobs have gone away for good, outmoded by machines. Since technology has such an insatiable appetite for eating up human jobs, this phenomenon will continue to restructure our economy in ways we cannot immediately foresee.

When there is rapid improvement in the price and performance of technology, jobs that were once thought to be immune from automation suddenly become threatened. This argument has attracted a lot of attention, via the success of the book Race Against the Machine, by Erik Brynjolfsson and Andrew McAfee, who both hail from MIT''s Center for Digital Business.

This is a powerful argument, and a scary one. And yet, John Hagel, author of The Power of Pull and other books, says Brynjolfsson and McAfee miss the reason why these jobs are so vulnerable to technology in the first place.

Hagel says we have designed jobs in the U.S. that tend to be "tightly scripted" and "highly standardized" ones that leave no room for "individual initiative or creativity." In short, these are the types of jobs that machines can perform much better at than human beings. That is how we have put a giant target sign on the backs of American workers, Hagel says.

It''s time to reinvent the formula for how work is conducted, since we are still relying on a very 20th century notion of work, Hagel says. In our rapidly changing economy, we more than ever need people in the workplace who can take initiative and exercise their imagination "to respond to unexpected events". That is not something machines are good at. They are designed to perform very predictable activities.

As Hagel notes, Brynjolfsson and McAfee indeed touched on this point in their book. We need to reframe race against the machine as race with the machine. In other words, we need to look at the ways in which machines can augment human labor rather than replace it. So then the problem is not really about technology, but rather, "how do we innovate our institutions and our work practices?"' WHERE id = 'd3b97d7d-9ce2-533d-a976-5ad5cb5eed15';
-- 2014 passage[4] (reading)
UPDATE public.passages SET content = 'When the government talks about infrastructure contributing to the economy the focus is usually on roads, railways, broadband and energy. Housing is seldom mentioned.

Why is that? To some extent the housing sector must shoulder the blame. We have not been good at communicating the real value that housing can contribute to economic growth. Then there is the scale of the typical housing project. It is hard to shove for attention among multibillion-pound infrastructure projects, so it is inevitable that the attention is focused elsewhere. But perhaps the most significant reason is that the issue has always been so politically charged.

Nevertheless, the affordable housing situation is desperate. Waiting lists increase all the time and we are simply not building enough new homes.

The comprehensive spending review offers an opportunity for the government to help rectify this. It needs to put historical prejudices to one side and take some steps to address our urgent housing need.

There are some indications that it is preparing to do just that. The communities minister, Don Foster, has hinted that George Osborne, Chancellor of the Exchequer, may introduce more flexibility to the current cap on the amount that local authorities can borrow against their housing stock debt. Evidence shows that 60,000 extra new homes could be built over the next five years if the cap were lifted, increasing GDP by 0.6%.

Ministers should also look at creating greater certainty in the rental environment, which would have a significant impact on the ability of registered providers to fund new developments from revenues.

But it is not just down to the government. While these measures would be welcome in the short term, we must face up to the fact that the existing £4.5bn programme of grants to fund new affordable housing, set to expire in 2015, is unlikely to be extended beyond then. The Labour party has recently announced that it will retain a large part of the coalition''s spending plans if it returns to power. The housing sector needs to accept that we are very unlikely to ever return to the era of large-scale public grants. We need to adjust to this changing climate.

While the government''s commitment to long-term funding may have changed, the very pressing need for more affordable housing is real and is not going away.' WHERE id = '6cf9c9d9-48d8-522b-b667-903fdc90f50a';
-- 2014 Q41
UPDATE public.questions SET explanation = '【精准定位】定位至第四段首句：“Long is Britain''s best-known Land Artist and his Stone Circle, a perfect ring of purplish rocks from Portishead beach laid out on the gallery floor, represents the elegant, rarefied side of the form.”
【命题解密】考查多项对应。理查德·朗的作品《石环》（Stone Circle）在画廊地面用紫色卵石摆出完美圆环，明确代表着英国大地艺术优雅高洁的一面。选项[D]“represents the elegance of the British land art”精准对应原文 elegant, rarefied side of the form，故选[D]。
【错项排除】[B]项指展览尾段对英国大地艺术总体特征的概括；[E]项对应博伊尔家族的《奥拉夫街研究》，与《石环》相反。' WHERE id = '143e03d1-ee7e-5188-bec3-f83f5ee4bda0';
-- 2015 passage[0] (cloze)
UPDATE public.passages SET content = 'In our contemporary culture, the prospect of communicating with — or even looking at — a stranger is virtually unbearable. Everyone around us seems to agree by the way they cling to their phones, even without a [1] on a subway.

It''s a sad reality — our desire to avoid interacting with other human beings — because there''s [2] to be gained from talking to the stranger standing by you. But you wouldn''t know it, [3] into your phone. This universal protection sends the [4] "Please don''t approach me."

What is it that makes us feel we need to hide [5] our screens?

One answer is fear, according to Jon Wortmann, an executive mental coach. We fear rejection, or that our innocent social advances will be [6] as "weird." We fear we''ll be [7]. We fear we''ll be disruptive.

Strangers are inherently [8] to us, so we are more likely to feel [9] when communicating with them compared with our friends and acquaintances. To avoid this uneasiness, we [10] to our phones. "Phones become our security blanket," Wortmann says. "They are our happy glasses that protect us from what we perceive is going to be more [11]."

But once we rip off the band-aid, tuck our smartphones in our pockets and look up, it doesn''t [12] so bad. In one 2011 experiment, behavioral scientists Nicholas Epley and Juliana Schroeder asked commuters to do the unthinkable: Start a [13]. They had Chicago train commuters talk to their fellow [14]. "When Dr. Epley and Ms. Schroeder asked other people in the same train station to [15] how they would feel after talking to a stranger, the commuters thought their [16] would be more pleasant if they sat on their own," The New York Times summarizes. Though the participants didn''t expect a positive experience, after they [17] with the experiment, "not a single person reported having been embarrassed." [18], these commutes were reportedly more enjoyable compared with those without communication, which makes absolute sense, [19] human beings thrive off of social connections. It''s that [20]: Talking to strangers can make you feel connected.' WHERE id = 'b6c718aa-1ace-58ff-8e8a-847e5ff6782c';
-- 2015 passage[4] (reading)
UPDATE public.passages SET content = 'Many people talked of the 288,000 new jobs the Labor Department reported for June, along with the drop in the unemployment rate to 6.1 percent, as good news. And they were right. For now it appears the economy is creating jobs at a decent pace. We still have a long way to go to get back to full employment, but at least we are now finally moving forward at a faster pace.

However, there is another important part of the jobs picture that was largely overlooked. There was a big jump in the number of people who report voluntarily working part-time. This figure is now 830,000 (4.4 percent) above its year ago level.

Before explaining the connection to the Obamacare, it is worth making an important distinction. Many people who work part-time jobs actually want full-time jobs. They take part-time work because this is all they can get. An increase in involuntary part-time work is evidence of weakness in the labor market and it means that many people will be having a very hard time making ends meet.

There was an increase in involuntary part-time in June, but the general direction has been down. Involuntary part-time employment is still far higher than before the recession, but it is down by 640,000 (7.9 percent) from its year ago level.

We know the difference between voluntary and involuntary part-time employment because people tell us. The survey used by the Labor Department asks people if they worked less than 35 hours in the reference week. If the answer is "yes," they are classified as working part-time. The survey then asks whether they worked less than 35 hours in that week because they wanted to work less than full time or because they had no choice. They are only classified as voluntary part-time workers if they tell the survey taker they chose to work less than 35 hours a week.

The issue of voluntary part-time relates to Obamacare because one of the main purposes was to allow people to get insurance outside of employment. For many people, especially those with serious health conditions or family members with serious health conditions, before Obamacare the only way to get insurance was through a job that provided health insurance.

However, Obamacare has allowed more than 12 million people to either get insurance through Medicaid or the exchanges. These are people who may previously have felt the need to get a full-time job that provided insurance in order to cover themselves and their families. With Obamacare there is no longer a link between employment and insurance.' WHERE id = '7e558466-7a01-5cc8-9f0d-41cd9bff9bbe';
-- 2015 Q6
UPDATE public.questions SET explanation = '［考点提炼］动词语义辨析与被动语态。
［精准定位］第四段第二句：We fear rejection, or that our innocent social advances will be [6] as "weird."
［命题解密］作者分析社交恐惧的根源：我们担心遭到拒绝，或者担心自己善意的社交举动会被对方“误解/曲解（misinterpreted）”为行为古怪（"weird"）。misinterpreted 准确传达了善意互动遭曲解的意思，故选[B]。
［错项排除］[A] misapplied（被误用）、[C] misadjusted（被错误调整）与 [D] mismatched（不匹配）均无法表达社交意图被对方错误解读之意。' WHERE id = '5cb1e86d-e628-587c-874a-17f9a84309f4';
-- 2015 Q7
UPDATE public.questions SET explanation = '［考点提炼］动词被动语义辨析与社交心理。
［精准定位］第四段第三句：We fear we''ll be [7]. We fear we''ll be disruptive.
［命题解密］本段连续以 We fear... 排比句式剖析心理阴影：人们害怕被拒绝、被评价被评头论足（judged）、害怕造成打扰。judged 意为“被评判/被指指点点”，切合社交焦虑的核心特征，故 A 项正确。
［错项排除］B项 fired（被解雇）、C项 replaced（被取代）与 D项 delayed（被延误）均属于职场或行程词汇，脱离了大众陌生人交流的心理范畴。' WHERE id = 'bc231fef-7c1d-5c8a-a101-a6356fe47996';
-- 2015 Q8
UPDATE public.questions SET explanation = '［考点提炼］形容词语义辨析与词汇复现。
［精准定位］第五段第一句：Strangers are inherently [8] to us, so we are more likely to feel...
［命题解密］strangers（陌生人）天然具有的特质就是“陌生的、不熟悉的（unfamiliar）”，这正是人们对其产生心理防备的生物学根源。故 D 项 unfamiliar 符合同根逻辑。
［错项排除］A项 unreasonable（不合理的）、B项 ungrateful（忘恩负义的）与 C项 unconventional（非传统的）皆非陌生人的固有本质属性。' WHERE id = 'c9acb565-7a2a-5985-bdb1-0908b6a00e29';
-- 2015 Q9
UPDATE public.questions SET explanation = '［考点提炼］形容词语义辨析与后文词汇照应。
［精准定位］第五段第一至二句：so we are more likely to feel [9]... To avoid this uneasiness, we...
［命题解密］第七句紧接着点出 To avoid this uneasiness（为了避免这种不安），this uneasiness 回指第[9]空，说明与陌生人交流比与熟人相处更容易感到焦虑不安，故 [C] anxious 正确。
［错项排除］[A] comfortable（舒适的）与 [B] confident（自信的）情感极性相反；[D] angry（愤怒的）不符合面对陌生人时的紧张拘束心理。' WHERE id = '3f740472-eb95-515d-8558-6acc622dfe2d';
-- 2015 Q10
UPDATE public.questions SET explanation = '［考点提炼］动词短语搭配与语义逻辑。
［精准定位］第五段第二句：To avoid this uneasiness, we [10] to our phones.
［命题解密］turn to sb./sth. 为固定搭配，意为“转向、求助于”。为回避与陌生人互动的不安，人们转而拿起手机寻求掩护与心理依托，故 [B] turn 正确。
［错项排除］[A] attend to（照料/专心处理）、[C] take to（喜欢上/养成……习惯）与 [D] point to（指向）均不能表达“为逃避焦虑而求助寄托”的语义。' WHERE id = '2c76eeb3-3a56-51b3-adc4-deb59790467c';
-- 2015 Q11
UPDATE public.questions SET explanation = '［考点提炼］形容词语义辨析与前文比喻照应。
［精准定位］第五段末句：protect us from what we perceive is going to be more [11].
［命题解密］前文将手机比喻为 security blanket（安全毯），安全毯的作用是保护我们免受潜在“危险/危害（dangerous）”的侵袭，对应社交恐惧中人们对外部不可控威胁的主观臆想。故 A 项 dangerous 正确。
［错项排除］B项 mysterious（神秘的）、C项 violent（暴力的）与 D项 boring（无聊的）均偏离了安全防护的比喻重心。' WHERE id = '24ee46fb-0c14-50c5-a89a-906315bfbe17';
-- 2015 Q12
UPDATE public.questions SET explanation = '［考点提炼］动词语义辨析与习语用法。
［精准定位］第六段第一句：But once we rip off the band-aid, tuck our smartphones in our pockets and look up, it doesn''t [12] so bad.
［命题解密］作者用“撕掉创可贴（rip off the band-aid）”作比喻：一旦收起手机抬头接触外界，其实“并没有那么痛/没那么糟（doesn''t hurt so bad）”。hurt 此处体现克服社交障碍时的心理不适或疼痛感，故 [C] hurt 正确。
［错项排除］[A] bend（弯曲）、[B] resist（抵抗）与 [D] decay（腐烂）均不与 so bad 搭配形容心理感受。' WHERE id = '6021ee3d-164c-5a45-bde5-bf0a9c19bf31';
-- 2015 Q13
UPDATE public.questions SET explanation = '［考点提炼］名词语义辨析与后文同义词复现。
［精准定位］第六段第二至三句：Start a [13]. They had Chicago train commuters talk to their fellow...
［命题解密］后文明确解释实验内容是让乘客与周围同行的人交谈（talk to），后文多次出现 talking to a stranger, communication。因此 start a conversation（开始交谈/攀谈）为标准表达，故 C 项正确。
［错项排除］A项 lecture（讲座）、B项 debate（辩论）与 D项 negotiation（谈判）皆为正式严肃的特殊沟通形式，非通勤车厢中自发的日常攀谈。' WHERE id = '4bd889dc-7acb-504f-8206-6ec0b974b4a3';
-- 2015 Q14
UPDATE public.questions SET explanation = '［考点提炼］名词语义辨析与场景常识。
［精准定位］第六段第三句：They had Chicago train commuters talk to their fellow [14].
［命题解密］train commuters 指火车通勤乘客，与其同行的人显然是同车“乘客（passengers）”。fellow passengers 意为同行乘客，故 D 项正确。
［错项排除］A项 trainees（实习生）、B项 employees（雇员）与 C项 researchers（研究员）与车厢公共交通环境不符。' WHERE id = 'f0aad498-cd56-516a-a0b0-8894efab8596';
-- 2015 Q15
UPDATE public.questions SET explanation = '［考点提炼］动词语义辨析与实验对比逻辑。
［精准定位］第六段第四句：asked other people in the same train station to [15] how they would feel after talking to a stranger...
［命题解密］实验人员让未参与交谈的站台路人“预测/设想（predict）”如果和陌生人搭讪会是什么感觉。路人预测自己单独坐着会更舒适，而实际参与实验的人体验却很愉快。这种前后反差体现 predict 的科学对比设计。故 C 项 predict 正确。
［错项排除］A项 reveal（揭示/透露）、B项 choose（选择）与 D项 design（设计）均非让受试者预判未来心理感受的准确词汇。' WHERE id = 'fca041ed-a564-5e72-8328-c11030036cd6';
-- 2015 Q16
UPDATE public.questions SET explanation = '［考点提炼］名词语义辨析与交通场景。
［精准定位］第六段第四句：the commuters thought their [16] would be more pleasant if they sat on their own...
［命题解密］乘坐火车、汽车等交通工具的通勤路程通常称作 ride（车程/乘坐）。后文也提到 these commutes were reportedly more enjoyable。故 D 项 ride 准确贴切。
［错项排除］A项 voyage（长途航海旅行）、B项 flight（飞机航班）与 C项 walk（步行）均与坐火车（train commuters）的场景相悖。' WHERE id = '1fc54b94-aa6f-5ed8-a41a-01542225db7b';
-- 2015 Q17
UPDATE public.questions SET explanation = '［考点提炼］动词短语搭配与上下文语义。
［精准定位］第六段第五句：after they [17] with the experiment, "not a single person reported having been embarrassed."
［命题解密］go through with sth. 意为“坚持完成、把……做到底”。受试者顶住最初顾虑完成了搭讪实验，结果竟然“没有一个人表示感到尴尬（embarrassed）”，故 [A] went through 正确。
［错项排除］[B] did away with（废除）、[C] caught up with（追赶上）与 [D] put up with（忍受）均不与完成实验（experiment）匹配。' WHERE id = 'baf6a010-2238-56f3-8081-361b430035d5';
-- 2015 Q18
UPDATE public.questions SET explanation = '［考点提炼］逻辑副词短语与语篇推进。
［精准定位］第六段第六句：[18], these commutes were reportedly more enjoyable compared with those without communication...
［命题解密］前一句指出受试者没有一人被冷落，本句进一步递进揭示惊喜的事实真相：事实上（In fact），比起一路沉默，这些进行了交流的通勤过程反而更加愉快。故 B 项 In fact 承前启后表达递进与事实陈述，最为精确。
［错项排除］A项 In turn（轮流/反过来）、C项 In particular（特别/尤其）与 D项 In consequence（结果）在此处均缺乏严密的逻辑支撑。' WHERE id = '032aec59-c6f9-5b2c-8ec7-02fd11fb1a70';
-- 2015 Q19
UPDATE public.questions SET explanation = '［考点提炼］连词辨析与因果论证。
［精准定位］第六段第六句：which makes absolute sense, [19] human beings thrive off of social connections.
［命题解密］前半句表示交谈带来快乐是完全讲得通的（makes absolute sense），后半句给出理论依据：因为（since）人类本就是依靠社会连接而繁衍兴旺的。since 引导原因状语从句，逻辑严谨。故 D 项 since 正确。
［错项排除］A项 unless（除非）、B项 whereas（然而/反之）与 C项 if（如果）均不能引导具有客观必然性的因果解释从句。' WHERE id = '001a28ab-ee6a-5a1c-88b6-7b72315a362d';
-- 2015 Q20
UPDATE public.questions SET explanation = '［考点提炼］形容词语义辨析与主旨收束。
［精准定位］第六段末句：It''s that [20]: Talking to strangers can make you feel connected.
［命题解密］It''s that simple 为英语常见收束表达，意为“道理就这么简单：与陌生人交谈能让你产生人际连结感”。作者用极其精炼有力的短句总结全文，呼吁大家打破冷漠屏障。故 B 项 simple 准确。
［错项排除］A项 funny（滑稽好笑的）、C项 logical（符合逻辑的）与 D项 rare（罕见的）均破坏了该总结性短语的地道凝练语感。' WHERE id = 'f46135bc-4585-5fb0-8059-3c95a3d6e776';
-- 2015 Q31
UPDATE public.questions SET explanation = '［考点提炼］细节事实题与直接定位。
［精准定位］第一段第一句：Even in traditional offices, "the lingua franca of corporate America has gotten much more emotional and much more right-brained than it was 20 years ago," said Harvard Business School professor Nancy Koehn.
［命题解密］哈佛商学院历史学家南希·克恩明确指出，如今美国企业的办公通用语变得更加情感化（has gotten much more emotional）。故 D 项 more emotional 完全忠实于原文直接信息，正确答案为 D。
［错项排除］A项 less strategic、B项 less energetic 和 C项 more objective 均取自下文所列举的昔日词汇与新词对比（There were goals, strategies... but we didn''t talk about energy...），并非办公室语言整体演变趋势的准确概括。' WHERE id = 'bb75770c-ea12-5187-b82e-b343d3e7b433';
-- 2015 Q32
UPDATE public.questions SET explanation = '［考点提炼］细节理解题与原因深层剖析。
［精准定位］第二段第一至二句：Koehn pointed out that this new era of corporate vocabulary is very "team"-oriented — and not by coincidence. "Let''s not forget sports - in male-dominated corporate America, it''s still a big deal..."
［命题解密］克恩指出新时代企业词汇偏向“团队”绝非巧合，根源在于美国企业界深受男性喜爱的“体育文化（sports culture）”影响，CEO把自己视作教练（coach），把员工视作球队（team）。故 A 项 sports culture 正确。
［错项排除］B项（性别差异）虽提到 male-dominated，但它只是体育文化在企业盛行的社会背景，而非词汇直接渊源；C项（历史事件）和 D项（健美型高管）纯属无中生有误导。' WHERE id = 'a76cca03-1e01-5907-b7f6-1c444dd8dcac';
-- 2016 passage[0] (cloze)
UPDATE public.passages SET content = 'Happy people work differently. They''re more productive, more creative, and willing to take greater risks. And new research suggests that happiness might influence [1] firms work, too.

Companies located in places with happier people invest more, according to a recent research paper. [2], firms in happy places spend more on R&D (research and development). That''s because happiness is linked to the kind of longer-term thinking [3] for making investments for the future.

The researchers wanted to know if the [4] and inclination for risk-taking that come with happiness would [5] the way companies invested. So they compared U.S. cities'' average happiness [6] by Gallup polling with the investment activity of publicly traded firms in those areas. [7] enough, firms'' investment and R&D intensity were correlated with the happiness of the area in which they were [8].

But is it really happiness that''s linked to investment, or could something else about happier cities [9] why firms there spend more on R&D? To find out, the researchers controlled for various [10] that might make firms more likely to invest - like size, industry, and sales - and for indicators that a place was [11] to live in, like growth in wages or population. The link between happiness and investment generally [12] even after accounting for these things.

The correlation between happiness and investment was particularly strong for younger firms, which the authors [13] to “less codified decision making process” and the possible presence of “younger and less [14] managers who are more likely to be influenced by sentiment.” The relationship was [15] stronger in places where happiness was spread more [16]. Firms seem to invest more in places where most people are relatively happy, rather than in places with happiness inequality.

[17] this doesn''t prove that happiness causes firms to invest more or to take a longer-term view, the authors believe it at least [18] at that possibility. It''s not hard to imagine that local culture and sentiment would help [19] how executives think about the future. “It surely seems plausible that happy people would be more forward-thinking and creative and [20] R&D more than the average,” said one researcher.' WHERE id = '213fe984-2e5d-5623-b439-5ee7b27fdc20';
-- 2016 passage[3] (reading)
UPDATE public.passages SET content = 'That everyone''s too busy these days is a cliche. But one specific complaint is made especially mournfully: There''s never any time to read.

What makes the problem thornier is that the usual time-management techniques don''t seem sufficient. The web''s full of articles offering tips on making time to read: “Give up TV” or “Carry a book with you at all times.” But in my experience, using such methods to free up the odd 30 minutes doesn''t work. Sit down to read and the flywheel of work-related thoughts keeps spinning - or else you''re so exhausted that a challenging book''s the last thing you need. The modern mind, Tim Parks, a novelist and critic, writes, “is overwhelmingly inclined toward communication... It is not simply that one is interrupted; it is that one is actually inclined to interruption.” Deep reading requires not just time, but a special kind of time which can''t be obtained merely by becoming more efficient.

In fact, "becoming more efficient" is part of the problem.

Thinking of time as a resource to be maximised means you approach it instrumentally, judging any given moment as well spent only in so far as it advances progress toward some goal. Immersive reading, by contrast, depends on being willing to risk inefficiency, goallessness, even time-wasting. Try to slot it in as a to-do list item and you''ll manage only goal-focused reading - useful, sometimes, but not the most fulfilling kind. “The future comes at us like empty bottles along an unstoppable and nearly infinite conveyor belt,” writes Gary Eberle in his book Sacred Time, “and we feel a pressure to fill these different-sized bottles (days, hours, minutes) as they pass, for if they get by without being filled, we will have wasted them.” No mind-set could be worse for losing yourself in a book.

So what does work? Perhaps surprisingly, scheduling regular times for reading. You''d think this might fuel the efficiency mind-set, but in fact, Eberle notes, such ritualistic behaviour helps us “step outside time''s flow” into “soul time.” You could limit distractions by reading only physical books, or on single-purpose e-readers. “Carry a book with you at all times” can actually work, too - providing you dip in often enough, so that reading becomes the default state from which you temporarily surface to take care of business, before dropping back down. On a really good day, it no longer feels as if you''re “making time to read,” but just reading, and making time for everything else.' WHERE id = 'eb685298-efa5-52b9-ae98-d84c4c04f5e3';
-- 2016 Q32
UPDATE public.questions SET explanation = '［精准定位］根据题干中的 "empty bottles" metaphor 定位至第 4 段后半部分。
［解题思路］第 4 段引用 Gary Eberle 的话指出：“''The future comes at us like empty bottles along an unstoppable and nearly infinite conveyor belt,'' writes Gary Eberle in his book Sacred Time, ''and we feel a pressure to fill these different-sized bottles (days, hours, minutes) as they pass, for if they get by without being filled, we will have wasted them.''” 未来就像传送带上一排排等待灌满的空瓶子，人们感受到必须把每一小时、每一分钟都填满充实的焦虑压力，否则便视之为虚度光阴。选项 [B] make passing time fulfilling 准确对应 fill these different-sized bottles as they pass，故选 [B]。
［错项排除］[A] update their to-do lists（更新待办事项清单），前文指出把阅读塞进 to-do list 会破坏沉浸式阅读，但空瓶子比喻针对的是把流逝时间塞满的压力，而非更新清单本身；[C] carry their plans through（贯彻计划）偏离对时间填满的隐喻；[D] pursue carefree reading（追求无忧阅读）与充满紧迫感的功利时间观完全相反。' WHERE id = 'f26d82a8-185d-5285-8a4e-83952980f708';
-- 2016 Q33
UPDATE public.questions SET explanation = '［精准定位］根据题干中的 Eberle 和 scheduling regular times for reading 定位至第 5 段前两句。
［解题思路］第 5 段前两句指出：“So what does work? Perhaps surprisingly, scheduling regular times for reading. You''d think this might fuel the efficiency mind-set, but in fact, Eberle notes, such ritualistic behaviour helps us ''step outside time''s flow'' into ''soul time.''” 安排固定的阅读时间能够帮助人们从传送带般匆忙的时间流中脱离出来，进入宁静的“灵魂时间”，从而实现第 4 段所说的沉浸式阅读（Immersive reading）。选项 [D] achieve immersive reading（实现沉浸式阅读）是对进入不受干扰的阅读境界的高度概括，故为正确答案。
［错项排除］[A] encourage the efficiency mind-set（助长效率至上的心态），文中明确指出“You''d think this might fuel the efficiency mind-set, but in fact... helps us step outside...”，表示它打破了效率迷思；[B] develop online reading habits（培养网络阅读习惯），后文建议读实体书（physical books），而非网络阅读；[C] promote ritualistic reading（促进仪式化阅读），文中是说 ritualistic behavior 带来良好效果，手段是工具而非最终目标。' WHERE id = 'a5e2930d-fb7e-5174-80c9-aed5ea4a200e';
-- 2016 Q34
UPDATE public.questions SET explanation = '［精准定位］根据题干中的 "Carry a book with you at all times" can work 定位至第 5 段倒数第 2 句。
［解题思路］第 5 段指出：“''Carry a book with you at all times'' can actually work, too — providing you dip in often enough, so that reading becomes the default state from which you temporarily surface to take care of business, before dropping back down.” 前提是足够频繁地翻看，从而让“阅读”成为日常默认状态，处理杂务只是暂时浮出水面，随后又回到阅读之中。也就是说阅读已成为每天最核心要务（primary business），故选 [A]。
［错项排除］[B] all the daily business has been promptly dealt with（所有日常事务已被迅速处理完），原文是暂离阅读处理事务，而非先把事务处理完再读；[C] you are able to drop back to business after reading（阅读后能回到工作事务中），把原文句序与主次彻底颠倒，原文明确说明是处理事务之后“回到阅读之中（dropping back down [to reading]）”；[D] time can be evenly split for reading and business（时间可均分），文中强调以阅读为默认常态，并非平均分配。' WHERE id = 'e32a1401-e94a-51b1-b131-eaf043a9a1d3';
-- 2016 Q35
UPDATE public.questions SET explanation = '［精准定位］全文主旨题，通读全文把握核心脉络。
［解题思路］文章开篇提出核心问题：人们普遍抱怨“没有时间读书（There''s never any time to read）”。第 2–4 段剖析常规的时间管理方法为何无效，指出现代人的时间焦虑和效率陷阱；第 5 段则针对性地提出破局良方：“So what does work? Perhaps surprisingly, scheduling regular times for reading...”，最终达到“making time for everything else”的境界。整篇文章全方位围绕“如何才能真正挤出时间来读书”展开。选项 [B] How to Find Time to Read（如何找到时间读书）最为精准传神，故为正确答案。
［错项排除］[A] How to Enjoy Easy Reading（如何享受轻松阅读），本文重点探讨的是深度阅读的时间困境而非轻松阅读；[C] How to Set Reading Goals（如何设定阅读目标），第 4 段明确指出 goal-focused reading 容易损害沉浸体验，并非主旨；[D] How to Read Extensively（如何进行泛读），文章倡导的是 deep reading / immersive reading，而非泛读。' WHERE id = '36656550-8007-5be9-8cd5-17626e51d867';
-- 2017 Q20
UPDATE public.questions SET explanation = '［考点提炼］形容词对比与文章主旨收束。
［精准定位］...perhaps different enough to throw himself [19] a hobby or a passion project with the intensity usually reserved for [20] matters.
［解题思路］后文将业余爱好（a hobby or a passion project）与以往仅用于工作事务的专注强度进行对比，这里指通常留给“职业/工作（professional）”事务的心力强度，收束全文关于劳动与闲暇转换的讨论，故选[B]。
［错项排除］[A] technological（技术的）、[C] educational（教育的）与[D] interpersonal（人际的）均脱离了“职业工作 vs 业余爱好”的对比框架。' WHERE id = '02d7be36-110a-5aab-a0ae-46fdc7acc221';
-- 2017 Q22
UPDATE public.questions SET explanation = '［考点提炼］事实细节题（第二段）。
［解题思路］第二段第二句指出，申奥规划文件曾承诺奥运会遗产将把民众从沙发上拉起来积极锻炼（lever a nation of sport lovers away from their couches），并激励一代人（"inspire a generation" / 第3段 wanted to get more people doing sport）；但随后作者指出成年人每周参加运动的比例加速下滑，可见伦敦奥运并未成功促进大众体育参与（promote sport participation）。
［错项排除］[A]项曲解了文中人口更健康强壮的愿景；[B]项城市形象并非文章讨论的遗产指标；[C]项学校运动时间减半是现状而非奥运承诺的目标。' WHERE id = 'c6dd7f77-4390-5e92-81af-f2e9e60acbbb';
-- 2017 Q26
UPDATE public.questions SET explanation = '［考点提炼］事实细节题（第一段）。
［解题思路］第一段第二句引述 Jenny Radesky 指出："Tech is designed to really suck you in... and digital products are there to promote maximal engagement." 其中 suck you in 与 promote maximal engagement 直接等同于吸引并占用用户的注意力（absorb user attention）。
［错项排除］[B]提高工作效率、[C]简化日常事务、[D]改善人际关系均为日常宣传用语，与 Radesky 所批评的产品利用算法深度吸取用户注意力的负面机制相反。' WHERE id = 'a1d07ff3-9a6e-5541-8940-14eddaf52d9b';
-- 2017 Q37
UPDATE public.questions SET explanation = '［考点提炼］例证目的与隐喻理解题（第三、四段）。
［解题思路］第三段指出另一个令人担忧的问题是公共资金是否被用于火灾高发区的建设（building homes that are likely to be lost to a wildfire）；第四段 Moritz 进一步质疑并提出是否应该用“放大镜”审视资金花费的去向，并将其引导至低风险区域。这表明使用“放大镜”旨在更严格地审查和确保公共资金支出的安全性与合理性（guarantee safer spending of public funds）。
［错项排除］[A]与原文引导资金重定向的主张相反；[B]寻找无野火区域过于字面化；[C]为易发区募集更多资金与重定向至低风险区的主张背道而驰。' WHERE id = 'b48d13e9-b664-5847-aa89-bceb0e768776';
-- 2017 Q38
UPDATE public.questions SET explanation = '［考点提炼］观点细节题（第六、七段）。
［解题思路］第六段指出过去十年讨论只聚焦于气候变化；第七段 Moritz 明确指出：虽然气候是关键要素，但不应以牺牲该复杂问题中的其他所有因素为代价（it shouldn''t come at the expense of the rest of the equation）。这直接表明不能忽视其他因素（other factors should not be overlooked）。
［错项排除］[A]公开辩论尚未平息并非 Moritz 的重点；[B]野火观念转变已经发生与后文呼吁转变观念相悖；[D]消防条件正在改善与前文野火加剧的事实相悖。' WHERE id = 'f1cd8c5e-5a05-54f3-bf8c-670acdbdd8ee';
-- 2018 passage[4] (reading)
UPDATE public.passages SET content = 'To combat the trap of putting a premium on being busy, Cal Newport, author of Deep Work: Rules for Focused Success in a Distracted World, recommends building a habit of "deep work" - the ability to focus without distraction.

There are a number of approaches to mastering the art of deep work - be it lengthy retreats dedicated to a specific task; developing a daily ritual; or taking a "journalistic" approach to seizing moments of deep work when you can throughout the day. Whichever approach, the key is to determine your length of focus time and stick to it.

Newport also recommends "deep scheduling" to combat constant interruptions and get more done in less time. "At any given point, I should have deep work scheduled for roughly the next month. Once on the calendar, I protect this time like I would a doctor''s appointment or important meeting," he writes.

Another approach to getting more done in less time is to rethink how you prioritise your day - in particular how we craft our to-do lists. Tim Harford, author of Messy: The Power of Disorder to Transform Our Lives, points to a study in the early 1980s that divided undergraduates into two groups: some were advised to set out monthly goals and study activities; others were told to plan activities and goals in much more detail, day by day.

While the researchers assumed that the well-structured daily plans would be most effective when it came to the execution of tasks, they were wrong: the detailed daily plans demotivated students. Harford argues that inevitable distractions often render the daily to-do list ineffective, while leaving room for improvisation in such a list can reap the best results.

In order to make the most of our focus and energy, we also need to embrace downtime, or as Newport suggests, "be lazy".

"Idleness is not just a vacation, an indulgence or a vice; it is as indispensable to the brain as vitamin D is to the body...[idleness] is, paradoxically, necessary to getting any work done," he argues.

Srini Pillay, an assistant professor of psychiatry at Harvard Medical School, believes this counterintuitive link between downtime and productivity may be due to the way our brains operate. When our brains switch between being focused and unfocused on a task, they tend to be more efficient.

"What people don''t realise is that in order to complete these tasks they need to use both the focus and unfocus circuits in their brain," says Pillay.' WHERE id = '2c6e2fe1-9dd2-52a5-960d-5be0c5f625d3';
-- 2018 Q38
UPDATE public.questions SET explanation = '［考点提炼］作者观点题＋同义转换。
［解题思路］根据定位词 Newport 与 idleness 定位至第七段（引述段）：[idleness] is, paradoxically, necessary to getting any work done, he argues（闲暇看似矛盾，实则是完成任何工作所必需的）。necessary to getting any work done 意即“完成任何工作所必不可少的”。A项 an essential factor in accomplishing any work（完成任何工作中不可或缺的要素）是对原文的完美同义转换。
［错项排除］[B] an effective way to save time and energy（节省时间和精力的有效方式）偏离文意，闲暇旨在恢复精力而非单纯节约时间；[C] a major contributor to physical health（身体健康的主要贡献者）借比喻维生素D进行过度引申；[D] a desirable mental state for busy people（忙碌人群理想的心态）未触及“完成工作所必需”的实质。' WHERE id = 'cdc9d9fa-6558-5d2c-a4e2-3ba15b7be02f';
-- 2018 Q39
UPDATE public.questions SET explanation = '［考点提炼］事实细节题＋同义改写。
［解题思路］根据定位词 Pillay 与 shift between being focused and unfocused 定位至第八段第二句：When our brains switch between being focused and unfocused on a task, they tend to be more efficient（当我们的大脑在一项任务上于专注与非专注状态之间切换时，往往效率更高）。B项 can bring about greater efficiency（能够带来更高的效率）是对 tend to be more efficient 的直接同义置换。
［错项排除］[A] can result in psychological well-being（能够带来心理健康）无中生有；[C] is aimed at better balance in work（旨在更好平衡工作）并非大脑机制的目标；[D] is driven by task urgency（受任务紧迫性驱动）偏离原文。' WHERE id = 'fb4a2a25-db56-55dc-94ea-a09a314a765c';
-- 2018 Q40
UPDATE public.questions SET explanation = '［考点提炼］主旨大意题＋篇章宏观归纳。
［解题思路］通读全文，文章开篇提出 Cal Newport 克服盲目忙碌陷阱的“深度工作”理念，第二段阐述掌握深度工作的多种途径（approaches to mastering the art of deep work），第三段提出高效日程规划以在更少时间内完成更多工作（get more done in less time），第四段探讨每日任务清单的灵活安排（Another approach to getting more done in less time），第五段以实验印证过于死板的日程会削弱学生动力；第六至九段则进一步阐明留出闲暇与专注/非专注脑回路切换对提升产出效率的关键作用。全文核心贯穿于如何在较少时间内完成更多工作的科学方法与途径。D项 approaches to getting more done in less time（在更少时间内完成更多工作的方法）为文章最佳主旨概括。
［错项排除］[A] the key to eliminating distractions（消除干扰的关键）与[B] the cause of the lack of focus time（缺乏专注时间的原因）以及[C] ways to relieve the tension of busy life（缓解忙碌生活紧张感的方法）均仅涉及局部细节或片面解读，无法涵盖整篇探讨工作效能方法的宏观架构。' WHERE id = 'fdcc858c-5c03-5f7e-8094-a1354832446b';
-- 2019 Q23
UPDATE public.questions SET explanation = '［考点提炼］观点态度题（考查学者Vaish对内疚感反思根源的认识）。

［解题思路］第二段中Vaish指出对内疚感的新反思属于心理学领域保护人们免受负面情绪影响趋势的一部分，她指出情绪并非非黑即白，而是取决于具体语境：emotions aren''t binary — feelings that may be advantageous in one context may be harmful in another（情绪并非二元对立——在某种语境下有益的情绪在另一种语境下可能有害）。同一种情绪在不同语境下可发挥相反作用，［D］an emotion can play opposing roles 准确同义转换了 advantageous in one context / harmful in another，故选［D］。

［错项排除］［A］情绪与语境无关与原文depending on the context直接相悖；［B］强调情绪具社会建设性仅局限于正面，遗漏了有益与无益的辩证对比；［C］情绪稳定有利于健康偏离文本论述核心。' WHERE id = '9450d67d-b64f-5cc0-a2ab-d8848e385878';
-- 2019 Q24
UPDATE public.questions SET explanation = '［考点提炼］事实细节题（考查学者Malti关于合作与分享行为的研究发现）。

［解题思路］第四段③句明确指出：Malti and others have shown that guilt and sympathy may represent different pathways to cooperation and sharing（马尔蒂等人指出，内疚感和同情心代表了通向合作与分享的不同路径）。有的孩子靠同情，有的孩子靠内疚，两者皆可激发合作与分享行为，［B］can result from either sympathy or guilt切中文意，故选［B］。

［错项排除］［A］纠正情绪缺陷与后文互补代偿机制不符；［C］带来情感满足颠倒了因果逻辑；［D］冲动行为的产物与理性道德情感的引导相反。' WHERE id = '07008f2f-b765-53dc-babe-bb3b9c49502b';
-- 2019 Q25
UPDATE public.questions SET explanation = '［考点提炼］词义句意题（考查代词语境与词汇含义推断）。

［解题思路］划线词位于第五段②句：In a 2014 study, for example, Malti looked at 244 children... she rated each child''s overall sympathy level and his or her tendency to feel negative emotions after moral transgressions（马尔蒂评估了孩子整体的同情心水平及其在面临道德越轨行为后的负面情绪倾向）。后文第六段末句进一步通过孩子所犯错误解释道：guilt tells them, we caused harm and we feel regret（内疚感告诉他们：我们造成了伤害，我们感到后悔）。造成伤害、引发违背道德良知的行为即为道德越轨/过错，transgressions在此即指wrongdoings（违法行为，过失，过错），故选［D］。

［错项排除］［A］teachings（教导）；［B］discussions（讨论）；［C］restrictions（限制），均与道德过失行为的含义相差甚远。' WHERE id = 'd1b17cb7-1d97-5e7b-bd6a-02a2719a7a87';
-- 2020 Q3
UPDATE public.questions SET explanation = '［考点提炼］上下文语义逻辑。
［解题思路］上段提到“定义做好父母”很难（也即：人们即使想做好父母，也可能无所适从），本段①②句指出“还有一种稍容易的父母：耐心的父母。所有年龄段的孩子都能从有耐心的养育方式受益”。很明显，本段退而求其次，向人们介绍一种确定性的好父母特质“耐心”。[A]Fortunately既体现tricky VS easier间对比逻辑，又契合论述的情感色彩：虽难界定，但幸好还有某种标准可依。
［错项排除］[B]Occasionally（= sometimes but not often）表频度，暗示“耐心的父母”只偶尔存在，与作者意图“介绍一种确定的好父母标准”不符。[C]Accordingly可表因果（=therefore），如The text was too long and the editor accordingly cut it by 20%.（文稿过长，因此编辑删减了五分之一。），还可表方式（=correspondingly），如We have to discover what his plans are and act accordingly.（我们必须弄清他有什么打算并采取相应行动。）；上文既非空格所在句的原因，也非其应该参照的情况，故排除。[D]Eventually用法有二：一为客观引出情况或过程的最终结局，二为影射某情况历经多时或万难总算达成，均表时间，而空格句并非最终结果。' WHERE id = '6e46515e-0516-551a-b3e2-d3798ae30a20';
-- 2020 Q6
UPDATE public.questions SET explanation = '［考点提炼］句内语义+名词辨析。
［解题思路］结合上题分析可知，this is no easy大意为“耐心不易达成”，而空格词为表语，故应与主语this（代指to be patient，表示“目标”）属于同类且互相呼应，[B]task尤指艰巨或令人厌烦的任务、工作，与“目标”相吻合，同时符合上下文文意，即：变得耐心并非易事。
［错项排除］[A]暗指“耐心未必能真正解决问题”，与②句“所有孩子都能受益于耐心的养育”矛盾；
[C]暗指“人们做出朝耐心努力这一选择”有一定困难，但文意实为“耐心本身不易达成”，而非“（外界因素等导致）选择难做”。[D]access表示“获得/使用/接近（某事/某地/某人）的能力、机会或权利”，常以介词to引出动作施加的对象，如have easy access to information（很容易获取信息）；故从结构上看，没有this is no easy access的说法，正确形式应为(there is) no easy access to sth；从语义上看，access的对象一般为资源、设施、场所、特定人物等，而“变耐心”为目标、任务，两者无法搭配。' WHERE id = '5f36eedb-a288-53b6-b2f0-70d97ae3bff4';
-- 2020 Q7
UPDATE public.questions SET explanation = '［考点提炼］句内语义逻辑+形容词辨析。
［解题思路］maintain a style框定父母在疲惫而沮丧时无法做到的事情，空格词与composed（沉着的）并列，而选项中同属正面、与“耐心”相关的只有[A]tolerant。
［错项排除］干扰项均无法与composed构成并列关系，脱离“耐心”语义场，具体来看，[B]formal用于说明穿着、言语、行为等适合正式或重要场合，而文中育儿行为不涉及正式或重要场合。formal还用于说明教育或培训是“在学校获得的（而非个人实践所得）、正规的”，如She didn''t have any formal dance training.（她没受过任何正规的舞蹈训练。），但文中空格词限定的是父母育儿方式/姿态（style），而非孩子所受教导。[C]rigid利用其表面义“严格”干扰，但该词实为负面导向，用于说明法律或制度僵死不变从而过于严格，当说明“人”时，意为“古板、头脑僵化”，不合文意。[D]critical同样利用“严格出教育”这一常见认知干扰，但该词修饰名词、作“批评的”讲时，后接“含批评内容的载体”，如critical comments/articles（批判性的评论/文章）；critical还表“有判断力的”，此时可接“方式、方法”，但此义侧重“思考与审慎能力”，与“耐心育儿”并无关联。·词汇注释与难句分析·
① parenting [ˈpeərəntɪŋ]n. 养育，抚养② rule-following [ruːl ˈfɒləʊɪŋ]adj. 遵守规则的③ sibling [ˈsɪblɪŋ]n. 兄弟姐妹④ composed [kəmˈpəʊzd]adj. 镇静的，平静的，沉着的But defining what it means to be a good parent is undoubtedly very tricky，particularly since children respond differently to the same style of parenting.
【结构切分】[But defining what it means to be a good parent is undoubtedly very tricky]（主句），[particularly since children respond differently to the same style of parenting]（原因状语从句）。' WHERE id = 'dcaecf51-171f-514a-bf87-7eb6e77cefd3';
-- 2020 Q9
UPDATE public.questions SET explanation = '［考点提炼］上下文语义+形容词辨析。
［解题思路］“the + 形容词”表示“…的事情”，冒号提示其是对随后“父母失去耐心的具体表现”的概括性评价，而上句“你只是凡人，孩子有时会逼得人发脾气”传达作者态度：这些不耐心的表现是人在情急下的正常反应，在所难免，情有可原，故[D]inevitable符合文意。
［错项排除］And then...happens表明①②句间为因果顺承关系，①句“孩子有时会把人逼得有些过头”这一情况为②句“父母失去耐心”提供了前提，且作者暗示两件事接连发生、在所难免。[A]mysterious、[B]illogical皆与文章所表达的“理所当然”之意相，故排除；the suspicious表示“可疑的人/事”，与犯罪或欺诈相关，脱离上下文语境，排除[C]。' WHERE id = 'c5b973f8-5cd5-5890-acdd-3372b098b045';
-- 2020 Q12
UPDATE public.questions SET explanation = '［考点提炼］上下文语义+副词辨析。
［解题思路］空格句先让步承认（even though）“这种情况很常见”（it回指上文“父母失去耐心而发怒”），随后转折引出建议“父母应记住…….（it''s important to keep in mind）”，下句阐述发怒行为的消极后果（do damage）。可知本段主旨为“父母向孩子发怒造成危害”，段首逻辑词应在上下段之间起转折过渡作用，传达“这一行为虽情有可原、谁都难免经历，但仍需警醒其会造成危害”之意，[C]正确。
［错项排除］[A]通常用于总结前文，其前后语义应保持一致，此处不符合原文逻辑。[B]、[D]均含转折意味，但instead侧重强调“后者替代前者（而发生）”，如：Geoff didn''t study law. Instead，he decided to become an actor.（杰夫没学法律，相反，他决定当演员。）；otherwise侧重强调“某人不照做某事、或某情况不发生/不同的后果”，两项均不符合文中“从探讨事物的正面转向探讨其负面（合理性→危害性）”，可排除。' WHERE id = '5d59f312-9eb0-5b97-99df-5f892823a4c8';
-- 2020 Q17
UPDATE public.questions SET explanation = '［考点提炼］上下文语义。
［解题思路］In fact（确切地说）提示④句在③句基础上说明“控制情绪”更重要/具体的作用，空格后stress呼应第二至四段所述父母发怒的诱因“压力、疲劳（exhausted、frustrated、fatigue）”，表明空格句所述“在被压力时调节/控制情绪的能力”能解决前文所述问题“父母在疲惫时易向孩子发怒”，空格词应表“影响/困扰”之意，be confronted by sth.指“面对（有威胁或难处理的事物）”，故[D]正确。
［错项排除］[A]、[C]均歪曲了压力对父母的影响，文中只提到压力会使父母无法控制情绪，并未提到压力会使父母思维混乱、虚实不分。[B]暗含“父母已被压力击溃、无可救药”之意，与文中建议的隐含义“父母可通过控制情绪避免被压力影响”相。·词汇注释与难句分析·
① consistently [kənˈsɪstəntli]adv. 一贯地；始终② inadvertently [ˌɪnədˈvɜːtəntli]adv. 无意地，不经意地③ model [ˈmɒdl]v. 塑造④ regulate [ˈreɡjuleɪt]v. 调节，规定；控制' WHERE id = '76df95d5-a5ad-5b2e-8695-95c5001c4199';
-- 2020 Q21
UPDATE public.questions SET explanation = '［精准定位］首段末句介绍奎因等的研究目标（tested whether）：测试老鼠是否能察觉机器鼠发出的社交信号，[A]正确。
［命题解密］“题干+[A]”同义改写首段末句，if...pickup...from non-living rats替换whether.. detect...from robotic rats/non-living beings。
[B]、[C]均利用①句已知信息干扰，[B]改写identify friends...and enemies，但“接收社交信号以分辨敌友”是老鼠已被证实的能力，而非待证实的能力；[C]将need to be highly attuned to social signals断章取义为“老鼠对社交信号不够敏感”，并在此基础上臆断研究者想要观察是否可通过特殊训练提升其技能（attain...through special training）。[D]将研究目标“观察老鼠能否接收/识别（detect）机器鼠（其相似物）发出的社交信息”窜改为完全反向的“观察老鼠是否会向其发出（send out）信息”。
［技巧总结］本题就首段命制事实题，意在考查新研究的目的，要求考生辨别“研究背景/已知信息”与“研究目标/待验证信息”。可采用思路：先由②句To find out if this extends to...梳理首段逻辑“①句先介绍已知信息，②句引出研究者在已知信息基础之上的进一步研究”，从而明确“②句为正确项来源，且①句很可能被用于设置干扰”。随后重点分析②句，可进一步锁定正确项来源whether rats can detect social signals from robotic rats，并结合前半句得知robotic rats代表non-living beings，从而确定
[A]正确。其余选项或利用①句背景信息干扰（[B]、[C]），或窜改研究目标（[D]）。
They housed eight adult rats with two types研究人员让8只成年鼠与2只不同类型of robotic rat—one social and one asocial—for four的机器鼠一一只爱社交，一只不合群days. The robot rats were quite minimalist,共处一室4天。这两只机器鼠外形相当简约resembling a chunkier version of a computer mouse抽象，就像矮胖版的电脑鼠标，靠轮子四处with wheels to move around and colourful markings移动，带有鲜艳的标记。Ⅲl During the experiment, the social robot rat在试验过程中，社交机器鼠跟随生物鼠followed the living rats around, played with the same们四处走动，玩同样的玩具，还会打开笼门toys, and opened cage doors to let trapped rats escape.让被困老鼠逃脱。在此期间，非社交机器鼠②Meanwhile, the asocial robot simply moved forwards则只是前后、左右移动。and backwards and side to side.' WHERE id = 'c1e6378a-6818-577c-a6ae-2116d521addd';
-- 2020 Q22
UPDATE public.questions SET explanation = '［精准定位］由the asocial robot、during the experiment定位至第三段末句。该句介绍试验过程中非社交机器鼠的表现：只是前后、左右移动。[D]正确。
［命题解密］正确项[D]同义改写第三段末句，alone点明了句中simply一词暗含的对比之意：与社交机器鼠相反，非社交机器鼠不与老鼠们同游同玩儿，而是独自前后左右移动。
[A]、[B]、[C]均张冠李戴，利用第三段首句社交机器鼠（the social robot）的表现捏造干扰，并非题目所问“非社交机器鼠（the asocial robot）行为”，[A]更是将“社交机器鼠跟随生物鼠走动”窜改为原文并未出现的信息“非社交机器鼠跟随社交机器鼠走动”。
［技巧总结］本题考查试验过程中某一对象（非社交机器鼠）的表现，要求考生辨别不同对象的行为，避免张冠李戴。具体来说，可借助During the experiment，the social robot rat...Meanwhile，the asocial robot simply...以及关键词对social VS asocial明确“社交鼠”和“非社交鼠”的行为截然不同，锁定②句信息，并警惕①句陷阱。' WHERE id = 'b1d0d12c-8fa4-5b57-95f3-ac7bfd0206ae';
-- 2020 Q23
UPDATE public.questions SET explanation = '［精准定位］第四段末句指出老鼠更倾向于解救社交机器鼠；第五段进一步分析指出，老鼠可能与社交机器鼠建立起了情感联结，希望将来自己被困时也能得到相应的回报，所以愿意施救，［B］正确。
［命题解密］正确项［B］同义改写第五段末句 wanting the robot to return the favour when they get trapped。
［错项排除］［A］将第四段①句 release them by pressing a lever 断章取义为老鼠想实践一种新的逃跑方法，但“按下控制杆”是老鼠帮助机器鼠脱困的方式，不是施救的原因；［C］将④句 displayed behaviours...（社交机器鼠曾表现出集体探险及游戏行为）曲解为“老鼠想要展示自己的智力”；［D］将④句 exploring and playing（老鼠先前曾与机器鼠共同游戏）曲解为“老鼠如今之所以营救机器鼠是因为认为这是个有趣的游戏”。
［技巧总结］本题针对“试验结果（老鼠解救社交机器鼠）的原因分析”命题。第五段①句 This suggests 开启分析，②③句以因果线索串联起施救逻辑：先前社交机器鼠参与老鼠的集体活动→老鼠与其建立更深情感联结→老鼠寄希望于机器鼠将来报答自己，因此更愿施救。' WHERE id = 'c4d607ff-98d2-5936-9acb-8f819fa8f6cb';
-- 2020 Q25
UPDATE public.questions SET explanation = '［精准定位］第六段①句指出，老鼠与设计简陋的机器鼠交朋友的行为出人意料；②③句解释：研究人员原以为要给机器鼠加上可活动的头和尾巴等，以使其更像老鼠，但事实证明这并不必要。第七段得出结论：老鼠对社交信号非常敏感，即使这些信号来自简单的机器鼠。可见，老鼠对社交信号的敏感超出研究者预期，[D]正确。
［命题解密］[D]正确解读第六段The readiness of the rats..was surprising...及第七段how sensitive...are to social cues，even when...传达的研究人员的“惊讶之情”。
[A]夸大其词：文中只提及“老鼠愿意与机器鼠交朋友”，由此无法推知“老鼠擅长适应新环境”。
[B]捏造比较：文中只提及老鼠对社交信号高度敏感，并未涉及与其他动物的比较。[C]与第七段②句相悖：“老鼠与儿童均可察觉到机器人发出的社交信号”表明“老鼠与儿童在社交方面表现相同”。
［技巧总结］根据题目位置（最后一题）及各选项内容（关于“老鼠”的论断）可知本题很可能考查研究结论。解题时需先把握核心发现，再确认具体细节：首先从首尾段快速提取核心信息：老鼠对社交信号十分敏感，即便这些信号来自简单的机器鼠，大致确定[D]为正确项。随后确认细节：[D]涉及研究人员对研究的预期，可定位至第六段首句surprising，并确认选项正确。而“老鼠适应新环境的能力”、“老鼠社交能力与其他动物的比较”文中均未提及，可排除[A]、[B]；[C]与第七段②句相悖，也错误。' WHERE id = '5bd17948-2aa2-5235-871a-60c49cf03a83';
-- 2020 Q27
UPDATE public.questions SET explanation = '［精准定位］第三段首句总领整段：CEO必须拥有更多的技能。随后各句以CEOs must...、They also...、Then...、Plus...、Beyond this...分述CEO所需的技能。其中④句指出“美国大公司的全球化程度空前，胜任CEO需要异常广博的知识”，由此可知，CEO需要经营更加全球化的公司。[D]正确。
［命题解密］[D]operate more globalized companies对应句CEO的职责之一To lead in that system（其中that system指向④句信息“供应链遍布更多国家的全球化程度空前的大公司”）。
[A]、[C]分别利用have a good sense of、tech companies设置干扰，[A]将原文“金融市场意识”曲解为“团队意识”，[C]将原文“大公司在向科技公司转变（暗示CEO需具备领导科技公司的技能）”曲解为“CEO与科技公司建立更紧密的联系”。[B]由文中financial（指向“金融市场”）捏造出动词finance（给……提供资金），且“研发”在文中无据可依。
［技巧总结］由题干关键词不难定位到第三段，借表列举的逻辑词（also、Then、Plus、Beyond this）以及相关近义表述（①句概述词many more skills引领后文a good sense of...、better...skills、requires knowledge、have to do等具体技能/知识）可推知该段呈总分结构。可将各项与②至⑥句分述的各项技能/职责逐一比对：原文未涉及“团队”“研发”，但出现了“科技公司”和“全球化公司”，故需理清CEO与两类公司的逻辑关系，[D]“（CEO）经营全球化公司”近义对应⑥句“（CEO）领导全球化公司”，故该项正确，而[C]暗示CEO领导的公司本身并非科技公司，与⑤句“CEO领导的美国大公司正逐渐成为科技公司”相悖。' WHERE id = 'b0c2b5ba-7aff-5f89-9dfc-fea2d1d94719';
-- 2020 Q30
UPDATE public.questions SET explanation = '［精准定位］本文首段引人“CEO高薪”现象，第二至末段论述该现象的合理性：其中第二、三段指出CEO高薪与其技能知识相匹配，第四、五段指出CEO高薪不是对公司的价值掠夺，反而能提升公司价值。综合可知，本文主要论述CEO高薪的合理性，[A]最贴合本文主旨。
［命题解密］[A]是基于各段主旨句/关键词（首段CEO pay has gone up；第二段limited CEO talent in a world...、CEOs really have upped their game...；第三段Today''s CEO...have many more skills...；第四段it is in the broader corporate interest to recruit top candidates...；第五段high CEO pay is not... depredation at the expense of the rest of the company、build up corporate value）的高度提炼与总结。
[B]只涵盖文中陈述事实“CEO薪酬近几十年来大幅上涨”，未触及文章写作意图（作者立场观点）“为CEO高薪作辩护”。[C]、[D]由第三段“如今CEO需具备更多技能和知识”分别臆断出“当今CEO面临更多挑战”“CEO职责复杂，很难界定”，两项均未涉及文章关注点“CEO的薪酬”。
［技巧总结］文章主旨题的解题步骤大体为：1.借开篇句群/段落（或第二段开头）确定文章话题；2.借复现、近义、反义等语义手段以及并列、转折、总分等逻辑衔接词串联各段大意，梳理文章脉络结构，总结文章主旨；3.带着文章话题主旨比对各项，要注意排除以偏概全、过于笼统、增添枝叶等含有原文部分内容的选项，确定与原文主旨最贴近的选项。具体看本题，由开篇段落可知文章话题为“CEO高薪”，故可排除与薪酬无关的[C]、[D]，串联各段大意（见本题“精准定位”）可知本文立场“CEO高薪有其合理性”，[B]仅涉及薪酬今昔变化，未表达任何论点，[A]以判断句式直陈论点，符合本文立意。' WHERE id = '7573126d-aef7-54fb-bfff-23729e12c3c1';
-- 2020 Q31
UPDATE public.questions SET explanation = '［精准定位］第二段末句明确指出：马德里“清洁空气区”的未来看起来很不明朗。也即，它的命运尚未确定。故[D]正确。
［命题解密］正确项[D]fate...yet to be decided同义改写第二段末句future looks uncertain。
[A]根据第一段末句“市议会暂停实施”第二段首句“市长反对”捏造出其反对理由“（实施）效果不确定”，但很明显与第二段①句despite所引出的客观事实 its success in improving air quality（‘清洁空气区’在改善空气质量方面取得良好效果）相悖；[C]则根据第一段②句“暂停实施”第二段①句客观事实“在改善空气质量方面取得良好效果”糅杂臆造出“清洁空气区”效果良好，市议会不应该暂停实施，理应得到更严厉的执行”，且由第二段②句“市政府中止实施VS法官责令恢复”可知“马德里清洁空气区”面临的问题并非“执行不力”，而是“能否继续实施”。[B]将反对“清洁空气区”的主体由第二段①句中的“市长”偷换为②句中的“法官”，而②句明确指出“法官推翻市议会决定，并责令恢复收取罚金（也即，支持“清洁空气区”）。
［技巧总结］Which型事实细节题的典型解题思路是“利用选项关键词回文对应一比对判别对错”。如本题，首先根据试题命制顺序按照文章由前至后原则以及题干关键词将范围限定至第一、二段，再根据选项关键词（核心名词/动词）将各选项回文定位：[A]effects对应第二段①句its success in improving、[B]a judge对应第二段②句，[C]tougher enforcement对应第一段②句suspended enforcement，[D]Its fate对应第二段③句the zone''s future。随后一一比对发现，[D]为原文同义转述。' WHERE id = '90261b64-0cbf-5416-8616-78fe1f6fd83c';
-- 2020 Q33
UPDATE public.questions SET explanation = '［精准定位］第四段③句指出：如果2021年将超低排放新区扩展至南北环路，一定会激起众多即将受影响的汽车车主的强烈反对，故[A]正确。
［命题解密］正确项[A]arouse strong resistance同义改写③句spark intense opposition。
[B]将第四段③句“萨迪克·汗选举成功将扩展Ulez”颠倒为“扩展Ulez将使萨迪克·汗选举成功”。[C]将第五段③至句所述Ulez的作用“改善空气质量、保障居民生命健康”偷换为“改善交通状况”。[D]将第四段③句Ulez扩展的影响对象“汽车车主”偷换为“汽车生产商”，进而得出Ulez扩展阻碍汽车的生产制造。
［技巧总结］本题考查作者针对Ulez扩展后果/影响的看法。解题关键在利用关键词定位，再于定位句中借助观点表达、因果表达以锁定正确答案。如本题，可先借助题干中extension、Ulez定位到第四段③句，随后借助句内观点表达it is sure to、因果表达spark intense opposition即可锁定正确答案[A]。
But mayors and councilors can only do so但是，针对这么一个影响范围远超一城much about a problem that is far bigger than any one city一镇的（空气污染）问题，市长们、议员们所or town. They are acting because national能做的也就仅此而已。他们之所以在行动，governments—Britain’s and others across Europe have是因为各国政府一英国以及所有其他欧failed to do so.洲国家的政府一未能做出行动。' WHERE id = '2598625d-36e8-5343-a627-a6b80c073e95';
-- 2020 Q34
UPDATE public.questions SET explanation = '［精准定位］第六段②句指出：市长们、市议员们（They的指代内容）之所以在采取行动（各种市级治理措施）是因为国家政府未能采取行动（so指代内容）。可见，作者认为本该由国家政府解决问题，[D]正确。
［命题解密］正确项+题干是对national governments... have failed to do so（failed意为“没有做，未做（应做的事情）”）的正确解读。
[A]将第五段③句中所涉人物主体Local（officials）、residents语义糅杂为local residents，且将居民作为空气污染治理的受益对象偷换为问题解决者。[B]、[C]均截取第六段①句mayors and councilors，但两者均为当前正在采取措施解决问题的主体，与题干所问“谁应该去解决问题却又没去解决”不符。
［技巧总结］常规思路：语义转折、取舍处与全文主旨息息相关，常作为命题焦点出现，所以必须重视but/however/yet等转折词后的内容，对于not...but.../rather than/instead of等取舍结构，则须重点明辨“取”的内容（“舍”常为干扰来源之一）。第六段①句以But与前文形成转折，强调作者否定态度：问题涉及范围过大而市长与市议员能力有限（only...so much），可推知真正主体应在能力上强大于市长、市议员，由此可初步选定[D]。②句主、从句A are acting because B... have failed to do so构成语义对比：“A=They=mayors and councils”正在采取行动VS“B=national governments”本该采取行动却没采取行动，确认[D]正确。非常规思路：四个选项指向不同主体，但全文尤其第六段首句中mayors and councilors表示两个主体处于并列平行状态（两者行为态度大体一致），故可将与之相关的[B]、[C]两项同时排除，最后再在[A]、[D]中做抉择，无论是借由第六段首句“空气污染问题并非局域性问题而是全局性问题”还是借由文意关注核心“污浊空气治理政策”可舍指向区域性基层人民的[A]而取指向全国性国家政府层面的[D]。' WHERE id = 'bcd0abf6-fa6c-56a1-8a2a-e4f23522581d';
-- 2021 Q8
UPDATE public.questions SET explanation = '［考点提炼］句内语义+动词辨析。
［解题思路］空格句指出，司机们根据其行程所用时间______ 或受到惩罚（_________or punished）。由上句分析可知，这一措施有助于解决“公交车晚点”的问题，即“根据其行程所用时间对司机进行______或惩罚”有利于提高准点率，空格词应与punished语义相对或类似，[C]rewarded表示“奖励，奖赏”，可有效激励司机提高准点率，故正确。
［错项排除］[A]hired（雇用；聘用）、[B]trained（训练；教育）与[D]grouped（使成群；成组）均无法与空格句中 or“（引出另一种可能性）或者；还是”所提示的对立奖惩并列结构（与 punished“惩罚”并列，体现激励准点）相契合，故均排除。' WHERE id = '72642469-9506-5ee8-a2e7-f24c61b63e9a';
-- 2022 Q10
UPDATE public.questions SET explanation = '［考点提炼］句内语义+上下文语义。
［解题思路］空格句指出，取决于你的“______”和“生活方式”，这可能意味着要减少花在“看电视”或“听音乐”上的时间。句内分析：your______ and your lifestyle 应能涵盖 watching television or listening to music 等活动。句间关联：空格句中 that 指代上句,watching television or listening to music 属于 day-to-day activities and some things you really enjoy,即 your______ and your lifestyle 应同样能体现 day-to-day activities and some things you really enjoy。综上，your______ and your lifestyle 应表示“兴趣爱好以及生活方式”,[B]interests正确。
［错项排除］[A]relations（关系；亲属）、[C]memories（记忆力；回忆）与[D]skills（技术；技能）均既无法涵盖前文所举“看电视”“听音乐”等休闲活动，又无法体现上句的“日常活动和喜欢之事”，故均可排除。' WHERE id = 'f93e8a8d-a351-5994-918c-4e5bd814357d';
-- 2022 Q18
UPDATE public.questions SET explanation = '［考点提炼］上下文语义。
［解题思路］末段①句指出，时间是有限的。②句（空格句）指出，年龄越大，时间似乎流逝得________。③句以We need to...顺而提出建议：确定活动的优先次序，将大部分时间花在我们真正要做的事情上。联系全文可知，末段进行升华，提醒读者时间有限、光阴飞逝，应将精力集中于优先事项。故空格词应表示“更快地”，[D]quicker正确。
［错项排除］[A]duller（更枯燥的；更无趣的）、[B]harder（更艰难的；更费力的）与[C]quieter（更安静的）虽均在一定程度上符合人们“年老后生活归于平淡或艰难”的刻板印象，但均无法与后句“时间有限、应优先投入热爱之事（Time is finite... use it as carefully as we can）”构成紧迫感顺承，故排除。' WHERE id = '925ed4e6-6a76-56ba-badc-b0b33c7bfc25';
-- 2022 Q25
UPDATE public.questions SET explanation = '［精准定位］约翰•布伦克尔和朱莉•斯坦顿分别出自末段和第五段。由第五段可知，朱莉•斯坦顿是一位学者，她对再生产品抱有怀疑态度，认为再生产品可能很难被市场接受（其市场前景可能并不好），而且再生农业对再生产品的改良作用也微乎其微。由末段可知，约翰•布伦克尔是Egg Innovations公司的总裁（暗示其代表的是蛋品生产商），而且他的言论（“年轻人很关心地球，他们正在改变食品供应链”，暗示年轻人更乐意购买环境友好型食品）与末段首句蛋品行业的看法（“那些为散养、非转基因等食品标签买单的消费者也会更乐意为可持续性买单”）本质上是一致的，均强调再生鸡蛋的市场前景：会吸引那些具有气候/环境意识的消费者。综上可知，二人对再生产品的市场前景持不同态度，［A］正确。
［命题解密］正确项［A］可以涵盖斯坦顿对再生产品市场前景的描述（第五段的could be a hard sell）以及末段布伦克尔/蛋品行业对再生鸡蛋市场前景的描述（the same consumers... will embrace sustainability、shoppers wanting to... protect the environment、really care about the planet）。
［B］源自第五段中斯坦顿的看法“再生产品的概念很难快速定义（暗示其定义比较复杂）”，但末段布伦克尔言论中并未涉及对再生产品的定义，而且文中也未提到蛋品行业在这方面的看法，故排除该项。
［C］源自第五段中斯坦顿的看法“再生农业技术对再生产品的改良作用微乎其微（尽管一些生产商宣称其鸡蛋含有更多蛋白质）”，但据此无法推知其他生产商或整个蛋品行业对再生鸡蛋营养价值的看法，而且末段布伦克尔的言论中并未谈论再生鸡蛋的营养价值，故也可排除该项。［D］在文中无据可依。
［技巧总结］题干中的would（也许；会）表示推测，表明本题为推理判断题。解题思路为：先找到与两个人物相关的句群或段落，然后根据人物的身份和言论信息解读人物的观点态度，最后比对两人的观点态度，推断出两人的分歧点。解题的主要难点是把握布伦克尔的观点态度，可结合其身份信息（蛋品生产商）以及全文主旨（蛋品行业/生产商看好再生鸡蛋的市场前景）推断出其言论暗含的观点态度。' WHERE id = '78ce4df8-06a5-5f14-8cfd-1d1dc2853f9a';
-- 2022 Q32
UPDATE public.questions SET explanation = '［精准定位］根据题干关键词 The 2019 study 定位到第三段。该段①句引用 2019 年针对黑暗模式展开的一项涵盖 5.3 万个产品页面和 1.1 万个网站的研究，说明“大约有十分之一的页面或网站运用了黑暗设计手法”；②句紧接着明确问题“尽管黑暗模式广泛存在（widely prevalent），却仍未被充分了解”；③句针对该问题提议各大组织领导了解并避免运用黑暗模式。可见，文中借该项研究说明黑暗模式“大量运用/普遍存在”，进而引出相关建议，［D］正确。
［命题解密］“题干 + ［D］”是对第三段①②句的正确推导，strong presence 不仅概括①句 53,000 product pages and 11,000 websites... one in 10 employs these design practices，而且契合②句 widely prevalent。
［错项排除］［A］由第三段末 avoid the gray areas they engender 反推而来；［B］揭示用户接口的复杂操纵特征与［C］说明商业利益驱动的策略设计均仅重述前两段提及的黑暗模式表象特征，三项均非本文引用 2019 年研究所说明的核心事实，也与写作目的不符。
［技巧总结］本题就引用论证处命制写作目的题，须注意引用的目的通常是引出主题或论证观点。解答本题时，可根据论据（2019 年关于黑暗模式的研究）本身的数据占比锁定［D］，再通过对比下文总结概括性内容（widely prevalent）确认［D］准确无误。' WHERE id = '450bd174-55c4-54ed-8c25-255d10b3b15b';
-- 2023 passage[2] (reading)
UPDATE public.passages SET content = 'It''s easy to dismiss as absurd the federal government''s ideas for plugging the chronic funding gap of our national parks. Can anyone really think it''s a good idea to allow Amazon deliveries to your tent in Yosemite or food trucks to line up under the redwood trees at Sequoia National Park?

But the government is right about one thing: U.S. national parks are in crisis. Collectively, they have a maintenance backlog of more than $12 billion. Roads, trails, restrooms, visitor centers and other infrastructure are crumbling.

But privatizing and commercializing the campgrounds would not be a cure-all. Campgrounds are a tiny portion of the overall infrastructure backlog, and businesses in the parks hand over, on average, only about 5% of their revenues to the National Park Service.

Moreover, increased privatization would certainly undercut one of the major reasons why 300 million visitors come to the parks each year: to enjoy nature and get a break from the commercial drumbeat that overwhelms daily life.

The real problem is that the parks have been chronically starved of funding. We conducted a comprehensive survey examining how U.S. residents view their national parks, and we found that Americans place a very high value on them—whether or not they actually visit them. The peer-reviewed economic survey of 700 U.S. taxpayers, conducted by mail and internet, also found that people would be willing to pay a significant amount of money to make sure the parks and their programs are kept intact. Some 81% of respondents said they would be willing to pay additional taxes for the next 10 years to avoid any cuts to the national parks.

The national parks provide great value to U.S. residents both as places to escape and as symbols of nature. On top of this, they produce value from their extensive educational programs, their positive impact on the climate through carbon sequestration, their contribution to our cultural and artistic life, and of course through tourism. The parks also help keep America''s past alive, working with thousands of local jurisdictions around the country to protect historical sites—including Ellis Island and Gettysburg—and to bring the stories of these places to life.

The parks do all this on a shoestring. Congress allocates only $3 billion a year to the national park system—an amount that has been flat since 2001 (in inflation-adjusted dollars) with the exception of a onetime boost in 2009 as part of the Obama stimulus package. Meanwhile, the number of annual visitors has increased by more than 50% since 1980, and now stands at 330 million visitors per year.' WHERE id = 'c595f087-f1cd-5ec1-a8f2-8287ae4c2458';
-- 2023 passage[3] (reading)
UPDATE public.passages SET content = 'The Internet may be changing merely what we remember, not our capacity to do so, suggests Columbia University psychology professor Betsy Sparrow. In 2011, Sparrow led a study in which participants were asked to record 40 factoids in a computer ("an ostrich''s eye is bigger than its brain," for example). Half of the participants were told the information would be erased, while the other half were told it would be saved. Guess what? The latter group made no effort to recall the information when quizzed on it later, because they knew they could find it on their computers. In the same study, a group was asked to remember both the information and the folders it was stored in. They didn''t remember the information, but they remembered how to find the folders. In other words, human memory is not deteriorating but "adapting to new communications technology," Sparrow says.

In a very practical way, the Internet is becoming an external hard drive for our memories, a process known as "cognitive offloading." Traditionally, this role was fulfilled by data banks, libraries, and other humans. Your father may never remember birthdays because your mother does, for instance. Some worry that this is having a destructive effect on society, but Sparrow sees an upside. Perhaps, she suggests, the trend will change our approach to learning from a focus on individual facts and memorization to an emphasis on more conceptual thinking—something that is not available on the Internet. "I personally have never seen all that much intellectual value in memorizing things," Sparrow says, adding that we haven''t lost our ability to do it.

Still other experts say it''s too soon to understand how the Internet affects our brains. "There is no experimental evidence showing that it interferes with our ability to focus, for instance," wrote psychologists Christopher Chabris and Daniel J. Simons. And surfing the web exercised the brain more than reading did among computer-savvy older adults in a 2008 study involving 24 participants at the Semel Institute for Neuroscience and Human Behavior at the University of California, Los Angeles.

"There may be costs associated with our increased reliance on the Internet, but I''d have to imagine that overall the benefits are going to outweigh those costs," observes psychology professor Benjamin Storm. "It seems pretty clear that memory is changing, but is it changing for the better? At this point, we don''t know."' WHERE id = 'ac3b8992-ddf1-5679-a19b-43e41c84a443';
-- 2023 passage[4] (reading)
UPDATE public.passages SET content = 'Teenagers are paradoxical. That''s a mild and detached way of saying something that parents often express with considerably stronger language. But the paradox is scientific as well as personal. In adolescence, helpless and dependent children who have relied on grown-ups for just about everything become independent people who can take care of themselves and help each other. At the same time, once cheerful and compliant children become rebellious teenage risk-takers.

A new study published in the journal Child Development, by Eveline Crone of the University of Leiden and colleagues, suggests that the positive and negative sides of teenagers go hand in hand. The study is part of a new wave of thinking about adolescence. For a long time, scientists and policy makers concentrated on the idea that teenagers were a problem that needed to be solved. The new work emphasizes that adolescence is a time of opportunity as well as risk.

The researchers studied "prosocial" and rebellious traits in more than 200 children and young adults, ranging from 11 to 28 years old. The participants filled out questionnaires about how often they did things that were altruistic and positive, like sacrificing their own interests to help a friend, or rebellious and negative, like getting drunk or staying out late.

Other studies have shown that rebellious behavior increases as you become a teenager and then fades away as you grow older. But the new study shows that, interestingly, the same pattern holds for prosocial behavior. Teenagers were more likely than younger children or adults to report that they did things like unselfishly help a friend.

Most significantly, there was a positive correlation between prosociality and rebelliousness. The teenagers who were more rebellious were also more likely to help others. The good and bad sides of adolescence seem to develop together.

Is there some common factor that underlies these apparently contradictory developments? One idea is that teenage behavior is related to what researchers call "reward sensitivity." Decision-making always involves balancing rewards and risks, benefits and costs. "Reward sensitivity" measures how much reward it takes to outweigh risk.

Teenagers are particularly sensitive to social rewards—winning the game, impressing a new friend, getting that boy to notice you. Reward sensitivity, like prosocial behavior and risk-taking, seems to go up in adolescence and then down again as we age. Somehow, when you hit 30, the chance that something exciting and new will happen at that party just doesn''t seem to outweigh the effort of getting up off the couch.' WHERE id = '34109d29-7b4c-588c-b5f8-0e0c3603004c';
-- 2023 Q24
UPDATE public.questions SET explanation = '［考点提炼］细节理解题（官方回应与政策导向）。
［精准定位］根据题干关键词 government 与 artificial grass 定位至最后两段。第五段首先明确政府回应称“目前无计划立法禁止人造草坪”；第六段进一步补充：政府更倾向于引导民众自主作出正确选择而非强制立法，“不过人造草坪的使用必须遵守现行旨在保护生物多样性及确保可持续排水的法律与政策保障条款（must comply with the legal and policy safeguards in place）”。可见政府虽不禁售，但会提醒并要求使用者遵守现行规定，故［C］Remind its users to obey existing rules 正确。
［错项排除］［A］推动立法限制与第五段“no plans to ban”及第六段“rather than legislating”相悖；［B］确保人造草坪质量未在文中出现；［D］强行以替代品取代与“不强制立法、仅鼓励公共机构考虑”的温和政策不符。' WHERE id = 'd7f1bdc3-aaa5-585d-a946-758bd816de56';
-- 2023 Q28
UPDATE public.questions SET explanation = '［考点提炼］细节事实题（民意调查数据定位）。
［精准定位］根据题干关键词 Paragraph 5 与 respondents in the survey 定位至经同行评审的 700 名美国纳税人调查。调查显示，绝大多数民众高度重视国家公园，且愿意拿出可观资金确保公园体系完好保留；具体而言，约 81% 的受访者表示未来 10 年愿意额外缴纳附加税（willing to pay additional taxes），以避免对国家公园削减预算。这直接印证大多数受访者同意为国家公园多掏费用，故［C］agree to pay extra for the national parks 正确。
［错项排除］［A］定期游览国家公园与文中强调“无论本人是否实际去参观（whether or not they actually visit them）都珍视其价值”相悖；［B］呼吁扩大财政预算虽接近态度但不如直接“自愿多缴税款”贴合受访者具体表态；［D］支持近期商业改革恰恰是全文极力批评的对象。' WHERE id = 'ea785cdd-0e4c-537b-8ee5-d637fcd24cdd';
-- 2023 Q30
UPDATE public.questions SET explanation = '［考点提炼］主旨推断题（根源揭示与政策呼吁）。
［精准定位］结合全文主线及第五段 The real problem is that the parks have been chronically starved of funding 与末段（第七段）The parks do all this on a shoestring 可知：国家公园长期经费拮据，国会每年仅拨款 30 亿美元（且自 2001 年起计入通胀后基本停滞，仅 2009 年有一笔一次性刺激拨款），与此同时年均游客人次却较 1980 年猛增超 50% 至 3.3 亿。由此可明确得出结论，国家公园体系亟需增加财政拨款，故［D］is in need of a funding increase 正确。
［错项排除］［A］应对人手短缺与［B］满足游客需求均与资源见肘现状不符；［C］需要制定新定价政策偏离主题，全文批判靠商业开发变现，主张解决公共拨款长期不足问题。' WHERE id = 'aefd0e74-939f-5ae6-a570-abc604fc6e63';
-- 2023 Q34
UPDATE public.questions SET explanation = '［考点提炼］段落主旨与态度推断题。
［精准定位］根据题干关键词 Paragraph 3 及 how the Internet affects our brains 定位至第三、四段。第三段开篇明确点出“还有其他专家认为，现在要弄清互联网如何影响我们的大脑还为时过早（it''s too soon to understand how the Internet affects our brains）”；第四段（末段）末句亦作总结：“似乎很明显记忆正在发生改变，但究竟是在变好还是变坏？在现阶段，我们还不得而知（At this point, we don''t know）”。这清晰表明该问题仍需进一步的学术研究，故［A］requires further academic research 正确。
［错项排除］［B］在老年人中最常被研究以偏概全（2008 年那项研究只是受试群体之一）；［C］体现在阅读速度中及［D］取决于上网习惯均属无中生有。' WHERE id = '0946f686-e2e5-5593-8f07-8f4c09bae484';
-- 2023 Q40
UPDATE public.questions SET explanation = '［考点提炼］主旨大意题（全篇行文脉络总结）。
［精准定位］文章首段即开门见山提出“Teenagers are paradoxical”的核心谜题：青少年同时展现无私独立与叛逆冒险的两面；第二至五段引用 Crone 团队对 200 多名青少年的调查，实证亲社会行为与叛逆行径竟呈正相关；最后两段从心理学机制“社交回报敏感度”揭示二者共存并随年龄回落的内在原因。全文始终围绕“青少年为何自我矛盾”层层解密，故［A］Why teenagers are self-contradictory 正确。
［错项排除］［B］为何青少年对风险敏感仅涉及最后两段的解释概念，且文中重在说明他们看重社交回报压倒风险而非单纯怕风险；［C］如何培养亲社会性及［D］如何变得独立均以偏概全。' WHERE id = 'fffa6286-825d-5895-b23c-db20f73a5d01';
-- 2024 Q23
UPDATE public.questions SET explanation = '［考点提炼］人物态度与担忧定位题。
［精准定位］根据题干询问 Coyle 对变革性技术的担忧，定位至第三、四段。第三段指出若想让人们接受颠覆性变化，社会认同（social buy-in）至关重要；第四段紧接转折指出许多人心头怨气正在暗涌（resentment is simmering among many），并进一步补充人们担忧好工作被摧毁、自己反而受害。这些均说明她担心变革性技术得不到公众欢迎甚至遭遇抵制，故［D］They may be unwelcome to the public 正确。
［错项排除］［A］影响工作生活平衡与［C］产生巨额财政开支在两段均未涉及；［B］部署不切实际偷换了民众情感排斥与技术落地可行性的概念。' WHERE id = 'abcc3be5-af70-488a-bd36-85bc95f974d6';
-- 2025 passage[4] (reading)
UPDATE public.passages SET content = 'Navigating beyond the organised pavements and parks of our urban spaces, desire paths are the unofficial footprints of a community, revealing the unspoken preferences, shared shortcuts and collective choices of humans. Often appearing as trodden dirt tracks through otherwise neat green spaces, these routes of collective disobedience cut corners, bisect lawns and cross hills, representing the natural capability of people (and animals) to go from point A to point B most effectively.

Urban planners interpret desire paths as more than just convenient shortcuts; they offer valuable insights into the dynamics between planning and behaviour. Ohio State University allowed its students to navigate the Oval, a lawn in the centre of campus, freely, then proceeded to pave the desire paths, creating a web of effective routes students had established.

Yet, reluctance persists among other planners to integrate desire paths into formal plans, citing concerns about safety, environmental impact, or primarily, aesthetics. A Reddit webpage devoted to the phenomenon, boasting nearly 50,000 members, showcases images of local desire paths adorned with signs instructing pedestrians to adhere to designated walkways, underscoring the rebellious nature inherent in these human-made tracks. This clash highlights an ongoing struggle between the organic, user-driven evolution of public spaces and the desire for a visually curated and controlled urban environment.

The Wickquasgeck Trail is an example of a historical desire path, created by Native Americans to cross the forests of Manhattan and move between settlements quickly. This trail, when Dutch colonists arrived, was widened and made into one of the main trade roads across the island, known at the time as de Heere Straat, or Gentlemen''s Street. Following the British assumption of control in New York, the street was renamed Broadway. Notably, Broadway stands out as one of the few areas in NYC that defies the grid-based system applied to the rest of the city, cutting a diagonal across parts of the city.

In online spaces, desire paths have sparked a fascination that can approach obsession, with the Reddit page serving as a hub. Contributors offer a wide array of stories, from little-known new shortcuts to long-established alternate routes.

Animal desire paths, such as ducks forging trails through frozen ponds or dogs carving direct routes in gardens, highlight the adaptability of these trails in both human and animal experiences. As desire paths criss-cross through both physical and virtual landscapes, they stand as a proof of the collective insistence on forging unconventional routes and embracing the spirit of communal choice.' WHERE id = '7b92f8eb-5e2a-5296-a03f-ac759d2d3331';
COMMIT;
