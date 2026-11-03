with open("scripts/ky2_reading_passages_raw.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if line.startswith("===") or line.startswith("--- Page"):
        print(f"L{idx:04d}: {line.strip()}")
