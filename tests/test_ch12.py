"""Check the key numbers quoted in the Chapter 12 text against the data. Run: python tests/test_ch12.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from scipy import stats

d = pd.read_csv(Path(__file__).resolve().parents[1] / "chapters/ch12/data/calls.csv")
h18 = d[d.hour == 18].groupby("day").size().reindex(range(1, 91), fill_value=0)
w = d.wait_sec
lw = np.log(w)
y = (d.ambulance == "yes").values
blocks = y[: len(y) // 12 * 12].reshape(-1, 12).sum(axis=1)
day1 = d[d.day == 1]
rng = np.random.default_rng(12)
draws = lw.values[rng.integers(0, len(lw), size=(10000, 10))]
tt = (draws.mean(axis=1) - lw.mean()) / (draws.std(axis=1, ddof=1) / np.sqrt(10))
checks = {
    "rows": (len(d), 12472),
    "mean 18h": (round(h18.mean(), 2), 7.52), "variance 18h": (round(h18.var(ddof=0), 2), 8.45), "sd 18h": (round(h18.std(ddof=0), 2), 2.91),
    "range": ((int(h18.min()), int(h18.max())), (2, 15)), "days with 7": (int((h18 == 7).sum()), 11),
    "P(X>=14)": (round(float(stats.poisson.sf(13, h18.mean())), 4), 0.0220), "days >=14": (int((h18 >= 14).sum()), 2),
    "ambulance": ((int(y.sum()), len(y)), (2227, 12472)), "p": (round(y.mean(), 4), 0.1786),
    "P(X>=5)": (round(float(stats.binom.sf(4, 12, y.mean())), 4), 0.0475), "blocks": ((len(blocks), int((blocks >= 5).sum())), (1039, 41)),
    "day 1": ((len(day1), int((day1.ambulance == "yes").sum())), (142, 25)),
    "hypergeometric": ((round(float(stats.hypergeom.pmf(0, 142, 25, 10)), 3), round(float(stats.hypergeom.cdf(1, 142, 25, 10)), 3), round(float(stats.hypergeom.sf(2, 142, 25, 10)), 3)), (0.134, 0.445, 0.247)),
    "wait": ((round(w.mean(), 1), round(w.std(ddof=0), 1), float(w.median()), int(w.max())), (107.3, 71.0, 90.0, 1137)),
    "over 240": ((int((w > 240).sum()), round(100 * (w > 240).mean(), 2)), (611, 4.90)),
    "normal": ((round(float(stats.norm.cdf(0, w.mean(), w.std(ddof=0))), 3), round(float(stats.norm.sf(240, w.mean(), w.std(ddof=0))), 3)), (0.065, 0.031)),
    "log": ((round(lw.mean(), 3), round(lw.std(ddof=0), 3)), (4.496, 0.599)),
    "lognormal": (round(float(stats.norm.sf((np.log(240) - lw.mean()) / lw.std(ddof=0))), 3), 0.050),
    "geometric gaps": ((int(len(np.diff(np.where(y)[0]))), round(float(np.diff(np.where(y)[0]).mean()), 2)), (2226, 5.6)),
    "gap exponential": (round(float(np.concatenate([np.diff(np.sort(g.second.values)) for _, g in d[d.hour == 18].groupby("day")]).mean()), 1), 413.5),
    "n200 exact": (round(float(stats.binom.sf(44, 200, y.mean())), 4), 0.0554),
    "dispersion": ((round(h18.var(ddof=0) / h18.mean(), 2), round(((h18 - h18.mean()) ** 2).sum() / h18.mean(), 1), round(float(stats.chi2.sf(((h18 - h18.mean()) ** 2).sum() / h18.mean(), 89)), 2)), (1.12, 101.1, 0.18)),
    "t simulation": ((round(100 * (abs(tt) > 1.96).mean(), 1), round(100 * (abs(tt) > stats.t.ppf(.975, 9)).mean(), 1)), (8.4, 5.1)),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["7.52", "8.45", "0.022", "0.0475", "0.134", "107.3", "4.9", "0.05", "8.4", "5.1", "16.92", "3.18", "101.1", "413.5", "0.0554", "193.1", "240.1"]
for name in ("ch12_random_variables_en.ipynb", "ch12_variaveis_aleatorias_pt.ipynb"):
    path = Path(__file__).resolve().parents[1] / "chapters/ch12" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [x for x in expected if x not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")

# Part B headings must carry the section number of the exercises in the book (12.13)
for name in ("ch12_random_variables_en.ipynb", "ch12_variaveis_aleatorias_pt.ipynb"):
    path = Path(__file__).resolve().parents[1] / "chapters/ch12" / name
    if not path.exists():
        continue
    heads = [c["source"] if isinstance(c["source"], str) else "".join(c["source"]) for c in json.load(open(path))["cells"] if c["cell_type"] == "markdown"]
    part_b = [h for h in heads if h.startswith("### 12.1") and ("Exercise" in h or "Exercício" in h)]
    assert part_b and all(h.startswith("### 12.13 ") for h in part_b), (name, part_b[:2])
    print(name, "Part B headings carry 12.13")
