-- Final deep OCR calibration fixes for KY2 (2012/2016/2017 Cloze + 2020-2022 explanations)
BEGIN;
-- 2012 Q7
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "implying", "content": "implying"}, {"key": "B", "value": "B", "text": "meaning", "content": "meaning"}, {"key": "C", "value": "C", "text": "symbolizing", "content": "symbolizing"}, {"key": "D", "value": "D", "text": "claiming", "content": "claiming"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］句内语义与现在分词辨析。
［精准定位］G.I. is just a military abbreviation [7] Government Issue...
［解题思路］句中指出 G.I. 只是一个军用缩略语，[7] Government Issue。对比可见，G 与 I 恰好是 Government Issue 两词的首字母组合，因此 Government Issue 正是在解释缩略语 G.I. 的完整含义。meaning 意为“意思是；表示……的意思”，现在分词短语 meaning Government Issue 作后置定语修饰 abbreviation，完美契合“缩写—全称解释”的语义关系，故选[B]。
［错项排除］[A] implying（暗示；暗指）侧重间接或隐含地表达含义，而 G.I. 与 Government Issue 存在直接明了的首字母对应关系，并非“暗指”，故排除；[C] symbolizing（象征；代表）侧重以具体事物表达抽象意义，而此处并非“具体—抽象”的象征关系，而是“缩写—全称”关系，故排除；[D] claiming 可表“声称（未经证实的观点）”或“认领；索取”，句中修饰“缩略语”而非“士兵”，逻辑均不符，故排除。'
WHERE id = '2b18f1a5-2003-5072-a5e9-8719af8ef08a';
-- 2012 Q8
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "handed out", "content": "handed out"}, {"key": "B", "value": "B", "text": "turned over", "content": "turned over"}, {"key": "C", "value": "C", "text": "brought back", "content": "brought back"}, {"key": "D", "value": "D", "text": "passed down", "content": "passed down"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］动词短语搭配与句内语义。
［精准定位］...and it was on all of the articles [8] to soldiers.
［解题思路］空格所在分句指出，G.I. 这个缩略语印在 [8] 给士兵的所有物品（articles）上。结合前文 G.I. 的全称 Government Issue（政府配发/发放）可知，这些物品是由政府或军方发放给士兵的。handed out（分发、发放）作过去分词短语 handed out to soldiers 修饰 articles，准确呼应 Government Issue 的内涵，故选[A]。
［错项排除］[B] turned over（移交；转交所有权/管理权）侧重把控制权或管理权正式交给他人，并非政府向普通士兵分发军需物品，故排除；[C] brought back（带回；使恢复）无法与“物品发往士兵”的语境搭配，故排除；[D] passed down（世代相传；自上而下流传）多指传统、财产或经验的代际传承，不合句意，故排除。'
WHERE id = '7018abe9-0249-5d5f-bbd9-c7ffc00e4aa8';
-- 2012 Q9
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "pushed", "content": "pushed"}, {"key": "B", "value": "B", "text": "got", "content": "got"}, {"key": "C", "value": "C", "text": "made", "content": "made"}, {"key": "D", "value": "D", "text": "managed", "content": "managed"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］固定习语搭配与上下文语义。
［精准定位］A common name for a guy who never [9] it to the top.
［解题思路］句中解释“Joe”是一个代表普通人的常见名字，他从未 [9] 过社会顶层；后文紧接着列举 Joe Blow、Joe Palooka、Joe Magrac 等工人阶级常用名予以印证。make it 为固定习语，意为“获得成功；闯出名堂”，never made it to the top 意为“从未成功攀上事业或社会巅峰”，契合平民与工人阶级语境，故选[C]。
［错项排除］[A] pushed 与虚指宾语 it 搭配时多表示“勉强；得寸进尺（push it）”，push sth to the top 需接具体实物，不合句意，故排除；[B] got（get it）意为“明白；得到”，其中的 it 需实指前文事物，且不与 to the top 搭配表达成功登顶，故排除；[D] managed 表“设法完成”时需接不定式（manage to do）或实指宾语，不能与虚指 it 构成 manage it to the top，故排除。'
WHERE id = 'f3628ec2-bb56-5972-bd08-bac445c511ee';
-- 2012 Q10
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "ever", "content": "ever"}, {"key": "B", "value": "B", "text": "never", "content": "never"}, {"key": "C", "value": "C", "text": "either", "content": "either"}, {"key": "D", "value": "D", "text": "neither", "content": "neither"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］上下文语义与否定副词用法。
［精准定位］The United States has [10] had a president or vice-president or secretary of state Joe.
［解题思路］本句作为佐证指出：美国 [10] 有过名叫“Joe”的总统、副总统或国务卿（均属最高层政要）。与前两句“never made it to the top（从未登上顶层）”“a working class name（工人阶级名字）”一脉相承，此处句中无其他否定词，应填入自身表完全否定含义的副词 never（从未），故选[B]。
［错项排除］[A] ever 意为“曾经；在任何时候”，本身不含否定意味，在无其他否定词的肯定陈述句中不能表“从未”，故排除；[C] either 作副词表“（用于否定句末）也”，前文并无否定词且位置不符，故排除；[D] neither 表“也不”，多用于承接前句的否定倒装结构（neither did...），不能置于助动词 has 与过去分词 had 之间否定单句，故排除。'
WHERE id = 'd56adb0e-32f2-54c7-baed-79725713adf8';
-- 2012 Q11
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "disguised", "content": "disguised"}, {"key": "B", "value": "B", "text": "disturbed", "content": "disturbed"}, {"key": "C", "value": "C", "text": "disputed", "content": "disputed"}, {"key": "D", "value": "D", "text": "distinguished", "content": "distinguished"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义与形容词辨析。
［精准定位］G.I. Joe had a [11] career fighting German, Japanese, and Korean troops.
［解题思路］第三段转入对“大兵乔”历史形象的正面颂扬，指出他曾与德军、日军及朝军作战，拥有一段 [11] 的军旅生涯，后被拍成经典电影并深受多国民众敬仰。distinguished 意为“卓越的；杰出的；战功显赫的”，与 career 搭配传神体现作者对其战功与贡献的高度褒奖，故选[D]。
［错项排除］[A] disguised 意为“伪装的；隐蔽的”，与大兵乔公开英勇作战的事迹不符，故排除；[B] disturbed 意为“心神不安的；受到干扰的”，含贬义，与全文赞扬基调相悖，故排除；[C] disputed 意为“有争议的”，原文并未质疑其军旅生涯的功绩，故排除。'
WHERE id = '4a9f738f-00bd-5185-81a2-2f58ea1a8fbc';
-- 2012 Q12
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "company", "content": "company"}, {"key": "B", "value": "B", "text": "community", "content": "community"}, {"key": "C", "value": "C", "text": "collection", "content": "collection"}, {"key": "D", "value": "D", "text": "colony", "content": "colony"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］固定搭配与抽象名词辨析。
［精准定位］He appears as a character, or a [12] of American personalities, in the 1945 movie The Story of G.I. Joe...
［解题思路］句意指出，在 1945 年电影《美国大兵乔的故事》中，G.I. Joe 作为一个角色出现，或者说是美国人性格特点的 [12]。结合上文“大兵乔泛指普通美军士兵，乔代表普通美国人”可知，该艺术形象汇聚了诸多普通美国人的性格特质。a collection of 意为“一批；集合”，a collection of American personalities 意为“美国人性格特点的集合”，契合语境，故选[C]。
［错项排除］[A] company 表“陪伴”或“为某一目的聚在一起的一群人”，不能与抽象的“性格特点”搭配，故排除；[B] community 指“社区居民群”或“生物群落”，亦不与抽象性格特征搭配，故排除；[D] colony 指“（同地区）动植物群”或“殖民地”，侧重有生命的生物群体，与无生命的 personalities 无法搭配，故排除。'
WHERE id = '7259ee36-588a-5679-a781-5009513bff56';
-- 2012 Q13
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "employed", "content": "employed"}, {"key": "B", "value": "B", "text": "appointed", "content": "appointed"}, {"key": "C", "value": "C", "text": "interviewed", "content": "interviewed"}, {"key": "D", "value": "D", "text": "questioned", "content": "questioned"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］上下文语义与动词辨析。
［精准定位］Some of the soldiers Pyle [13] portrayed themselves in the film.
［解题思路］前句交代电影改编自著名战地记者厄尼·派尔（war correspondent Ernie Pyle）生命最后时光的经历；本句指出派尔 [13] 过的一些士兵在影片中本色出演了自己。基于战地记者（记者与一线官兵）的身份定位，“采访”是其核心报道方式，interviewed（采访）最能构建“采访—记录—改编电影”的连贯逻辑，故选[C]。
［错项排除］[A] employed 意为“雇用”，战地记者并非士兵的雇主，逻辑不符，故排除；[B] appointed 意为“任命；委派”，记者无权任命军队士兵，故排除；[D] questioned 虽可译作“提问”，但语体侧重审讯、盘问或官方质询，不适用于记者与战地士兵之间的日常访谈场景，故排除。'
WHERE id = '0cf4d743-f1de-5546-af66-a0cebbfa6a4a';
-- 2012 Q14
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "human", "content": "human"}, {"key": "B", "value": "B", "text": "military", "content": "military"}, {"key": "C", "value": "C", "text": "political", "content": "political"}, {"key": "D", "value": "D", "text": "ethical", "content": "ethical"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］句内对比语义与熟词僻义。
［精准定位］Pyle was famous for covering the [14] side of the war, writing about the dirt-snow-and-mud soldiers...
［解题思路］句中对比表明，派尔因报道战争 [14] 的一面而闻名：他笔下写的是满身泥尘风雪的普通士兵，而非推进了多少英里或攻占了哪些城镇等宏大战事。human 除“人的”外，在此语境下意为“有人情味的；关注普通人处境的”，the human side of the war 与具体的基层士兵形成完美照应，故选[A]。
［错项排除］[B] military（军事的）恰恰对应后文否定成分中“行军英里数、攻占/解放城镇”等纯军事进展，与 not 所引导的对比逻辑相悖，故排除；[C] political（政治的）与 [D] ethical（伦理道德的）均属宏观或抽象层面议题，并非派尔聚焦微观一线士兵冷暖的写作重心，故排除。'
WHERE id = '7f305287-9260-5859-81cb-257ecde9ed54';
-- 2012 Q15
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "ruined", "content": "ruined"}, {"key": "B", "value": "B", "text": "commuted", "content": "commuted"}, {"key": "C", "value": "C", "text": "patrolled", "content": "patrolled"}, {"key": "D", "value": "D", "text": "gained", "content": "gained"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］熟词僻义与动宾语义搭配。
［精准定位］...not how many miles were [15] or what towns were captured or liberated.
［解题思路］空格位于与 towns were captured or liberated 并列的分句中，主语为 how many miles（多少英里），共同说明宏观层面的军事战果进展。gain 除基本义“获得；增加”外，可作熟词僻义表“（军队等）向前推进（一段距离）”，可直接接长度单位（如 gain miles），变为被动语态 miles were gained 表示“战线推进了多少英里”，契合语境，故选[D]。
［错项排除］[A] ruined（毁坏；破坏）不能以距离单位“英里”作为承受动作的逻辑宾语，语义不通，故排除；[B] commuted（通勤往返）常与 between/to/from 等地点介词连用描述日常生活上班，不接长度度量且不符战争语境，故排除；[C] patrolled（巡逻；巡查）需以“区域、道路、边境”而非纯距离“多少英里”作宾语（若表距离须为 miles of road were patrolled），且“巡逻”不体现前线推进战果，故排除。'
WHERE id = '1ff254da-97db-5828-a835-9ab451c14b2f';
-- 2012 Q17
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "neglected", "content": "neglected"}, {"key": "B", "value": "B", "text": "emphasized", "content": "emphasized"}, {"key": "C", "value": "C", "text": "avoided", "content": "avoided"}, {"key": "D", "value": "D", "text": "admired", "content": "admired"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］上下文呼应与动词辨析。
［精准定位］Both men [17] the dirt and exhaustion of war, the [18] of civilization that the soldiers shared...
［解题思路］前两句先介绍战地记者派尔擅长刻画满身泥雪的士兵，接着指出其报道与著名漫画家比尔·莫尔丁的作品异曲同工（paralleled）；本句由此总结“两人（Both men）都 [17] 战争的肮脏与疲惫”。emphasized 意为“强调；着重表现”，准确呼应上文对真实战场艰辛细节的着力刻画，故选[B]。
［错项排除］[A] neglected（忽视）和 [C] avoided（回避）均与上文派尔专注描写 dirt-snow-and-mud soldiers 的核心特点完全相反，故排除；[D] admired（钦佩；赞赏）作及物动词接“肮脏与疲惫（dirt and exhaustion）”，在语义情感上荒谬不通，作品刻画的是战争残酷而非赞美肮脏疲惫，故排除。'
WHERE id = '9f4730e1-775f-5f39-806d-4a4693cf375b';
-- 2012 Q18
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "stages", "content": "stages"}, {"key": "B", "value": "B", "text": "illusions", "content": "illusions"}, {"key": "C", "value": "C", "text": "fragments", "content": "fragments"}, {"key": "D", "value": "D", "text": "advances", "content": "advances"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义与同位语列举概括。
［精准定位］...the [18] of civilization that the soldiers shared with each other and the civilians: coffee, tobacco, whiskey, shelter, sleep.
［解题思路］空格前出现并列宾语“战争的肮脏与疲惫”，后接冒号同位语列举“咖啡、烟草、威士忌、容身之所、片刻睡眠”。在残酷动荡的战火废墟中，这些零星微薄的日常物事正是文明生活遗落下来的吉光片羽与零碎点滴。fragments（碎片；零星片段）既概括了五类具体列举的共性，又以“文明残片”强化战时生活的匮乏与艰辛，故选[C]。
［错项排除］[A] stages（时期；阶段）无法概括咖啡、住所与睡眠等具体物质/状态例举，故排除；[B] illusions（幻想；错觉）与后文列举的真实可感物品（咖啡、烟草、威士忌、住所、睡眠）性质矛盾，故排除；[D] advances（进步；进展）多指文明或科技的新近突破发展，无法概括“睡眠、遮蔽所”这类基本生存需求且偏离战时艰苦语境，故排除。'
WHERE id = '63f2e00f-531a-5dd5-b022-55dcc7cb5641';
-- 2012 Q19
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "With", "content": "With"}, {"key": "B", "value": "B", "text": "To", "content": "To"}, {"key": "C", "value": "C", "text": "Among", "content": "Among"}, {"key": "D", "value": "D", "text": "Beyond", "content": "Beyond"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］句内逻辑与介词辨析。
［精准定位］[19] Egypt, France, and a dozen more countries, G.I. Joe was any American soldier, [20] the most important person in their lives.
［解题思路］句中代词 their 回指 Egypt, France, and a dozen more countries（的民众），指出大兵乔在战时是“他们生命中最重要的人”。这里需要一个介词引出持有某种观点、态度或情感归属的主体。To sb/some country 意为“对……而言；在……看来/心目中”，用于引出感受与评价主体，完美契合语境，故选[B]。
［错项排除］[A] With 表态度时多接承受态度的对象（如 happy with sth），而不能直接置于句首引出持有看法的国家民众主体，故排除；[C] Among 意为“在……之中”，引出观点群体时常与 common、popular 等形容词连用，本句并无此类对应词且易产生歧义，故排除；[D] Beyond 意为“超出（范围）；除……之外”，不能引出感知“最重要之人”的情感主体，故排除。'
WHERE id = 'cc33a1c9-bf87-5b8b-8fd0-fe1ab8759fad';
-- 2016 Q7
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Sure", "content": "Sure"}, {"key": "B", "value": "B", "text": "Odd", "content": "Odd"}, {"key": "C", "value": "C", "text": "Unfortunate", "content": "Unfortunate"}, {"key": "D", "value": "D", "text": "Often", "content": "Often"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］固定短语与上下文逻辑衔接。
［精准定位］[7] enough, firms'' investment and R&D intensity were correlated with the happiness of the area...
［解题思路］空格位于句首插入语“___ enough”，后文指出“企业的投资和研发力度确实与其所在地区的幸福感呈正相关”。前段刚提出检验地方幸福感是否影响企业投资的设想，此处研究数据证实了预期。Sure enough 为固定习惯搭配，意为“果然；果不其然”，精准呼应并证实前文预期，故选[A]。
［错项排除］[B] Odd enough 意为“奇怪的是”，表达与常理或预期相反，与研究结果证实预期之义相悖，故排除；[C] Unfortunate（不幸的）既很少用作 Unfortunate enough 句首固定插入语（常为 Unfortunately），也与中性科研结论不符，故排除；[D] Often enough 意为“经常；屡屡”，无法表达“预期得到印证”的逻辑语义，故排除。'
WHERE id = '3d290e53-a2e6-5f64-838d-cd156202f023';
-- 2017 Q20
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "technological", "content": "technological"}, {"key": "B", "value": "B", "text": "professional", "content": "professional"}, {"key": "C", "value": "C", "text": "educational", "content": "educational"}, {"key": "D", "value": "D", "text": "interpersonal", "content": "interpersonal"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］形容词对比与文章主旨收束。
［精准定位］...we tend to engage in them with the intensity usually reserved for [20] matters.
［解题思路］后文将业余爱好（a hobby or a passion project）与以往仅用于工作事务的专注强度进行对比，这里指通常留给“职业/工作（professional）”事务的心力强度，收束全文关于劳动与闲暇转换的讨论，故选[B]。
［错项排除］[A] technological（技术的）、[C] educational（教育的）与[D] interpersonal（人际的）均脱离了“职业工作 vs 业余爱好”的对比框架。'
WHERE id = '02d7be36-110a-5aab-a0ae-46fdc7acc221';
-- 2020 Q1
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "tedious", "content": "tedious"}, {"key": "B", "value": "B", "text": "pleasant", "content": "pleasant"}, {"key": "C", "value": "C", "text": "instructive", "content": "instructive"}, {"key": "D", "value": "D", "text": "tricky", "content": "tricky"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义+形容词辨析。
［解题思路］①②句中路标词 of course → But 提示两句间转折逻辑：“（当好父母的）理想固然好，但现实存在障碍”，结合②句主句主语 defining what it means to...（阐明“做好父母”的内涵）以及原因状语从句 particularly since...（对于同一种育儿方式，不同的孩子的反应不同），可知育儿方式难有固定标准、相当棘手。[D]tricky 意为 difficult to do or deal with（难办的、棘手的），符合文意。
［错项排除］从总体导向看，[B]、[C]两项均为正面语义，与句间转折逻辑矛盾；具体来说，pleasant 指“令人愉快、吸引人的”或“对人友善、客气的（~ to sb）”，如 a pleasant environment（宜人的环境），instructive 指“有启发性的（giving a lot of useful information）”，如 an instructive experience（富有启发的经历），[A]tedious 意为“冗长乏味的”，均不契合“因人而异、难以界定”的语境。'
WHERE id = 'b8322430-4461-56e7-b7c4-f703dd94628e';
-- 2020 Q2
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "in addition", "content": "in addition"}, {"key": "B", "value": "B", "text": "for example", "content": "for example"}, {"key": "C", "value": "C", "text": "at once", "content": "at once"}, {"key": "D", "value": "D", "text": "by accident", "content": "by accident"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］句间语义逻辑+副词短语辨析。
［解题思路］空格词在句中作插入语，可先看句子主干信息A calm，rule-following child...better... than...a younger sibling，可知该句是针对上句宽泛结论children respond differently...（不同孩子对同种育儿风格反应不同）给出的具体实例——性格、年龄不同，则反应不同（更稳重、守规和年长的孩子适应力更强），故空格词应表“举例说明”，[B]正确。
［错项排除］[A]in addition（=also，as well）表并列，位于句中时，前后信息完整（其后常为省略形式），互为补充，如They study their instruments and，in addition，theory and music history.（他们研究其乐器，还研究其理论和音乐史。），文中空格前后皆不完整，需相连才能构成完整信息（better...than.. a younger sibling），故两者并非并列关系。注：副词短语In addition多见于句首，位于句中时常由and、but等连词引出。[C]at once（=immediately；without delay或at the same time）表时间，用于强调动作在短时内或同时发生/实现，如Come here at once！（马上到这里来！），Don''t all speak at once！（大家不要同时讲！）；[D]by accident表方式，用于说明某事的发生是偶然、非刻意的，如Helen got into acting purely by accident.（海伦当演员完全出于偶然。）；文中③句谓语为respond better，为普遍状况，而非短时内或偶然之事，故排除两项。'
WHERE id = 'f69d94e1-5233-57eb-90d8-ce14d93e700c';
-- 2020 Q3
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Fortunately", "content": "Fortunately"}, {"key": "B", "value": "B", "text": "Occasionally", "content": "Occasionally"}, {"key": "C", "value": "C", "text": "Accordingly", "content": "Accordingly"}, {"key": "D", "value": "D", "text": "Eventually", "content": "Eventually"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］上下文语义逻辑。
［解题思路］上段提到“定义做好父母”很难（也即：人们即使想做好父母，也可能无所适从），本段①②句指出“还有一种稍容易的父母：耐心的父母。所有年龄段的孩子都能从有耐心的养育方式受益”。很明显，本段退而求其次，向人们介绍一种确定性的好父母特质“耐心”。[A]Fortunately既体现tricky VS easier间对比逻辑，又契合论述的情感色彩：虽难界定，但幸好还有某种标准可依。
［错项排除］[B]Occasionally（= sometimes but not often）表频度，暗示“耐心的父母”只偶尔存在，与作者意图“介绍一种确定的好父母标准”不符。[C]Accordingly可表因果（=therefore），如Thetextwas too long and the editor accordingly cut it by20%.（文稿过长，因此编辑删减了五分之一。），还可表方式（=correspondingly），如Wehave to discover what his plans are andact accordingly.（我们必须弄清他有什么打算并采取相应行动。）；上文既非空格所在句的原因，也非其应该参照的情况，故排除。[D]Eventually用法有二：一为客观引出情况或过程的最终结局，二为影射某情况历经多时或万难总算达成，均表时间，而空格句并非最终结果。'
WHERE id = '6e46515e-0516-551a-b3e2-d3798ae30a20';
-- 2020 Q5
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "while", "content": "while"}, {"key": "B", "value": "B", "text": "because", "content": "because"}, {"key": "C", "value": "C", "text": "unless", "content": "unless"}, {"key": "D", "value": "D", "text": "once", "content": "once"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］句内语义逻辑。
［解题思路］空格词体现主句与从句间逻辑，需先明确两句大意。Still位于句首提示转折，表明本句与上文传递的积极情感“（虽难有明确的标准，但至少）可将耐心作为努力目标”方向相反，可能引出该方法的局限性或实现障碍，由此可见，主句this is no easy...（this回指to be patient）大意应为“耐心并不好达成”，明显与空格所在的分句“所有父母都想成为有耐心之人”为转折逻辑（理想虽好，但现实困难），故[A]while符合文意。
［错项排除］[B]because、[D]once（=as soon as；when）利用“人人都向往的事情往往不易”这一常理干扰，但二者并非因果关系，也非条件关系：“都想有耐心”并非导致或触发“耐心不易”的因素或条件；[C]unless 指向“除非大家都想有耐心，否则这并不容易”，但“都想有耐心”并非“耐心容易”的前提条件，三个选项均存在逻辑错误。'
WHERE id = '9144d602-b688-5770-b67c-3c969a80f028';
-- 2020 Q6
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "answer", "content": "answer"}, {"key": "B", "value": "B", "text": "task", "content": "task"}, {"key": "C", "value": "C", "text": "choice", "content": "choice"}, {"key": "D", "value": "D", "text": "access", "content": "access"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］句内语义+名词辨析。
［解题思路］结合上题分析可知，this is no easy大意为“耐心不易达成”，而空格词为表语，故应与主语this（代指to be patient，表示“目标”）属于同类且互相呼应，[B]task尤指艰巨或令人厌烦的任务、工作，与“目标”相吻合，同时符合上下文文意，即：变得耐心并非易事。
［错项排除］[A]暗指“耐心未必能真正解决问题”，与②句“所有孩子都能受益于耐心的养育”矛盾；
[C]暗指“人们做出朝耐心努力这一选择”有一定困难，但文意实为“耐心本身不易达成”，而非“（外界因素等导致）选择难做”。[D]access表示“获得/使用/接近（某事/某地/某人）的能力、机会或权利”，常以介词to引出动作施加的对象，如have easy access to information（很容易获取信息）；故从结构上看，没有is this no easy access的说法，正确形式应为(there is) no easy access to sth；从语义上看，access的对象一般为资源、设施、场所、特定人物等，而“变耐心”为目标、任务，两者无法搭配。'
WHERE id = '5f36eedb-a288-53b6-b2f0-70d97ae3bff4';
-- 2020 Q7
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "tolerant", "content": "tolerant"}, {"key": "B", "value": "B", "text": "formal", "content": "formal"}, {"key": "C", "value": "C", "text": "rigid", "content": "rigid"}, {"key": "D", "value": "D", "text": "critical", "content": "critical"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］句内语义逻辑+形容词辨析。
［解题思路］maintaina style框定父母在疲惫而沮丧时无法做到的事情，空格词与composed（沉着的）并列，而选项中同属正面、与“耐心”相关的只有[A]tolerant。
［错项排除］干扰项均无法与composed构成并列关系，脱离“耐心”语义场，具体来看，[B]formal用于说明穿着、言语、行为等适合正式或重要场合，而文中育儿行为不涉及正式或重要场合。formal还用于说明教育或培训是“在学校获得的（而非个人实践所得）、正规的”，如Shedidn''t have any formal dance training.（她没受过任何正规的舞蹈训练。），但文中空格词限定的是父母育儿方式/姿态（style），而非孩子所受教导。[C]rigid利用其表面义“严格”干扰，但该词实为负面导向，用于说明法律或制度僵死不变从而过于严格，当说明“人”时，意为“古板、头脑僵化”，不合文意。[D]critical同样利用“严格出教育”这一常见认知干扰，但该词修饰名词、作“批评的”讲时，后接“含批评内容的载体”，如critical comments/articles（批判性的评论/文章）；critical还表“有判断力的”，此时可接“方式、方法”，但此义侧重“思考与审慎能力”，与“耐心育儿”并无关联。·词汇注释与难句分析·
① parenting [ˈpeərəntɪŋ]n. 养育，抚养② rule-following [ruːl ˈfɒləʊɪŋ]adj. 遵守规则的③ sibling [ˈsɪblɪŋ]n. 兄弟姐妹④ composed [kəmˈpəʊzd]adj. 镇静的，平静的，沉着的But defining what it means to be a good parent is undoubtedly very tricky，particularly since children respond differently to the same style of parenting.
【结构切分】[But defining what it means to be a good parent is undoubtedly very tricky]（主句），[particularly since children respond differently to the same style of parenting]（原因状语从句）。'
WHERE id = 'dcaecf51-171f-514a-bf87-7eb6e77cefd3';
-- 2020 Q8
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "move", "content": "move"}, {"key": "B", "value": "B", "text": "drag", "content": "drag"}, {"key": "C", "value": "C", "text": "push", "content": "push"}, {"key": "D", "value": "D", "text": "send", "content": "send"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义+固定搭配。
［解题思路］空格句指出，有时你的孩子会逼得你有些过头。结合上文“耐心不易”以及空格前半句“你只不过是凡人”可知，本句意在解释“父母为何难以做到耐心”，故文意应为“孩子让父母不得已失去耐心”，push有“迫使、促使”之意，push sb too far为固定搭配，意为“逼人太甚、逼得某人发脾气”，故[C]正确。
［错项排除］本题考查固定短语，选项中只有[C]能与you...toofar搭配传达“逼迫某人”之意，且
[A]“感动过头”与“失去耐心”的语义相悖；[B]drag 也有“强迫”之意，但表示“生拉硬拽，劝人勉强来/去某地”，如 I''m sorry to drag you all this way in the heat.（抱歉这么热的天硬拉着你跑了这一路），文中并无“拉拽去某地”之意；[D]send 虽有“让人向某方向移动”或“使作出某种反应/行动（send sb to/into sth）”之意，但 too far 并非方向或行为，无法与之搭配。'
WHERE id = '2dc8b38c-00bd-5302-b437-ee0ded64d012';
-- 2020 Q9
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "mysterious", "content": "mysterious"}, {"key": "B", "value": "B", "text": "illogical", "content": "illogical"}, {"key": "C", "value": "C", "text": "suspicious", "content": "suspicious"}, {"key": "D", "value": "D", "text": "inevitable", "content": "inevitable"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义+形容词辨析。
［解题思路］“the + 形容词”表示“…的事情”，冒号提示其是对随后“父母失去耐心的具体表现”的概括性评价，而上句“你只是凡人，孩子有时会逼得人发脾气”传达作者态度：这些不耐心的表现是人在情急下的正常反应，在所难免，情有可原，故[D]inevitable符合文意。
［错项排除］Andthen...happens表明①②句间为因果顺承关系，①句“孩子有时会把人逼得有些过头”这一情况为②句“父母失去耐心”提供了前提，且作者暗示两件事接连发生、在所难免。[A]mysterious、[B]illogical皆与文章所表达的“理所当然”之意相，故排除；the suspicious表示“可疑的人/事”，与犯罪或欺诈相关，脱离上下文语境，排除[C]。'
WHERE id = 'c5b973f8-5cd5-5890-acdd-3372b098b045';
-- 2020 Q10
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "boring", "content": "boring"}, {"key": "B", "value": "B", "text": "naive", "content": "naive"}, {"key": "C", "value": "C", "text": "harsh", "content": "harsh"}, {"key": "D", "value": "D", "text": "vague", "content": "vague"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义+形容词辨析。
［解题思路］句中either...or...与and分别呈现两组并列信息：scream at your kids与say something that...均为失去耐心后的表现，内容应相近；a bit too和does nobody any good并列修饰something（父母失去耐心后的言辞），应同为消极色彩。可见空格词应该同时体现“朝孩子大喊、对谁都没好处”，故文意应为“向孩子说狠话”，[C]harsh 可用于说明行为或言语“严酷无情”，符合文意。
［错项排除］[A]boring、[B]naive和[D]vague分别指向父母的话“无聊乏味（孩子听不进去）、无知而缺乏经验（没有指导意义）、含糊而不具体（难以理解）”，从育儿角度看三种言辞确实没有好处，但文中does nobody any good实为“对父母、孩子双方都无益”，消极程度更甚，其次三项均不能与scream at your kids构成并列内容。'
WHERE id = '03679ada-b7c1-5d48-9700-d30ec4152c95';
-- 2020 Q11
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "turn back", "content": "turn back"}, {"key": "B", "value": "B", "text": "take apart", "content": "take apart"}, {"key": "C", "value": "C", "text": "set aside", "content": "set aside"}, {"key": "D", "value": "D", "text": "cover up", "content": "cover up"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］上下文语义+固定搭配。
［解题思路］空格句前句描述父母对孩子发怒时的表现及后果，too...does nobody any good说明表现过度。空格句指出，你（父母）希望可以[11]（让时光倒流）、重新开始。可见空格句应体现“父母为此前的发怒行为感到懊悔”；由句内逻辑（and提示衔接/并列）可进一步明确，[11]the clock 应与 start over 语义同向，表“回到过去、重新再来”。turn back the clock为固定搭配，表“使时光倒流”，[A]正确。
［错项排除］由语境可知，文中theclock以具象的“时钟”指代抽象的“时间”，[B]take apart（拆解；拆开）只体现对时钟的物理操作，无法传达抽象含义；[C]set aside（留出；不顾）“将时钟放在一边”指向“不顾时间（流逝）”；[D]cover up（掩盖）“遮盖时钟”指向“掩盖时间（流逝）”，均不符合原文所要传达的“悔恨过往行为、期盼时光倒转”之意。① push sb. too far 逼人太甚② lose one''s patience 失去耐心③ scream at sb. 朝某人吼叫④ do sb. good 对某人有好处• start over 从头开始'
WHERE id = '1092e8ea-d56a-5af5-8cc4-c3e93e6584a9';
-- 2020 Q14
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "raise", "content": "raise"}, {"key": "B", "value": "B", "text": "affect", "content": "affect"}, {"key": "C", "value": "C", "text": "justify", "content": "justify"}, {"key": "D", "value": "D", "text": "reflect", "content": "reflect"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］句内语义。
［解题思路］空格所在句以not only...but also结构呈现句内语义递进，your child’s self-esteem（孩子的自尊）应与damage...child（破坏亲子关系）同样体现父母发怒行为的危害，且程度更甚，故文意应为“伤害/打击孩子自尊心”，[B]affect表“影响”时多指向负面影响，故正确。
［错项排除］[A]raise表明父母行为对孩子的自尊有正面影响（提升自尊心），与文意恰恰相反。[C]justify意为“证明某事有理/有必要”，而self-esteem指对自身价值、能力的信心，重要性毫无争议，无需“证明”。[D]reflect指向“父母发怒行为会体现/表明孩子的自尊心”，不合常理，且不涉及“危害”，故排除。'
WHERE id = '78a504ad-d408-5a56-84e1-92e08935e903';
-- 2020 Q15
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "time", "content": "time"}, {"key": "B", "value": "B", "text": "bond", "content": "bond"}, {"key": "C", "value": "C", "text": "race", "content": "race"}, {"key": "D", "value": "D", "text": "cool", "content": "cool"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义+固定搭配。
［解题思路］空格句内条件状语从句If...then提示“你给孩子树立缺乏情绪控制的范例”为“你不断对孩子失去”的结果（文中you均指“父母”），则空格词应与“情绪控制”语义相近。结合贯穿全文的话题“父母对孩子失去耐心”，可进一步明确空格词应表与“耐心”相近的特质，选项中只有[D]cool（平静、镇静）与之有交集，故正确，lose/keep your cool为习语，意为“火冒三丈/保持沉着”。
［错项排除］[A]time指向“父母与孩子相处时间不足”，偏离文中要义“育儿难保持耐心”。[B]颠倒因果：bond虽与上段末句relationship同义，但“亲子关系遭破坏”是“父母对孩子发怒”的结果而非原因；[C]race 借“孩子捣蛋、父母发怒”臆想竞赛场景并强加关联，但父母输赢与情绪自控力无关，均可排除。'
WHERE id = 'ce01fb7f-0f23-57a8-a057-57cb9cefcfe5';
-- 2020 Q17
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "cheated", "content": "cheated"}, {"key": "B", "value": "B", "text": "defeated", "content": "defeated"}, {"key": "C", "value": "C", "text": "confused", "content": "confused"}, {"key": "D", "value": "D", "text": "confronted", "content": "confronted"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义。
［解题思路］Infact（确切地说）提示④句在③句基础上说明“控制情绪”更重要/具体的作用，空格后stress呼应第二至四段所述父母发怒的诱因“压力、疲劳（exhausted、frustrated、fatigue）”，表明空格句所述“在被压力时调节/控制情绪的能力”能解决前文所述问题“父母在疲惫时易向孩子发怒”，空格词应表“影响/困扰”之意，be confronted by sth.指“面对（有威胁或难处理的事物）”，故[D]正确。
［错项排除］[A]、[C]均歪曲了压力对父母的影响，文中只提到压力会使父母无法控制情绪，并未提到压力会使父母思维混乱、虚实不分。[B]暗含“父母已被压力击溃、无可救药”之意，与文中建议的隐含义“父母可通过控制情绪避免被压力影响”相。·词汇注释与难句分析·
① consistently [kənˈsɪstəntli]adv. 一贯地；始终② inadvertently [ˌɪnədˈvɜːtəntli]adv. 无意地，不经意地③ model [ˈmɒdl]v. 塑造④ regulate [ˈreɡjuleɪt]v. 调节，规定；控制'
WHERE id = '76df95d5-a5ad-5b2e-8695-95c5001c4199';
-- 2020 Q18
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "terrible", "content": "terrible"}, {"key": "B", "value": "B", "text": "hard", "content": "hard"}, {"key": "C", "value": "C", "text": "strange", "content": "strange"}, {"key": "D", "value": "D", "text": "wrong", "content": "wrong"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］上下文语义。
［解题思路］空格句指出“当然，始终对孩子保持耐心相当。”下句指出“一种更可行的做法是”。可见，空格句承上文“保持耐心的重要性”退而承认保持耐心很难，并引出更实际可行的做法，
[B]符合文意。同时契合第三、四段要义“成为耐心的父母并非一项简单的任务”“父母对孩子发怒情有可原”。
［错项排除］[A]、[D]均传达“父母始终对孩子保持耐心是一种错误做法”之意，[C]strange表示“某情况不正常、出人意料，令人担忧或害怕”，同样否定了该做法的意义，偏离作者态度“始终对孩子保持耐心是最理想的状态，尽管很难”。'
WHERE id = '1e030c54-94e0-5203-a814-6d23abfc0a0e';
-- 2020 Q19
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "trying", "content": "trying"}, {"key": "B", "value": "B", "text": "changing", "content": "changing"}, {"key": "C", "value": "C", "text": "exciting", "content": "exciting"}, {"key": "D", "value": "D", "text": "surprising", "content": "surprising"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］上下文语义+熟词僻义。
［解题思路］空格句指出，一个更现实可行的目标是父母在面临涉及孩子的情况时尽可能地保持镇静。回溯上文多次复现的信息“成为耐心的父母并不容易，父母时常被孩子逼得情绪失控”可知，situations involving your children应为“令人烦恼或失去耐心的、难应付的育儿时刻”，[A]trying用于说明“某事/人惹人烦、难对付”，故正确。
［错项排除］由上下文可知，空格词应体现处境对父母不利，首先排除含正向语义的[C]exciting。
[B]changing、[D]surprising虽可传达负面语义，但前者表意过于宽泛，不能直接指向文中关注的焦点情况“育儿中失去耐心而暴怒”，而后者与文中I understand this、We''''ve all been there、it''scommon所暗示的该情况“司空见惯，父母皆有体会”相矛盾。'
WHERE id = 'b8798c5f-8a80-58f0-9eac-1fd1ee11a1ed';
-- 2020 Q20
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "hide", "content": "hide"}, {"key": "B", "value": "B", "text": "emerge", "content": "emerge"}, {"key": "C", "value": "C", "text": "withdraw", "content": "withdraw"}, {"key": "D", "value": "D", "text": "escape", "content": "escape"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］上下文语义+动词辨析。
［解题思路］空格句说明目标达成（goal与②句A more practical goal同指）的结果（promise you this、As a result... this goal）：父母和孩子都将从紧张的时刻中获益并[20]（摆脱出来），身心状态都得到提升。根据上下文以及and可知，[20]from stressful moments应和“从中获益”一样，皆体现积极结果，emerge from sth意为“（从困境或苦难经历中）幸存下来，摆脱出来”，故[B]符合文意。
［错项排除］[A]、[C]、[D]均可表示“与…分离，从…中出来”，但均含“因无法解决问题/被击溃而被动消极地逃避”之意，谈不上“最终结果积极、结局良好”。·词汇注释与难句分析·
① incredibly [ɪnˈkredəbli]adv. 难以置信地；极其② practical [ˈpræktɪkl]adj. 实际的，务实的③ to the best 尽全力④ composed [kəmˈpəʊzd]adj. 镇静的；沉着的• be faced with 面对；面临• as a result of 由于；作为……的结果A more practical goal is to try, to the best of your ability, to be as tolerant and composed as you can when faced with trying situations involving your children.
【结构切分】A more practical goal is [to try, to the best of your ability, to be as tolerant and composed as you can]（不定式作表语，含插入语 to the best of your ability） [when faced with trying situations involving your children]（时间状语从句分词省略结构）。'
WHERE id = 'a5439ffd-d7e6-5d7c-8338-89e3e4883c40';
-- 2020 Q21
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "pick up social signals from non-living rats", "content": "pick up social signals from non-living rats"}, {"key": "B", "value": "B", "text": "distinguish a friendly rat from a hostile one", "content": "distinguish a friendly rat from a hostile one"}, {"key": "C", "value": "C", "text": "attain sociable traits through special training", "content": "attain sociable traits through special training"}, {"key": "D", "value": "D", "text": "send out warning messages to their fellows", "content": "send out warning messages to their fellows"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［精准定位］首段末句介绍奎因等的研究目标（tested whether）：测试老鼠是否能察觉机器鼠发出的社交信号，[A]正确。
［命题解密］“题干+[A]”同义改写首段末句，if...pickup...from non-living rats替换whether.. detect...from robotic rats/non-living beings。
[B]、[C]均利用①句已知信息干扰，[B]改写identify friends...andenemies，但“接收社交信号以分辨敌友”是老鼠已被证实的能力，而非待证实的能力；[C]将need to be highly attuned to social signals断章取义为“老鼠对社交信号不够敏感”，并在此基础上臆断研究者想要观察是否可通过特殊训练提升其技能（attain...through special training）。[D]将研究目标“观察老鼠能否接收/识别（detect）机器鼠（其相似物）发出的社交信息”窜改为完全反向的“观察老鼠是否会向其发出（sendout）信息”。
［技巧总结］本题就首段命制事实题，意在考查新研究的目的，要求考生辨别“研究背景/已知信息”与“研究目标/待验证信息”。可采用思路：先由②句To find out if this extends to...梳理首段逻辑“①句先介绍已知信息，②句引出研究者在已知信息基础之上的进一步研究”，从而明确“②句为正确项来源，且①句很可能被用于设置干扰”。随后重点分析②句，可进一步锁定正确项来源whether rats can detect social signals from robotic rats，并结合前半句得知robotic rats代表non-living beings，从而确定
[A]正确。其余选项或利用①句背景信息干扰（[B]、[C]），或窜改研究目标（[D]）。
They housed eight adult rats with two types研究人员让8只成年鼠与2只不同类型ofrobotic rat—one social and one asocial—for four的机器鼠一一只爱社交，一只不合群days. The robot rats were quite minimalist,共处一室4天。这两只机器鼠外形相当简约resembling a chunkier version of a computer mouse抽象，就像矮胖版的电脑鼠标，靠轮子四处with wheels to move around and colourful markings移动，带有鲜艳的标记。Ⅲl During the experiment, the social robot rat在试验过程中，社交机器鼠跟随生物鼠followed the living rats around, played with the same们四处走动，玩同样的玩具，还会打开笼门toys, and opened cage doors to let trapped rats escape.让被困老鼠逃脱。在此期间，非社交机器鼠②Meanwhile, the asocial robot simply moved forwards则只是前后、左右移动。and backwards and side to side.'
WHERE id = 'c1e6378a-6818-577c-a6ae-2116d521addd';
-- 2020 Q22
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "It followed the social robot.", "content": "It followed the social robot."}, {"key": "B", "value": "B", "text": "It played with some toys.", "content": "It played with some toys."}, {"key": "C", "value": "C", "text": "It set the trapped rats free.", "content": "It set the trapped rats free."}, {"key": "D", "value": "D", "text": "It moved around alone.", "content": "It moved around alone."}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］由the asocial robot、during the experiment定位至第三段末句。该句介绍试验过程中非社交机器鼠的表现：只是前后、左右移动。[D]正确。
［命题解密］正确项[D]同义改写第三段末句，alone点明了句中simply一词暗含的对比之意：与社交机器鼠相反，非社交机器鼠不与老鼠们同游同玩儿，而是独自前后左右移动。
[A]、[B]、[C]均张冠李戴，利用第三段首句社交机器鼠（thesocial robot）的表现捏造干扰，并非题目所问“非社交机器鼠（the asocial robot）行为”，[A]更是将“社交机器鼠跟随生物鼠走动”窜改为原文并未出现的信息“非社交机器鼠跟随社交机器鼠走动”。
［技巧总结］本题考查试验过程中某一对象（非社交机器鼠）的表现，要求考生辨别不同对象的行为，避免张冠李戴。具体来说，可借助During the experiment，thesocial robotrat...Meanwhile，the asocial robot simply...以及关键词对social VS asocial明确“社交鼠”和“非社交鼠”的行为截然不同，锁定②句信息，并警惕①句陷阱。'
WHERE id = 'b1d0d12c-8fa4-5b57-95f3-ac7bfd0206ae';
-- 2020 Q24
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "can remember other rats'' facial features", "content": "can remember other rats'' facial features"}, {"key": "B", "value": "B", "text": "differentiate smells better than sizes", "content": "differentiate smells better than sizes"}, {"key": "C", "value": "C", "text": "respond more to actions than to looks", "content": "respond more to actions than to looks"}, {"key": "D", "value": "D", "text": "can be scared by a plastic box on wheels", "content": "can be scared by a plastic box on wheels"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［精准定位］由题干人名关键词Janet Wiles定位至第六、七段。第六段③句指出，Wiles原以为要给机器鼠加上各种仿真的外形设计（可活动的头、尾等），老鼠才会愿意与其交朋友，但结果证明这些根本没有必要，即：尽管机器鼠样貌不够逼真，但老鼠仍然会因其行动而亲近它，[C]正确。
［命题解密］正确项是对第六段③句We''d assumed... but that wasn''t necessary反映出的“对老鼠来说，机器鼠的样貌没那么重要（其行动更为重要）”的正确解读。
[A]、[B]、[D]利用第六段②③句提及的facial features、scent、smell、size、a plastic box on wheels臆测出“老鼠对面部特征、气味、体型等这些外形特征的具体反应”，但原文意在说明“这些特征的缺失并不妨碍老鼠与机器鼠建立情感联结”（即：老鼠对这些特征并不在意/反应不大），选项与此相悖。从另一个角度看，文中论及的是老鼠对“机器鼠”的反应，并未提及对“其他老鼠”的反应，[A]偏离文意；文中并未提及老鼠对“味道”和“体型大小”的不同反应，[B]捏造比较；文中指出老鼠愿意与机器鼠（带轮子的塑料盒）做朋友，[D]违背文意。
［技巧总结］本题考查某一研究人员对于研究对象的看法，要求考生正确理解人物观点。第六、七段均涉及Wiles观点，需整体理解。另外，理解过程中需结合其身份“研究者之一”，意识到正确项应顺应研究发现。第六段①②句指出研究发现尽管机器鼠外形简陋，老鼠仍然愿意与其交朋友，这令人惊讶；③句Wiles以虚拟语气指出“我们原以为必须给它加上…但（结果证明）没有必要”。第七段首句Wiles以让步结构强调“机器鼠对社交信号高度敏感，哪怕它来自外形设计简陋的机器鼠”。整体理解可知，Wiles意在说明“机器鼠外形不重要，其行动（回应第三段内容）已足以引起老鼠的交友意愿”，[C]正确。'
WHERE id = '1faad9a8-e6cd-594a-a59a-ece75baeb574';
-- 2020 Q25
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "appear to be adaptable to new surroundings", "content": "appear to be adaptable to new surroundings"}, {"key": "B", "value": "B", "text": "are more socially active than other animals", "content": "are more socially active than other animals"}, {"key": "C", "value": "C", "text": "behave differently from children in socializing", "content": "behave differently from children in socializing"}, {"key": "D", "value": "D", "text": "are more sensitive to social cues than expected", "content": "are more sensitive to social cues than expected"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］第六段①句指出，老鼠与设计简陋的机器鼠交朋友的行为出人意料；②③句解释：研究人员原以为要给机器鼠加上可活动的头和尾巴等，以使其更像老鼠，但事实证明这并不必要。第七段得出结论：老鼠对社交信号非常敏感，即使这些信号来自简单的机器鼠。可见，老鼠对社交信号的敏感超出研究者预期，[D]正确。
［命题解密］[D]正确解读第六段The readiness of the rats..was surprising...及第七段how sensitive...are to social cues，evenwhen...传达的研究人员的“惊讶之情”。
[A]夸大其词：文中只提及“老鼠愿意与机器鼠交朋友”，由此无法推知“老鼠擅长适应新环境”。
[B]捏造比较：文中只提及老鼠对社交信号高度敏感，并未涉及与其他动物的比较。[C]与第七段②句相悖：“老鼠与儿童均可察觉到机器人发出的社交信号”表明“老鼠与儿童在社交方面表现相同”。
［技巧总结］根据题目位置（最后一题）及各选项内容（关于“老鼠”的论断）可知本题很可能考查研究结论。解题时需先把握核心发现，再确认具体细节：首先从首尾段快速提取核心信息：老鼠对社交信号十分敏感，即便这些信号来自简单的机器鼠，大致确定[D]为正确项。随后确认细节：[D]涉及研究人员对研究的预期，可定位至第六段首句surprising，并确认选项正确。而“老鼠适应新环境的能力”、“老鼠社交能力与其他动物的比较”文中均未提及，可排除[A]、[B]；[C]与第七段②句相悖，也错误。'
WHERE id = '5bd17948-2aa2-5235-871a-60c49cf03a83';
-- 2020 Q27
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "foster a stronger sense of teamwork", "content": "foster a stronger sense of teamwork"}, {"key": "B", "value": "B", "text": "finance more research and development", "content": "finance more research and development"}, {"key": "C", "value": "C", "text": "establish closer ties with tech companies", "content": "establish closer ties with tech companies"}, {"key": "D", "value": "D", "text": "operate more globalized companies", "content": "operate more globalized companies"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］第三段首句总领整段：CEO必须拥有更多的技能。随后各句以CEOsmust...、They also...、Then...、Plus...、Beyondthis...分述CEO所需的技能。其中④句指出“美国大公司的全球化程度空前，胜任CEO需要异常广博的知识”，由此可知，CEO需要经营更加全球化的公司。[D]正确。
［命题解密］[D]operate more globalized companies对应句CEO的职责之一Toleadinthat system（其中thatsystem指向④句信息“供应链遍布更多国家的全球化程度空前的大公司”）。
[A]、[C]分别利用have a good sense of、tech companies设置干扰，[A]将原文“金融市场意识”曲解为“团队意识”，[C]将原文“大公司在向科技公司转变（暗示CEO需具备领导科技公司的技能）”曲解为“CEO与科技公司建立更紧密的联系”。[B]由文中financial（指向“金融市场”）捏造出动词finance（给……提供资金），且“研发”在文中无据可依。
［技巧总结］由题干关键词不难定位到第三段，借表列举的逻辑词（also、Then、Plus、Beyondthis）以及相关近义表述（①句概述词many more skills引领后文agood sense of...、better...skills、requires knowledge、haveto do等具体技能/知识）可推知该段呈总分结构。可将各项与②至⑥句分述的各项技能/职责逐一比对：原文未涉及“团队”“研发”，但出现了“科技公司”和“全球化公司”，故需理清CEO与两类公司的逻辑关系，[D]“（CEO）经营全球化公司”近义对应⑥句“（CEO）领导全球化公司”，故该项正确，而[C]暗示CEO领导的公司本身并非科技公司，与⑤句“CEO领导的美国大公司正逐渐成为科技公司”相悖。'
WHERE id = 'b0c2b5ba-7aff-5f89-9dfc-fea2d1d94719';
-- 2020 Q28
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "continual internal opposition", "content": "continual internal opposition"}, {"key": "B", "value": "B", "text": "strict corporate governance", "content": "strict corporate governance"}, {"key": "C", "value": "C", "text": "conservative business strategies", "content": "conservative business strategies"}, {"key": "D", "value": "D", "text": "repeated government warnings", "content": "repeated government warnings"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［精准定位］第四段②③句以让步转折逻辑指出：虽然上世纪70年代以来公司治理变得更为严格，但CEO高薪及上涨趋势恰恰出现于该强化治理时期，故[B]正确。
［命题解密］[B]是对②③句让步转折逻辑中让步信息corporate governance has become a lot tighter and more rigorous的合理概括。
[A]由①句普遍看法“CEO的高薪很大程度上是对员工的剥削”过度推断出原文未论及的信息“公司内部员工一直反对CEO拿高薪”。[C]源自商业常识“企业的商业战略往往影响薪酬水平：如果企业采取保守性战略，其薪酬水平通常也较保守”，但原文并未论及“商业战略”。[D]将②③句关键信息“公司治理力度不断强化（公司自我治理趋严）”曲解为“政府一再告诫公司强化治理（政府对公司的监管趋严）”。
［技巧总结］本题考查让步转折逻辑中的让步信息（由despite体现），定位句②③句中，②句为让步信息，可初步定为答案来源，③句为转折信息（Yet），可用于验证答案来源。具体来看，③句用强调句式“it is + 特定时期 + that + 发生的事件”凸显CEO薪酬上涨情形的特定时期背景during this period of stronger governance，其中stronger governance是对②句主干corporate governance... tighter and more rigorous的高度概括，由此提炼两句逻辑“正是在70年代以来公司治理趋严的这段时期CEO薪酬却在不断上涨”，可确定答案[B]。本题还可借助段落主旨解题：首尾句提示段落主旨要义一驳斥惯常看法“CEO高薪伤害普通员工利益/不合理”，认定其“保障总体利益/合理”，故②③句为论据，表面上介绍CEO涨薪的发生背景，实则以子之矛攻子之盾：既然CEO高薪不合理，则治理严时应“修正”；而事实却正相反。选项“内部反对”“战略保守”和“政府警告”与题干“CEO薪酬上涨”虽能构成矛盾关系，但恰恰迎合了惯常看法，无益于佐证段落主旨。'
WHERE id = '8352b1f6-fedd-52fb-9482-b36ed5d5bbdd';
-- 2020 Q29
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "confirm the status of CEOs", "content": "confirm the status of CEOs"}, {"key": "B", "value": "B", "text": "motive inside candidates", "content": "motive inside candidates"}, {"key": "C", "value": "C", "text": "boost the efficiency of CEOs", "content": "boost the efficiency of CEOs"}, {"key": "D", "value": "D", "text": "increase corporate value", "content": "increase corporate value"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］第四段表明“CEO 高薪是企业严格治理下的举措，不是对普通员工的剥削，而是符合公司整体利益；CEO 高薪制用于吸引外部顶尖人才而非内部安稳人士，故不会牺牲普通员工利益，反而有助于增加公司价值（具体逻辑链为：对 CEO 采取薪酬激励措施（如与股价挂钩）→促使 CEO 提升公司经营业绩→公司股价上涨，公司升值）”。综合可知 [D]正确。
［命题解密］[D]直接对应第五段末句给 CEO 带来高薪的薪酬激励措施的作用 build up corporate value（增加公司价值）。
[A]蕴含逻辑为“薪酬与地位相匹配：高薪可巩固 CEO 的权威地位”，原文并未提及，且选项有意凸显“精英与平民地位有别”反而削减了 CEO 高薪的合理性。[B]与第五段①句信息“最高薪酬是为了吸引外部候选人（即激励外部候选人）而非安逸的内部人选”相悖。[C]结合第三段工作技能等信息将第五段①句“安逸的内部人选”曲解为“在任者安于现状，不思进取，效率低下”，进而臆断出“高薪可激励他们提高干劲”，而该句主旨实为“公司倾向于高薪外聘，而非内部提拔”。
［技巧总结］本题难点一是解读题干信息：can be justified（justify 意为“证明……有道理；为……辩护”）提示考查“高薪的合理性/正当性”，it helps 进一步聚焦考查点“高薪的作用”，根据题文同序原则及末两段论述角度可锁定末两段。难点二是分析定位处长难句：[B]、[D]分别源自第五段的两个长句，对两个长句进行句法语义分析可知，[B]混淆了第五段首句的激励对象（外部候选人而非内部安稳人士），唯有 [D]才是对第五段末句的正确解读。'
WHERE id = 'd860303f-91c8-52cb-8c5a-95893ddf0328';
-- 2020 Q30
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "CEOs Are Not Overpaid", "content": "CEOs Are Not Overpaid"}, {"key": "B", "value": "B", "text": "CEO Pay: Past and Present", "content": "CEO Pay: Past and Present"}, {"key": "C", "value": "C", "text": "CEOs'' Challenges of Today", "content": "CEOs'' Challenges of Today"}, {"key": "D", "value": "D", "text": "CEO Traits: Not Easy to Define", "content": "CEO Traits: Not Easy to Define"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［精准定位］本文首段引人“CEO高薪”现象，第二至末段论述该现象的合理性：其中第二、三段指出CEO高薪与其技能知识相匹配，第四、五段指出CEO高薪不是对公司的价值掠夺，反而能提升公司价值。综合可知，本文主要论述CEO高薪的合理性，[A]最贴合本文主旨。
［命题解密］[A]是基于各段主旨句/关键词（首段CEO pay has gone up；第二段limited CEO talent in aworld...、CEOs really have upped their game...；第三段Today''s CEO...havemany more skills...；第四段it is in the broader corporate interest to recruit top candidates...；第五段high CEOpay is not... depredation at the expense of the rest of the company、build up corporate value）的高度提炼与总结。
[B]只涵盖文中陈述事实“CEO薪酬近几十年来大幅上涨”，未触及文章写作意图（作者立场观点）“为CEO高薪作辩护”。[C]、[D]由第三段“如今CEO需具备更多技能和知识”分别臆断出“当今CEO面临更多挑战”“CEO职责复杂，很难界定”，两项均未涉及文章关注点“CEO的薪酬”。
［技巧总结］文章主旨题的解题步骤大体为：1.借开篇句群/段落（或第二段开头）确定文章话题；2.借复现、近义、反义等语义手段以及并列、转折、总分等逻辑衔接词串联各段大意，梳理文章脉络结构，总结文章主旨；3.带着文章话题主旨比对各项，要注意排除以偏概全、过于笼统、增添枝叶等含有原文部分内容的选项，确定与原文主旨最贴近的选项。具体看本题，由开篇段落可知文章话题为“CEO高薪”，故可排除与薪酬无关的[C]、[D]，串联各段大意（见本题“精准定位”）可知本文立场“CEO高薪有其合理性”，[B]仅涉及薪酬今昔变化，未表达任何论点，[A]以判断句式直陈论点，符合本文立意。'
WHERE id = '7573126d-aef7-54fb-bfff-23729e12c3c1';
-- 2020 Q31
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Its effects are questionable.", "content": "Its effects are questionable."}, {"key": "B", "value": "B", "text": "It has been opposed by a judge.", "content": "It has been opposed by a judge."}, {"key": "C", "value": "C", "text": "It needs tougher enforcement.", "content": "It needs tougher enforcement."}, {"key": "D", "value": "D", "text": "Its fate is yet to be decided.", "content": "Its fate is yet to be decided."}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］第二段末句明确指出：马德里“清洁空气区”的未来看起来很不明朗。也即，它的命运尚未确定。故[D]正确。
［命题解密］正确项[D]fate...yet to be decided同义改写第二段末句future looks uncertain。
[A]根据第一段末句“市议会暂停实施”第二段首句“市长反对”捏造出其反对理由“（实施）效果不确定”，但很明显与第二段①句despite所引出的客观事实 its success in improving air quality（‘清洁空气区’在改善空气质量方面取得良好效果）相悖；[C]则根据第一段②句“暂停实施”第二段①句客观事实“在改善空气质量方面取得良好效果”糅杂臆造出“清洁空气区”效果良好，市议会不应该暂停实施，理应得到更严厉的执行”，且由第二段②句“市政府中止实施VS法官责令恢复”可知“马德里清洁空气区”面临的问题并非“执行不力”，而是“能否继续实施”。[B]将反对“清洁空气区”的主体由第二段①句中的“市长”偷换为②句中的“法官”，而②句明确指出“法官推翻市议会决定，并责令恢复收取罚金（也即，支持“清洁空气区”）。
［技巧总结］Which型事实细节题的典型解题思路是“利用选项关键词回文对应一比对判别对错”。如本题，首先根据试题命制顺序按照文章由前至后原则以及题干关键词将范围限定至第一、二段，再根据选项关键词（核心名词/动词）将各选项回文定位：[A]effects对应第二段①句its success in improving、[B]ajudge对应第二段②句，[C]tougher enforcement对应第一段②句suspended enforcement，[D]Itsfate对应第二段③句thezone''sfuture。随后一一比对发现，[D]为原文同义转述。'
WHERE id = '90261b64-0cbf-5416-8616-78fe1f6fd83c';
-- 2020 Q32
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "They are biased against car manufacturers.", "content": "They are biased against car manufacturers."}, {"key": "B", "value": "B", "text": "They prove impractical for city councils.", "content": "They prove impractical for city councils."}, {"key": "C", "value": "C", "text": "They are deemed too mild for politicians.", "content": "They are deemed too mild for politicians."}, {"key": "D", "value": "D", "text": "They put too much burden on individual motorists.", "content": "They put too much burden on individual motorists."}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］第三段①句指出市级污浊空气治理措施的一个薄弱之处：引发政治争议、易招致抨击；②句阐释原因：市级措施将空气清洁成本加诸车主个人而非引发有毒污染的真正“凶手”汽车生产商。可见，车主个人被迫承担了本不属于自己而应属于汽车生产商的责任，故[D]正确。
［命题解密］题干+[D]put too much burden on individual motorists是对第三段段落主旨句 Among other weaknesses，the measures...are...That''s because they put the costs...on to individual drivers...rather than on to the car manufacturers...的高度概括。
[A]将第三段②句取舍结构put the costs...onto A...rather than onto B中的A、B对调，将不公允对象由“车主个人”调换为“汽车生产商”（注：biased against...“对……有成见/不公允”与biasedfor/towards/in favor of...“偏袒……”为反向关系）。[B]将第一段②句作者观点“马德里市议会（city council）中止实施‘清洁空气区’这一行为可能致使该措施走向失败（demise）”曲解为市议会观点“马德里清洁空气区可能失败、不切实际（impractical）”，并将其上升为各城市措施的薄弱之处。[C]源自第三段①句politically contentious...vulnerable，错误有二：一将“引发政治争议（即，各派政治家们观点对立）”曲解为“观点一致：政治家们认为处罚力度不够”；二将“易招致抨击、脆弱不堪（即，措施可能被否决/推翻）”曲解为“治理力度不够、太轻”。
［技巧总结］常规思路：定位段围绕“市级措施的薄弱之处”展开论述，关键是理清其中论述逻辑、剥离次要信息、明确weaknesses所指。首先由①句从属结构Among other weaknesses，the measures.. are A确定A为所举市级措施的薄弱处：引发政治争议。再由回指词 + 因果标志词结构（That''s because）可知②句解释①句，而取舍结构Bratherthan（而非）C提示争议来源：将空气净化成本错误施加于车主个人而非汽车生产商。最终敲定[D]。非常规思路：纵观选项发现各选项指向不同人物主体，其中B、C的city councils、politicians在段落中（由weakness可定位至第三段）并无明确提及，而A的car manufacturers、individual motorists则原词复现或同义复现段末原文，进而细读该句发现取舍结构put...onto A rather than onto B，最终锁定[D]为正确项。'
WHERE id = 'f7205989-7a7a-55d8-ac84-ac612c79b4d5';
-- 2020 Q33
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "arouse strong resistance", "content": "arouse strong resistance"}, {"key": "B", "value": "B", "text": "ensure Khan''s electoral success", "content": "ensure Khan''s electoral success"}, {"key": "C", "value": "C", "text": "improve the city''s traffic", "content": "improve the city''s traffic"}, {"key": "D", "value": "D", "text": "discourage car manufacturing", "content": "discourage car manufacturing"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［精准定位］第四段③句指出：如果2021年将超低排放新区扩展至南北环路，一定会激起众多即将受影响的汽车车主的强烈反对，故[A]正确。
［命题解密］正确项[A]arouse strong resistance同义改写③句spark intense opposition。
[B]将第四段③句“萨迪克·汗选举成功将扩展Ulez”颠倒为“扩展Ulez将使萨迪克·汗选举成功”。[C]将第五段③至句所述Ulez的作用“改善空气质量、保障居民生命健康”偷换为“改善交通状况”。[D]将第四段③句Ulez扩展的影响对象“汽车车主”偷换为“汽车生产商”，进而得出Ulez扩展阻碍汽车的生产制造。
［技巧总结］本题考查作者针对Ulez扩展后果/影响的看法。解题关键在利用关键词定位，再于定位句中借助观点表达、因果表达以锁定正确答案。如本题，可先借助题干中extension、Ulez定位到第四段③句，随后借助句内观点表达itissureto、因果表达spark intense opposition即可锁定正确答案[A]。
But mayors and councilors can only do so但是，针对这么一个影响范围远超一城much about a problem that is far bigger than any onecity一镇的（空气污染）问题，市长们、议员们所ortown. They are acting because national能做的也就仅此而已。他们之所以在行动，governments—Britain’s and others across Europehave是因为各国政府一英国以及所有其他欧failed to do so.洲国家的政府一未能做出行动。'
WHERE id = '2598625d-36e8-5343-a627-a6b80c073e95';
-- 2020 Q34
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Local residents.", "content": "Local residents."}, {"key": "B", "value": "B", "text": "Mayors.", "content": "Mayors."}, {"key": "C", "value": "C", "text": "Councilors.", "content": "Councilors."}, {"key": "D", "value": "D", "text": "National governments.", "content": "National governments."}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］第六段②句指出：市长们、市议员们（They的指代内容）之所以在采取行动（各种市级治理措施）是因为国家政府未能采取行动（so指代内容）。可见，作者认为本该由国家政府解决问题，[D]正确。
［命题解密］正确项+题干是对national governments... have failed to do so（failed意为“没有做，未做（应做的事情）”）的正确解读。
[A]将第五段③句中所涉人物主体Local（officials）、residents语义糅杂为local residents，且将居民作为空气污染治理的受益对象偷换为问题解决者。[B]、[C]均截取第六段①句mayors and councilors，但两者均为当前正在采取措施解决问题的主体，与题干所问“谁应该去解决问题却又没去解决”不符。
［技巧总结］常规思路：语义转折、取舍处与全文主旨息息相关，常作为命题焦点出现，所以必须重视but/however/yet等转折词后的内容，对于not...but.../ratherthan/insteadof等取舍结构，则须重点明辨“取”的内容（“舍”常为干扰来源之一）。第六段①句以But与前文形成转折，强调作者否定态度：问题涉及范围过大而市长与市议员能力有限（only...SOmuch），可推知真正主体应在能力上强大于市长、市议员，由此可初步选定[D]。②句主、从句A are acting because B... have failed to do so构成语义对比：“A=They=mayors and councils”正在采取行动VS“B=national governments”本该采取行动却没采取行动，确认[D]正确。非常规思路：四个选项指向不同主体，但全文尤其第六段首句中mayorsand councilors表示两个主体处于并列平行状态（两者行为态度大体一致），故可将与之相关的[B]、[C]两项同时排除，最后再在[A]、[D]中做抉择，无论是借由第六段首句“空气污染问题并非局域性问题而是全局性问题”还是借由文意关注核心“污浊空气治理政策”可舍指向区域性基层人民的[A]而取指向全国性国家政府层面的[D]。'
WHERE id = 'bcd0abf6-fa6c-56a1-8a2a-e4f23522581d';
-- 2020 Q35
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "will raise low-emission car production", "content": "will raise low-emission car production"}, {"key": "B", "value": "B", "text": "should be forced to follow regulations", "content": "should be forced to follow regulations"}, {"key": "C", "value": "C", "text": "will upgrade the design of their vehicles", "content": "will upgrade the design of their vehicles"}, {"key": "D", "value": "D", "text": "should be put under public supervision", "content": "should be put under public supervision"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［精准定位］末段首句指出：目前缺乏更大规模的行动来确保现有管控措施的严格执行、来要求汽车公司生产合规机动车；末句又指出：我们虽在竭尽一切所能却独独没有坚持要求汽车生产商清洁其汽车。言外之意即为，汽车生产商/汽车公司应该被强制要求遵守相关规章制度，故[B]正确。
［命题解密］正确项是末段首末句针对汽车公司所述内容的合理引申。
[A]、[C]均只见①句require auto companies to bring their vehicles into compliance而臆测“汽车公司将积极转型、升级汽车”，而未见其前信息absence“缺乏此类要求”，与第三段末句“汽车公司舞弊以致毒害空气”所隐藏文意“汽车公司无视法律、生产高污染汽车”的消极态度相悖。[D]利用末句We''re doing everything but insist that...望文生义出“我们（普通大众）正竭尽一切所能以坚持要求汽车公司…”，从而推断出“置于公众监督之下”，而句意实为“我们（政府官员们）正在做力所能及之事，却独独没有要求汽车公司”。
［技巧总结］段落推理题通常可以按照“紧贴段落主旨”原则解题。可以先借助段落首末句、或者同义/近义复现所展示的相关语义场、或者特殊的句式等揣摩段落主旨，随后将选项与段落主旨比对，正确项通常不直接对应原文字句，而是段落主旨思想的转述或升华。如本题，末段首尾句分借the absence of a larger effort“缺乏更大规模的行动”、doing everything but insist“做了一切，却独独没有要求”两个隐含否定表达锁定正确项[B]；再有，两句中effort（“特别的行动”）与 insist“坚决要求”指向“更为严格、更具针对性的要求或行动”，properly enforce、regulations、bring into compliance指向“严格遵守规章制度”，auto companies、manufacturers指向“汽车公司”，三者共同指向“需对汽车公司严加管控、强制遵守”，最终敲定[B]正确。'
WHERE id = 'ba3ac9fc-1013-5606-95be-35253a71cd6a';
-- 2020 Q37
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "what their parents expect of them", "content": "what their parents expect of them"}, {"key": "B", "value": "B", "text": "how valuable a counselor''s advice is", "content": "how valuable a counselor''s advice is"}, {"key": "C", "value": "C", "text": "what a tough economic situation is like", "content": "what a tough economic situation is like"}, {"key": "D", "value": "D", "text": "how they differ from past generations", "content": "how they differ from past generations"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［精准定位］第二段③句首先指出，Z世代清楚经济火车失事的惨状。④句紧接着解释：Z世代在2008年经济危机到来之时正是易受影响的孩子，当时他们许多人的父母失去了工作或毕生积蓄。由此可知，Z世代非常明白“严酷的经济形势是什么样子”，[C]正确。
［命题解密］正确项[C]中（keenly aware）what a tough economic situation is like是对③句（know）what an economic train wreck looks like的同义转换。
[A]对④5句强加因果，认为Z世代“对冒险不感兴趣”是迎合经济危机中“丢掉工作或毕生积蓄”的父母之“期待”的结果，但文中并未提及他们父母的期待。[B]将②句内容“职业顾问和专家认为Z世代是头脑清醒的经济实用主义者”歪曲为“Z世代认同并珍惜职业顾问的建议”。[D]将①句事实“Z世代与千禧一代不同”歪曲为“Z世代知道自己与前几代人的区别”。
［技巧总结］本题继续围绕Z世代进行考查，涉及Z世代的主观感受，解题关键是结合题干和选项中的关键词回文定位，然后比对信息确定答案。具体来看：题干中Generation Zs are keenly aware同义替换原文③句中Gen Zs know，因此正确答案应该是对原文what an economic train wreck looks like的同义改写，故可直接锁定[C]。其他三项均利用该段中涉及的其他对象进行干扰（[A]涉及“父母”、[B]涉及“顾问”[D]涉及“千禧一代”），均不是Z世代的认识对象。'
WHERE id = '2cfa1cba-1f8c-5537-9e54-07e3ecc2aa39';
-- 2020 Q40
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "less realistic", "content": "less realistic"}, {"key": "B", "value": "B", "text": "less adventurous", "content": "less adventurous"}, {"key": "C", "value": "C", "text": "more diligent", "content": "more diligent"}, {"key": "D", "value": "D", "text": "more generous", "content": "more generous"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［精准定位］根据题干人名Michelsen及关键词Generation Zs定位至第四段③④句。两句指出，Z世代寻求确定性与稳定性、不愿冒风险，[B]是对这一性格特点的同义改写。
［命题解密］正确项[B]是对looking for more certainty and stability、quite risk averse的同义改写。
[A]与Z世代“高度重视（工作）稳定性”所体现的“讲求现实（practical、pragmatist）”相。[C]、[D]将第三段个别词汇inspiring purpose、a sense of being dedicated to a cause体现的“崇高的职业目标、为崇高事业作贡献”分别歪曲为“Z世代辛勤工作”和“Z世代乐于帮助别人”，既不符合原文信息，原文中也未将Z世代与千禧一代在这两个方面的差异进行比较。
［技巧总结］本题考查两个群体之间的特征对比，可按照“分类整理各群体特征一与选项比对后确定答案”的思路解题，具体来看：1.Michelsen针对千禧一代和Z世代分别给出“追求更多灵活性”和“追求更多确定性和稳定性、极力规避风险”的描述；2.题干询问Z世代的特征，浏览各选项后可轻松锁定[B]。'
WHERE id = 'af897db4-f759-5b85-bd9b-954409170201';
-- 2021 Q1
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "therefore", "content": "therefore"}, {"key": "B", "value": "B", "text": "however", "content": "however"}, {"key": "C", "value": "C", "text": "again", "content": "again"}, {"key": "D", "value": "D", "text": "moreover", "content": "moreover"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］上下文语义逻辑。
［解题思路］首句指出，设定目标并不难；空格句指出，______，认识到这些目标的负面影响要难得多。可见，两句存在语义反差（It''s not difficult vs It is much harder）,空格词作为插入语应体现两句间的转折对比逻辑，[B]however符合要求。
［错项排除］[A]therefore用于引出结果，[D]moreover表示递进关系，用于引出补充或支撑前一论述的新信息，但“认识目标设定的负面影响较难”并非“目标设定不难”导致的结果，也非对其的进一步补充说明或论证。[C]again用于表示“某事在发生之后再次发生”或“某事又回到过去的状态或地方”，例:You''ll soon feel well again.（你很快就会康复的。）但①②句间不存在再次发生的事件或两个相同的状态/地点，故“再一次，返回原处”无从谈起。'
WHERE id = 'a26d5e7d-e8b6-5b90-bfdb-0c7f89e6133b';
-- 2021 Q2
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Emphasize", "content": "Emphasize"}, {"key": "B", "value": "B", "text": "Identify", "content": "Identify"}, {"key": "C", "value": "C", "text": "Assess", "content": "Assess"}, {"key": "D", "value": "D", "text": "Explain", "content": "Explain"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］上下文语义+动词辨析。
［解题思路］③④句指出，与工作相关的行为含有多个要素，______其中一个，其他就会变得扭曲。此两句与①②句“目标设定会带来不良影响”之间不存在任何显性关联词，表明两者间存在顺承关系，③④句“______一个会扭曲其他”应意在解释说明①②句“目标设定的不良影响”，空格词应该与“目标设定（想要达到的标准）”相关，指向“关注，聚焦，以……为目标/重点”等意，[A]Emphasize表示to give special importance to sth“重视”，“重视一个要素”即“将之设立为目标”，故正确。
［错项排除］总体而言，“确认/评估/解释某一个要素”与“其他要素被扭曲”不存在因果关联（and暗藏因果关联），且其语义内涵与“目标设定”关系较远。具体来看，[B]Identify可表示“找到，找出”，例：First of all we must identify the problem areas.（首先我们必须找出问题所在。）但由上句可知，各个要素是“已知的、显现的”。[C]Assess指的是对人/物的性质、质量而非构成成分进行评定。[D]Explain重“介绍事物的细节或原因以使他人理解”，其解释的对象应该是“某种复杂难解的事物或行为等”，而one已经是“被分解的、不难理解的一个要素”。'
WHERE id = 'f1b87586-83c0-568b-9347-c7b182bfb9f3';
-- 2021 Q3
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "nearly", "content": "nearly"}, {"key": "B", "value": "B", "text": "curiously", "content": "curiously"}, {"key": "C", "value": "C", "text": "eagerly", "content": "eagerly"}, {"key": "D", "value": "D", "text": "quickly", "content": "quickly"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义+副词辨析。
［解题思路］空格句指出，乘坐伦敦的公交车出行，你就会______ 明白这（this回指上段末句“目标设定的消极影响：扭曲目标以外的要素”）是如何发生在司机身上的；结合上文“要理解目标设定的负面影响很难”以及下文“公交司机频繁闯红灯”可知，空格句意在引岀公交车司机频繁闯红灯的例子来形象展示“设定目标的危害”，空格词应重点传递这一示例作用的有效性，[D]quickly与see结合表示“快速明白/理解”，故正确。
［错项排除］[A]nearly表程度，暗示“不能完全理解/明白”，与事例“公交司机频繁闯灯（负面语义赫然纸上）”的服务目的“让大家理解目标设定的不良影响”不符。[B]curiously.CC]eagerly均利用人物心理“人们在车上好奇/热切地看”捏造干扰，但此处see表示思维上的“理解/明白”，而非行为上的“看/张望”，故与“好奇地”“热切地”无法形成合理搭配。
［选项释义与词汇辨析］[A]nearly: 几乎；将近
[B]curiously: 好奇地
[C]eagerly: 热切地
[D]quickly: 迅速地；很快地'
WHERE id = '3ad2ea30-6be2-5a07-80de-eb1149460673';
-- 2021 Q4
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "claim", "content": "claim"}, {"key": "B", "value": "B", "text": "prove", "content": "prove"}, {"key": "C", "value": "C", "text": "check", "content": "check"}, {"key": "D", "value": "D", "text": "recall", "content": "recall"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义+动词辨析。
［解题思路］空格句提出问题，有检票员_______人们已经付钱了吗？空格词的逻辑主语为inspectors,宾语为具体的情况that people have paid;故空格词应表示公交车上检票员的动作行为，结合常识不难判断空格词应表示“检查，核实，核查”等，[C]check可表示to find out if sth/sb is correct or true “查明，核实”,“核实人们是否购票”与检票员的职责对应，故正确。
［错项排除］[A]claim可表示“索取；索要”，后应接费用、利益等，如claim unemployment benefit（申领失业救济金），而本句中空格词的宾语为“人们是否已经付款/买票”这一具体情况，语义上无法搭配。[B]prove表示“（用证据、论据）证明某事属实”，[D]recall后接宾语从句时表示“回想起某事”，但检票员的职责是“核实/确保”而非“证明/回想起”乘客已经付钱（应该是“乘客”而非“检票员”用证据证明自己已经付钱，也只有“乘客”自己才能想起自己已经付钱）。
［选项释义与词汇辨析］[A]claim: 宣称；要求；索要
[B]prove: 证明；证实
[D]recall: 记起；使想起
[C]check: 可表示to find out if sth/sb is correct or'
WHERE id = '092e0dd4-0c63-5eec-b16c-574a15777889';
-- 2021 Q5
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "threatened", "content": "threatened"}, {"key": "B", "value": "B", "text": "ignored", "content": "ignored"}, {"key": "C", "value": "C", "text": "mocked", "content": "mocked"}, {"key": "D", "value": "D", "text": "blamed", "content": "blamed"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］上下文语义+动词辨析。
［解题思路］空格句前句提出问题：那些跑着追赶公交的人怎么样了？空格句作出回答：他们被______。结合空格上下文“公交车上无人查票，司机频繁闯红灯”可知本句应在讲述公交（司机）对待“追赶着想要赶上车的人”的态度，[B]ignored有“佯装未见，不予理睬”之意，契合上下文语境“对乘客是否购票无视，对路上车辆行人/车上乘客安全无视”，故正确。结合第四段③句“人们抱怨车辆晚点”亦可佐证“司机为赶时间会忽略那些还在跑着追赶公交的人”。
［错项排除］[A]、[C]、[D]均利用常规思维“某些人（其他乘客、路人）会威胁/嘲笑/责怪那些跑着追赶公交车的人”设障，但都无法契合上下文“无人查票、频繁闯灯、人们抱怨晚点”所传递的“司机为争抢时间而无视收益、无视安全、无视乘客上车的需求”。
［选项释义与词汇辨析］[A]threatened: 威胁；恐吓
[B]ignored: 忽视；不予理睬
[D]blamed: 责怪；指责'
WHERE id = '12660896-40da-50b3-b953-2190fa29754b';
-- 2021 Q6
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "punctuality", "content": "punctuality"}, {"key": "B", "value": "B", "text": "hospitality", "content": "hospitality"}, {"key": "C", "value": "C", "text": "competition", "content": "competition"}, {"key": "D", "value": "D", "text": "innovation", "content": "innovation"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］上下文语义+名词辨析。
［解题思路］空格句指出原因：因为目标是______。结合空格上文所述伦敦公交的状况“不查车票、不顾追赶公交的人、频繁闯红灯”以及下文“人们抱怨公交车晚点”“司机们根据其行程所用时间……或受到惩罚”可知，此目标应与“时间”有关,[A]punctuality表示the fact or quality of being on time,符合上下文语义逻辑。
［错项排除］[B]hospitality强调“对他人友好、热情的态度”，与上段公交车对跑着追赶公交之人的态度“视而不见”正好相悖。[C]competition强调的是“团队内部成员之间的争抢/争夺”，而上下文并未涉及到“司机之间的竞争”，故排除。[D]innovation由“增加公交车和公交车专用道”捏造而来，但由人们的抱怨及司机受罚的原因可知，这些措施的目的是“保证公交车的速度和班次”，与“创新”无关。
［选项释义与词汇辨析］[A]punctuality: 准时；守时
[B]hospitality: 殷勤好客；款待
[C]competition: 竞争；比赛
[D]innovation: 创新；新思想'
WHERE id = '9b16c695-7606-55da-883b-cef9f69f600d';
-- 2021 Q7
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Yet", "content": "Yet"}, {"key": "B", "value": "B", "text": "So", "content": "So"}, {"key": "C", "value": "C", "text": "Besides", "content": "Besides"}, {"key": "D", "value": "D", "text": "Still", "content": "Still"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］上下文语义逻辑。
［解题思路］空格句前句介绍人们对公交车的抱怨“晚点、班次少”;空格句介绍与公交车有关的措施“增加公交车和公交车道的数量，依据司机的行程时间对其……或惩罚”，可见这些措施是为了解决公交车“晚点、班次少”的问题,人们的抱怨是“因”，相关措施是“果”，空格词应体现因果关系，[B]So 正确。
［错项排除］[A]Yet、[D]Still置于句首时都有转折意味（despite what has just been said）,表示“不过，可是（用在先前说过的内容之后，引出令人惊讶的事实或情况）”，例：The weather was cold and wet. Still, we had a great time.（天气又冷又潮，不过我们仍旧玩得很开心。）但相应整改措施（增加公交车（道）的数量、依据行程时间惩罚）于公众抱怨（晚点、班次少）而言并没有令人惊讶/转折之处。[C]Besides 作副词时，可表示“此外”，常置于句尾，例：I''m capable of doing the work, and a lot more besides.（我有能力做这工作，除此之外，还可以干更多的事。）besides还可表示“而且”，用于补充一个想法或解释，例：I don''t really want to go. Besides, it''s too late now.（我并不真的想去，而且现在太晚了。）上述两义项中besides呈递的是一种并列或递进关联，而“公交系统的应对措施”与“公众抱怨”并非并列/递进关系，而是因果关系。
［选项释义与词汇辨析］[A]Yet: 然而；已经；还
[B]So: 所以；因此
[C]Besides: 此外；而且
[D]Still: 还；仍然；不过'
WHERE id = '5993a341-70b7-51d0-bcfb-1c3daf83d5be';
-- 2021 Q8
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "hired", "content": "hired"}, {"key": "B", "value": "B", "text": "trained", "content": "trained"}, {"key": "C", "value": "C", "text": "rewarded", "content": "rewarded"}, {"key": "D", "value": "D", "text": "grouped", "content": "grouped"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义+动词辨析。
［解题思路］空格句指出，司机们根据其行程所用时间______ 或受到惩罚（_________or punished）。由上句分析可知，这一措施有助于解决“公交车晚点”的问题，即“根据其行程所用时间对司机进行______或惩罚”有利于提高准点率，空格词应与punished语义相对或类似，[C]rewarded表示“奖励，奖赏”，可有效激励司机提高准点率，故正确。
［错项排除］[A]、[B]、[D]均无法与空格句中or“（用以引出另一种可能性）或，或者，还是”所呈递出的“并列语义（即与受罚相并列的另一种可能性）”契合，故排除。
［选项释义与词汇辨析］[D]grouped: （使）成群，成组'
WHERE id = '72642469-9506-5ee8-a2e7-f24c61b63e9a';
-- 2021 Q9
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "only", "content": "only"}, {"key": "B", "value": "B", "text": "rather", "content": "rather"}, {"key": "C", "value": "C", "text": "once", "content": "once"}, {"key": "D", "value": "D", "text": "also", "content": "also"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义+副词辨析。
［解题思路］前一句指出“司机们达到了（准时的）指标（And drivers hit these targets.）”，紧接着用 But 进行语意转折/补充：“但他们____撞到了骑行者（But they [9]hit cyclists.）”。此处呼应前文“只追求单一指标会产生负面后果”，且连用两个 hit（hit these targets / hit cyclists）形成强烈对比：司机们既完成了准点指标，同时也撞到了骑车人，因此填入 [D]also（也）最贴合句意与语境。
［错项排除］[A]only（仅仅）代入后意为“但他们只撞了骑行者”，违背常识与上下文（司机既达成了准点目标，又引发了撞人后果）；[B]rather（反而，相当）若表“反而”通常需与否定结构或 rather than 搭配，置于主谓之间不合此处递进/双关语义；[C]once（曾经，一旦）强调时间上的过去或条件，与全文一般过去时态下并列发生的客观后果不符。
［选项释义与词汇辨析］[A]only: 仅仅；只有
[B]rather: 相当；反而；宁愿
[C]once: 曾经；一旦
[D]also: 也；同样'
WHERE id = '9132fb0c-485b-5046-8e9a-c0f9e97a3207';
-- 2021 Q10
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "comfort", "content": "comfort"}, {"key": "B", "value": "B", "text": "revenue", "content": "revenue"}, {"key": "C", "value": "C", "text": "efficiency", "content": "efficiency"}, {"key": "D", "value": "D", "text": "security", "content": "security"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］条件关系+句内语义。
［解题思路］空格句指出，如果目标变成了______，就会有更多的检票员，定价也会更加灵活。“更多检票员”“更灵活的定价”均与公交收费有关，空格词应传递“票价、金钱、收益”等含义才可与之构成“条件一结果”关联，[B]revenue可表示“（公司、组织或政府的）收入”，正确。
［错项排除］均利用常规思维“公共交通应舒适、高效、安全”设障，但均无法契合主句所示语境“公交费用”，无法与更多检票员、更灵活定价构成“条件一结果”关联。
［选项释义与词汇辨析］[A]comfort: 舒适；安慰
[B]revenue: 收益；收入
[C]efficiency: 效率；功效
[D]security: 安全工作；保护措施'
WHERE id = '97e4cac3-1657-5a50-b5ff-a24cdbb81f5a';
-- 2021 Q11
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "friendly", "content": "friendly"}, {"key": "B", "value": "B", "text": "quiet", "content": "quiet"}, {"key": "C", "value": "C", "text": "cautious", "content": "cautious"}, {"key": "D", "value": "D", "text": "diligent", "content": "diligent"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］条件关系+句内语义。
［解题思路］空格句指出，如果标准变成了安全，就会有更多______司机，他们会遵守交通法规。________ drivers 一方面是条件从句“标准变成了安全”带来的结果，另一方面应该与drivers的定语从句who obeyed traffic laws的语义指向一致，[C]cautious表示being careful about what you say or do, especially to avoid danger“小心谨慎的”，符合上述两项条件。
［错项排除］[A]friendly（友好的）、[B]quiet（安静的；沉稳的）与[D]diligent（勤勉的；尽职的）均利用常规思维设障（看似都是公交车司机的正面品质），但均无法契合条件句所传递的语境“安全”，不能与“将安全作为标准”构成“条件—结果”关联，故均可排除。'
WHERE id = '5f1e3abf-eff1-5fef-a043-98d76cbf290c';
-- 2021 Q12
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "purpose", "content": "purpose"}, {"key": "B", "value": "B", "text": "problem", "content": "problem"}, {"key": "C", "value": "C", "text": "prejudice", "content": "prejudice"}, {"key": "D", "value": "D", "text": "policy", "content": "policy"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］段际逻辑+名词词义辨析。
［解题思路］空格句指出，还存在另一个______。而上文伦敦公交示例“为了实现准时，对收益、对安全、对意欲乘车的顾客熟视无睹；而如若将目标设置为安全或收益，又无法做到准时”意在说明首段所提出的“设定目标的负面影响：使得目标以外的要素受到扭曲”，此处应接续介绍目标设定的另一负面影响（another________），且由本段末句“一个小时的航程现在号称需要两小时”所传递出的贬义色彩也能感知此空格应表“问题，负面影响”等，[B]problem正确。
［错项排除］从总体语义导向看，[A]、[D]均为中性（偏正面）语义，与段间并列逻辑矛盾。具体而言，[A]purpose表示抽象的“意义”时指“人生或生活的意义/目的感”，例:Volunteer work gives her life（a sense of） purpose.（做志愿工作使她的生活有了意义。） [D]policy可指“宏观政治或经济上的政策、方针”，也可指“某种行事的原则”,例：Honesty is the best policy.（诚实为上。）但空格后“人们（已经）变得极具创意”强调的是一种已然发生的事态变化，并非指向常态性的生活目标、行事原则，故均排除。[C]prejudice虽为负面语义，但着力强调的是一种负面态度/看法，也无法与空格后所述事实“事态变化”相契合。'
WHERE id = '034097dd-7d68-595d-91b8-2e95a202613d';
-- 2021 Q14
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "break", "content": "break"}, {"key": "B", "value": "B", "text": "trip", "content": "trip"}, {"key": "C", "value": "C", "text": "departure", "content": "departure"}, {"key": "D", "value": "D", "text": "transfer", "content": "transfer"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］上下文语义+名词辨析。
［解题思路］空格句指出，航空公司只是修改了一下_______所需的时间。后一句具体介绍航空公司如何修改时间：一小时的航程被号称为两小时（one-hour flight -> two-hour flight）。可见，航空公司修改的是“一趟航行/航程（flight）”所需的时间，空格词应与flight近义，[B]trip表示“出行，旅行”，正确。
［错项排除］[A]break（休息；间歇）、[C]departure（离开；出发）与[D]transfer（中转；换乘）分别利用航班的“经停/起飞/中转”时间捏造干扰，但由 one-hour flight -> two-hour flight 可知，航空公司修改的不是旅程中间某一阶段所花费的时间，而是整个旅程总共耗费的时间；另外，departure time 指航班起飞的时间点，与 is meant to take（时间段）无法搭配，故均可排除。'
WHERE id = 'c6a77b93-0fb9-5d68-8286-670e3ea2e381';
-- 2021 Q15
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "moral", "content": "moral"}, {"key": "B", "value": "B", "text": "background", "content": "background"}, {"key": "C", "value": "C", "text": "style", "content": "style"}, {"key": "D", "value": "D", "text": "form", "content": "form"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］上下文语义+名词辨析。
［解题思路］空格句指出：这个故事的______很简单（The [15]of the story is simple.）。空格句下文指出：大部分工作都有多个维度、多个标准，选择一个标准，很可能就要以其他标准为代价。两者之间为顺承阐释关系，可见“工作有多个维度、多个标准，顾此失彼”正是上文伦敦公交与航空公司事例所传递的深层道理与教训，[A]moral（寓意，教益）符合文意。
［错项排除］[B]background（背景）、[C]style（风格）、[D]form（形式）均利用常见搭配设障，但若说“故事的背景/风格/形式简单”，下文应围绕背景、风格或形式展开，无法引出“大多数工作是多维度的”这一规律性启示。'
WHERE id = '965beb77-0bca-58e4-b4ad-b8be426a95b4';
-- 2021 Q16
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "interpret", "content": "interpret"}, {"key": "B", "value": "B", "text": "criticize", "content": "criticize"}, {"key": "C", "value": "C", "text": "sacrifice", "content": "sacrifice"}, {"key": "D", "value": "D", "text": "tolerate", "content": "tolerate"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义+动词辨析。
［解题思路］空格句指出：选择一个工作标准，那么就很可能______ 其他标准。就空格句内部而言,and you may well...传递的是Choose one criterion的结果，根据常识“选择一个意味着舍弃其他”可锁定[C]。就上文语境而言，首段指出“与工作相关的行为含有多个要素，重视一个，其他要素就会扭曲”，第二、三段列举公交车示例“当目标设定为准时时，收益、安全等就会被忽略；当目标设为安全或收益时，准时就无法保证”，整体语境表明空格词应表“损害，放弃，扭曲”等贬义词，[C]sacrifice正确。
［错项排除］总体而言，[A]interpret“领会”、［D］tolerate“容忍”均不符合空格词的贬义语义指向。具体来看，[A]interpret表示“把理解为”或“以某种方式解读”，常用interpret sth as sth结构，[D]tolerate暗示宾语为“不同意、不喜欢或难以接受之事”，但是“解读其他标准”“容忍其他标准”均无法与空格前Choose one“选择一个标准”形成因果关联（and... may well表结果/因果）。[B]criticize虽为消极语义指向，但空格句中Choose... and you may well并不蕴藏“赞扬vs批评”的语意。
［选项释义与词汇辨析］[A]interpret: 诠释；领会；口译
[B]criticize: 批评；批判
[C]sacrifice: 牺牲；舍弃
[D]tolerate: 容许；忍受'
WHERE id = '65044aa0-10ae-5bc5-8f34-9927ec3334cb';
-- 2021 Q17
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "task", "content": "task"}, {"key": "B", "value": "B", "text": "secret", "content": "secret"}, {"key": "C", "value": "C", "text": "product", "content": "product"}, {"key": "D", "value": "D", "text": "cost", "content": "cost"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义+句内语义+名词辨析。
［解题思路］空格句指出：所有事都能以更快的速度、更低的价格完成，但是有______（but there is a [17]）。空格句内部，but 标示语义转折，空格词应指向与 faster, cheaper 相反的负面代价，锁定具有负面语义的 [D]。结合上句“选择一个标准就会以其他标准为代价（at the expense of others）”及下句 negative consequences，[D]cost 表示“代价，损失”，完全符合这一语义逻辑。
［错项排除］[A]task（任务）、[B]secret（秘密）、[C]product（产物）均无法契合空格前后 but、negative consequences 所渲染的负面代价含义。'
WHERE id = '71c28b7c-0ad1-5ebf-999c-f92de5dc3a4a';
-- 2021 Q18
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "leading to", "content": "leading to"}, {"key": "B", "value": "B", "text": "calling for", "content": "calling for"}, {"key": "C", "value": "C", "text": "relating to", "content": "relating to"}, {"key": "D", "value": "D", "text": "accounting for", "content": "accounting for"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义+动词词组辨析。
［解题思路］空格句介绍好的目标的要求：应该要有多个标准______如时间、金钱、质量、顾客反馈等关键因素。根据上文公交车示例“以时间（标准）为目标时，金钱、顾客反馈、质量等（标准）会遭到忽视，以金钱、顾客反馈等（标准）为目标时，时间（标准）会受到忽略”可知空格词后“时间、金钱、质量、顾客反馈等关键因素”同空格词前“标准”语义指向一致，属上下义关联，[C]relating to符合文意。
［错项排除］[A]leading to可用于表示结果，强调的是因果关联；[B]calling for指向的是需求关联；[D]accounting for可用于表示原因，同样传递因果关联，均与句内“指向一致，上下义关联”不符。'
WHERE id = '0f355053-7cba-5350-9435-a91c01657c03';
-- 2021 Q19
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "specify", "content": "specify"}, {"key": "B", "value": "B", "text": "predict", "content": "predict"}, {"key": "C", "value": "C", "text": "restore", "content": "restore"}, {"key": "D", "value": "D", "text": "create", "content": "create"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］上下文语义+动词辨析。
［解题思路］空格句介绍设立好的目标的窍门：不仅要______ 目标的一两个维度，还要了解如何帮助人们更好地……目标。结合上文“好的目标需要有多个标准集成”可知设定一个好的目标首先必须符合“多个标准集成/选择多个标准”这一先决条件，空格词应表“设定，指定，规定，选择，选取”等，[A]specify 表示 to state sth explicitly or in detail,符合语义逻辑。
［错项排除］[B]predict“预测”暗示“目标维度目前尚未出现”,[C]restore“恢复”暗示“目标维度已经遭到破坏”，［D］create表示“创造”时强调“从无到有”，暗示“目标维度并不存在”，而上文已提及“大部分工作都有多个维度和标准”，且并未提及“目标维度遭受破坏”的相关信息，故此三项均不符合上下文语义逻辑。'
WHERE id = '656deb9a-05d5-5a2d-8e13-8b0c0a5b06d5';
-- 2021 Q20
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "modify", "content": "modify"}, {"key": "B", "value": "B", "text": "review", "content": "review"}, {"key": "C", "value": "C", "text": "present", "content": "present"}, {"key": "D", "value": "D", "text": "achieve", "content": "achieve"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］句内语义+动词辨析。
［解题思路］空格句以not only... but also呈现递进关系：不仅要指定目标的一两个维度，还要了解如何帮助人们更好地______目标。空格词应体现对“设立目标”的递进，[D]achieve表示“实现”，从“确立目标”到“实现目标”不仅体现了not only... but also...的递进关系，也充分表现了trick（a way of doing sth that works well）的内在含义。此外，结合本段首两句“探讨目标的后果”可知，本句应关注“目标的实现”。
［错项排除］[A]modify、[B]review均体现了对前述目标的“不赞同、不认可”，且动作发出者应该指向“目标设定者”，这与空格句中所示动作发出者people“目标执行者”不符（文首句明确指出“企业设定目标，员工去实现目标”）。[C]present表示to show or describe sth/sb in a particular way“展现，表现”，但“设立目标”与“展现目标”之间并没有明显的语义递进，也无法体现trick的“智慧方法”之意。'
WHERE id = '92c11f06-06ae-5b26-b191-4284e38554ef';
-- 2021 Q21
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "an increase in full-time employment", "content": "an increase in full-time employment"}, {"key": "B", "value": "B", "text": "an urgent demand for new job skills", "content": "an urgent demand for new job skills"}, {"key": "C", "value": "C", "text": "a steady growth of job opportunities", "content": "a steady growth of job opportunities"}, {"key": "D", "value": "D", "text": "a controversy about the \"core skills\"", "content": "a controversy about the \"core skills\""}]'::jsonb,
    correct_answer = 'B',
    explanation = '［精准定位］根据题干关键词Research by the World Economic Forum定位至首段③句，该句介绍世界经济论坛的研究发现：到2022年，各类职业中平均42%的“核心技能”将发生变化。这一研究发现支撑了②句“工作岗位的技能需求将迅速发生变化”这一时代趋势。结合末句“到2022年是非常短的时间”可知，未来的工作岗位迫切需要新的工作技能，［B］正确。
［命题解密］正确项［B］中 demand for new job skills 是对③句 “core skills” within job roles will change 和②句 the jobs in demand will change rapidly 的同义转述，urgent 对应末句 a very short timeline。
［A］利用首段①句a lot of would-be workers设置干扰，将我们对未来的期望“潜在劳动力不被大量抛弃”误解为“全职就业岗位将增多”，但原文并未涉及“全职工作”这一话题。［C］利用②句the jobs in demand will change rapidly设置干扰，但文中the jobs in demand实指“社会所需的工作（技能）”而非“社会提供的工作机会”，且“迅速变化”不意味着“稳步增长”。［D］由③句“平均42%的核心技能将发生变化”主观臆断出“核心技能存在争议”，但文中并未提及人们对核心技能的不同看法。
［技巧总结］本题为事实细节题，解题关键在于准确锁定关键词。如本题，根据题干可定位至首段③句，其内容是“到2022年，各类职业中42%的核心技能将发生变化”，关键词是core skills和change。“工作的核心技能发生变化”也即“需要新的工作技能”，浏览四个选项可轻松锁定［B］。而并未涉及“工作技能”，［D］虽触及“工作（核心）技能”，但“争议”在文中并未提及。'
WHERE id = '9de58b50-9efc-5fc5-aeaf-cc2db9a08723';
-- 2021 Q24
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "call for policy adjustment", "content": "call for policy adjustment"}, {"key": "B", "value": "B", "text": "change in hiring practices", "content": "change in hiring practices"}, {"key": "C", "value": "C", "text": "lack of medical workers", "content": "lack of medical workers"}, {"key": "D", "value": "D", "text": "sign of economic recovery", "content": "sign of economic recovery"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［精准定位］第三段①句指出，疫情期间失业率居高不下。随后，②③句以具体数据说明疫情导致失业率大幅走高（潜在逻辑：疫情加剧—用人单位用工需求下降—失业率大幅走高），然后转折指出员工短缺的问题依然存在。④句进而以医疗领域员工短缺的现象为例予以佐证。由此可见，［C］正确。
［命题解密］题干 +正确项［C］是对第三段④句 there were still clear shortages of doctors, nurses and other medical personnel 的同义改写。
［A］根据该段所述客观现象“失业率走高、医护人员短缺”主观臆断出“人民不满政府的作为，呼吁调整政策”，但文中并未提及人们对政府政策的诉求。［B］将②③句“二月（疫情初期）员工短缺问题普遍存在—五月（疫情高峰期）员工短缺问题大多不复存在”所体现的“用工需求发生变化”窜改为“用工制度/雇佣惯例发生变化”。［D］与②③句所述现象“失业率由低到高、经济走向低迷”相悖。
［技巧总结］让步转折处常常引出信息重点，也是命题人的关注点。本题对应的第三段中③句后半句although many... not all...形成让步转折，并将语义重点落在“员工短缺问题依然存在（not all had done so）”上；随后④句以“医务人员短缺”进行例证。掌握信息关键点后，很容易就能锁定正确项［C］。'
WHERE id = '0f9fe0e4-019a-52f1-a9ee-0819ad6b68ac';
-- 2021 Q25
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "create job vacancies for the unemployed", "content": "create job vacancies for the unemployed"}, {"key": "B", "value": "B", "text": "prepare their laid-off workers for other jobs", "content": "prepare their laid-off workers for other jobs"}, {"key": "C", "value": "C", "text": "retrain their cabin staff for better services", "content": "retrain their cabin staff for better services"}, {"key": "D", "value": "D", "text": "finance their staff''s college education", "content": "finance their staff''s college education"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［精准定位］由题干关键词Scandinavian Airlines快速定位至末段③句。该句指出，北欧航空公司决定重新培训其下岗员工，以期让他们支援医护人员。［B］与此意相符。
［命题解密］正确项［B］中prepare... for...（给某人进行预备教育或训练）对应末段③句 retraining/reskilled, other jobs 即指末段③句 to support hospital staff。
［A］将北欧航空公司的方案“培训内部失业人员支援外部紧缺人员”曲解为“在公司内部为失业人员创造更多空缺职位”。［C］窜改原文信息：首先将培训对象“下岗空乘人员”扩大为“（所有）空乘人员”，其次将培训目的“支援医护人员”窜改为“提升航空服务”。［D］利用末段末句a Swedish university设置干扰，原文实指“一所瑞典大学也参与了北欧航空公司的下岗员工再培训方案”，而非“北欧航空公司决定资助所有员工接受大学教育”。
［技巧总结］本题容易定位且定位内容只有一句，除了常规的“将原文定位内容与选项一一对比”这种解题方法，还可以从选项出发。首先纵观各项涉及的对象：［A］the unemployed泛指“所有失业人员”，［B］their laid-off workers 特指“该公司下岗员工”，［C］their cabin staff 和［D］their staff 指向“该公司所有（空乘）员工”。而定位句 forced to furlough... their cabin staff、the laid-off workers 针对的是“该公司下岗（空乘）员工”，与此相符的只有［B］项。然后将该项进一步与定位句对比，发现prepare... for other jobs 对应原文 reskilled... to support hospital staff，从而敲定［B］为正确项。'
WHERE id = '7334576a-351e-52fc-a957-43cb124b5e57';
-- 2021 Q29
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "rely largely on imports for fresh produce", "content": "rely largely on imports for fresh produce"}, {"key": "B", "value": "B", "text": "enjoy a steady rise in fruit consumption", "content": "enjoy a steady rise in fruit consumption"}, {"key": "C", "value": "C", "text": "are seeking effective ways to cut calorie intake", "content": "are seeking effective ways to cut calorie intake"}, {"key": "D", "value": "D", "text": "are trying to grow new varieties of grains", "content": "are trying to grow new varieties of grains"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［精准定位］末段①句指出“如今英国人食用的果蔬中仅有23%产自本国”，可知其余77%/大部分都依靠进口，［A］正确。
［命题解密］［A］中 rely largely on imports 是对①句 Just 23 per cent... are currently home-grown 的正确计算和合理推断。
［B］错误理解段中23%和30%两个数据的含义，这里是在指出“产自本国的果蔬占果蔬总食用量的23%，采用最极端手段可以达到30%”，并非“果蔬食用量上升”。［C］和［D］分别将②句“英国人若采用极端手段尽力满足果蔬需求，则需要另找地方种植提供大部分卡路里摄入的谷物等（look for... the grains, sugars, seeds... the vast bulk of our current calorie intake）”曲解为“英国人正寻求减少卡路里摄入”和“英国人正努力培育新的谷物类型”。
［技巧总结］题目就末段考查事实细节，需要将各项核心关键词回文比对，进行合理引申推断，关键在于理清数据关系（①句23%, 30%），辨别信息虚实（②句是在以假定情形说明采用极端手段种植果蔬不可行）：分别利用选项关键名词［A］fresh produce, ［B］fruit consumption, ［C］calorie intake, ［D］grains 定位原文，然后进行比对，发现［B］、［C］、［D］其余部分 enjoy a steady rise、are seeking effective ways to cut、are trying to grow new varieties 歪曲了文中信息，可排除；而［A］rely largely on imports 是对 Just 23 per cent of the fruit and vegetables... are currently home-grown 的正确推算，故为正确项。'
WHERE id = '45172221-b859-553c-af50-68353e84f4af';
-- 2021 Q30
UPDATE public.questions
SET options = '[{"key": "A", "text": "defensive", "value": "A", "content": "defensive"}, {"key": "B", "text": "doubtful", "value": "B", "content": "doubtful"}, {"key": "C", "text": "tolerant", "value": "C", "content": "tolerant"}, {"key": "D", "text": "optimistic", "value": "D", "content": "optimistic"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［精准定位］本文整体脉络为：引出话题“英国粮食自给自足是否可行”（第二段末）——分析问题，先指出就算采用极端手段，也无法满足英国人对动物性食品的需求，唯一可能就是减少动物性饮食，转向植物性饮食（第三、四段），然后进一步指出转向植物性饮食同样不可行，就算采用极端手段，可用土地也无法满足人们的总体需求（第五、六段），可见作者对英国实现自给自足持怀疑态度，［B］正确。
［命题解密］［B］doubtful 准确概括了第二段末 Sounds great—but how feasible is this vision? 第三段末 even covering... wouldn''t allow us、第五段末 Even if... we would achieve only... 第六段末 That is before we look for... 等传递出的作者态度。
［A］错误理解文章总体脉络，将文章“提出一种观点——指出这种美好愿景很难实现”理解为“提出一种观点，为之进行辩护”。［C］将第三段末、第五段末的让步表达（就算……，……）曲解为作者对计划的容忍，但作者实际是以极度夸张的提议来强调计划的不合理。［D］将第二段的“其他人的观点（作者认为很难实现）”当成作者的观点。
［技巧总结］本题考查作者态度，应注意区分作者观点和他人观点，同时注意理解特殊表达传达的作者态度。如第五段末句“就算把所有条件适宜的土地都变成果蔬园地，取消所有的自然保护区，让成千上万的人们搬离家园——我们能实现的粮食产量增长也只有30%而已”并非说明作者真的认为“可以考虑把所有土地变成果蔬园地”，而是要凸显“就算如此，仍不能解决问题，更何况这本身实行起来会造成巨大代价”。'
WHERE id = 'bc3a6553-5c28-5abb-9a82-0ec7a0ea2615';
-- 2021 Q31
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Their engineers were retained.", "content": "Their engineers were retained."}, {"key": "B", "value": "B", "text": "Their market values declined.", "content": "Their market values declined."}, {"key": "C", "value": "C", "text": "Their tech features improved.", "content": "Their tech features improved."}, {"key": "D", "value": "D", "text": "Their products were re-priced.", "content": "Their products were re-priced."}]'::jsonb,
    correct_answer = 'A',
    explanation = '［精准定位］由after their acquisitions定位至第二段首句中later。该段指出Wunderlist与Sunrise被收购后的情况：软件被下架（①句），工程师被留用（②句），故[A]正确。
［命题解密］[A]Their engineers were retained 同义改写第二段②句 Their... engineers stayed on。[B]源于第六段①句their... market value，但此处谈论的是“五大科技巨头的市场价值巨大”而非“Wunderlist与Sunrise的市场价值下滑”。[C]张冠李戴：由第二段①句“微软将它们的最佳性能融入自身产品”，可知科技性能得到提升的对象为微软自家产品而非被收购的两款应用。[D]利用首段①句“微软收购两款软件”与常识“换东家后会重新定价”捏造，但“重新定价”所含的信息“仍在市场上销售”与第二段①句所含的信息“被下架”相悖。
［技巧总结］四个选项的指向性很明确、辨识度也很高，对于此类事实细节题按照“回文定位法”最为合适。根据题干Wunderlist and Sunrise after their acquisitions直接定位至第二段，该段两句成段，第一句指向“软件的命运（下架）”，第二句指向“软件工程师的命运（留用）”，与之相匹配的唯有[A]，其余各选项要么捏造，要么偷换概念。'
WHERE id = 'b1b41992-d881-5a0c-a552-8d64ad1da8a1';
-- 2021 Q43
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Stay calm", "content": "Stay calm"}, {"key": "B", "value": "B", "text": "Stay humble", "content": "Stay humble"}, {"key": "C", "value": "C", "text": "Decide whether to wait", "content": "Decide whether to wait"}, {"key": "D", "value": "D", "text": "Be realistic about the risks", "content": "Be realistic about the risks"}, {"key": "E", "value": "E", "text": "Don''t make judgements", "content": "Don''t make judgements"}, {"key": "F", "value": "F", "text": "Identify a shared goal", "content": "Identify a shared goal"}, {"key": "G", "value": "G", "text": "Ask permission to disagree", "content": "Ask permission to disagree"}]'::jsonb,
    correct_answer = 'G',
    explanation = '［定位/考点］段落主旨匹配（第4段）。
［解题思路］第四段先评价“这一做法（This step）”：看似过于顺从，实则是卸下上司心理防卫的明智之举。后举例说明“这一做法”：向上司请求表达异议的许可。最后指出该做法的作用：让上司更可能听取反对意见。综合可见，G项“请求允许表达异议”与该段主旨一致，其中Ask permission与⑤句Would that be OK的请求之意相符。
［错项排除］B项humble虽近义复现段首deferential,也与④⑤句would like to、Would that be OK体现的谦恭态度相符，但由②至⑤句可知，恭顺是为征得表达异议的许可这一目标服务，⑥⑦句也均围绕“上司许可与否（opt in says yes）”展开，【B】 Stay humble仅契合段落首句，无法概括余下内容，故排除。'
WHERE id = 'bb42d1f8-2299-5833-8fdd-685384bbb560';
-- 2021 Q45
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Stay calm", "content": "Stay calm"}, {"key": "B", "value": "B", "text": "Stay humble", "content": "Stay humble"}, {"key": "C", "value": "C", "text": "Decide whether to wait", "content": "Decide whether to wait"}, {"key": "D", "value": "D", "text": "Be realistic about the risks", "content": "Be realistic about the risks"}, {"key": "E", "value": "E", "text": "Don''t make judgements", "content": "Don''t make judgements"}, {"key": "F", "value": "F", "text": "Identify a shared goal", "content": "Identify a shared goal"}, {"key": "G", "value": "G", "text": "Ask permission to disagree", "content": "Ask permission to disagree"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［定位/考点］段落主旨匹配（第6段）。
［解题思路］第六段先建议读者向上司强调自己仅是在提供“个人观点”而非“绝对真理”，后又提出要采用试探性的表达、收敛自信（talk tentatively and slightly understate your confidence），最后指出要保持好奇心并耐心倾听对方的意见甚至批评（invite critique / Be open to hearing other opinions）。[B]Stay humble（保持谦逊，不要自视甚高）是对这些建议的准确概括，其中 humble 近义复现句中的 understate your confidence。
［错项排除］［E］Don''t make judgements（不要下评判）虽然看似与“不要将自己的观点视作真理”相近，但段落并非反对提出判断（相反作者鼓励清晰陈述观点，只是将其作为个人立场而非绝对事实），而是强调陈述时要谦逊收敛、乐于倾听他人批评，故排除［E］。'
WHERE id = '669e1daa-2cf1-58ef-bfcc-fd7e68420805';
-- 2022 Q1
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "difficult", "content": "difficult"}, {"key": "B", "value": "B", "text": "normal", "content": "normal"}, {"key": "C", "value": "C", "text": "steady", "content": "steady"}, {"key": "D", "value": "D", "text": "pleasant", "content": "pleasant"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］句内语义+上下文语义。
［解题思路］首句说明哈兰•科本的观点：作家总能找到时间来写作；找不到写作时间的人不可称为作家。②句（空格句）指出，对哈兰•科本而言，写作是一份______ 工作—和其他任何工作一样。从②句句内来看，破折号后内容（a job like any other）解释说明a________ job,即空格词应说明写作的“普通/平常”。再联系①句可知，空格句意在说明写作只是一项普通工作，作家也应像其他行业的工作者一样花时间做好本职工作。综上，空格词应表示“平常的/普通的”，［B］normal正确。
［错项排除］［A］、［C］、［D］均可描述写作的特点，且［A］、［D］看似符合①句暗含之意“人们往往很难找到时间来写作；但写作应是作家的优先项/爱做之事”，但三项都与破折号后的解释说明内容不符。'
WHERE id = '81548c26-9d13-54f3-a594-3946fc6d1547';
-- 2022 Q2
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "combined", "content": "combined"}, {"key": "B", "value": "B", "text": "compared", "content": "compared"}, {"key": "C", "value": "C", "text": "confused", "content": "confused"}, {"key": "D", "value": "D", "text": "confronted", "content": "confronted"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］句内语义+上下文语义。
［解题思路］空格句指出，哈兰•科本将写作（it = writing）与修管道（plumbing）________，指出管道工不会在早上醒来后说自己今天没法修理管道。联系上两句内容“如果你是一名作家，那你一定能找到时间来写作；写作和其他任何工作一样”可知，空格句是在将“写作”与最普通的工作“管道修理”相较，以此来直观说明“写作并没有什么特别之处，作家应该像管道工一样尽职尽责地完成工作”。空格词应表示“比较/对比”，compare A with B意为“将A与B比较”，［B］compared正确。
［错项排除］其他三项干扰性在于均能与with搭配，但［A］combine A with B表示“使A和B结合”；［C］confuse A with B表示“将A和B混淆；将A误认为B”；［D］confront A with B表示“使A面对B（令人不快或难处的人、场合）”，均偏离文意。'
WHERE id = 'ab8c6d20-06e9-53ce-b1d8-b62cbb8485f3';
-- 2022 Q3
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "If", "content": "If"}, {"key": "B", "value": "B", "text": "Though", "content": "Though"}, {"key": "C", "value": "C", "text": "Once", "content": "Once"}, {"key": "D", "value": "D", "text": "Unless", "content": "Unless"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］句内语义逻辑+段际衔接。
［解题思路］空格句从句部分指出，______，像现在的大多数作家一样，你干着一份糊口的工作。主句部分则指出，找到写作的时间不……。可见，从句是在引导读者想象自己是一位“边干其他工作养家边写作的作家”，来分析“这种情况下找到写作时间的难易等”，空格词应表示“如果/假设”等以引出假想情况，且这一“假定的具体情形”恰能顺接上段内容，[A]If正确。
［错项排除］[B]Though表转折，利用空格句和随后句的转折关系（But）设障，但though位于句首时，体现的是“句内转折关系”或“对上句的让步”，且不与but成对出现。如Though she was tiny, she had a very loud voice.（虽然她个头很小，嗓门却很大。）I like him. Though he makes me angry sometimes.（我喜欢他，尽管他有时惹我生气。）文中并非though的正确用法。[C]Once表条件，含一定的假设意味，有较强干扰。once与if的区别主要在于：if表示假设，其引出的情况可真可假（可以是真实条件句，也可以是假定情形）；而once（as soon as; when“就；一旦；当时候”）则表示实现某事的条件，其引出的情况一般都为真，如The water is fine once you''re in!（你一旦下了水，就会觉得水里挺舒适！）。文中“你是一名作家”为假设情形而非真实条件，故[C]错误。[D]Unless表示某事不成立的唯一条件，如Unless it rains, the game will be played.（除非下雨，比赛将照常进行=只有下雨，比赛才会取消）,Unless填入文中表示“除非像大多数作家一样干着养家糊口的工作，否则找到写作时间将不是一件……的事”，若空格4表示“困难、不可能等”，则完全成立。这时需借助下句But it''s not impossible先判断空4应大致表示“容易、可行等”，确定unless不符合逻辑。'
WHERE id = '8eff9704-1239-579e-8670-0b56abaf4b16';
-- 2022 Q4
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "enough", "content": "enough"}, {"key": "B", "value": "B", "text": "strange", "content": "strange"}, {"key": "C", "value": "C", "text": "wrong", "content": "wrong"}, {"key": "D", "value": "D", "text": "easy", "content": "easy"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］句内语义+句间逻辑。
［解题思路］空格句指出，如果你像大多数作家一样，干着一份养家糊口的工作，则找到写作时间不______。随后一句则转而指出，但这不是不可能（But it''s not impossible.）。联系两句间逻辑以及常识常识可知句群意在说明作家在养家糊口的同时要找到时间写作“确有难处”，it''s not _________指向“有难度”，空格词应表示“容易/简单”，[D]easy正确。
［错项排除］[A]enough利用“作家需要养家糊口（to pay the bills）”得出貌似合乎逻辑的语义“作家仅仅找时间写作是不够的（还要挣钱养家）”，但从句实则表示“分工并行”（一份工作来养家；同时进行写作），且后句转折指出“但这并非不可能”，故[A]偏离文意。[B]strange / [C]wrong 填入文中表示“找时间写作不奇怪/没有错”，均无法与前后文形成合乎逻辑的语义关系。'
WHERE id = 'd60d57ae-e56c-5165-a87f-d2c66610ed2c';
-- 2022 Q5
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Accept", "content": "Accept"}, {"key": "B", "value": "B", "text": "Explain", "content": "Explain"}, {"key": "C", "value": "C", "text": "Remember", "content": "Remember"}, {"key": "D", "value": "D", "text": "Suppose", "content": "Suppose"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］上下文语义。
［解题思路］空格句指出，______ 大多数畅销书作家当初开始写作的时候都在干着其他赖以谋生的工作。结合前三句大意“干着养家糊口工作的作家要找到写作时间不容易，但并非不可能，只是这需要决心和专注”可知，空格句是在以“畅销书作家大都经历的情形”来提醒/安慰/鼓励读者“开始写作的初期都是辛苦的（要想成为成功作家，必然要经历艰辛）”,[C]Remember正确。
［错项排除］[A]Accept指向“接受/承认（某种对自己不利的情况）”，而空格后为“其他作家的成功经历”，不存在接受/不接受的问题。[B]Explain指向“解释说明某事发生的理由”，而下文中并未展开说明畅销书作家这样做的理由。[D]Suppose用于“假设某种情形”（其后从句常用一般现在时或现在/过去进行时），而空格后从句是在以一般过去时介绍大多数畅销书作家曾有的经历。'
WHERE id = 'a78256f8-f6fd-5953-bf74-a310aa0e88dd';
-- 2022 Q8
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "cause", "content": "cause"}, {"key": "B", "value": "B", "text": "purpose", "content": "purpose"}, {"key": "C", "value": "C", "text": "question", "content": "question"}, {"key": "D", "value": "D", "text": "condition", "content": "condition"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］上下文语义。
［解题思路］空格句指出，正如哈兰•科本所说，这是一个优先项的______。“这(it)”指代II段所述问题“作家能否在从事其他工作的同时找到写作时间”，联系首段的科本观点“如果你找不到时间来写作，那写作就不是你的优先项，你也就不是一名作家”可知，空格句是在点明II段所述问题的实质“作家能否找到写作时间取决于写作是否被视为优先项”，空格词应体现“核心/关键问题”，a question of sth意为“……的问题”，表示问题的本质，[C]question正确。
［错项排除］[A]cause（原因）、[B]purpose（目的）与[D]condition（条件）填入文中分别表示 it（II 段所述问题）为“优先项”的起因、目的和条件，但分析可知，it 与“优先项”实指同一件事，两者为“表—里”关系而非因果或条件关系，故三项均偏离文意。'
WHERE id = 'fd9394cb-7f0b-56c3-be6e-0d8ff06cdc0e';
-- 2022 Q9
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "highlight", "content": "highlight"}, {"key": "B", "value": "B", "text": "sacrifice", "content": "sacrifice"}, {"key": "C", "value": "C", "text": "continue", "content": "continue"}, {"key": "D", "value": "D", "text": "explore", "content": "explore"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］词义分析+上下文语义。
［解题思路］空格句指出，要想让写作成为优先项，你必须______ 一些日常活动和一些自己喜欢做的事。根据 priority 含义 sth that you think is more important than other things and should be dealt with first“优先事项；最重要的事”可知，“日常活动(day-to-day activities)”和“喜欢做的事(some things you really enjoy)”位于写作之后，居于次要地位，应做出让步/牺牲。根据下文spending less time、less socialising也可进一步推测，空格词应表加“减少/牺牲/舍弃”，[B]sacrifice 正确。
［错项排除］[A]highlight 意为 to emphasize sth, especially so that people give it more attention“突出；强调；给予更多关注”，与“日常活动”等的次要地位相悖；[C]continue（继续）与[D]explore（探索）虽能与 activities 搭配，但均无法体现“让位给写作”这一优先项与次要项之间的取舍关系，故三项均可排除。'
WHERE id = '485e6eb5-8889-5a5d-ab9c-81476b02607f';
-- 2022 Q10
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "relations", "content": "relations"}, {"key": "B", "value": "B", "text": "interests", "content": "interests"}, {"key": "C", "value": "C", "text": "memories", "content": "memories"}, {"key": "D", "value": "D", "text": "skills", "content": "skills"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］句内语义+上下文语义。
［解题思路］空格句指出，取决于你的“______”和“生活方式”，这可能意味着要减少花在“看电视”或“听音乐”上的时间。句内分析：your______ and your lifestyle 应能涵盖 watching television or listening to music 等活动 o 句间关联：空格句中 that 指代上句,watching television or listening to music 属于 day-to-day activities and some things you really enjoy,即 your and your lifestyle 应同样胄总体现 day-to-day activities and some things you really enjoy。综上，your and your lifestyle 应表示“兴趣爱好以及生活方式”,[B]interests正确。
［错项排除］[A]、[C]、[D]三项既无法涵盖“看电视”“听音乐”等活动，又无法体现上句的“日常活动和喜欢之事”，可排除。'
WHERE id = 'f93e8a8d-a351-5994-918c-4e5bd814357d';
-- 2022 Q11
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "until", "content": "until"}, {"key": "B", "value": "B", "text": "because", "content": "because"}, {"key": "C", "value": "C", "text": "while", "content": "while"}, {"key": "D", "value": "D", "text": "before", "content": "before"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义+常识。
[B]because 因为
[D]before 在... 以前
［解题思路］空格句指出，要让写作成为优先项，就要减少看电视或听音乐的时间，尽管有人可以写作______ 听音乐。though提示转折，即空格所在部分应指向“不必减少听音乐的时间”，结合常识可知，该部分表示“写作与听音乐可同时进行，两者并不冲突”，空格词应表示“与……同时”，[C]while正确。
［错项排除］[A]until填入文中表示“直到听音乐前一直写作”意即“一开始听音乐就要停止写作”,表明写作需要让位于听音乐，不符合写作作为“优先项”的地位。[B]because填入文中表示“写作是因为听音乐”，显然不合逻辑，也无法和前半句形成转折。[D]before填入文中表示“在听音乐前写作”，同样表明两项活动无法同时进行，在时间上有冲突，无法与前半句形成转折。'
WHERE id = 'fe3f51c4-c2b7-5590-a22f-4d041724e717';
-- 2022 Q12
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "put up with", "content": "put up with"}, {"key": "B", "value": "B", "text": "make up for", "content": "make up for"}, {"key": "C", "value": "C", "text": "hang on to", "content": "hang on to"}, {"key": "D", "value": "D", "text": "cut down on", "content": "cut down on"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义+固定短语。
［解题思路］空格句指出，你可能不得不
[B]make up for 补偿；弥补
[D]cut down on 削减；减少锻炼或运动的量。其中，“锻炼（exercise）”“运动（sport）”指向兴趣爱好/生活方式，可见空格句承上继续列举为了写作需要做出牺牲的活动，空格词应与上文 sacrifice‘spending less time 语义同向,表示“减少”,[D]cut down on 正确。
［错项排除］[A]、[C]指向“保持现有的运动的量”,[B]指向“以其他方式补上运动量”,三项均错误。'
WHERE id = '909893e6-ae96-5d3a-a89d-e5059dd4cc31';
-- 2022 Q13
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "intelligent", "content": "intelligent"}, {"key": "B", "value": "B", "text": "occasional", "content": "occasional"}, {"key": "C", "value": "C", "text": "intensive", "content": "intensive"}, {"key": "D", "value": "D", "text": "emotional", "content": "emotional"}]'::jsonb,
    correct_answer = 'B',
    explanation = '［考点提炼］形容词词义辨析与上下文对比逻辑。
［解题思路］空格句指出，你将不得不让使用社交媒体成为一项______活动（an [13]activity）。联系上文“减少看电视、听音乐与运动时间”可知，“使用社交媒体”同样是需要为写作让路、作出时间妥协的活动，空格词应体现“偶尔为之的、非经常性的”含义，与后句“每日例行的、耗费时间的（daily, time-consuming）”形成反义照应，故选［B］occasional。
［错项排除］［A］intelligent（明智的、智能的）与［D］emotional（情感的、情绪化的）均偏离“活动占用时间频率”这一核心语义场；［C］intensive（集中的、高强度的）意指加大投入精力与时间，与全文“削减社交娱乐时间以保证写作”的方向完全相反。'
WHERE id = '727984e4-c7af-551c-bda7-a24edb08578d';
-- 2022 Q14
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "habit", "content": "habit"}, {"key": "B", "value": "B", "text": "test", "content": "test"}, {"key": "C", "value": "C", "text": "decision", "content": "decision"}, {"key": "D", "value": "D", "text": "plan", "content": "plan"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］句内语义。
［解题思路］空格句指出，要让使用社交媒体成为一项偶尔为之的活动，而不是每日例行的、耗费时间的______。取舍结构 rather than 表明，a daily, time-consuming 应与“an occasional activity（偶尔为之的活动）”语义相对，再结合空格前修饰成分daily（每日例行的）、time-consuming（耗费时间的）可知，空格词应表示“日常习惯/常规活动”，［A］habit正确。
［错项排除］[B]test（测验；考验）、[C]decision（决定）和[D]plan（计划）均可与 daily, time-consuming 搭配，但均无法与前文的 occasional activity（偶尔为之的活动）形成“偶发行为 vs 固定惯例”的对比，不符合 rather than 所体现的取舍逻辑，故均可排除。'
WHERE id = 'a22a18d4-b1a9-57f8-9c48-922d7b26f4ad';
-- 2022 Q15
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "tough", "content": "tough"}, {"key": "B", "value": "B", "text": "gentle", "content": "gentle"}, {"key": "C", "value": "C", "text": "rapid", "content": "rapid"}, {"key": "D", "value": "D", "text": "funny", "content": "funny"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］句内语义+上下文语义。
［解题思路］空格句指出，这是一条______ 学习曲线，而且并不一定能让你大受欢迎。结合上文可知，“这(It)”概括上文内容“为了找出写作时间，牺牲掉多种兴趣爱好及日常活动”。此处learning curve含义不明，应根据语义逻辑解题。首先进行句内分析：结合其字面义“学习曲线”和“并不一定能让你大受欢迎”，可推测learning curve指“学习过程”，a________ learning curve应指“一条艰难的/曲折的学习曲线”,体现“虽然过程艰难，但结果不一定如愿”之意，空格词应体现“艰难的/痛苦的/需要毅力的”等意。随后，结合上文用词 have to sacrifice, have to cut down on、have to make、have to be less 等隐含的“虽不情愿但不得不努力减少自己用于多种兴趣爱好的时间”，可进一步确认这一推测，［A］tough正确。
［错项排除］[B]gentle（温和的；平缓的）、[C]rapid（快速的；迅速的）与[D]funny（有趣的；滑稽的）语义色彩均偏正面或中性轻松，不符合上文“不得不克服困难、咬牙取舍”的沉重感；另外，[B]填入文中前后两个分句无法顺接（“过程平缓顺畅却并不总能让你受欢迎”不合逻辑），[C]侧重“速度快”亦不能契合艰难取舍的过程，[D]看似能形成顺畅表意（“有趣不一定让人受欢迎”），实则偏离文意，故均可排除。'
WHERE id = '48b6c45c-e75a-5e92-9faf-6035c497e360';
-- 2022 Q16
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "in place of", "content": "in place of"}, {"key": "B", "value": "B", "text": "in charge of", "content": "in charge of"}, {"key": "C", "value": "C", "text": "in response to", "content": "in response to"}, {"key": "D", "value": "D", "text": "in addition to", "content": "in addition to"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义。
［解题思路］空格句指出，只有一件事你应该尽力留出一些时间去做，___写作—那就是阅读。上文提到，作家应将写作视为优先项，需为此牺牲一系列日常活动和兴趣爱好。联系可知，空格句是在转承上段，指出唯有“阅读”是唯一必须留时间去做的事，是重要性仅次于写作的事，故空格词应表示“除……之外/仅次于”，［D］in addition to正确。
［错项排除］［A］填入文中表示“阅读可代替写作”，这与本文主题“作家如何寻找写作时间”不符，且与随后一句信息“阅读是写作必不可少的支撑”不一致。［B］填入文中表示“阅读负责/主管写作”，貌似符合实际情形“阅读面很大程度上决定你的写作水平”，但实则不合英文逻辑。［C］利用“阅读是为了应对写作的需求”这一常识设置干扰，但 in response to(response 意为 a reaction to sth that has happened)意为“对……做出反应/响应”，实际上并不能表达这种需求关系。'
WHERE id = '9cb7f685-8e34-5127-ba30-88f97f7c983e';
-- 2022 Q18
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "duller", "content": "duller"}, {"key": "B", "value": "B", "text": "harder", "content": "harder"}, {"key": "C", "value": "C", "text": "quieter", "content": "quieter"}, {"key": "D", "value": "D", "text": "quicker", "content": "quicker"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义。
［解题思路］末段①句指出，时间是有限的。②句（空格句）指出，年龄越大，时间似乎流逝得________。③句以We need to...顺而提出建议：确定活动的优先次序，将大部分时间花在我们真正要做的事情上。联系全文可知，末段进行升华，提醒读者时间有限、光阴飞逝，应将精力集中于优先事项。故空格词应表示“更快地”，[D]quicker正确。
［错项排除］[A]、[B]、[C]三项均能在一定程度上体现年老（The older you get）的生活的特点，但无法与前后文内容顺接。'
WHERE id = '925ed4e6-6a76-56ba-badc-b0b33c7bfc25';
-- 2022 Q19
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "peacefully", "content": "peacefully"}, {"key": "B", "value": "B", "text": "generously", "content": "generously"}, {"key": "C", "value": "C", "text": "productively", "content": "productively"}, {"key": "D", "value": "D", "text": "gratefully", "content": "gratefully"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［考点提炼］句内语义+上下文语义。
［解题思路］空格句指出，我们要尽可能谨慎且______ 地利用时间，这意味着要确定活动的优先次序，以便将大多数时间花在我们真正要做的事情上。从句内来看，空格词应与其前的并列副词carefully（谨慎地）指向一致，“谨慎、______利用时间”应与其后的解释性从句“确定活动的优先次序，将时间花在真正要做的事上”语义一致，空格词应表示“合理地/有效地/明智地”等。此外，由上两句“时间有限、光阴飞逝”也可得出此结论，[C]productively正确。
［错项排除］[A]peacefully虽与carefully搭配合理，但其强调“安静地、平和地”做某事，文中并未体现这一内容。[B]generously强调做某事时毫不吝啬、慷慨大方，与前后文意相悖。[D]gratefully能与其前顺接，形成“时间有限，且年龄越大流逝越快，因而我们应认真地、心存感激地利用自己所拥有的时间”这一合理逻辑，但与随后的解释性从句语义不一致，也偏离本文论述对象。'
WHERE id = '8f1dff67-e854-516e-9fdc-a7ec20d74d83';
-- 2022 Q20
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "at most", "content": "at most"}, {"key": "B", "value": "B", "text": "in turn", "content": "in turn"}, {"key": "C", "value": "C", "text": "on average", "content": "on average"}, {"key": "D", "value": "D", "text": "above all", "content": "above all"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［考点提炼］上下文语义。
［解题思路］空格句指出，如果你是一名作家，那意味着一_____ 写作。“那（that）”指代上文的泛泛而谈“我们应确定活动的优先次序，将大多数时间花在真正要做的事情上”。结合句间逻辑（从面向所有人到聚焦“作家”）、文章主旨（作家的优先项是写作）以及生活常识（作家的首要任务是写作）可知，故空格词应与prioritising, spend most time on语义指向一致，表示“优先/首要”,[D]above all正确。
［错项排除］[A]at most表示“（数量、程度）等不超过某一数值”，如He faces at most 12 years in prison.（他面临最多12年的监禁。）该短语显然不符合文中语境。[B]in turn 利用中文表达“人们都应将时间花在优先事项上，轮到作家，优先事项则是写作”设置干扰。但in turn并不能用于表达这一情形。该词主要有两种用法：1.表示“多人依顺序做某事”，如We look after him in turn.（我们依次照顾他。）2.表示“继而;转而”，如Increased production will, in turn, lead to increased profits.（增加生产会继而增加利润。）这两种用法均不符合此处情形。[C]on average表示“一系列数值/情况的平均水平”，不符合此处语境。'
WHERE id = 'e20c1f2e-7abd-54c0-bf74-b2efb8233a9b';
-- 2022 Q26
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "over half of the retirees are physically fit for work", "content": "over half of the retirees are physically fit for work"}, {"key": "B", "value": "B", "text": "the old workforce is as active as the younger one", "content": "the old workforce is as active as the younger one"}, {"key": "C", "value": "C", "text": "one in three Americans enjoy earlier retirement", "content": "one in three Americans enjoy earlier retirement"}, {"key": "D", "value": "D", "text": "more Americans are willing to work in retirement", "content": "more Americans are willing to work in retirement"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］根据survey conducted by Harris Poll定位至第二段。该段介绍两项调查结果（...according to a survey... the survey showed）：①句指出，三分之一的美国人已经或计划在退休后继续工作；②句指出，其中有超过一半的人表示他们这样做是因为自己想要继续工作，而不是迫于生计。可见，该调查表明越来越多的美国人选择退休后继续工作，［D］正确。
［命题解密］［D］中的willing to work是对第二段②句they would be employed because they want to, not because they have to的同义替换。
［A］曲解第二段②句的内容：该句指出有超过一半的人表示退休后想要继续工作，但并未提及他们的身体状况，physically fit for work在文中无据可依。［B］由第一段的threatens to upend the old workforce model捏造而来，文中并未在年老员工与年轻员工之间作对比，as active as the younger one在文中缺乏依据，亦排除。［C］one in three Americans enjoy earlier retirement曲解第二段①句的信息，文中指出三分之一的美国人打算在退休后继续工作，而非三分之一的美国人乐于提前退休。［D］既与两项具体发现的核心义相一致，也契合该调查所服务的“现象句”，故为正确项。
［技巧总结］本题题干关键词指向第二段的调查，但需结合第一段的主题句理解第二段的调查结果。第一段指出，越来越多的美国人选择退休后继续工作，这一增长趋势可能会颠覆旧有的劳动力模式。第二段紧接着引用哈里斯民调的调查数据对第一段的观点进行数据支撑。因此，正确项不仅要准确反映第二段的具体调查结果，而且要与第一段的主旨句保持高度一致，［D］完美契合这两点要求。'
WHERE id = 'aec1555c-0c72-5d55-b4dd-f97e61fc5cf7';
-- 2022 Q27
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "retirement may cause problems for them", "content": "retirement may cause problems for them"}, {"key": "B", "value": "B", "text": "boredom can be relieved after retirement", "content": "boredom can be relieved after retirement"}, {"key": "C", "value": "C", "text": "the mental health of retirees is overlooked", "content": "the mental health of retirees is overlooked"}, {"key": "D", "value": "D", "text": "“unretirement” contributes to the economy", "content": "“unretirement” contributes to the economy"}]'::jsonb,
    correct_answer = 'A',
    explanation = '【精准定位】根据题干定位至第三段。该段①②句指出美国人不退休的两个原因“财务需求”和“个人满足感/情感需求”，③句援引受访者的看法具体说明：有人不退休是为了心理健康，有人是为了生计。可见，美国人认为不退休可以避免财务或健康问题，换言之即退休可能会引发这些问题，故［A］正确。
【命题解密】［A］是对美国人的看法“不退休以避免财务或健康问题”的合理推断。
【排除干扰】
［B］利用第三段②句boredom干扰，但与该句暗含文意“不退休可防止无聊”恰好相反。
［C］利用第三段②③句复现词mentally fit干扰，但原文实指“一些人不退休是为了保持心理健康”，并未提及“退休人员的心理健康是否得到关注”。
［D］中the economy源自第三段①句Financial needs，但根据本段末句making ends meet（维持生计）及上段末句even if they had enough money可知，文意实指“不退休旨在满足个人的财务需求”，而非“利于宏观经济发展”。
【技巧总结】推理引申题往往难以直接选出正确项，可采用排除法。本题中，［A］没有明显定位词，难以直接判断正误，可先保留。［B］可根据关键词boredom轻松定位，并判断出该项与文意相悖，故排除。［C］虽近义复现文中关键词mentally fit，但其核心义is overlooked在文中并无依据，故排除。［D］可根据the economy定位至第三段①③句，但回文阅读后发现该项曲解原文含义，故排除。此时再检视［A］，发现该项可由本段主旨“美国人为避免财务和心理问题而不退休”反推而来，故正确。'
WHERE id = 'ee090953-2ec7-59b2-978c-0bd47960b9a4';
-- 2022 Q29
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "investing more in stocks", "content": "investing more in stocks"}, {"key": "B", "value": "B", "text": "taking up odd jobs", "content": "taking up odd jobs"}, {"key": "C", "value": "C", "text": "getting well-paid work", "content": "getting well-paid work"}, {"key": "D", "value": "D", "text": "spending less", "content": "spending less"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］根据increasing their savings定位至第六段②句，该句指出，许多“不退休者”都在增加储蓄，③句进一步指出，这些人最常用的增加储蓄的方法包括减少总体开支（doing this回指increasing their savings），可见［D］正确。
［命题解密］［D］spending less是对第六段③句reducing their overall expenses的同义转述。
［错项排除］[A]investing more in stocks（多投资股票）、[B]taking up odd jobs（打零工）与[C]getting well-paid work（找一份高薪工作）均利用常识“增加收入即可增加储蓄”臆断干扰，但文中第六段③句明确说明最常用的方式是削减总体开支（reducing their overall expenses），三项在文中均未提及，故排除。
［技巧总结］本题易于定位，但定位句并未提供答案，此时应通读对应文段，从上下文寻找线索。先看上文，该句与定位句含义一致，仅指出“美国人在增加储蓄”这一事实，并未具体说明“增储方法”；再看下文，该句出现关键词ways（方法）及表方式的标志词by（通过……；借由……），由此可判断该介词后内容为答案来源，［D］符合原文reducing their overall expenses，故正确。'
WHERE id = 'da1a5552-10d5-5a24-809f-205aec90a803';
-- 2022 Q30
UPDATE public.questions
SET options = '[{"key": "A", "text": "unprepared", "value": "A", "content": "unprepared"}, {"key": "B", "text": "unafraid", "value": "B", "content": "unafraid"}, {"key": "C", "text": "disappointed", "value": "C", "content": "disappointed"}, {"key": "D", "text": "enthusiastic", "value": "D", "content": "enthusiastic"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［精准定位］根据Brent Weiss定位至第七、八段。第七段中，韦斯指出，许多人因担心晚年生计而被迫选择不退休，但他们实际应该在退休前咨询财务顾问，设定长期的财务目标。可见在韦斯眼中，对于退休，许多人尚未做好财务准备。第八段中，韦斯继续指出，退休还是一个情感决定，许多人认为自己不能退休，即尚未做好退休的情感准备。［A］概括了许多人面对退休时的状态，正确。
［命题解密］题干+［A］是对韦斯话语的合理推断。
［B］unafraid与第七段①句are worried about体现的“担忧、害怕”情绪恰好相反。［C］disappointed利用第七段段首的Unfortunately干扰，将之曲解为“退休后的生活令人遗憾、失望”，但此处实际指韦斯对人们的退休观念感到遗憾、惋惜。［D］enthusiastic利用末段emotional干扰，将之曲解为表积极正面的“有感染力的、激动人心的”，但此处该词意为“情感的；情绪的”，为中性词。
［技巧总结］本题易于定位，难点在于定位句表意委婉，考生需进行适度推理。各项均为描述人物状态或态度的词，故应尤其注意定位句处的情感态度表达词（如情态动词、形容词、副词等）。Unfortunately一词奠定了定位段的情感基调，即韦斯评述的是一种令人遗憾惋惜的现象。most challenging形容退休极具挑战，worried、can''t retire体现许多人对退休的担忧和恐惧，只有［A］最能契合这一态度。与此相反，［C］disappointed适用于描述“退休后生活不如预期”的情形，与本题提问对象“选择不退休的许多人”不符，故均排除。'
WHERE id = '2accdad5-e99c-5b92-8712-6739c0ae4bbf';
-- 2022 Q36
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "hard to determine", "content": "hard to determine"}, {"key": "B", "value": "B", "text": "narrowly interpreted", "content": "narrowly interpreted"}, {"key": "C", "value": "C", "text": "difficult to ignore", "content": "difficult to ignore"}, {"key": "D", "value": "D", "text": "poorly summarized", "content": "poorly summarized"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［精准定位］第一段①句指出，科学家们拿不准道德课是否真的能够改变人们的行为，因为证据不足，依赖的大多是人为的实验室测试或是不可靠的自陈报告（are unsure if their lessons can actually change people''s behavior; evidence either way is weak）。换言之，科学家们普遍认为道德课的影响难以确定，故［A］正确。
［命题解密］正确项［A］hard to determine 是对文首句 are unsure 与 evidence either way is weak 的同义概括。
［干扰排除］［B］曲解文意，文中并未指责道德课的效果被狭隘理解。
［C］反向干扰，科学家拿不准其是否有效果，而非其效果难以忽视。
［D］无中生有，文中并未谈及对效果的总结质量问题。
［技巧总结］首句细节题注意对比转折词前的让步与疑问焦点（unsure 对应 hard to determine）。'
WHERE id = '88539a0f-b76b-5daa-800d-5f4fd09c242c';
-- 2022 Q37
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "It is common among students.", "content": "It is common among students."}, {"key": "B", "value": "B", "text": "It is a behavior easy to measure.", "content": "It is a behavior easy to measure."}, {"key": "C", "value": "C", "text": "It is important to students.", "content": "It is important to students."}, {"key": "D", "value": "D", "text": "It is a hot topic in ethics classes.", "content": "It is a hot topic in ethics classes."}]'::jsonb,
    correct_answer = 'B',
    explanation = '［精准定位］第二段②句指出，研究人员之所以选择研究吃肉行为，是因为这是一种普遍且易于量化的行为（eating meat ... is a real-world behavior that is easy to measure）。由此可知，易于测量是选择其作为研究对象的原因，［B］正确。
［命题解密］正确项［B］It is a behavior easy to measure 与原文 easy to measure 直接吻合。
［干扰排除］［A］虽然吃肉很普遍，但研究者看重的是容易客观量化（超市购买记录）。
［C］与［D］属于无中生有，文中并未提及这对学生是否重要或是课堂热点辩题。
［技巧总结］因果事实题直接对照原文中的解释说明从句（a behavior that is easy to measure）。'
WHERE id = 'ec215c23-35fd-5294-8be8-eb8371ccc438';
-- 2022 Q38
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "are seldom critical of their students", "content": "are seldom critical of their students"}, {"key": "B", "value": "B", "text": "are less sociable than other professors", "content": "are less sociable than other professors"}, {"key": "C", "value": "C", "text": "are not sensitive to political issues", "content": "are not sensitive to political issues"}, {"key": "D", "value": "D", "text": "are not necessarily ethically better", "content": "are not necessarily ethically better"}]'::jsonb,
    correct_answer = 'D',
    explanation = '［精准定位］第三段①句指出，研究者此前发现伦理学教授与其他学科教授在诸多现实行为上并无二致（ethics professors do not differ from other professors on a range of behaviors），比如投票率、献血、按时还书等。这说明伦理学教授在道德层面上未必比其他人表现得更好，［D］正确。
［命题解密］正确项［D］are not necessarily ethically better 是对 do not differ from other professors on a range of behaviors 的合理深层引申。
［干扰排除］［A］与［B］主观臆断伦理学教授对学生的宽容度或自身的社交性格，文中无依据。
［C］将句中的投票率细节偷换为对政治问题不敏感。
［技巧总结］例证推理题需要把握引证所要说明的宏观论点：知识上的道德并不必然转化为行为上的优越。'
WHERE id = '7bf202e4-7d07-5660-bf84-a1c3fe8f2089';
-- 2022 Q39
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "permanent", "content": "permanent"}, {"key": "B", "value": "B", "text": "predictable", "content": "predictable"}, {"key": "C", "value": "C", "text": "uncertain", "content": "uncertain"}, {"key": "D", "value": "D", "text": "unrepeatable", "content": "unrepeatable"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［精准定位］第四段②③句指出心理学家尼娜·施特罗明格的看法：她希望这种影响是真实的，但无法排除存在未知的混杂变量；而且即便是真实的，也可能会被另一个轻微的干预所逆转（cannot rule out some unknown confounding variable ... might be reversible）。这表明她认为这种干预的效果是不确定的，［C］正确。
［命题解密］正确项［C］uncertain 是对 cannot rule out some unknown confounding variable 以及 might be reversible 的高度抽象提炼。
［干扰排除］［A］与末句“来得快，去得也快（Easy come, easy go）”完全相悖。
［B］与［D］将不确定性偷换为可预测性或不可重复性。
［技巧总结］人物观点题抓关键情态动词与转折词（cannot rule out, might be reversible 即 uncertain）。'
WHERE id = 'e53f2ac5-dca6-5558-acf3-cd8e428d365a';
-- 2022 Q40
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "can bring psychological benefits", "content": "can bring psychological benefits"}, {"key": "B", "value": "B", "text": "can be analyzed statistically", "content": "can be analyzed statistically"}, {"key": "C", "value": "C", "text": "is a result of multiple factors", "content": "is a result of multiple factors"}, {"key": "D", "value": "D", "text": "is a sign of self-development", "content": "is a sign of self-development"}]'::jsonb,
    correct_answer = 'C',
    explanation = '［精准定位］第五段①句指出，施维茨格贝尔推测最大的影响来自社会影响——即同学或助教在讨论中起到的示范作用；②句接着指出，这一影响可能不仅包含理性说服，还夹杂着情感驱动（not only rational argument but also emotional engagement）。由此可知，学生行为的改变是多种因素共同作用的结果，［C］正确。
［命题解密］正确项［C］is a result of multiple factors 是对文中 social influence, rational argument 以及 emotional engagement 等多重维度的概括。
［干扰排除］［A］无中生有，文中并未讨论心理健康益处。
［B］将前面的实验统计事实误用为对成因的猜测。
［D］过度解读，行为变化并非单纯自我发展的标志。
［技巧总结］归纳总结题注意段落中并列递进的要素结构（not only ... but also ... 提示多重因素驱动）。'
WHERE id = '7c47cec7-595f-5ac0-8a44-25f2b7a26cdc';
-- 2022 Q42
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Make It a Habit", "content": "Make It a Habit"}, {"key": "B", "value": "B", "text": "Don''t Go It Alone", "content": "Don''t Go It Alone"}, {"key": "C", "value": "C", "text": "Start Low, Go Slow", "content": "Start Low, Go Slow"}, {"key": "D", "value": "D", "text": "Talk With Your Doctor", "content": "Talk With Your Doctor"}, {"key": "E", "value": "E", "text": "Listen to Your Body", "content": "Listen to Your Body"}, {"key": "F", "value": "F", "text": "Go Through the Motions", "content": "Go Through the Motions"}, {"key": "G", "value": "G", "text": "Round Out Your Routine", "content": "Round Out Your Routine"}]'::jsonb,
    correct_answer = 'E',
    explanation = '［定位/考点］段落主旨匹配（第3段）。
［解题思路］第三段围绕运动者的身体反应提出建议：如果喘得太厉害，就停下来；如果没有不良反应，就可以多运动一会儿；并对一些严重的症状保持警惕，如果不适的症状过于明显，那么需要立即寻求治疗。可见，第三段建议运动者时刻关注自己的身体状况，运动时要根据身体的不同反应来调整运动量，E项“倾听身体的声音”准确概括该段主旨，其中Listen to与段中stay alert to近义，段中的 breathing feel / feeling symptoms 等是 your body 的具体体现。
［错项排除］C项Go Slow虽与段中back off / Go easier所传达的“停下来”或“慢慢来”之意相符，但②句明确指出如果运动时感觉良好，可以增长运动时间或者提高运动的速度。可见，第三段并非一味强调“要从低基础开始慢慢加码”，而更侧重于强调“根据身体的反应来调整运动的强度和节奏”，故可排除C项。D项的Doctor虽与段中末句的medical attention语义相关，但本段末句仅针对严重的身体症状提议“立即寻求治疗”，并未明确指出要“与医生交谈”,D项无法正确概括段意，故排除。'
WHERE id = '6ba926eb-48b3-5ad9-b358-083e0a9716d4';
-- 2022 Q43
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Make It a Habit", "content": "Make It a Habit"}, {"key": "B", "value": "B", "text": "Don''t Go It Alone", "content": "Don''t Go It Alone"}, {"key": "C", "value": "C", "text": "Start Low, Go Slow", "content": "Start Low, Go Slow"}, {"key": "D", "value": "D", "text": "Talk With Your Doctor", "content": "Talk With Your Doctor"}, {"key": "E", "value": "E", "text": "Listen to Your Body", "content": "Listen to Your Body"}, {"key": "F", "value": "F", "text": "Go Through the Motions", "content": "Go Through the Motions"}, {"key": "G", "value": "G", "text": "Round Out Your Routine", "content": "Round Out Your Routine"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［定位/考点］段落主旨匹配（第4段）。
［解题思路］第四段首先点明坚持不懈是增强体力、耐力和毅力的关键因素，随后提出具体可行的建议“每天步行十分钟”并说明原因。由此可见，第四段强调运动不在时长和强度，而在于每天的坚持，也就是说要将运动变成每天的习惯。A项契合本段段意，故正确。
［错项排除］C项的Go Slow所体现的“慢慢来”看似是段中the easiest“最简单的”之意的体现，但本段重在强调将“每天十分钟运动”这一运动方式的简单易行、可坚持，而非强调“要慢慢增加运动强度”，故排除C项。G项的Round Out“完善”之意虽然与段中的a good start is a great first step所传递的“步行可以作为其他运动形式的补充和过渡”之意相近，但本段段末彰显“步行”的好处，是为了例证“每天运动十分钟”这一建议的可操作性，G项“完善你的常规锻炼”无法概括本段主旨，故排除。'
WHERE id = 'ff6d0e7f-bcac-576c-a207-5765b884d0e7';
-- 2022 Q44
UPDATE public.questions
SET options = '[{"key": "A", "value": "A", "text": "Make It a Habit", "content": "Make It a Habit"}, {"key": "B", "value": "B", "text": "Don''t Go It Alone", "content": "Don''t Go It Alone"}, {"key": "C", "value": "C", "text": "Start Low, Go Slow", "content": "Start Low, Go Slow"}, {"key": "D", "value": "D", "text": "Talk With Your Doctor", "content": "Talk With Your Doctor"}, {"key": "E", "value": "E", "text": "Listen to Your Body", "content": "Listen to Your Body"}, {"key": "F", "value": "F", "text": "Go Through the Motions", "content": "Go Through the Motions"}, {"key": "G", "value": "G", "text": "Round Out Your Routine", "content": "Round Out Your Routine"}]'::jsonb,
    correct_answer = 'F',
    explanation = '［定位/考点］段落主旨匹配（第5段）。
［解题思路］第五段观点鲜明，呈“总一分”的论证模式，围绕“练习动作”这一中心话题展开。首句先引出中心话题“练习动作”，随后以击球、划船、游泳等运动为例，具体解释如何在不具备相关器械或条件的情况下练习动作，末句指出练习动作的益处。F项“练习动作”精确概括本段段意，其中,Go Through近义复现段中的practice, Motions近义复现段中的moves。
［错项排除］G项的Round Out、Routine虽然与段中的prime、moves近义，但第五段侧重强调在不能去打球、划船或游泳的情况下，练习击球、划桨和游泳等动作，以调动运动状态，且prime强调“这些练习会使肌肉为恢复运动做好准备”，并非指完善锻炼组合，G项无法准确概括段落大意。'
WHERE id = '1f2f80ab-95f7-5c2f-8295-419d6cf5be38';
COMMIT;
