"""Generate the Chapter 12 record: 90 days of calls to the emergency call center of a city.

One row is one call. Columns: call_id, day (1 to 90), hour (0 to 23, hour of the call), second (0 to 3599, second of the hour at
which the call arrived; rows are in chronological order), wait_sec (seconds the caller waited until an operator answered),
ambulance (yes/no, an ambulance was sent).
Calls per hour are Poisson with a rate that depends on the hour of the day (8.0 between 18:00 and 18:59);
waits are lognormal (median 90 seconds, shape 0.6); 18% of calls get an ambulance. Teaching values, not estimates for a real service.
Seed 12 (seed 1212 for the second of arrival, drawn separately so that the other columns do not depend on it). Running time: about one second.
"""
from pathlib import Path
import csv
import math
import random

RATES = [3.0, 2.5, 2.2, 2.0, 2.0, 2.5, 3.5, 5.0, 6.5, 7.5, 8.5, 9.0,
         9.0, 8.5, 8.5, 8.0, 8.0, 8.0, 8.0, 7.5, 7.0, 6.0, 4.5, 3.5]


def poisson(rng, lam):
    limit, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limit:
            return k
        k += 1


def generate(output_dir=None):
    output_dir = Path(output_dir) if output_dir is not None else Path(__file__).resolve().parent / "data"
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(12)
    rng_second = random.Random(1212)
    rows, n = [], 0
    for day in range(1, 91):
        for hour in range(24):
            k = poisson(rng, RATES[hour])
            seconds = sorted(rng_second.randrange(3600) for _ in range(k))
            for sec in seconds:
                n += 1
                wait = max(1, round(rng.lognormvariate(math.log(90), 0.6)))
                rows.append({"call_id": f"C{n:05d}", "day": day, "hour": hour, "second": sec, "wait_sec": wait,
                             "ambulance": "yes" if rng.random() < 0.18 else "no"})
    with open(output_dir / "calls.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(len(rows), "calls written")


if __name__ == "__main__":
    generate()
