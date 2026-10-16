import json
import sys
import os
import re

sys.stdout.reconfigure(encoding='utf-8')

exam_file = "public/data/exams/47036de0-e57d-5ccb-9bc8-b3f86d4e6457.json"
with open(exam_file, "r", encoding="utf-8") as f:
    exam_data = json.load(f)

# Load final extracted explanations
expls = json.load(open("scratch_2004_reading_expls_final.json", encoding="utf-8"))

passages_content = {
    # Text 1
    "57971afc-9129-55e9-b22e-fd98fdae267e": (
        "Hunting for a job late last year, lawyer Gant Redmon stumbled across CareerBuilder, "
        "a job database on the Internet. He searched it with no success but was attracted by "
        "the site's \"personal search agent\". It's an interactive feature that lets visitors "
        "key in job criteria such as location, title, and salary, then E-mails them when a "
        "matching position is posted in the database. Redmon chose the keywords legal, intellectual "
        "property, and Washington, D.C. Three weeks later, he got his first notification of an opening. "
        "\"I struck gold,\" says Redmon, who E-mailed his resume to the employer and won a position "
        "as in-house counsel for a company.\n\n"
        "With thousands of career-related sites on the Internet, finding promising openings can be "
        "time-consuming and inefficient. Search agents reduce the need for repeated visits to the "
        "databases. But although a search agent worked for Redmon, career experts see drawbacks. "
        "Narrowing your criteria, for example, may work against you: \"Every time you answer a question "
        "you eliminate a possibility,\" says one expert.\n\n"
        "For any job search, you should start with a narrow concept—what you think you want to do—then "
        "broaden it. \"None of these programs do that,\" says another expert. \"There's no career "
        "counseling implicit in all of this.\" Instead, the best strategy is to use the agent as a kind "
        "of tip service to keep abreast of jobs in a particular database; when you get E-mail, consider "
        "it a reminder to check the database again. \"I would not rely on agents for finding everything "
        "that is added to a database that might interest me,\" says the author of a job-searching guide.\n\n"
        "Some sites design their agents to tempt job hunters to return. When CareerSite's agent offers "
        "each job hunter only three job options through its E-mail service, for example, it includes "
        "only three potential jobs—those it considers the best matches. There may be more matches in "
        "the database; job hunters will have to visit the site again to find them—and they do. \"On the "
        "day after we send our messages, we see a sharp increase in our traffic,\" says Seth Peets, "
        "vice president of marketing for CareerSite.\n\n"
        "Even those who aren't hunting for jobs may find search agents worthwhile. Some use them to "
        "keep a close watch on the demand for their line of work or gather information on compensation "
        "to arm themselves when negotiating for a raise. Although happily employed, Redmon maintains "
        "his agent at CareerBuilder. \"You always keep your eyes open,\" he says. Working with a "
        "personal search agent means having another set of eyes looking out for you."
    ),

    # Text 2
    "70cbad07-a70f-5a06-83ad-7c31b09398b3": (
        "Over the past century, all kinds of unfairness and discrimination have been condemned or "
        "made illegal. But one insidious form continues to thrive: alphabetism. This, for those as "
        "yet unaware of such a disadvantage, refers to discrimination against those whose surnames "
        "begin with a letter in the lower half of the alphabet.\n\n"
        "It has long been known that a taxi firm called AAAA cars has a big advantage over Zodiac "
        "cars when customers thumb through their phone directories. Less well known is the advantage "
        "that Adam Abbott has in life over Zoe Zysman. English names are fairly evenly spread between "
        "the halves of the alphabet. Yet a suspiciously large number of top people have surnames "
        "beginning with letters between A and G.\n\n"
        "Thus the American president and vice-president have surnames starting with B and C "
        "respectively, and 26 of George Bush's predecessors (including his father) had surnames "
        "in the first half of the alphabet against just 16 in the second half. Even more striking, "
        "six of the seven heads of government of the G7 rich countries are alphabetically advantaged "
        "(Berlusconi, Blair, Bush, Chirac, Chrétien and Koizumi). The world's three top central "
        "bankers (Greenspan, Duisenberg and Hayami) are all close to the top of the alphabet, even "
        "if one of them really uses Japanese characters. As are the world's five richest men "
        "(Gates, Buffett, Allen, Ellison and Albrecht).\n\n"
        "Can this merely be coincidence? One theory, dreamt up in all the spare time enjoyed by "
        "the alphabetically disadvantaged, is that the rot sets in early. At the start of the first "
        "year in infant school, teachers seat pupils alphabetically from the front, to make it easier "
        "to remember their names. So short-sighted Zysman junior gets stuck in the back row, and is "
        "rarely asked the improving questions posed by those insensitive teachers. At the time the "
        "alphabetically disadvantaged may think they have had a lucky escape. Yet the result may be "
        "worse qualifications, because they get less individual attention, as well as less confidence "
        "in speaking publicly.\n\n"
        "The humiliation continues. At university graduation ceremonies, the ABCs proudly get their "
        "awards first; by the time they reach the Zysmans most people are literally having a ZZZ. "
        "Shortlists for job interviews, election ballot papers, lists of conference speakers and "
        "attendees: all tend to be drawn up alphabetically, and their recipients lose interest as "
        "they plough through them."
    ),

    # Text 3
    "543ff84f-2399-5fe5-acfe-8388547fb57d": (
        "When it comes to the slowing economy, Ellen Spero isn't biting her nails just yet—but she "
        "isn't polishing as many nails as she'd like to, either. Most of her clients spend $12 to "
        "$50 weekly, but last month two longtime customers suddenly stopped showing up. Spero blames "
        "the softening economy. \"I'm a good economic indicator,\" she says. \"I provide a service "
        "that people wouldn't mind doing without when they're concerned about saving some dollars.\" "
        "So Spero is downscaling, shopping at middle-brow Dillard's department store near her "
        "suburban Cleveland home, instead of Neiman Marcus. \"I don't know if other clients are "
        "going to abandon me, too,\" she says.\n\n"
        "Even before Alan Greenspan's admission that America's red-hot economy is cooling, lots of "
        "working folks had already seen signs of the slowdown themselves. From car dealerships to "
        "Gap outlets, sales have been lagging for months as shoppers temper their spending. For "
        "retailers, who last year had to turn away customers for lack of supply of products as varied "
        "as faux fur and Playstation 2 consoles, the cautious approach is coming at a crucial time. "
        "Already, serious truss manufacturers and other industrial suppliers are beginning to cut back. "
        "But don't sound any alarms just yet. Consumers seem only mildly concerned, not panicked, and "
        "many say they remain optimistic about America's long-term prospects, even as they do some "
        "modest belt-tightening.\n\n"
        "Consumers say they're not in despair because, despite the dreadful headlines, their own "
        "fortunes still feel pretty good. Home prices are holding steady in most regions. In Manhattan, "
        "\"there's a new gold rush happening in the $4 million to $10 million range, predominantly "
        "fed by Wall Street bonuses,\" says broker Barbara Corcoran. In San Francisco, prices are "
        "still rising even as frenzied overbidding quiets. \"Instead of 20 to 30 offers, now maybe you "
        "only get two or three,\" says one local broker. And most folks still feel pretty comfortable "
        "about their ability to find and keep a job.\n\n"
        "Many folks see silver linings to this slowdown. Potential home buyers would cheer for lower "
        "interest rates. Employers wouldn't mind a little fewer bubbles in the job market. Many "
        "consumers seem to have been influenced by stock-market swings, which investors now view as "
        "a necessary ingredient to a sustained boom. Diners might see an upside, too. Getting a table "
        "at Manhattan's hot new Alain Ducasse restaurant used to be impossible. Not anymore. For that, "
        "Greenspan & Co. may still be worth toasting."
    ),

    # Text 4
    "b1a7c543-3c20-5f0a-8efa-ee954df1c075": (
        "Americans today don't place a very high value on intellect. Our heroes are athletes, "
        "entertainers, and entrepreneurs, not scholars. Even our schools are where we send our "
        "children to get a practical education—not to pursue knowledge for the sake of knowledge. "
        "Symptoms of pervasive anti-intellectualism in our schools aren't difficult to find.\n\n"
        "\"We have a tradition in America that practical is more important than intellectual,\" says "
        "education writer Diane Ravitch. \"Schools could be a counterbalance.\" Ravitch's latest book, "
        "Left Back: A Century of Failed School Reforms, traces the roots of anti-intellectualism in "
        "our schools, concluding they are anything but a counterbalance to the American distaste for "
        "intellectual pursuits.\n\n"
        "But they could and should be. Encouraging kids to reject the life of the mind leaves them "
        "vulnerable to exploitation and control. Without the ability to think critically, to defend "
        "their ideas and understand the ideas of others, they cannot fully participate in our "
        "democracy. Continuing along this path, says writer Earl Shorris, \"We will become a "
        "second-rate country. We will have a less civil society.\"\n\n"
        "\"Historically, America's schools have tended to reflect other values of American culture,\" "
        "says historian and professor Richard Hofstadter in Anti-Intellectualism in American Life, "
        "a Pulitzer-Prize winning book on the roots of anti-intellectualism in US politics, religion, "
        "and education. From the beginning of our history, says Hofstadter, our democratic and "
        "populist urges have driven us to reject anything that smells of elitism. Practicality, common "
        "sense, and native intelligence have been considered more noble qualities than anything you "
        "could learn from a book.\n\n"
        "Ralph Waldo Emerson and other Transcendentalist philosophers thought schooling and rigorous "
        "book learning put unnatural restraints on children: \"We are shut up in schools and college "
        "recitation rooms for 10 or 15 years and come out at last with a bellyful of words and do "
        "not know a thing.\" Mark Twain's The Adventures of Huckleberry Finn exemplified American "
        "anti-intellectualism. Its hero avoids being civilized—going to school and learning to "
        "read—so he can preserve his innate goodness.\n\n"
        "Intellect, according to Hofstadter, is different from native intelligence, a quality we "
        "reluctantly admire. Intellect is the critical, creative, and contemplative side of the "
        "mind. Intelligence seeks to grasp, manipulate, re-order, and adjust, while intellect "
        "examines, ponders, wonders, theorizes, criticizes and imagines.\n\n"
        "School remains a place where intellect is mistrusted. Hofstadter says our country's "
        "educational system is in the grip of people who \"joyfully and militantly proclaim their "
        "hostility to intellect and their eagerness to identify with children who show the least "
        "intellectual promise.\""
    )
}

# Questions mapping
questions_data = {
    21: {
        "stem": "How did Redmon find his job?",
        "options": [
            {"key": "A", "value": "A", "text": "By searching openings in a job database."},
            {"key": "B", "value": "B", "text": "By posting a matching position in a database."},
            {"key": "C", "value": "C", "text": "By using a special service of a database."},
            {"key": "D", "value": "D", "text": "By E-mailing his resume to a database."}
        ],
        "answer": "C"
    },
    22: {
        "stem": "Which of the following can be a disadvantage of search agents?",
        "options": [
            {"key": "A", "value": "A", "text": "Lack of counseling."},
            {"key": "B", "value": "B", "text": "Limited number of visits."},
            {"key": "C", "value": "C", "text": "Lower efficiency."},
            {"key": "D", "value": "D", "text": "Fewer successful matches."}
        ],
        "answer": "A"
    },
    23: {
        "stem": "The expression \"tip service\" (Line 4, Paragraph 3) most probably means",
        "options": [
            {"key": "A", "value": "A", "text": "advisory."},
            {"key": "B", "value": "B", "text": "compensation."},
            {"key": "C", "value": "C", "text": "interaction."},
            {"key": "D", "value": "D", "text": "reminder."}
        ],
        "answer": "D"
    },
    24: {
        "stem": "Why does CareerSite's agent offer each job hunter only three job options?",
        "options": [
            {"key": "A", "value": "A", "text": "To focus on better job matches."},
            {"key": "B", "value": "B", "text": "To attract more returning visits."},
            {"key": "C", "value": "C", "text": "To reserve space for more messages."},
            {"key": "D", "value": "D", "text": "To increase the rate of success."}
        ],
        "answer": "B"
    },
    25: {
        "stem": "Which of the following is true according to the text?",
        "options": [
            {"key": "A", "value": "A", "text": "Personal search agents are indispensable to job-hunters."},
            {"key": "B", "value": "B", "text": "Some sites keep E-mailing job seekers to trace their demands."},
            {"key": "C", "value": "C", "text": "Personal search agents are also helpful to those already employed."},
            {"key": "D", "value": "D", "text": "Some agents stop sending information to people once they are employed."}
        ],
        "answer": "C"
    },
    26: {
        "stem": "What does the author intend to illustrate with AAAA cars and Zodiac cars?",
        "options": [
            {"key": "A", "value": "A", "text": "A kind of overlooked inequality."},
            {"key": "B", "value": "B", "text": "A type of conspicuous bias."},
            {"key": "C", "value": "C", "text": "A type of personal prejudice."},
            {"key": "D", "value": "D", "text": "A kind of brand discrimination."}
        ],
        "answer": "A"
    },
    27: {
        "stem": "What can we infer from the first three paragraphs?",
        "options": [
            {"key": "A", "value": "A", "text": "In both East and West, names are essential to success."},
            {"key": "B", "value": "B", "text": "The alphabet is to blame for the failure of Zoe Zysman."},
            {"key": "C", "value": "C", "text": "Customers often pay a lot of attention to companies' names."},
            {"key": "D", "value": "D", "text": "Some form of discrimination is too subtle to recognize."}
        ],
        "answer": "D"
    },
    28: {
        "stem": "The 4th paragraph suggests that",
        "options": [
            {"key": "A", "value": "A", "text": "questions are often put to the more intelligent students."},
            {"key": "B", "value": "B", "text": "alphabetically disadvantaged students often escape from class."},
            {"key": "C", "value": "C", "text": "teachers should pay attention to all of their students."},
            {"key": "D", "value": "D", "text": "students should be seated according to their eyesight."}
        ],
        "answer": "C"
    },
    29: {
        "stem": "What does the author mean by \"most people are literally having a ZZZ\" (Lines 2-3, Paragraph 5)?",
        "options": [
            {"key": "A", "value": "A", "text": "They are getting impatient."},
            {"key": "B", "value": "B", "text": "They are noisily dozing off."},
            {"key": "C", "value": "C", "text": "They are feeling humiliated."},
            {"key": "D", "value": "D", "text": "They are busy with word puzzles."}
        ],
        "answer": "B"
    },
    30: {
        "stem": "Which of the following is true according to the text?",
        "options": [
            {"key": "A", "value": "A", "text": "People with surnames beginning with N to Z are often ill-treated."},
            {"key": "B", "value": "B", "text": "VIPs in the Western world gain a great deal from alphabetism."},
            {"key": "C", "value": "C", "text": "The campaign to eliminate alphabetism still has a long way to go."},
            {"key": "D", "value": "D", "text": "Putting things alphabetically may lead to unintentional bias."}
        ],
        "answer": "D"
    },
    31: {
        "stem": "By \"Ellen Spero isn't biting her nails just yet\" (Line 1, Paragraph 1), the author means",
        "options": [
            {"key": "A", "value": "A", "text": "Spero can hardly maintain her business."},
            {"key": "B", "value": "B", "text": "Spero is too much engaged in her work."},
            {"key": "C", "value": "C", "text": "Spero has grown out of her bad habit."},
            {"key": "D", "value": "D", "text": "Spero is not in a desperate situation."}
        ],
        "answer": "D"
    },
    32: {
        "stem": "How do the public feel about the current economic situation?",
        "options": [
            {"key": "A", "value": "A", "text": "Optimistic."},
            {"key": "B", "value": "B", "text": "Confused."},
            {"key": "C", "value": "C", "text": "Carefree."},
            {"key": "D", "value": "D", "text": "Panicked."}
        ],
        "answer": "A"
    },
    33: {
        "stem": "When mentioning \"the $4 million to $10 million range\" (Line 3, Paragraph 3), the author is talking about",
        "options": [
            {"key": "A", "value": "A", "text": "gold market."},
            {"key": "B", "value": "B", "text": "real estate."},
            {"key": "C", "value": "C", "text": "stock exchange."},
            {"key": "D", "value": "D", "text": "venture investment."}
        ],
        "answer": "B"
    },
    34: {
        "stem": "Why can many people see \"silver linings\" to the economic slowdown?",
        "options": [
            {"key": "A", "value": "A", "text": "They would benefit in certain ways."},
            {"key": "B", "value": "B", "text": "The stock market shows signs of recovery."},
            {"key": "C", "value": "C", "text": "Such a slowdown usually precedes a boom."},
            {"key": "D", "value": "D", "text": "The purchasing power would be enhanced."}
        ],
        "answer": "A"
    },
    35: {
        "stem": "To which of the following is the author likely to agree?",
        "options": [
            {"key": "A", "value": "A", "text": "A new boom, on the horizon."},
            {"key": "B", "value": "B", "text": "Tighten the belt, the single remedy."},
            {"key": "C", "value": "C", "text": "Caution all right, panic not."},
            {"key": "D", "value": "D", "text": "The more ventures, the more chances."}
        ],
        "answer": "C"
    },
    36: {
        "stem": "What do American parents expect their children to acquire in school?",
        "options": [
            {"key": "A", "value": "A", "text": "The habit of thinking independently."},
            {"key": "B", "value": "B", "text": "Profound knowledge of the world."},
            {"key": "C", "value": "C", "text": "Practical abilities for future career."},
            {"key": "D", "value": "D", "text": "The confidence in intellectual pursuits."}
        ],
        "answer": "C"
    },
    37: {
        "stem": "We can learn from the text that Americans have a history of",
        "options": [
            {"key": "A", "value": "A", "text": "undervaluing intellect."},
            {"key": "B", "value": "B", "text": "favoring intellectualism."},
            {"key": "C", "value": "C", "text": "supporting school reform."},
            {"key": "D", "value": "D", "text": "suppressing native intelligence."}
        ],
        "answer": "A"
    },
    38: {
        "stem": "The views of Ravitch and Emerson on schooling are",
        "options": [
            {"key": "A", "value": "A", "text": "identical."},
            {"key": "B", "value": "B", "text": "similar."},
            {"key": "C", "value": "C", "text": "complementary."},
            {"key": "D", "value": "D", "text": "opposite."}
        ],
        "answer": "D"
    },
    39: {
        "stem": "Emerson, according to the text, is probably",
        "options": [
            {"key": "A", "value": "A", "text": "a pioneer of education reform."},
            {"key": "B", "value": "B", "text": "an opponent of intellectualism."},
            {"key": "C", "value": "C", "text": "a scholar in favor of intellect."},
            {"key": "D", "value": "D", "text": "an advocate of regular schooling."}
        ],
        "answer": "B"
    },
    40: {
        "stem": "What does the author think of intellect?",
        "options": [
            {"key": "A", "value": "A", "text": "It is second to intelligence."},
            {"key": "B", "value": "B", "text": "It evolves from common sense."},
            {"key": "C", "value": "C", "text": "It is to be pursued."},
            {"key": "D", "value": "D", "text": "It underlies power."}
        ],
        "answer": "C"
    }
}

# Update Passages in exam_data
for p in exam_data.get("passages", []):
    p_id = p.get("id")
    if p_id in passages_content:
        p["content"] = passages_content[p_id]
        print(f"Updated passage {p_id}: new length={len(p['content'])}")

# Update Questions in exam_data
for q in exam_data.get("questions", []):
    sort_order = q.get("sort_order")
    if sort_order in questions_data:
        meta = questions_data[sort_order]
        q["stem"] = meta["stem"]
        q["options"] = meta["options"]
        q["correct_answer"] = meta["answer"]
        q["answer"] = meta["answer"]
        q["points"] = 2
        q["q_type"] = "reading_item"
        # Explanation
        if str(sort_order) in expls:
            q["explanation"] = expls[str(sort_order)]
        print(f"Updated Q{sort_order}: stem='{q['stem'][:40]}...', ans={q['answer']}, expl_len={len(q['explanation'])}")

# Save updated JSON
with open(exam_file, "w", encoding="utf-8") as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"Successfully saved {exam_file}!")

# Update version.json
version_file = "public/data/version.json"
if os.path.exists(version_file):
    vdata = json.load(open(version_file, encoding="utf-8"))
    import datetime
    now_str = datetime.datetime.now(datetime.timezone.utc).isoformat()
    vdata["lastUpdated"] = now_str
    # bump revision
    cur_rev = int(vdata.get("revision", 1))
    vdata["revision"] = cur_rev + 1
    with open(version_file, "w", encoding="utf-8") as f:
        json.dump(vdata, f, ensure_ascii=False, indent=2)
    print(f"Updated {version_file} to revision {vdata['revision']} at {now_str}")
