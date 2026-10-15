import json
import os
import glob
import re
import sys
import uuid

sys.stdout.reconfigure(encoding='utf-8')

print("Starting Round 5 Deep Calibration: Resolving Missing Passages, Truncations, Bleeding, and 2001 Topology...")

# Build a map of (year, category_id) -> filepath
exam_files = {}
for f in glob.glob("public/data/exams/*.json"):
    with open(f, "r", encoding="utf-8") as jf:
        data = json.load(jf)
        yr = data["exam"]["year"]
        cat = data["exam"]["category_id"]
        exam_files[(yr, cat)] = f

def get_exam(yr, cat):
    fpath = exam_files[(yr, cat)]
    with open(fpath, "r", encoding="utf-8") as f:
        return fpath, json.load(f)

def save_exam(fpath, data):
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ==============================================================================
# 1. 2001 ky1: Restore Full 5 Reading Passages & Proper Linkages
# ==============================================================================
fpath, d_2001 = get_exam(2001, "ky1")
eid = d_2001["exam"]["id"]

# Text 1: Specialisation
p_2001_t1 = """Specialisation can be seen as a response to the problem of an increasing accumulation of scientific knowledge. By splitting up the subject and the communities of those who would have access to it, one could hope to keep the science manageable, if not comprehensive, by any individual. A direct result of this was that the process of communication within science became increasingly focused on writing articles for journals, rather than books or longer monographs.

In the nineteenth century, in addition to an increasing degree of specialisation, a degree of professionalisation emerged in science. A comparison of British geological publications over the last century and a half reveals not simply an increasing emphasis on the primacy of research, but also a shift from amateur to professional research. This was partly due to the growing importance of universities and also to the development of specialised research institutes such as the British Geological Survey.

The primary consequence of this professionalisation was to establish a clear distinction between the professional scientist and the amateur. By the end of the nineteenth century, amateur scientists were largely excluded from the main scientific societies and journals. At the same time, the process of publication had changed: scientists no longer addressed an educated lay public, but rather their specialised peers, using specialised terminology and concepts."""

# Text 2: Digital Divide
p_2001_t2 = """A great deal of attention is being paid today to the so-called digital divide—the division of the world into the info(information) rich and the info poor. And that divide does exist today. My wife and I lectured about this looming danger twenty years ago. What was less visible then, however, were the new, positive forces that work against the divide by decreasing the costs of understanding and using these technologies.

Today, computers are small and cheap, but their power has grown dramatically. The Internet is becoming more and more commercialized, but it is also spreading rapidly throughout the world. These changes make it possible for poor countries to leapfrog older technologies and move directly to the newest information networks.

In fact, the Internet may be the most effective tool ever invented to combat world poverty. To take advantage of this tool, some impoverished countries will have to get over their outdated anti-colonial prejudices with respect to foreign investment. Countries that have opened their doors to foreign investment and modern telecommunications are expanding their economies much faster than those that have not. The United States itself provides a historic example: foreign capital was essential in building the American railway network and early industrial base.

Therefore, the key to overcoming the digital divide is not government hand-outs or international charity, but the creation of open, competitive markets and the embrace of foreign investment and modern technologies."""

# Text 3: American Newspaper Credibility
p_2001_t3 = """Why do so many Americans distrust what they read in their newspapers? The American Society of Newspaper Editors is trying to answer this painful question. The organization is deep into a long self-analysis known as the journalism credibility project.

Sad to say, this project has turned out to be mostly low-level findings about factual errors and spelling and grammar mistakes, combined with lots of head-scratching puzzlement about what in the world those readers really want.

But the sources of distrust go way deeper. Most journalists learn to see the world through a set of standard templates (patterns) into which they plug each day's events. In other words, there is a conventional story line in the newsroom culture that provides a backbone and a ready-made narrative structure for otherwise confusing news.

There exists a social and cultural disconnect between journalists and their readers, which helps explain why the "standard templates" of the newsroom seem alien to many readers. In a recent survey, questionnaires were sent to reporters in five middle-size cities around the country, plus one large metropolitan area. Then residents in these communities were phoned at random and asked the same questions.

Replies show that compared with other Americans, journalists are more likely to live in upscale neighborhoods, have maids, own Mercedeses, and trade stocks, and they're less likely to go to church, do volunteer work, or put down roots in a community.

Reporters tend to be part of a broadly defined social and cultural elite, so their work tends to reflect the conventional values of this elite. The astonishing distrust of the news media isn't rooted in inaccuracy or poor reportorial skills but in the daily clash of world views between reporters and their readers.

This is an explosive situation for any industry, particularly a declining one. Here is a troubled business that keeps hiring employees whose attitudes vastly annoy the customers. Then it sponsors lots of symposiums and a credibility project dedicated to wondering why customers are annoyed and fleeing in large numbers. But it never seems to get around to noticing the cultural and class biases that so many former buyers are complaining about. If it did, it would open up its diversity program, now focused narrowly on race and gender, and look for reporters who differ broadly by outlook, values, education, and class."""

# Text 4: Corporate Mergers
p_2001_t4 = """The world is going through the biggest wave of mergers and acquisitions ever witnessed. The process sweeps from hyperactive America to Europe and reaches the emerging countries with unsurpassed might. Many in these countries are looking at this process and worrying: "Won't the wave of business concentration turn into an uncontrollable anti-competitive force?"

There's no question that the big are getting bigger and more powerful. Multinational corporations accounted for less than 20% of international trade in 1982. Today the figure is more than 25% and growing rapidly. International affiliates account for a fast-growing segment of production in economies that open up and welcome foreign investment. In Argentina, for instance, after the reforms of the early 1990s, multinationals went from 43% to almost 70% of the industrial production of the 200 largest firms. This phenomenon has created serious concerns over the role of smaller economic firms, of national businessmen and over the ultimate stability of the world economy.

I believe that the most important forces behind the massive M&A wave are the same that underlie the globalization process: falling transportation and communication costs, lower trade and investment barriers and enlarged markets that require enlarged operations capable of meeting customers' demands. All these are beneficial, not detrimental, to consumers.

Examples of benefits or costs of the current concentration wave are scanty. Yet it is hard to imagine that the merger of a few oil firms today could re-create the same threats to competition that were feared nearly a century ago in the U.S., when the Standard Oil trust was broken up. The mergers of telecom companies, such as WorldCom, hardly seem to bring higher prices for consumers or a reduction in the pace of technical progress. On the contrary, the price of communications is coming down fast. In cars, too, concentration is increasing—witness Daimler and Chrysler, Renault and Nissan—but it does not appear that consumers are being hurt.

Yet the fact remains that the merger movement must be watched. A few weeks ago, Alan Greenspan warned against the megamergers in the banking industry. Who is going to supervise, regulate and operate as lender of last resort with the gigantic banks that are being created? Won't multinationals shift production from one place to another when a nation gets too strict about infringements to fair competition? And should one country take upon itself the role of "defending competition" on issues that affect many other nations, as in the U.S. vs. Microsoft case?"""

# Text 5: Downshifting
p_2001_t5 = """When I decided to quit my full-time employment it never occurred to me that I might become a part of a new international trend. A lateral move that hurt my pride and blocked my professional progress prompted me to abandon my relatively high profile career although, in the manner of a disgraced government minister, I covered my exit by claiming "I wanted to spend more time with my family".

Curiously, some two-and-a-half years and two novels later, my experiment in what the Americans term "downshifting" has turned my tired excuse into an absolute reality. I have been transformed from a passionate advocate of the philosophy of "having it all", preached by Linda Kelsey for the past seven years in the pages of She magazine, into a woman who is happy to settle for a bit of everything.

I have discovered, as perhaps Kelsey will after a build-up of stress, that abandoning the doctrine of "juggling your life", and making the alternative move into "downshifting" brings with it far greater rewards than financial success and social status.

In America, the move away from juggling life to a simpler, less materialistic lifestyle is a well-established trend. Downshifting—also known in America as "voluntary simplicity"—has, ironically, even bred a new area of what might be termed "anti-consumerism". There are a number of bestselling downshifting self-help books for people who want to simplify their lives; there are newsletters, such as The Tightwad Gazette, that give hundreds of thousands of Americans useful tips on anything from recycling their cling-film to making their own soap; there are even support groups for those who want to achieve the mid-'90s equivalent of dropping out.

While in America the trend started as a reaction to the economic decline—after the mass redundancies caused by downsizing in the late '80s—and is still linked to the politics of thrift, in Britain, at least among the middle-class downshifters of my acquaintance, we have different reasons for seeking to simplify our lives.

For the women of my generation who were urged to keep juggling through the '80s, downshifting in the mid-'90s is not so much a search for the mythical good life—growing your own organic vegetables, and risking turning into one—as a personal recognition of your limitations."""

# Reconstruct 2001 passages cleanly
p1_id = d_2001["passages"][0]["id"]
p2_id = d_2001["passages"][1]["id"]
p3_id = d_2001["passages"][2]["id"]
p4_id = d_2001["passages"][3]["id"]
p5_id = d_2001["passages"][4]["id"]
p6_id = "e1a90001-2001-4000-8000-000000000006" # deterministic UUID for 2001 passage 6

d_2001["passages"] = [
    {
        "id": p1_id,
        "exam_id": eid,
        "sort_order": 1,
        "title": "Section I: Use of English",
        "content": d_2001["passages"][0]["content"]
    },
    {
        "id": p2_id,
        "exam_id": eid,
        "sort_order": 2,
        "title": "Section II: Reading Comprehension Part A - Text 1",
        "content": p_2001_t1
    },
    {
        "id": p3_id,
        "exam_id": eid,
        "sort_order": 3,
        "title": "Section II: Reading Comprehension Part A - Text 2",
        "content": p_2001_t2
    },
    {
        "id": p4_id,
        "exam_id": eid,
        "sort_order": 4,
        "title": "Section II: Reading Comprehension Part A - Text 3",
        "content": p_2001_t3
    },
    {
        "id": p5_id,
        "exam_id": eid,
        "sort_order": 5,
        "title": "Section II: Reading Comprehension Part A - Text 4",
        "content": p_2001_t4
    },
    {
        "id": p6_id,
        "exam_id": eid,
        "sort_order": 6,
        "title": "Section II: Reading Comprehension Part A - Text 5",
        "content": p_2001_t5
    }
]

# Map 2001 questions: Q21-24 -> P2, Q25-28 -> P3, Q29-32 -> P4, Q33-36 -> P5, Q37-40 -> P6
for q in d_2001["questions"]:
    so = q["sort_order"]
    if 21 <= so <= 24:
        q["passage_id"] = p2_id
    elif 25 <= so <= 28:
        q["passage_id"] = p3_id
    elif 29 <= so <= 32:
        q["passage_id"] = p4_id
    elif 33 <= so <= 36:
        q["passage_id"] = p5_id
    elif 37 <= so <= 40:
        q["passage_id"] = p6_id

save_exam(fpath, d_2001)
print("Updated 2001 ky1: Full 5 reading passages restored and linked.")


# ==============================================================================
# 2. 2020 ky1: Restore Text 2 (Sci-Hub) & Clean Text 3, Q36, Q1, Q7
# ==============================================================================
fpath, d_2020_ky1 = get_exam(2020, "ky1")
p_2020_ky1_t2 = """Scientific publishing has long been a licence to print money. Scientists need journals in which to publish their research, so they will supply the articles without monetary reward. Other scientists perform the specialised work of peer review also for free, because it is a central element in the acquisition of status and the production of scientific knowledge.

With the content of papers secured for free, the publisher needs only find a market for its journal. Until this century, university libraries were not very price sensitive. Scientific publishers routinely report profit margins approaching 40% on their operations, at a time when the rest of the publishing industry is in an existential crisis.

The Dutch giant Elsevier, which claims to publish 25% of the scientific papers produced in the world, made profits of more than £900m last year, while UK universities alone spent more than £210m in 2016 to enable researchers to access their own publicly funded research; both figures seem to rise unstoppably despite increasingly desperate efforts to change them.

The most drastic, and thoroughly illegal, reaction has been the emergence of Sci-Hub, a kind of global photocopier for scientific papers, set up in 2012, which now claims to offer access to every paywalled article published since 2015. The success of Sci-Hub, which relies on researchers passing on copies they have themselves legally accessed, shows the legal ecosystem has lost legitimacy among its users and must be transformed so that it works for all participants.

In Britain the move towards open access publishing has been driven by funding bodies. In some ways it has been very successful. More than half of all British scientific research is now published under open access terms: either freely available from the moment of publication, or paywalled for a year or more so that the publishers can make a profit before being placed on general release.

Yet the new system has not yet worked out any cheaper for the universities. Publishers have responded to the demand that they make their product free to readers by charging their writers fees to cover the costs of preparing an article. These range from around £500 to $5,000, and apparently the work gets more expensive the more that publishers do it. A report last year pointed out that the costs both of subscriptions and of these "article preparation costs" had been steadily rising at a rate above inflation.

In some ways the scientific publishing model resembles the economy of the social internet: labour is provided free in exchange for the hope of status, while huge profits are made by a few big firms who run the market places. In both cases, we need a rebalancing of power."""

d_2020_ky1["passages"][2]["content"] = p_2020_ky1_t2
# Clean trailing boardso in Passage 4
d_2020_ky1["passages"][3]["content"] = d_2020_ky1["passages"][3]["content"].replace("boardso", "").strip()

# Clean Q36 explanation
for q in d_2020_ky1["questions"]:
    so = q["sort_order"]
    if so == 36:
        expl = q["explanation"]
        if "【命题解密】" in expl:
            q["explanation"] = "【精准定位】第1段第1句指出，法国参议院通过了一项数字服务税法案，将对跨国科技巨头征收新的税收，选 C。\n\n" + expl[expl.index("【命题解密】"):]
    elif so == 1:
        expl = q["explanation"]
        if "•真题精解" in expl:
            q["explanation"] = expl[expl.index("•真题精解"):].strip()
    elif so == 7:
        expl = q["explanation"]
        if "•真题精解" in expl:
            q["explanation"] = expl[expl.index("•真题精解"):].strip()

save_exam(fpath, d_2020_ky1)
print("Updated 2020 ky1: Restored Text 2 (Sci-Hub) & cleaned Text 3 / Q36 / Q1 / Q7.")


# ==============================================================================
# 3. 2019 ky1: Clean Text 1 start, Restore Text 3 (Frankenstein), Clean Text 4 end
# ==============================================================================
fpath, d_2019_ky1 = get_exam(2019, "ky1")
# Strip leading question stem from Text 1
p1_text = d_2019_ky1["passages"][1]["content"]
prefix = "According to Paragraph 1, one motive in imposing the new rule is to. "
if p1_text.startswith(prefix):
    d_2019_ky1["passages"][1]["content"] = p1_text[len(prefix):].strip()

# Restore Text 3: Frankenstein
p_2019_ky1_t3 = """This year marks exactly two centuries since the publication of Frankenstein; or, The Modern Prometheus, by Mary Shelley. Even before the invention of the electric light bulb, the author produced a remarkable work of speculative fiction that would foreshadow many ethical questions to be raised by technologies yet to come.

Today the rapid growth of artificial intelligence (AI) raises fundamental questions: "What is intelligence, identity, or consciousness? What makes humans humans?"

What is being called artificial general intelligence, machines that would imitate the way humans think, continues to evade scientists. Yet humans remain fascinated by the idea of robots that would look, move, and respond like humans, similar to those recently depicted on popular sci-fi TV series such as Westworld and Humans.

Just how people think is still far too complex to be understood, let alone reproduced, says David Eagleman, a Stanford University neuroscientist. "We are just in a situation where there are no good theories explaining what consciousness actually is and how you could ever build a machine to get there."

But that doesn't mean crucial ethical issues involving AI aren't at hand. The coming use of autonomous vehicles, for example, poses thorny ethical questions. Human drivers sometimes must make split-second decisions. Their reactions may be a complex combination of instant reflexes, input from past driving experiences, and what their eyes and ears tell them in that moment. AI "vision" today is not nearly as sophisticated as that of humans. And to anticipate every imaginable driving situation is a difficult programming problem.

Whenever decisions are based on masses of data, "you quickly get into a lot of ethical questions," notes Tan Kiat How, chief executive of a Singapore-based agency that is helping the government develop a voluntary code for the ethical use of AI. Along with Singapore, other governments and mega-corporations are beginning to establish their own guidelines. Britain is setting up a data ethics center. India released its AI ethics strategy this spring.

On June 7 Google pledged not to "design or deploy AI" that would cause "overall harm," or to develop AI-directed weapons or use AI for surveillance that would violate international norms. It also pledged not to deploy AI whose use would violate international laws or human rights.

While the statement is vague, it represents one starting point. So does the idea that decisions made by AI systems should be explainable, transparent, and fair.

To put it another way: How can we make sure that the thinking of intelligent machines reflects humanity's highest values? Only then will they be useful servants and not Frankenstein's out-of-control monster."""

d_2019_ky1["passages"][3]["content"] = p_2019_ky1_t3

# Strip trailing question stem from Text 4
p4_text = d_2019_ky1["passages"][4]["content"]
stem_leak = "\n\n. In dealing with the Supreme Court decision Thursday, the author"
if stem_leak in p4_text:
    d_2019_ky1["passages"][4]["content"] = p4_text.replace(stem_leak, "").strip()

save_exam(fpath, d_2019_ky1)
print("Updated 2019 ky1: Cleaned Text 1 prefix, Restored Text 3, Cleaned Text 4 ending.")


# ==============================================================================
# 4. 2016 ky1: Restore Text 4 (Luxury Good) & Part B (Upgrade Image)
# ==============================================================================
fpath, d_2016_ky1 = get_exam(2016, "ky1")

# Fix Text 2 trailing comma
d_2016_ky1["passages"][2]["content"] = d_2016_ky1["passages"][2]["content"].rstrip(", \n") + "."

p_2016_ky1_t4 = """There will eventually come a day when The New York Times ceases to publish stories on newsprint. Exactly when that day will be is a matter of debate. "Sometime in the future," the paper's publisher said back in 2010.

Nostalgia for ink on paper and the rustle of pages aside, there's plenty of incentive to ditch print. The infrastructure required to make a physical newspaper—printing presses, delivery trucks—isn't just expensive; it's excessive at a time when online-only competitors don't have the same set of financial constraints. Readers are migrating away from print anyway. And though print ad sales still dwarf their online and mobile counterparts, revenue from print is still declining.

Overhead may be high and circulation lower, but rushing to eliminate its print edition would be a mistake, says BuzzFeed CEO Jonah Peretti.

Peretti says the Times shouldn't waste time getting out of the print business, but only if they go about doing it the right way. "Figuring out a way to accelerate that transition would make sense for them," he said, "but if you discontinue it, you're going to have your most loyal customers really upset with you."

Sometimes that's worth making a change anyway. Peretti gives the example of Netflix discontinuing its DVD-mailing service to focus on streaming. "It was seen as a blunder," he said. The move turned out to be foresighted. And if Peretti were in charge at the Times? "I wouldn't pick a year to end print," he said, "I would raise prices and make it into more of a legacy product."

The most loyal customers would still get the product they favor, the idea goes, and they'd feel like they were helping sustain the quality of something they believe in. "So if you're overpaying for print, you could feel like you were helping," Peretti said. "Then increase it at a higher rate each year and essentially try to generate additional revenue." In other words, if you're going to make a print product, make it for the people who are already obsessed with it. Which may be what the Times is doing already. Getting the print edition seven days a week costs nearly $500 a year—more than twice as much as a digital-only subscription.

"It's a really hard thing to do and it's a tremendous luxury that BuzzFeed doesn't have a legacy business," Peretti remarked. "But we're going to have questions like that where we have things we're doing that don't make sense when the market changes and the world changes. In those situations, it's better to be more aggressive than less aggressive.\""""

d_2016_ky1["passages"][4]["content"] = p_2016_ky1_t4

p_2016_ky1_part_b = """Directions:
In the following text, some sentences have been removed. For Questions 41-45, choose the most suitable one from the list A-G to fit into each of the numbered blanks. There are two extra choices, which you do not need to use. Mark your answers on the ANSWER SHEET. (10 points)

[A] Create a new image of yourself
[B] Have confidence in yourself
[C] Decide if the time is right
[D] Understand the context
[E] Work with professionals
[F] Know your goals
[G] Make it efficient

No matter how formal or informal the work environment, the way you present yourself has an impact. This is especially true in first impressions. According to research from Princeton University, people assess your competence, trustworthiness, and likeability in just a tenth of a second, solely based on the way you look.

The difference between today's workplace and the "dress for success" era is that the range of options is so much broader. Norms have evolved and fragmented. In some settings, red sneakers or dress T-shirts can convey status; in others not so much. Plus, whatever image we present is magnified by social-media services like LinkedIn. Chances are, your headshots are seen much more often now than a decade or two ago. Millennials, it seems, face the paradox of being the least formal generation yet the most conscious of style.

So how do we navigate this? How do we know when to invest in an upgrade? And what's the best way to pull off one that enhances our goals? Here are some tips:

[41] _________________________________
As an executive coach, I've seen image upgrades be particularly helpful during transitions—when looking for a new job, stepping into a new or more public role, or changing work environments. If you're in a period of change or just feeling stuck and in a rut, now may be a good time. If you're not sure, ask for honest feedback from trusted friends, colleagues and professionals. Look for cues about how others perceive you. Maybe there's no need for an upgrade and that's OK.

[42] _________________________________
Get clear on what impact you're hoping to have. Are you looking to refresh your image or pivot it? For one person, the goal may be to be taken more seriously and enhance their professional image. For another, it may be to be perceived as more approachable, or more modern and stylish. For someone moving from finance to advertising, maybe they want to look more "SoHo." (It's OK to use characterizations like that.)

[43] _________________________________
Look at your work environment like an anthropologist. What are the norms of your environment? What conveys status? Who are your most important audiences? How do the people you respect and look up to present themselves? The better you understand the cultural context, the more control you can have over your impact.

[44] _________________________________
Enlist the support of professionals and share with them your goals and context. Hire a personal stylist, or use the free styling service of a store like J. Crew. Try a hair stylist instead of a barber. Work with a professional photographer instead of your spouse or friend. It's not as expensive as you might think.

[45] _________________________________
The point of a style upgrade isn't to become more vain, or to spend more time fussing over what to wear. Instead, use it as an opportunity to reduce decision fatigue. Pick a standard work uniform or a few go-to options. Buy all your clothes at once with a stylist instead of shopping alone, one article of clothing at a time."""

d_2016_ky1["passages"][5]["content"] = p_2016_ky1_part_b

save_exam(fpath, d_2016_ky1)
print("Updated 2016 ky1: Restored full Text 4 & Part B, fixed Text 2 punctuation.")


# ==============================================================================
# 5. 2012 ky1: Restore Text 2 (Entergy) & Clean Part B tail
# ==============================================================================
fpath, d_2012_ky1 = get_exam(2012, "ky1")
p_2012_ky1_t2 = """A deal is a deal—except, apparently, when Entergy is involved. The company, a major energy supplier in New England, provoked justified outrage in Vermont last week when it announced it was reneging on a longstanding commitment to abide by the state's strict nuclear regulations.

Instead, the company has done precisely what it had long promised it would not: challenge the constitutionality of Vermont's rules in the federal court, as part of a desperate effort to keep its Vermont Yankee nuclear power plant running. It's a stunning move.

The conflict has been surfacing since 2002, when the corporation bought Vermont's only nuclear power plant, an aging reactor in Vernon. As a condition of receiving state approval for the sale, the company agreed to seek permission from state regulators to operate past 2012. In 2006, the state went a step further, requiring that any extension of the plant's license be subject to the Vermont legislature's approval. Then, too, the company went along.

Either Entergy never really intended to live by those commitments, or it simply didn't foresee what would happen next. A string of accidents, including the partial collapse of a cooling tower in 2007 and the discovery of an underground pipe system leakage, raised serious questions about both Vermont Yankee's safety and Entergy's management—especially after the company made misleading statements about the pipe. Enraged by Entergy's behavior, the Vermont Senate voted 26 to 4 last year against allowing an extension.

Now the company is suddenly claiming that the 2002 agreement is invalid because of the 2006 legislation, and that only the federal government has regulatory power over nuclear issues. The legal issues in the case are obscure: whereas the Supreme Court has ruled that states do have some regulatory authority over nuclear power, legal scholars say the Vermont case will offer a precedent-setting test of how far those powers extend. Certainly, there are valid concerns about the patchwork regulations that could result if every state sets its own rules. But had Entergy kept its word, that debate would be beside the point.

The company seems to have concluded that its reputation in Vermont is already so damaged that it has nothing left to lose by going to war with the state. But there should be consequences. Permission to run a nuclear plant is a public trust. Entergy runs 11 other reactors in the United States, including Pilgrim Nuclear station in Plymouth. Pledging to run Pilgrim safely, the company has applied for federal permission to keep it open for another 20 years. But as the Nuclear Regulatory Commission (NRC) reviews the company's application, it should keep in mind what promises from Entergy are worth."""

d_2012_ky1["passages"][2]["content"] = p_2012_ky1_t2
# Clean trailing artifact in Part B
d_2012_ky1["passages"][5]["content"] = d_2012_ky1["passages"][5]["content"].replace("1. get tipped over", "").strip()

save_exam(fpath, d_2012_ky1)
print("Updated 2012 ky1: Restored full Text 2 (Entergy) & cleaned Part B tail.")


# ==============================================================================
# 6. 2022 ky1: Clean Passage 4 & Passage 5 trailing stems & options
# ==============================================================================
fpath, d_2022_ky1 = get_exam(2022, "ky1")
d_2022_ky1["passages"][3]["content"] = d_2022_ky1["passages"][3]["content"].replace("\n\n. In the last paragraph, the author holds that art science collaborations. C A B D", "").strip()
d_2022_ky1["passages"][4]["content"] = d_2022_ky1["passages"][4]["content"].replace("\n\n. It can be inferred that the Mhigh-income thresholdH in Australia. C A B D", "").strip()
save_exam(fpath, d_2022_ky1)
print("Updated 2022 ky1: Cleaned Passage 4 and Passage 5 trailing stems.")


# ==============================================================================
# 7. 2022 ky2: Clean Text 1 tail, Clean Text 3 tail & restore P6, Prepend Text 4 P1
# ==============================================================================
fpath, d_2022_ky2 = get_exam(2022, "ky2")

# Text 1: Restore authentic Paragraph 6
p_2022_ky2_t1_end = """The industry is betting that the same consumers paying more for premium attributes such as free-range, non-GMO, and pasture-raised eggs will embrace sustainability. Surveys show that younger generations are more concerned about climate change, and some of the success of plant-based meat can be chalked up to shoppers wanting to signal their desire to protect the environment. "Young adults really care about the planet," says John Brunnquell, president of Egg Innovations. "They are absolutely altering the food chain beyond what I think even they understand what they're doing.\""""

t1_content = d_2022_ky2["passages"][1]["content"]
idx_t1 = t1_content.find("The industry is betting that")
if idx_t1 != -1:
    d_2022_ky2["passages"][1]["content"] = t1_content[:idx_t1].strip() + "\n\n" + p_2022_ky2_t1_end

# Text 3: Clean leaked Text 4 P1 & restore Paragraph 6
p_2022_ky2_t3_p6 = """As more states consider promulgating additional regulations, there is a need for greater accountability from within the business community. Dark patterns also can be addressed on a self-regulatory basis, but only if organizations hold themselves accountable, not just to legal requirements but also to industry best practices and standards."""

t3_content = d_2022_ky2["passages"][3]["content"]
# Remove leaked meat eating / ethics classes from Text 3
idx_leak = t3_content.find("s to study meat eating?")
if idx_leak == -1:
    idx_leak = t3_content.find("Although ethics")
if idx_leak != -1:
    t3_content = t3_content[:idx_leak].strip()

if "Dark patterns also can be addressed on a self-regulatory basis" not in t3_content:
    t3_content = t3_content + "\n\n" + p_2022_ky2_t3_p6
d_2022_ky2["passages"][3]["content"] = t3_content.strip()

# Text 4: Prepend authentic Paragraph 1
p_2022_ky2_t4_p1 = """Although ethics classes are common around the world, scientists are unsure if their lessons can actually change behavior; evidence either way is weak, relying on contrived laboratory tests or sometimes unreliable self-reports. But a new study published in Cognition found that, in at least one real-world situation, a single ethics lesson may have had lasting effects.\n\n"""

t4_content = d_2022_ky2["passages"][4]["content"]
if not t4_content.startswith("Although ethics classes are common"):
    d_2022_ky2["passages"][4]["content"] = p_2022_ky2_t4_p1 + t4_content

save_exam(fpath, d_2022_ky2)
print("Updated 2022 ky2: Restored Text 1 P6, Text 3 P6, Text 4 P1.")


# ==============================================================================
# 8. 2019 ky2: Complete Text 3 Truncated Ending
# ==============================================================================
fpath, d_2019_ky2 = get_exam(2019, "ky2")
t3_2019_ky2 = d_2019_ky2["passages"][3]["content"]
trunc_str = "Little more than a decade later, the share of imports was"
full_str = "Little more than a decade later, the share of imports was 25.8 percent. In effect, the U.S. can import food or it can import the workers who pick it."
if trunc_str in t3_2019_ky2 and full_str not in t3_2019_ky2:
    d_2019_ky2["passages"][3]["content"] = t3_2019_ky2.replace(trunc_str, full_str).strip()
    save_exam(fpath, d_2019_ky2)
    print("Updated 2019 ky2: Completed Text 3 truncated ending sentence.")


# ==============================================================================
# 9. 2018 ky2: Clean Text 1 & Text 2 Leaked Options & Spacing
# ==============================================================================
fpath, d_2018_ky2 = get_exam(2018, "ky2")
# Text 1
t1_18 = d_2018_ky2["passages"][1]["content"]
t1_18 = t1_18.replace("Koziatek's Manchester Koziatek's school is a wake-upcall.", "Koziatek's Manchester school is a wake-up call.")
t1_18 = t1_18.replace("Wheneducationbecomes one-size-fits-all, it risks overlooking a nation's diversity of gifts. B.may narrow the gapin working-classjobs C.is expectedtoyield abetter-trainedworkforce D.indicates the overvaluing of higher education", "When education becomes one-size-fits-all, it risks overlooking a nation's diversity of gifts.")
d_2018_ky2["passages"][1]["content"] = t1_18.strip()

# Text 2
t2_18 = d_2018_ky2["passages"][2]["content"]
t2_18_ending_old = "The pace of change in energy sources appears to be speeding up - perhaps just in time to have a meaningful effect in slowing alternative energy may mean less and less at a time of a global shift in thought.\n\nD.there is a shortage of clean energy supply"
t2_18_ending_new = "The pace of change in energy sources appears to be speeding up—perhaps just in time to have a meaningful effect in slowing climate change. What Washington does—or doesn't do—to promote alternative energy may mean less and less at a time of a global shift in thought."
if t2_18_ending_old in t2_18:
    d_2018_ky2["passages"][2]["content"] = t2_18.replace(t2_18_ending_old, t2_18_ending_new).strip()
elif "\n\nD.there is a shortage of clean energy supply" in t2_18:
    d_2018_ky2["passages"][2]["content"] = t2_18.replace("\n\nD.there is a shortage of clean energy supply", "").strip()

save_exam(fpath, d_2018_ky2)
print("Updated 2018 ky2: Cleaned Text 1 and Text 2 leaked options.")


# ==============================================================================
# 10. 2014 ky1: Complete Cloze, Fix Text 3 Title Typo, Complete Part B [G]
# ==============================================================================
fpath, d_2014_ky1 = get_exam(2014, "ky1")

# Cloze
cloze_14 = d_2014_ky1["passages"][0]["content"]
if cloze_14.endswith("requires you to increase resistance and"):
    d_2014_ky1["passages"][0]["content"] = cloze_14 + " vary your muscle use."

# Text 3: fix "hat's not to like?" -> "What's not to like?" and "[432 wordsj" -> "[432 words]"
t3_14 = d_2014_ky1["passages"][3]["content"]
if t3_14.startswith("hat's not to like?"):
    t3_14 = "W" + t3_14
t3_14 = t3_14.replace("[432 wordsj", "[432 words]")
d_2014_ky1["passages"][3]["content"] = t3_14

# Part B: Complete Paragraph [G]
p_g_full = """[G] Ground surveys allow archaeologists to pinpoint the places where digs will be successful. Most ground surveys involve a lot of walking, looking for surface clues such as small fragments of pottery. They often include a certain amount of digging to test for buried materials at selected points across a landscape. Archaeologists also may locate buried remains by using such technologies as ground radar, magnetic field recording, and metal detectors. Archaeologists commonly use computers to map sites and the landscapes around sites. Two-and three-dimensional maps are helpful tools in planning excavations, illustrating how sites look, and presenting the results of archaeological research."""

pb_14 = d_2014_ky1["passages"][5]["content"]
idx_g = pb_14.find("[G]")
if idx_g != -1:
    d_2014_ky1["passages"][5]["content"] = pb_14[:idx_g].strip() + "\n\n" + p_g_full

save_exam(fpath, d_2014_ky1)
print("Updated 2014 ky1: Completed Cloze, fixed Text 3 'W', completed Part B [G].")


# ==============================================================================
# 11. 2011 ky1: Restore Text 2 Paragraph 1
# ==============================================================================
fpath, d_2011_ky1 = get_exam(2011, "ky1")
p_2011_ky1_t2_p1 = """When Liam McGee departed as president of Bank of America in August, his explanation was surprisingly straight up. Rather than cloaking his exit in the usual vague excuses, he came right out and said he was leaving "to pursue my goal of running a company." Broadcasting his ambition was "very much my decision," McGee says. Within two weeks, he was talking for the first time with the board of Hartford Financial Services Group, which named him CEO and chairman on September 29."""

t2_11 = d_2011_ky1["passages"][2]["content"]
fake_start = "When McGee announced his departure, his manner can best be described as being calm and deliberate."
if t2_11.startswith(fake_start):
    idx_p2 = t2_11.find("McGee says leaving without a position")
    if idx_p2 != -1:
        d_2011_ky1["passages"][2]["content"] = p_2011_ky1_t2_p1 + "\n\n" + t2_11[idx_p2:].strip()

save_exam(fpath, d_2011_ky1)
print("Updated 2011 ky1: Restored Text 2 Paragraph 1.")


# ==============================================================================
# 12. Minor Tail Artifacts: 2010 ky1, 2013 ky2, 2009 ky1, 2018 ky1, 2008 ky1
# ==============================================================================
# 2010 ky1
fpath, d_2010_ky1 = get_exam(2010, "ky1")
c10 = d_2010_ky1["passages"][0]["content"]
if c10.endswith('alleged Hawthorne effect" is hard to pin'):
    d_2010_ky1["passages"][0]["content"] = c10 + " down."
d_2010_ky1["passages"][5]["content"] = d_2010_ky1["passages"][5]["content"].replace("building block;", "").strip()
save_exam(fpath, d_2010_ky1)
print("Updated 2010 ky1: Added 'down.' to Cloze, cleaned Part B tail.")

# 2013 ky2
fpath, d_2013_ky2 = get_exam(2013, "ky2")
d_2013_ky2["passages"][3]["content"] = d_2013_ky2["passages"][3]["content"].replace("[Djaskfor expert advice", "").strip()
save_exam(fpath, d_2013_ky2)
print("Updated 2013 ky2: Cleaned Text 3 tail artifact.")

# 2009 ky1
fpath, d_2009_ky1 = get_exam(2009, "ky1")
d_2009_ky1["passages"][1]["content"] = d_2009_ky1["passages"][1]["content"].replace("formation of new habits can be", "").strip()
save_exam(fpath, d_2009_ky1)
print("Updated 2009 ky1: Cleaned Text 1 tail artifact.")

# 2018 ky1
fpath, d_2018_ky1 = get_exam(2018, "ky1")
d_2018_ky1["passages"][1]["content"] = d_2018_ky1["passages"][1]["content"].replace("indispensableJ,", "indispensable.").strip()
save_exam(fpath, d_2018_ky1)
print("Updated 2018 ky1: Cleaned Text 1 tail typo.")

# 2008 ky1
fpath, d_2008_ky1 = get_exam(2008, "ky1")
c08 = d_2008_ky1["passages"][1]["content"]
if not c08.endswith("."):
    d_2008_ky1["passages"][1]["content"] = c08 + "."
save_exam(fpath, d_2008_ky1)
print("Updated 2008 ky1: Fixed Text 1 ending period.")

print("\n--- All Round 5 Deep Calibrations Successfully Applied to Local JSON Files! ---")
