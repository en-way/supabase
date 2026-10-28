import sys
import json
import glob

supabase_scripts = r"d:\A16pro\Aing\antigravity\supabase\scripts"
sys.path.append(supabase_scripts)
import db_ops

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 91 Calibration Sync to Supabase ===")

# Sync the 14 passages whose type and section_type were normalized
target_ids = [
    "b4374d5b-74ec-5aaa-815f-3240b17bce48",
    "027994fc-a97b-5b0c-9eec-a8b499cf62fd",
    "ec90837a-70ab-52e5-8b01-92083581086b",
    "9f24f54d-5ab2-5198-b801-988201cf6f5a",
    "1d1a3e13-c857-5497-a0dc-65438288b1ae",
    "71580345-b4ce-57d9-a313-30a09b94c68c",
    "fa949cef-2c2c-5709-9648-dc2a9e9ed7a6",
    "b9f237eb-485a-5206-a698-73bc1cfc4043",
    "c76a6eb9-98a3-5621-9b4e-b007c2adda6e",
    "32b062f2-1e30-4aaf-8069-0bcfbd3ee534",
    "a1544000-9bdb-5015-a707-d9cc0c34ea89",
    "9c54136b-95a2-59d3-8026-72e8728e4dbc",
    "d50924c8-cd18-5461-86f3-1235bc925a5d",
    "1eefd825-1417-5e7a-9ce7-355f2db261f1"
]

exam_files = sorted(glob.glob("public/data/exams/*.json"))
passages_map = {}
for ef in exam_files:
    with open(ef, "r", encoding="utf-8") as fp:
        d = json.load(fp)
    for p in d.get("passages", []):
        if p["id"] in target_ids:
            passages_map[p["id"]] = p

print(f"Found {len(passages_map)} target passages to update in Supabase DB.")

for pid, p in passages_map.items():
    pt = p["type"]
    st = p["section_type"]
    sql = f"""
UPDATE passages
SET type = '{pt}',
    section_type = '{st}'
WHERE id = '{pid}';
"""
    db_ops.run_sql(sql)
    print(f"Synced passage {pid} (so={p['sort_order']}) -> type='{pt}', section_type='{st}'")

print("=== Round 91 Calibration Sync Complete ===")
