import json

def fix_data():
    # טוען את הקובץ
    with open("data.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    # אם הקובץ הוא רשימה של אנשים – עוטפים אותו במבנה חדש
    if isinstance(raw, list):
        data = {
            "days": [],
            "active_day": None,
            "people": raw
        }
    else:
        data = raw
        data.setdefault("days", [])
        data.setdefault("active_day", None)
        data.setdefault("people", [])

    # עובר על כל בחור ומוסיף שדות חסרים
    for person in data["people"]:
        person.setdefault("donations", [])
        person.setdefault("mobile_donations", [])
        person.setdefault("place", "")

    # שומר את הקובץ בחזרה
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("הקובץ תוקן בהצלחה ✔️")

fix_data()