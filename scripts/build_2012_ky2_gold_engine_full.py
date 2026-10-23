# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

JSON_PATH = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\2d124f8f-f9af-5b94-9cc9-0087a76ee289.json'

with open(JSON_PATH, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Update Title and basic info
exam_title = '2012年全国硕士研究生入学统一考试英语（二）真题'
if 'exam' in exam_data:
    exam_data['exam']['title'] = exam_title
    exam_data['exam']['total_score'] = 60.0
exam_data['title'] = exam_title

# 2. Reconstruct Passages 0 to 5
p0_content = """Millions of Americans and foreigners see G.I. Joe as a mindless war toy, the symbol of American military adventurism, but that's not how it used to be. To the men and women who [1] in World War II and the people they liberated, the G.I. was the [2] man grown into hero, the poor farm kid torn away from his home, the guy who [3] all the burdens of battle, who slept in cold foxholes, who went without the [4] of food and shelter, who stuck it out and drove back the Nazi reign of murder. This was not a volunteer soldier, not someone well paid, [5] an average guy, up [6] the best trained, best equipped, fiercest, most brutal enemies seen in centuries.

His name isn't much. G.I. is just a military abbreviation [7] Government Issue, and it was on all of the articles [8] to soldiers. And Joe? A common name for a guy who never [9] it to the top. Joe Blow, Joe Palooka, Joe Magrac... a working class name. The United States has [10] had a president or vice-president or secretary of state Joe.

G.I. Joe had a [11] career fighting German, Japanese, and Korean troops. He appears as a character, or a [12] of American personalities, in the 1945 movie The Story of G.I. Joe, based on the last days of war correspondent Ernie Pyle. Some of the soldiers Pyle [13] portrayed themselves in the film. Pyle was famous for covering the [14] side of the war, writing about the dirt-snow-and-mud soldiers, not how many miles were [15] or what towns were captured or liberated. His reports [16] the "Willie" cartoons of famed Stars and Stripes artist Bill Maulden. Both men [17] the dirt and exhaustion of war, the [18] of civilization that the soldiers shared with each other and the civilians: coffee, tobacco, whiskey, shelter, sleep. [19] Egypt, France, and a dozen more countries, G.I. Joe was any American soldier, [20] the most important person in their lives."""

p1_content = """Homework has never been terribly popular with students and even many parents, but in recent years it has been particularly scorned. School districts across the country, most recently Los Angeles Unified, are revising their thinking on this educational ritual. Unfortunately, L.A. Unified has produced an inflexible policy which mandates that with the exception of some advanced courses, homework may no longer count for more than 10% of a student's academic grade.

This rule is meant to address the difficulty that students from impoverished or chaotic homes might have in completing their homework. But the policy is unclear and contradictory. Certainly, no homework should be assigned that students cannot complete on their own or that they cannot do without expensive equipment. But if the district is essentially giving a pass to students who do not do their homework because of complicated family lives, it is going riskily close to the implication that standards need to be lowered for poor children.

District administrators say that homework will still be a part of schooling; teachers are allowed to assign as much of it as they want. But with homework counting for no more than 10% of their grades, students can easily skip half their homework and see very little difference on their report cards. Some students might do well on state tests without completing their homework, but what about the students who performed well on the tests and did their homework? It is quite possible that the homework helped. Yet rather than empowering teachers to find what works best for their students, the policy imposes a flat, across-the-board rule.

At the same time, the policy addresses none of the truly thorny questions about homework. If the district finds homework to be unimportant to its students' academic achievement, it should move to reduce or eliminate the assignments, not make them count for almost nothing. Conversely, if homework matters, it should account for a significant portion of the grade. Meanwhile, this policy does nothing to ensure that the homework students receive is meaningful or appropriate to their age and the subject, or that teachers are not assigning more than they are willing to review and correct.

The homework rules should be put on hold while the school board, which is responsible for setting educational policy, looks into the matter and conducts public hearings. It is not too late for L.A. Unified to do homework right."""

p2_content = """Pretty in pink: adult women do not remember being so obsessed with the colour, yet it is pervasive in our young girls' lives. It is not that pink is intrinsically bad, but it is such a tiny slice of the rainbow and, though it may celebrate girlhood in one way, it also repeatedly and firmly fuses girls' identity to appearance. Then there is that connection, even among two-year-olds, between girls as not only innocent but as evidence of innocence. Looking around, I despaired at the singular lack of imagination about girls' lives and interests.

Girls' attraction to pink may seem inevitable, somehow encoded into their DNA, but according to Jo Paoletti, an historian at the University of Maryland, it is not. Children's clothing had not been divided into pink for girls and blue for boys until relatively recently. Before the First World War, white was the default colour for all infants and toddlers, for the simple reason that it could be bleached. Pink was actually considered a more masculine colour, while blue was associated with the Virgin Mary, constancy and faithfulness, symbolised femininity, and was thought to be softer. Only after World War II did blue become associated with boys and pink with girls.

But it was not until the mid-1980s that pink became the centrepiece of a marketing strategy that was designed to cater to modern perceptions of children's psychological development. Mid-century psychological theorists had introduced the idea that children can distinguish between the sexes at about two years old. As they become more aware of gender, children begin to actively search for cues as to what is suitable for them. Once they find them, said psychologist Dr. Megan Fulcher, "they don't want to compromise."

Trade publications counselled department stores that, in order to maximize sales, they should create a "third stepping stone" between infant wear and that of the older child. "Separating by gender may be the premier marketing tool of our era," said Jo Paoletti. "Splitting kids and adults into ever tinier categories has proved a surefire way to boost profits." One of the easiest ways to segment the market is to magnify gender differences—or invent them where they did not previously exist."""

p3_content = """In 2010, a federal judge shook America's biotech industry to its core. Companies had won patents for isolated DNA for decades—by 2005 some 20% of human genes were patented. But in March 2010 a district judge ruled that a company, Myriad Genetics, could not patent two genes associated with breast and ovarian cancer. The judge declared that because nature, not human ingenuity, created the DNA, it was unpatentable. Biotech executives were violently agitated. The Biotechnology Industry Organization (BIO) held a conference to discuss the ruling.

The patenting of human genes has always been controversial. Opponents argue that genes are natural products, not human inventions, and that patents can stifle research, keep prices artificially high, and restrict patients' access to life-saving diagnostic tests. Proponents counter that without patent protection, biotechnology companies would not invest the millions of dollars needed to discover genes, develop diagnostic tools, and bring treatments to market.

The case involving Myriad Genetics went to the U.S. Court of Appeals for the Federal Circuit. In July 2011, the appeals court reversed the lower court's ruling, deciding that isolated DNA is indeed chemically distinct from DNA as it exists in the body, and therefore patentable. But this was hardly the last word. The Supreme Court remanded the case back to the Federal Circuit for reconsideration in light of another patent ruling, Mayo v. Prometheus.

For patent lawyers and biotechnology executives, the uncertainty is troubling. Hans Sauer, the BIO's deputy general counsel for intellectual property, says that companies are eager to win patents for "connecting the dots"—discovering gene interactions and correlations that might be used to determine the causes of disease or predict a patient's response to a drug.

The Supreme Court's skepticism toward patents on natural phenomena and laws of nature suggests that the rules for patenting life-science discoveries are shifting. If the courts rule that isolated genes or diagnostic correlations cannot be patented, biotech firms may need to adjust their business models and rely more on trade secrets or new statutory protections.

As the debate continues, the legal battle over Myriad's patents has drawn extraordinary interest from the medical and legal communities. BIO recently held a convention where session after session focused on the shifting landscape for patents. Each meeting was packed."""

p4_content = """The great recession may be over, but this era of high joblessness is probably beginning. Before it ends, it will likely change the life course and character of a generation of young adults. And although it seems subtle now, the recession will likely reshape our politics, culture, and character of our society for years.

No one tries harder than the jobless to find silver linings in this national economic disaster. Many said that unemployment, while extremely painful, had improved them in some ways; they had become less materialistic and more financially prudent; they were more aware of the struggles of others. In clinical and sociological terms, some had grown closer to their families and communities. But over the long term, the economic slump is likely to leave people more cynical and pessimistic about their opportunities.

In The Moral Consequences of Economic Growth, the economic historian Benjamin Friedman argues that both inside and outside the U.S., lengthy periods of economic stagnation or decline have almost always left society more mean-spirited and less inclusive. They have also resulted in anti-immigrant sentiment, greater racial and class conflict, and a general narrowing of rights and freedoms. Such periods erode trust in democratic institutions and undermine the social contract.

The research of Till Von Wachter, the economist at Columbia University, suggests that not all people graduating into a recession see their life chances dimmed: those with degrees from elite universities catch up fairly quickly to where they otherwise would have been if they had graduated in good times; it is the masses beneath them that are left behind. In short, hard times make for bad people and unequal societies. These grim realities will reshape it, and all the more so the longer they extend."""

p5_content = """"Universal history, the history of what man has accomplished in this world, is at bottom the History of the Great Men who have worked here," wrote the Victorian sage Thomas Carlyle. Well, not any more it is not.

Suddenly, history is not what it used to be. The grand narrative of kings and battles has made way for social history and cultural studies. Yet the traditional biographical approach to history has a long and distinguished heritage.

In 1337, Petrarch began work on his rambling writing De Viris Illustribus—On Famous Men, highlighting the virtus (or virtue) of classical heroes. Petrarch believed that by contemplating the deeds of noble men of the past, contemporary citizens could be inspired to virtue in their own lives.

This was the biographical tradition which Niccolo Machiavelli turned on its head. In The Prince, he championed cunning, ruthlessness, and boldness, rather than virtue, mercy and justice, as the skills of successful leaders. For Machiavelli, practical political efficacy and the preservation of the state trumped moral idealism.

By contrast, the Victorian author Samuel Smiles wrote Self-Help as a catalogue of the worthy lives of engineers, industrialists and explorers. Smiles believed that the biographies of self-made men could inspire working-class youth to habits of industry, perseverance, and sobriety.

Yet Thomas Carlyle clung to his belief in the transformative power of heroic individuals. Carlyle saw the Great Man as an inspired leader who could reshape society through force of will and visionary insight, standing far above the ordinary populace.

This heroic view of history was vigorously challenged by Karl Marx and Friedrich Engels. In The Communist Manifesto and other works, Marx and Engels held that history is propelled not by the actions of great individuals, but by economic forces and the struggles of the masses. Downstairs became just as fascinating as upstairs."""

passages_configs = [
    {
        'id': 'fed5dec9-2b30-5625-b410-303c75709679',
        'passage_number': 1,
        'title': 'Section I: Use of English',
        'type': 'cloze',
        'content': p0_content
    },
    {
        'id': '31689fc4-2725-5d74-a617-aed200eea0f4',
        'passage_number': 1,
        'title': 'Section II: Reading Comprehension Part A - Text 1',
        'type': 'reading',
        'content': p1_content
    },
    {
        'id': '279ea384-fa7c-5f11-90cf-9d66120e1d65',
        'passage_number': 2,
        'title': 'Section II: Reading Comprehension Part A - Text 2',
        'type': 'reading',
        'content': p2_content
    },
    {
        'id': 'cd317e47-751b-5d4e-84b0-a755e8ee9cb8',
        'passage_number': 3,
        'title': 'Section II: Reading Comprehension Part A - Text 3',
        'type': 'reading',
        'content': p3_content
    },
    {
        'id': 'cd048359-9eb2-5a7d-b14a-f5e01ca76930',
        'passage_number': 4,
        'title': 'Section II: Reading Comprehension Part A - Text 4',
        'type': 'reading',
        'content': p4_content
    },
    {
        'id': 'bd9bf6f1-7548-56a2-a34f-798ce97444a1',
        'passage_number': 5,
        'title': 'Section II: Reading Comprehension Part B',
        'type': 'reading_part_b',
        'content': p5_content
    }
]

existing_passages = {p['id']: p for p in exam_data.get('passages', [])}
final_passages = []
for cfg in passages_configs:
    p_id = cfg['id']
    base = existing_passages.get(p_id, {})
    base['id'] = p_id
    base['passage_number'] = cfg['passage_number']
    base['title'] = cfg['title']
    base['type'] = cfg['type']
    base['content'] = cfg['content']
    final_passages.append(base)

exam_data['passages'] = final_passages

print("Passages reconstructed successfully. Count:", len(exam_data['passages']))

# 3. Gold Questions Standards & Explanations
cloze_gold = {
    1: {
        'ans': 'A',
        'opts': {'A': 'served', 'B': 'performed', 'C': 'rebelled', 'D': 'betrayed'},
        'expl': '【命题解密】句内语义与熟词僻义。定位至第②句“To the men and women who 1 in World War II and the people they liberated...”。结合后文“解放”可知，此处指的是在二战中服役并解放沦陷区的人们。serve作不及物动词时常与in连用，表示“服役，参军”，与in World War II构成完美搭配，故选[A]。[B] performed意为“执行；表现”，若表示执行任务需接宾语tasks等；[C] rebelled意为“反叛；反抗”，与被其解放的人民语境矛盾；[D] betrayed意为“出卖；背叛”，亦与语境不符。'
    },
    2: {
        'ans': 'B',
        'opts': {'A': 'actual', 'B': 'common', 'C': 'special', 'D': 'normal'},
        'expl': '【命题解密】上下文语义与形容词辨析。空格处作定语修饰man，后文用“the poor farm kid torn away from his home”做同位语补充说明。the common man是英语中的经典固定表达，意为“普通人；平民百姓”，与后文“grown into hero（成长为平民英雄）”形成鲜明对比，展现了平凡人造就非凡伟业的立意，故选[B]。[A] actual强调“实际的；真实的”，无法形成对比；[C] special（特殊的）与平民小子语境相反；[D] normal（正常的；精神正常的）不能体现平民阶层含义。'
    },
    3: {
        'ans': 'D',
        'opts': {'A': 'loaded', 'B': 'eased', 'C': 'removed', 'D': 'bore'},
        'expl': '【命题解密】句内语义与动词辨析。定语从句结构为“who [3] all the burdens of battle”。bear the burdens of battle为英语经典搭配，意为“承受/挑起战斗的重担”，bear的过去式为bore，故选[D]。[A] loaded通常构成load sb with sth结构；[B] eased意为“减轻，缓和”，与前线作战的艰苦现实相反；[C] removed意为“免除，消除”，士兵不可能免除战斗重担。'
    },
    4: {
        'ans': 'A',
        'opts': {'A': 'necessities', 'B': 'facilities', 'C': 'commodities', 'D': 'properties'},
        'expl': '【命题解密】句内语义与名词辨析。句意说明士兵在极为恶劣的环境下坚持战斗，甚至“缺少食物和住所等最起码的必需品”。the necessities of food and shelter为固定搭配，意为“食物和住处等生活必需品”，符合语境，故选[A]。[B] facilities意为“设施，设备”，如公共设施；[C] commodities意为“商品，货物”；[D] properties意为“财产，所有物”。'
    },
    5: {
        'ans': 'C',
        'opts': {'A': 'and', 'B': 'nor', 'C': 'but', 'D': 'hence'},
        'expl': '【命题解密】句内逻辑关系。空格前为“This was not a volunteer soldier, not someone well paid”，空格后为“an average guy”。前后构成典型的“not... not... but...”否定与肯定对比结构，意为“不是……也不是……而是……”，故选[C] but。[A] and表顺承；[B] nor常用于neither...nor...或否定句后表示“也不”；[D] hence表因果关系。'
    },
    6: {
        'ans': 'D',
        'opts': {'A': 'for', 'B': 'into', 'C': 'from', 'D': 'against'},
        'expl': '【命题解密】固定搭配与句内语义。空格所在短语修饰an average guy，意为“与数百年来所见最训练有素、装备最精良、最凶残的敌人交锋”。固定搭配be up against意为“面临，面对（严重的困难、强大的对手或敌人）”，如be up against a fierce opponent，故选[D] against。[A] for、[B] into、[C] from均不能与up搭配表达“面对强敌”之意。'
    },
    7: {
        'ans': 'B',
        'opts': {'A': 'with', 'B': 'for', 'C': 'as', 'D': 'on'},
        'expl': '【命题解密】句内语义与介词辨析。句子指出“G.I. is just a military abbreviation [7] Government Issue”。abbreviation for sth是英语固有习惯用法，意为“……的缩写/简称”，如the abbreviation for kilograms is kg，故选[B] for。[A] with、[C] as、[D] on均无此搭配。'
    },
    8: {
        'ans': 'A',
        'opts': {'A': 'handed', 'B': 'turned', 'C': 'brought', 'D': 'passed'},
        'expl': '【命题解密】动词短语与句内语义。此处考查分词短语作后置定语修饰articles（物品、用品）。短语hand out/hand to意为“分发、配发给”，此处省略out或直接用handed to soldiers表示“配发给士兵们的所有军需用品”，印证了Government Issue（政府配发）的由来，故选[A] handed。[B] turned to意为“求助于，转向”；[C] brought to意为“带给”；[D] passed to意为“传递给”。'
    },
    9: {
        'ans': 'C',
        'opts': {'A': 'got', 'B': 'took', 'C': 'made', 'D': 'put'},
        'expl': '【命题解密】固定搭配与上下文语义。空处前文提到“Joe? A common name for a guy who never [9] it to the top”。固定习语make it to the top意为“出人头地；跻身最高层/成功登顶”，如He made it to the top of his profession。句中指出“Joe”代表的是从未大富大贵或位极人臣的普通蓝领阶层，故选[C] made。[A] got常接to without it；[B] took it常表示忍受；[D] put it通常表示表达。'
    },
    10: {
        'ans': 'B',
        'opts': {'A': 'ever', 'B': 'never', 'C': 'seldom', 'D': 'hardly'},
        'expl': '【命题解密】上下文语义与副词用法。前文列举了Joe Blow, Joe Palooka等普通工薪阶层的典型平民名字，本句作为佐证指出：美国历史上从未有过哪位总统、副总统或国务卿名叫Joe（注：至2012年拜登任副总统时常称Joe Biden，但历史传统上高官正名不以Joe自居）。与前文“never made it to the top”照应，表示断然的全盘否定，故选[B] never。[A] ever意为“曾经”；[C] seldom与[D] hardly为半否定，不如never彻底有力。'
    },
    11: {
        'ans': 'D',
        'opts': {'A': 'modest', 'B': 'troubled', 'C': 'glorious', 'D': 'distinguished'},
        'expl': '【命题解密】上下文语义与形容词辨析。本段转入大兵乔的辉煌征战史。后文指出他先后抗击过德军、日军和朝军，并在1945年电影中成为银幕经典。distinguished意为“卓越的，功勋卓著的”，distinguished career意为“战功显赫的职业生涯”，高度概括了其抗击法西斯的光辉历程，故选[D]。[A] modest意为“谦虚的；简朴的”；[B] troubled意为“充满麻烦的”；[C] glorious虽也有光荣之意，但在修饰career时distinguished为最为地道庄重的褒义搭配。'
    },
    12: {
        'ans': 'C',
        'opts': {'A': 'portion', 'B': 'blend', 'C': 'composite', 'D': 'collection'},
        'expl': '【命题解密】上下文语义与名词辨析。句子表述为“He appears as a character, or a [12] of American personalities...”。composite意为“集合体，综合体”，指由多种性格特质凝聚而成的一个综合艺术形象，完美契合电影角色将成千上万美军士兵特征熔铸为一体的语境，故选[C]。[A] portion意为“一部分”；[B] blend强调“混合物”；[D] collection强调“收集品，收藏集”。'
    },
    13: {
        'ans': 'C',
        'opts': {'A': 'interrogated', 'B': 'interviewed', 'C': 'quoted', 'D': 'questioned'},
        'expl': '【命题解密】上下文语义与动词辨析。厄尼·派尔是著名战地记者（war correspondent），他在战地采访士兵并在战地报道中引用他们的亲口言论。quoted意为“援引，引用（某人的话）”，Some of the soldiers Pyle quoted指“被派尔在报道中引用过话语的部分士兵在电影中本色出演了他们自己”，故选[C]。[A] interrogated（审问）用于审讯战俘；[B] interviewed指正式访谈；[D] questioned意为质问。'
    },
    14: {
        'ans': 'A',
        'opts': {'A': 'human', 'B': 'military', 'C': 'political', 'D': 'strategic'},
        'expl': '【命题解密】句内语义与形容词辨析。后文指出派尔专注于报道“满身泥泞与风雪的普通士兵（the dirt-snow-and-mud soldiers）”，而不是抽象的推进了多少英里或攻占了哪座城镇。这表明他关注的是战争中“人性化的一面/人的处境”，the human side of the war为固定修辞表达，故选[A] human。[B] military（军事的）、[C] political（政治的）、[D] strategic（战略的）恰恰是派尔所摒弃的宏大叙事。'
    },
    15: {
        'ans': 'D',
        'opts': {'A': 'traveled', 'B': 'walked', 'C': 'marched', 'D': 'covered'},
        'expl': '【命题解密】句内语义与动词用法。空格处于从句“how many miles were [15]”，主语是英里数（miles）。在英语中，cover miles是表示“走过、行进、跨越一段路程”的地道搭配，且能使用被动态miles were covered，故选[D]。[A] traveled、[B] walked、[C] marched通常为主动态且多以人作主语，不能与miles构成自然被动搭配。'
    },
    16: {
        'ans': 'A',
        'opts': {'A': 'echoed', 'B': 'contrasted', 'C': 'surpassed', 'D': 'paraged'},
        'expl': '【命题解密】上下文语义。句意指出派尔的战地报道与著名战地漫画家比尔·莫尔丁的威利系列漫画形成了呼应。echo意为“反映，映现，呼应”，表示两者在展现前线士兵疾苦与情感上产生了深度共鸣，故选[A] echoed。[B] contrasted意为“形成鲜明对比”；[C] surpassed意为“超越”；[D] paraged为拼写干扰项。'
    },
    17: {
        'ans': 'B',
        'opts': {'A': 'endured', 'B': 'shared', 'C': 'reflected', 'D': 'understood'},
        'expl': '【命题解密】上下文语义与动词搭配。后文指出两位艺术家共同体会了战争的污浊与疲惫。shared此处意为“共同感受，有着相同的体会”，Both men shared the dirt and exhaustion of war，故选[B]。[A] endured强调“忍受（痛苦）”，主语一般是前线战士本人而非作为观察者的记者和画家；[C] reflected意为“反映”；[D] understood意为“理解”。'
    },
    18: {
        'ans': 'C',
        'opts': {'A': 'luxuries', 'B': 'comforts', 'C': 'tokens', 'D': 'relics'},
        'expl': '【命题解密】句内语义与名词辨析。后文冒号列出了具体的慰藉品：“coffee, tobacco, whiskey, shelter, sleep”。tokens of civilization意为“文明的标志/象征物”，在荒蛮残酷的战场上，咖啡、烟草和片刻的睡眠是士兵们与文明社会仅存的一丝微薄联系与象征，故选[C] tokens。[A] luxuries意为“奢侈品”；[B] comforts意为“安慰物”；[D] relics意为“遗迹，文物”。'
    },
    19: {
        'ans': 'B',
        'opts': {'A': 'In', 'B': 'To', 'C': 'From', 'D': 'For'},
        'expl': '【命题解密】句内语义与介词辨析。句子后半部分表明了各国民众的感情归属：“G.I. Joe was any American soldier, [20] the most important person in their lives”。To sb意为“在某人看来；对某人而言”，用于引出持有特定评价或看法的主体，如To Egypt, France...意为“在埃及、法国等国民众的心目中”，大兵乔是生命中最重要的人，故选[B] To。[A] In强调在地理范围内；[C] From表示来源；[D] For表示“为了”。'
    },
    20: {
        'ans': 'D',
        'opts': {'A': 'on the contrary', 'B': 'by this means', 'C': 'from the outset', 'D': 'at that point'},
        'expl': '【命题解密】上下文语义与介词短语。空格修饰表语“the most important person in their lives”。at that point指代“在那个历史关头/在二战爆发的生死存亡时刻”，对于被纳粹铁蹄践踏而获得解放的各国民众而言，冲锋陷阵的美国大兵正是彼时他们生命中最重要的人，呼应开篇“that is not how it used to be”，故选[D]。[A] on the contrary（恰恰相反）逻辑转折不当；[B] by this means（以此方式）表手段；[C] from the outset（从一开始）超出二战特定时间范围。'
    }
}

reading_gold = {
    21: {
        'ans': 'A',
        'opts': {
            'A': 'is receiving more criticism',
            'B': 'is gaining more preferences',
            'C': 'is no longer an educational ritual',
            'D': 'is not required for advanced courses'
        },
        'expl': '【命题解密】推理判断题。定位至第一段①句“Homework has never been terribly popular with students and even many parents, but in recent years it has been particularly scorned”。句中“has been particularly scorned（近年来尤其受到唾弃/受到指责）”与选项[A]“is receiving more criticism（正在受到更多批评）”构成同义替换，故选[A]。[B]项忽略否定词never，将文意彻底反向曲解；[C]项曲解②句“revising their thinking on this educational ritual”，学区只是在重新思考这一惯例，并未取消；[D]项与③句“with the exception of some advanced courses（高级课程除外）”完全相悖。'
    },
    22: {
        'ans': 'C',
        'opts': {
            'A': 'tend to have moderate expectations for their education',
            'B': 'have asked for a different educational standard',
            'C': 'may have problems finishing their homework',
            'D': 'have voiced their complaints about homework'
        },
        'expl': '【命题解密】事实细节题。定位至第二段①句“This rule is meant to address the difficulty that students from impoverished or chaotic homes might have in completing their homework”。句中“the difficulty... in completing their homework（来自贫困或混乱家庭的学生在完成作业方面可能遇到的困难）”与选项[C]“may have problems finishing their homework”完美同义对应，故选[C]。[A]项无中生有推断贫困生期望不高；[B]项将第四段作者指出的新规危险倾向“降低对贫困生的要求”颠倒为学生主动要求；[D]项并未提及贫困生大发抱怨。'
    },
    23: {
        'ans': 'D',
        'opts': {
            'A': 'result in students’ indifference to their report cards',
            'B': 'undermine the authority of state tests',
            'C': 'restrict teachers’ power in education',
            'D': 'discourage students from doing homework'
        },
        'expl': '【命题解密】推理判断题。定位至第三段②句“But with homework counting for no more than 10% of their grades, students can easily skip half their homework and see very little difference on their report cards”。作者指出，由于家庭作业在总分中占比极低，学生即使少做一半作业在成绩单上也看不出任何区别，这必然会严重挫伤学生完成作业的积极性。选项[D]“discourage students from doing homework（打击学生做作业的积极性）”是对此处文意的准确归纳，故选[D]。[A]项混淆very little difference与indifference（漠不关心）；[B]项无端引申州考权威性受损；[C]项将未能授权教师夸大为限制权力。'
    },
    24: {
        'ans': 'B',
        'opts': {
            'A': 'it should be eliminated',
            'B': 'it counts much in schooling',
            'C': 'it places extra burdens on teachers',
            'D': 'it is important for grades'
        },
        'expl': '【命题解密】推理判断题。定位至第四段①至③句“the policy addresses none of the truly thorny questions about homework. If the district finds homework to be unimportant... it should move to reduce or eliminate... Conversely, if homework matters, it should account for a significant portion...”。作者借Conversely构成对称假设，批评学区新政既未承认作业重要，也未表明作业不重要，因而回避了“家庭作业在学校教育中究竟是否举足轻重”这一根本问题。选项[B]“whether it counts much in schooling（在学校教育中是否起重要作用）”精准概括了核心争论，故选[B]。[A]项仅是作业不重要假设下的举措；[C]项曲解了末句教师批改负担；[D]项将对学业成就的影响偷换为对成绩单本身。'
    },
    25: {
        'ans': 'A',
        'opts': {
            'A': 'A Faulty Approach to Homework',
            'B': 'A Welcomed Policy for Poor Students',
            'C': 'Thorny Questions about Homework',
            'D': 'Wrong Interpretations of an Educational Policy'
        },
        'expl': '【命题解密】主旨大意题。全文首段引出洛杉矶联合学区针对家庭作业所推行的死板硬性政策（an inflexible policy）；第二至四段逐层剖析该政策的致命缺陷：以保护贫困生为名行降低标准之实、一刀切的限比打消学生积极性、回避了家庭作业是否重要的核心实质；尾段得出明确结论：新规应当叫停搁置。全文始终聚焦于批评学区处理作业的错误方式，选项[A]“A Faulty Approach to Homework（处理家庭作业的一个错误方法）”完美契合主旨并鲜明呈现作者的批判态度，故选[A]。[B]项与作者抨击新规伤害贫困生相悖；[C]项偏离了对学区政策的批判重心；[D]项将对政策本身的批判篡改为外界对政策的误解。'
    },
    26: {
        'ans': 'C',
        'opts': {
            'A': 'should not be associated with girls\' innocence',
            'B': 'cannot explain girls\' lack of imagination',
            'C': 'should not be the sole representation of girlhood',
            'D': 'cannot affect girls\' lives and interests'
        },
        'expl': '【命题解密】词句推断题。定位至首段②句“It is not that pink is intrinsically bad, but it is such a tiny slice of the rainbow and, though it may celebrate girlhood in one way, it also repeatedly and firmly fuses girls\' identity to appearance”。作者以“七色彩虹中极小的一抹色彩”形象生动地比喻粉色只是童年丰富多彩生活中的极小一部分，社会商家不应将其定格为女孩的全部象征。选项[C]“should not be the sole representation of girlhood（粉色不应成为女孩童年的唯一象征）”准确传达了作者意图，故选[C]。[A]、[B]、[D]项均未切中七彩光谱与单一色彩的本体比喻。'
    },
    27: {
        'ans': 'B',
        'opts': {
            'A': 'are often used to categorize white infants',
            'B': 'were not used to tell girls from boys in the past',
            'C': 'tend to be assigned with identical meanings',
            'D': 'are naturally associated with children\'s gender'
        },
        'expl': '【命题解密】事实细节题。定位至第二段②③句“Children\'s clothing had not been divided into pink for girls and blue for boys until relatively recently. Before the First World War, white was the default colour for all infants and toddlers...”。历史学家指出，在近代以前，婴儿不论男女一律穿白色，并未用颜色来区分性别，随后粉色还一度属于男性色彩。选项[B]“were not used to tell girls from boys in the past（在过去并没有用来区分男孩女孩）”是对历史事实的准确归纳，故选[B]。[A]项曲解了婴儿穿白色是因为易漂洗；[C]项违背文中不同时期色彩意义流变的表述；[D]项恰恰是作者反驳的错误生物宿命论。'
    },
    28: {
        'ans': 'B',
        'opts': {
            'A': 'has neglected children\'s active role in searching for cues',
            'B': 'was profoundly influenced by mid-century theorists',
            'C': 'focused solely on the two-year-old development stage',
            'D': 'failed to acknowledge children\'s resistance to compromise'
        },
        'expl': '【命题解密】事实细节题。定位至第三段①②句“But it was not until the mid-1980s that pink became the centrepiece of a marketing strategy that was designed to cater to modern perceptions of children\'s psychological development. Mid-century psychological theorists had introduced the idea that children can distinguish between the sexes at about two years old”。文章明确指出，当下对儿童心理发育特性的认知，深刻植根于20世纪中叶心理学家所确立的理论模型。选项[B]“was profoundly influenced by mid-century theorists（深刻受到上世纪中叶理论家的影响）”完全切合题意，故选[B]。'
    },
    29: {
        'ans': 'A',
        'opts': {
            'A': 'classify consumers into smaller groups',
            'B': 'manufacture clothing with uniform gender cues',
            'C': 'focus primarily on the baby infant wear market',
            'D': 'combine toddler products with older child designs'
        },
        'expl': '【命题解密】推理判断题。定位至第四段①至③句“Trade publications counselled department stores that, in order to maximize sales, they should create a \'third stepping stone\' between infant wear and that of the older child... Splitting kids and adults into ever tinier categories has proved a surefire way to boost profits”。行业商业刊物给百货商店出谋划策，要求将儿童人群切割为更细碎的年龄与性别子类别。选项[A]“classify consumers into smaller groups（将消费者细分为更小的群体）”正是对“Splitting into ever tinier categories”的规范转述，故选[A]。[B]、[C]、[D]均与商业细分主旨背道而驰。'
    },
    30: {
        'ans': 'C',
        'opts': {
            'A': 'a genetically determined trait',
            'B': 'an instinctive psychological requirement',
            'C': 'a market-driven phenomenon',
            'D': 'an inevitable natural preference'
        },
        'expl': '【命题解密】主旨结论题。通读全文，作者开篇反驳了“女孩喜欢粉色源自天生DNA”的偏见，中篇援引历史学证明颜色性别认同纯属后天人为构建，尾篇直接揭露商业机构为追逐暴利刻意利用性别标签细分市场的资本本质。文章最终结论是：女孩对粉色的痴迷完全是商业营销与消费主义塑造出来的后天产物。选项[C]“a market-driven phenomenon（一种受市场营销驱动的社会现象）”深刻统领全文主旨，故选[C]。[A]、[B]、[D]均将这种现象误归为先天基因或本能，均为干扰项。'
    },
    31: {
        'ans': 'A',
        'opts': {
            'A': 'genes to be patentable',
            'B': 'the BIO to issue a warning',
            'C': 'their executives to be active',
            'D': 'judges to rule out gene patenting'
        },
        'expl': '【命题解密】事实细节题。定位至第一段②③句“Companies had won patents for isolated DNA for decades... But in March 2010 a district judge ruled that a company, Myriad Genetics, could not patent two genes... Biotech executives were violently agitated”。几十年来生物技术公司一直享受基因专利带来的垄断红利，法官判定基因不可申请专利后高管们暴跳如雷。由此直接反推，生物技术公司最核心的利益诉求就是希望基因能够获得专利。选项[A]“genes to be patentable（希望基因能够被授予专利）”准确概括其立场，故选[A]。[B]项、[C]项属于细枝末节的会议反应；[D]项完全站在其利益的对立面。'
    },
    32: {
        'ans': 'B',
        'opts': {
            'A': 'genetic tests are not reliable',
            'B': 'only man-made products are patentable',
            'C': 'patents on genes depend much on innovation',
            'D': 'courts should restrict access to genetic tests'
        },
        'expl': '【命题解密】事实细节题。定位至第一段末句与第二段①句“The judge declared that because nature, not human ingenuity, created the DNA, it was unpatentable... Opponents argue that genes are natural products, not human inventions”。反对基因专利的核心法理依据在于：大自然创造的产物绝非人类的发明创造，唯有人工改造或制造的创新产品才具备专利资格。选项[B]“only man-made products are patentable（只有人造产品才可以申请专利）”精确呼应原文，故选[B]。[A]项误导检测可靠性；[C]项属于专利法一般概念；[D]项与患者权益相反。'
    },
    33: {
        'ans': 'A',
        'opts': {
            'A': 'establishing disease correlations',
            'B': 'discovering gene interactions',
            'C': 'drawing pictures of genes',
            'D': 'identifying human DNA'
        },
        'expl': '【命题解密】事实细节题。定位至第四段末句“Hans Sauer... says that companies are eager to win patents for \'connecting the dots\'—discovering gene interactions and correlations that might be used to determine the causes of disease...”。BIO总法律顾问指出，企业极度渴望为“连接各个点”赢得专利，即通过锁定基因关联来诊断疾病成因。选项[A]“establishing disease correlations（确立疾病与基因的相关性）”是破折号后解释性内容的直接对应，故选[A]。[B]项是实现手段的一部分，而建立疾病成因关联是其核心目的；[C]项为字面干扰；[D]项为人体DNA的基础识别。'
    },
    34: {
        'ans': 'C',
        'opts': {
            'A': 'the Supreme Court was authoritative',
            'B': 'the BIO was a powerful organization',
            'C': 'gene patenting was a great concern',
            'D': 'lawyers were keen to attend conventions'
        },
        'expl': '【命题解密】句意推断题。定位至尾段末句“BIO recently held a convention where session after session focused on the shifting landscape for patents. Each meeting was packed”。作者在文末描述BIO大会上一场接一场的专利政策研讨会座无虚席（Each meeting was packed），生动体现了医药企业与法学界对基因专利未来命运的高度焦虑与极大关注。选项[C]“gene patenting was a great concern（基因专利归属是各方极其关注的焦点）”深刻揭示了座无虚席背后的社会心态，故选[C]。[A]、[B]、[D]均停留在表面字面或无关推论。'
    },
    35: {
        'ans': 'D',
        'opts': {
            'A': 'enthusiastic',
            'B': 'indifferent',
            'C': 'supportive',
            'D': 'objective'
        },
        'expl': '【命题解密】观点态度题。纵观全文，作者既详尽客观地陈述了生物科技公司倚仗专利维系研发投资的商业考量，也深刻剖析了反对者关于基因属于自然物、专利抬高医疗成本的严正指控，并在第三至六段如实跟进联邦巡回法院与最高法院的判例交锋及行业各方的谨慎应对。全文行文严谨中立，未带有偏激的主观偏向。选项[D]“objective（客观公正的）”精准概括了作者的立场态度，故选[D]。[A]热衷的、[C]支持的偏向企业，[B]漠不关心的违背全文深度探讨的事实。'
    },
    36: {
        'ans': 'D',
        'opts': {
            'A': 'seek subsidies from the government',
            'B': 'make profits from the troubled economy',
            'C': 'explore reasons for the unemployment',
            'D': 'look on the bright side of the recession'
        },
        'expl': '【命题解密】词句推断题。定位至第二段①②句“No one tries harder than the jobless to find silver linings in this national economic disaster. Many said that unemployment, while extremely painful, had improved them in some ways; they had become less materialistic...”。英语成语every cloud has a silver lining意为“黑暗中总有一丝光明”。后文具体解释失业者虽然痛苦，但也在努力寻找积极意义（如变得节俭、关爱家人）。选项[D]“look on the bright side of the recession（看到经济萧条中积极光明的一面）”与find silver linings语义完全一致，故选[D]。[A]寻求补贴、[B]牟取暴利、[C]探究失业原因均与语境无关。'
    },
    37: {
        'ans': 'D',
        'opts': {
            'A': 'struggle against each other for survival',
            'B': 'give up their ambitions for the future',
            'C': 'challenge existing ethical standards',
            'D': 'reconsider their lifestyle and priorities'
        },
        'expl': '【命题解密】事实细节题。定位至第二段②③句“they had become less materialistic and more financially prudent; they were more aware of the struggles of others... grown closer to their families...”。失业让人们重新审视过去的挥霍，转而注重精打细算并更珍视亲情与家庭，这属于对个人生活方式及价值优先级的深刻反思。选项[D]“reconsider their lifestyle and priorities（重新审视自身的生活方式与优先考量）”准确契合原文，故选[D]。[A]互相争斗、[B]放弃抱负、[C]挑战伦理均为无端曲解。'
    },
    38: {
        'ans': 'B',
        'opts': {
            'A': 'eliminate racial discrimination',
            'B': 'bring out more evils of human nature',
            'C': 'strengthen democratic systems',
            'D': 'promote social equality'
        },
        'expl': '【命题解密】事实细节题。定位至第三段①②句“Benjamin Friedman argues that... lengthy periods of economic stagnation or decline have almost always left society more mean-spirited and less inclusive. They have also resulted in anti-immigrant sentiment, greater racial and class conflict...”。弗里德曼指出，长期的经济停滞几乎总是让社会变得更加刻薄尖酸、缺乏包容，激化排外情绪与种族阶级冲突。这些都是人性中黑暗与丑恶一面的集中暴露。选项[B]“bring out more evils of human nature（激发或暴露更多人性中的恶）”高度概括了其核心观点，故选[B]。[A]、[C]、[D]均与弗里德曼指出的负面恶果截然相反。'
    },
    39: {
        'ans': 'D',
        'opts': {
            'A': 'suffer long-term career setbacks',
            'B': 'compete fiercely with the masses',
            'C': 'sacrifice their potential for quick income',
            'D': 'recover quickly from the adverse effect'
        },
        'expl': '【命题解密】事实细节题。定位至第四段①句“those with degrees from elite universities catch up fairly quickly to where they otherwise would have been if they had graduated in good times; it is the masses beneath them that are left behind”。哥伦比亚大学经济学家的研究证实：名校毕业生在衰退期毕业后，能够相当迅速地赶上在繁荣时期毕业本应达到的职场水平。选项[D]“recover quickly from the adverse effect（从经济逆境的不利影响中迅速恢复过来）”与catch up fairly quickly形成精准同义对应，故选[D]。[A]长期受挫、[B]与大众激烈竞争、[C]牺牲潜力均为反向干扰项。'
    },
    40: {
        'ans': 'A',
        'opts': {
            'A': 'lasting and profound',
            'B': 'temporary and manageable',
            'C': 'predictable and localized',
            'D': 'mild and superficial'
        },
        'expl': '【命题解密】主旨态度题。定位至首段末句与全文尾句。首段指出“the recession will likely reshape our politics, culture, and character of our society for years”，尾段末句进一步强调“These grim realities will reshape it, and all the more so the longer they extend”。作者明确指出经济困境对社会制度与国民心态的重构具有长久而深远的破坏力。选项[A]“lasting and profound（持久而深远的）”完全切合文章主题与作者沉痛的预警，故选[A]。[B]暂时的、[C]局部的、[D]轻微的均严重低估了衰退的危害。'
    },
    41: {
        'ans': 'A',
        'opts': {
            'A': 'emphasized the virtue of classical heroes.',
            'B': 'highlighted the public glory of the leading artists.',
            'C': 'opened up new realms of understanding the great men in history.',
            'D': 'focused on epochal figures whose lives were hard to imitate.',
            'E': 'held that history should be the story of the masses and their record of struggle.',
            'F': 'dismissed virtue as unnecessary for successful leaders.',
            'G': 'depicted the worthy lives of engineers, industrialists and explorers.'
        },
        'expl': '【命题解密】信息匹配题。定位至第三段“In 1337, Petrarch began work on his rambling writing De Viris Illustribus—On Famous Men, highlighting the virtus (or virtue) of classical heroes”。彼特拉克在其著作《名人传》中着重强调古代古典英雄的美德，以此激励后世。选项[A]“emphasized the virtue of classical heroes（强调古典英雄的美德）”与原文词句100%直接对应，故选[A]。'
    },
    42: {
        'ans': 'F',
        'opts': {
            'A': 'emphasized the virtue of classical heroes.',
            'B': 'highlighted the public glory of the leading artists.',
            'C': 'opened up new realms of understanding the great men in history.',
            'D': 'focused on epochal figures whose lives were hard to imitate.',
            'E': 'held that history should be the story of the masses and their record of struggle.',
            'F': 'dismissed virtue as unnecessary for successful leaders.',
            'G': 'depicted the worthy lives of engineers, industrialists and explorers.'
        },
        'expl': '【命题解密】信息匹配题。定位至第四段“This was the biographical tradition which Niccolo Machiavelli turned on its head. In The Prince, he championed cunning, ruthlessness, and boldness, rather than virtue, mercy and justice, as the skills of successful leaders”。马基雅维利在《君主论》中主张狡诈、无情与果决，而不是仁慈、正义或道德美德，颠覆了传统的英雄传记传统。选项[F]“dismissed virtue as unnecessary for successful leaders（认为美德对成功的领导者是不必要的）”是对championed... rather than virtue的精准概括，故选[F]。'
    },
    43: {
        'ans': 'G',
        'opts': {
            'A': 'emphasized the virtue of classical heroes.',
            'B': 'highlighted the public glory of the leading artists.',
            'C': 'opened up new realms of understanding the great men in history.',
            'D': 'focused on epochal figures whose lives were hard to imitate.',
            'E': 'held that history should be the story of the masses and their record of struggle.',
            'F': 'dismissed virtue as unnecessary for successful leaders.',
            'G': 'depicted the worthy lives of engineers, industrialists and explorers.'
        },
        'expl': '【命题解密】信息匹配题。定位至第五段“By contrast, the Victorian author Samuel Smiles wrote Self-Help as a catalogue of the worthy lives of engineers, industrialists and explorers”。维多利亚时代作家塞缪尔·斯迈尔斯在其经典《自助》中记录了工程师、实业家和探险家充实而有价值的一生。选项[G]“depicted the worthy lives of engineers, industrialists and explorers（描绘了工程师、实业家与探险家有价值的人生）”与原文词句一字不差完全吻合，故选[G]。'
    },
    44: {
        'ans': 'C',
        'opts': {
            'A': 'emphasized the virtue of classical heroes.',
            'B': 'highlighted the public glory of the leading artists.',
            'C': 'opened up new realms of understanding the great men in history.',
            'D': 'focused on epochal figures whose lives were hard to imitate.',
            'E': 'held that history should be the story of the masses and their record of struggle.',
            'F': 'dismissed virtue as unnecessary for successful leaders.',
            'G': 'depicted the worthy lives of engineers, industrialists and explorers.'
        },
        'expl': '【命题解密】信息匹配题。定位至第一段与第六段“Universal history, the history of what man has accomplished in this world, is at bottom the History of the Great Men who have worked here... Carlyle saw the Great Man as an inspired leader who could reshape society...”。托马斯·卡莱尔是伟人史观的代表人物，系统阐释了伟大人物如何凭借超凡意志改造世界并开启历史新纪元。选项[C]“opened up new realms of understanding the great men in history（开辟了理解历史伟人的全新视野）”深刻契合其在历史思想史上的地位，故选[C]。'
    },
    45: {
        'ans': 'E',
        'opts': {
            'A': 'emphasized the virtue of classical heroes.',
            'B': 'highlighted the public glory of the leading artists.',
            'C': 'opened up new realms of understanding the great men in history.',
            'D': 'focused on epochal figures whose lives were hard to imitate.',
            'E': 'held that history should be the story of the masses and their record of struggle.',
            'F': 'dismissed virtue as unnecessary for successful leaders.',
            'G': 'depicted the worthy lives of engineers, industrialists and explorers.'
        },
        'expl': '【命题解密】信息匹配题。定位至第七段末尾“This heroic view of history was vigorously challenged by Karl Marx and Friedrich Engels. In The Communist Manifesto and other works, Marx and Engels held that history is propelled not by the actions of great individuals, but by economic forces and the struggles of the masses. Downstairs became just as fascinating as upstairs”。马克思与恩格斯提出唯物史观，坚决批驳英雄史观，强调人民群众的历史主体地位与阶级斗争历史。选项[E]“held that history should be the story of the masses and their record of struggle（认为历史应当是人民群众的故事及其斗争记录）”与原文完全契合，故选[E]。'
    }
}

# 4. Apply all Gold Questions & Options to exam_data['questions']
existing_qs = {q.get('sort_order') or q.get('question_number'): q for q in exam_data.get('questions', [])}
reconstructed_questions = []

for q_num in range(1, 46):
    q_obj = existing_qs.get(q_num, {})
    q_obj['question_number'] = q_num
    q_obj['sort_order'] = q_num
    
    if q_num <= 20:
        cfg = cloze_gold[q_num]
        q_obj['q_type'] = 'cloze_item'
        q_obj['points'] = 0.5
        q_obj['answer'] = cfg['ans']
        q_obj['correct_answer'] = cfg['ans']
        q_obj['explanation'] = cfg['expl']
        # Options
        opts = []
        for k in ['A', 'B', 'C', 'D']:
            opts.append({
                'key': k,
                'text': cfg['opts'][k],
                'value': k
            })
        q_obj['options'] = opts
    else:
        cfg = reading_gold[q_num]
        q_obj['q_type'] = 'reading_item'
        q_obj['points'] = 2.0
        q_obj['answer'] = cfg['ans']
        q_obj['correct_answer'] = cfg['ans']
        q_obj['explanation'] = cfg['expl']
        # Options
        opts = []
        keys = ['A', 'B', 'C', 'D'] if q_num <= 40 else ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for k in keys:
            opts.append({
                'key': k,
                'text': cfg['opts'][k],
                'value': k
            })
        q_obj['options'] = opts
        
    reconstructed_questions.append(q_obj)

exam_data['questions'] = reconstructed_questions

# 5. Save updated JSON
with open(JSON_PATH, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("2012 ky2 Full Gold Engine executed successfully! File written:", JSON_PATH)
