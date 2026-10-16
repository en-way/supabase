import json
import glob

exams = sorted(glob.glob('public/data/exams/*.json'))

targets = [
    (2021, 'ky1'),
    (2009, 'ky1'),
    (2008, 'ky1'),
    (2007, 'ky1'),
    (2006, 'ky1')
]

for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data['exam']
    year = exam['year']
    cat = exam['category_id']
    if (year, cat) in targets:
        print(f"\n==================== {year} {cat} ====================")
        for q in data['questions']:
            q_num = q['sort_order']
            opts = q.get('options', [])
            # Print any question where an option looks truncated or has intra-word spacing
            suspicious = False
            for o in opts:
                t = o.get('text', '')
                if any(x in t for x in [' b se ', ' ta bl ', ' e ne ra ', ' a rdl ', ' l em e ', ' l oca ', ' sco r', ' eakag', 'odds w', 'process il', ' the sp', ' keep th', ' ch anc', ' ubli s', ' rms will', ' by ge', 'that will', 'decision is']):
                    suspicious = True
                    break
            if suspicious:
                print(f"--- Q{q_num} (Answer: {q.get('correct_answer')}) ---")
                print(f"Stem: {q.get('stem')}")
                for o in opts:
                    print(f"  [{o['key']}]: {o['text']}")
                print(f"Analysis snippet: {q.get('explanation', '')[:120]}...\n")
