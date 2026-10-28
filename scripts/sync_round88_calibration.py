import sys
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 88 Calibration Sync to Supabase ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Sync 2011 ky2 Passage 3, Q26, Q29
f2011 = "public/data/exams/53a52573-0afc-51a4-86b6-b2f321cbe6a8.json"
with open(f2011, "r", encoding="utf-8") as f:
    d2011 = json.load(f)

p3_2011 = [p for p in d2011["passages"] if p["sort_order"] == 3][0]
p3_2011_id = p3_2011["id"]
content_2011 = sql_escape(p3_2011["content"])

sql_p3_2011 = f"""
UPDATE passages
SET content = {content_2011}
WHERE id = '{p3_2011_id}';
"""
db_ops.run_sql(sql_p3_2011)
print(f"Synced 2011 ky2 Passage 3 to Supabase (id: {p3_2011_id})")

q26_2011 = [q for q in d2011["questions"] if q["sort_order"] == 26][0]
sql_q26_2011 = f"""
UPDATE questions
SET stem = {sql_escape(q26_2011['stem'])}
WHERE id = '{q26_2011['id']}';
"""
db_ops.run_sql(sql_q26_2011)
print(f"Synced 2011 ky2 Q26 stem to Supabase (id: {q26_2011['id']})")

q29_2011 = [q for q in d2011["questions"] if q["sort_order"] == 29][0]
opts_2011 = json.dumps(q29_2011["options"], ensure_ascii=False)
sql_q29_2011 = f"""
UPDATE questions
SET options = '{opts_2011.replace("'", "''")}'::jsonb
WHERE id = '{q29_2011['id']}';
"""
db_ops.run_sql(sql_q29_2011)
print(f"Synced 2011 ky2 Q29 options to Supabase (id: {q29_2011['id']})")

# 2. Sync 2005 ky1 Passage 3
f2005 = "public/data/exams/d8ba7d14-5305-538d-b81b-f0f7ef3db461.json"
with open(f2005, "r", encoding="utf-8") as f:
    d2005 = json.load(f)

p3_2005 = [p for p in d2005["passages"] if p["sort_order"] == 3][0]
p3_2005_id = p3_2005["id"]
content_2005 = sql_escape(p3_2005["content"])

sql_p3_2005 = f"""
UPDATE passages
SET content = {content_2005}
WHERE id = '{p3_2005_id}';
"""
db_ops.run_sql(sql_p3_2005)
print(f"Synced 2005 ky1 Passage 3 to Supabase (id: {p3_2005_id})")

print("=== Round 88 Calibration Sync Complete ===")
