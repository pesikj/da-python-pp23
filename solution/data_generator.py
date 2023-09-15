import random
import datetime
import json

employees = {"Marta Nováková": [0, 1], "Michael Rostock-Poplar": [1, 2, 3], "Ondřej Bartoš": [4], "Daniela Bérová": [0, 2], "Ivan Pilný": [2, 3]}
record_types = ["work", "holiday", "care", "unpaid"]
remaining_holiday = {"Marta Nováková": 15, "Michael Rostock-Poplar": 12, "Ondřej Bartoš": 5, "Daniela Bérová": 21, "Ivan Pilný": 4}
project_list = ["DataDive", "TrendVision", "PulseCheck", "Mandala", "FinanceFlare"]
"""
[
{"date": "2023-08-01", "employee": "Marta Nováková", "record_type": "work", "worked_on": {"DataDive": 5, "Mandala": 4}},
{"date": "2023-08-02", "employee": "Marta Nováková", "record_type": "holiday"},
]
"""

data = []

for employee in employees:
    previous_activity = None
    holiday_segments = 0
    for day in range(1, 32):
        date = datetime.datetime(2023, 8, day).date()
        if date.isoweekday() in (6, 7):
            continue
        row = {"date": str(date), "employee": employee}
        random_number = random.uniform(0, 1)
        if (random_number < 0.3 or (previous_activity == "holiday" and random_number < 0.5)) and remaining_holiday[employee] > 0  and previous_activity != "care" and holiday_segments <= 2:
            row["record_type"] = "holiday"
            data.append(row)
            remaining_holiday[employee] -= 1
            previous_activity = "holiday"
            if previous_activity != "holiday":
                holiday_segments += 1
            continue
        random_number = random.uniform(0, 1)
        if (random_number < 0.05 or (previous_activity == "care" and random_number < 0.3)):
            row["record_type"] = "care"
            data.append(row)
            previous_activity = "care"
            continue
        random_number = random.uniform(0, 1)
        if random_number < 0.01:
            row["record_type"] = "unpaid"
            data.append(row)
            previous_activity = "unpaid"
            continue
        row["record_type"] = "work"
        worked_on = {}
        current_projects = employees[employee].copy()
        project_count = random.randint(1, len(current_projects))
        remaining_hours = random.randint(6, 10)
        for _ in range(project_count):
            if remaining_hours == 0:
                break
            if len(current_projects) > 1:
                hours = random.randint(min(remaining_hours, 6), remaining_hours)
            else:
                hours = remaining_hours
            project_id = random.choice(current_projects)
            current_projects.remove(project_id)
            worked_on[project_list[project_id]] = hours
            remaining_hours -= hours
            previous_activity = "work"
        row["worked_on"] = worked_on
        data.append(row)

with open("work_hours.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
