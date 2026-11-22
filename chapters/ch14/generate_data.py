"""Generate the Chapter 14 record: 800 elective surgery patients of the general surgery department of two hospitals.

One row is one patient. Columns: patient_id, hospital (A or B), weekday (Mon to Sun, day of admission), asa_class (1 to 4, anesthesia risk class),
los_days (length of stay in days), readmitted (yes/no, readmitted within 30 days), pain_day1 and pain_day3 (pain score from 0 to 10 on the
first and the third day after surgery). Teaching values, not estimates for a real department. Seed 14. Running time: about one second.
"""
from pathlib import Path
import csv
import math
import random

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
DAY_P = [0.2208, 0.2016, 0.1920, 0.1824, 0.1632, 0.0250, 0.0150]
ASA_P = [0.25, 0.40, 0.27, 0.08]
READ_BY_ASA = [0.04, 0.08, 0.13, 0.22]


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(14)
    rows = []
    for i in range(1, 801):
        hospital = "A" if rng.random() < 0.6 else "B"
        weekday = rng.choices(DAYS, DAY_P)[0]
        asa = rng.choices([1, 2, 3, 4], ASA_P)[0]
        los = rng.gammavariate(6.25, 0.79) if hospital == "A" else rng.gammavariate(3.3, 1.7)
        los = max(1, round(los))
        p = READ_BY_ASA[asa - 1] * (1.35 if hospital == "B" else 1.0)
        readmitted = "yes" if rng.random() < p else "no"
        p1 = min(10, max(0, round(rng.gauss(5.4, 1.6))))
        p3 = min(10, max(0, round(p1 - 0.6 + rng.gauss(0, 1.4))))
        rows.append({"patient_id": f"P{i:04d}", "hospital": hospital, "weekday": weekday, "asa_class": asa, "los_days": los,
                     "readmitted": readmitted, "pain_day1": p1, "pain_day3": p3})
    with open(output_dir / "surgery.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "patients written")


if __name__ == "__main__":
    generate()
