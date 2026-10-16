import glob
import json
import re
import os

legit_domains = [
    'guardian', 'nytimes', 'economist', 'scientificamerican', 'nature',
    'bbc', 'reuters', 'theatlantic', 'wsj', 'telegraph', 'forbes', 'wired',
    'harvard', 'oxford', 'cambridge', 'wikipedia', 'doi.org', 'wiley',
    'springer', 'cell.com', 'sciencemag', 'pnas', 'mit.edu', 'stanford.edu'
]

pattern = re.compile(r'(?:https?://[^\s\"\'\>\<\,\;]+|www\.[^\s\"\'\>\<\,\;]+|微信|公众号|店铺|旺旺|淘宝|企鹅|QQ群|qq\.com|baidu\.com)')

print("Scanning all 41 exam JSON files for watermarks and URLs...")
watermark_hits = []

for f in sorted(glob.glob(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\*.json")):
    data = json.load(open(f, encoding="utf-8"))
    yr = data["exam"]["year"]
    cat = data["exam"]["category_id"]
    
    # Check questions
    for q in data["questions"]:
        so = q["sort_order"]
        expl = q.get("explanation") or ""
        stem = q.get("stem") or ""
        combined = f"{stem} {expl}"
        matches = pattern.findall(combined)
        bad_matches = [m for m in matches if not any(ld in m.lower() for ld in legit_domains)]
        if bad_matches:
            matching_lines = [l for l in combined.split('\n') if any(m in l for m in bad_matches)]
            watermark_hits.append({
                "file": os.path.basename(f),
                "year": yr,
                "cat": cat,
                "type": "question",
                "so": so,
                "matches": bad_matches,
                "context": matching_lines
            })
            
    # Check passages
    for p in data.get("passages", []):
        so = p["sort_order"]
        content = p.get("content") or ""
        matches = pattern.findall(content)
        bad_matches = [m for m in matches if not any(ld in m.lower() for ld in legit_domains)]
        if bad_matches:
            watermark_hits.append({
                "file": os.path.basename(f),
                "year": yr,
                "cat": cat,
                "type": "passage",
                "so": so,
                "matches": bad_matches
            })

print(f"Total watermark hits found: {len(watermark_hits)}")
for h in watermark_hits:
    print(f"[{h['year']} {h['cat']}] {h['type']} {h['so']}: {h['matches']}")
    if 'context' in h:
        print(f"   Context: {h['context']}")
