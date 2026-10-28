import sys
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 90 Calibration Sync to Supabase ===")

# 1. 2022 ky1 Q38 & Q39
f2022 = "public/data/exams/6d676d85-a38a-5fe4-9506-31de03b648b6.json"
with open(f2022, "r", encoding="utf-8") as fp:
    d2022 = json.load(fp)

for so in [38, 39]:
    q = next(item for item in d2022["questions"] if item.get("sort_order") == so)
    opts_json = json.dumps(q["options"], ensure_ascii=False)
    sql_q = f"""
UPDATE questions
SET options = '{opts_json.replace("'", "''")}'::jsonb
WHERE id = '{q['id']}';
"""
    db_ops.run_sql(sql_q)
    print(f"Synced 2022 ky1 Q{so} options to Supabase (id: {q['id']})")

# 2. 2018 ky1 Q22
f2018 = "public/data/exams/e95fe05a-07f4-53d1-a11f-9b636acc6469.json"
with open(f2018, "r", encoding="utf-8") as fp:
    d2018 = json.load(fp)

q22 = next(item for item in d2018["questions"] if item.get("sort_order") == 22)
opts_json = json.dumps(q22["options"], ensure_ascii=False)
sql_q22 = f"""
UPDATE questions
SET options = '{opts_json.replace("'", "''")}'::jsonb
WHERE id = '{q22['id']}';
"""
db_ops.run_sql(sql_q22)
print(f"Synced 2018 ky1 Q22 options to Supabase (id: {q22['id']})")

# 3. 2025 ky1 Q41-Q45
f2025 = "public/data/exams/c75ee9ef-ec21-5396-b3bf-4e30260d2918.json"
with open(f2025, "r", encoding="utf-8") as fp:
    d2025 = json.load(fp)

for so in range(41, 46):
    q = next(item for item in d2025["questions"] if item.get("sort_order") == so)
    opts_json = json.dumps(q["options"], ensure_ascii=False)
    sql_q = f"""
UPDATE questions
SET options = '{opts_json.replace("'", "''")}'::jsonb
WHERE id = '{q['id']}';
"""
    db_ops.run_sql(sql_q)
    print(f"Synced 2025 ky1 Q{so} options to Supabase (id: {q['id']})")

print("=== Round 90 Calibration Sync Complete ===")
