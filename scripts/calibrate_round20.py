import json
import os

# Helper to find exam JSON by year and category
def find_exam_file(year, cat):
    target_dir = 'public/data/exams'
    for fname in os.listdir(target_dir):
        if fname.endswith('.json'):
            fpath = os.path.join(target_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as fp:
                d = json.load(fp)
            exam = d.get('exam', {})
            if exam.get('year') == year and exam.get('category_id') == cat:
                return fpath, d
    return None, None

def save_exam_file(fpath, data):
    with open(fpath, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)
    print(f"Saved calibrated exam: {fpath}")

# ==============================================================================
# 1. Calibrate 2007 ky1
# ==============================================================================
fpath_2007, d_2007 = find_exam_file(2007, 'ky1')
assert d_2007, "2007 ky1 file not found"

for q in d_2007['questions']:
    so = q['sort_order']
    # Cloze
    if so == 4:
        q['options'] = [
            {'key': 'A', 'text': 'related (to)', 'value': 'A'},
            {'key': 'B', 'text': 'close (to)', 'value': 'B'},
            {'key': 'C', 'text': 'open (to)', 'value': 'C'},
            {'key': 'D', 'text': 'devoted (to)', 'value': 'D'}
        ]
    elif so == 5:
        q['options'] = [
            {'key': 'A', 'text': 'access (to)', 'value': 'A'},
            {'key': 'B', 'text': 'succession (to)', 'value': 'B'},
            {'key': 'C', 'text': 'right (to)', 'value': 'C'},
            {'key': 'D', 'text': 'return (to)', 'value': 'D'}
        ]
    elif so == 8:
        q['options'] = [
            {'key': 'A', 'text': 'freedom', 'value': 'A'},
            {'key': 'B', 'text': 'origin', 'value': 'B'},
            {'key': 'C', 'text': 'impact', 'value': 'C'},
            {'key': 'D', 'text': 'reform', 'value': 'D'}
        ]
        q['correct_answer'] = 'A'
        q['answer'] = 'A'
    elif so == 10:
        for opt in q['options']:
            if opt['key'] == 'C': opt['text'] = 'among'
    elif so == 11:
        q['options'] = [
            {'key': 'A', 'text': 'allowed', 'value': 'A'},
            {'key': 'B', 'text': 'preached', 'value': 'B'},
            {'key': 'C', 'text': 'granted', 'value': 'C'},
            {'key': 'D', 'text': 'funded', 'value': 'D'}
        ]
    elif so == 14:
        q['options'] = [
            {'key': 'A', 'text': 'spread', 'value': 'A'},
            {'key': 'B', 'text': 'interference', 'value': 'B'},
            {'key': 'C', 'text': 'exclusion', 'value': 'C'},
            {'key': 'D', 'text': 'influence', 'value': 'D'}
        ]
    elif so == 15:
        q['options'] = [
            {'key': 'A', 'text': 'support', 'value': 'A'},
            {'key': 'B', 'text': 'cry', 'value': 'B'},
            {'key': 'C', 'text': 'plea', 'value': 'C'},
            {'key': 'D', 'text': 'wish', 'value': 'D'}
        ]
        q['correct_answer'] = 'B'
        q['answer'] = 'B'
    elif so == 19:
        for opt in q['options']:
            if opt['key'] == 'D': opt['text'] = 'preferred'

    # Reading
    elif so == 23:
        q['stem'] = "According to Ericsson, good memory ________."
        for opt in q['options']:
            if opt['key'] == 'C':
                opt['text'] = "is determined by genetic rather than psychological factors"
    elif so == 26:
        q['stem'] = "Which of the following may be required in an intelligence test?"
        for opt in q['options']:
            if opt['key'] == 'C':
                opt['text'] = "Telling the differences between certain concepts."
    elif so == 27:
        q['stem'] = "What can be inferred about intelligence testing from Paragraph 3?"
        q['options'] = [
            {'key': 'A', 'text': 'People no longer use IQ scores as an indicator of intelligence.', 'value': 'A'},
            {'key': 'B', 'text': 'More versions of IQ tests are now available on the Internet.', 'value': 'B'},
            {'key': 'C', 'text': 'The test content and formats for adults and children may be different.', 'value': 'C'},
            {'key': 'D', 'text': 'Scientists have defined the important elements of human intelligence.', 'value': 'D'}
        ]
    elif so == 28:
        q['stem'] = "People nowadays can no longer achieve IQ scores as high as vos Savant's because ________."
        q['options'] = [
            {'key': 'A', 'text': 'the scores are obtained through different computational procedures', 'value': 'A'},
            {'key': 'B', 'text': 'creativity rather than analytical skills is emphasized now', 'value': 'B'},
            {'key': 'C', 'text': "vos Savant's case is an extreme one that will not repeat", 'value': 'C'},
            {'key': 'D', 'text': 'the defining characteristic of IQ tests has changed', 'value': 'D'}
        ]
    elif so == 29:
        q['stem'] = "We can conclude from the last paragraph that ________."
        q['options'] = [
            {'key': 'A', 'text': "test scores may not be reliable indicators of one's ability", 'value': 'A'},
            {'key': 'B', 'text': 'IQ scores and SAT results are highly correlated', 'value': 'B'},
            {'key': 'C', 'text': 'testing involves a lot of guesswork', 'value': 'C'},
            {'key': 'D', 'text': 'traditional tests are out of date', 'value': 'D'}
        ]
    elif so == 32:
        q['stem'] = "As a result of President Bush's reform, retired people may have ________."
        q['options'] = [
            {'key': 'A', 'text': 'a higher sense of security', 'value': 'A'},
            {'key': 'B', 'text': 'less secured payments', 'value': 'B'},
            {'key': 'C', 'text': 'less chance to invest', 'value': 'C'},
            {'key': 'D', 'text': 'a guaranteed future', 'value': 'D'}
        ]
    elif so == 37:
        q['stem'] = "According to Paragraph 2, some organizations check their systems to find out ________."
        q['options'] = [
            {'key': 'A', 'text': 'whether there is any weak point', 'value': 'A'},
            {'key': 'B', 'text': 'what sort of data has been stolen', 'value': 'B'},
            {'key': 'C', 'text': 'who is responsible for the leakage', 'value': 'C'},
            {'key': 'D', 'text': 'how the potential spies can be located', 'value': 'D'}
        ]
    elif so == 38:
        q['stem'] = "In bringing up the concept of GASP the author is making the point that ________."
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "shareholders' interests should be properly attended to"
    elif so == 40:
        q['stem'] = "It can be inferred from Paragraph 5 that ________."
        q['options'] = [
            {'key': 'A', 'text': 'data leakage is more severe in Europe', 'value': 'A'},
            {'key': 'B', 'text': "FTC's decision is essential to data security", 'value': 'B'},
            {'key': 'C', 'text': 'California takes the lead in security legislation', 'value': 'C'},
            {'key': 'D', 'text': 'legal penalty is a major solution to data leakage', 'value': 'D'}
        ]

save_exam_file(fpath_2007, d_2007)

# ==============================================================================
# 2. Calibrate 2006 ky1
# ==============================================================================
fpath_2006, d_2006 = find_exam_file(2006, 'ky1')
assert d_2006, "2006 ky1 file not found"

for q in d_2006['questions']:
    so = q['sort_order']
    # Cloze
    if so == 1:
        q['options'] = [
            {'key': 'A', 'text': 'Indeed', 'value': 'A'},
            {'key': 'B', 'text': 'Likewise', 'value': 'B'},
            {'key': 'C', 'text': 'Therefore', 'value': 'C'},
            {'key': 'D', 'text': 'Furthermore', 'value': 'D'}
        ]
    elif so == 2:
        q['options'] = [
            {'key': 'A', 'text': 'stand', 'value': 'A'},
            {'key': 'B', 'text': 'cope', 'value': 'B'},
            {'key': 'C', 'text': 'approve', 'value': 'C'},
            {'key': 'D', 'text': 'retain', 'value': 'D'}
        ]
    elif so == 3:
        for opt in q['options']:
            if opt['key'] == 'D': opt['text'] = 'toward'
    elif so == 5:
        q['options'] = [
            {'key': 'A', 'text': 'Generally', 'value': 'A'},
            {'key': 'B', 'text': 'Almost', 'value': 'B'},
            {'key': 'C', 'text': 'Hardly', 'value': 'C'},
            {'key': 'D', 'text': 'Not', 'value': 'D'}
        ]
    elif so == 6:
        q['options'] = [
            {'key': 'A', 'text': 'cover', 'value': 'A'},
            {'key': 'B', 'text': 'change', 'value': 'B'},
            {'key': 'C', 'text': 'range', 'value': 'C'},
            {'key': 'D', 'text': 'differ', 'value': 'D'}
        ]
    elif so == 7:
        q['options'] = [
            {'key': 'A', 'text': 'Now that', 'value': 'A'},
            {'key': 'B', 'text': 'Although', 'value': 'B'},
            {'key': 'C', 'text': 'Provided', 'value': 'C'},
            {'key': 'D', 'text': 'Except that', 'value': 'D'}
        ]
    elif so == 8:
        q['options'] = [
            {'key': 'A', 'text': 'inflating', 'value': 'A'},
            {'key': 'B', 'text': 'expanding', 'value': 'B'},
            {'key': 'C', 'text': 'increasing', 'value': 'C'},
            {'key': 'D', 'text': 'extending', 'value': 'D'}
        ]
    elif so == 9:
        q['options'] = [
            {'key': 'A', 'text': 'predicts', 'value': 'A'},
            {'key': 'B', 'text': 'displays', 'value': 'B'},
            {'key': 'C', 'text': 'proves', 'value': 'C'},
            {'key': 'D', 'text': 'discovers', 'value': 'D'}
        ]
        q['correct_answer'] = 'A'
        q['answer'] = 'A'
    elif so == 10:
        q['options'] = [
            {'key': 'A', 'text': 'assist', 'value': 'A'},
            {'key': 'B', 'text': 'track', 'value': 'B'},
            {'key': 'C', 'text': 'sustain', 'value': 'C'},
            {'key': 'D', 'text': 'dismiss', 'value': 'D'}
        ]
    elif so == 11:
        q['options'] = [
            {'key': 'A', 'text': 'Hence', 'value': 'A'},
            {'key': 'B', 'text': 'But', 'value': 'B'},
            {'key': 'C', 'text': 'Even', 'value': 'C'},
            {'key': 'D', 'text': 'Only', 'value': 'D'}
        ]
    elif so == 12:
        q['options'] = [
            {'key': 'A', 'text': 'lodging', 'value': 'A'},
            {'key': 'B', 'text': 'shelter', 'value': 'B'},
            {'key': 'C', 'text': 'dwelling', 'value': 'C'},
            {'key': 'D', 'text': 'house', 'value': 'D'}
        ]
    elif so == 13:
        q['options'] = [
            {'key': 'A', 'text': 'searching', 'value': 'A'},
            {'key': 'B', 'text': 'strolling', 'value': 'B'},
            {'key': 'C', 'text': 'crowding', 'value': 'C'},
            {'key': 'D', 'text': 'wandering', 'value': 'D'}
        ]
    elif so == 14:
        for opt in q['options']:
            if opt['key'] == 'B': opt['text'] = 'once'
            elif opt['key'] == 'C': opt['text'] = 'while'
    elif so == 15:
        for opt in q['options']:
            if opt['key'] == 'B': opt['text'] = 'existence'
            elif opt['key'] == 'D': opt['text'] = 'maintenance'
    elif so == 16:
        q['options'] = [
            {'key': 'A', 'text': '(turn) around', 'value': 'A'},
            {'key': 'B', 'text': '(turn) over', 'value': 'B'},
            {'key': 'C', 'text': '(turn) on', 'value': 'C'},
            {'key': 'D', 'text': '(turn) up', 'value': 'D'}
        ]
    elif so == 17:
        q['options'] = [
            {'key': 'A', 'text': 'complex', 'value': 'A'},
            {'key': 'B', 'text': 'comprehensive', 'value': 'B'},
            {'key': 'C', 'text': 'complementary', 'value': 'C'},
            {'key': 'D', 'text': 'compensating', 'value': 'D'}
        ]
    elif so == 19:
        for opt in q['options']:
            if opt['key'] == 'A': opt['text'] = 'puts'
            elif opt['key'] == 'B': opt['text'] = 'interprets'
            elif opt['key'] == 'D': opt['text'] = 'makes'

    # Reading
    elif so == 26:
        q['stem'] = "From the first two paragraphs, we learn that ________."
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "the townsfolk deny the RSC's contribution to the town's revenue"
            elif opt['key'] == 'B':
                opt['text'] = "the actors of the RSC imitate Shakespeare on and off stage"
    elif so == 29:
        q['stem'] = "According to the townsfolk, the RSC deserves no subsidy because ________."
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "ticket prices can be raised to cover the spending"
    elif so == 34:
        q['stem'] = "Dr. Myers and other researchers hold that ________."
        q['options'] = [
            {'key': 'A', 'text': 'people should look for a baseline that can work for a longer time', 'value': 'A'},
            {'key': 'B', 'text': 'fisheries should keep their yields below 50% of the biomass', 'value': 'B'},
            {'key': 'C', 'text': 'the ocean biomass should be restored to its original level', 'value': 'C'},
            {'key': 'D', 'text': 'people should adjust the fishing baseline to the changing situation', 'value': 'D'}
        ]
    elif so == 35:
        q['stem'] = "The author seems to be mainly concerned with most fisheries' ________."
        q['options'] = [
            {'key': 'A', 'text': 'management efficiency', 'value': 'A'},
            {'key': 'B', 'text': 'biomass level', 'value': 'B'},
            {'key': 'C', 'text': 'catch-size limits', 'value': 'C'},
            {'key': 'D', 'text': 'technological application', 'value': 'D'}
        ]

save_exam_file(fpath_2006, d_2006)

# ==============================================================================
# 3. Calibrate 2008 ky1
# ==============================================================================
fpath_2008, d_2008 = find_exam_file(2008, 'ky1')
assert d_2008, "2008 ky1 file not found"

for q in d_2008['questions']:
    so = q['sort_order']
    # Cloze
    if so == 1:
        q['options'] = [
            {'key': 'A', 'text': '(be) selected (to do)', 'value': 'A'},
            {'key': 'B', 'text': '(be) prepared (to do)', 'value': 'B'},
            {'key': 'C', 'text': '(be) obliged (to do)', 'value': 'C'},
            {'key': 'D', 'text': '(be) pleased (to do)', 'value': 'D'}
        ]
    elif so == 5:
        for opt in q['options']:
            if opt['key'] == 'C': opt['text'] = 'Even'
    elif so == 6:
        q['options'] = [
            {'key': 'A', 'text': '(at the) thought (of)', 'value': 'A'},
            {'key': 'B', 'text': '(at the) sight (of)', 'value': 'B'},
            {'key': 'C', 'text': '(at the) cost (of)', 'value': 'C'},
            {'key': 'D', 'text': '(at the) risk (of)', 'value': 'D'}
        ]
    elif so == 9:
        q['options'] = [
            {'key': 'A', 'text': 'attaining', 'value': 'A'},
            {'key': 'B', 'text': 'scoring', 'value': 'B'},
            {'key': 'C', 'text': 'reaching', 'value': 'C'},
            {'key': 'D', 'text': 'calculating', 'value': 'D'}
        ]
    elif so == 10:
        q['options'] = [
            {'key': 'A', 'text': 'normal', 'value': 'A'},
            {'key': 'B', 'text': 'common', 'value': 'B'},
            {'key': 'C', 'text': 'mean', 'value': 'C'},
            {'key': 'D', 'text': 'total', 'value': 'D'}
        ]
    elif so == 12:
        q['options'] = [
            {'key': 'A', 'text': 'missions', 'value': 'A'},
            {'key': 'B', 'text': 'fortunes', 'value': 'B'},
            {'key': 'C', 'text': 'interests', 'value': 'C'},
            {'key': 'D', 'text': 'careers', 'value': 'D'}
        ]
    elif so == 14:
        q['options'] = [
            {'key': 'A', 'text': 'moreover', 'value': 'A'},
            {'key': 'B', 'text': 'therefore', 'value': 'B'},
            {'key': 'C', 'text': 'however', 'value': 'C'},
            {'key': 'D', 'text': 'meanwhile', 'value': 'D'}
        ]
    elif so == 15:
        q['options'] = [
            {'key': 'A', 'text': 'given up (to sb/sth)', 'value': 'A'},
            {'key': 'B', 'text': 'got over (to sb)', 'value': 'B'},
            {'key': 'C', 'text': 'carried on', 'value': 'C'},
            {'key': 'D', 'text': 'put down (to sth)', 'value': 'D'}
        ]
    elif so == 16:
        q['options'] = [
            {'key': 'A', 'text': 'assessing', 'value': 'A'},
            {'key': 'B', 'text': 'supervising', 'value': 'B'},
            {'key': 'C', 'text': 'administering', 'value': 'C'},
            {'key': 'D', 'text': 'valuing', 'value': 'D'}
        ]
    elif so == 17:
        q['options'] = [
            {'key': 'A', 'text': 'development', 'value': 'A'},
            {'key': 'B', 'text': 'origin', 'value': 'B'},
            {'key': 'C', 'text': 'consequence', 'value': 'C'},
            {'key': 'D', 'text': 'instrument', 'value': 'D'}
        ]
    elif so == 18:
        q['options'] = [
            {'key': 'A', 'text': 'linked', 'value': 'A'},
            {'key': 'B', 'text': 'integrated', 'value': 'B'},
            {'key': 'C', 'text': 'woven', 'value': 'C'},
            {'key': 'D', 'text': 'combined', 'value': 'D'}
        ]
    elif so == 19:
        q['options'] = [
            {'key': 'A', 'text': 'limited (sb to sth)', 'value': 'A'},
            {'key': 'B', 'text': 'subjected (sb to sth)', 'value': 'B'},
            {'key': 'C', 'text': 'converted (sb to sth)', 'value': 'C'},
            {'key': 'D', 'text': 'directed (sb to sth)', 'value': 'D'}
        ]

    # Reading
    elif so == 28:
        q['stem'] = "According to the text, online publication is significant in that ________."
        q['options'] = [
            {'key': 'A', 'text': 'it provides an easier access to scientific results', 'value': 'A'},
            {'key': 'B', 'text': 'it brings huge profits to scientific researchers', 'value': 'B'},
            {'key': 'C', 'text': 'it emphasizes the crucial role of scientific knowledge', 'value': 'C'},
            {'key': 'D', 'text': 'it facilitates public investment in scientific research', 'value': 'D'}
        ]
    elif so == 29:
        q['stem'] = "With the open-access publishing model, the author of a paper is required to ________."
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = "cover the cost of its publication"
            elif opt['key'] == 'B':
                opt['text'] = "subscribe to the journal publishing it"
            elif opt['key'] == 'C':
                opt['text'] = "allow other online journals to use it freely"
    elif so == 34:
        q['stem'] = "We learn from the last paragraph that in the near future ________."
        q['options'] = [
            {'key': 'A', 'text': 'the garment industry will reconsider the uniform size', 'value': 'A'},
            {'key': 'B', 'text': 'the design of military uniforms will remain unchanged', 'value': 'B'},
            {'key': 'C', 'text': 'genetic testing will be employed in selecting sportsmen', 'value': 'C'},
            {'key': 'D', 'text': 'the existing data of human height will still be applicable', 'value': 'D'}
        ]
    elif so == 40:
        for opt in q['options']:
            if opt['key'] == 'B': opt['text'] = "military experience"
            elif opt['key'] == 'D': opt['text'] = "political stand"

save_exam_file(fpath_2008, d_2008)

# ==============================================================================
# 4. Calibrate 2009 ky1
# ==============================================================================
fpath_2009, d_2009 = find_exam_file(2009, 'ky1')
assert d_2009, "2009 ky1 file not found"

for q in d_2009['questions']:
    so = q['sort_order']
    if so == 1:
        for opt in q['options']:
            if opt['key'] == 'C': opt['text'] = 'Observe'
    elif so == 3:
        for opt in q['options']:
            if opt['key'] == 'A': opt['text'] = 'thinner'
            elif opt['key'] == 'B': opt['text'] = 'stabler'
    elif so == 6:
        for opt in q['options']:
            if opt['key'] == 'D': opt['text'] = 'long'
    elif so == 10:
        for opt in q['options']:
            if opt['key'] == 'B': opt['text'] = 'forward'
            elif opt['key'] == 'C': opt['text'] = 'afterward'
            elif opt['key'] == 'D': opt['text'] = 'backward'
    elif so == 35:
        for opt in q['options']:
            if opt['key'] == 'A': opt['text'] = 'results directly from competitive'

save_exam_file(fpath_2009, d_2009)

# ==============================================================================
# 5. Calibrate 2014 ky1
# ==============================================================================
fpath_2014, d_2014 = find_exam_file(2014, 'ky1')
assert d_2014, "2014 ky1 file not found"

for q in d_2014['questions']:
    so = q['sort_order']
    if so == 9:
        for opt in q['options']:
            if opt['key'] == 'A': opt['text'] = 'channel'

save_exam_file(fpath_2014, d_2014)

# ==============================================================================
# 6. Calibrate 2021 ky1
# ==============================================================================
fpath_2021, d_2021 = find_exam_file(2021, 'ky1')
assert d_2021, "2021 ky1 file not found"

for q in d_2021['questions']:
    so = q['sort_order']
    if so == 18:
        for opt in q['options']:
            if opt['key'] == 'B': opt['text'] = 'process'
    elif so == 39:
        for opt in q['options']:
            if opt['key'] == 'C': opt['text'] = 'is at odds with its earlier rulings'

save_exam_file(fpath_2021, d_2021)

print("\nAll 6 exams successfully calibrated for Round 20!")
