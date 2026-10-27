import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
path = 'public/data/exams/59181a61-cd5e-560e-b413-d3ecd3fc1e32.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Exam metadata
exam = data['exam']
exam['title'] = '2025年全国硕士研究生招生考试英语（二）真题'
exam['duration_minutes'] = 180
exam['total_score'] = 60.0
exam['pass_score'] = 36.0
exam['approval_status'] = 'approved'
exam['is_published'] = True
exam['category_id'] = 'ky2'

passages = data['passages']

# Passage 1: Cloze (5 paragraphs, 352 words)
p1 = passages[0]
p1_paras = [p.strip() for p in p1['content'].split('\n\n') if p.strip()]
if p1_paras[0].startswith('Directions:'):
    p1_paras = p1_paras[1:]
p1['content'] = '\n\n'.join(p1_paras)
p1['title'] = 'Section I: Use of English'
p1['section_type'] = 'use_of_english'
p1['passage_type'] = 'cloze'
p1['sort_order'] = 1

# Passage 2: Text 1 (7 paragraphs, 373 words)
p2 = passages[1]
p2['title'] = 'Section II: Reading Comprehension Part A - Text 1'
p2['section_type'] = 'reading'
p2['passage_type'] = None
p2['sort_order'] = 2

# Passage 3: Text 2 (6 paragraphs, 404 words)
p3 = passages[2]
p3['title'] = 'Section II: Reading Comprehension Part A - Text 2'
p3['section_type'] = 'reading'
p3['passage_type'] = None
p3['sort_order'] = 3

# Passage 4: Text 3 (6 paragraphs, 403 words)
p4 = passages[3]
p4['title'] = 'Section II: Reading Comprehension Part A - Text 3'
p4['section_type'] = 'reading'
p4['passage_type'] = None
p4['sort_order'] = 4

# Passage 5: Text 4 (5 paragraphs, 410 words)
p5 = passages[4]
p5['title'] = 'Section II: Reading Comprehension Part A - Text 4'
p5['section_type'] = 'reading'
p5['passage_type'] = None
p5['sort_order'] = 5

# Passage 6: Part B (8 paragraphs)
p6 = passages[5]
p6_title = "Five Steps to Suggesting a Change at Work That'll Actually Get Taken Seriously"
p6_subheadings = """[A] Stay positive
[B] Respect the past
[C] Use channels
[D] Give it time
[E] Invite resistance
[F] Be a salesman
[G] Be humble"""

p6_intro = ("Everyone wants to be that person—the one who looks at the same information as everyone else, "
            "but who sees a fresh, innovative solution. However, it takes more than simply having a good idea. "
            "How you share it is as important as the suggestion itself. Why? Because writing a new script—literally "
            "or figuratively—means that other team members will have to adapt to something new. So whether you're "
            "suggesting a (seemingly) benign change like streamlining outdated protocol, or a bigger change like "
            "adding an hour to each workday so people can leave early on Fridays, you're asking others to reimagine "
            "their workflow or schedule. Not to mention, if the process you're scrapping is one someone else "
            "suggested, there's the possibility of hurt feelings. To gain buy-in on an innovative, new idea, follow these steps:")

p6_q41 = ("[41] Great ideas don't stand alone. In other words, you can't mention your suggestion once and expect it "
          "to be adopted. To see a change, you'll need to champion your plan and sell its merits. In addition, you "
          "need to be willing to stand up to scrutiny and criticism and be prepared to explain your innovation in "
          "different ways for various audiences.")

p6_q42 = ('[42] Sometimes it makes sense to go to your boss first. But other times, it\'s useful to build a coalition '
          'among your co-workers or other stakeholders. When it works, it works great—because you\'re ready for your '
          'stubborn supervisor\'s pushback with answers like, "Actually, I connected with a few people in our tech '
          'department to discuss how much time these kinds of website updates would take, and they suggested they '
          'have the bandwidth."')

p6_q43 = ('[43] One of the biggest barriers to gaining buy-in occurs when the owner of an idea is viewed as argumentative, '
          'defensive, or close-minded. Because, let\'s be honest: No one likes a know-it-all. So, if people disagree with you, '
          'don\'t be indignant. Instead, listen to their concerns fully, try to understand their perspective, and include '
          'their concerns (and possible remedies) in future discussions. So, instead of saying, "Martha, our current '
          'slogan is confusing and should be updated," you could try, "Martha raises a great point that our current '
          'slogan has a long history for our stakeholders, but I wonder if we might be able to brainstorm a tagline '
          'that could build on that—and be clearer for new customers."')

p6_q44 = ('[44] New ideas are the grandchildren of old ones. In other words, don\'t throw old solutions under the bus '
          'to make your improvement stand out. Remember that in light of whatever the problem the old system '
          'solved—or, maybe, has failed to solve in recent memory—it was a great idea at the time. Appreciating '
          'the older solution demonstrates that you understand the institutional history, and making respect clear '
          'will reassure long-tenured employees rather than alienating them from your idea.')

p6_q45 = ('[45] When pitching a new idea, it\'s important to use the language of abundance instead of the language '
          'of deficit. Instead of saying what is wrong, broken, or suboptimal, talk about what is right, fixable, '
          'or ideal. For example, try, "I can see lots of applications for this new approach" rather than, '
          '"This innovation is the only way." Be optimistic but realistic, and you will stand out.')

p6_paras = [p6_title, p6_subheadings, p6_intro, p6_q41, p6_q42, p6_q43, p6_q44, p6_q45]
p6['content'] = '\n\n'.join(p6_paras)
p6['title'] = 'Section II: Reading Comprehension Part B'
p6['section_type'] = 'reading'
p6['passage_type'] = None
p6['sort_order'] = 6

# Questions
questions = data['questions']
exp_answers = {
    1: 'D', 2: 'A', 3: 'C', 4: 'B', 5: 'D', 6: 'B', 7: 'A', 8: 'C', 9: 'D', 10: 'A',
    11: 'A', 12: 'B', 13: 'D', 14: 'D', 15: 'B', 16: 'A', 17: 'C', 18: 'C', 19: 'B', 20: 'C',
    21: 'B', 22: 'C', 23: 'A', 24: 'D', 25: 'A',
    26: 'B', 27: 'C', 28: 'C', 29: 'B', 30: 'C',
    31: 'A', 32: 'B', 33: 'A', 34: 'B', 35: 'D',
    36: 'C', 37: 'D', 38: 'A', 39: 'D', 40: 'D',
    41: 'F', 42: 'C', 43: 'G', 44: 'B', 45: 'A'
}

for i, q in enumerate(questions, 1):
    q['sort_order'] = i
    q['question_number'] = i
    pts = 0.5 if i <= 20 else 2.0
    q['points'] = pts
    q['score'] = pts
    q['q_type'] = 'cloze_item' if i <= 20 else 'reading_item'
    q['category_id'] = 'ky2'
    q['exam_id'] = '59181a61-cd5e-560e-b413-d3ecd3fc1e32'
    
    # check answer alignment
    expected_ans = exp_answers[i]
    q['answer'] = expected_ans
    q['correct_answer'] = expected_ans
    
    # standardize options
    opts = q.get('options', [])
    new_opts = []
    for o in opts:
        k = o.get('key')
        t = o.get('text') or o.get('content')
        new_opts.append({
            'key': k,
            'value': k,
            'text': t,
            'content': t
        })
    q['options'] = new_opts

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('Successfully built 2025 ky2 pure gold JSON!')
print('Passages summary:')
for i, p in enumerate(passages, 1):
    paras = [x.strip() for x in p['content'].split('\n\n') if x.strip()]
    words = len(p['content'].split())
    print(f'Passage {i} ({p["title"]}): {len(paras)} paras, {words} words')
print(f'Questions summary: {len(questions)} questions calibrated.')
