import csv
import json

boys = []

with open("boys.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        boys.append({
            "id": int(row["id"]),
            "name": row["name"],
            "status": "נמצא",
            "donations": [],
            "mobile_donations": []
        })

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(boys, f, ensure_ascii=False, indent=2)

print("data.json נוצר בהצלחה!")