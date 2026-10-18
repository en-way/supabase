import json
import glob
import re

exams = sorted(glob.glob('public/data/exams/*.json'))

print(f"Total exams: {len(exams)}")

# 1. Cross-check correct_answer vs explanation mentioned answer across all 1825 questions
answer_discrepancies = []
# 2. Check options across pre-2005 exams
pre2005_option_issues = []
# 3. Check ky2 options for truncations or intra-word spaces
ky2_option_issues = []
# 4. Check Part B options across all exams
part_b_issues = []

for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data['exam']
    year = exam['year']
    cat = exam['category_id']
    title = exam['title']

    for q in data['questions']:
        so = q['sort_order']
        ans = q.get('correct_answer')
        expl = q.get('explanation', '')
        opts = q.get('options', [])

        # Check 1: Explanation answer cross-check
        # Look for patterns like "故选[A]", "故选 A", "故[A]正确", "故选B", "答案为[C]", "［精准定位］...，D正确", "正确答案为 C"
        # Extract explicit answer statements
        match = re.search(r'(?:故(?:选|正确答案为|答案为|选答案)|正确答案[为是]|因此(?:选|答案为)|故\s*\[?([A-G])\]?\s*正确|故选\s*\[?([A-G])\]?|正确项(?:为|是)?\s*\[?([A-G])\]?|［([A-G])］\s*正确|\[([A-G])\]\s*正确)\b', expl)
        if match:
            # find the group that matched
            matched_ans = [g for g in match.groups() if g]
            if matched_ans:
                declared_ans = matched_ans[0]
                if declared_ans != ans:
                    answer_discrepancies.append((year, cat, so, ans, declared_ans, match.group(0), expl[:100]))

        # Check 2: Pre-2005 options
        if year < 2005:
            for o in opts:
                k = o.get('key')
                t = o.get('text', '')
                tokens = re.findall(r"\b[a-zA-Z]+\b", t)
                # check single letters
                bad_single = [tok for tok in tokens if len(tok) == 1 and tok.lower() not in ('a', 'i')]
                if bad_single:
                    pre2005_option_issues.append((year, cat, so, k, t, f"single letters: {bad_single}"))
                if tokens:
                    last_tok = tokens[-1].lower()
                    if len(last_tok) <= 2 and last_tok not in {'it', 'in', 'on', 'up', 'so', 'to', 'by', 'at', 'no', 'us', 'me', 'do', 'be', 'he', 'we', 'is', 'as', 'if', 'or', 'an', 'am', 'all', 'out', 'off', 'not', 'too', 'day', 'one', 'new', 'now', 'way', 'law', 'art', 'men', 'job', 'car', 'war', 'oil', 'tax', 'bed', 'end', 'dog', 'sea', 'sky', 'sun', 'air', 'eye', 'god', 'act', 'age', 'arm', 'bar', 'box', 'boy', 'bus', 'cat', 'cup', 'ear', 'egg', 'fan', 'fat', 'fee', 'fit', 'fix', 'fly', 'fun', 'gap', 'gas', 'gun', 'guy', 'hat', 'hit', 'ice', 'ink', 'jar', 'jaw', 'joy', 'key', 'kid', 'lab', 'leg', 'lie', 'lip', 'log', 'lot', 'map', 'mud', 'net', 'nut', 'pan', 'pen', 'pet', 'pie', 'pig', 'pin', 'pit', 'pot', 'rag', 'rat', 'raw', 'ray', 'rib', 'rip', 'rod', 'row', 'rug', 'run', 'sad', 'set', 'sin', 'sir', 'son', 'spy', 'tap', 'tea', 'tie', 'tin', 'tip', 'toe', 'ton', 'top', 'toy', 'van', 'vet', 'via', 'vow', 'wet', 'win', 'zoo', 'dna', 'fcc', 'ftc', 'rsc', 'nrc', 'dnt', 'prh', 'cct', 'gpa', 'ai', 'tv'}:
                        pre2005_option_issues.append((year, cat, so, k, t, f"truncated last word: {last_tok}"))

        # Check 3: ky2 options
        if cat == 'ky2':
            for o in opts:
                k = o.get('key')
                t = o.get('text', '')
                tokens = re.findall(r"\b[a-zA-Z]+\b", t)
                bad_single = [tok for tok in tokens if len(tok) == 1 and tok.lower() not in ('a', 'i')]
                if bad_single:
                    ky2_option_issues.append((year, cat, so, k, t, f"single letters: {bad_single}"))

        # Check 4: Part B (Q41-45)
        if 41 <= so <= 45:
            for o in opts:
                k = o.get('key')
                t = o.get('text', '')
                if len(t.strip()) < 5:
                    part_b_issues.append((year, cat, so, k, t, "too short option text"))
                if '' in t:
                    part_b_issues.append((year, cat, so, k, t, "replacement char in option"))

print(f"\n1. Answer Discrepancies in Explanations: {len(answer_discrepancies)}")
for ad in answer_discrepancies:
    print(f"  {ad[0]} {ad[1]} Q{ad[2]}: correct_answer='{ad[3]}' but expl says '{ad[4]}' (pattern: '{ad[5]}')")

print(f"\n2. Pre-2005 Option Issues: {len(pre2005_option_issues)}")
for poi in pre2005_option_issues[:20]:
    print(f"  {poi[0]} {poi[1]} Q{poi[2]} [{poi[3]}]: '{poi[4]}' --> {poi[5]}")

print(f"\n3. ky2 Option Issues: {len(ky2_option_issues)}")
for koi in ky2_option_issues[:20]:
    print(f"  {koi[0]} {koi[1]} Q{koi[2]} [{koi[3]}]: '{koi[4]}' --> {koi[5]}")

print(f"\n4. Part B Issues: {len(part_b_issues)}")
for pbi in part_b_issues[:20]:
    print(f"  {pbi[0]} {pbi[1]} Q{pbi[2]} [{pbi[3]}]: '{pbi[4]}' --> {pbi[5]}")
