import glob, json, os, sys

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXAMS_DIR = os.path.join(ROOT_DIR, "public", "data", "exams")

def main():
    print("=== ZERO-TOLERANCE EXAM CALIBRATION QUALITY VERIFICATION ===")
    
    # 1. Check categories
    cat_path = os.path.join(ROOT_DIR, "public", "data", "categories.json")
    with open(cat_path, "r", encoding="utf-8") as f:
        categories = json.load(f)
    cat_ids = set(c["id"] for c in categories)
    assert cat_ids == {"ky1", "ky2"}, f"Categories must be strictly ky1 and ky2, got {cat_ids}"
    print(f"✅ Categories check passed: {cat_ids}")

    # 2. Check exams.json
    exams_path = os.path.join(ROOT_DIR, "public", "data", "exams.json")
    with open(exams_path, "r", encoding="utf-8") as f:
        exams_list = json.load(f)
    assert len(exams_list) == 26, f"Expected 26 exams in exams.json, got {len(exams_list)}"
    print(f"✅ exams.json index check passed: 26 exams present.")

    # 3. Check individual exam JSON files
    files = glob.glob(os.path.join(EXAMS_DIR, "*.json"))
    assert len(files) == 26, f"Expected 26 exam files in public/data/exams/, got {len(files)}"

    total_q_count = 0
    total_p_count = 0

    for fp in files:
        with open(fp, "r", encoding="utf-8") as f:
            d = json.load(f)
            
        exam = d.get("exam", {})
        title = exam.get("title")
        year = exam.get("year")
        cat = exam.get("category_id")
        questions = d.get("questions", [])
        passages = d.get("passages", [])
        
        # Verify exam metadata
        assert exam.get("id"), f"Missing exam id in {fp}"
        assert cat in ["ky1", "ky2"], f"Invalid category {cat} in {fp}"
        assert 2001 <= year <= 2025, f"Invalid year {year} in {fp}"
        
        # Verify passages
        assert len(passages) in [5, 6], f"{title}: Expected 5 or 6 passages, got {len(passages)}"
        for p in passages:
            assert p.get("id"), f"{title}: Missing passage id"
            assert p.get("category_id") == cat, f"{title}: Mismatched passage category"
            assert p.get("section_type") in ["cloze", "reading"], f"{title}: Invalid section type {p.get('section_type')}"
            assert len(p.get("content", "").strip()) >= 300, f"{title} P{p.get('sort_order')}: Passage content too short ({len(p.get('content',''))} chars)"
            total_p_count += 1
            
        # Verify questions
        expected_qs = 40 if (cat == "ky1" and year <= 2004) else 45
        assert len(questions) == expected_qs, f"{title}: Expected {expected_qs} questions, got {len(questions)}"
        
        for q in questions:
            qnum = q.get("sort_order")
            assert q.get("id"), f"{title} Q{qnum}: Missing id"
            assert q.get("category_id") == cat, f"{title} Q{qnum}: Mismatched question category"
            assert q.get("q_type") in ["choice", "cloze_item", "reading_item"], f"{title} Q{qnum}: Invalid q_type {q.get('q_type')}"
            assert len(q.get("stem", "").strip()) >= 5, f"{title} Q{qnum}: Stem too short: {repr(q.get('stem'))}"
            assert q.get("correct_answer") in ["A", "B", "C", "D", "E", "F", "G"], f"{title} Q{qnum}: Invalid answer {q.get('correct_answer')}"
            
            opts = q.get("options", [])
            assert isinstance(opts, list), f"{title} Q{qnum}: options is not a list"
            assert len(opts) >= 4, f"{title} Q{qnum}: options count < 4"
            
            for o in opts:
                assert isinstance(o, dict), f"{title} Q{qnum}: option item is not a dict: {o}"
                assert o.get("key") in ["A", "B", "C", "D", "E", "F", "G"], f"{title} Q{qnum}: Invalid option key {o.get('key')}"
                assert o.get("text"), f"{title} Q{qnum}: Empty option text"
                assert o.get("text") not in ["Option A", "Option B", "Option C", "Option D"], f"{title} Q{qnum}: Fallback option detected!"
                
            total_q_count += 1

    print(f"✅ Passages check passed: {total_p_count} passages across 26 exams (all > 300 chars).")
    print(f"✅ Questions check passed: {total_q_count} questions across 26 exams (0 fallback options, 0 string options).")
    print("\n🎉 ALL ZERO-TOLERANCE ASSERTIONS PASSED WITH 100% SUCCESS!")

if __name__ == "__main__":
    main()
