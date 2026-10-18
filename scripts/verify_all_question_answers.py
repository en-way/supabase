import json
import glob
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

exams = sorted(glob.glob('public/data/exams/*.json'))

mismatches = []
unclear = []

for f in exams:
    with open(f, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    exam = data['exam']
    year = exam['year']
    cat = exam['category_id']

    for q in data['questions']:
        so = q['sort_order']
        ans = q.get('correct_answer')
        expl = q.get('explanation', '')

        # Regex patterns to detect the stated answer in explanation:
        # e.g.:
        # 故[A]正确 / 故选[A] / 故选A / 故 A 项正确 / 故正确答案为 A / 选 A / ［A］正确 / 正确项[A]
        patterns = [
            r'故\s*\[?([A-G])\]?\s*(?:项)?\s*正确',
            r'故选\s*\[?([A-G])\]?',
            r'因此选\s*\[?([A-G])\]?',
            r'故正确答案为\s*\[?([A-G])\]?',
            r'正确答案为\s*\[?([A-G])\]?',
            r'正确答案是\s*\[?([A-G])\]?',
            r'正确项为\s*\[?([A-G])\]?',
            r'正确项是\s*\[?([A-G])\]?',
            r'\[([A-G])\]\s*为正确答案',
            r'\[([A-G])\]\s*为正确选项',
            r'［([A-G])］\s*正确',
            r'【([A-G])】\s*正确',
            r'\[([A-G])\]\s*正确',
            r'锁定正确项为\s*([A-G])',
            r'锁定正确答案为\s*([A-G])',
        ]

        found_answers = set()
        for p in patterns:
            for m in re.finditer(p, expl):
                found_answers.add(m.group(1))

        if found_answers:
            if ans not in found_answers:
                mismatches.append((year, cat, so, ans, list(found_answers), expl[:120]))

print(f"Total answer mismatches between correct_answer and expl: {len(mismatches)}")
for m in mismatches:
    print(f"\n{m[0]} {m[1]} Q{m[2]}: DB ans='{m[3]}' vs Expl mentions {m[4]}")
    print(f"Snippet: {m[5]}")
