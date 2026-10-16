import os
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

DATA_DIR = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def make_options(opts_dict):
    """Takes a dict like {'A': 'text', 'B': 'text', ...} and returns list of dicts"""
    return [{'key': k, 'text': opts_dict[k], 'value': k} for k in sorted(opts_dict.keys())]

def load_exam(cat, yr):
    for f in os.listdir(DATA_DIR):
        if not f.endswith('.json'):
            continue
        fp = os.path.join(DATA_DIR, f)
        with open(fp, 'r', encoding='utf-8') as fp_in:
            d = json.load(fp_in)
        exam = d.get('exam', d)
        if exam.get('category_id') == cat and exam.get('year') == yr:
            return f, d
    return None, None

def save_exam(f, data):
    fp = os.path.join(DATA_DIR, f)
    with open(fp, 'w', encoding='utf-8') as fp_out:
        json.dump(data, fp_out, ensure_ascii=False, indent=2)

def update_q(questions, so, stem=None, options=None, ans=None, expl=None):
    for q in questions:
        if q.get('sort_order') == so:
            if stem is not None:
                q['stem'] = stem
            if options is not None:
                if isinstance(options, dict):
                    q['options'] = make_options(options)
                else:
                    q['options'] = options
            if ans is not None:
                q['correct_answer'] = ans
                q['answer'] = ans
            if expl is not None:
                q['explanation'] = expl
            return True
    return False

def clean_watermarks(text):
    if not text:
        return text
    lines = text.split('\n')
    cleaned = [l for l in lines if not any(w in l for w in ['淘宝', '旺旺', '店主', '店铺', '购买正版', '唯一店铺'])]
    return '\n'.join(cleaned)

def run_calibrations():
    print("=== Starting Round 7 Forensic Calibrations (Complete Final Edition) ===")
    total_exams_updated = 0
    total_qs_updated = 0

    # 1. 2001 ky1
    f, d = load_exam('ky1', 2001)
    if d:
        for q in d['questions']:
            if q.get('sort_order') == 39:
                for o in q.get('options', []):
                    if o.get('key') == 'B':
                        o['text'] = o['text'].replace('o£', 'of')
                        total_qs_updated += 1
        save_exam(f, d)
        print("Updated 2001 ky1")
        total_exams_updated += 1

    # 2. 2002 ky1 (watermarks)
    f, d = load_exam('ky1', 2002)
    if d:
        for q in d['questions']:
            if q.get('explanation'):
                q['explanation'] = clean_watermarks(q['explanation'])
        save_exam(f, d)
        print("Updated 2002 ky1")
        total_exams_updated += 1

    # 3. 2006 ky1 (Q4, Q40)
    f, d = load_exam('ky1', 2006)
    if d:
        update_q(d['questions'], 4,
                 options={'A': 'raise', 'B': 'add', 'C': 'take', 'D': 'keep'},
                 ans='A')
        update_q(d['questions'], 40,
                 stem="Which of the following is true of the text?",
                 options={
                     'A': 'Religion once functioned as a reminder of misery.',
                     'B': 'Art provides a balance between expectation and reality.',
                     'C': 'People feel disappointed at the realities of modern society.',
                     'D': 'Mass media are inclined to cover disasters and deaths.'
                 },
                 ans='A')
        save_exam(f, d)
        print("Updated 2006 ky1 (Q4, Q40)")
        total_exams_updated += 1
        total_qs_updated += 2

    # 4. 2007 ky1 (Q7)
    f, d = load_exam('ky1', 2007)
    if d:
        update_q(d['questions'], 7,
                 options={'A': 'unique', 'B': 'common', 'C': 'particular', 'D': 'typical'},
                 ans='B')
        save_exam(f, d)
        print("Updated 2007 ky1 (Q7)")
        total_exams_updated += 1
        total_qs_updated += 1

    # 5. 2008 ky1 (Q4, Q8, Q11)
    f, d = load_exam('ky1', 2008)
    if d:
        update_q(d['questions'], 4,
                 options={'A': 'subsequently', 'B': 'presently', 'C': 'previously', 'D': 'lately'},
                 ans='C')
        update_q(d['questions'], 8,
                 options={'A': '(in) progress', 'B': '(in) fact', 'C': '(in) need', 'D': '(in) question'},
                 ans='D')
        update_q(d['questions'], 11,
                 options={'A': 'unconsciously', 'B': 'disproportionately', 'C': 'indefinitely', 'D': 'unaccountably'},
                 ans='B')
        save_exam(f, d)
        print("Updated 2008 ky1 (Q4, Q8, Q11)")
        total_exams_updated += 1
        total_qs_updated += 3

    # 6. 2009 ky1 (Q4, Q8, Q12)
    f, d = load_exam('ky1', 2009)
    if d:
        update_q(d['questions'], 4,
                 options={'A': 'tendency', 'B': 'advantage', 'C': 'inclination', 'D': 'priority'},
                 ans='B')
        update_q(d['questions'], 8,
                 options={'A': 'fight', 'B': 'doubt', 'C': 'stop', 'D': 'think'},
                 ans='C')
        update_q(d['questions'], 12,
                 options={'A': 'outside', 'B': 'on', 'C': 'by', 'D': 'across'},
                 ans='B')
        save_exam(f, d)
        print("Updated 2009 ky1 (Q4, Q8, Q12)")
        total_exams_updated += 1
        total_qs_updated += 3

    # 7. 2010 ky1 (Q26, Q33, Q36, Q40)
    f, d = load_exam('ky1', 2010)
    if d:
        update_q(d['questions'], 26,
                 options={
                     'A': 'their emotional problems',
                     'B': 'their connection with asset allocation',
                     'C': 'their misunderstanding of market trends',
                     'D': 'their risk-mitigating strategies'
                 },
                 ans='B')
        for q in d['questions']:
            if q.get('sort_order') == 33:
                for o in q.get('options', []):
                    o['text'] = o['text'].replace('o£', 'of')
            if q.get('sort_order') == 36:
                q['stem'] = "Bankers complained that they were forced to"
        update_q(d['questions'], 40,
                 stem="The author's attitude towards standard-setters is one of",
                 options={
                     'A': 'satisfaction',
                     'B': 'skepticism',
                     'C': 'objectiveness',
                     'D': 'sympathy'
                 },
                 ans='D')
        save_exam(f, d)
        print("Updated 2010 ky1 (Q26, Q33, Q36, Q40)")
        total_exams_updated += 1
        total_qs_updated += 4

    # 8. 2011 ky1 (Q11, Q26, Q27, Q33, Q34)
    f, d = load_exam('ky1', 2011)
    if d:
        update_q(d['questions'], 11,
                 options={'A': 'Except for', 'B': 'According to', 'C': 'Due to', 'D': 'As for'},
                 ans='B')
        update_q(d['questions'], 26, stem="We learn from Paragraph 1 that Gilbert's study shows")
        update_q(d['questions'], 27, stem="Gilbert's study finds that our negative feelings")
        update_q(d['questions'], 33, stem="The discovery of the 'peer effect' in human behavior shows that")
        update_q(d['questions'], 34, stem="According to Paragraph 4, the public health campaign")
        save_exam(f, d)
        print("Updated 2011 ky1 (Q11, Q26, Q27, Q33, Q34)")
        total_exams_updated += 1
        total_qs_updated += 5

    # 9. 2012 ky1 (Q7)
    f, d = load_exam('ky1', 2012)
    if d:
        update_q(d['questions'], 7,
                 options={'A': 'resorts (to)', 'B': 'sticks (to)', 'C': 'leads (to)', 'D': 'applies (to)'},
                 ans='D')
        save_exam(f, d)
        print("Updated 2012 ky1 (Q7)")
        total_exams_updated += 1
        total_qs_updated += 1

    # 10. 2013 ky1 (Q10, Q14, Q24, Q30, Q35, Q37, Q38, Q40, Part B Q41-45)
    f, d = load_exam('ky1', 2013)
    if d:
        update_q(d['questions'], 10,
                 options={'A': 'found', 'B': 'studied', 'C': 'chosen', 'D': 'identified'},
                 ans='C')
        update_q(d['questions'], 14,
                 options={'A': 'put', 'B': 'got', 'C': 'took', 'D': 'gave'},
                 ans='C')
        update_q(d['questions'], 24, stem="The author believes that the digital divide")
        update_q(d['questions'], 30, stem="The author suggests that the future development of the press")
        for q in d['questions']:
            if q.get('sort_order') == 35:
                for o in q.get('options', []):
                    o['text'] = o['text'].replace('o£', 'of')
        update_q(d['questions'], 37, stem="The author mentions the Supreme Court case in order to")
        update_q(d['questions'], 38, stem="It can be learned from Paragraph 4 that the administration")
        update_q(d['questions'], 40,
                 stem="What can be learned from the last paragraph?",
                 options={
                     'A': 'Immigration issues are usually decided by Congress.',
                     'B': 'The Administration is dominant over immigration issues.',
                     'C': 'Justices wanted to strengthen its coordination with Congress.',
                     'D': 'Justices intended to check the power of the Administration.'
                 },
                 ans='D')
        # Part B answers: Q41: E, Q42: F, Q43: D, Q44: G, Q45: A
        update_q(d['questions'], 41, ans='E')
        update_q(d['questions'], 42, ans='F')
        update_q(d['questions'], 43, ans='D')
        update_q(d['questions'], 44, ans='G')
        update_q(d['questions'], 45, ans='A')
        save_exam(f, d)
        print("Updated 2013 ky1 (Q10, Q14, Q24, Q30, Q35, Q37, Q38, Q40, Part B Q41-45)")
        total_exams_updated += 1
        total_qs_updated += 13

    # 11. 2013 ky2 (Part B canonical options & answers, stems & Passage 6)
    f, d = load_exam('ky2', 2013)
    if d:
        canonical_2013_ky2_opts = {
            'A': 'Shopkeepers are your friends',
            'B': 'Remember to treat yourself',
            'C': 'Stick to what you need',
            'D': 'Live like a peasant',
            'E': 'Balance your diet',
            'F': 'Planning is everything',
            'G': 'Waste not, want not'
        }
        # Answers: 41: F, 42: C, 43: G, 44: A, 45: B
        update_q(d['questions'], 41,
                 stem="Choose the most suitable subheading from A-G for section [41]:",
                 options=canonical_2013_ky2_opts, ans='F')
        update_q(d['questions'], 42,
                 stem="Choose the most suitable subheading from A-G for section [42]:",
                 options=canonical_2013_ky2_opts, ans='C')
        update_q(d['questions'], 43,
                 stem="Choose the most suitable subheading from A-G for section [43]:",
                 options=canonical_2013_ky2_opts, ans='G')
        update_q(d['questions'], 44,
                 stem="Choose the most suitable subheading from A-G for section [44]:",
                 options=canonical_2013_ky2_opts, ans='A')
        update_q(d['questions'], 45,
                 stem="Choose the most suitable subheading from A-G for section [45]:",
                 options=canonical_2013_ky2_opts, ans='B')
        total_qs_updated += 5

        for p in d.get('passages', []):
            if p.get('sort_order') == 6 or p.get('passage_type') == 'reading_part_b':
                content = p.get('content', '')
                clean_sentence = "He's feeling positive, but he'll carry on writing the blog until he's back in work: 'It keeps me sane, but it's also a record of how you can live in a non-deprived state, with barely any money to spend on food' - but eating well on a budget."
                if 's e n no os' in content:
                    content = re.sub(r"He's feeling positive.*?eating well on a budget\.", clean_sentence, content, flags=re.DOTALL)
                    p['content'] = content
                    print("  Cleaned 2013 ky2 Passage 6 OCR corruption")
        save_exam(f, d)
        print("Updated 2013 ky2 (Part B options & answers, stems & Passage 6)")
        total_exams_updated += 1

    # 12. 2014 ky1 (Q3, Q8 Cloze, Q17, Q22, Q25, Q32, Q34, Q36, Part B Q41-45)
    f, d = load_exam('ky1', 2014)
    if d:
        update_q(d['questions'], 3,
                 options={'A': 'Unless', 'B': 'While', 'C': 'Once', 'D': 'If'},
                 ans='B')
        update_q(d['questions'], 8,
                 stem="Choose the best option for blank [8] in the passage:",
                 options={'A': 'visual', 'B': 'financial', 'C': 'physical', 'D': 'mental'},
                 ans='B')
        update_q(d['questions'], 17,
                 options={'A': 'on', 'B': 'to', 'C': 'for', 'D': 'with'},
                 ans='A')
        update_q(d['questions'], 22, stem="The author mentions the American Academy of Arts and Sciences report to show that")
        update_q(d['questions'], 25, stem="Which of the following would be the best title for the text?")
        update_q(d['questions'], 32, stem="The discovery of the 'God particle' suggests that")
        update_q(d['questions'], 34, stem="The author believes that theoretical physicists should")
        update_q(d['questions'], 36, stem="The US government's recent decision on student loans is")
        # Part B answers: Q41: C, Q42: F, Q43: G, Q44: D, Q45: B
        update_q(d['questions'], 41, ans='C')
        update_q(d['questions'], 42, ans='F')
        update_q(d['questions'], 43, ans='G')
        update_q(d['questions'], 44, ans='D')
        update_q(d['questions'], 45, ans='B')
        save_exam(f, d)
        print("Updated 2014 ky1 (Q3, Q8, Q17, Q22, Q25, Q32, Q34, Q36, Part B Q41-45)")
        total_exams_updated += 1
        total_qs_updated += 13

    # 13. 2015 ky1 (Q13, Q23, Q26, Q27, Q29, Q33, Q34, Q38, Q39)
    f, d = load_exam('ky1', 2015)
    if d:
        update_q(d['questions'], 13,
                 options={'A': 'according to', 'B': 'rather than', 'C': 'regardless of', 'D': 'along with'},
                 ans='B')
        update_q(d['questions'], 23, stem="The author believes that friendship among genetically similar people")
        update_q(d['questions'], 26,
                 stem="The author mentions the police department's program to show that",
                 options={
                     'A': 'their risk-mitigating strategies are flawed',
                     'B': 'their surveillance technologies have flaws',
                     'C': "suspects' privacy rights are frequently infringed",
                     'D': 'the deployment of new technology needs justification'
                 })
        update_q(d['questions'], 27, stem="It can be learned from Paragraph 3 that the program")
        update_q(d['questions'], 29, stem="The author suggests that the collection of personal data")
        update_q(d['questions'], 33, stem="According to Paragraph 2, journalists are expected to")
        update_q(d['questions'], 34, stem="The decline of local newspapers has led to")
        update_q(d['questions'], 38, stem="The author believes that the publication of the report")
        update_q(d['questions'], 39, stem="Which of the following is true of the committee's decision?")
        for q in d['questions']:
            if q.get('explanation'):
                q['explanation'] = clean_watermarks(q['explanation'])
        save_exam(f, d)
        print("Updated 2015 ky1 (Q13, Q23, Q26, Q27, Q29, Q33, Q34, Q38, Q39)")
        total_exams_updated += 1
        total_qs_updated += 9

    # 14. 2016 ky1 (Q28, Q30)
    f, d = load_exam('ky1', 2016)
    if d:
        update_q(d['questions'], 28,
                 stem="Which of the following can be inferred from Paragraph 3?",
                 options={
                     'A': 'Labour is under attack for opposing development.',
                     'B': 'The Conservatives may abandon "off-plan" building.',
                     'C': 'Ukip may gain from its support for rural conservation.',
                     'D': 'The Liberal Democrats are losing political influence.'
                 },
                 ans='C')
        update_q(d['questions'], 30,
                 stem="In the last paragraph, the author shows his appreciation of",
                 options={
                     'A': 'the size of population in Britain',
                     'B': 'the enviable urban lifestyle in Britain',
                     'C': 'the town-and-country planning in Britain',
                     'D': "the political life in today's Britain"
                 },
                 ans='C')
        save_exam(f, d)
        print("Updated 2016 ky1 (Q28, Q30)")
        total_exams_updated += 1
        total_qs_updated += 2

    # 15. 2017 ky1 (Q7, Q11)
    f, d = load_exam('ky1', 2017)
    if d:
        update_q(d['questions'], 7,
                 options={'A': 'devoted', 'B': 'exposed', 'C': 'lost', 'D': 'attracted'},
                 ans='B')
        update_q(d['questions'], 11,
                 options={'A': 'Even', 'B': 'Still', 'C': 'Rather', 'D': 'Thus'},
                 ans='A')
        save_exam(f, d)
        print("Updated 2017 ky1 (Q7, Q11)")
        total_exams_updated += 1
        total_qs_updated += 2

    # 16. 2018 ky1 (Q25, Q32, Q33, Q37, Q39)
    f, d = load_exam('ky1', 2018)
    if d:
        update_q(d['questions'], 25, stem="In the text, the author presents a problem with")
        update_q(d['questions'], 32, stem="The trust responded to Denham's verdict with")
        update_q(d['questions'], 33, stem="The author argues in Paragraph 2 that")
        update_q(d['questions'], 37, stem="The USPS fails to modernize itself due to")
        update_q(d['questions'], 39, stem="The author seems to view legislators with")
        save_exam(f, d)
        print("Updated 2018 ky1 (Q25, Q32, Q33, Q37, Q39)")
        total_exams_updated += 1
        total_qs_updated += 5

    # 17. 2020 ky1 (Q7, Q21, Q34, Q36, Q38)
    f, d = load_exam('ky1', 2020)
    if d:
        update_q(d['questions'], 7,
                 options={'A': 'forget', 'B': 'regret', 'C': 'finish', 'D': 'avoid'},
                 ans='D')
        update_q(d['questions'], 21, stem="Critics argue that a 'town of culture' award could")
        update_q(d['questions'], 34, stem="The nationwide corporate gender quota has led to")
        update_q(d['questions'], 36, stem="The French Senate has passed a bill to")
        update_q(d['questions'], 38, stem="Proponents of multilateral measures share the opinion that")
        for q in d['questions']:
            if q.get('explanation'):
                q['explanation'] = clean_watermarks(q['explanation'])
        save_exam(f, d)
        print("Updated 2020 ky1 (Q7, Q21, Q34, Q36, Q38)")
        total_exams_updated += 1
        total_qs_updated += 5

    # 18. 2020 ky2 (Q22, Q27, Q33, Q34, Q36)
    f, d = load_exam('ky2', 2020)
    if d:
        update_q(d['questions'], 22, stem="In the experiment, the asocial robot was")
        update_q(d['questions'], 27, stem="Compared with their predecessors, today's CEOs are required to")
        update_q(d['questions'], 33, stem="The runway expansion provoked strong protests because")
        update_q(d['questions'], 34, stem="European mayors are taking action mainly because")
        update_q(d['questions'], 36, stem="The issue has received increasing attention recently because")
        save_exam(f, d)
        print("Updated 2020 ky2 (Q22, Q27, Q33, Q34, Q36)")
        total_exams_updated += 1
        total_qs_updated += 5

    # 19. 2021 ky1 (Q3, Q15)
    f, d = load_exam('ky1', 2021)
    if d:
        update_q(d['questions'], 3,
                 options={'A': 'while', 'B': 'since', 'C': 'once', 'D': 'until'},
                 ans='A')
        update_q(d['questions'], 15,
                 options={'A': 'compensations', 'B': 'symptoms', 'C': 'demands', 'D': 'treatments'},
                 ans='D')
        save_exam(f, d)
        print("Updated 2021 ky1 (Q3, Q15)")
        total_exams_updated += 1
        total_qs_updated += 2

    # 20. 2021 ky2 (Q9, Q21, Q23, Q24, Q25, Q26, Q27, Q29, Q30, Q32, Q35)
    f, d = load_exam('ky2', 2021)
    if d:
        update_q(d['questions'], 9,
                 options={'A': 'only', 'B': 'rather', 'C': 'once', 'D': 'also'},
                 ans='D')
        update_q(d['questions'], 21,
                 stem="Research by the World Economic Forum suggests",
                 options={
                     'A': 'an increase in full-time employment',
                     'B': 'an urgent demand for new job skills',
                     'C': 'a steady growth of job opportunities',
                     'D': 'a controversy about "core skills"'
                 })
        update_q(d['questions'], 23, stem="Efforts to resolve the skills mismatch in Canada")
        update_q(d['questions'], 24, stem="We can learn from Paragraph 3 that there was")
        update_q(d['questions'], 25,
                 stem="Scandinavian Airlines decided to",
                 options={
                     'A': 'create job vacancies for the unemployed',
                     'B': 'prepare their laid-off workers for other jobs',
                     'C': 'retrain their cabin staff for better services',
                     'D': "finance their staff's college education"
                 },
                 ans='B')
        update_q(d['questions'], 26, stem="Some people argue that food self-sufficiency in the UK would")
        update_q(d['questions'], 27, stem="The report by the University of Leeds shows that in the UK")
        update_q(d['questions'], 29, stem="It can be learned from the last paragraph that British people")
        update_q(d['questions'], 30, stem="The author's attitude to food self-sufficiency in the UK is")
        update_q(d['questions'], 32, stem="Microsoft's critics believe that the big tech companies")
        update_q(d['questions'], 35, stem="For the five biggest tech companies, their small acquisitions")
        save_exam(f, d)
        print("Updated 2021 ky2 (Q9, Q21, Q23, Q24, Q25, Q26, Q27, Q29, Q30, Q32, Q35)")
        total_exams_updated += 1
        total_qs_updated += 11

    # 21. 2022 ky1 (Q30, Q34)
    f, d = load_exam('ky1', 2022)
    if d:
        update_q(d['questions'], 30,
                 stem="What can be concluded about Generation Z from the last two paragraphs?",
                 options={
                     'A': 'Lifelong learning will define them.',
                     'B': 'They will make qualified educators.',
                     'C': 'Degrees will no longer appeal them.',
                     'D': 'They will have a limited choice of jobs.'
                 },
                 ans='A')
        update_q(d['questions'], 34,
                 stem="What does the author say about CAVS?",
                 options={
                     'A': 'It was headed alternately by artists and scientists.',
                     'B': 'It exemplified valuable art-science alliances.',
                     'C': 'Its projects aimed at advancing visual studies.',
                     'D': 'Its founders sought to raise the status of artists.'
                 },
                 ans='B')
        save_exam(f, d)
        print("Updated 2022 ky1 (Q30, Q34)")
        total_exams_updated += 1
        total_qs_updated += 2

    # 22. 2022 ky2 (Q5, Q9, Q12, Q25, Q29)
    f, d = load_exam('ky2', 2022)
    if d:
        update_q(d['questions'], 5,
                 options={'A': 'Accept', 'B': 'Explain', 'C': 'Remember', 'D': 'Suppose'},
                 ans='C')
        update_q(d['questions'], 9,
                 options={'A': 'highlight', 'B': 'sacrifice', 'C': 'continue', 'D': 'explore'},
                 ans='B')
        update_q(d['questions'], 12,
                 options={'A': 'put up with', 'B': 'make up for', 'C': 'hang on to', 'D': 'cut down on'},
                 ans='D')
        update_q(d['questions'], 25,
                 stem="John Brunnquell would disagree with Julie Stanton over regenerative eggs'",
                 options={
                     'A': 'market prospects',
                     'B': 'standard definition',
                     'C': 'nutritional value',
                     'D': 'moral implication'
                 },
                 ans='A')
        update_q(d['questions'], 29, stem="Many 'unretirees' are increasing their savings")
        save_exam(f, d)
        print("Updated 2022 ky2 (Q5, Q9, Q12, Q25, Q29)")
        total_exams_updated += 1
        total_qs_updated += 5

    print(f"\nAll calibrations complete! Updated {total_exams_updated} exams, {total_qs_updated} questions/passages.")

if __name__ == '__main__':
    run_calibrations()
