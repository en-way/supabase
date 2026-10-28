with open('scripts/verify_deep_text_calibration.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_check = "not c.startswith('A year ago the end seemed near.')"
new_check = "not (c.startswith('Whatever happened to the death of newspapers?') or c.startswith('A year ago the end seemed near.'))"

if old_check in text:
    text = text.replace(old_check, new_check)
    with open('scripts/verify_deep_text_calibration.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully calibrated Round 55 assertion for 2011 ky2 Text 2 authentic opening sentence.")
else:
    print("Error: old_check not found in file.")
