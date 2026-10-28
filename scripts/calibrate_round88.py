import json
import os

print("=== Starting Round 88 Calibrations ===")

# 1. Calibrate 2011 ky2 Passage 3 (Text 2) and Q26, Q29
f2011_ky2 = "public/data/exams/53a52573-0afc-51a4-86b6-b2f321cbe6a8.json"
with open(f2011_ky2, "r", encoding="utf-8") as f:
    d2011_ky2 = json.load(f)

# Authentic 5-paragraph text of 2011 ky2 Text 2 from Yellow Book
text2_2011_ky2 = """Whatever happened to the death of newspapers? A year ago the end seemed near. The recession threatened to remove the advertising and readers that had not already fled to the internet. Newspapers like the San Francisco Chronicle were chronicling their own doom. America's Federal Trade Commission launched a round of talks about how to save newspapers. Should they become charitable corporations? Should the state subsidize them? It will hold another meeting soon. But the discussions now seem out of date.

In much of the world there is little sign of crisis. German and Brazilian papers have shrugged off the recession. Even American newspapers, which inhabit the most troubled corner of the global industry, have not only survived but often returned to profit. Not the 20% profit margins that were routine a few years ago, but profit all the same.

It has not been much fun. Many papers stayed afloat by pushing journalists overboard. The American Society of News Editors reckons that 13,500 newsroom jobs have gone since 2007. Readers are paying more for slimmer products. Some papers even had the nerve to refuse delivery to distant suburbs. Yet these desperate measures have proved the right ones and, sadly for many journalists, they can be pushed further.

Newspapers are becoming more balanced businesses, with a healthier mix of revenues from readers and advertisers. American papers have long been highly unusual in their reliance on ads. Fully 87% of their revenues came from advertising in 2008, according to the Organization for Economic Cooperation & Development (OECD). In Japan the proportion is 35%. Not surprisingly, Japanese newspapers are much more stable.

The whirlwind that swept through newsrooms harmed everybody, but much of the damage has been concentrated in areas where newspapers are least distinctive. Car and film reviewers have gone. So have science and general business reporters. Foreign bureaus have been savagely cut off. Newspapers are less complete as a result. But completeness is no longer a virtue in the newspaper business."""

for p in d2011_ky2.get("passages", []):
    if p.get("sort_order") == 3:
        p["content"] = text2_2011_ky2
        print("Updated 2011 ky2 Passage 3 with authentic 5-paragraph Yellow Book text (329 words).")

for q in d2011_ky2.get("questions", []):
    if q.get("sort_order") == 26:
        q["stem"] = 'By saying "Newspapers like... their own doom" (Lines 3-4, Para. 1), the author indicates that newspapers'
        print("Standardized 2011 ky2 Q26 stem ellipsis.")
    elif q.get("sort_order") == 29:
        for opt in q.get("options", []):
            if opt.get("key") == "B":
                opt["text"] = "Completeness is to blame for the failure of newspapers."
                opt["content"] = "Completeness is to blame for the failure of newspapers."
                print("Corrected 2011 ky2 Q29 opt B typo to 'failure of newspapers.'")

with open(f2011_ky2, "w", encoding="utf-8") as f:
    json.dump(d2011_ky2, f, ensure_ascii=False, indent=2)

out2011 = "out/data/exams/53a52573-0afc-51a4-86b6-b2f321cbe6a8.json"
if os.path.exists(out2011):
    with open(out2011, "w", encoding="utf-8") as f:
        json.dump(d2011_ky2, f, ensure_ascii=False, indent=2)

# 2. Calibrate 2005 ky1 Passage 3 (Text 2)
f2005_ky1 = "public/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json"
with open(f2005_ky1, "r", encoding="utf-8") as f:
    d2005_ky1 = json.load(f)

text2_2005_ky1 = """Do you remember all those years when scientists argued that smoking would kill us but the doubters insisted that we didn't know for sure? That the evidence was inconclusive, the science uncertain? That the antismoking lobby was out to destroy our way of life and the government should stay out of the way? Lots of Americans bought that nonsense, and over three decades, some 10 million smokers went to early graves.

There are upsetting parallels today, as scientists in one wave after another try to awaken us to the growing threat of global warming. The latest was a panel from the National Academy of Sciences, enlisted by the White House, to tell us that the Earth's atmosphere is definitely warming and that the problem is largely man-made. The clear message is that we should get moving to protect ourselves. The president of the National Academy, Bruce Alberts, added this key point in the preface to the panel's report: "Science never has all the answers. But science does provide us with the best available guide to the future, and it is critical that our nation and the world base important policies on the best judgments that science can provide concerning the future consequences of present actions."

Just as on smoking, voices now come from many quarters insisting that the science about global warming is incomplete, that the panel's recommendations are hasty, that we should only conduct more research and avoid any immediate action to restrict greenhouse gases in the air until we know for sure. This is a dangerous game: by the time 100 percent of the evidence is in, it may be too late. With the risks so high, the simplest self-preservation demands that we act now on what we do know.

Fortunately, the White House is starting to pay attention. But it's obvious that a majority of the president's advisers still don't take global warming seriously. Instead of a plan of action, they continue to press for more research — a classic case of "paralysis by analysis."

To serve as responsible stewards of the planet, we must press forward on deeper atmospheric and oceanic research. But research alone is inadequate. If the Administration won't take the legislative initiative, Congress should help to begin fashioning conservation measures. A bill by Democratic Senator Robert Byrd of West Virginia, which would offer financial incentives for private industry, is a promising start. Many see that the country is getting ready to build lots of new power plants to meet our energy needs. If we are ever going to protect the atmosphere, it is crucial that those new plants be environmentally sound."""

for p in d2005_ky1.get("passages", []):
    if p.get("sort_order") == 3:
        p["content"] = text2_2005_ky1
        print("Updated 2005 ky1 Passage 3 with authentic 5-paragraph Yellow Book text (422 words).")

with open(f2005_ky1, "w", encoding="utf-8") as f:
    json.dump(d2005_ky1, f, ensure_ascii=False, indent=2)

out2005 = "out/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json"
if os.path.exists(out2005):
    with open(out2005, "w", encoding="utf-8") as f:
        json.dump(d2005_ky1, f, ensure_ascii=False, indent=2)

print("=== Round 88 Local JSON Calibrations Complete ===")
