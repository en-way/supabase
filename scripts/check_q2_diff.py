import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from db_ops import run_sql

res = run_sql("SELECT explanation FROM questions WHERE exam_id = 'cc4bf627-e456-538f-87e2-4a99ebb613ed' AND sort_order = 2;")
data = res if isinstance(res, list) else json.loads(res)
db_expl = data[0]['explanation'] if data else ''
print('DB Q2 expl len:', len(db_expl))

with open('public/data/exams/cc4bf627-e456-538f-87e2-4a99ebb613ed.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
local_q2 = [q for q in d['questions'] if q['sort_order'] == 2][0]
print('Local Q2 expl len:', len(local_q2['explanation']))

for i in range(min(len(db_expl), len(local_q2['explanation']))):
    if db_expl[i] != local_q2['explanation'][i]:
        print(f'Diff at {i}: DB={db_expl[i]!r} vs Local={local_q2["explanation"][i]!r}')
        print('DB context:', repr(db_expl[max(0, i-20):i+30]))
        print('Local context:', repr(local_q2['explanation'][max(0, i-20):i+30]))
        break
