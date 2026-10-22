# -*- coding: utf-8 -*-
import json
import sys

sys.path.append(r'd:\A16pro\Aing\antigravity\supabase\scripts')
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

p = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\111d6c78-81a1-53dc-a039-dad4c94ebd35.json'
with open(p, 'r', encoding='utf-8') as f:
    d = json.load(f)

q20 = d['questions'][19]
exp = q20['explanation']

# Remove Section H Reading Comprehension
if 'Section H Reading Comprehension' in exp:
    exp = exp.replace('\nSection H Reading Comprehension', '').strip()
    # Also clean newline inside quotes if needed
    exp = exp.replace('用于引出“和 \n之前情况相反的内容”', '用于引出“和之前情况相反的内容”')
    q20['explanation'] = exp
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"Local Q20 fixed! Len: {len(q20['explanation'])}")
    print("End of expl:", repr(exp[-50:]))
    
    # sync to DB
    sql_exp = q20['explanation'].replace("'", "''")
    db_ops.run_sql(f"UPDATE questions SET explanation = '{sql_exp}' WHERE id = '{q20['id']}';")
    print("DB Q20 synchronized!")
else:
    print("Pattern not found!")
