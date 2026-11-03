import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open(r"d:\A16pro\Aing\antigravity\supabase\public\data\exams\ee996af1-3aaa-5380-9465-08125c4db713.json", "r", encoding="utf-8") as f:
    d = json.load(f)

for q in d['questions']:
    qn = q['question_number']
    expl = q.get('explanation', '')
    
    # 1. O followed by Capital letter e.g. OWe, OThe
    matches_o = re.findall(r'[^\w][OQ][A-Z][a-z]+', expl)
    if matches_o:
        print(f"Q{qn} O+Capital: {matches_o}")
        
    # 2. Check for missing spaces after periods between English words: [a-z]\.[A-Z]
    matches_p = re.findall(r'[a-z]\.[A-Z][a-z]+', expl)
    if matches_p:
        print(f"Q{qn} punct_glued: {matches_p}")

    # 3. Check for words concatenated with in/to/the/of: e.g. 'balancesin', 'According tothe', 'trialseach'
    matches_glued_prep = re.findall(r'[a-z]+(?:in|to|of|the|each|for|and)[A-Z][a-z]+', expl)
    if matches_glued_prep:
        print(f"Q{qn} prep_glued: {matches_glued_prep}")
