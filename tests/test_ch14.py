"""Check the key numbers quoted in the Chapter 14 text against the data. Run: python tests/test_ch14.py"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
from math import sqrt
from scipy import stats

d = pd.read_csv(Path(__file__).resolve().parents[1] / "chapters/ch14/data/surgery.csv")
x = d.los_days.values; n = len(x); m = x.mean(); s = x.std(ddof=1)
a = d[d.hospital == "A"].los_days.values; b = d[d.hospital == "B"].los_days.values
t1 = stats.ttest_1samp(x, 5); w = stats.ttest_ind(b, a, equal_var=False); st = stats.ttest_ind(b, a)
k = int((d.readmitted == "yes").sum())
tab = pd.crosstab(d.hospital, d.readmitted); ch = stats.chi2_contingency(tab, correction=False)
checks = {
    "rows": (n, 800), "mean sd": ((round(m, 3), round(s, 3)), (5.344, 2.690)),
    "t one-sample": ((round(t1.statistic, 2), round(t1.pvalue, 5)), (3.61, 0.00032)),
    "readmitted": ((k, round(100 * k / n, 2)), (95, 11.88)),
    "z proportion": (round((k / n - .10) / sqrt(.09 / n), 2), 1.77),
    "hospital means": ((len(a), round(a.mean(), 2), round(a.std(ddof=1), 2), len(b), round(b.mean(), 2), round(b.std(ddof=1), 2)), (467, 5.05, 2.13, 333, 5.75, 3.28)),
    "student welch": ((round(st.statistic, 3), round(w.statistic, 3), round(w.pvalue, 5)), (3.668, 3.427, 0.00066)),
    "F": (round(b.var(ddof=1) / a.var(ddof=1), 2), 2.37),
    "paired pilot": (round(stats.ttest_rel(d.pain_day3[:30], d.pain_day1[:30]).pvalue, 3), 0.524),
    "chi2 hospital": ((round(ch[0], 3), round(ch[1], 3)), (2.049, 0.152)),
    "n for 0.5 day": (int(np.ceil((stats.norm.ppf(.975) + stats.norm.ppf(.8)) ** 2 * s ** 2 / .25)), 228),
}
bad = {k_: v for k_, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["43.0", "3.61", "0.00032", "0.0003", "5.55", "22.25", "227.2", "228", "46.0", "480.7", "315.8", "230", "3.668", "3.427", "0.00066", "2.367", "56.9", "0.524", "-0.645", "-0.73", "-0.53", "66.7", "19.9", "2.049", "0.269", "1.48", "0.032", "5.91", "34.9", "42.2", "77.8", "80.4", "-1.2", "8.1", "22.9", "12.4", "1.768"]
for name in ("ch14_hypothesis_testing_en.ipynb", "ch14_testes_hipoteses_pt.ipynb"):
    path = Path(__file__).resolve().parents[1] / "chapters/ch14" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c in json.load(open(path))["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")
