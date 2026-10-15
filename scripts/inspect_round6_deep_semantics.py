import json
import glob
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

print("=== Round 6 Deep Semantic & Quality Audit for 1,825 Questions & 243 Passages ===")

exam_files = sorted(glob.glob("public/data/exams/*.json"))

empty_or_short_options = []
duplicate_options = []
unbalanced_quotes_stems = []
chinese_parens_in_options = []
explanation_semantic_mismatches = []
passage_spelling_anomalies = []
new_type_option_checks = []

for fpath in exam_files:
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    title = data["exam"]["title"]
    year = data["exam"]["year"]
    cat = data["exam"]["category_id"]

    passages = data.get("passages", [])
    questions = data.get("questions", [])

    # 1. Inspect questions & options
    for q in questions:
        so = q.get("sort_order")
        stem = q.get("stem", "")
        opts = q.get("options", [])
        ans = q.get("correct_answer", "")
        expl = q.get("explanation", "")

        # Check options
        texts = []
        for opt in opts:
            k = opt.get("key")
            t = (opt.get("text") or "").strip()
            texts.append(t)
            if len(t) == 0:
                empty_or_short_options.append((title, so, k, "EMPTY"))
            elif len(t) <= 1 and t not in ["T", "F", "A", "B", "C", "D"]:
                empty_or_short_options.append((title, so, k, f"SHORT: {t}"))
            
            # Check for Chinese parentheses in purely English options
            if "（" in t or "）" in t:
                chinese_parens_in_options.append((title, so, k, t))

        # Check for duplicates
        if len(texts) != len(set(texts)) and len(texts) > 0:
            duplicate_options.append((title, so, texts))

        # Check for quotes balance in stems
        # count standard double quotes
        dquotes = stem.count('"')
        if dquotes % 2 != 0:
            # check if curly quotes exist
            if '“' not in stem and '”' not in stem:
                unbalanced_quotes_stems.append((title, so, stem))

        # Check explanation semantic assertions
        # Patterns like: 故选[A]、故选择[A]、因此[A]项正确、正确答案是[A]、答案应为[A]、正确选项为[A]
        # Only take the concluding sentences
        conclusions = re.findall(r'(?:故|因此|所以|本题|显然|综上所述)?(?:正确答案|正确选项|答案)(?:为|是|应为|应是|选|为\s*项)?\s*\[?([A-G])\]?', expl)
        for c_ans in conclusions:
            if c_ans != ans:
                # Double check context
                # Sometimes it mentions distractor, like "如果选A，则..."
                # Let's inspect
                explanation_semantic_mismatches.append((title, so, ans, c_ans, expl[:120]))

        # Check New-Type (Part B) questions (sort_order 41-45)
        if so >= 41:
            # Check if options are [A]-[G]
            keys = [o.get("key") for o in opts]
            if len(opts) < 4:
                new_type_option_checks.append((title, so, keys))

print(f"\n1. Empty or very short options: {len(empty_or_short_options)}")
for item in empty_or_short_options[:10]:
    print("  ", item)

print(f"\n2. Duplicate options in questions: {len(duplicate_options)}")
for item in duplicate_options[:10]:
    print("  ", item)

print(f"\n3. Unbalanced double quotes in stems: {len(unbalanced_quotes_stems)}")
for item in unbalanced_quotes_stems[:10]:
    print("  ", item)

print(f"\n4. Chinese parentheses in options: {len(chinese_parens_in_options)}")
for item in chinese_parens_in_options[:10]:
    print("  ", item)

print(f"\n5. Potential Explanation Semantic Mismatches: {len(explanation_semantic_mismatches)}")
for item in explanation_semantic_mismatches[:15]:
    print(f"   [{item[0]} Q{item[1]}] Key Answer: {item[2]} vs Mentioned in Expl: {item[3]}")
    print(f"      Snippet: {item[4]}")

print(f"\n6. New Type (Part B) option anomalies: {len(new_type_option_checks)}")
for item in new_type_option_checks[:10]:
    print("  ", item)
