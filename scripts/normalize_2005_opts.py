# -*- coding: utf-8 -*-
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Normalizing 2005 ky1 options schema key == value ===")

PART_B_OPTIONS = [
    {
        "key": "A",
        "value": "A",
        "text": "Quebec's resistance to a national agency is provincialist ideology. One of the first advocates for a national list was a researcher at Laval University. Quebec's Drug Insurance Fund has seen its costs skyrocket with annual increases from 14.3 per cent to 26.8 per cent!",
        "content": "Quebec's resistance to a national agency is provincialist ideology. One of the first advocates for a national list was a researcher at Laval University. Quebec's Drug Insurance Fund has seen its costs skyrocket with annual increases from 14.3 per cent to 26.8 per cent!"
    },
    {
        "key": "B",
        "value": "B",
        "text": 'Or they could read Mr. Kirby\'s report: "the substantial buying power of such an agency would strengthen the public prescription-drug insurance plans to negotiate the lowest possible purchase prices from drug companies".',
        "content": 'Or they could read Mr. Kirby\'s report: "the substantial buying power of such an agency would strengthen the public prescription-drug insurance plans to negotiate the lowest possible purchase prices from drug companies".'
    },
    {
        "key": "C",
        "value": "C",
        "text": 'What does "national" mean? Roy Romanow and Senator Michael Kirby recommended a federal-provincial body much like the recently created National Health Council.',
        "content": 'What does "national" mean? Roy Romanow and Senator Michael Kirby recommended a federal-provincial body much like the recently created National Health Council.'
    },
    {
        "key": "D",
        "value": "D",
        "text": "The problem is simple and stark: health care costs have been, are, and will continue to increase faster than government revenues.",
        "content": "The problem is simple and stark: health care costs have been, are, and will continue to increase faster than government revenues."
    },
    {
        "key": "E",
        "value": "E",
        "text": "According to the Canadian Institute for Health Information, prescription drug costs have risen since 1997 at twice the rate of overall health-care spending. Part of the increase comes from drugs being used to replace other kinds of treatments. Part of it arises from new drugs costing more than older kinds. Part of it is higher prices.",
        "content": "According to the Canadian Institute for Health Information, prescription drug costs have risen since 1997 at twice the rate of overall health-care spending. Part of the increase comes from drugs being used to replace other kinds of treatments. Part of it arises from new drugs costing more than older kinds. Part of it is higher prices."
    },
    {
        "key": "F",
        "value": "F",
        "text": "So, if the provinces want to run the health-care show, they should prove they can run it, starting with an interprovincial health list that would end duplication, save administrative costs, prevent one province from being played off against another, and bargain for better drug prices.",
        "content": "So, if the provinces want to run the health-care show, they should prove they can run it, starting with an interprovincial health list that would end duplication, save administrative costs, prevent one province from being played off against another, and bargain for better drug prices."
    },
    {
        "key": "G",
        "value": "G",
        "text": "Of course, the pharmaceutical companies will scream. They like divided buyers; they can lobby better that way. They can use the threat of removing jobs from one province to another. They can hope that, if one province includes a drug on its list, the pressure will cause others to include it on theirs. They wouldn't like a national agency, but self interest would lead them to deal with it.",
        "content": "Of course, the pharmaceutical companies will scream. They like divided buyers; they can lobby better that way. They can use the threat of removing jobs from one province to another. They can hope that, if one province includes a drug on its list, the pressure will cause others to include it on theirs. They wouldn't like a national agency, but self interest would lead them to deal with it."
    }
]

for ddir in ['public/data/exams', 'out/data/exams']:
    fpath = os.path.join(ddir, 'd8ba7d14-5305-538d-b81b-f0f7ef3db461.json')
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for q in data['questions']:
        if q.get('sort_order') in [41, 42, 43, 44, 45]:
            q['options'] = PART_B_OPTIONS
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated options in {fpath}")

print("Normalized options successfully!")
