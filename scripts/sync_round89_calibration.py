import sys
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 89 Calibration Sync to Supabase ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. 2018 ky1 Q8 (id: 39b95d9d-4154-51b2-85b2-8dcb41a07afb)
f2018 = "public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json"
with open(f2018, "r", encoding="utf-8") as fp:
    d2018 = json.load(fp)

q8_2018 = next(q for q in d2018["questions"] if q.get("sort_order") == 8)
opts_2018 = json.dumps(q8_2018["options"], ensure_ascii=False)
expl_2018 = sql_escape(q8_2018["explanation"])

sql_q8 = f"""
UPDATE questions
SET options = '{opts_2018.replace("'", "''")}'::jsonb,
    explanation = {expl_2018}
WHERE id = '{q8_2018['id']}';
"""
db_ops.run_sql(sql_q8)
print(f"Synced 2018 ky1 Q8 options and explanation to Supabase (id: {q8_2018['id']})")

# 2. 2021 ky1 Q23, Q26, Q28
f2021 = "public/data/exams/e7dfeb60-9e71-5912-8e2c-0828e345b98c.json"
with open(f2021, "r", encoding="utf-8") as fp:
    d2021 = json.load(fp)

for so in [23, 26, 28]:
    q = next(item for item in d2021["questions"] if item.get("sort_order") == so)
    sql_q = f"""
UPDATE questions
SET explanation = {sql_escape(q['explanation'])}
WHERE id = '{q['id']}';
"""
    db_ops.run_sql(sql_q)
    print(f"Synced 2021 ky1 Q{so} explanation to Supabase (id: {q['id']})")

print("=== Round 89 Calibration Sync Complete ===")
