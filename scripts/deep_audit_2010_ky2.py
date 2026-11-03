import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_id = "207d2963-734a-52bd-9fa3-6c341efb5974"
json_path = f"public/data/exams/{exam_id}.json"

print(f"=== Deep Audit 2010 ky2: {json_path} ===")

with open(json_path, 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Title in root:", d.get('title'))
print("Exam object:", d.get('exam'))

passages = d.get('passages', [])
print(f"\nPassages Count: {len(passages)}")
for i, p in enumerate(passages):
    pid = p.get('id')
    ptype = p.get('type')
    pnum = p.get('passage_number')
    title = p.get('title')
    content = p.get('content', '')
    words = len(content.split())
    paras = content.count('\n\n') + 1
    print(f"Passage {i}: id={pid}, type={ptype}, num={pnum}, title={title}, paras={paras}, words={words}")
    lines = [l.strip() for l in content.split('\n') if l.strip()]
    if lines:
        print(f"   First line: {lines[0][:60]}")
        print(f"   Last line:  {lines[-1][-60:]}")

questions = d.get('questions', [])
print(f"\nQuestions Count: {len(questions)}")
missing_qnum = 0
missing_type = 0
pts_sum = 0.0

for idx, q in enumerate(questions):
    so = q.get('sort_order')
    qnum = q.get('question_number')
    qtype = q.get('type') or q.get('q_type')
    pts = q.get('points')
    ans = q.get('correct_answer')
    stem = q.get('stem', '')
    expl = q.get('explanation', '')
    opts = q.get('options', [])
    
    if qnum is None:
        missing_qnum += 1
    if qtype is None:
        missing_type += 1
    if pts:
        pts_sum += float(pts)
        
    if idx < 3 or idx in [19, 20, 24, 25, 39, 40, 44]:
        print(f"Q{idx+1} (so={so}, num={qnum}, type={qtype}, pts={pts}, ans={ans}):")
        print(f"   Stem: {stem[:60]}")
        print(f"   Opts: {len(opts)} options -> {[o.get('key')+': '+o.get('text')[:20] for o in opts] if isinstance(opts, list) else opts}")
        print(f"   Expl (len={len(expl)}): {expl[:60]}...{expl[-40:] if len(expl)>40 else ''}")

print(f"\nAudit Summary: Missing QNum={missing_qnum}, Missing Type={missing_type}, Total Points={pts_sum}")
