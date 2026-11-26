"""Generate the Chapter 15 record: a randomized trial of 7 versus 14 days of antibiotic therapy for bloodstream infection with a urinary source.

One row is one enrolled adult. Columns: patient_id (P0001 to P1200, in order of enrollment), site (S01 to S12), month (month of enrollment,
1 to 24), allocated (short = 7 days, standard = 14 days), received (the course actually given), failure_30d (yes/no, clinical failure within
30 days). Patients who did not receive the course they were allocated (5% of the short arm, 6% of the standard arm) have a 1.6 times higher
risk of failure. Teaching values, not estimates for a real trial. Seed 1964. Running time: about one second.
"""
from pathlib import Path
import csv
import random


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(1964)
    rows = []
    for i in range(1, 1201):
        site = 1 + (i - 1) % 12
        allocated = "short" if rng.random() < 0.5 else "standard"
        deviates = rng.random() < (0.05 if allocated == "short" else 0.06)
        received = ("standard" if allocated == "short" else "short") if deviates else allocated
        p = 0.095 if received == "standard" else 0.115
        if deviates:
            p *= 1.6
        failure = "yes" if rng.random() < p else "no"
        rows.append({"patient_id": f"P{i:04d}", "site": f"S{site:02d}", "month": 1 + (i - 1) * 24 // 1200, "allocated": allocated,
                     "received": received, "failure_30d": failure})
    with open(output_dir / "trial.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "patients written")


if __name__ == "__main__":
    generate()
