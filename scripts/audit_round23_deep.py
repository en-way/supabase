import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Deep Forensic Audit for Round 23 ===")

exam_files = sorted(glob.glob('public/data/exams/*.json'))

# 1. Answer vs Explanation Conflict Check
# Check all questions where explanation explicitly concludes [A/B/C/D] is correct, but correct_answer is different!
answer_conflicts = []

# 2. Suspicious Incomplete / Truncated Stems
suspicious_stems = []

# 3. Suspicious Truncated Options (e.g. ends with incomplete word or hyphen, or extremely short for reading)
suspicious_options = []

# 4. Leaked Question Numbers / Explanations inside Explanation
leaked_explanations = []

for fpath in exam_files:
    data = json.load(open(fpath, encoding='utf-8'))
    t = data['exam'].get('title', '')
    yr = data['exam'].get('year')
    cat = data['exam'].get('category_id')
    questions = data.get('questions', [])
    
    for q in questions:
        so = q.get('sort_order')
        stem = q.get('stem', '').strip()
        ans = q.get('correct_answer', '').strip()
        expl = q.get('explanation', '').strip()
        opts = q.get('options', [])
        opt_map = {o['key']: o['text'] for o in opts}
        
        # 1. Check Answer vs Explanation Consistency
        # Look for patterns like ［A］正确, ［A］为正确, 选［A］, 故［A］, 确定［A］, 故选A, 答案为A, etc.
        # Check if the primary mentioned answer matches `ans`
        m_expl_ans = re.findall(r'(?:故|可见|因此|所以|确定|选|为正确选项|为正确答案|符合题意|符合文意)[^。；\n]{0,20}[［\[【]([A-G])[］\]】](?:正确|符合|为最佳)?', expl)
        if m_expl_ans:
            # check the last conclusion
            last_ans = m_expl_ans[-1]
            if last_ans != ans and len(set(m_expl_ans)) == 1:
                # If all mentions are the same letter, and it doesn't match ans
                answer_conflicts.append((yr, cat, so, ans, m_expl_ans, expl[:120]))
        
        # Check Part B / Part A reading stems
        if so >= 21:
            # Check for suspicious stem endings (e.g. ending with dangling preposition or conjunction without blank)
            # like ending with 'with', 'by', 'for', 'of', 'to', 'that', 'which', 'is', 'in' but no blank marker and no question mark
            if re.search(r'\b(with|by|for|of|to|that|which|is|in|on|at|from|as|about)\s*$', stem, re.IGNORECASE):
                # check if there's no trailing punctuation
                suspicious_stems.append((yr, cat, so, stem))
            elif len(stem) < 18 and not stem.startswith('Choose the') and not stem.startswith('['):
                suspicious_stems.append((yr, cat, so, stem))
                
        # 3. Check Options for truncation / corruptions
        for o in opts:
            ot = o.get('text', '').strip()
            k = o.get('key', '')
            
            # Check for dangling hyphen at end
            if ot.endswith('-') or ot.endswith('—'):
                suspicious_options.append((yr, cat, so, k, 'dangling_hyphen', ot))
            # Check for dangling incomplete word like single letter or space-letter at end
            if re.search(r'\s+[a-zA-Z]$', ot) and not ot.endswith(' a') and not ot.endswith(' I'):
                suspicious_options.append((yr, cat, so, k, 'dangling_char', ot))
            # Check for reading comprehension options that are absurdly short (< 3 chars)
            if so in range(21, 41) and len(ot) < 3:
                suspicious_options.append((yr, cat, so, k, 'too_short', ot))
            # Check for weird non-ASCII corruptions
            if re.search(r'[#\$%\^&~_|\\]', ot):
                suspicious_options.append((yr, cat, so, k, 'special_char', ot))
                
        # 4. Check for leaked question numbers inside explanation
        lines = expl.splitlines()
        for l in lines:
            ls = l.strip()
            # check for next question marker like "32. " inside Q31
            m_q = re.match(r'^([1-4]\d)\.\s+[A-Za-z\u4e00-\u9fa5]', ls)
            if m_q and int(m_q.group(1)) != so:
                leaked_explanations.append((yr, cat, so, m_q.group(1), ls[:60]))

print(f"\n1. Answer vs Explanation Conflicts ({len(answer_conflicts)}):")
for item in answer_conflicts:
    print(f"  - {item[0]} {item[1]} Q{item[2]}: Correct Answer in DB/JSON is [{item[3]}], but Explanation concludes {item[4]}!")
    print(f"    Preview: {item[5]}")

print(f"\n2. Suspicious Stems ({len(suspicious_stems)}):")
for item in suspicious_stems:
    print(f"  - {item[0]} {item[1]} Q{item[2]}: {repr(item[3])}")

print(f"\n3. Suspicious Options ({len(suspicious_options)}):")
for item in suspicious_options:
    print(f"  - {item[0]} {item[1]} Q{item[2]} [{item[3]}]: ({item[4]}) -> {repr(item[5])}")

print(f"\n4. Leaked Question Explanations ({len(leaked_explanations)}):")
for item in leaked_explanations:
    print(f"  - {item[0]} {item[1]} Q{item[2]}: leaked Q{item[3]} -> {item[4]}")
