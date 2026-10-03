import os, sys, glob, json, re
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXAMS_DIR = os.path.join(ROOT_DIR, "public", "data", "exams")

from scripts.data_partb_options import PART_B_DB
from scripts.enhanced_pdf_extractor import (
    get_pdf_path,
    normalize_text,
    clean_opt_text,
    extract_cloze,
    extract_reading
)

# Authentic fallbacks for the 22 edge cases identified and decoded from official MOE / Huangpi Shu
FALLBACK_OPTIONS = {
    # 2011 ky1
    (2011, 'ky1', 30): {
        "stem": "Which of the following is the best title for the text?",
        "options": [
            {"key": "A", "text": "CEOs: Where to Go?"},
            {"key": "B", "text": "CEOs: All the Way Up?"},
            {"key": "C", "text": "Top Managers Jump without a Net"},
            {"key": "D", "text": "The Only Way Out for Top Performers"}
        ],
        "key": "C"
    },
    (2011, 'ky1', 39): {
        "stem": "According to Paragraph 4, the message conveyed by celebrity magazines is",
        "options": [
            {"key": "A", "text": "soothing"},
            {"key": "B", "text": "ambiguous"},
            {"key": "C", "text": "compensatory"},
            {"key": "D", "text": "misleading"}
        ],
        "key": "D"
    },

    # 2001 ky1
    (2001, 'ky1', 25): {
        "stem": "Digital divide is something",
        "options": [
            {"key": "A", "text": "getting worse because of the Internet"},
            {"key": "B", "text": "the rich countries are responsible for"},
            {"key": "C", "text": "the world must guard against"},
            {"key": "D", "text": "considered positive today"}
        ],
        "key": "C"
    },

    # 2021 ky2
    (2021, 'ky2', 15): {
        "options": [
            {"key": "A", "text": "moral"},
            {"key": "B", "text": "background"},
            {"key": "C", "text": "style"},
            {"key": "D", "text": "form"}
        ],
        "key": "A"
    },

    # 2019 ky1
    (2019, 'ky1', 21): {
        "stem": "According to Paragraph 1, one motive in imposing the new rule is to",
        "options": [
            {"key": "A", "text": "enhance bankers' sense of responsibility"},
            {"key": "B", "text": "guarantee the bonuses of top executives"},
            {"key": "C", "text": "avoid the embarrassment of bank directors"},
            {"key": "D", "text": "foster the competition in the banking industry"}
        ],
        "key": "A"
    },
    (2019, 'ky1', 24): {
        "stem": "The US and France examples are used to illustrate",
        "options": [
            {"key": "A", "text": "the obstacles to preventing 'short-termism'"},
            {"key": "B", "text": "the significance of long-term thinking"},
            {"key": "C", "text": "the approaches to tackling financial crises"},
            {"key": "D", "text": "the necessity of reducing bonuses"}
        ],
        "key": "A"
    },
    (2019, 'ky1', 28): {
        "stem": "According to Paragraph 5, grade forgiveness enables colleges to",
        "options": [
            {"key": "A", "text": "obtain more financial support"},
            {"key": "B", "text": "boost their student enrollments"},
            {"key": "C", "text": "improve their teaching quality"},
            {"key": "D", "text": "meet local governments' needs"}
        ],
        "key": "A"
    },

    # 2015 ky1
    (2015, 'ky1', 14): {
        "options": [
            {"key": "A", "text": "chances"},
            {"key": "B", "text": "responses"},
            {"key": "C", "text": "missions"},
            {"key": "D", "text": "benefits"}
        ],
        "key": "D"
    },
    (2015, 'ky1', 19): {
        "options": [
            {"key": "A", "text": "political"},
            {"key": "B", "text": "religious"},
            {"key": "C", "text": "ethnic"},
            {"key": "D", "text": "economic"}
        ],
        "key": "C"
    },

    # 2003 ky1
    (2003, 'ky1', 25): {
        "stem": "Straitford is most proud of its",
        "options": [
            {"key": "A", "text": "official status"},
            {"key": "B", "text": "nonconformist image"},
            {"key": "C", "text": "efficient staff"},
            {"key": "D", "text": "military background"}
        ],
        "key": "B"
    },

    # 2009 ky1
    (2009, 'ky1', 13): {
        "options": [
            {"key": "A", "text": "deliver"},
            {"key": "B", "text": "carry"},
            {"key": "C", "text": "perform"},
            {"key": "D", "text": "apply"}
        ],
        "key": "C"
    },

    # 2012 ky1
    (2012, 'ky1', 25): {
        "stem": "The author suggests in the last paragraph that the effect of peer pressure is",
        "options": [
            {"key": "A", "text": "harmful"},
            {"key": "B", "text": "desirable"},
            {"key": "C", "text": "profound"},
            {"key": "D", "text": "questionable"}
        ],
        "key": "D"
    },

    # 2005 ky1
    (2005, 'ky1', 25): {
        "stem": "Dr. Brosnan and Dr. de Waal have eventually found in their study that the monkeys",
        "options": [
            {"key": "A", "text": "prefer grapes to cucumbers"},
            {"key": "B", "text": "can be taught to exchange things"},
            {"key": "C", "text": "will not be co-operative if feeling cheated"},
            {"key": "D", "text": "are unhappy when separated from others"}
        ],
        "key": "C"
    },
    (2005, 'ky1', 37): {
        "stem": "The word 'talking' (Line 5, Para. 3) denotes",
        "options": [
            {"key": "A", "text": "modesty"},
            {"key": "B", "text": "personality"},
            {"key": "C", "text": "sincerity"},
            {"key": "D", "text": "talkativeness"}
        ],
        "key": "A"
    },
    (2005, 'ky1', 39): {
        "stem": "The description of Russians' love of memorizing poetry shows the author's",
        "options": [
            {"key": "A", "text": "interest in their language"},
            {"key": "B", "text": "appreciation of their efforts"},
            {"key": "C", "text": "admiration for their poetry"},
            {"key": "D", "text": "contempt for their educational system"}
        ],
        "key": "B"
    },

    # 2002 ky1
    (2002, 'ky1', 20): {
        "options": [
            {"key": "A", "text": "above"},
            {"key": "B", "text": "upon"},
            {"key": "C", "text": "against"},
            {"key": "D", "text": "with"}
        ],
        "key": "C"
    },

    # 2010 ky1
    (2010, 'ky1', 25): {
        "stem": "What would be the best title for the text?",
        "options": [
            {"key": "A", "text": "Newspapers of the Good Old Days"},
            {"key": "B", "text": "The Lost Horizon in Newspapers"},
            {"key": "C", "text": "Mournful Decline of Journalism"},
            {"key": "D", "text": "Prominent Critics in Memory"}
        ],
        "key": "B"
    },

    # 2021 ky1
    (2021, 'ky1', 36): {
        "stem": "There has long been concern that broadband providers would",
        "options": [
            {"key": "A", "text": "bring web-based firms under control"},
            {"key": "B", "text": "slow down the traffic on their network"},
            {"key": "C", "text": "show partiality in treating clients"},
            {"key": "D", "text": "intensify competition with their rivals"}
        ],
        "key": "C"
    },

    # 2018 ky1
    (2018, 'ky1', 10): {
        "options": [
            {"key": "A", "text": "counterparts"},
            {"key": "B", "text": "substitutes"},
            {"key": "C", "text": "colleagues"},
            {"key": "D", "text": "supporters"}
        ],
        "key": "A"
    },

    # 2020 ky1
    (2020, 'ky1', 8): {
        "options": [
            {"key": "A", "text": "partially"},
            {"key": "B", "text": "regularly"},
            {"key": "C", "text": "easily"},
            {"key": "D", "text": "initially"}
        ],
        "key": "A"
    },
    (2020, 'ky1', 36): {
        "stem": "The French Senate has passed a bill to",
        "options": [
            {"key": "A", "text": "regulate digital services platforms"},
            {"key": "B", "text": "protect French companies' interests"},
            {"key": "C", "text": "impose a levy on tech multinationals"},
            {"key": "D", "text": "curb the influence of advertising"}
        ],
        "key": "C"
    },
    (2020, 'ky1', 37): {
        "stem": "It can be learned from Paragraph 2 that the digital services tax",
        "options": [
            {"key": "A", "text": "may trigger countermeasures against France"},
            {"key": "B", "text": "is apt to arouse criticism at home and abroad"},
            {"key": "C", "text": "aims to promote fair competition in multilateral trade"},
            {"key": "D", "text": "will be applied to all international enterprises in France"}
        ],
        "key": "A"
    }
}

synthetic_keywords = [
    'Authentic verified standard key option',
    'The primary contextual factor',
    'Alternative contextual interpretation',
    'Secondary perspective',
    'Comprehensive analytical view',
    'Paragraph A: The underlying psychological mechanisms'
]

def calibrate_all():
    files = sorted(glob.glob(os.path.join(EXAMS_DIR, "*.json")))
    print(f"Loaded {len(files)} exam files.")
    
    total_repaired = 0
    
    # Cache for extracted PDF texts
    pdf_text_cache = {}
    
    for f in files:
        with open(f, 'r', encoding='utf-8') as fp:
            d = json.load(fp)
            
        exam = d.get('exam', {})
        year = exam.get('year')
        cat = exam.get('category_id')
        title = exam.get('title')
        questions = d.get('questions', [])
        
        modified = False
        exam_repaired = 0
        
        for q in questions:
            qnum = q['sort_order']
            opts = q.get('options', [])
            
            # Check if this question has synthetic options
            has_synthetic = any(any(kw in (opt.get('text', '') if isinstance(opt, dict) else str(opt)) for kw in synthetic_keywords) for opt in opts)
            needs_part_b_fix = (41 <= qnum <= 45 and (year, cat) in PART_B_DB and len(opts) < 7)
            
            if not has_synthetic and not needs_part_b_fix:
                continue
                
            # Case 1: Part B (41-45)
            if 41 <= qnum <= 45:
                if (year, cat) in PART_B_DB:
                    b_data = PART_B_DB[(year, cat)]
                    q['options'] = b_data['options']
                    if qnum in b_data['keys']:
                        q['correct_answer'] = b_data['keys'][qnum]
                        q['correct_option'] = b_data['keys'][qnum]
                    modified = True
                    exam_repaired += 1
                    total_repaired += 1
                else:
                    print(f"Warning: Part B data missing for {year} {cat} Q{qnum}")
                    
            # Case 2: In FALLBACK_OPTIONS
            elif (year, cat, qnum) in FALLBACK_OPTIONS:
                fb = FALLBACK_OPTIONS[(year, cat, qnum)]
                q['options'] = fb['options']
                if 'key' in fb:
                    q['correct_answer'] = fb['key']
                    q['correct_option'] = fb['key']
                if 'stem' in fb and fb['stem']:
                    q['stem'] = fb['stem']
                modified = True
                exam_repaired += 1
                total_repaired += 1
                
            # Case 3: Cloze or Reading from PDF Extractor
            else:
                cache_key = (year, cat)
                if cache_key not in pdf_text_cache:
                    pdf_p = get_pdf_path(year, cat)
                    if pdf_p:
                        doc = pymupdf.open(pdf_p)
                        raw = "\n".join([page.get_text() for page in doc])
                        # Pre-clean middle dots and commas after question numbers
                        raw = re.sub(r'(?<=\n)\s*(\d+)\s*[・·•,，]\s*', r'\n\1. ', raw)
                        pdf_text_cache[cache_key] = normalize_text(raw)
                    else:
                        pdf_text_cache[cache_key] = None
                        
                norm_text = pdf_text_cache[cache_key]
                if norm_text:
                    extracted_opts = extract_cloze(norm_text, qnum) if qnum <= 20 else extract_reading(norm_text, qnum)
                    if extracted_opts and len(extracted_opts) == 4:
                        q['options'] = extracted_opts
                        modified = True
                        exam_repaired += 1
                        total_repaired += 1
                    else:
                        print(f"ERROR: Could not extract {year} {cat} Q{qnum} from PDF!")
                else:
                    print(f"ERROR: No PDF for {year} {cat} Q{qnum}!")
                    
        if modified:
            with open(f, 'w', encoding='utf-8') as fp:
                json.dump(d, fp, ensure_ascii=False, indent=2)
            print(f"Updated {year} {cat} ({title}): {exam_repaired} questions calibrated.")

    print(f"\nTotal calibrated questions: {total_repaired}")

if __name__ == "__main__":
    calibrate_all()
