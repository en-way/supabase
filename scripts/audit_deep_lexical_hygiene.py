import json
import glob
import re
import os

def audit_lexical_hygiene():
    exam_files = sorted(glob.glob('public/data/exams/*.json'))
    print(f"Scanning {len(exam_files)} exam files...")

    results = {
        'key_value_mismatch': [],
        'text_content_mismatch': [],
        'opt_whitespace': [],
        'opt_redundant_prefix': [],
        'stem_whitespace': [],
        'stem_number_prefix': [],
        'invisible_unicode': [],
        'duplicate_options': [],
        'empty_options': [],
        'part_a_opt_keys_abnormal': [],
        'cloze_opt_keys_abnormal': [],
        'part_b_opt_keys_abnormal': []
    }

    for ef in exam_files:
        with open(ef, 'r', encoding='utf-8') as f:
            data = json.load(f)
        exam_title = data.get('title', os.path.basename(ef))
        passages = data.get('passages', [])
        questions = data.get('questions', [])
        
        # Check passages for invisible unicode
        for p in passages:
            p_title = p.get('title', 'Unknown')
            p_content = p.get('content', '')
            for char_code, char_name in [('\u200b', 'ZERO-WIDTH SPACE'), ('\ufeff', 'BOM'), ('\u3000', 'FULL-WIDTH SPACE')]:
                if char_code in p_content:
                    results['invisible_unicode'].append((exam_title, f"Passage {p_title}", char_name))
                    
        for q in questions:
            q_num = q.get('question_number')
            stem = q.get('stem', '')
            options = q.get('options', [])
            
            # Stem checks
            if stem != stem.strip():
                results['stem_whitespace'].append((exam_title, q_num, repr(stem)))
            if re.match(r'^\s*(?:\[?\d+\]?[\.\:\s、]|Q\d+)', stem):
                results['stem_number_prefix'].append((exam_title, q_num, stem[:25]))
                
            for char_code, char_name in [('\u200b', 'ZERO-WIDTH SPACE'), ('\ufeff', 'BOM'), ('\u3000', 'FULL-WIDTH SPACE')]:
                if char_code in stem:
                    results['invisible_unicode'].append((exam_title, f"Stem Q{q_num}", char_name))
                    
            # Options checks
            opt_texts = []
            opt_keys = []
            for opt in options:
                k = opt.get('key')
                v = opt.get('value')
                t = opt.get('text')
                c = opt.get('content')
                
                if k != v:
                    results['key_value_mismatch'].append((exam_title, q_num, k, v))
                if t != c:
                    results['text_content_mismatch'].append((exam_title, q_num, t[:20] if t else None, c[:20] if c else None))
                    
                if t is not None:
                    if t != t.strip():
                        results['opt_whitespace'].append((exam_title, q_num, k, repr(t)))
                    if not t.strip():
                        results['empty_options'].append((exam_title, q_num, k))
                    # Check redundant prefix like '[A]' or 'A.' or 'A、' or 'A:' or 'B '..'G '
                    if re.match(r'^(?:\[[A-G]\]|[A-G][\.\:\、]|[A-G]\s{2,})\s*', t) or re.match(r'^[B-G]\s+[a-zA-Z]', t):
                        results['opt_redundant_prefix'].append((exam_title, q_num, k, t[:30]))
                        
                    for char_code, char_name in [('\u200b', 'ZERO-WIDTH SPACE'), ('\ufeff', 'BOM'), ('\u3000', 'FULL-WIDTH SPACE')]:
                        if char_code in t:
                            results['invisible_unicode'].append((exam_title, f"Opt Q{q_num}_{k}", char_name))
                            
                    opt_texts.append(t.strip().lower())
                else:
                    results['empty_options'].append((exam_title, q_num, k))
                opt_keys.append(k)
                
            # Duplicate option texts check
            if len(opt_texts) != len(set(opt_texts)):
                results['duplicate_options'].append((exam_title, q_num, opt_texts))
                
            # Key validity check
            if q_num <= 20: # Cloze
                if opt_keys != ['A', 'B', 'C', 'D']:
                    results['cloze_opt_keys_abnormal'].append((exam_title, q_num, opt_keys))
            elif 21 <= q_num <= 40: # Part A Reading
                if opt_keys != ['A', 'B', 'C', 'D']:
                    results['part_a_opt_keys_abnormal'].append((exam_title, q_num, opt_keys))
            elif 41 <= q_num <= 45: # Part B
                # In Part B, options usually are 7 choices [A-G] or 5-6 choices depending on question type
                if not (5 <= len(opt_keys) <= 7) or not all(k in ['A', 'B', 'C', 'D', 'E', 'F', 'G'] for k in opt_keys):
                    results['part_b_opt_keys_abnormal'].append((exam_title, q_num, opt_keys))

    print("\n=== Audit Results Summary ===")
    total_issues = 0
    for cat, lst in results.items():
        print(f"[{cat}]: {len(lst)} occurrences")
        total_issues += len(lst)
        for item in lst[:10]:
            print(f"   -> {item}")
        if len(lst) > 10:
            print(f"   ... and {len(lst) - 10} more")
    print(f"\nTotal Lexical/Typographic Hygiene Issues: {total_issues}")
    return results

if __name__ == '__main__':
    audit_lexical_hygiene()
