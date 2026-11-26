"""Check the key numbers quoted in the Chapter 15 text against the data. Run: python tests/test_ch15.py"""
from pathlib import Path
import json
import pandas as pd
from math import sqrt
from scipy.stats import norm

d = pd.read_csv(Path(__file__).resolve().parents[1] / "chapters/ch15/data/trial.csv"); d["y"] = (d.failure_30d == "yes").astype(int)
s = d[d.allocated == "short"].y; c = d[d.allocated == "standard"].y
th = s.mean() - c.mean(); se = sqrt(s.mean() * (1 - s.mean()) / len(s) + c.mean() * (1 - c.mean()) / len(c))
pp = d[d.allocated == d.received]; ps_ = pp[pp.allocated == "short"].y; pc_ = pp[pp.allocated == "standard"].y
th2 = ps_.mean() - pc_.mean(); se2 = sqrt(ps_.mean() * (1 - ps_.mean()) / len(ps_) + pc_.mean() * (1 - pc_.mean()) / len(pc_))
checks = {
    "rows": (len(d), 1200), "arms": ((len(s), int(s.sum()), len(c), int(c.sum())), (591, 68, 609, 63)),
    "itt": ((round(100 * th, 2), round(100 * se, 2), round(100 * (th + 1.96 * se), 2)), (1.16, 1.8, 4.69)),
    "z p": ((round((th - .05) / se, 2), round(norm.cdf((th - .05) / se), 3)), (-2.13, 0.017)),
    "pp": ((len(pp), round(100 * th2, 2), round(100 * (th2 + 1.96 * se2), 2), round(norm.cdf((th2 - .05) / se2), 3)), (1132, 1.74, 5.33, 0.038)),
    "deviated": (int((d.allocated != d.received).sum()), 68),
    "superiority p": (round(2 * norm.sf(abs(th / se)), 2), 0.52),
}
bad = {k: v for k, v in checks.items() if v[0] != v[1]}
assert not bad, bad
print("all", len(checks), "checks pass")

expected = ["0.0166", "5.33", "0.84", "540", "723", "1638", "0.5193", "4.12", "55.9", "0.0085", "0.474", "0.0204", "33.3", "2.8", "16.0", "5.1", "2.289", "3.471", "2.454", "2.004", "0.535", "40.2", "-6.3", "2.361", "12.9", "0.0166", "4.77", "0.386", "2.32", "0.0085", "0.474", "0.0204", "0.0042", "0.46", "4.4", "1638", "883", "5.7", "54.3", "0.0093", "0.0096", "0.058", "5.1e-06", "0.0042"]
for name in ("ch15_pvalue_meaning_en.ipynb", "ch15_significado_valor_p_pt.ipynb"):
    path = Path(__file__).resolve().parents[1] / "chapters/ch15" / name
    if not path.exists():
        continue
    text = " ".join("".join(o.get("text", "")) for c_ in json.load(open(path))["cells"] if c_["cell_type"] == "code" for o in c_.get("outputs", []))
    missing = [v for v in expected if v not in text]
    assert not missing, (name, missing)
    print(name, "carries all", len(expected), "numbers of the book")
