import json

with open('public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

round59_anomalies = []
title = data['exam'].get('title', '')
if title != '2013年全国硕士研究生入学统一考试英语（二）真题':
    round59_anomalies.append(('2013_ky2_title', title))
if float(data['exam'].get('total_score', 0)) != 60.0:
    round59_anomalies.append(('2013_ky2_total_score', data['exam'].get('total_score')))

p_list = data.get('passages', [])
if len(p_list) != 6:
    round59_anomalies.append(('2013_ky2_passages_count', len(p_list)))
else:
    cloze = p_list[0]
    c_paras = [p for p in cloze.get('content', '').split('\n\n') if p.strip()]
    if len(c_paras) != 4:
        round59_anomalies.append(('2013_ky2_cloze_paras', len(c_paras)))
    if not cloze.get('content', '').startswith('Given the advantages of electronic money'):
        round59_anomalies.append(('2013_ky2_cloze_header', 'corrupted'))

    t1 = p_list[1]
    t1_paras = [p for p in t1.get('content', '').split('\n\n') if p.strip()]
    if len(t1_paras) != 6:
        round59_anomalies.append(('2013_ky2_t1_paras', len(t1_paras)))
    if 'Davidson relates a joke from cotton country' not in t1.get('content', ''):
        round59_anomalies.append(('2013_ky2_t1_header', 'corrupted'))
    if 'G.I. Bill' not in t1.get('content', ''):
        round59_anomalies.append(('2013_ky2_t1_gi_bill', 'missing'))

    t2 = p_list[2]
    t2_paras = [p for p in t2.get('content', '').split('\n\n') if p.strip()]
    if len(t2_paras) != 5:
        round59_anomalies.append(('2013_ky2_t2_paras', len(t2_paras)))
    if 'A century ago, the immigrants from across the Atlantic' not in t2.get('content', ''):
        round59_anomalies.append(('2013_ky2_t2_header', 'corrupted'))

    t3 = p_list[3]
    t3_paras = [p for p in t3.get('content', '').split('\n\n') if p.strip()]
    if len(t3_paras) != 6:
        round59_anomalies.append(('2013_ky2_t3_paras', len(t3_paras)))
    if 'Scientists have found that although we are prone' not in t3.get('content', ''):
        round59_anomalies.append(('2013_ky2_t3_header', 'corrupted'))
    if 'John Gottman' not in t3.get('content', ''):
        round59_anomalies.append(('2013_ky2_t3_gottman', 'missing'))

    t4 = p_list[4]
    t4_paras = [p for p in t4.get('content', '').split('\n\n') if p.strip()]
    if len(t4_paras) != 7:
        round59_anomalies.append(('2013_ky2_t4_paras', len(t4_paras)))
    if 'Do we need quotas' not in t4.get('content', ''):
        round59_anomalies.append(('2013_ky2_t4_p3_quota', 'missing'))

    pb = p_list[5]
    pb_paras = [p for p in pb.get('content', '').split('\n\n') if p.strip()]
    if len(pb_paras) != 6:
        round59_anomalies.append(('2013_ky2_pb_paras', len(pb_paras)))
    if '[41]' not in pb.get('content', '') or '[45]' not in pb.get('content', ''):
        round59_anomalies.append(('2013_ky2_pb_labels', 'missing'))

q_list = data.get('questions', [])
if len(q_list) != 45:
    round59_anomalies.append(('2013_ky2_questions_count', len(q_list)))
else:
    for i, q in enumerate(q_list, 1):
        if q.get('question_number') != i:
            round59_anomalies.append((f'2013_ky2_q{i}_number', q.get('question_number')))
        if q.get('question_type') != 'multiple_choice':
            round59_anomalies.append((f'2013_ky2_q{i}_type', q.get('question_type')))
        exp_score = 0.5 if i <= 20 else 2.0
        q_pts = q.get('points') if q.get('points') is not None else q.get('score')
        if float(q_pts or 0) != exp_score:
            round59_anomalies.append((f'2013_ky2_q{i}_points', q_pts))
        opts = q.get('options', {})
        for opt_k, opt_v in opts.items():
            if opt_v.strip() == opt_k:
                round59_anomalies.append((f'2013_ky2_q{i}_placeholder_opt', opt_k))
        expl = q.get('explanation', '')
        if not expl or ('【精准定位】' not in expl and '【命题解密】' not in expl and '【错项排除】' not in expl):
            round59_anomalies.append((f'2013_ky2_q{i}_explanation_structure', 'incomplete'))

    gold_ans = {
        1:'B', 2:'D', 3:'B', 4:'A', 5:'C', 6:'B', 7:'A', 8:'D', 9:'C', 10:'A',
        11:'A', 12:'C', 13:'B', 14:'D', 15:'C', 16:'D', 17:'A', 18:'B', 19:'D', 20:'C',
        21:'A', 22:'D', 23:'B', 24:'B', 25:'C',
        26:'A', 27:'C', 28:'C', 29:'B', 30:'D',
        31:'D', 32:'A', 33:'B', 34:'C', 35:'B',
        36:'B', 37:'C', 38:'A', 39:'D', 40:'C',
        41:'F', 42:'C', 43:'G', 44:'A', 45:'B'
    }
    for q_no, exp_a in gold_ans.items():
        act_a = q_list[q_no-1].get('answer')
        if act_a != exp_a:
            round59_anomalies.append((f'2013_ky2_q{q_no}_ans', f'expected {exp_a}, got {act_a}'))

print('Round 59 Anomalies count:', len(round59_anomalies))
if round59_anomalies:
    print('Anomalies:', round59_anomalies)
else:
    print('SUCCESS: All 2013 ky2 assertions PASSED flawlessly!')
