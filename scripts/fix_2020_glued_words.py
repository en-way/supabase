import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

exams_file = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams.json"
exams_dir = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

with open(exams_file, "r", encoding="utf-8") as f:
    all_exams_meta = json.load(f)

ky2_map = {e.get("year"): e.get("id") for e in all_exams_meta if e.get("category_id") == "ky2"}

eid_2020 = ky2_map[2020]
fpath_2020 = os.path.join(exams_dir, f"{eid_2020}.json")
with open(fpath_2020, "r", encoding="utf-8") as f:
    d = json.load(f)

# Comprehensive replacement map for 2020 KY2
replacements = {
    # Q1
    "givingalotofusefulinformation": "giving a lot of useful information",
    "aninstructiveexperience": "an instructive experience",
    # Q3
    "=sometimesbutnotoften": "= sometimes but not often",
    # Q7
    "Shedidn'thaveanyformaldance training": "She didn't have any formal dance training",
    "Butdefiningwhatitmeans tobeagoodparentisundoubtedlyverytricky，particularlysincechildren responddifferentlytothesamestyleofparenting.":
        "But defining what it means to be a good parent is undoubtedly very tricky, particularly since children respond differently to the same style of parenting.",
    "Butdefiningwhatitmeans": "But defining what it means",
    "tobeagoodparentisundoubtedlyverytricky": "to be a good parent is undoubtedly very tricky",
    "particularlysincechildren": "particularly since children",
    "responddifferentlytothesamestyleofparenting": "respond differently to the same style of parenting",
    # Q12
    "it'simportanttokeepinmind": "it's important to keep in mind",
    # Q13
    "momentoffatigue": "moment of fatigue",
    "saysomethingtoyourchildthat": "say something to your child that",
    # Q14
    "youcansaysomethingtoyourchildthatyoumayregretforalongtime": "you can say something to your child that you may regret for a long time",
    "theclockandstartover": "the clock and start over",
    "VIfyouconsistentlyloseyour": "If you consistently lose your",
    "inadvertentlymodelinga": "inadvertently modeling a",
    "patiencefor theyoungergeneration.Thisisa skillthatwill": "patience for the younger generation. This is a skill that will",
    "emotionallyregulateormaintain emotionalcontrolwhen": "emotionally regulate or maintain emotional control when",
    # Q20
    "Amorepracticalgoalis totry，tothebestofyourability，tobeastolerantandcomposedasyoucan when facedwith trying situations involvingyour children.":
        "A more practical goal is to try, to the best of your ability, to be as tolerant and composed as you can when faced with trying situations involving your children.",
    "Amorepracticalgoalis": "A more practical goal is",
    "tothebestofyourability": "to the best of your ability",
    "tobeastolerantandcomposedasyoucan": "to be as tolerant and composed as you can",
    "facedwith": "faced with",
    "involvingyour": "involving your",
    # Q21
    "socialsignalsfromroboticrats": "social signals from robotic rats",
    "non-livingbeings": "non-living beings",
    "ITheyhousedeightadultratswith two types": "They housed eight adult rats with two types",
    "Therobotratswerequiteminimalist，": "The robot rats were quite minimalist, ",
    "resemblingachunkierversionofacomputermouse": "resembling a chunkier version of a computer mouse",
    "withwheelstomovearoundandcolourfulmarkings": "with wheels to move around and colourful markings",
    "followedthelivingratsaround，playedwith the same": "followed the living rats around, played with the same",
    "Meanwhile,theasocialrobotsimplymovedforwards": "Meanwhile, the asocial robot simply moved forwards",
    # Q22
    "asocialrobotsimply": "asocial robot simply",
    "socialVSasocial": "social VS asocial",
    "cagesandgavetheratstheopportunitytoreleasethem": "cages and gave the rats the opportunity to release them",
    "thattheratsperceived thesocial robot as agenuinesocial": "that the rats perceived the social robot as a genuine social",
    "socialrobot": "social robot",
    "becauseit": "because it",
    "displayedbehaviourslike": "displayed behaviours like",
    "communalexploringandplaying": "communal exploring and playing",
    "Thiscouldlead to": "This could lead to",
    "theratsbetterrememberinghavingfreeditearlier": "the rats better remembering having freed it earlier",
    "formsofreciprocalhelpandcooperation": "forms of reciprocal help and cooperation",
    "directreciprocitywhere": "direct reciprocity where",
    # Q23
    "wantingtherobottoreturn thefavourwhentheyget": "wanting the robot to return the favour when they get",
    "MThereadinessoftheratstobefriendthesocial": "The readiness of the rats to befriend the social",
    "robotwasthesamesizeasaregularratbutresembleda": "robot was the same size as a regular rat but resembled a",
    "simpleplasticboxonwheels": "simple plastic box on wheels",
    "“We'dassumedwe'd": "\"We'd assumed we'd",
    "have togiveitamovinghead": "have to give it a moving head",
    "QueenslandinAustralia,whohelpedwiththeresearch": "Queensland in Australia, who helped with the research",
    # Q26
    "IToday'sCEO,atleastformajorAmericanfirms，": "Today's CEO, at least for major American firms, ",
    "Today'sCEO,atleastformajorAmericanfirms": "Today's CEO, at least for major American firms",
    "financialmarketsandmaybeevenhow thecompanyshould": "financial markets and maybe even how the company should",
    "slipupcanbesignificant": "slip up can be significant",
    "knowledgethatisfairlymind-boggling": "knowledge that is fairly mind-boggling",
    "CEOsstillhavetodoalltheday-to-dayworktheyhave": "CEOs still have to do all the day-to-day work they have",
    # Q28
    "corporategovernance...tighterandmore": "corporate governance... tighter and more",
    # Q29
    "highCEOpayisnotsomekindofdepredation": "high CEO pay is not some kind of depredation",
    # Q30
    "CEOsreallyhaveupped theirgame": "CEOs really have upped their game",
    "attheexpenseoftherestofthecompany": "at the expense of the rest of the company",
    "buildupcorporatevalue": "build up corporate value",
    # Q31
    "successinimprovingairquality": "success in improving air quality",
    "That'sbecausetheyinevitablyput": "That's because they inevitably put",
    "on tothe carmanufacturerswhosecheatingis the": "on to the car manufacturers whose cheating is the",
    # Q32
    "ratherthanontothecarmanufacturers": "rather than on to the car manufacturers",
    "ontoAratherthanontoB": "onto A rather than onto B",
    # Q33
    "VButmayorsandcouncilorscan onlydoso": "But mayors and councilors can only do so",
    "Theyare actingbecausenational": "They are acting because national",
    # Q34
    "nationalgovernments...havefailedtodoso": "national governments... have failed to do so",
    "mayorsandcouncils": "mayors and councils",
    # Q35
    "doingeverythingbutinsistthat": "doing everything but insist that",
    "ofalargereffort": "of a larger effort",
    "doingeverythingbutinsist": "doing everything but insist",
    # Q36
    "whenmanyoftheirparentslosttheirjobsortheir": "when many of their parents lost their jobs or their",
    "done little to assuagethis underlyinggenerational sense": "done little to assuage this underlying generational sense",
    # Q38
    "thisunderlyinggenerationalsenseofanxiousurgency": "this underlying generational sense of anxious urgency",
    "One surveyfromAccenturefoundthat 88": "One survey from Accenture found that 88",
    "percent of graduatingseniorsthisyear chose theirmajor": "percent of graduating seniors this year chose their major",
    "mostdesirabletraitinafutureemployerwastheability": "most desirable trait in a future employer was the ability",
    "tooffersecureemployment（followedbyprofessional": "to offer secure employment (followed by professional",
    "followedbyprofessional": "followed by professional",
    # Q39
    "followedbyprofessional...training": "followed by professional... training",
    # Q45
    "Putyourselvesinothers’shoes": "Put yourselves in others' shoes",
    "Considertheper": "Consider the per..."
}

fixes_count = 0
for q in d["questions"]:
    expl = q.get("explanation", "")
    old_expl = expl
    for target, rep in replacements.items():
        if target in expl:
            expl = expl.replace(target, rep)
            fixes_count += 1
    if expl != old_expl:
        q["explanation"] = expl
        print(f"Fixed glued words in 2020 Q{q['question_number']}")

with open(fpath_2020, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"\nTotal replacements applied to 2020 KY2: {fixes_count}")
