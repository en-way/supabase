import glob, json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

files = glob.glob('public/data/exams/*.json')
print(f'Total exam JSON files: {len(files)}')

audit_results = []
for fp in files:
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    exam = d.get('exam', {})
    title = exam.get('title')
    cat = exam.get('category_id')
    year = exam.get('year')
    questions = d.get('questions', [])
    passages = d.get('passages', [])
    
    # 1. Check passages
    empty_passages = [p['sort_order'] for p in passages if len(p.get('content', '').strip()) < 50]
    
    # 2. Check fallback options & string options
    fallback_opts = []
    string_opts = []
    for q in questions:
        opts = q.get('options', [])
        for o in opts:
            if isinstance(o, str):
                string_opts.append(q['sort_order'])
                break
            elif isinstance(o, dict) and o.get('text') in ['Option A', 'Option B', 'Option C', 'Option D']:
                fallback_opts.append(q['sort_order'])
                break
    
    # 3. Check short or suspicious stems
    weird_stems = [q['sort_order'] for q in questions if len(q.get('stem', '').strip()) < 5]
    
    # 4. Check answer distribution
    ans_dist = {}
    for q in questions:
        a = q.get('correct_answer', '?')
        ans_dist[a] = ans_dist.get(a, 0) + 1
        
    audit_results.append({
        'year': year,
        'cat': cat,
        'title': title,
        'q_count': len(questions),
        'p_count': len(passages),
        'empty_p': empty_passages,
        'fallback_opts': fallback_opts,
        'string_opts': string_opts,
        'weird_stems': weird_stems,
        'ans_dist': ans_dist
    })

audit_results.sort(key=lambda x: (x['cat'], x['year']))
for r in audit_results:
    flag = []
    if r['fallback_opts']:
        flag.append(f"FallbackOpts: {len(r['fallback_opts'])}")
    if r['string_opts']:
        flag.append(f"StringOpts: {len(r['string_opts'])}")
    if r['empty_p']:
        flag.append(f"EmptyPassages: {r['empty_p']}")
    if r['weird_stems']:
        flag.append(f"WeirdStems: {r['weird_stems']}")
    if r['q_count'] not in [40, 45]:
        flag.append(f"QCountError: {r['q_count']}")
    
    status_str = ", ".join(flag) if flag else "PERFECT"
    print(f"{r['cat']} {r['year']} ({r['q_count']} Qs, {r['p_count']} Passages) -> {status_str}")
    if r['fallback_opts']:
        print(f"   Fallback Qs: {r['fallback_opts']}")
    if r['string_opts']:
        print(f"   String Qs: {r['string_opts']}")
