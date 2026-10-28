import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 85 Calibration: 2005 ky1 Text Reconstruction & 2012 ky1 Sort Order ===")

# 1. 2005 ky1 clean texts
P1_CONTENT = """The human nose is an underrated tool. Humans are often thought to be insensitive smellers compared with animals, [1] this is largely because, [2] animals, we stand upright. This means that our noses are [3] to perceiving those smells which float through the air, [4] the majority of smells which stick to surfaces. In fact, [5], we are extremely sensitive to smells, [6] we do not generally realize it. Our noses are capable of [7] human smells even when these are [8] to far below one part in one million.

Strangely, some people find that they can smell one type of flower but not another, [9] others are sensitive to the smells of both flowers. This may be because some people do not have the genes necessary to generate [10] smell receptors in the nose. These receptors are the cells which sense smells and send [11] to the brain. However, it has been found that even people insensitive to a certain smell [12] can suddenly become sensitive to it when [13] to it often enough.

The explanation for insensitivity to smells seems to be that the brain finds it [14] to keep all smell receptors working all the time but can [15] new receptors if necessary. This may [16] explain why we are not usually [17] of the usual smell of our own house, but we [18] new smells when we visit someone else's. The brain finds it best to keep smell receptors [19] for unfamiliar and emergency signals [20] the smell of smoke, which might indicate the danger of fire."""

P2_CONTENT = """Everybody loves a fat pay rise. Yet pleasure at your own can vanish if you learn that a colleague has been given a bigger one. Indeed, if he has a reputation for slacking, you might even be outraged. Such behaviour is regarded as "all too human", with the underlying assumption that other animals would not be capable of this finely developed sense of grievance. But a study by Sarah Brosnan and Frans de Waal of Emory University in Atlanta, Georgia, which has just been published in Nature, suggests that it is all too monkey, as well.

The researchers studied the behaviour of female brown capuchin monkeys. They look cute. They are good-natured, co-operative creatures, and they share their food readily. Above all, like their female human counterparts, they tend to pay much closer attention to the value of "goods and services" than males. Such characteristics make them perfect candidates for Dr. Brosnan's and Dr. de Waal's study.

The researchers spent two years teaching their monkeys to exchange tokens for food. Normally, the monkeys were happy enough to exchange pieces of rock for slices of cucumber. However, when two monkeys were placed in separate but adjoining chambers, so that each could observe what the other was getting in return for its rock, their behaviour became markedly different.

In the world of capuchins, grapes are luxury goods (and much preferable to cucumbers). So when one monkey was handed a grape in exchange for her token, the second was reluctant to hand hers over for a mere piece of cucumber. And if one received a grape without having to provide her token in exchange at all, the other either tossed her own token at the researcher or out of the chamber, or refused to accept the slice of cucumber. Indeed, the mere presence of a grape in the other chamber (without an actual monkey to eat it) was enough to induce resentment in a female capuchin.

The researchers suggest that capuchin monkeys, like humans, are guided by social emotions. In the wild, they are a co-operative, group-living species. Such co-operation is likely to be stable only when each animal feels it is not being cheated. Feelings of righteous indignation, it seems, are not the preserve of people alone. Refusing a lesser reward completely makes these feelings abundantly clear to other members of the group. However, whether such a sense of fairness evolved independently in capuchins and humans, or whether it stems from the common ancestor that the species had 35 million years ago, is, as yet, an unanswered question."""

P4_CONTENT = """Of all the components of a good night's sleep, dreams seem to be least within our control. In dreams, a window opens into a world where logic is suspended and dead people speak. A century ago, Freud formulated his revolutionary theory that dreams were the disguised shadows of our unconscious desires and fears; by the late 1970s, neurologists had switched to thinking of them as just "mental noise"—the random byproducts of the neural-repair work that goes on during sleep. Now researchers suspect that dreams are part of the mind's emotional thermostat, regulating moods while the brain is "off-line". And one leading authority says that these intensely powerful mental events can be not only harnessed but actually brought under conscious control, to help us sleep and feel better. "It's your dream," says Rosalind Cartwright, chair of psychology at Chicago's Medical Center. "If you don't like it, change it."

Evidence from brain imaging supports this view. The brain is as active during REM (rapid eye movement) sleep—when most vivid dreams occur—as it is when fully awake, says Dr. Eric Nofzinger at the University of Pittsburgh. But not all parts of the brain are equally involved; the limbic system (the "emotional brain") is especially active, while the prefrontal cortex (the center of intellect and reasoning) is relatively quiet. "We wake up from dreams happy or depressed, and those feelings can stay with us all day," says Stanford sleep researcher Dr. William Dement.

The link between dreams and emotions shows up among the patients in Cartwright's clinic. Most people seem to have more bad dreams early in the night, progressing toward happier ones before awakening, suggesting that they are working through negative feelings generated during the day. Because our conscious mind is occupied with daily life we don't always think about the emotional significance of the day's events—until, it appears, we begin to dream.

And this process need not be left to the unconscious. Cartwright believes one can exercise conscious control over recurring bad dreams. As soon as you awaken, identify what is upsetting about the dream. Visualize how you would like it to end instead; the next time it occurs, try to wake up just enough to control its course. With much practice people can learn to, literally, do it in their sleep.

At the end of the day, there's probably little reason to pay attention to our dreams at all unless they keep us from sleeping or "we wake up in a panic," Cartwright says. Terrorism, economic uncertainties and general feelings of insecurity have increased people's anxiety. Those suffering from persistent nightmares should seek help from a therapist. For the rest of us, the brain has its ways of working through bad feelings. Sleep—or rather dream—on it and you'll feel better in the morning."""

P6_CONTENT = """Canada’s premiers (the leaders of provincial governments), if they have any breath left after complaining about Ottawa at their late July annual meeting, might spare a moment to do something, together, to reduce health care costs.

They’re all groaning about soaring health budgets, the fastest-growing component of which are pharmaceutical costs.

[41]

What to do? Both the Romanow commission and the Kirby committee on health care—to say nothing of reports from other experts—recommended the creation of a national drug agency. Instead of each province having its own list of approved drugs, bureaucracy, procedures and limited bargaining power, all would pool resources, work with Ottawa, and create a national institution.

[42]

But "national" doesn't have to mean that. "National" could mean interprovincial—provinces combining efforts to create one body.

Either way, one benefit of a "national" organization would be to negotiate better prices, if possible, with drug manufacturers. Instead of having one province—or a series of hospitals within a province—negotiate a price for a given drug on the provincial list, the national agency would negotiate on behalf of all provinces.

Rather than, say, Quebec, negotiating on behalf of seven million people, the national agency would negotiate on behalf of 31 million people. Basic economics suggests the greater the potential consumers, the higher the likelihood of a better price.

[43]

A small step has been taken in the direction of a national agency with the creation of the Canadian Co-ordinating Office for Health Technology Assessment, funded by Ottawa and the provinces. Under it, a Common Drug Review recommends to provincial lists which new drugs should be included. Predictably, and regrettably, Quebec refused to join.

A few premiers are suspicious of any federal-provincial deal-making. They (particularly Quebec and Alberta) just want Ottawa to fork over additional billions with few, if any, strings attached. That’s one reason why the idea of a national list hasn’t gone anywhere while drug costs keep rising fast.

[44]

Premiers love to quote Mr. Romanow’s report selectively, especially the parts about more federal money. Perhaps they should read what he had to say about drugs: "A national drug agency would provide governments more influence on pharmaceutical companies in order to try to constrain the ever increasing cost of drugs."

[45]

So when the premiers gather in Niagara Falls to assemble their usual complaint list, they should also get cracking about something in their jurisdiction that would help their budgets and patients."""

PART_B_OPTIONS = [
    {
        "key": "A",
        "value": "Quebec's resistance to a national agency is provincialist ideology. One of the first advocates for a national list was a researcher at Laval University. Quebec's Drug Insurance Fund has seen its costs skyrocket with annual increases from 14.3 per cent to 26.8 per cent!",
        "text": "Quebec's resistance to a national agency is provincialist ideology. One of the first advocates for a national list was a researcher at Laval University. Quebec's Drug Insurance Fund has seen its costs skyrocket with annual increases from 14.3 per cent to 26.8 per cent!",
        "content": "Quebec's resistance to a national agency is provincialist ideology. One of the first advocates for a national list was a researcher at Laval University. Quebec's Drug Insurance Fund has seen its costs skyrocket with annual increases from 14.3 per cent to 26.8 per cent!"
    },
    {
        "key": "B",
        "value": 'Or they could read Mr. Kirby\'s report: "the substantial buying power of such an agency would strengthen the public prescription-drug insurance plans to negotiate the lowest possible purchase prices from drug companies".',
        "text": 'Or they could read Mr. Kirby\'s report: "the substantial buying power of such an agency would strengthen the public prescription-drug insurance plans to negotiate the lowest possible purchase prices from drug companies".',
        "content": 'Or they could read Mr. Kirby\'s report: "the substantial buying power of such an agency would strengthen the public prescription-drug insurance plans to negotiate the lowest possible purchase prices from drug companies".'
    },
    {
        "key": "C",
        "value": 'What does "national" mean? Roy Romanow and Senator Michael Kirby recommended a federal-provincial body much like the recently created National Health Council.',
        "text": 'What does "national" mean? Roy Romanow and Senator Michael Kirby recommended a federal-provincial body much like the recently created National Health Council.',
        "content": 'What does "national" mean? Roy Romanow and Senator Michael Kirby recommended a federal-provincial body much like the recently created National Health Council.'
    },
    {
        "key": "D",
        "value": "The problem is simple and stark: health care costs have been, are, and will continue to increase faster than government revenues.",
        "text": "The problem is simple and stark: health care costs have been, are, and will continue to increase faster than government revenues.",
        "content": "The problem is simple and stark: health care costs have been, are, and will continue to increase faster than government revenues."
    },
    {
        "key": "E",
        "value": "According to the Canadian Institute for Health Information, prescription drug costs have risen since 1997 at twice the rate of overall health-care spending. Part of the increase comes from drugs being used to replace other kinds of treatments. Part of it arises from new drugs costing more than older kinds. Part of it is higher prices.",
        "text": "According to the Canadian Institute for Health Information, prescription drug costs have risen since 1997 at twice the rate of overall health-care spending. Part of the increase comes from drugs being used to replace other kinds of treatments. Part of it arises from new drugs costing more than older kinds. Part of it is higher prices.",
        "content": "According to the Canadian Institute for Health Information, prescription drug costs have risen since 1997 at twice the rate of overall health-care spending. Part of the increase comes from drugs being used to replace other kinds of treatments. Part of it arises from new drugs costing more than older kinds. Part of it is higher prices."
    },
    {
        "key": "F",
        "value": "So, if the provinces want to run the health-care show, they should prove they can run it, starting with an interprovincial health list that would end duplication, save administrative costs, prevent one province from being played off against another, and bargain for better drug prices.",
        "text": "So, if the provinces want to run the health-care show, they should prove they can run it, starting with an interprovincial health list that would end duplication, save administrative costs, prevent one province from being played off against another, and bargain for better drug prices.",
        "content": "So, if the provinces want to run the health-care show, they should prove they can run it, starting with an interprovincial health list that would end duplication, save administrative costs, prevent one province from being played off against another, and bargain for better drug prices."
    },
    {
        "key": "G",
        "value": "Of course, the pharmaceutical companies will scream. They like divided buyers; they can lobby better that way. They can use the threat of removing jobs from one province to another. They can hope that, if one province includes a drug on its list, the pressure will cause others to include it on theirs. They wouldn't like a national agency, but self interest would lead them to deal with it.",
        "text": "Of course, the pharmaceutical companies will scream. They like divided buyers; they can lobby better that way. They can use the threat of removing jobs from one province to another. They can hope that, if one province includes a drug on its list, the pressure will cause others to include it on theirs. They wouldn't like a national agency, but self interest would lead them to deal with it.",
        "content": "Of course, the pharmaceutical companies will scream. They like divided buyers; they can lobby better that way. They can use the threat of removing jobs from one province to another. They can hope that, if one province includes a drug on its list, the pressure will cause others to include it on theirs. They wouldn't like a national agency, but self interest would lead them to deal with it."
    }
]

# Apply to 2005 ky1 in both public and out
for ddir in ['public/data/exams', 'out/data/exams']:
    fpath = os.path.join(ddir, 'd8ba7d14-5305-538d-b81b-f0f7ef3db461.json')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Update passages
    for p in data['passages']:
        so = p.get('sort_order')
        if so == 1:
            p['content'] = P1_CONTENT
        elif so == 2:
            p['content'] = P2_CONTENT
        elif so == 4:
            p['content'] = P4_CONTENT
        elif so == 6:
            p['content'] = P6_CONTENT
            
    # Update questions 41-45
    for q in data['questions']:
        so = q.get('sort_order')
        if so in [41, 42, 43, 44, 45]:
            q['stem'] = f"Choose the best paragraph [A]-[G] that fits into gap [{so}]:"
            q['options'] = PART_B_OPTIONS
            
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated 2005 ky1 in {fpath}")

# Apply 2012 ky1 sort_order fix
for ddir in ['public/data/exams', 'out/data/exams']:
    fpath = os.path.join(ddir, 'baa66182-74ec-5a78-b2d2-077ffdcad9dc.json')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for idx, p in enumerate(data['passages']):
        p['sort_order'] = idx + 1
        
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated 2012 ky1 sort_orders in {fpath}")

print("Local JSON files updated successfully!")
