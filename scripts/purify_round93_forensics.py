import json, glob, re, os

EXAMS_DIR = 'd:/A16pro/Aing/antigravity/supabase/public/data/exams'
files = sorted(glob.glob(os.path.join(EXAMS_DIR, '*.json')))

fixed_summary = {
    'soft_hyphens': 0,
    'ocr_c_parens': 0,
    'corrupted_brackets': 0,
    'early_cloze_spaced_words': 0,
    'double_punctuation': 0
}

# OCR bracket mappings
CORRUPTED_BRACKETS = [
    ('［ALEE段落之间', '［A］［E］两段之间'),
    ('［AL', '［A］'),
    ('［BL', '［B］'),
    ('［BJ', '［B］'),
    ('［CJ', '［C］'),
    ('［DJ', '［D］'),
    ('[AL]', '[A]'),
    ('[BL]', '[B]'),
    ('[BL', '[B]'),
    ('[BJ', '[B]'),
    ('[CJ', '[C]'),
    ('[DJ', '[D]'),
    ('[AJ', '[A]'),
    ('[A ]', '[A]'),
    ('[B ]', '[B]'),
    ('[C ]', '[C]'),
    ('[D ]', '[D]')
]

# OCR C-as-paren mappings
OCR_C_PARENS = [
    ('tightensC使）', 'tightens（使）'),
    ('frustratedC感到受骗或懊恼）', 'frustrated（感到受骗或懊恼）'),
    ('conditionC必要条件）', 'condition（必要条件）'),
    ('brakesC踩刹车）', 'brakes（踩刹车）'),
    ('occasionC适合该场合的言辞）', 'occasion（适合该场合的言辞）'),
    ('remarkC轻率的言论）', 'remark（轻率的言论）'),
    ('debatesC指向不同的或对立的看法）', 'debates（指向不同的或对立的看法）')
]

# Early cloze broken spacing and typos
EARLY_CLOZE_REPLACEMENTS = [
    ('a lth ough', 'although'),
    ('i g n ori n g', 'ignoring'),
    ('mi ss in g', 'missing'),
    ('a n yway', 'anyway'),
    ('in s t ea d', 'instead'),
    ('th e r e for e', 'therefore'),
    ('Ind eed', 'Indeed'),
    ('Likew i se', 'Likewise'),
    ('Th e refore', 'Therefore'),
    ('Fu rt h ermo r e', 'Furthermore'),
    ('sta nd', 'stand'),
    ('ap pro ve', 'approve'),
    ('r eta in', 'retain'),
    ('nati ves', 'natives'),
    ('inhabit a nt s', 'inhabitants'),
    ('peop l es', 'peoples'),
    ('indi v i d u a l s', 'individuals'),
    ('indi v i', 'indivi'),
    ('confused l y', 'confusedly'),
    ('cheerfu ll y', 'cheerfully'),
    ('hopefu ll y', 'hopefully'),
    ('worried l y', 'worriedly'),
    ('巳 xpo se d', 'exposed'),
    ('st i mu l us', 'stimulus'),
    ('剌激（物）', '刺激（物）'),
    ('catc hing', 'catching'),
    ('b ove', 'above'),
    ('unlik e', 'unlike'),
    ('comm itt ed', 'committed'),
    ('limit ed', 'limited'),
    ('i nsens i t附 to', 'insensitivity to'),
    ('t h ey should/ they should also', 'they should / they should also')
]

# Double punctuation / OCR noise
DOUBLE_PUNCT_REPLACEMENTS = [
    ('transformed from,, . into a woman', 'transformed from ... into a woman'),
    ('cells...),,o 第二句', 'cells...). 第二句'),
    ('smells ，，应体现', 'smells，应体现'),
    ('分别 形成对！！夜， 凸 显 差 别', '分别形成对比，凸显差别'),
    ('and creating jobs,,', 'and creating jobs,')
]

modified_files = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        raw = fp.read()
    
    orig_raw = raw
    
    # 1. Soft hyphens (\u00ad)
    if '\u00ad' in raw:
        cnt = raw.count('\u00ad')
        raw = raw.replace('\u00ad', '')
        fixed_summary['soft_hyphens'] += cnt
        
    # 2. Corrupted brackets
    for old_b, new_b in CORRUPTED_BRACKETS:
        if old_b in raw:
            cnt = raw.count(old_b)
            raw = raw.replace(old_b, new_b)
            fixed_summary['corrupted_brackets'] += cnt

    # 3. OCR C parens
    for old_c, new_c in OCR_C_PARENS:
        if old_c in raw:
            cnt = raw.count(old_c)
            raw = raw.replace(old_c, new_c)
            fixed_summary['ocr_c_parens'] += cnt

    # 4. Early cloze spaced words
    for old_w, new_w in EARLY_CLOZE_REPLACEMENTS:
        if old_w in raw:
            cnt = raw.count(old_w)
            raw = raw.replace(old_w, new_w)
            fixed_summary['early_cloze_spaced_words'] += cnt

    # 5. Double punctuation
    for old_p, new_p in DOUBLE_PUNCT_REPLACEMENTS:
        if old_p in raw:
            cnt = raw.count(old_p)
            raw = raw.replace(old_p, new_p)
            fixed_summary['double_punctuation'] += cnt

    if raw != orig_raw:
        # Validate valid JSON before saving
        data = json.loads(raw)
        with open(f, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=2)
        modified_files += 1

print(f"=== PURIFY ROUND 93 COMPLETE ===")
print(f"Total files modified: {modified_files}")
for k, v in fixed_summary.items():
    print(f"  {k}: {v}")
