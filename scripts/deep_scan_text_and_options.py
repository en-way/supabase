# -*- coding: utf-8 -*-
"""
deep_scan_text_and_options.py
Comprehensive deterministic scanner for passages and options across all 41 exams (2001-2025).
"""

import os
import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

EXAMS_DIR = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

def scan_all_exams():
    exam_files = glob.glob(os.path.join(EXAMS_DIR, "*.json"))
    print(f"=== Starting Deep Deterministic Scan Across {len(exam_files)} Exams ===")
    
    findings = {
        'ky1_early': {},   # 2001-2009 (Agent 1)
        'ky1_mid': {},     # 2010-2017 (Agent 2)
        'ky1_late': {},    # 2018-2025 (Agent 3)
        'ky2_early': {},   # 2010-2017 (Agent 4)
        'ky2_late': {},    # 2018-2025 (Agent 5)
    }
    
    summary_stats = {
        'total_exams': len(exam_files),
        'total_passages': 0,
        'total_questions': 0,
        'passage_spacing_issues': 0,
        'passage_emdash_issues': 0,
        'passage_hyphen_breaks': 0,
        'passage_cloze_blank_issues': 0,
        'passage_direction_leaks': 0,
        'option_duplicates': 0,
        'option_key_leaks': 0,
        'option_key_missing': 0,
        'option_answer_mismatch': 0,
        'option_truncated': 0
    }

    for fpath in sorted(exam_files):
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        exam = data.get('exam', {})
        eid = exam.get('id')
        title = exam.get('title', '')
        year = exam.get('year')
        cat = exam.get('category_id')
        
        # Determine agent group
        if cat == 'ky1':
            if year <= 2009:
                group = 'ky1_early'
            elif year <= 2017:
                group = 'ky1_mid'
            else:
                group = 'ky1_late'
        else: # ky2
            if year <= 2017:
                group = 'ky2_early'
            else:
                group = 'ky2_late'
                
        exam_report = {
            'id': eid,
            'title': title,
            'year': year,
            'category': cat,
            'passage_anomalies': [],
            'question_anomalies': []
        }
        
        passages = sorted(data.get('passages', []), key=lambda x: x.get('sort_order', 0))
        questions = sorted(data.get('questions', []), key=lambda x: x.get('sort_order', 0))
        
        summary_stats['total_passages'] += len(passages)
        summary_stats['total_questions'] += len(questions)
        
        # 1. Audit Passages
        for p_idx, p in enumerate(passages, 1):
            pid = p.get('id')
            ptitle = p.get('title', '')
            content = p.get('content', '')
            paras = [para.strip() for para in content.split('\n\n') if para.strip()]
            words = len(content.split())
            
            # Check for leaked Directions
            if any(para.startswith('Directions:') or 'ANSWER SHEET' in para for para in paras):
                exam_report['passage_anomalies'].append({
                    'type': 'direction_leak',
                    'passage': ptitle,
                    'desc': 'Contains Directions or ANSWER SHEET text'
                })
                summary_stats['passage_direction_leaks'] += 1
                
            # Check for non-breaking spaces \xa0
            if '\xa0' in content:
                exam_report['passage_anomalies'].append({
                    'type': 'non_breaking_space',
                    'passage': ptitle,
                    'desc': f'Contains {content.count(chr(160))} non-breaking spaces (\\xa0)'
                })
                summary_stats['passage_spacing_issues'] += 1
                
            # Check for double spaces (outside of markdown/code)
            double_spaces = len(re.findall(r'[^\n\r]  [^\n\r]', content))
            if double_spaces > 0:
                exam_report['passage_anomalies'].append({
                    'type': 'double_space',
                    'passage': ptitle,
                    'desc': f'Contains {double_spaces} double spaces'
                })
                summary_stats['passage_spacing_issues'] += 1
                
            # Check for punctuation missing following space (e.g., word,word or word.Word, excluding decimals like 3.14 or abbreviations like e.g. / U.S.)
            punct_no_space = re.findall(r'([A-Za-z]{2,}[,\.:;][A-Za-z]{2,})', content)
            # Filter false positives like https://, e.g., i.e.
            punct_no_space = [x for x in punct_no_space if not x.startswith('http') and x not in ['e.g.', 'i.e.']]
            if punct_no_space:
                exam_report['passage_anomalies'].append({
                    'type': 'punct_missing_space',
                    'passage': ptitle,
                    'samples': punct_no_space[:5]
                })
                summary_stats['passage_spacing_issues'] += len(punct_no_space)
                
            # Check for broken hyphens from line wraps (e.g., "repre- sent", "infor- mation")
            hyphen_breaks = re.findall(r'([a-z]{3,}-\s+[a-z]{3,})', content)
            if hyphen_breaks:
                exam_report['passage_anomalies'].append({
                    'type': 'hyphen_line_break',
                    'passage': ptitle,
                    'samples': hyphen_breaks[:5]
                })
                summary_stats['passage_hyphen_breaks'] += len(hyphen_breaks)
                
            # Check Cloze sequential blanks [1] .. [20]
            if p_idx == 1:
                blanks = [int(m) for m in re.findall(r'\[(\d+)\]', content)]
                expected_blanks = list(range(1, 21))
                if blanks != expected_blanks:
                    missing = set(expected_blanks) - set(blanks)
                    unexpected = set(blanks) - set(expected_blanks)
                    exam_report['passage_anomalies'].append({
                        'type': 'cloze_blank_mismatch',
                        'passage': ptitle,
                        'desc': f'Blanks mismatch: found {len(blanks)} blanks, missing={missing}, unexpected={unexpected}'
                    })
                    summary_stats['passage_cloze_blank_issues'] += 1
                    
            # Check corrupted dashes like -- or weird unicode characters
            if '--' in content:
                exam_report['passage_anomalies'].append({
                    'type': 'double_hyphen',
                    'passage': ptitle,
                    'desc': f'Found double hyphens (--) instead of em-dash (—)'
                })
                summary_stats['passage_emdash_issues'] += 1
                
        # 2. Audit Questions & Options
        for q_idx, q in enumerate(questions, 1):
            qid = q.get('id')
            qnum = q.get('question_number')
            so = q.get('sort_order')
            stem = q.get('stem', '')
            ans = q.get('answer')
            cans = q.get('correct_answer')
            opts = q.get('options', [])
            expl = q.get('explanation', '')
            pts = q.get('points')
            sc = q.get('score')
            
            # Answer consistency
            if ans != cans:
                exam_report['question_anomalies'].append({
                    'q_num': qnum or q_idx,
                    'type': 'answer_mismatch',
                    'desc': f'answer={ans} != correct_answer={cans}'
                })
                summary_stats['option_answer_mismatch'] += 1
                
            # Option keys & count
            exp_count = 4 if q_idx <= 40 else 7
            if len(opts) != exp_count:
                # Some early years may have 4 options for Part B if multiple choice, but ky2 has 7 subheadings
                pass
                
            opt_keys = [o.get('key') for o in opts]
            opt_texts = [o.get('text') or o.get('content') or '' for o in opts]
            
            # Check duplicate options
            non_empty_texts = [t.strip().lower() for t in opt_texts if t.strip()]
            if len(non_empty_texts) != len(set(non_empty_texts)):
                duplicates = [t for t in set(non_empty_texts) if non_empty_texts.count(t) > 1]
                exam_report['question_anomalies'].append({
                    'q_num': qnum or q_idx,
                    'type': 'duplicate_options',
                    'duplicates': duplicates
                })
                summary_stats['option_duplicates'] += 1
                
            # Check option structure: {key, value, text, content}
            for o in opts:
                missing_keys = [k for k in ['key', 'value', 'text', 'content'] if k not in o]
                if missing_keys:
                    exam_report['question_anomalies'].append({
                        'q_num': qnum or q_idx,
                        'type': 'missing_option_keys',
                        'desc': f'Option missing keys: {missing_keys}'
                    })
                    summary_stats['option_key_missing'] += 1
                    break
                    
                # Check leaked key in text
                otext = o.get('text', '')
                if re.match(r'^[A-G][\.\:\)\]]\s+', otext):
                    exam_report['question_anomalies'].append({
                        'q_num': qnum or q_idx,
                        'type': 'leaked_option_prefix',
                        'desc': f'Option text starts with prefix: {repr(otext[:10])}'
                    })
                    summary_stats['option_key_leaks'] += 1
                    
                # Check suspicious truncated option
                if otext.endswith('-') or otext.endswith(','):
                    exam_report['question_anomalies'].append({
                        'q_num': qnum or q_idx,
                        'type': 'suspicious_truncated_option',
                        'desc': f'Option text ends suspiciously: {repr(otext[-10:])}'
                    })
                    summary_stats['option_truncated'] += 1

            # Check if answer exists in option keys
            if cans and cans not in opt_keys:
                exam_report['question_anomalies'].append({
                    'q_num': qnum or q_idx,
                    'type': 'answer_not_in_keys',
                    'desc': f'Answer {cans} not in keys {opt_keys}'
                })
                summary_stats['option_answer_mismatch'] += 1

        findings[group][f"{year}_{cat}"] = exam_report

    # Save raw findings to scratch json
    out_path = r"scripts/deep_scan_findings.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(findings, f, ensure_ascii=False, indent=2)
        
    print("\n=== Scan Completed Successfully ===")
    print(f"Total exams analyzed: {summary_stats['total_exams']}")
    print(f"Total passages analyzed: {summary_stats['total_passages']}")
    print(f"Total questions analyzed: {summary_stats['total_questions']}")
    print("Summary of detected anomalies across 41 exams:")
    for k, v in summary_stats.items():
        if k.startswith('total'):
            continue
        print(f"  - {k}: {v}")
        
    # Per-group summary
    for grp, exams in findings.items():
        grp_anomalies = sum(len(ex['passage_anomalies']) + len(ex['question_anomalies']) for ex in exams.values())
        print(f"Group [{grp}]: {len(exams)} exams, total anomalies flagged = {grp_anomalies}")

if __name__ == '__main__':
    scan_all_exams()
