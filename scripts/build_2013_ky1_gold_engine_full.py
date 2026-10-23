# -*- coding: utf-8 -*-
"""
build_2013_ky1_gold_engine_full.py
Complete Forensic Golden Reconstruction Engine for 2013 ky1 exam
UUID: 6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5
"""

import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting 2013 ky1 Golden Reconstruction Engine ===")

json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5.json'
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

exam_id = "6c56eb6e-75e7-54d2-a03e-3ad93fc61fa5"

# 1. Update Exam Meta
if "exam" in exam_data:
    exam_data["exam"]["title"] = "2013年全国硕士研究生入学统一考试英语（一）真题"
    exam_data["exam"]["total_score"] = 60.0
exam_data["title"] = "2013年全国硕士研究生入学统一考试英语（一）真题"
exam_data["total_score"] = 60.0

# 2. Reconstruct Passages 0-5
# Passage 0: Cloze
cloze_p1 = "People are, on the whole, poor at considering background information when making individual decisions. At first glance this might seem like a strength that [1] the ability to make judgments which are unbiased by [2] factors. But Dr Uri Simonsohn speculated that an inability to consider the big [3] was leading decision-makers to be biased by the daily samples of information they were working with. [4], he theorised that a judge [5] of appearing too soft [6] crime might be more likely to send someone to prison [7] he had already sentenced five or six other defendants only to forced community service on that day."
cloze_p2 = "To [8] this idea, he turned to the university-admissions process. In theory, the [9] of an applicant should not depend on the few others [10] randomly for interview during the same day, but Dr Simonsohn suspected the truth was [11]."
cloze_p3 = "He studied the results of 9,323 MBA interviews [12] by 31 admissions officers. The interviewers had [13] applicants on a scale of one to five. This scale [14] numerous factors into consideration. The scores were [15] used in conjunction with an applicant's score on the Graduate Management Admission Test, or GMAT, a standardised exam which is [16] out of 800 points, to make a decision on whether to accept him or her."
cloze_p4 = "Dr Simonsohn found if the score of the previous candidate in a daily series of interviewees was 0.75 points or more higher than that of the one [17] that, then the score for the next applicant would [18] by an average of 0.075 points. This might sound small, but to [19] the effects of such a decrease a candidate would need 30 more GMAT points than would otherwise have been [20]."

# Passage 1: Text 1
t1_p1 = "In the 2006 film version of The Devil Wears Prada, Miranda Priestly, played by Meryl Streep, scolds her unattractive assistant for imagining that high fashion doesn't affect her. Priestly explains how the deep blue color of the assistant's sweater descended over the years from fashion shows to department stores and to the bargain bin in which the poor girl doubtless found her garment."
t1_p2 = "This top-down conception of the fashion business couldn't be more out of date or at odds with the feverish world described in Overdressed, Elizabeth Cline's three-year indictment of \"fast fashion\". In the last decade or so, advances in technology have allowed mass-market labels such as Zara, H&M, and Uniqlo to react to trends more quickly and anticipate demand more precisely. Quicker turnarounds mean less wasted inventory, more frequent releases, and more profit. These labels encourage style-conscious consumers to see clothes as disposable—meant to last only a wash or two, although they don't advertise that—and to renew their wardrobe every few weeks. By offering on-trend items at dirt-cheap prices, Cline argues, these brands have hijacked fashion cycles, shaking an industry long accustomed to a seasonal pace."
t1_p3 = "The victims of this revolution, of course, are not limited to designers. For H&M to offer a $5.95 knit miniskirt in all its 2,300-plus stores around the world, it must rely on low-wage overseas labor, order in volumes that strain natural resources, and use massive amounts of harmful chemicals."
t1_p4 = "Overdressed is the fashion world's answer to consumer-activist bestsellers like Michael Pollan's The Omnivore's Dilemma. \"Mass-produced clothing, like fast food, fills a hunger and need, yet is non-durable and wasteful,\" Cline argues. Americans, she finds, buy roughly 20 billion garments a year—about 64 items per person—and no matter how much they give away, this excess leads to waste."
t1_p5 = "Towards the end of Overdressed, Cline introduced her ideal, a Brooklyn woman named Sarah Kate Beaumont, who since 2008 has made all of her own clothes—and beautifully. But as Cline is the first to note, it took Beaumont decades to perfect her craft; her example can't be knocked off."
t1_p6 = "Though several fast-fashion companies have made efforts to curb their impact on labor and the environment—including H&M, with its green Conscious Collection line—Cline believes lasting change can only be effected by the customer. She exhibits the idealism common to many advocates of sustainability, be it in food or in energy. Vanity is a constant; people will only start shopping more sustainably when they can't afford not to."

# Passage 2: Text 2
t2_p1 = "An old saying has it that half of all advertising budgets are wasted—the trouble is, no one knows which half. In the internet age, at least in theory, this fraction can be much reduced. By watching what people search for, click on and say online, companies can aim \"behavioural\" ads at those most likely to buy."
t2_p2 = "In the past couple of weeks a quarrel has illustrated the value to advertisers of such fine-grained information: Should advertisers assume that people are happy to be tracked and sent behavioural ads? Or should they have explicit permission?"
t2_p3 = "In December 2010 America's Federal Trade Commission (FTC) proposed adding a \"do not track\" (DNT) option to internet browsers, so that users could tell advertisers that they did not want to be followed. Microsoft's Internet Explorer and Apple's Safari both offer DNT; Google's Chrome is due to do so this year. In February the FTC and the Digital Advertising Alliance (DAA) agreed that the industry would get cracking on responding to DNT requests."
t2_p4 = "On May 31st Microsoft set off the row. It said that Internet Explorer 10, the version due to appear with Windows 8, would have DNT as a default."
t2_p5 = "Advertisers are horrified. Human nature being what it is, most people stick with default settings. Few switch DNT on now, but if tracking is off it will stay off. Bob Liodice, the chief executive of the Association of National Advertisers, says consumers will be worse off if the industry cannot collect information about their preferences. People will not get fewer ads, he says. \"They'll get less meaningful, less targeted ads.\""
t2_p6 = "It is not yet clear how advertisers will respond. Getting a DNT signal does not oblige anyone to stop tracking, although some companies have promised to do so. Unable to tell whether someone really objects to behavioural ads or whether they are sticking with Microsoft's default, some may ignore a DNT signal and press on anyway."
t2_p7 = "Also unclear is why Microsoft has gone it alone. After all, it has an ad business too, which it says will comply with DNT requests, though it is still working out how. If it is trying to upset Google, which relies almost wholly on advertising, it has chosen an indirect method: there is no guarantee that DNT by default will become the norm. DNT does not seem an obviously huge selling point for Windows 8—though the firm has compared some of its other products favourably with Google's on that count before. Brendon Lynch, Microsoft's chief privacy officer, blogged: \"We believe consumers should have more control.\" Could it really be that simple?"

# Passage 3: Text 3
t3_p1 = "Up until a few decades ago, our visions of the future were largely—though by no means uniformly—glowingly positive. Science and technology would cure all the ills of humanity, leading to lives of fulfilment and opportunity for all."
t3_p2 = "Now utopia has grown unfashionable, as we have gained a deeper appreciation of the range of threats facing us, from asteroid strike and epidemic flu to climate change and nuclear devastation. You might even be tempted to assume that humanity has little future to look forward to."
t3_p3 = "But such gloominess is misplaced. The fossil record shows that many species have endured for millions of years—so why shouldn't we? Take a broader look at our species' place in the universe, and it becomes clear that we have an excellent chance of surviving for tens, if not hundreds, of thousands of years. Look up Homo sapiens in the \"Red List\" of threatened species of the International Union for the Conservation of Nature (IUCN), and you will read: \"Listed as Least Concern as the species is very widely distributed, adaptable, currently increasing, and there are no major threats resulting in an overall population decline.\""
t3_p4 = "So what does our deep future hold? A growing number of researchers and organisations are now thinking seriously about that. For example, the Long Now Foundation, based in San Francisco, have created a mechanical clock that has been designed to still be marking time thousands of years hence."
t3_p5 = "Perhaps willfully, it may be easier to think about such lengthy timescales than about the more immediate future. The potential evolution of today's technology, and its social consequences, is dazzlingly complicated, and it's perhaps best left to science fiction writers and futurologists to explore the many possibilities we can envisage. That's one reason why we have launched Arc, a new publication dedicated to the near future."
t3_p6 = "But take a longer view and there is a surprising amount that we can say with considerable assurance. As so often, the past holds the key to the future: we have now identified enough of the long-term patterns shaping the history of the planet, and our species, to make evidence-based forecasts about the situations in which our descendants will find themselves."
t3_p7 = "This long perspective makes the pessimistic view of our prospects seem more likely to be a passing fad. To be sure, the future is not all rosy. But we are now knowledgeable enough to reduce many of the risks that threatened the existence of earlier humans, and to improve the lot of those to come."

# Passage 4: Text 4
t4_p1 = "On a five to three vote, the Supreme Court knocked out much of Arizona's immigration law Monday—a modest policy victory for the Obama Administration. But on the more important matter of the Constitution, the decision was an 8-0 defeat for the Administration's effort to upset the balance of power between the federal government and the states."
t4_p2 = "In Arizona v. United States, the majority overturned three of the four contested provisions of Arizona's controversial plan to have state and local police enforce federal immigration law. The Constitutional principles that Washington alone has the power to \"establish a uniform Rule of Naturalization\" and that federal laws precede state laws are noncontroversial. Arizona had attempted to fashion state policies that ran parallel to the existing federal ones."
t4_p3 = "Justice Anthony Kennedy, joined by Chief Justice John Roberts and the Court's liberals, ruled that the state flew too close to the federal sun. He wrote that Congress had deliberately \"occupied the field\" of the overturned provisions and that Arizona had thus intruded on the federal's privileged powers."
t4_p4 = "However, the Justices said that Arizona police would be allowed to verify the legal status of people who come in contact with law enforcement. That's because Congress has always envisioned joint federal-state immigration enforcement and explicitly encourages state officers to share information and cooperate with federal colleagues."
t4_p5 = "Two of the three objecting Justices—Samuel Alito and Clarence Thomas—agreed with this Constitutional logic but disagreed about which provisions should be struck down. Only Justice Antonin Scalia was willing to defend the privileged powers of states to regulate immigration, going back to the Naturalization Act of 1798 to argue for \"the alien and sedition acts\"."
t4_p6 = "The 8-0 objection to President Obama turns on what Justice Samuel Alito describes in his objection as \"a shocking assertion of federal power\". The White House argued that after Congress set a uniform immigration policy the Administration had the exclusive authority to enforce that law, not local or state officers. Arizona, this argument continues, had no power to write laws that enforced federal policies unless the White House agreed with them. In other words, the Administration claimed that the Constitution gave it the authority to invalidate any otherwise legitimate state law that it disagrees with."
t4_p7 = "Some powers do belong exclusively to the federal government, and control of citizenship and the borders is among them. But if the Constitution really gives the executive branch broad power to ignore the laws passed by Congress—and the right to tell states they must ignore them as well—then we have a problem much bigger than Arizona. Fortunately, all eight Justices rightly rejected this remarkable claim."

# Passage 5: Part B
pb_p1 = "The social sciences are flourishing. As of 2005, there were almost half a million professional social scientists from all fields in the world, working both inside and outside academia. According to the World Social Science Report 2010, the number of social-science students worldwide has swollen by about 11% every year since 2000."
pb_p2 = "Yet this enormous resource is not contributing enough to today's global challenges including climate change, security, sustainable development and health. [41] ____________ Humanity has the necessary agro-technological tools to eradicate hunger, from genetically engineered crops to artificial fertilizers. Here, too, the problems are social: the organization and distribution of food, wealth and prosperity."
pb_p3 = "[42] ____________ This is a shame—the community should be grasping the opportunity to raise its influence in the real world. To paraphrase the great social scientist Joseph Schumpeter: there is no radical innovation without creative destruction."
pb_p4 = "Today's social sciences are largely focused on disciplinary problems and internal scholarly debates, rather than topics with external impact. Analyses in the World Social Science Report 2010 show that the number of papers including the keywords \"environmental change\" or \"climate change\" have increased rapidly since 2004. [43] ____________"
pb_p5 = "When they do tackle practical issues, the focus is generally on the local level: in Belgium, for example, research focuses on Belgian problems. Whether this will contribute to an overall accumulation of knowledge is doubtful."
pb_p6 = "The problem is not necessarily the amount of available funding. [44] ____________ This is an adequate amount so long as it is aimed in the right direction. Social scientists who complain about a lack of funding should not expect more in today's economic climate."
pb_p7 = "The trick is to direct these funds better. The European Union Framework funding programs have long had a category specifically targeted at social scientists. This year, it was proposed that the system be changed: Horizon 2020, a new program to be enacted in 2014, would not have such a category. This has resulted in protests from social scientists. But the intention is not to neglect social science; rather, the complete opposite. [45] ____________ That should create more collaborative endeavors and help to develop projects aimed directly at solving global problems."

pb_options = """[A] The idea is to force social scientists to integrate their work with other categories, including health and demographic change; food security; marine research and the bio-economy; clean, efficient energy; and inclusive, innovative and secure societies.

[B] The solution is to change the mindset of the academic community, and what it considers to be its main goal. Global challenges and social innovation ought to receive much more attention from scientists, especially the young ones.

[C] It could be that we are evolving two communities of social scientists: one that is discipline-oriented and publishing in highly specialized journals, and one that is problem-oriented and publishing elsewhere, such as policy briefs.

[D] However, the numbers are still small: in 2010, about 1,600 of the 100,000 social-sciences papers published globally included one of these keywords.

[E] These issues all have root causes in human behavior: all require behavioral change and social innovations, as well as technological development. Stemming climate change, for example, is as much about changing consumption patterns and promoting tax acceptance as it is about developing clean energy.

[F] Despite these factors, many social scientists seem reluctant to tackle such problems. And in Europe, some are up in arms over a proposal to drop a specific funding category for social-science research and to integrate it within cross-cutting topics of sustainable development.

[G] During the late 1990s, national spending on social sciences and the humanities as a percentage of all research and development funds—including government, higher education, non-profit and corporate—varied from around 4% to 25%; in most European nations, it is about 15%."""

passages_data = [
    {
        "id": "135973f9-098b-5f42-950d-bf4050b631de",
        "exam_id": exam_id,
        "title": "Section I: Use of English",
        "content": "\n\n".join([cloze_p1, cloze_p2, cloze_p3, cloze_p4]),
        "section_type": "cloze",
        "sort_order": 1
    },
    {
        "id": "10d8fb90-e783-5aab-aa05-4b3dc983dc1b",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part A - Text 1",
        "content": "\n\n".join([t1_p1, t1_p2, t1_p3, t1_p4, t1_p5, t1_p6]),
        "section_type": "reading",
        "sort_order": 2
    },
    {
        "id": "af9727e8-1f96-57e2-bbb7-d356a28319d0",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part A - Text 2",
        "content": "\n\n".join([t2_p1, t2_p2, t2_p3, t2_p4, t2_p5, t2_p6, t2_p7]),
        "section_type": "reading",
        "sort_order": 3
    },
    {
        "id": "bc537609-ecd4-512d-923d-97b884b42f06",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part A - Text 3",
        "content": "\n\n".join([t3_p1, t3_p2, t3_p3, t3_p4, t3_p5, t3_p6, t3_p7]),
        "section_type": "reading",
        "sort_order": 4
    },
    {
        "id": "06e64256-4883-5c05-9182-868310a80f81",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part A - Text 4",
        "content": "\n\n".join([t4_p1, t4_p2, t4_p3, t4_p4, t4_p5, t4_p6, t4_p7]),
        "section_type": "reading",
        "sort_order": 5
    },
    {
        "id": "f1619752-4d99-5e3f-99ee-a3214c446001",
        "exam_id": exam_id,
        "title": "Section II: Reading Comprehension Part B",
        "content": "\n\n".join([pb_p1, pb_p2, pb_p3, pb_p4, pb_p5, pb_p6, pb_p7, pb_options]),
        "section_type": "reading",
        "sort_order": 6
    }
]

exam_data["passages"] = passages_data

# 3. Extract High Quality Clean Explanations from Huangpishu PDF
with open(r'd:\A16pro\Aing\antigravity\supabase\scripts\pdf_dump_2013.txt', 'r', encoding='utf-8') as f:
    dump_text = f.read()

def clean_ocr(s):
    if not s:
        return ""
    s = s.replace('［', '[').replace('］', ']').replace('【', '[').replace('】', ']')
    s = s.replace('•', '·').replace('・', '·').replace('“', '"').replace('”', '"')
    s = re.sub(r'PAGE \d+ =+', '', s)
    s = re.sub(r'[①②③④⑤⑥⑦⑧⑨⑩❶❷❸❹❺❻❼❽❾❿]', '', s)
    s = re.sub(r'\n+', '\n', s)
    return s.strip()

# Cloze explanations
cloze_expls = {}
for q in range(1, 21):
    q_str = '&' if q == 8 else f'{q}.'
    pos = dump_text.find(f'{q_str} ［A］')
    if pos == -1:
        pos = dump_text.find(f'{q_str} [A]')
    if pos != -1:
        next_str = '&' if q+1 == 8 else f'{q+1}.'
        end_pos = dump_text.find(f'{next_str} ［A］', pos)
        if end_pos == -1:
            end_pos = dump_text.find(f'{next_str} [A]', pos)
        if end_pos == -1:
            end_pos = pos + 2500
        
        block = dump_text[pos:end_pos]
        for cut in ['Section II', 'Text 1', 'II ❶', 'III ❶', 'IV ❶', 'm ❶']:
            c_pos = block.find(cut)
            if c_pos > 200:
                block = block[:c_pos]
        cloze_expls[q] = clean_ocr(block)

# Reading explanations
reading_expls = {}
for q in range(21, 41):
    m = re.search(rf'(?:^|\n)\s*{q}\s*[\.・．、]\s*(.*?)(?=\n\s*(?:{q+1}\s*[\.・．、]|Section|Part\s+[A-C]|PAGE 17|PAGE 26|PAGE 37|PAGE 45|\Z))', dump_text, re.DOTALL)
    if m:
        block = m.group(0)
        lines = block.split('\n')
        clean_lines = []
        in_expl = False
        for l in lines:
            l_s = l.strip()
            if any(k in l_s for k in ['［精准定位］', '[精准定位]', '［命题解密］', '[命题解密]', '［考点提炼］', '[考点提炼]']):
                in_expl = True
            if in_expl:
                if any(k in l_s for k in ['•词汇注释', '•语篇分析', '•经典搭配', '【深层解读】', '总体分析', '外教朗读', 'Text ']):
                    break
                if re.match(r'^(I|II|III|IV|V|VI|VII)\s+[❶回囤]', l_s):
                    break
                if any(l_s.startswith(tr) for tr in ['在这场亚利桑那', '在过去的两周里', '当然，这一革命', '但是，如果采取更长远', '或许有悖常理', '广告商将做何反应尚不清楚', '广告商们恐慌了']):
                    break
            clean_lines.append(l)
        reading_expls[q] = clean_ocr("\n".join(clean_lines))

# Part B explanations
p51 = dump_text.find("PAGE 51 ==")
p54 = dump_text.find("PAGE 54 ==")
sub_pb = dump_text[p51:p54]

pb_expls = {}
for q in range(41, 46):
    m = re.search(rf'{q}\.\s*本题考核的知识点是：(.*?)(?=\n\s*(?:{q+1}\.|\Z|Part|PAGE|；Part))', sub_pb, re.DOTALL)
    if m:
        raw_pb = f"{q}. 【考点提炼】本题考核的知识点是：" + m.group(1).strip()
        pb_expls[q] = clean_ocr(raw_pb)

# 4. Canonical Question Definitions (Q1-Q45)
raw_questions_defs = [
    # Cloze (Q1-Q20)
    (1, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [1] in the passage:",
     {"A": "grants", "B": "submits", "C": "transmits", "D": "delivers"}, "A"),
    (2, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [2] in the passage:",
     {"A": "minor", "B": "external", "C": "crucial", "D": "objective"}, "B"),
    (3, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [3] in the passage:",
     {"A": "issue", "B": "vision", "C": "picture", "D": "moment"}, "C"),
    (4, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [4] in the passage:",
     {"A": "Above all", "B": "On average", "C": "In principle", "D": "For example"}, "D"),
    (5, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [5] in the passage:",
     {"A": "fond", "B": "fearful", "C": "capable", "D": "thoughtless"}, "B"),
    (6, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [6] in the passage:",
     {"A": "in", "B": "for", "C": "to", "D": "on"}, "D"),
    (7, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [7] in the passage:",
     {"A": "if", "B": "until", "C": "though", "D": "unless"}, "A"),
    (8, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [8] in the passage:",
     {"A": "test", "B": "emphasize", "C": "share", "D": "promote"}, "A"),
    (9, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [9] in the passage:",
     {"A": "decision", "B": "quality", "C": "status", "D": "success"}, "D"),
    (10, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [10] in the passage:",
     {"A": "found", "B": "studied", "C": "chosen", "D": "identified"}, "C"),
    (11, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [11] in the passage:",
     {"A": "otherwise", "B": "defensible", "C": "replaceable", "D": "exceptional"}, "A"),
    (12, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [12] in the passage:",
     {"A": "inspired", "B": "expressed", "C": "conducted", "D": "secured"}, "C"),
    (13, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [13] in the passage:",
     {"A": "assigned", "B": "rated", "C": "matched", "D": "arranged"}, "B"),
    (14, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [14] in the passage:",
     {"A": "put", "B": "got", "C": "took", "D": "gave"}, "C"),
    (15, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [15] in the passage:",
     {"A": "instead", "B": "then", "C": "ever", "D": "rather"}, "B"),
    (16, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [16] in the passage:",
     {"A": "selected", "B": "passed", "C": "marked", "D": "introduced"}, "C"),
    (17, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [17] in the passage:",
     {"A": "below", "B": "after", "C": "above", "D": "before"}, "D"),
    (18, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [18] in the passage:",
     {"A": "jump", "B": "float", "C": "fluctuate", "D": "drop"}, "D"),
    (19, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [19] in the passage:",
     {"A": "achieve", "B": "undo", "C": "maintain", "D": "disregard"}, "B"),
    (20, "cloze_item", 0.5, "135973f9-098b-5f42-950d-bf4050b631de",
     "Choose the best option for blank [20] in the passage:",
     {"A": "necessary", "B": "possible", "C": "promising", "D": "helpful"}, "A"),

    # Reading Text 1 (Q21-Q25)
    (21, "reading_item", 2.0, "10d8fb90-e783-5aab-aa05-4b3dc983dc1b",
     "Priestly criticizes her assistant for her ________.",
     {"A": "insensitivity to fashion", "B": "obsession with high fashion",
      "C": "poor bargaining skill", "D": "lack of imagination"}, "A"),
    (22, "reading_item", 2.0, "10d8fb90-e783-5aab-aa05-4b3dc983dc1b",
     "According to Cline, mass-market labels urge consumers to ________.",
     {"A": "combat unnecessary waste", "B": "shop for their garments more frequently",
      "C": "resist the influence of advertisements", "D": "shut out the feverish fashion world"}, "B"),
    (23, "reading_item", 2.0, "10d8fb90-e783-5aab-aa05-4b3dc983dc1b",
     "The word \"indictment\" (Line 3, Para. 2) is closest in meaning to ________.",
     {"A": "tolerance", "B": "indifference", "C": "enthusiasm", "D": "accusation"}, "D"),
    (24, "reading_item", 2.0, "10d8fb90-e783-5aab-aa05-4b3dc983dc1b",
     "Which of the following can be inferred from the last paragraph?",
     {"A": "Vanity has more often been found in idealists.", "B": "The fast-fashion industry ignores sustainability.",
      "C": "Pricing is vital to environment-friendly purchasing.", "D": "People are more interested in unaffordable garments."}, "C"),
    (25, "reading_item", 2.0, "10d8fb90-e783-5aab-aa05-4b3dc983dc1b",
     "What is the subject of the text?",
     {"A": "Satire on an extravagant lifestyle.", "B": "Challenge to a high-fashion myth.",
      "C": "Criticism of the fast-fashion industry.", "D": "Exposure of a mass-market secret."}, "C"),

    # Reading Text 2 (Q26-Q30)
    (26, "reading_item", 2.0, "af9727e8-1f96-57e2-bbb7-d356a28319d0",
     "It is suggested in Paragraph 1 that \"behavioural\" ads help advertisers to ________.",
     {"A": "provide better online services", "B": "ease competition among themselves",
      "C": "avoid complaints from consumers", "D": "lower their operational costs"}, "D"),
    (27, "reading_item", 2.0, "af9727e8-1f96-57e2-bbb7-d356a28319d0",
     "\"the industry\" (Line 4, Para. 3) refers to ________.",
     {"A": "internet browser developers", "B": "digital information analysts",
      "C": "e-commerce conductors", "D": "online advertisers"}, "A"),
    (28, "reading_item", 2.0, "af9727e8-1f96-57e2-bbb7-d356a28319d0",
     "Bob Liodice holds that setting DNT as a default ________.",
     {"A": "may cut the number of junk ads", "B": "fails to affect the ad industry",
      "C": "will not benefit consumers", "D": "goes against human nature"}, "C"),
    (29, "reading_item", 2.0, "af9727e8-1f96-57e2-bbb7-d356a28319d0",
     "Which of the following is true according to Paragraph 6?",
     {"A": "Advertisers are willing to implement DNT.", "B": "DNT may not serve its intended purpose.",
      "C": "DNT is losing its popularity among consumers.", "D": "Advertisers are obliged to offer behavioural ads."}, "B"),
    (30, "reading_item", 2.0, "af9727e8-1f96-57e2-bbb7-d356a28319d0",
     "The author's attitude towards what Brendon Lynch said in his blog is one of ________.",
     {"A": "indulgence", "B": "understanding", "C": "appreciation", "D": "skepticism"}, "D"),

    # Reading Text 3 (Q31-Q35)
    (31, "reading_item", 2.0, "bc537609-ecd4-512d-923d-97b884b42f06",
     "Our vision of the future used to be inspired by ________.",
     {"A": "our desire for lives of fulfillment", "B": "our faith in science and technology",
      "C": "our awareness of potential risks", "D": "our belief in equal opportunity"}, "B"),
    (32, "reading_item", 2.0, "bc537609-ecd4-512d-923d-97b884b42f06",
     "The IUCN's \"Red List\" suggests that human beings are ________.",
     {"A": "a sustained species", "B": "the world's dominant power",
      "C": "a threat to the environment", "D": "a misplaced race"}, "A"),
    (33, "reading_item", 2.0, "bc537609-ecd4-512d-923d-97b884b42f06",
     "Which of the following is true according to Paragraph 5?",
     {"A": "The interest in science fiction is on the rise.", "B": "Arc helps limit the scope of futurological studies.",
      "C": "Technology offers solutions to social problems.", "D": "Our immediate future is hard to conceive."}, "D"),
    (34, "reading_item", 2.0, "bc537609-ecd4-512d-923d-97b884b42f06",
     "To ensure the future of mankind, it is crucial to ________.",
     {"A": "adopt an optimistic view of the world", "B": "draw on our experience from the past",
      "C": "explore our planet's abundant resources", "D": "curb our ambition to reshape history"}, "B"),
    (35, "reading_item", 2.0, "bc537609-ecd4-512d-923d-97b884b42f06",
     "Which of the following would be the best title for the text?",
     {"A": "The Ever-bright Prospects of Mankind.", "B": "Science, Technology and Humanity.",
      "C": "Evolution of the Human Species.", "D": "Uncertainty about Our Future."}, "A"),

    # Reading Text 4 (Q36-Q40)
    (36, "reading_item", 2.0, "06e64256-4883-5c05-9182-868310a80f81",
     "Three provisions of Arizona's plan were overturned because they ________.",
     {"A": "disturbed the power balance between different states", "B": "overstepped the authority of federal immigration law",
      "C": "deprived the federal police of Constitutional powers", "D": "contradicted both the federal and state policies"}, "B"),
    (37, "reading_item", 2.0, "06e64256-4883-5c05-9182-868310a80f81",
     "On which of the following did the Justices agree, according to Paragraph 4?",
     {"A": "Congress's intervention in immigration enforcement.", "B": "Federal officers' duty to withhold immigrants' information.",
      "C": "States' legitimate role in immigration enforcement.", "D": "States' independence from federal immigration law."}, "C"),
    (38, "reading_item", 2.0, "06e64256-4883-5c05-9182-868310a80f81",
     "It can be inferred from Paragraph 5 that the Alien and Sedition Acts ________.",
     {"A": "stood in favor of the states", "B": "supported the federal statute",
      "C": "undermined the states' interests", "D": "violated the Constitution"}, "A"),
    (39, "reading_item", 2.0, "06e64256-4883-5c05-9182-868310a80f81",
     "The White House claims that its power of enforcement ________.",
     {"A": "is dependent on the states' support", "B": "is established by federal statutes",
      "C": "outweighs that held by the states", "D": "rarely goes against state laws"}, "C"),
    (40, "reading_item", 2.0, "06e64256-4883-5c05-9182-868310a80f81",
     "What can be learned from the last paragraph?",
     {"A": "Immigration issues are usually decided by Congress.", "B": "The Administration is dominant over immigration issues.",
      "C": "Justices wanted to strengthen its coordination with Congress.", "D": "Justices intended to check the power of the Administration."}, "D"),

    # Reading Part B (Q41-Q45)
    (41, "reading_item", 2.0, "f1619752-4d99-5e3f-99ee-a3214c446001",
     "Choose the best paragraph [A]-[G] that fits into gap (41):",
     {
         "A": "The idea is to force social scientists to integrate their work with other categories, including health and demographic change; food security; marine research and the bio-economy; clean, efficient energy; and inclusive, innovative and secure societies.",
         "B": "The solution is to change the mindset of the academic community, and what it considers to be its main goal. Global challenges and social innovation ought to receive much more attention from scientists, especially the young ones.",
         "C": "It could be that we are evolving two communities of social scientists: one that is discipline-oriented and publishing in highly specialized journals, and one that is problem-oriented and publishing elsewhere, such as policy briefs.",
         "D": "However, the numbers are still small: in 2010, about 1,600 of the 100,000 social-sciences papers published globally included one of these keywords.",
         "E": "These issues all have root causes in human behavior: all require behavioral change and social innovations, as well as technological development. Stemming climate change, for example, is as much about changing consumption patterns and promoting tax acceptance as it is about developing clean energy.",
         "F": "Despite these factors, many social scientists seem reluctant to tackle such problems. And in Europe, some are up in arms over a proposal to drop a specific funding category for social-science research and to integrate it within cross-cutting topics of sustainable development.",
         "G": "During the late 1990s, national spending on social sciences and the humanities as a percentage of all research and development funds—including government, higher education, non-profit and corporate—varied from around 4% to 25%; in most European nations, it is about 15%."
     }, "E"),
    (42, "reading_item", 2.0, "f1619752-4d99-5e3f-99ee-a3214c446001",
     "Choose the best paragraph [A]-[G] that fits into gap (42):",
     {
         "A": "The idea is to force social scientists to integrate their work with other categories, including health and demographic change; food security; marine research and the bio-economy; clean, efficient energy; and inclusive, innovative and secure societies.",
         "B": "The solution is to change the mindset of the academic community, and what it considers to be its main goal. Global challenges and social innovation ought to receive much more attention from scientists, especially the young ones.",
         "C": "It could be that we are evolving two communities of social scientists: one that is discipline-oriented and publishing in highly specialized journals, and one that is problem-oriented and publishing elsewhere, such as policy briefs.",
         "D": "However, the numbers are still small: in 2010, about 1,600 of the 100,000 social-sciences papers published globally included one of these keywords.",
         "E": "These issues all have root causes in human behavior: all require behavioral change and social innovations, as well as technological development. Stemming climate change, for example, is as much about changing consumption patterns and promoting tax acceptance as it is about developing clean energy.",
         "F": "Despite these factors, many social scientists seem reluctant to tackle such problems. And in Europe, some are up in arms over a proposal to drop a specific funding category for social-science research and to integrate it within cross-cutting topics of sustainable development.",
         "G": "During the late 1990s, national spending on social sciences and the humanities as a percentage of all research and development funds—including government, higher education, non-profit and corporate—varied from around 4% to 25%; in most European nations, it is about 15%."
     }, "F"),
    (43, "reading_item", 2.0, "f1619752-4d99-5e3f-99ee-a3214c446001",
     "Choose the best paragraph [A]-[G] that fits into gap (43):",
     {
         "A": "The idea is to force social scientists to integrate their work with other categories, including health and demographic change; food security; marine research and the bio-economy; clean, efficient energy; and inclusive, innovative and secure societies.",
         "B": "The solution is to change the mindset of the academic community, and what it considers to be its main goal. Global challenges and social innovation ought to receive much more attention from scientists, especially the young ones.",
         "C": "It could be that we are evolving two communities of social scientists: one that is discipline-oriented and publishing in highly specialized journals, and one that is problem-oriented and publishing elsewhere, such as policy briefs.",
         "D": "However, the numbers are still small: in 2010, about 1,600 of the 100,000 social-sciences papers published globally included one of these keywords.",
         "E": "These issues all have root causes in human behavior: all require behavioral change and social innovations, as well as technological development. Stemming climate change, for example, is as much about changing consumption patterns and promoting tax acceptance as it is about developing clean energy.",
         "F": "Despite these factors, many social scientists seem reluctant to tackle such problems. And in Europe, some are up in arms over a proposal to drop a specific funding category for social-science research and to integrate it within cross-cutting topics of sustainable development.",
         "G": "During the late 1990s, national spending on social sciences and the humanities as a percentage of all research and development funds—including government, higher education, non-profit and corporate—varied from around 4% to 25%; in most European nations, it is about 15%."
     }, "D"),
    (44, "reading_item", 2.0, "f1619752-4d99-5e3f-99ee-a3214c446001",
     "Choose the best paragraph [A]-[G] that fits into gap (44):",
     {
         "A": "The idea is to force social scientists to integrate their work with other categories, including health and demographic change; food security; marine research and the bio-economy; clean, efficient energy; and inclusive, innovative and secure societies.",
         "B": "The solution is to change the mindset of the academic community, and what it considers to be its main goal. Global challenges and social innovation ought to receive much more attention from scientists, especially the young ones.",
         "C": "It could be that we are evolving two communities of social scientists: one that is discipline-oriented and publishing in highly specialized journals, and one that is problem-oriented and publishing elsewhere, such as policy briefs.",
         "D": "However, the numbers are still small: in 2010, about 1,600 of the 100,000 social-sciences papers published globally included one of these keywords.",
         "E": "These issues all have root causes in human behavior: all require behavioral change and social innovations, as well as technological development. Stemming climate change, for example, is as much about changing consumption patterns and promoting tax acceptance as it is about developing clean energy.",
         "F": "Despite these factors, many social scientists seem reluctant to tackle such problems. And in Europe, some are up in arms over a proposal to drop a specific funding category for social-science research and to integrate it within cross-cutting topics of sustainable development.",
         "G": "During the late 1990s, national spending on social sciences and the humanities as a percentage of all research and development funds—including government, higher education, non-profit and corporate—varied from around 4% to 25%; in most European nations, it is about 15%."
     }, "G"),
    (45, "reading_item", 2.0, "f1619752-4d99-5e3f-99ee-a3214c446001",
     "Choose the best paragraph [A]-[G] that fits into gap (45):",
     {
         "A": "The idea is to force social scientists to integrate their work with other categories, including health and demographic change; food security; marine research and the bio-economy; clean, efficient energy; and inclusive, innovative and secure societies.",
         "B": "The solution is to change the mindset of the academic community, and what it considers to be its main goal. Global challenges and social innovation ought to receive much more attention from scientists, especially the young ones.",
         "C": "It could be that we are evolving two communities of social scientists: one that is discipline-oriented and publishing in highly specialized journals, and one that is problem-oriented and publishing elsewhere, such as policy briefs.",
         "D": "However, the numbers are still small: in 2010, about 1,600 of the 100,000 social-sciences papers published globally included one of these keywords.",
         "E": "These issues all have root causes in human behavior: all require behavioral change and social innovations, as well as technological development. Stemming climate change, for example, is as much about changing consumption patterns and promoting tax acceptance as it is about developing clean energy.",
         "F": "Despite these factors, many social scientists seem reluctant to tackle such problems. And in Europe, some are up in arms over a proposal to drop a specific funding category for social-science research and to integrate it within cross-cutting topics of sustainable development.",
         "G": "During the late 1990s, national spending on social sciences and the humanities as a percentage of all research and development funds—including government, higher education, non-profit and corporate—varied from around 4% to 25%; in most European nations, it is about 15%."
     }, "A")
]

# Ensure Q45 explanation is populated properly
if not pb_expls.get(45):
    pb_expls[45] = """45. 【考点提炼】类似句式结构+上下文逻辑
【空格推测】由空格上文“欧盟改革方案本意并非是要忽视社会科学，而是恰恰相反”推知，空格处很可能进一步明确“改革方案的本意”。
【答案敲定】由选项分析可知，[A]为本题备选项。
[A]指出“其目的是促进社会科学家跨领域协作（The idea is to...）”，能够承接上文具体解释 the intention is ... the complete opposite 所指。另外该改革本意也与空格后句该项改革的积极影响“激发更多协作性努力”表义一致。整段逻辑为“提出观点（①句）——事例论证（随后各句）”，事例论证部分逻辑为“事例介绍（②③④句）——事例评判（其余各句）”。故敲定[A]为本题答案。
[B]虽与本文主旨密切相关，且针对文章所述问题“社会科学对解决全球问题贡献不足”提出解决方案，但与空格上句“欧盟改革的目的不是……，而是恰恰相反”无法顺畅衔接，故排除。"""

# Existing question objects by sort_order
existing_q_map = {q.get("sort_order"): q for q in exam_data.get("questions", [])}

new_questions = []
for (qno, q_type, points, passage_id, stem, opts_dict, correct_ans) in raw_questions_defs:
    ex_q = existing_q_map.get(qno, {})
    qid = ex_q.get("id") or f"2013-ky1-q{qno:02d}"
    
    # Options list format: [{'key': 'A', 'text': '...', 'value': 'A'}, ...]
    options_list = [{"key": k, "text": v, "value": k} for k, v in sorted(opts_dict.items())]
    
    # Explanation
    if qno <= 20:
        expl = cloze_expls.get(qno) or ex_q.get("explanation", "")
    elif qno <= 40:
        expl = reading_expls.get(qno) or ex_q.get("explanation", "")
    else:
        expl = pb_expls.get(qno) or ex_q.get("explanation", "")
    
    q_obj = {
        "id": qid,
        "exam_id": exam_id,
        "passage_id": passage_id,
        "question_number": qno,
        "sort_order": qno,
        "stem": stem,
        "options": options_list,
        "correct_answer": correct_ans,
        "answer": correct_ans,
        "points": points,
        "q_type": q_type,
        "explanation": expl
    }
    new_questions.append(q_obj)

exam_data["questions"] = new_questions

# 5. Write to local JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"Successfully reconstructed 2013 ky1 exam JSON at {json_path}")
print(f"Total passages: {len(exam_data['passages'])}, Total questions: {len(exam_data['questions'])}")
total_pts = sum(q['points'] for q in exam_data['questions'])
print(f"Total points: {total_pts}")
