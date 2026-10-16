import glob
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

DATA_DIR = r"d:\A16pro\Aing\antigravity\supabase\public\data\exams"

for fpath in sorted(glob.glob(os.path.join(DATA_DIR, "*.json"))):
    data = json.load(open(fpath, encoding="utf-8"))
    title = data["exam"].get("title", "")
    
    # Check 18: non canonical option orders
    for q in data.get("questions", []):
        so = q.get("sort_order")
        opts = q.get("options")
        if isinstance(opts, list):
            keys = [o.get("key") for o in opts if "key" in o]
            if keys != sorted(keys):
                print(f"[NON-CANONICAL ORDER] {title} Q{so}: {keys}")
                
    # Check 26: corrupted string in passage
    for p in data.get("passages", []):
        pt = p.get("title", "")
        c = p.get("content", "")
        for s in ["o£", "th&r", "s e n no os"]:
            if s in c:
                idx = c.find(s)
                snippet = c[max(0, idx - 40):min(len(c), idx + 60)].replace('\n', ' ')
                print(f"[CORRUPTED STRING IN PASSAGE] {title} - {pt}: '{s}' in snippet: {repr(snippet)}")
