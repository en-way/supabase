import json

file_path = 'public/data/exams/1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

changed = 0
for q in data.get('questions', []):
    opts = q.get('options')
    if isinstance(opts, dict):
        new_opts = []
        for k in sorted(opts.keys()):
            new_opts.append({
                "key": k,
                "text": opts[k],
                "value": k
            })
        q['options'] = new_opts
        changed += 1

print(f"Standardized options to list format for {changed} questions.")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved updated 1ac5713f-fb5d-560f-a22a-3c5c3431d03f.json successfully.")
