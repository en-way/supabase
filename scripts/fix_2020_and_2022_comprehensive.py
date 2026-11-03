import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 1. FIX 2022 KY2 (cc4bf627-e456-538f-87e2-4a99ebb613ed.json)
p2022 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\cc4bf627-e456-538f-87e2-4a99ebb613ed.json"
with open(p2022, "r", encoding="utf-8") as f:
    d2022 = json.load(f)

for q in d2022["questions"]:
    qn = q["question_number"]
    expl = q.get("explanation", "")
    
    # Q3: remove trailing page number 2
    if qn == 3 and expl.strip().endswith("\n2"):
        q["explanation"] = expl.strip()[:-2].rstrip()
        print("2022 Q3: removed trailing page number '2'")
        
    # Q34: addressslowlyat -> address slowly at
    if qn == 34 and "addressslowlyat" in expl:
        q["explanation"] = expl.replace("addressslowlyat", "address slowly at")
        print("2022 Q34: replaced addressslowlyat -> address slowly at")
        
    # Q42: back offGo easier -> back off, Go easier
    if qn == 42 and "back offGo easier" in expl:
        q["explanation"] = expl.replace("back offGo easier", "back off / Go easier")
        print("2022 Q42: replaced back offGo easier -> back off / Go easier")

with open(p2022, "w", encoding="utf-8") as f:
    json.dump(d2022, f, ensure_ascii=False, indent=2)

print("Saved 2022 KY2 fixes.")

# 2. FIX 2020 KY2 (ee996af1-3aaa-5380-9465-08125c4db713.json)
p2020 = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json"
with open(p2020, "r", encoding="utf-8") as f:
    d2020 = json.load(f)

replacements_2020 = [
    # Trailing page numbers & divider cleanups
    (1, "\n1\n", "\n"),
    (1, "\n1$", ""),
    (7, "结构切分：\n3", "【结构切分】[But defining what it means to be a good parent is undoubtedly very tricky]（主句），[particularly since children respond differently to the same style of parenting]（原因状语从句）。"),
    (7, "\n3$", ""),
    (8, "\n4$", ""),
    (15, "\n7$", ""),
    (20, "\n结构切分：\n9\n\n====================", "\n【结构切分】A more practical goal is [to try, to the best of your ability, to be as tolerant and composed as you can]（不定式作表语，含插入语 to the best of your ability） [when faced with trying situations involving your children]（时间状语从句分词省略结构）。"),
    (20, "［考点提炼］上下文语义十动词辨析。", "［考点提炼］上下文语义+动词辨析。"),
    (25, "\n18$", ""),
    (29, "\n26$", ""),
    (35, "\n37$", ""),
    (45, "\n53$", ""),

    # Q20 vocab and text fixes
    (20, "①incredibly[inkredabli]ad.难以置信地；极其\nS\n④composed[kampauzd]a.镇静的；沉着的\n②practical['prektikl]a.实际的，务实的\nbefaced with面对；面临\n③tothebest尽全力\nasaresultof由于；作为....的结果",
         "① incredibly [ɪnˈkredəbli] adv. 难以置信地；极其\n② practical [ˈpræktɪkl] adj. 实际的，务实的\n③ to the best 尽全力\n④ composed [kəmˈpəʊzd] adj. 镇静的；沉着的\n• be faced with 面对；面临\n• as a result of 由于；作为……的结果"),
    (20, "A more practical goal is totry，to the best of your ability，to be as tolerant and composed as you can\nwhen faced with trying situations involving your children.",
         "A more practical goal is to try, to the best of your ability, to be as tolerant and composed as you can when faced with trying situations involving your children."),
    (20, "Amorepracticalgoal", "A more practical goal"),
    (20, "fromstressfulmoments", "from stressful moments"),
    (20, "promiseyou\nthis", "promise you this"),
    (20, "Asaresult...thisgoal", "As a result... this goal"),

    # Glued tokens across questions
    (1, "definingwhatitmeansto", "defining what it means to"),
    (1, "particularlysince", "particularly since"),
    (1, "difficulttodoordealwith", "difficult to do or deal with"),
    (1, "apleasantenvironment", "a pleasant environment"),

    (2, "followingchild", "following child"),
    (2, "childrenresponddifferently", "children respond differently"),
    (2, "theirinstruments", "their instruments"),
    (2, "andmusichistory", "and music history"),
    (2, "ayoungersibling", "a younger sibling"),
    (2, "Comehereatonce", "Come here at once"),
    (2, "tallspeakatonce", "t all speak at once"),
    (2, "Helengotintoacting", "Helen got into acting"),
    (2, "purelybyaccident", "purely by accident"),

    (3, "trickyVSeasier", "tricky VS easier"),
    (3, "toolongandtheeditoraccordinglycutitby", "too long and the editor accordingly cut it by"),

    (4, "Theapplesarehardtoreach", "The apples are hard to reach"),

    (6, "haveeasyaccesstoinformation", "have easy access to information"),

    (7, "thaveanyformaldance", "t have any formal dance"),
    (7, "criticalcomments", "critical comments"),

    (10, "screamatyourkids", "scream at your kids"),
    (10, "doesnobodyanygood", "does nobody any good"),

    (11, "doesnobodyanygood", "does nobody any good"),
    (11, "turnbacktheclock", "turn back the clock"),

    (12, "tobecomeanactor", "to become an actor"),
    (12, "w.Instead", "w. Instead"),

    (14, "Sometimesparents", "Sometimes parents"),
    (14, "Thismaynotonly", "This may not only"),
    (14, "exhaustedandfrustrated", "exhausted and frustrated"),
    (14, "increasinglyawareofthe", "increasingly aware of the"),
    (14, "ofmodelingtoleranceand", "of modeling tolerance and"),
    (14, "fatigue.Ina", "fatigue. In a"),

    (16, "throughoutlife", "throughout life"),
    (16, "thebasicqualities", "the basic qualities"),

    (17, "beconfrontedbysth", "be confronted by sth."),

    (19, "situationsinvolving", "situations involving"),
    (19, "Iunderstandthis", "I understand this"),
    (19, "veallbeenthere", "'ve all been there"),

    (21, "identifyfriends", "identify friends"),
    (21, "needtobehighlyattunedto", "need to be highly attuned to"),
    (21, "specialtraining", "special training"),
    (21, "Tofindoutifthisextendsto", "To find out if this extends to"),
    (21, "whetherratscan", "whether rats can"),
    (21, "animals.The", "animals. The"),

    (22, "duringtheexperiment", "during the experiment"),
    (22, "Duringtheexperiment", "During the experiment"),
    (22, "centmorelikelyon", "cent more likely on"),
    (22, "therobottoreturn", "the robot to return"),
    (22, "cues.Across", "cues. Across"),
    (22, "cooperate.This", "cooperate. This"),
    (22, "session.The", "session. The"),
    (22, "training.This", "training. This"),

    (23, "releasethembypressingalever", "release them by pressing a lever"),
    (23, "displayedbehaviours", "displayed behaviours"),
    (23, "facialfeatures", "facial features"),
    (23, "JanetWiles at theUniversityof", "Janet Wiles at the University of"),
    (23, "anetWiles", "anet Wiles"),
    (23, "theUniversityof", "the University of"),
    (23, "cues.Similarly", "cues. Similarly"),
    (23, "direction.The", "direction. The"),

    (24, "JanetWiles", "Janet Wiles"),

    (25, "Thereadinessoftherats", "The readiness of the rats"),
    (25, "aretosocialcues", "are to social cues"),
    (25, "WhyCEOsActuallyDeserveTheirGazillion\nDollarSalaries", "Why CEOs Actually Deserve Their Gazillion Dollar Salaries"),
    (25, "WhyCEOsActuallyDeserveTheirGazillionDollarSalaries", "Why CEOs Actually Deserve Their Gazillion Dollar Salaries"),

    (26, "Thebestmodelforunderstanding", "The best model for understanding"),
    (26, "dynamicelements", "dynamic elements"),
    (26, "simplybeingableto", "simply being able to"),
    (26, "Theyalsoneedbetterpublicrelations", "They also need better public relations"),
    (26, "largeAmerican", "large American"),
    (26, "majorAmerican", "major American"),
    (26, "point.Thenthere", "point. Then there"),
    (26, "companies.Tolead", "companies. To lead"),
    (26, "running.Plus", "running. Plus"),
    (26, "manner.Beyond", "manner. Beyond"),

    (27, "operatemoreglobalizedcompanies", "operate more globalized companies"),
    (27, "haveagoodsenseof", "have a good sense of"),
    (27, "manymoreskills", "many more skills"),

    (28, "corporategovernancehasbecomealottighter", "corporate governance has become a lot tighter"),
    (28, "andmorerigorous", "and more rigorous"),
    (28, "duringthisperiodof", "during this period of"),
    (28, "strongergovernance", "stronger governance"),

    (29, "buildupcorporate", "build up corporate"),
    (29, "canbejustified", "can be justified"),
    (29, "itisinthebroadercorporateinterestto", "it is in the broader corporate interest to"),

    (30, "CEOpayhasgoneup", "CEO pay has gone up"),
    (30, "limitedCEOtalent", "limited CEO talent"),
    (30, "Today'sCEO", "Today's CEO"),

    (31, "yettobedecided", "yet to be decided"),
    (31, "futurelooksuncertain", "future looks uncertain"),
    (31, "tougherenforcement", "tougher enforcement"),
    (31, "buybettervehicles", "buy better vehicles"),
    (31, "toxicpollution", "toxic pollution"),

    (32, "puttoomuchburdenonindividualmotorists", "put too much burden on individual motorists"),
    (32, "ratherthanontoB", "rather than onto B"),
    (32, "politicallycontentious", "politically contentious"),
    (32, "Amongotherweaknesses", "Among other weaknesses"),
    (32, "individualmotorists", "individual motorists"),
    (32, "putthecosts...ontoA...ratherthanontoB", "put the costs... onto A... rather than onto B"),
    (32, "ontoA", "onto A"),
    (32, "areA", "are A"),

    (33, "strongresistance", "strong resistance"),
    (33, "sparkintenseopposition", "spark intense opposition"),
    (33, "thatisfarbigger", "that is far bigger"),

    (34, "localresidents", "local residents"),
    (34, "mayorsandcouncilors", "mayors and councilors"),
    (34, "AareactingbecauseB...havefailedtodoso", "A are acting because B... have failed to do so"),
    (34, "areactingbecauseB", "are acting because B"),
    (34, "havefailedtodoso", "have failed to do so"),
    (34, "nationalgovernments", "national governments"),

    (35, "requireautocompanies", "require auto companies"),
    (35, "tobringtheirvehiclesintocompliance", "to bring their vehicles into compliance"),
    (35, "properlyenforce", "properly enforce"),
    (35, "bringintocompliance", "bring into compliance"),

    (36, "theattentionhasbeenrisingsteadilyinrecentweeks", "the attention has been rising steadily in recent weeks"),
    (36, "graduatinginto", "graduating into"),
    (36, "Theywereimpressionablekidsduringthecrashof", "They were impressionable kids during the crash of"),
    (36, "theFederalReserve", "the Federal Reserve"),
    (36, "theFederal", "the Federal"),
    (36, "theU.S.", "the U.S."),
    (36, "theU", "the U"),
    (36, "factors.According", "factors. According"),
    (36, "decades.Despite", "decades. Despite"),
    (36, "crash.They", "crash. They"),
    (36, "loans.The", "loans. The"),
    (36, "debt.College", "debt. College"),

    (37, "whatatougheconomicsituationislike", "what a tough economic situation is like"),
    (37, "whataneconomictrainwrecklookslike", "what an economic train wreck looks like"),
    (37, "GenerationZsarekeenlyaware", "Generation Zs are keenly aware"),
    (37, "enerationZsarekeenlyaware", "Generation Zs are keenly aware"),
    (37, "GenZsknow", "Gen Zs know"),
    (37, "enZsknow", "Gen Zs know"),

    (38, "Theboomingeconomy", "The booming economy"),
    (38, "seemstohavedonelittleto", "seems to have done little to"),
    (38, "thisunderlyinggenerationalsenseof", "this underlying generational sense of"),
    (38, "anxiousurgency", "anxious urgency"),
    (38, "withajobinmind.Ina2019surveyofUniversityof", "with a job in mind. In a 2019 survey of University of"),
    (38, "withajobinmind", "with a job in mind"),
    (38, "surveyofUniversityof", "survey of University of"),
    (38, "Ina2019", "In a 2019"),
    (38, "d.Ina", "d. In a"),
    (38, "careerofficefound", "career office found"),
    (38, "inspiringpurpose", "inspiring purpose"),
    (38, "Jobsecurityorstabilitywasthesecondmostimportant", "Job security or stability was the second most important"),

    (39, "chosetheirmajorwithajobinmind", "chose their major with a job in mind"),

    (40, "lookingformorecertaintyandstability", "looking for more certainty and stability"),
    (40, "quiteriskaverse", "quite risk averse"),
    (40, "inspiringpurpose", "inspiring purpose"),
    (40, "senseofbeingdedicatedtoacause", "sense of being dedicated to a cause"),
    (40, "GenerationsZs", "Generation Zs"),
    (40, "enerationsZs", "Generation Zs"),

    (42, "Givecompliments", "Give compliments"),
    (42, "justnottoomany", "just not too many"),
    (42, "tellothershowwefeel", "tell others how we feel")
]

applied_count = 0
for q in d2020["questions"]:
    qn = q["question_number"]
    expl = q.get("explanation", "")
    orig = expl
    for target_qn, target_str, rep in replacements_2020:
        if target_qn == qn:
            if target_str.startswith("\n") and target_str.endswith("$"):
                # trailing regex pattern
                num = target_str[1:-1]
                if expl.strip().endswith("\n" + num):
                    expl = expl.strip()[:-len(num)].rstrip()
                    print(f"2020 Q{qn}: removed trailing number {num}")
                    applied_count += 1
            elif target_str in expl:
                expl = expl.replace(target_str, rep)
                print(f"2020 Q{qn}: replaced '{target_str[:25]}...' -> '{rep[:25]}...'")
                applied_count += 1
    q["explanation"] = expl

with open(p2020, "w", encoding="utf-8") as f:
    json.dump(d2020, f, ensure_ascii=False, indent=2)

print(f"Saved 2020 KY2 fixes! Total replacements applied: {applied_count}")
