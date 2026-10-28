import sys
import os
import json

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 87 Calibration Sync to Supabase ===")

def sql_escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# 1. Sync 2021 ky1 Q35
f2021 = "public/data/exams/e7dfeb60-9e71-5912-8e2c-0828e345b98c.json"
with open(f2021, "r", encoding="utf-8") as f:
    d2021 = json.load(f)

q35 = [q for q in d2021["questions"] if q["sort_order"] == 35][0]
q35_id = q35["id"]
q35_opts_json = json.dumps(q35["options"], ensure_ascii=False)

sql_q35 = f"""
UPDATE questions
SET options = '{q35_opts_json.replace("'", "''")}'::jsonb
WHERE id = '{q35_id}';
"""
db_ops.run_sql(sql_q35)
print(f"Synced 2021 ky1 Q35 options to Supabase (id: {q35_id})")

# 2. Sync 2017 ky1 Q41-Q45
f2017 = "public/data/exams/4fd42872-4822-5786-8d16-0317051bf03d.json"
with open(f2017, "r", encoding="utf-8") as f:
    d2017 = json.load(f)

for q in d2017["questions"]:
    if q["sort_order"] >= 41:
        qid = q["id"]
        opts_json = json.dumps(q["options"], ensure_ascii=False)
        sql_pb = f"""
        UPDATE questions
        SET options = '{opts_json.replace("'", "''")}'::jsonb
        WHERE id = '{qid}';
        """
        db_ops.run_sql(sql_pb)
        print(f"Synced 2017 ky1 Q{q['sort_order']} options to Supabase (id: {qid})")

print("=== Round 87 Calibration Sync Complete ===")
