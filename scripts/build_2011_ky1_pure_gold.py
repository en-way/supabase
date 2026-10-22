# -*- coding: utf-8 -*-
import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

exam_json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\111d6c78-81a1-53dc-a039-dad4c94ebd35.json'

with open(exam_json_path, encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Update Title and metadata
exam_data['title'] = "2011年全国硕士研究生入学统一考试英语（一）真题"
exam_data['category_id'] = "ky1"
exam_data['total_score'] = 60.0

# 2. Golden Passages
# Passage 0: Cloze
p0_content = """Ancient Greek philosopher Aristotle viewed laughter as "a bodily exercise precious to health." But [1] some claims to the contrary, laughing probably has little influence on physical fitness. Laughter does [2] short-term changes in the function of the heart and its blood vessels, [3] heart rate and oxygen consumption. But because hard laughter is difficult to [4], a good laugh is unlikely to have [5] benefits the way, say, walking or jogging does.

[6], instead of straining muscles to build them, as exercise does, laughter apparently accomplishes the [7]. Studies dating back to the 1930s indicate that laughter [8] muscles, decreasing muscle tone for up to 45 minutes after the laugh dies down.

Such bodily reaction might conceivably help [9] the effects of psychological stress. Anyway, the act of laughing probably does produce other types of [10] feedback that improve an individual's emotional state. [11] one classical theory of emotion, our feelings are partially rooted [12] physical reactions. It was argued at the end of the 19th century that humans do not cry [13] they are sad but they become sad when the tears begin to flow.

Although sadness also [14] tears, evidence suggests that emotions can flow [15] muscular responses. In an experiment published in 1988, social psychologist Fritz Strack of the University of Wurzburg in Germany asked volunteers to [16] a pen either with their teeth — thereby creating an artificial smile — or with their lips, which would produce a(n) [17] expression. Those forced to exercise their smiling muscles [18] more enthusiastically to funny cartoons than did those whose mouths were contracted in a frown, [19] that expressions may influence emotions rather than just the other way around. [20], the physical act of laughter could improve mood."""

# Passage 1: Text 1
p1_content = """The decision of the New York Philharmonic to hire Alan Gilbert as its next music director has been the talk of the classical-music world ever since the sudden announcement of his appointment in 2009. For the most part, the response has been favorable, to say the least. "Hooray! At last!" wrote Anthony Tommasini, a sober-sided classical-music critic.

One of the reasons why the appointment came as such a surprise, however, is that Gilbert is comparatively little known. Even Tommasini, who had advocated Gilbert's appointment in the Times, calls him "an unpretentious musician with no air of the formidable conductor about him." As a description of the next music director of an orchestra that has hitherto been led by musicians like Gustav Mahler and Pierre Boulez, that seems likely to have struck at least some Times readers as faint praise.

For my part, I have no idea whether Gilbert is a great conductor or even a good one. To be sure, he performs an impressive variety of interesting compositions, but it is not necessary for me to visit Avery Fisher Hall, or anywhere else, to hear interesting orchestral music. All I have to do is to go to my CD shelf, or boot up my computer and download still more recorded music from iTunes.

Devoted concertgoers who reply that recordings are no substitute for live performance are missing the point. For the time, attention, and money of the art-loving public, classical instrumentalists must compete not only with opera houses, dance troupes, theater companies, and museums, but also with the recorded performances of the great classical musicians of the 20th century. These recordings are cheap, available everywhere, and very often much higher in artistic quality than today's live performances; moreover, they can be "consumed" at a time and place of the listener's choosing. The widespread availability of such recordings has thus brought about a crisis in the institution of the traditional classical concert.

One possible response is for classical performers to program attractive new music that is not yet available on record. Gilbert's own interest in new music has been widely noted: Alex Ross, a classical-music critic, has described him as a man who is capable of turning the Philharmonic into "a markedly different, more vibrant organization." But what will be the nature of that difference? Merely expanding the orchestra's repertoire will not be enough. If Gilbert and the Philharmonic are to succeed, they must first change the relationship between America's oldest orchestra and the new audience it hopes to attract."""

# Passage 2: Text 2
p2_content = """When Liam McGee departed as president of Bank of America in August, his explanation was surprisingly straight up. Rather than cloaking his exit in the usual vague excuses, he came right out and said he was leaving "to pursue my goal of running a company." Broadcasting his ambition was "very much my decision," McGee says. Within two weeks, he was talking for the first time with the board of Hartford Financial Services Group, which named him CEO and chairman on September 29.

McGee says leaving without a position lined up gave him time to reflect on what kind of company he wanted to run. It also sent a clear message to the outside world about his aspirations. And McGee isn't alone. In recent weeks the No. 2 executives at Avon and American Express quit with similar declarations. As boards scrutinize succession plans in response to shareholder pressure, executives who don't get the nod also may wish to move on. A turbulent business environment also has senior managers cautious of letting vague pronouncements cloud their reputations.

As the first signs of recovery begin to take hold, deputy chiefs may be more willing to make the jump without a net. In the third quarter, CEO turnover was down 23% from a year ago as nervous boards stuck with the leaders they had, according to Liberum Research. As the economy picks up, opportunities will abound for aspiring leaders.

The decision to quit a senior position to look for a better one is unconventional. For years executives and headhunters have adhered to the rule that the most attractive CEO candidates are the ones who must be poached. Says Korn/Ferry senior partner Dennis Carey: "I can't think of a single search I've done where a board has not instructed me to look at sitting CEOs first."

Those who jumped without a job haven't always landed in top positions quickly. Ellen Marram quit as chief of Tropicana a decade ago, saying she wanted to be a CEO. It was a year before she became head of a tiny Internet-based commodities exchange. Robert Willumstad left Citigroup in 2005 with ambitions to be a CEO. He finally took that post at a major financial institution three years later.

Many recruiters say the old disgrace is fading for top performers. The financial crisis has made it more acceptable to be between jobs or to leave a bad one. "The traditional rule was it's safer to stay where you are, but that's been fundamentally inverted," says one headhunter. "The people who've been hurt the worst are those who've stayed too long.\""""

# Passage 3: Text 3 (Complete with fully restored 68-word beginning)
p3_content = """The rough guide to marketing success used to be that you got what you paid for. No longer. While traditional "paid" media — such as television commercials and print advertisements — still play a major role, companies today can exploit many alternative forms of media. Consumers passionate about a product may create "earned" media by willingly promoting it to friends, and a company may leverage "owned" media by sending e-mail alerts about products and sales to customers registered with its Web site. The way consumers now approach the process of making purchase decisions means that marketing's impact stems from a broad range of factors beyond conventional paid media.

Paid and owned media are controlled by marketers promoting their own products. For earned media, such marketers act as the initiator for users' responses. But in some cases, one marketer's owned media become another marketer's paid media — for instance, when an e-commerce retailer sells ad space on its Web site. We define such sold media as owned media whose traffic is so strong that other organizations place their content or e-commerce engines within that environment. This trend, which we believe is still in its infancy, effectively began with retailers and travel providers such as airlines and hotels and will no doubt go further. Johnson & Johnson, for example, has created BabyCenter, a stand-alone media property that promotes complementary and even competitive products. Besides generating income, the presence of other marketers makes the site seem objective, gives companies opportunities to learn valuable information about the appeal of other companies' marketing, and may help expand user traffic for all companies concerned.

The same dramatic technological changes that have provided marketers with more (and more diverse) communications choices have also increased the risk that passionate consumers will voice their opinions in quicker, more visible, and much more damaging ways. Such hijacked media are the opposite of earned media: an asset or campaign becomes hostage to consumers, other stakeholders, or activists who make negative allegations about a brand or product. Members of social networks, for instance, are learning that they can hijack media to apply pressure on the businesses that originally created them.

If that happens, passionate consumers would try to persuade others to boycott products, putting the reputation of the target company at risk. In such a case, the company's response may not be sufficiently quick or thoughtful, and the learning curve has been steep. Toyota Motor, for example, alleviated some of the damage from its recall crisis earlier this year with a relatively quick and well-orchestrated social-media response campaign, which included efforts to engage with consumers directly on sites such as Twitter and the social-news site Digg."""

# Passage 4: Text 4 (Cleaned, fully restored paragraph 4, no OCR annotations)
p4_content = """It's no surprise that Jennifer Senior's insightful, provocative magazine cover story, "I Love My Children, I Hate My Life," is arousing much chatter — nothing gets people talking like the suggestion that child rearing is anything less than a completely fulfilling, life-enriching experience. Rather than concluding that children make parents either happy or miserable, Senior suggests we need to redefine happiness: instead of thinking of it as something that can be measured by moment-to-moment joy, we should consider being happy as a past-tense condition. Even though the day-to-day experience of raising kids can be soul-crushingly hard, Senior writes that "the very things that in the moment dampen our moods can later be sources of intense gratification and delight."

The magazine cover showing an attractive mother holding a cute baby is hardly the only Madonna-and-child image on newsstands this week. There are also stories about newly adoptive — and newly single — mom Sandra Bullock, as well as the usual "Jennifer Aniston is pregnant" news. Practically every week features at least one celebrity mom, or mom-to-be, smiling on the newsstands.

In a society that so persistently celebrates procreation, is it any wonder that admitting you regret having children is equivalent to admitting you support kitten-killing? It doesn't seem quite fair, then, to compare the regrets of parents to the regrets of the childless. Unhappy parents rarely are provoked to wonder if they shouldn't have had kids, but unhappy childless folks are bothered with the message that children are the single most important thing in the world: obviously their misery must be a direct result of the gaping baby-size holes in their lives.

Of course, the image of parenthood that celebrity magazines like Us Weekly and People present is hugely unrealistic, especially when the parents are single mothers like Bullock. According to several studies concluding that parents are less happy than childless couples, single parents are the least happy of all. No shock there, considering how much work it is to raise a kid without a partner to lean on; yet to hear Sandra and Britney tell it, raising a kid on their "own" (read: with round-the-clock help) is a piece of cake.

It's hard to imagine that many people are dumb enough to want children just because Reese and Angelina make it look so glamorous: most adults understand that a baby is not a haircut. But it's interesting to wonder if the images we see every week of stress-free, happiness-enhancing parenthood aren't in some small, subconscious way contributing to our own dissatisfactions with the actual experience, in the same way that a small part of us hoped getting "the Rachel" might make us look just a little bit like Jennifer Aniston."""

# Passage 5: Part B (Humanities Professionalism / Louis Menand)
p5_content = """Directions:
In the following text, the first and third paragraphs [G] and [E] have been given. The other five paragraphs [A], [B], [C], [D], and [F] are in random order. For Questions 41-45, choose the most suitable paragraph for each numbered box (41-45). Write your answers on the ANSWER SHEET. (10 points)

[G] -> 41 -> 42 -> [E] -> 43 -> 44 -> 45

[A] No disciplines have seized on professionalism with as much enthusiasm as the humanities. You can, Mr. Menand points out, become a lawyer in three years and a medical doctor in four. But the regular time it takes to get a doctoral degree in the humanities is nine years. Not surprisingly, up to half of all doctoral students in English drop out before getting their degrees.

[B] His concern is mainly with the humanities: literature, languages, philosophy and so on. These are disciplines that are going out of style: 22% of American college graduates now major in business compared with only 2% in history and 4% in English. However, many leading American universities want their undergraduates to have a grounding in the basic canon of ideas that every educated person should possess. But most find it difficult to agree on what a "general education" should look like. At Harvard, Mr. Menand notes, "the great books are read because they have been read" — they form a sort of social glue.

[C] Equally unsurprisingly, only about half end up with professorships for which they entered graduate school. There are simply too few posts. This is partly because universities continue to produce ever more PhDs. But fewer students want to study humanities subjects: English departments awarded more bachelor's degrees in 1970-71 than they did 20 years later. Fewer students require fewer teachers. So, at the end of a decade of thesis-writing, many humanities students leave the profession to do something for which they have not been trained.

[D] One reason why it is hard to design and teach such courses is that they cut across the insistence by top American universities that liberal-arts education and professional education should be kept separate, taught in different schools. Many students experience both varieties. Although more than half of Harvard undergraduates end up in law, medicine or business, future doctors and lawyers must study a non-specialist liberal-arts degree before embarking on a professional qualification.

[E] Besides professionalising the professions by this separation, top American universities have professionalised the professor. The growth in public money for academic research has speeded the process: federal research grants rose fourfold between 1960 and 1990, but faculty teaching hours fell by half as research took its toll. Professionalism has turned the acquisition of a doctoral degree into a prerequisite for a successful academic career: as late as 1969 a third of American professors did not possess one. But the key idea behind professionalisation, argues Mr. Menand, is that "the knowledge and skills needed for a particular specialisation are transmissible but not transferable." So disciplines acquire a monopoly not just over the production of knowledge, but also over the production of the producers of knowledge.

[F] The key to reforming higher education, concludes Mr. Menand, is to alter the way in which "the producers of knowledge are produced". Otherwise, academics will continue to think dangerously alike, increasingly detached from the societies which they study, investigate and criticise. "Academic inquiry, at least in some fields, may need to become less exclusionary and more holistic." Yet quite how that happens, Mr. Menand does not say.

[G] The subtle and intelligent little book The Marketplace of Ideas: Reform and Resistance in the American University should be read by every student thinking of applying to take a doctoral degree. They may then decide to go elsewhere. For something curious has been happening in American universities, and Louis Menand, a professor of English at Harvard University, captured it skillfully."""

passages_configs = [
    (0, "cloze", 1, "Section I: Use of English", p0_content),
    (1, "reading", 1, "Text 1", p1_content),
    (2, "reading", 2, "Text 2", p2_content),
    (3, "reading", 3, "Text 3", p3_content),
    (4, "reading", 4, "Text 4", p4_content),
    (5, "reading_part_b", 5, "Part B", p5_content),
]

for idx, p_type, p_num, title, content in passages_configs:
    p = exam_data['passages'][idx]
    p['passage_type'] = p_type
    p['type'] = p_type
    p['passage_number'] = p_num
    p['sort_order'] = idx + 1
    p['title'] = title
    p['content'] = content

print("Passages updated successfully.")

# 3. Update Questions:
# Cloze Q1-Q20 explanations extraction from PDF to eliminate the raw word list
import fitz
doc = fitz.open(r"C:\Users\57867\Desktop\WYJ\考研\考研英语历年真题（分题型版）\英语一真题解析（2001-2025）\2011黄皮书真题解析（英语一）.pdf")
cloze_pdf_text = ""
for p in range(0, 7):
    cloze_pdf_text += f"\n--- PAGE {p+1} ---\n" + doc[p].get_text()
cloze_pdf_text = cloze_pdf_text.replace('\n& ［A］', '\n8. ［A］')

def get_cloze_exp(q_n):
    pat = rf'(\n{q_n}\..*?)(?=\n{q_n+1}\.|\n--- PAGE 7|\nText 1|\Z)'
    m = re.search(pat, cloze_pdf_text, re.S)
    if not m:
        return None
    raw = m.group(1).strip()
    # clean raw: find ［考点提炼］ or [考点提炼]
    kd_idx = raw.find('［考点提炼］')
    if kd_idx == -1:
        kd_idx = raw.find('[考点提炼]')
    if kd_idx != -1:
        # extract options translation
        opts_part = raw[:kd_idx].strip()
        body_part = raw[kd_idx:].strip()
        # Clean options part
        lines = [l.strip() for l in opts_part.splitlines() if l.strip()]
        opts_clean = []
        for l in lines:
            if l.startswith(f'{q_n}.'):
                l = l[len(f'{q_n}.'):].strip()
            if l:
                opts_clean.append(l)
        opts_header = ' '.join(opts_clean)
        # Format as standard explanation
        res = f"［选项辨析］{opts_header}\n\n{body_part}"
        return res
    return raw

# Update Q1-Q20
for i in range(20):
    q = exam_data['questions'][i]
    q_num = i + 1
    q['stem'] = f"Choose the best option for blank [{q_num}] in the passage:"
    q['q_type'] = "cloze_item"
    q['points'] = 0.5
    q['sort_order'] = q_num
    pdf_exp = get_cloze_exp(q_num)
    if pdf_exp:
        q['explanation'] = pdf_exp

# Update Q21-Q40
# Ensure points are float 2.0, sort_order is 21..40
for i in range(20, 40):
    q = exam_data['questions'][i]
    q_num = i + 1
    q['q_type'] = "reading_item"
    q['points'] = 2.0
    q['sort_order'] = q_num

# Special fix for Q25: Ensure question stem and options match exam PDF
q25 = exam_data['questions'][24]
q25['stem'] = "Regarding Gilbert's role in revitalizing the Philharmonic, the author feels ________."
q25['options'] = [
    {"key": "A", "text": "doubtful", "value": "A"},
    {"key": "B", "text": "enthusiastic", "value": "B"},
    {"key": "C", "text": "confident", "value": "C"},
    {"key": "D", "text": "puzzled", "value": "D"}
]
q25['correct_answer'] = "A"
q25['explanation'] = """［精准定位］根据题干revitalizing定位到第五段。该段②句指出Gilbert在新音乐方面的能力受到音乐界的广泛认可，但③句随即以疑问句进行质疑，④句进而指出这一措施的局限性：仅仅扩充乐团的演奏曲目是远远不够的。可见作者对吉尔伯特能否振兴乐团持怀疑态度，［A］正确。

［命题解密］正确项［A］是对③句质疑及④句“仅仅扩充曲目远远不够”所传达的作者怀疑态度的同义概括。

［错项排除］［B］、［C］均与作者质疑立场截然相反。［D］具有一定干扰性，但质疑（doubtful）和困惑（puzzled）有本质区别：质疑包含作者自身的判断与保留意见，困惑仅表现为不解、迷茫，而作者在末句清楚指明了乐团必须做的事情（must first change the relationship），并无困惑之意。

［技巧总结］本题属于观点态度题。解题关键在于抓住第五段转折质疑处的作者基调（But what will be the nature of that difference? Merely expanding the repertoire will not be enough），准确体会作者的保留与怀疑态度。"""

# Special check for Q40: Ensure correct_answer is B
q40 = exam_data['questions'][39]
q40['correct_answer'] = "B"

# Update Q41-Q45: New Type (Ordering)
part_b_answers = ['B', 'D', 'A', 'C', 'F']
part_b_opts = [
    {"key": "A", "text": "[A] No disciplines have seized on professionalism with as much enthusiasm as the humanities...", "value": "A"},
    {"key": "B", "text": "[B] His concern is mainly with the humanities: literature, languages, philosophy and so on...", "value": "B"},
    {"key": "C", "text": "[C] Equally unsurprisingly, only about half end up with professorships for which they entered graduate school...", "value": "C"},
    {"key": "D", "text": "[D] One reason why it is hard to design and teach such courses is that they cut across the insistence by top American universities...", "value": "D"},
    {"key": "E", "text": "[E] Besides professionalising the professions by this separation, top American universities have professionalised the professor...", "value": "E"},
    {"key": "F", "text": "[F] The key to reforming higher education, concludes Mr. Menand, is to alter the way in which the producers of knowledge are produced...", "value": "F"},
    {"key": "G", "text": "[G] The subtle and intelligent little book The Marketplace of Ideas: Reform and Resistance in the American University...", "value": "G"}
]

for i in range(40, 45):
    q = exam_data['questions'][i]
    q_num = i + 1
    q['q_type'] = "reading_item"
    q['points'] = 2.0
    q['sort_order'] = q_num
    q['stem'] = f"Choose the correct paragraph [A]-[G] for position ({q_num}):"
    q['options'] = part_b_opts
    q['correct_answer'] = part_b_answers[i - 40]

with open(exam_json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("2011 ky1 pure gold json built and saved successfully!")
