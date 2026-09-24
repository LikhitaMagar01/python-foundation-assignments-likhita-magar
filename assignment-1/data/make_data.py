import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(11)

CITIES = ["Kathmandu", "Pokhara", "Biratnagar", "Lalitpur", "Birgunj", "Dharan"]
SUBJECTS = ["Python Programming", "Statistics", "Machine Learning",
            "Databases", "Linear Algebra"]
FIRST = ["Aarav", "Bibek", "Chandni", "Deepika", "Esha", "Faiz", "Gita",
         "Hari", "Ishan", "Jyoti", "Kiran", "Laxmi", "Manish", "Nisha",
         "Ojaswi", "Prakash", "Rita", "Sujan", "Tara", "Umesh"]
LAST = ["Shrestha", "Gurung", "Thapa", "Rai", "Adhikari", "Karki"]


def messy_city(name):
    """Same city, inconsistently typed — students must normalise this."""
    style = random.random()
    if style < 0.25:
        return name.lower()
    if style < 0.45:
        return name.upper()
    if style < 0.70:
        return "  " + name + " "
    return name


def main():
    students = []
    for i in range(40):
        students.append({
            "student_id": 1001 + i,
            "name": f"{FIRST[i % len(FIRST)]} {LAST[i % len(LAST)]}",
            "city": CITIES[i % len(CITIES)],
        })

    start = date(2026, 1, 5)
    rows = []
    for s in students:
        for subject in random.sample(SUBJECTS, 3):
            marks = random.randint(28, 98)
            attendance = round(random.uniform(52, 99), 1)
            exam_date = start + timedelta(days=random.randint(0, 84))
            rows.append({
                "student_id": s["student_id"],
                "name": s["name"],
                "city": messy_city(s["city"]),
                "subject": subject,
                "marks": marks,
                "attendance_percent": attendance,
                "exam_date": exam_date.isoformat(),
            })

    random.shuffle(rows)

    # Missing values: 9 blank attendances, 4 blank marks (no overlap).
    blank_attendance = random.sample(range(len(rows)), 9)
    for i in blank_attendance:
        rows[i]["attendance_percent"] = ""
    blank_marks = random.sample([i for i in range(len(rows))
                                 if i not in blank_attendance], 4)
    for i in blank_marks:
        rows[i]["marks"] = ""

    # Two impossible marks, so describe() has something to catch.
    for i in random.sample([i for i in range(len(rows))
                            if rows[i]["marks"] != ""], 2):
        rows[i]["marks"] = 150

    # Six exact duplicate rows, scattered.
    for i in random.sample(range(len(rows)), 6):
        rows.append(dict(rows[i]))
    random.shuffle(rows)

    out = Path(__file__).with_name("scores_raw.csv")
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "student_id", "name", "city", "subject",
            "marks", "attendance_percent", "exam_date"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {out} — {len(rows)} rows")


if __name__ == "__main__":
    main()