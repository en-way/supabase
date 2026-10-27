import json
import uuid

exam_file = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\f303f3fb-abfe-477f-a2e5-8dcd1ba78ef0.json'

with open(exam_file, 'r', encoding='utf-8') as f:
    orig = json.load(f)

# Exam metadata
exam = orig['exam']
exam['title'] = '2024年全国硕士研究生招生考试英语（一）真题'
exam['year'] = 2024
exam['category_id'] = 'ky1'
exam['total_score'] = 60.0
exam['pass_score'] = 36.0
exam['duration_minutes'] = 180
exam['approval_status'] = 'approved'
exam['is_published'] = True

# Passage IDs
p_ids = [p['id'] for p in orig['passages']]
assert len(p_ids) == 6

# Passages pure gold text
cloze_text = """There's nothing more welcoming than a door opening for you. [1] _______ the need to be touched to open or close, automatic doors are essential in [2] _______ disabled access to buildings and helping provide general [3] _______ to commercial buildings. Self-sliding doors began to emerge as a commercial product in 1960 after being invented six years [4] _______ by two Americans, Dee Horton and Lew Hewitt. They [5] _______ as a novelty feature on restaurants and hotels in the 1960s and 1970s, before becoming increasingly popular in supermarkets and shopping centers, bringing general [6] _______ to societies within our technologically advanced world.

Particularly [7] _______ in busy locations like airports, train stations and other transport hubs with intense flows of traffic, automatic doors [8] _______ crowd management in these high-volume settings, aiding the orderly movement of people and preventing bottlenecks, whilst ensuring that emergency exits are not put in people's way.

[9] _______ making access both in and out of buildings easier for people, the difference in the way many of these doors open helps reduce the total area [10] _______ by them. Automatic doors often open to the side, with the panels sliding across one another. Replacing swing doors, these [11] _______ smaller buildings to maximise the usable space inside without having to [12] _______ the way for a large, sticking-out door.

There are many different types of automatic door, with each [13] _______ specific signals to tell them when to open. [14] _______ these methods differ, the main [15] _______ remain the same. Each automatic door system [16] _______ the light, sound, weight or movement in their vicinity as a signal to open. Sensor types are chosen to [17] _______ the different environments they are needed in. [18] _______, a busy street might not [19] _______ a motion-sensored door, as it would constantly be opening for passers-by. A pressure-sensitive mat would be more [20] _______ to limit the surveyed area."""

text1_text = """Nearly 2,000 years ago, as the Romans began to pull out of Scotland, they left behind a curious treasure: 10 tons of nails, nearly a million of the things. The nail hoard was discovered in 1960 in a four-metre-deep pit covered by two metres of gravel.

Why had the Romans buried a million nails? The likely explanation is that the withdrawal was rushed, and they didn't want the local Caledonians getting their hands on 10 tons of weapon-grade iron. The Romans buried the nails so deep that they would not be discovered for almost two millennia.

Later civilisations would value the skilled blacksmith's labour in a nail even more than the raw material. As Roma Agrawal explains in her new delightful book Nuts and Bolts, early 17th-century Virginians would sometimes burn down their homes if they were planning to relocate. This was an attempt to recover the valuable nails which could be reused after sifting the ashes. The idea that one might burn down an entire house just to reclaim the nails underlines how scarce, costly and valuable the simple-seeming technology was.

The price of nails fell by 90% between the late 1700s and mid-1900s, as economist Daniel Sichel points out in a research paper. According to Sichel, although the falling price of nails was driven partly by cheaper iron and cheaper energy, most of the credit goes to nail manufacturers who simply found more efficient ways to turn steel into nails.

Nails themselves have changed over the years, but Sichel studied them because they haven't changed much. Roman lamps and Roman chariots are very different from LED strips and sports cars, but Roman nails are still clearly nails. It would be absurd to try to track the changing price of sports cars since 1695, but to ask the same question of nails makes perfect sense.

I make no apology for being obsessed by a particular feature of everyday objects: their price. I am an economist, after all. After writing two books about the history of inventions, one thing I've learnt is that while it is the enchantingly sophisticated technologies that get all the hype, it's the cheap technologies that change the world.

The Gutenberg printing press transformed civilisation not by changing the nature of writing but by changing its cost - and it would have achieved little without a parallel collapse in the price of surfaces to write on, thanks to an often-overlooked technology called paper. Solar panels had a few niche uses until they became cheap; now they are transforming the global energy system."""

text2_text = """Parenting tips obtained from hunter-gatherers in Africa may be the key to bringing up more contented children, researchers have suggested. The idea is based on studies of communities such as the Kung of Botswana, where each child is cared for by many adults. Kung children as young as four will help to look after younger ones and "baby-wearing", in which infants are carried in slings, is considered the norm.

According to Dr Nikhil Chaudhary, an evolutionary anthropologist at Cambridge University, these practices, known as alloparenting, could lead to less anxiety for children and parents.

Dr Annie Swanepoel, a child psychiatrist, believes that there are ways to incorporate them into western life. In Germany, one scheme has paired an old people's home with a nursery. The residents help to look after the children, an arrangement akin to alloparenting. Another measure could be encouraging friendships between children in different school years to mirror the unsupervised mixed-age playgroups in hunter-gatherer communities.

In a paper published in the Journal of Child Psychology and Psychiatry, researchers said that the western nuclear family was a recent invention which broke with evolutionary history. This abrupt shift to an "intensive mothering narrative", which suggests that mothers should manage childcare alone, was likely to have been harmful. "Such narratives can lead to maternal exhaustion and have dangerous consequences," they wrote.

By contrast, in hunter-gatherer societies adults other than the parents can provide almost half of a child's care. One previous study looked at the Efé people of the Democratic Republic of Congo. It found that infants had an average of 14 alloparents a day by the time they were 18 weeks old and were passed between caregivers eight times an hour.

Chaudhary said that parents now had less childcare support from family and social networks than during most of humans' evolutionary history, but introducing additional caregivers could reduce stress and maternal depression, which could have a "knock-on" benefit to a child's wellbeing. An infant born to a hunter-gatherer society could have more than ten caregivers - this contrasts starkly to nursery settings in the UK where regulations call for a ratio of one carer to four children aged two to three.

While hunter-gatherer children learnt from observation and imitation in mixed-age playgroups, researchers said that western "instructive teaching" where pupils are asked to sit still, may contribute to conditions such as attention deficit hyperactivity disorder. Chaudhary said that Britain should explore the possibility that older siblings helping their parents "might also enhance their own social development"."""

text3_text = """A Polish digital artist who uses classical painting styles to create dreamy fantasy landscapes, Greg Rutkowski has made illustrations for games such as Dungeons & Dragons and Magic: The Gathering. And he's become a sudden hit in the new world of text-to-image AI generation.

His distinctive style is now one of the most commonly used prompts in the new open-source AI art generator Stable Diffusion. The tool, along with other popular image-generation AI models, allows anyone to create impressive images based on text prompts. For example, type in "Wizard with sword and a glowing orb of magic fire fights a fierce dragon Greg Rutkowski," and the system will produce something that looks not a million miles away from works in Rutkowski's style.

But these open-source programs are built by scraping images from the internet, often without permission and proper attribution to artists. As a result, they are raising tricky questions about ethics and copyright. And artists like Rutkowski have had enough.

According to the website Lexica, which tracks over 10 million Stable Diffusion images and prompts, Rutkowski's name has been used as a prompt around 93,000 times. Rutkowski was initially surprised but thought it might be a good way to reach new audiences. Then he tried searching for his name to see if a piece he had worked on had been published. The online search brought back work that had his name attached to it but wasn't his.

"It's been just a month. What about in a year? I probably won't be able to find my work out there because the internet will be flooded with AI art," Rutkowski said. "That's concerning."

Other artists besides Rutkowski have been surprised by the apparent popularity of their work in text-to-image generators — and some are now fighting back.

Karla Ortiz, an illustrator based in San Francisco who found her work in Stable Diffusion's data set, has been raising awareness about the issues around AI art and copyright. Artists say they risk losing income as people start using AI-generated images based on copyrighted material for commercial purposes. But it's also a lot more personal, Ortiz says, arguing that because art is so closely linked to a person, it could raise data protection and privacy problems.

"There is a coalition growing within artist industries to figure out how to tackle or mitigate this," says Ortiz. The group is in its early days of mobilization, which could involve pushing for new policies or regulation. One suggestion is that AI models could be trained on images in the public domain, and AI companies could forge partnerships with museums and artists, Ortiz says."""

text4_text = """The miracle of the Chesapeake Bay lies not in its depths, but in the complexity of its natural construction, the interaction of fresh and saline waters, and the mix of land and water. The shallows provide homes for hundreds of species while storing floodwaters, filtering pollutants from water, and protecting nearby communities from potentially destructive storm surges.

All this was put at great risk late last month, when the U.S. Supreme Court issued a ruling in an Idaho case that provides the U.S. Environmental Protection Agency (EPA) far less authority to regulate wetlands and waterways. Specifically, a 5-4 majority decided that wetlands protected by the EPA under its Clean Water Act authority must have a "continuous surface connection" to bodies of water. This narrowing of the regulatory scope was a victory for builders, mining operators and other commercial interests often at odds with environmental rules. And it carries "significant repercussions for water quality and flood control throughout the United States," as Justice Brett Kavanaugh observed.

In Maryland, the good news is that there are many state laws in place that provide wetlands protections. But that's a very shortsighted view, particularly when it comes to the Chesapeake Bay. The reality is that water, and the pollutants that so often come with it, don't respect state boundaries. The Chesapeake draws from a 64,000-square-mile watershed that extends into Virginia, Pennsylvania, New York, West Virginia, the District of Columbia and Delaware. Will those jurisdictions extend the same protections now denied under Sackett v. EPA? Perhaps some, but all? That seems unlikely.

It is too easy, and misleading, to see such court rulings as merely standing up for the rights of land owners when the consequences can be so dire for their neighbors. And it's a reminder that the EPA's involvement in the Chesapeake Bay Program has long been crucial as the means to transcend the influence of deep-pocketed special interests in neighboring states. Pennsylvania farmers, to use one telling example, aren't thinking about next year's blue crab harvest in Maryland when they decide whether to spread animal waste on their fields, yet the runoff into nearby creeks can have enormous impact downstream.

And so we would call on state lawmakers from Richmond to Albany to consider reviewing their own wetlands protections and see for themselves the enormous stakes involved. We can offer them a visit to Blackwater National Wildlife Refuge in Dorchester County where bald eagles fly over tidal marshes so shallow you could not paddle a boat across them but teeming with aquatic life. It's worth the scenic drive."""

partb_text = """Hannah: Simply, there are people in Nigeria who cannot travel to the Smithsonian Institution to see that part of their history and culture represented by the Benin Bronzes. These should be available to them as part of their cultural heritage and history and as a source of national pride. There is no good reason that these artifacts should be beyond the ordinary reach of the educational objectives or inspiration of the generations to which they were left. They serve no purpose in a museum in the United States or elsewhere except as curious objects. They cannot be compared to works of art produced for sale which can be passed from hand to hand and place to place by purchase.

Buck: We know very exact reproductions of artwork can be and are regularly produced. Perhaps museums and governments might explore some role for the use of nearly exact reproductions as a means of resolving issues relating to returning works of art and antiquities. The context of any exhibit is more important to me than whether the object being displayed is 2,000 years old or 2 months old. In many cases the experts have a hard time agreeing on what is the real object and what is a forgery. Again, the story an exhibit is trying to tell is what matters. The monetary value of the objects on display is a distant second place in importance.

Sara: When visiting the Baltimore Museum of Art, I came across a magnificent 15th-century Chinese sculpture. It inspired me to learn more about the culture that it represented. Artifacts in museums have the power to inspire, and perhaps spark that need to learn and understand the nature of their creators. Having said that, I do feel that whatever artifacts find their way to public museums should, in fact, be sanctioned as having been obtained on loan, legally purchased, or obtained by treaty. Stealing artifacts from other peoples' cultures is obscene; it robs not only the physical objects, but the dignity and spirit of their creators.

Victor: Ancient art that is displayed in foreign countries by all means should be returned to the original country. The foreign countries have no right to hold back returning the items. I would ask that the foreign nations and the original country discuss the terms of transfer. Yes, there is the risk that the original country will not have as good security as do the foreign countries. But look at what happened to Boston's Gardner Museum theft in 1990, including the loss of Rembrandt, Vermeer, Manet, and other masterpieces. Nothing is absolutely safe, nowhere. And now Climate Change agitators are attacking publicly displayed works in European museums.

Julia: To those of you in the comments section who are having strong feelings about artifacts being removed from cities in the US and Britain and returned to their countries of origin, I would ask you to consider: why do you think Americans have more of a right to easily access the Benin Bronzes than the people of Nigeria? Why are people who live within a day's drive of London entitled to go and see the Elgin Marbles whenever they want, but the people of Athens aren't? What intrinsic factors make the West a suitable home for these artifacts but preclude them from being preserved and displayed by their countries of origin? If your conclusion is that the West is better able to preserve these artifacts, think about why you're assuming that to be true."""

passages_data = [
    {
        "id": p_ids[0],
        "exam_id": exam["id"],
        "category_id": "ky1",
        "section_type": "cloze",
        "title": "Section I: Use of English",
        "content": cloze_text,
        "sort_order": 1,
        "passage_type": "cloze"
    },
    {
        "id": p_ids[1],
        "exam_id": exam["id"],
        "category_id": "ky1",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part A - Text 1",
        "content": text1_text,
        "sort_order": 2,
        "passage_type": "reading"
    },
    {
        "id": p_ids[2],
        "exam_id": exam["id"],
        "category_id": "ky1",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part A - Text 2",
        "content": text2_text,
        "sort_order": 3,
        "passage_type": "reading"
    },
    {
        "id": p_ids[3],
        "exam_id": exam["id"],
        "category_id": "ky1",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part A - Text 3",
        "content": text3_text,
        "sort_order": 4,
        "passage_type": "reading"
    },
    {
        "id": p_ids[4],
        "exam_id": exam["id"],
        "category_id": "ky1",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part A - Text 4",
        "content": text4_text,
        "sort_order": 5,
        "passage_type": "reading"
    },
    {
        "id": p_ids[5],
        "exam_id": exam["id"],
        "category_id": "ky1",
        "section_type": "reading",
        "title": "Section II: Reading Comprehension Part B",
        "content": partb_text,
        "sort_order": 6,
        "passage_type": "reading"
    }
]

# Standardize Questions 1 to 45
q_defs = {
    # Cloze 1-20
    1: {"passage": 0, "stem": "Select the correct option to fill in the blank [1]:", "ans": "D", "opts": [("A", "Through"), ("B", "Despite"), ("C", "Besides"), ("D", "Without")]},
    2: {"passage": 0, "stem": "Select the correct option to fill in the blank [2]:", "ans": "C", "opts": [("A", "revealing"), ("B", "demanding"), ("C", "improving"), ("D", "tracing")]},
    3: {"passage": 0, "stem": "Select the correct option to fill in the blank [3]:", "ans": "B", "opts": [("A", "experience"), ("B", "convenience"), ("C", "guidance"), ("D", "reference")]},
    4: {"passage": 0, "stem": "Select the correct option to fill in the blank [4]:", "ans": "A", "opts": [("A", "previously"), ("B", "temporarily"), ("C", "successively"), ("D", "eventually")]},
    5: {"passage": 0, "stem": "Select the correct option to fill in the blank [5]:", "ans": "B", "opts": [("A", "held on"), ("B", "started out"), ("C", "settled down"), ("D", "went by")]},
    6: {"passage": 0, "stem": "Select the correct option to fill in the blank [6]:", "ans": "C", "opts": [("A", "threats"), ("B", "concerns"), ("C", "benefits"), ("D", "origins")]},
    7: {"passage": 0, "stem": "Select the correct option to fill in the blank [7]:", "ans": "A", "opts": [("A", "useful"), ("B", "flexible"), ("C", "stable"), ("D", "common")]},
    8: {"passage": 0, "stem": "Select the correct option to fill in the blank [8]:", "ans": "D", "opts": [("A", "call for"), ("B", "yield to"), ("C", "look into"), ("D", "act as")]},
    9: {"passage": 0, "stem": "Select the correct option to fill in the blank [9]:", "ans": "A", "opts": [("A", "As well as"), ("B", "In terms of"), ("C", "In addition to"), ("D", "In place of")]},
    10: {"passage": 0, "stem": "Select the correct option to fill in the blank [10]:", "ans": "D", "opts": [("A", "connected"), ("B", "shared"), ("C", "defended"), ("D", "occupied")]},
    11: {"passage": 0, "stem": "Select the correct option to fill in the blank [11]:", "ans": "A", "opts": [("A", "allow"), ("B", "expect"), ("C", "require"), ("D", "direct")]},
    12: {"passage": 0, "stem": "Select the correct option to fill in the blank [12]:", "ans": "C", "opts": [("A", "adopt"), ("B", "lead"), ("C", "clear"), ("D", "change")]},
    13: {"passage": 0, "stem": "Select the correct option to fill in the blank [13]:", "ans": "C", "opts": [("A", "adapting to"), ("B", "deriving from"), ("C", "relying on"), ("D", "pointing at")]},
    14: {"passage": 0, "stem": "Select the correct option to fill in the blank [14]:", "ans": "D", "opts": [("A", "Once"), ("B", "Since"), ("C", "Unless"), ("D", "Although")]},
    15: {"passage": 0, "stem": "Select the correct option to fill in the blank [15]:", "ans": "C", "opts": [("A", "positions"), ("B", "restrictions"), ("C", "principles"), ("D", "categories")]},
    16: {"passage": 0, "stem": "Select the correct option to fill in the blank [16]:", "ans": "B", "opts": [("A", "controls"), ("B", "analyses"), ("C", "predicts"), ("D", "produces")]},
    17: {"passage": 0, "stem": "Select the correct option to fill in the blank [17]:", "ans": "D", "opts": [("A", "decorate"), ("B", "ignore"), ("C", "establish"), ("D", "match")]},
    18: {"passage": 0, "stem": "Select the correct option to fill in the blank [18]:", "ans": "C", "opts": [("A", "In contrast"), ("B", "By comparison"), ("C", "For example"), ("D", "Above all")]},
    19: {"passage": 0, "stem": "Select the correct option to fill in the blank [19]:", "ans": "B", "opts": [("A", "assess"), ("B", "suit"), ("C", "protect"), ("D", "identify")]},
    20: {"passage": 0, "stem": "Select the correct option to fill in the blank [20]:", "ans": "A", "opts": [("A", "appropriate"), ("B", "sensitive"), ("C", "accessible"), ("D", "accurate")]},

    # Text 1 (21-25)
    21: {"passage": 1, "stem": "The Romans buried the nails probably for the sake of", "ans": "D", "opts": [("A", "saving them for future use"), ("B", "keeping them from rusting"), ("C", "letting them grow in value"), ("D", "hiding them from the locals")]},
    22: {"passage": 1, "stem": "The example of early 17th-century Virginians is used to", "ans": "D", "opts": [("A", "highlight the thriftiness of early American colonists"), ("B", "illustrate the high status of blacksmiths in that period"), ("C", "contrast the attitudes of different civilisations towards nails"), ("D", "show the preciousness of nail-making technology at that time")]},
    23: {"passage": 1, "stem": "What played the major role in lowering the price of nails after the late 1700s?", "ans": "A", "opts": [("A", "Increased productivity."), ("B", "Wider use of new energies."), ("C", "Fiercer market competition."), ("D", "Reduced cost of raw materials.")]},
    24: {"passage": 1, "stem": "It can be learned from Paragraph 5 that nails", "ans": "B", "opts": [("A", "have undergone many technological improvements"), ("B", "have remained basically the same since Roman times"), ("C", "are less studied than other everyday products"), ("D", "are one of the world's most significant inventions")]},
    25: {"passage": 1, "stem": "Which of the following best summarises the last two paragraphs?", "ans": "A", "opts": [("A", "Cheap technologies bring about revolutionary change."), ("B", "Technological innovation is integral to economic success."), ("C", "Technology defines people's understanding of the world."), ("D", "Sophisticated technologies develop from small inventions.")]},

    # Text 2 (26-30)
    26: {"passage": 2, "stem": "According to the first two paragraphs, alloparenting refers to the practice of", "ans": "A", "opts": [("A", "sharing childcare among community members"), ("B", "assigning babies to specific adult caregivers"), ("C", "teaching parenting skills to older children"), ("D", "carrying infants around by their parents")]},
    27: {"passage": 2, "stem": "The scheme in Germany is mentioned to illustrate", "ans": "B", "opts": [("A", "an attempt to facilitate intergenerational communication"), ("B", "an approach to integrating alloparenting into western society"), ("C", "the conventional parenting style in western culture"), ("D", "the differences between western and African ways of living")]},
    28: {"passage": 2, "stem": "According to Paragraph 4, the \"intensive mothering narrative\"", "ans": "D", "opts": [("A", "alleviates parenting pressures"), ("B", "consolidates family relationships"), ("C", "results in the child-centred family"), ("D", "departs from the course of evolution")]},
    29: {"passage": 2, "stem": "What can be inferred about the nurseries in the UK?", "ans": "C", "opts": [("A", "They tend to fall short of official requirements."), ("B", "They have difficulty finding enough caregivers."), ("C", "They ought to improve their carer-to-child ratio."), ("D", "They should try to prevent parental depression.")]},
    30: {"passage": 2, "stem": "Which of the following would be the best title for the text?", "ans": "B", "opts": [("A", "Instructive teaching: a dilemma for anxious parents"), ("B", "For a happier family, learn from the hunter-gatherers"), ("C", "Mixed-age playgroup, a better choice for lonely children"), ("D", "Tracing the history of parenting: from Africa to Europe")]},

    # Text 3 (31-35)
    31: {"passage": 3, "stem": "What can be learned about Rutkowski from the first two paragraphs?", "ans": "B", "opts": [("A", "He is enthusiastic about using AI models."), ("B", "He is popular with users of an AI art generator."), ("C", "He attracts admiration from other illustrators."), ("D", "He specializes in classical painting digitalization.")]},
    32: {"passage": 3, "stem": "The problem with open-source AI art generators is that they", "ans": "C", "opts": [("A", "lack flexibility in responding to prompts"), ("B", "produce artworks in unpredictable styles"), ("C", "make unauthorized use of online images"), ("D", "collect user information without consent")]},
    33: {"passage": 3, "stem": "After searching online, Rutkowski found", "ans": "C", "opts": [("A", "a unique way to reach audiences"), ("B", "a new method to identify AI images"), ("C", "AI-generated work bearing his name"), ("D", "heated disputes regarding his copyright")]},
    34: {"passage": 3, "stem": "According to Ortiz, AI companies are advised to", "ans": "D", "opts": [("A", "campaign for new policies or regulation"), ("B", "offer their services to public institutions"), ("C", "strengthen their relationships with AI users"), ("D", "adopt a different strategy for AI model training")]},
    35: {"passage": 3, "stem": "What is the text mainly about?", "ans": "A", "opts": [("A", "Artists' responses to AI art generation."), ("B", "AI's expanded role in artistic creation."), ("C", "Privacy issues in the application of AI."), ("D", "Opposing views on AI development.")]},

    # Text 4 (36-40)
    36: {"passage": 4, "stem": "The Chesapeake Bay is described in Paragraph 1 as", "ans": "A", "opts": [("A", "a valuable natural environment"), ("B", "a controversial conservation area"), ("C", "a place with commercial potential"), ("D", "a headache for nearby communities")]},
    37: {"passage": 4, "stem": "The U.S. Supreme Court's ruling in the Idaho case", "ans": "B", "opts": [("A", "reinforces water pollution control"), ("B", "weakens the EPA's regulatory power"), ("C", "will end conflicts among local residents"), ("D", "may face opposition from mining operators")]},
    38: {"passage": 4, "stem": "How does the author feel about the future of the Chesapeake Bay?", "ans": "A", "opts": [("A", "Worried."), ("B", "Puzzled."), ("C", "Relieved."), ("D", "Encouraged.")]},
    39: {"passage": 4, "stem": "What can be inferred about the EPA's involvement in the Chesapeake Bay Program?", "ans": "D", "opts": [("A", "It has restored the balance among neighboring jurisdictions."), ("B", "It has triggered a radical reform in commercial fisheries."), ("C", "It has set a fine example of respecting state authorities."), ("D", "It has ensured the coordination of protection efforts.")]},
    40: {"passage": 4, "stem": "The author holds that the state lawmakers should", "ans": "B", "opts": [("A", "be cautious about the influence of land owners"), ("B", "attach due importance to wetlands protections"), ("C", "recognize the need to expand wildlife refuges"), ("D", "improve the wellbeing of endangered species")]},

    # Part B (41-45)
    41: {
        "passage": 5, "stem": "Hannah", "ans": "E",
        "opts": [
            ("A", "It is clear that the countries of origin have never been compensated for the stolen artifacts."),
            ("B", "It is a flawed line of reasoning to argue against returning artifacts to their countries of origin."),
            ("C", "Museum visitors can still learn as much from artifacts' copies after the originals are returned."),
            ("D", "Reproductions, even if perfectly made, cannot take the place of the authentic objects."),
            ("E", "The real value of artifacts can only be recognized in their countries of origin rather than anywhere else."),
            ("F", "Ways to get artifacts from other countries must be decent and lawful."),
            ("G", "Concern over security is no excuse for refusing to return artifacts to their countries of origin.")
        ]
    },
    42: {
        "passage": 5, "stem": "Buck", "ans": "C",
        "opts": [
            ("A", "It is clear that the countries of origin have never been compensated for the stolen artifacts."),
            ("B", "It is a flawed line of reasoning to argue against returning artifacts to their countries of origin."),
            ("C", "Museum visitors can still learn as much from artifacts' copies after the originals are returned."),
            ("D", "Reproductions, even if perfectly made, cannot take the place of the authentic objects."),
            ("E", "The real value of artifacts can only be recognized in their countries of origin rather than anywhere else."),
            ("F", "Ways to get artifacts from other countries must be decent and lawful."),
            ("G", "Concern over security is no excuse for refusing to return artifacts to their countries of origin.")
        ]
    },
    43: {
        "passage": 5, "stem": "Sara", "ans": "F",
        "opts": [
            ("A", "It is clear that the countries of origin have never been compensated for the stolen artifacts."),
            ("B", "It is a flawed line of reasoning to argue against returning artifacts to their countries of origin."),
            ("C", "Museum visitors can still learn as much from artifacts' copies after the originals are returned."),
            ("D", "Reproductions, even if perfectly made, cannot take the place of the authentic objects."),
            ("E", "The real value of artifacts can only be recognized in their countries of origin rather than anywhere else."),
            ("F", "Ways to get artifacts from other countries must be decent and lawful."),
            ("G", "Concern over security is no excuse for refusing to return artifacts to their countries of origin.")
        ]
    },
    44: {
        "passage": 5, "stem": "Victor", "ans": "G",
        "opts": [
            ("A", "It is clear that the countries of origin have never been compensated for the stolen artifacts."),
            ("B", "It is a flawed line of reasoning to argue against returning artifacts to their countries of origin."),
            ("C", "Museum visitors can still learn as much from artifacts' copies after the originals are returned."),
            ("D", "Reproductions, even if perfectly made, cannot take the place of the authentic objects."),
            ("E", "The real value of artifacts can only be recognized in their countries of origin rather than anywhere else."),
            ("F", "Ways to get artifacts from other countries must be decent and lawful."),
            ("G", "Concern over security is no excuse for refusing to return artifacts to their countries of origin.")
        ]
    },
    45: {
        "passage": 5, "stem": "Julia", "ans": "B",
        "opts": [
            ("A", "It is clear that the countries of origin have never been compensated for the stolen artifacts."),
            ("B", "It is a flawed line of reasoning to argue against returning artifacts to their countries of origin."),
            ("C", "Museum visitors can still learn as much from artifacts' copies after the originals are returned."),
            ("D", "Reproductions, even if perfectly made, cannot take the place of the authentic objects."),
            ("E", "The real value of artifacts can only be recognized in their countries of origin rather than anywhere else."),
            ("F", "Ways to get artifacts from other countries must be decent and lawful."),
            ("G", "Concern over security is no excuse for refusing to return artifacts to their countries of origin.")
        ]
    }
}

orig_q_by_num = {q.get('sort_order', idx+1): q for idx, q in enumerate(orig['questions'])}

calibrated_questions = []
for q_num in range(1, 46):
    q_def = q_defs[q_num]
    orig_q = orig_q_by_num.get(q_num, {})
    qid = orig_q.get('id') or str(uuid.uuid4())
    pts = 0.5 if q_num <= 20 else 2.0
    q_type = 'cloze_item' if q_num <= 20 else 'reading_item'
    
    std_opts = [
        {"key": opt[0], "value": opt[0], "text": opt[1], "content": opt[1]}
        for opt in q_def["opts"]
    ]
    
    q_stem = f"Choose the best option for blank [{q_num}] in the passage:" if q_num <= 20 else q_def["stem"]
    q_obj = {
        "id": qid,
        "exam_id": exam["id"],
        "passage_id": p_ids[q_def["passage"]],
        "category_id": "ky1",
        "q_type": q_type,
        "stem": q_stem,
        "options": std_opts,
        "correct_answer": q_def["ans"],
        "explanation": orig_q.get("explanation") or "",
        "points": pts,
        "sort_order": q_num,
        "answer": q_def["ans"],
        "question_number": q_num,
        "score": pts
    }
    calibrated_questions.append(q_obj)

# Update exam object
exam["questions"] = calibrated_questions
exam["passages"] = passages_data

output_data = {
    "exam": exam,
    "passages": passages_data,
    "questions": calibrated_questions,
    "exportedAt": orig.get("exportedAt")
}

with open(exam_file, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Successfully reconstructed 2024 ky1 pure gold: {len(passages_data)} passages, {len(calibrated_questions)} questions.")
