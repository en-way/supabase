import json
import re

exam_file = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\47036de0-e57d-5ccb-9bc8-b3f86d4e6457.json"
data = json.load(open(exam_file, encoding="utf-8"))

replacements = {
    # Q1
    "etysuggestt)at": "they suggest that",
    "on)eproblemsofadolescence": "on the problems of adolescence",
    "：oncerningy(句中的focusingon": "concerning与③句中的focusing on",
    "：enteron": "center on",
    "acts on)ebrain": "acts on the brain",
    "bad weather)ere": "bad weather here",
    
    # Q4
    "(句中that引导的宾语从句": "④句中that引导的宾语从句",
    "：ommitcrimes": "commit crimes",
    "retur；只与介词": "return只与介词",
    "inreturnfor": "in return for",
    "inreplyto和inresponseto": "in reply to和in response to",
    "repl，和response": "reply和response",
    "repl，指": "reply指",
    "“自发的a本能的反应行为”": "“自发的、本能的反应行为”",
    "[D] inresponseto": "[D] in response to",
    "(文中inresponseto": "(文中in response to",
    "“行为原因”h": "“行为原因”)",
    "Inresponsetoyourinquiry": "In response to your inquiry",
    "答复……yThelaw waspassedinresponsetopublicpressure": "答复……。The law was passed in response to public pressure",
    "retur；在词义上": "return在词义上",
    "for your)elp- 感谢你帮忙，我请你吃午饭好吗-": "for your help? 感谢你帮忙，我请你吃午饭好吗？",
    "she)ejust askedmeaquestioninreturn": "she just asked me a question in return",
    "repl，构成": "reply构成",
    "Ivmwritinginreplytoyourletterof16。arch": "I'm writing in reply to your letter of 16 March",
    "inre“erenceto更常见的形式为withre“erenceto": "in reference to更常见的形式为with reference to",
    "With re“erencetoyourrecent advertisementyIvmwritingtorequest“urther details": "With reference to your recent advertisement, I'm writing to request further details",

    # Q6
    "focusedon形成反义对照": "focused on形成反义对照",
    "consider与)ighligh(对ignore": "consider与highlight对ignore",
    "10% ofthedatawasdiscardedasunreliable": "10% of the data was discarded as unreliable",

    # Q7
    "句主语thelatter": "②句主语the latter",
    "“富有家庭的孩子”n": "“富有家庭的孩子”。",
    "Thelattercommitcrimes和lackofadequateparentalcontrol": "The latter commit crimes和lack of adequate parental control",
    "onyforywith": "on、for、with",
    "forlackof": "for lack of",
    "Hegotanawardforbravery": "He got an award for bravery",
    "astorybasedonfact": "a story based on fact",
    "i；可以表示": "in可以表示",
    "parentalcontrol.wit)可意为": "parental control。with可意为",
    "His“ingerswerenumbedwithcold": "His fingers were numbed with cold",

    # Q9
    "Changesinthesocialstructure，宾语是”u-\nvenilecrimerates": "Changes in the social structure，宾语是juvenile crime rates",
    "Changesinthesocialstructure，宾语是”u-venilecrimerates": "Changes in the social structure，宾语是juvenile crime rates",
    "indirectl，修饰": "indirectly修饰",
    "：heck或reduce": "check或reduce",
    "How will(hesec)an-\ngesaffectus- 这些变化对我们会有什么影响-": "How will these changes affect us? 这些变化对我们会有什么影响？",
    "How will(hesec)an-gesaffectus- 这些变化对我们会有什么影响-": "How will these changes affect us? 这些变化对我们会有什么影响？",
    "(ocheckthegrowt)ofpublicspending": "To check the growth of public spending",
    "Hismusicre-\n“lec(s)isinterestinA“ricanculture": "His music reflects his interest in African culture",
    "Hismusicre-“lec(s)isinterestinA“ricanculture": "His music reflects his interest in African culture",

    # Q10
    "changesinthee-\nconomy": "changes in the economy",
    "changesinthee-conomy": "changes in the economy",
    "fewerjobopportunitiesandrisingunem-\nployment": "fewer job opportunities and rising unemployment",
    "fewerjobopportunitiesandrisingunem-ployment": "fewer job opportunities and rising unemployment",
    "[B] leadto": "[B] lead to",
    "到达r等同于": "到达或等同于",
    "leadto，实际上": "lead to，实际上",
    "leadstoillness": "leads to illness",
    "pointto意为": "point to意为",
    "success“ful": "successful",
    "cometo意为": "come to意为",
    "cometoanunderstanding": "come to an understanding",
    "ThebillcametoY30": "The bill came to $30",
    "amountto意为“总计，共计；等于，相当于”y\n如：Herstandardsamountedtoper“ection": "amount to意为“总计，共计；等于，相当于”，如：Her standards amounted to perfection",
    "amountto意为“总计，共计；等于，相当于”y如：Herstandardsamountedtoper“ection": "amount to意为“总计，共计；等于，相当于”，如：Her standards amounted to perfection",
    "短语动词：applyto(适合)ybringto(苏醒，停下来)yconformto(相称)yfallto(开\n始)yob”ectto(反对)yre“erto(提及，指)ysetto(着手)ytaketo(喜爱上，专心于)yyieldto(屈服于)": "短语动词：apply to (适合)、bring to (苏醒，停下来)、conform to (相称)、fall to (开始)、object to (反对)、refer to (提及，指)、set to (着手)、take to (喜爱上，专心于)、yield to (屈服于)",
    "短语动词：applyto(适合)ybringto(苏醒，停下来)yconformto(相称)yfallto(开始)yob”ectto(反对)yre“erto(提及，指)ysetto(着手)ytaketo(喜爱上，专心于)yyieldto(屈服于)": "短语动词：apply to (适合)、bring to (苏醒，停下来)、conform to (相称)、fall to (开始)、object to (反对)、refer to (提及，指)、set to (着手)、take to (喜爱上，专心于)、yield to (屈服于)",

    # Q13
    "“幸免于变化”a“注意到变化”a“着手进行变化”": "“幸免于变化”、“注意到变化”、“着手进行变化”",
    "；otice和un-\ndertake不与“amil，": "notice和undertake不与family",
    "；otice和un-dertake不与“amil，": "notice和undertake不与family",
    "下文，句提到": "下文②句提到",
    "痛苦r愉快": "痛苦或愉快",
    "customs)avesur-\nvivedfromearliertimes": "customs have survived from earlier times",
    "customs)avesur-vivedfromearliertimes": "customs have survived from earlier times",
    "any birds didn't survive t)esevere\nwinter": "Many birds didn't survive the severe winter",
    "any birds didn't survive t)esevere winter": "Many birds didn't survive the severe winter",
    "toundertakeapro”ectrinvestigation承担一个项目r进行调查": "to undertake a project or investigation承担一个项目或进行调查",
    "与：hange构成": "与change构成",
    "当：hange作": "当change作",
    "bringabou(": "bring about",
    "accommodate to)radaptedtoradjustto": "accommodate to、adapt to或adjust to",

    # Q14
    "：onsequentl，符合要求": "consequently符合要求",
    "enmust wear": "Men must wear",
    "skirttordressandnottrousers": "skirt or dress and not trousers",
    "ThegamewillbebroadcastsimultaneouslyonT\\andradio": "The game will be broadcast simultaneously on TV and radio",

    # Q15
    "tha；兼有": "than兼有",
    "tha；搭配": "than搭配",
    "tha；兼有连词": "than兼有连词",
    "wascommoninthetraditionalfamily": "was common in the traditional family",
    "thanwhatwascommoninthetraditionalfamily": "than what was common in the traditional family",
    "lesssupervi-\nsion": "less supervision",
    "lesssupervi-sion": "less supervision",
    "which)和as": "which和as",
    "：hildrenarelikely(ohavelesssupervision": "children are likely to have less supervision",
    "tha；的特殊用法。tha；做关系代词": "than的特殊用法。than做关系代词",
    "相当于(than what，如：Theboyhaseatenmore\nfoodthan is good for his health.tX...eatenmorefoodthanwhatisgoodforhishealth)那个孩子吃": "相当于than what，如：The boy has eaten more food than is good for his health. (即...eaten more food than what is good for his health)那个孩子吃",
    "相当于(than what，如：Theboyhaseatenmore foodthan is good for his health.tX...eatenmorefoodthanwhatisgoodforhishealth)那个孩子吃": "相当于than what，如：The boy has eaten more food than is good for his health. (即...eaten more food than what is good for his health)那个孩子吃",
    "which)wasunlaw“ul": "which was unlawful",
    "a“fter lunch": "after lunch",

    # Q16
    "thetraditional“am-\nily16与句内上文“amilies": "the traditional family与句内上文families",
    "thetraditional“am-ily16与句内上文“amilies": "the traditional family与句内上文families",
    "changesinthesocialstructure": "changes in the social structure",
    "“amil，的常用搭配": "family的常用搭配",
    "theconceptofin“initespace": "the concept of infinite space",
    "Italy，意大利": "Italy，意大利",

    # Q17
    "Other17causesofoffensiveacts与上文(句中aninfluence(影响，原因)on\njuvenilecrimerates": "Other causes of offensive acts与上文①句中an influence (影响，原因) on juvenile crime rates",
    "Other17causesofoffensiveacts与上文(句中aninfluence(影响，原因)on juvenilecrimerates": "Other causes of offensive acts与上文①句中an influence (影响，原因) on juvenile crime rates",
    "修饰：auses": "修饰causes",
    "酗酒a\n毒品": "酗酒、毒品",
    "酗酒a毒品": "酗酒、毒品",
    "identi“，派生出": "identify派生出",
    "buildingisassessable": "building is assessable",
    "assessableincome": "assessable income",
    "Inbuyinga\nsuityadifferenceoftencentsinpricesisnegligible": "In buying a suit, a difference of ten cents in prices is negligible",
    "Inbuyinga suityadifferenceoftencentsinpricesisnegligible": "In buying a suit, a difference of ten cents in prices is negligible",
    "wasdressedwithincrediblespeed": "was dressed with incredible speed",

    # Q18
    "ofdrugsandalcohol": "of drugs and alcohol",
    "提高”a“对毒品和酒精的限制trestriction)": "提高”、“对毒品和酒精的限制 (restriction)",
    "availabilit，本身": "availability本身",
    "Theavail-\nabilityofcleanwaterresourceisbecomingmoreandmoredifficult": "The availability of clean water resource is becoming more and more difficult",
    "Theavail-abilityofcleanwaterresourceisbecomingmoreandmoredifficult": "The availability of clean water resource is becoming more and more difficult",
    "Sugarisunderallocationduringwartime": "Sugar is under allocation during wartime",

    # Q19
    "popularit，普及": "popularity普及",
    "ofchildabuseandchildneglect": "of child abuse and child neglect",
    "awareness tha不断暴露": "awareness that不断暴露",
    "Thereisahighincidenceofmalariainthetropics": "There is a high incidence of malaria in the tropics",
    "popularit，则是": "popularity则是",
    "at homewant": "at home want",
    ")arm“ul": "harmful",
    "Thecomedianen”oyedgreatpopularityduring\n(he30sand40s": "The comedian enjoyed great popularity during the 30s and 40s",
    "Thecomedianen”oyedgreatpopularityduring (he30sand40s": "The comedian enjoyed great popularity during the 30s and 40s",

    # Q21
    "21.HowdidRedmonfindhisjob-": "21. How did Redmon find his job?",
    "[A] Bysearchingopeningsinajobdatabase.": "[A] By searching openings in a job database.",
    "[B] Bypostingamatchingpositioninadatabase.": "[B] By posting a matching position in a database.",
    "[C] Byusingaspecialserviceofadatabase.": "[C] By using a special service of a database.",
    "[D] ByE-mailinghisresumetoadatabase.": "[D] By E-mailing his resume to a database.",
    "f个人\n搜索代理jy": "“个人搜索代理”，",
    "f个人搜索代理jy": "“个人搜索代理”，",
    "工作[C] 中“特殊服务j指的就是网站上提供的f个人搜索代理”": "工作。[C]中“特殊服务”指的就是网站上提供的“个人搜索代理”",
    "正确项[C]是，句的同义改写。adatabase对应文中thesiteyaspecialservice\n对应文中personalsearchagentM注意yy句中thesite即；句中的CareerBuilderyajobdatabase。": "正确项[C]是②句的同义改写。a database对应文中the site，a special service对应文中personal search agent。注意②句中the site即①句中的CareerBuilder, a job database。",
    "正确项[C]是，句的同义改写。adatabase对应文中thesiteyaspecialservice对应文中personalsearchagentM注意yy句中thesite即；句中的CareerBuilderyajobdatabase。": "正确项[C]是②句的同义改写。a database对应文中the site，a special service对应文中personal search agent。注意②句中the site即①句中的CareerBuilder, a job database。",
    "[A]反向干扰。y句...searcheditwithnosuccess...中的i（指；句的jobdatabasey可见，他并\n\n不是在这个数据库中搜到空缺职位从而找到工作的[B] 和[D]偷梁换柱[B] 将（句中f当资料库\n里贴出了相匹配的职位时j偷换成“雷德曼自己张贴相匹配的职位”n[D]将o句提到的雷德曼简历\n的接收者theemployer偷换成adatabase": "[A]反向干扰。①句“...searched it with no success...”中的it指①句的job database，可见，他并不是在这个数据库中搜到空缺职位从而找到工作的。[B]和[D]偷梁换柱：[B]将④句中“当资料库里贴出了相匹配的职位时”偷换成“雷德曼自己张贴相匹配的职位”；[D]将⑤句提到的雷德曼简历的接收者the employer偷换成a database。",

    # Q22
    "22.Whichofthefollowingcanbeadisadvantageof\nsearchagents-": "22. Which of the following can be a disadvantage of search agents?",
    "22.Whichofthefollowingcanbeadisadvantageof searchagents-": "22. Which of the following can be a disadvantage of search agents?",
    "[A] ^ackofcounseling.": "[A] Lack of counseling.",
    "[B] ^imitednumberofvisits.": "[B] Limited number of visits.",
    "[C] ^owerefficiency.": "[C] Lower efficiency.",
    "[D] Fewersuccessfulmatches.": "[D] Fewer successful matches.",
    "由第三段y（句可知：所有求职程序都不隐含求职建议tnocareercounselingim？\nplicitinallofthishy其中allofthis回指上文，句提到的theseprogramsy虽然没有明确指出searcha？\ngentsy但却包含在内，因此[A]正确。": "由第三段①句可知：所有求职程序都不隐含求职建议(no career counseling implicit in all of this)，其中all of this回指上文提到these programs，虽然没有明确指出search agents，但却包含在内，因此[A]正确。",
    "文章第二a三段都在分析搜索代理的优缺点，第二段，句先指出搜索代理的优点：\n减少了人工重复性访问数据库的需要。te句转折指出了它的缺陷：每缩小一次搜索条件，对求职\n者来说就意味着丧失了一次机会。但这个缺点在四个选项中都没有提到。搜索代理的另外一个缺点在\n文章中比较隐蔽，需要考生仔细阅读。正确项[A]为第三段（句的改写ycounseling对应原文中；ocareer\ncounselingM": "文章第二、三段都在分析搜索代理的优缺点，第二段①句先指出搜索代理的优点：减少了人工重复性访问数据库的需要。②句转折指出了它的缺陷：每缩小一次搜索条件，对求职者来说就意味着丧失了一次机会。但这个缺点在四个选项中都没有提到。搜索代理的另外一个缺点在文章中比较隐蔽，需要考生仔细阅读。正确项[A]为第三段①句的改写，counseling对应原文中no career counseling。",
    "[B]曲解文义，第二段，句中reducetheneedforrepeatedvisits是搜索代理的优点，而非局限\n性[C] 张冠李戴y^owerefficiency为求职网站的缺点（第二段；句，正是搜索代理的优点）[D] 无\n中生有，利用文中第四段的three（三个）捏造信息fewer（更少的）n且断章取义，文中matches指的是\njobmatches（职位匹配）y而不是successfulmatches（成功匹配）。": "[B]曲解文义，第二段①句中reduce the need for repeated visits是搜索代理的优点，而非局限性。[C]张冠李戴，Lower efficiency为求职网站的缺点（第二段①句，正是搜索代理的优点）。[D]无中生有，利用文中第四段的three（三个）捏造信息fewer（更少的）；且断章取义，文中matches指的是job matches（职位匹配），而不是successful matches（成功匹配）。",

    # Q23
    "23.Theexpressionftipservicejt^ine3y[aragraph\n3hmostprobablymeans\n.": "23. The expression \"tip service\" (Line 3, Paragraph 3) most probably means _______.",
    "23.Theexpressionftipservicejt^ine3y[aragraph 3hmostprobablymeans .": "23. The expression \"tip service\" (Line 3, Paragraph 3) most probably means _______.",
    "23.（第三段第三行）最可能的含义是\nMM": "23.（第三段第三行）最可能的含义是",
    "定位到第三段e句。句中分号表示了前后语义上的并列，即后面部\n分是对前面部分的解释和说明。前面部分提到，可以把搜索代理当作一种tipservicen下文对此进行\n解释：当你收到电子邮件时，把它看作是再次核查数据库的提示treminderhM根据句意判断yuse...asa\nkindoftipservice和：onsideritareminder意思是一样，\nreminder与tipservice前后呼应，应为同义解释y[D]\n正确。": "定位到第三段②句。句中分号表示了前后语义上的并列，即后面部分是对前面部分的解释和说明。前面部分提到，可以把搜索代理当作一种tip service；下文对此进行解释：当你收到电子邮件时，把它看作是再次核查数据库的提示(reminder)。根据句意判断，use...as a kind of tip service和consider it a reminder意思是一样，reminder与tip service前后呼应，应为同义解释，[D]正确。",
    "tip本是一个多义词，它不仅表示“小费”y还可以表示f忠告，指点jy本题主要考查\n考生将tip置身语境中探寻其意义的能力。正确项[D]为同义解释ytip此处意为asmallpieceofad？\nviceaboutsthpracticalf指点，实用的提示jyreminder是tipservice在文中的准确含义。\n[A]反向干扰，利用第三段（句；ocareercounseling中：ounseling进行反向干扰。但是考生须\n知yadvisory作形容词时，意为f咨询的，劝告的jtgivingadvicehn作名词时，指的是f官方通告，警告j\ntwarninghy而不是f建议，咨询jtcounselingh[B] 无中生有，其实意在将考生往“小费”的思路上引。\n[C]答非所问，\ninteractive虽然是搜索代理的特点（第一段（句）y但和tipservice无关": "tip本是一个多义词，它不仅表示“小费”，还可以表示“忠告，指点”；本题主要考查考生将tip置身语境中探寻其意义的能力。正确项[D]为同义解释，tip此处意为a small piece of advice about sth practical（指点，实用的提示），reminder是tip service在文中的准确含义。\n[A]反向干扰，利用第三段①句no career counseling中counseling进行反向干扰。但是考生须知，advisory作形容词时，意为“咨询的，劝告的”(giving advice)；作名词时，指的是“官方通告，警告”(warning)，而不是“建议，咨询”(counseling)。[B]无中生有，其实意在将考生往“小费”的思路上引。\n[C]答非所问，interactive虽然是搜索代理的特点（第一段①句），但和tip service无关。",

    # Q24
    "24.Why does CareerSite'sagentoffereachjob\nhunteronlythreejoboptions-": "24. Why does CareerSite's agent offer each job hunter only three job options?",
    "24.Why does CareerSite'sagentoffereachjob hunteronlythreejoboptions-": "24. Why does CareerSite's agent offer each job hunter only three job options?",
    "[A] Tofocusonbetterjobmatches.": "[A] To focus on better job matches.",
    "[B] Toattractmorereturningvisits.": "[B] To attract more returning visits.",
    "[C] Toreservespaceformoremessages.": "[C] To reserve space for more messages.",
    "[D] Toincreasetherateofsuccess.": "[D] To increase the rate of success.",
    "threejoboptions可以定位到文章第四段。该段首句指出f一些网\n站设计搜索代理的目的是为了吸引求职者回访网站。j接着y（句以CareerSite向每个求职者只提\n供三个选择为例对；进行详细说明。因此[B]正确。": "three job options可以定位到文章第四段。该段首句指出“一些网站设计搜索代理的目的是为了吸引求职者回访网站”。接着②句以CareerSite向每个求职者只提供三个选择为例进行详细说明。因此[B]正确。",
    "文中的temp（改成了attract": "文中的tempt改成了attract",
    "[A]首先曲解文意，第四段（句可知，网站代理只提供三个选择是为了吸引求职者来网站寻找\n更多相匹配的工作，而不是更好的匹配工作；其次张冠李戴，是求职者而不是网站关注更多相匹配的\n工作[C] 和[D]无中生有，文中未提及": "[A]首先曲解文意，第四段②句可知，网站代理只提供三个选择是为了吸引求职者来网站寻找更多相匹配的工作，而不是更好的匹配工作；其次张冠李戴，是求职者而不是网站关注更多相匹配的工作。[C]和[D]无中生有，文中未提及。",

    # Q26
    "26.Whatdoestheauthorintendtoillustratewith\nAAAAcarsandZodiaccars-": "26. What does the author intend to illustrate with AAAA cars and Zodiac cars?",
    "26.Whatdoestheauthorintendtoillustratewith AAAAcarsandZodiaccars-": "26. What does the author intend to illustrate with AAAA cars and Zodiac cars?",
    "26.作者借用“AAAA 汽车j和fZodiac汽车”": "26.作者借用“AAAA 汽车”和“Zodiac 汽车”",
    "[A] Akindofoverlookedinequality.": "[A] A kind of overlooked inequality.",
    "[B] Atypeofconspicuousbias.": "[B] A type of conspicuous bias.",
    "[C] Atypeofpersonalprejudice.": "[C] A type of personal prejudice.",
    "[D] Akindofbranddiscrimination.": "[D] A kind of brand discrimination.",
    "“AAAAcarsj和fZodiaccars”定位到第二段；句：AAAA 出\n租车公司的名称在电话薄上排在Zodiac公司之前，因而占有很大优势。y句接着指出Adam Abbott\n在姓名排序中比Zoe Zysman靠前，也享有优势。作者举例旨在说明首段提出的主题：姓氏字母排序\n是一种隐蔽的不公和歧视，其中“隐蔽的j暗含着f被忽视的”之意[A] 正确。": "“AAAA cars”和“Zodiac cars”定位到第二段①句：AAAA出租车公司的名称在电话簿上排在Zodiac公司之前，因而占有很大优势。②句接着指出Adam Abbott在姓名排序中比Zoe Zysman靠前，也享有优势。作者举例旨在说明首段提出的主题：姓氏字母排序是一种隐蔽的不公和歧视，其中“隐蔽的”暗含着“被忽视的”之意，[A]正确。",
    "inequalityabiasaprejudiceadiscrimination": "inequality、bias、prejudice、discrimination",
    "正确项[A]中over？\nlooked是insidiousyunaware的近义替换；\ninequality是discrimination的近义替换。": "正确项[A]中overlooked是insidious、unaware的近义替换；inequality是discrimination的近义替换。",
    "[B]a[C]反向干扰[B] 将insidious（隐蔽的）换成了：onspicuous（显而易见的）n[C]将首段提出\n的姓氏字母排序歧视是一种“社会歧视现象j换成了f个人偏见”[D] 将事实本身等同于写作目的，\n文中提及AAAcarsyZodiaccars绝不是只限于讨论品牌，而是揭示姓氏字母排序歧视的社会现象": "[B]、[C]反向干扰：[B]将insidious（隐蔽的）换成了conspicuous（显而易见的）；[C]将首段提出的姓氏字母排序歧视是一种“社会歧视现象”换成了“个人偏见”。[D]将事实本身等同于写作目的，文中提及AAAA cars、Zodiac cars绝不是只限于讨论品牌，而是揭示姓氏字母排序歧视的社会现象。",

    # Q27
    "27.Whatcanweinferfromthefirstthree[aragraphs-": "27. What can we infer from the first three paragraphs?",
    "[A] InbothEastand Westynamesareessentialto\nsuccess.": "[A] In both East and West, names are essential to success.",
    "[A] InbothEastand Westynamesareessentialto success.": "[A] In both East and West, names are essential to success.",
    "[B] Thealphabetistoblameforthefailureof‘o.\nZysman.": "[B] The alphabet is to blame for the failure of Zoe Zysman.",
    "[B] Thealphabetistoblameforthefailureof‘o. Zysman.": "[B] The alphabet is to blame for the failure of Zoe Zysman.",
    "[C] Customersoftenpayalotofattentiontocom-\npaniesvnames.": "[C] Customers often pay a lot of attention to companies' names.",
    "[C] Customersoftenpayalotofattentiontocom- paniesvnames.": "[C] Customers often pay a lot of attention to companies' names.",
    "[D] Someformofdiscriminationistoosubtleto\nrecognize.": "[D] Some form of discrimination is too subtle to recognize.",
    "[D] Someformofdiscriminationistoosubtleto recognize.": "[D] Some form of discrimination is too subtle to recognize.",
    "第二a三段都是第一段主题的例证段。四个选项中只有[D]是对第一段中主旨内容的\n理解，其他三项都是都只是对照第二a三段的部分内容。再者，从文中关键词如insidiousform（隐蔽\n的形式）和lesswellknown（鲜为人知的）y可以确认[D]正确。": "第二、三段都是第一段主题的例证段。四个选项中只有[D]是对第一段中主旨内容的理解，其他三项都只是对照第二、三段的部分内容。再者，从文中关键词如insidious form（隐蔽的形式）和less well known（鲜为人知的），可以确认[D]正确。",
    "[A]夸大其辞，将第三段提到的f许多成功者（既有东方人也有西方人）的姓氏排在字母表的前\n\n半部分j夸大为“名字是所有人成功的关键”n文中只表明姓氏排序靠前可能是一种优势，但并不能由\n此推出名字是所有人成败的关键因素[B] 和[C]偷换概念y[B]将f（人为的）字母排序歧视j偷换为\n“字母表”n导致Zoe Zysman失败的是人为的歧视，而非字母表本身[C] 将第二段首句提到的f对\n名称排序靠前的公司的关注j偷换为“对公司名称的关注”n该例子主要是用来说明字母排序歧视现\n象确实存在，而不是用来说明顾客是否关注公司名称。": "[A]夸大其辞，将第三段提到的“许多成功者（既有东方人也有西方人）的姓氏排在字母表的前半部分”夸大为“名字是所有人成功的关键”；文中只表明姓氏排序靠前可能是一种优势，但并不能由此推出名字是所有人成败的关键因素。[B]和[C]偷换概念：[B]将“（人为的）字母排序歧视”偷换为“字母表”；导致Zoe Zysman失败的是人为的歧视，而非字母表本身。[C]将第二段首句提到的“对名称排序靠前的公司的关注”偷换为“对公司名称的关注”；该例子主要是用来说明字母排序歧视现象确实存在，而不是用来说明顾客是否关注公司名称。",

    # Q28
    "28.The4thparagraphsuggeststhat\n.\n28.文章第四段暗示\nM": "28. The 4th paragraph suggests that ______.\n28. 文章第四段暗示：",
    "[A] questionsareoftenputtothemoreintelligent\nstudentsM": "[A] questions are often put to the more intelligent students.",
    "[A] questionsareoftenputtothemoreintelligent studentsM": "[A] questions are often put to the more intelligent students.",
    "[B] alphabeticallydisadvantagedstudentsoftenes-\ncapefromclass": "[B] alphabetically disadvantaged students often escape from class.",
    "[B] alphabeticallydisadvantagedstudentsoftenes- capefromclass": "[B] alphabetically disadvantaged students often escape from class.",
    "[C] teachersshouldpayattentiontoalloftheir\nstudentsM": "[C] teachers should pay attention to all of their students.",
    "[C] teachersshouldpayattentiontoalloftheir studentsM": "[C] teachers should pay attention to all of their students.",
    "[D] studentsshouldbeseatedaccordingtotheir\neyesightM": "[D] students should be seated according to their eyesight.",
    "[D] studentsshouldbeseatedaccordingtotheir eyesightM": "[D] students should be seated according to their eyesight.",
    "[A]偷梁换柱，将“姓氏在字母表中靠前的学生j偷换为f聪明的学生”y由e句可反推出老师经常\n提问的对象是坐在前排的学生即姓氏字母靠前的学生[B] 望文生义yo句中）adaluckyescape指f不\n具备排序优势的学生逃脱了老师的提问jy[B]将其曲解为“经常逃课”[D] 无中生有，过于片面ye句\n提及“近视眼的学生被固定在后排”是为了强调姓氏字母排序歧视现象的负面影响，而非排座建议": "[A]偷梁换柱，将“姓氏在字母表中靠前的学生”偷换为“聪明的学生”，由②句可反推出老师经常提问的对象是坐在前排的学生即姓氏字母靠前的学生。[B]望文生义，⑤句中had a lucky escape指“不具备排序优势的学生逃脱了老师的提问”，[B]将其曲解为“经常逃课”。[D]无中生有，过于片面，②句提及“近视眼的学生被固定在后排”是为了强调姓氏字母排序歧视现象的负面影响，而非排座建议。",

    # Q29
    "29.Whatdoestheauthormeanby fmostpeopleare\nliterallyhavinga‘‘‘jt^ine2y[aragraph5h-": "29. What does the author mean by \"most people are literally having a ZZZ\" (Line 2, Paragraph 5)?",
    "29.Whatdoestheauthormeanby fmostpeopleare literallyhavinga‘‘‘jt^ine2y[aragraph5h-": "29. What does the author mean by \"most people are literally having a ZZZ\" (Line 2, Paragraph 5)?",
    "29.fmostpeopleareliterallyhavinga‘‘‘j（第\n五段第二行）在文中的含义是什么？": "29. “most people are literally having a ZZZ”（第五段第二行）在文中的含义是什么？",
    "[A] Theyaregettingimpatient.": "[A] They are getting impatient.",
    "[B] Theyarenoisilydozingoff.": "[B] They are noisily dozing off.",
    "[C] Theyarefeelinghumiliated.": "[C] They are feeling humiliated.",
    "[D] Theyarebusywithwordpuzzles.": "[D] They are busy with word puzzles.",
    "根据题干信息直接定位到第五段，句：大学毕业典礼上，姓氏以ABC开头的学生先\n领到毕业证，当轮到那些姓氏以‘开头的学生时，大多数参加者真是已经在‘‘‘了。‘‘‘是英文拟声\n词，是漫画中睡觉的符号，表示打鼾声，故[B]为最佳选项。": "根据题干信息直接定位到第五段②句：大学毕业典礼上，姓氏以ABC开头的学生先领到毕业证，当轮到那些姓氏以Z开头的学生时，大多数参加者真是已经在ZZZ了。ZZZ是英文拟声词，是漫画中睡觉的符号，表示打鼾声，故[B]为最佳选项。",
    "该句是；句f（姓氏排序中靠后的人得到的）羞辱依然在继续j的例证，旨在说明The\nhumiliationM本题既考查学生根据上下文理解句意的能力，同时也考查他们透过语言符号代码解读文\n化的能力。正确项[B]是结合段落主旨对事实细节的正确理解。首先yhavinga‘‘‘是作者以幽默风\n趣的手法描绘了台下观众百无聊赖的情形，暗示他们等候的时间太长；其次‘‘‘是英文拟声词，作为\n符号出现在一些漫画中，表示打鼾声，比如：瑞星杀毒软件中就有只狮子发出f‘‘‘j声的画面，表示它\n在酣睡。": "该句是①句“（姓氏排序中靠后的人得到的）羞辱依然在继续”的例证，旨在说明The humiliation。本题既考查学生根据上下文理解句意的能力，同时也考查他们透过语言符号代码解读文化的能力。正确项[B]是结合段落主旨对事实细节的正确理解。首先，having a ZZZ是作者以幽默风趣的手法描绘了台下观众百无聊赖的情形，暗示他们等候的时间太长；其次ZZZ是英文拟声词，作为符号出现在一些漫画中，表示打鼾声，比如：瑞星杀毒软件中就有只狮子发出“ZZZ”声的画面，表示它在酣睡。",
    "[C]根据第五段首句中）umiliation一词设置无关干扰，首句说的是姓氏字母排序歧视现象所造成\n的羞辱依然在继续，指的是姓氏排序靠后的人感到羞辱，而无法推出毕业典礼使得大多数人感到羞\n辱[A] 过度引申y“变得不耐烦”这么具体的反应无从推知[D] 望文生义，将‘‘‘错误地理解为f字\n谜游戏j。": "[C]根据第五段首句中humiliation一词设置无关干扰，首句说的是姓氏字母排序歧视现象所造成的羞辱依然在继续，指的是姓氏排序靠后的人感到羞辱，而无法推出毕业典礼使得大多数人感到羞辱。[A]过度引申，“变得不耐烦”这么具体的反应无从推知。[D]望文生义，将ZZZ错误地理解为“字谜游戏”。",

    # Q36
    "36.WhatdoAmericanparentsexpecttheirchildren\ntoacquireinschool-": "36. What do American parents expect their children to acquire in school?",
    "36.WhatdoAmericanparentsexpecttheirchildren toacquireinschool-": "36. What do American parents expect their children to acquire in school?",
    "[A] Thehabitofthinkingindependently.": "[A] The habit of thinking independently.",
    "[B] [rofoundknowledgeoftheworld.": "[B] Profound knowledge of the world.",
    "[C] [racticalabilitiesforfuturecareer.": "[C] Practical abilities for future career.",
    "[D] Theconfidenceinintellectualpursuits.": "[D] The confidence in intellectual pursuits.",
    "根据第一段（句f甚至学校也只是送孩子去接受实用教育tapracticaleducationhlll而不是为\n了知识而去求知tpursueknowledge“orthesakeofknowledgeh的地方”y可以得出答案为[C]y同时排\n除[B]。": "根据第一段①句“甚至学校也只是送孩子去接受实用教育 (a practical education)……而不是为了知识而去求知 (to pursue knowledge for the sake of knowledge) 的地方”，可以得出答案为[C]，同时排除[B]。",
    "正确项[C]为（句中togetapracticaledu？\ncation的同义改写。": "正确项[C]为①句中to get a practical education的同义改写。",
    "[A]利用“才智”设置干扰；“独立思考的习惯”和实用教育相违背，而且文中也没有提及[B] 与\n正确项相反，故排除[D] 利用（句后半部分；ottopursueknowledgeforthesakeofknowledge设\n置干扰；根据e句“学校中不难发现反才智主义的普遍存在”排除": "[A]利用“才智”设置干扰；“独立思考的习惯”和实用教育相违背，而且文中也没有提及。[B]与正确项相反，故排除。[D]利用①句后半部分not to pursue knowledge for the sake of knowledge设置干扰；根据②句“学校中不难发现反才智主义的普遍存在”排除。",

    # Q37
    "37.WecanlearnfromthetextthatAmericanshave\nahistoryof\n.": "37. We can learn from the text that Americans have a history of _______.",
    "37.WecanlearnfromthetextthatAmericanshave ahistoryof .": "37. We can learn from the text that Americans have a history of _______.",
    "37.从文章中我们可以知道美国人具有\n的历史。": "37. 从文章中我们可以知道美国人具有_______的历史。",
    "[A] undervaluingintellect": "[A] undervaluing intellect",
    "[B] favoringintellectualism": "[B] favoring intellectualism",
    "[C] supportingschoolreform": "[C] supporting school reform",
    "[D] suppressingnativeintelligence": "[D] suppressing native intelligence",
    "根据标志词）istoryy可以定位到第四段。第四段提到，历史学家霍夫斯坦特教授在\n他的一本书中探讨了美国政治a宗教和教育领域中反才智主义的根源。他指出：从美国历史一开始，\n对民主和平民主义的追求驱使我们拒绝任何带有精英优越论味道的东西。实用a常识a先天的智力\n被认为是比书本中学到的东西更加高尚的素质。可见y“精英优越论味道的东西”在这里指的就是才\n智主义。因此，美国有史以来就是反对才智主义的，答案为[A]。": "根据标志词history可以定位到第四段。第四段提到，历史学家霍夫斯坦特教授在他的一本书中探讨了美国政治、宗教和教育领域中反才智主义的根源。他指出：从美国历史一开始，对民主和平民主义的追求驱使我们拒绝任何带有精英优越论味道的东西。实用、常识、先天的智力被认为是比书本中学到的东西更加高尚的素质。可见，“精英优越论味道的东西”在这里指的就是才智主义。因此，美国有史以来就是反对才智主义的，答案为[A]。",
    "正确项\n[A]的信息暗含于第四段最后两句中trejectanything...ymorenoblethanh。": "正确项[A]的信息暗含于第四段最后两句中(reject anything... more noble than)。",
    "正确项[A]的信息暗含于第四段最后两句中trejectanything...ymorenoblethanh。": "正确项[A]的信息暗含于第四段最后两句中(reject anything... more noble than)。",
    "[B]a[D]反向干扰。favoring和suppressing分别对应首句的resen（和末句的：onsideredmore\nnoble[C] 无中生有。": "[B]、[D]反向干扰。favoring和suppressing分别对应首句的resent和末句的considered more noble。[C]无中生有。",

    # Q38
    "38.TheviewsofRavitchandEmersononschooling\nare\n.\n38.拉维奇和爱默生对于学校教育的观点\n是\nM": "38. The views of Ravitch and Emerson on schooling are _______.\n38. 拉维奇和爱默生对于学校教育的观点是：",
    "第二段schoolcouldbeacounterbalance暗含拉维奇对学校作用的期望：学校应该\n扭转美国对才智的厌恶，由此可知，拉维奇是赞同学校教育的；第五段中putunnaturalrestraintsydo\nnotknowathing则体现了Emerson对学校教育持完全否定态度。故[D]正确。": "第二段school could be a counterbalance暗含拉维奇对学校作用的期望：学校应该扭转美国对才智的厌恶，由此可知，拉维奇是赞同学校教育的；第五段中put unnatural restraints, do not know a thing则体现了Emerson对学校教育持完全否定态度。故[D]正确。",

    # Q39
    "39.Emersonyaccordingtothetextyisprobably\n.\n39.根据文章，爱默生可能是\nM": "39. Emerson, according to the text, is probably _______.\n39. 根据文章，爱默生可能是：",
    "[A] apioneerofeducationreform": "[A] a pioneer of education reform",
    "[B] anopponentofintellectualism": "[B] an opponent of intellectualism",
    "[C] ascholarinfavorofintellect": "[C] a scholar in favor of intellect",
    "[D] anadvocateofregularschooling": "[D] an advocate of regular schooling",
    "从第五段可推知，爱默生对学校教育和书本知识持否定态度，而它们就是与讲究实\n际a常识和先天的智力不同的才智教育。因此答案是[B]。": "从第五段可推知，爱默生对学校教育和书本知识持否定态度，而它们就是与讲究实际、常识和先天的智力不同的才智教育。因此答案是[B]。",
    "无论从写作目的（第五段Em？\nerson的观点作为论据支持开篇提出的观点“美国轻视才智”h还是否定性的词语tunanturalre？\nstraints等）都可以判断出[B]是Emerson的立场。": "无论从写作目的（第五段Emerson的观点作为论据支持开篇提出的观点“美国轻视才智”）还是否定性的词语(unnatural restraints等)都可以判断出[B]是Emerson的立场。",
    "[A]根据“爱默生批判学校教育”的细节做无关联想[C] 反向干扰[D] 与文意相反，爱默生反\n对常规学校教育，认为学校教育禁锢孩子天性": "[A]根据“爱默生批判学校教育”的细节做无关联想。[C]反向干扰。[D]与文意相反，爱默生反对常规学校教育，认为学校教育禁锢孩子天性。",
}

mod_count = 0
for q in data['questions']:
    expl = q.get('explanation', '')
    orig = expl
    for k, v in replacements.items():
        if k in expl:
            expl = expl.replace(k, v)
    if expl != orig:
        q['explanation'] = expl
        mod_count += 1
        print(f"Updated Q{q['question_number']}")

with open(exam_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total 2004 questions updated: {mod_count}")
