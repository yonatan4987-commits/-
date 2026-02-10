import json

DATA_FILE = "data.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

changed = False

for boy in data:
    if "place" not in boy:
        boy["place"] = ""
        changed = True

if changed:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✔ נוסף שדה place לכל בחור שהיה חסר.")
else:
    print("✔ לכל הבחורים כבר יש place — אין מה לתקן.")