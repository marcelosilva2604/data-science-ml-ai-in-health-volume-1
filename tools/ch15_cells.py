"""All code cells of the Chapter 15 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered
comments, output as plain sentences. Beginner-friendly Python: print with commas, round(), no f-strings, no helper functions.
Written once in English; the Portuguese cell is the same code with every comment and printed text translated whole through
the PT table in tools/ch15_pt.py (added with the Portuguese edition)."""
import re

try:
    from ch15_pt import PT
except ImportError:
    PT = {}


def tr(code):
    def comment(m):
        text = m.group(2)
        if text not in PT:
            raise KeyError("comment not translated: " + text)
        return m.group(1) + "# " + PT[text]
    def literal(m):
        text = m.group(1)
        if text in PT:
            return '"' + PT[text] + '"'
        if " " in text or text.endswith(":") or text.endswith("="):
            raise KeyError("string not translated: " + text)
        return m.group(0)
    code = re.sub(r'(^|\s)# ([^\n"]*)', comment, code, flags=re.M)
    return re.sub(r'"([^"\n]*)"', literal, code)


LOAD = '''# 1. Read the trial file: one row is one enrolled patient
import numpy as np
import pandas as pd
from math import sqrt, ceil, log2
from scipy import stats
from scipy.stats import norm, multivariate_normal
from scipy.optimize import brentq
from scipy.integrate import quad

df = pd.read_csv("data/trial.csv")

# 2. Count rows and columns
rows, columns = df.shape
print("The trial file has", rows, "rows (one per patient) and", columns, "columns.")

# 3. Add a helper column that is 1 for a failure and 0 otherwise (the notebook's calculations use it)
df["fail"] = (df["failure_30d"] == "yes").astype(int)
df.head()                                      # The first five rows
'''

C_NI = '''# 1. Failures in each arm, by allocation
short = df[df["allocated"] == "short"]["fail"]
standard = df[df["allocated"] == "standard"]["fail"]
n_s, k_s, p_s = len(short), int(short.sum()), short.mean()
n_c, k_c, p_c = len(standard), int(standard.sum()), standard.mean()
print("Short:", k_s, "of", n_s, "(", round(100 * p_s, 1), "%); standard:", k_c, "of", n_c, "(", round(100 * p_c, 1), "%)")

# 2. Difference, standard error, upper limit, and the test against the margin of 0.05
margin = 0.05
theta = p_s - p_c
se = sqrt(p_s * (1 - p_s) / n_s + p_c * (1 - p_c) / n_c)
z_ni = (theta - margin) / se
print("Difference:", round(100 * theta, 2), "points; standard error:", "%.2f" % (100 * se), "points")
print("95% CI:", round(100 * (theta - 1.96 * se), 1), "to", round(100 * (theta + 1.96 * se), 1), "; z =", round(z_ni, 2), "; one-sided p =", round(norm.cdf(z_ni), 4))

# 3. Reading: noninferiority is shown when the upper limit is below the margin
if theta + 1.96 * se < margin:
    print("The upper limit is below the margin of 5 points: noninferiority is shown by allocation.")
else:
    print("The upper limit is not below the margin of 5 points: noninferiority is not shown by allocation.")
'''

C_ITT = '''# 1. Patients who did not receive the course they were assigned
deviated = df[df["allocated"] != df["received"]]
print("Deviated:", len(deviated), "(short to standard:", int(((df["allocated"] == "short") & (df["received"] == "standard")).sum()), "; standard to short:", int(((df["allocated"] == "standard") & (df["received"] == "short")).sum()), ")")
print("Failure among deviators:", round(100 * deviated["fail"].mean(), 1), "%; among the others:", round(100 * df[df["allocated"] == df["received"]]["fail"].mean(), 1), "%")

# 2. Per-protocol analysis: patients who received what they were assigned
pp = df[df["allocated"] == df["received"]]
pp_s = pp[pp["allocated"] == "short"]["fail"]
pp_c = pp[pp["allocated"] == "standard"]["fail"]
theta_pp = pp_s.mean() - pp_c.mean()
se_pp = sqrt(pp_s.mean() * (1 - pp_s.mean()) / len(pp_s) + pp_c.mean() * (1 - pp_c.mean()) / len(pp_c))
z_pp = (theta_pp - margin) / se_pp
print("Per protocol:", len(pp), "patients;", int(pp_s.sum()), "of", len(pp_s), "and", int(pp_c.sum()), "of", len(pp_c))
print("Difference:", round(100 * theta_pp, 2), "points; standard error:", "%.2f" % (100 * se_pp), "; upper limit:", round(100 * (theta_pp + 1.96 * se_pp), 2), "; z =", round(z_pp, 2), "; one-sided p =", round(norm.cdf(z_pp), 3))

# 3. Reading
if theta_pp + 1.96 * se_pp < margin:
    print("Per protocol the upper limit is below the margin: noninferiority is shown.")
else:
    print("Per protocol the upper limit is not below the margin: noninferiority is not shown.")
'''

C_TOST = '''# 1. Two one-sided tests against the margins -0.05 and +0.05
z_low = (theta + margin) / se
p_low = norm.sf(z_low)
p_up = norm.cdf((theta - margin) / se)
print("Lower test: z =", round(z_low, 2), "; p =", round(p_low, 5), "; upper test: p =", round(p_up, 4))

# 2. The TOST p-value is the larger of the two
print("TOST p =", round(max(p_low, p_up), 4), "; 95% CI inside the margins:", theta - 1.96 * se > -margin and theta + 1.96 * se < margin)
if max(p_low, p_up) < 0.025:
    print("Both one-sided tests reject: equivalence within 5 points is shown by allocation.")
'''

C_SIZE = '''# 1. Patients per arm for a noninferiority test with equal courses and a standard failure rate of 9.5%
za = norm.ppf(0.975)
p0 = 0.095
for power, zb in (("80%", norm.ppf(0.80)), ("90%", norm.ppf(0.90))):
    n_arm = (za + zb) ** 2 * (2 * p0 * (1 - p0)) / margin ** 2
    print("Power", power, ": patients per arm", round(n_arm, 1), "-> rounded up", ceil(n_arm))

# 2. Power of 600 patients per arm for a true loss of 0, 1, 2, and 3 points
for loss in (0.0, 0.01, 0.02, 0.03):
    se_true = sqrt(p0 * (1 - p0) / 600 + (p0 + loss) * (1 - p0 - loss) / 600)
    print("True loss (points):", round(100 * loss), "; power", round(norm.cdf((margin - loss) / se_true - za), 3))

# 3. Patients per arm for 80% power when the short course is truly 2 points worse
loss = 0.02
print("Patients per arm for a 2-point loss:", ceil((za + 0.8416) ** 2 * (p0 * (1 - p0) + (p0 + loss) * (1 - p0 - loss)) / (margin - loss) ** 2))

# 4. Simulation: 10,000 trials of 600 per arm; share declaring noninferiority for several true losses
rng = np.random.default_rng(15)
for loss in (0.05, 0.0, 0.01, 0.02):
    standard_rate = rng.binomial(600, p0, 10000) / 600
    short_rate = rng.binomial(600, p0 + loss, 10000) / 600
    standard_vs_short = short_rate - standard_rate
    se_sim = np.sqrt(standard_rate * (1 - standard_rate) / 600 + short_rate * (1 - short_rate) / 600)
    print("True loss (points):", round(100 * loss), "; noninferiority declared in", round(100 * ((standard_vs_short) + 1.96 * se_sim < margin).mean(), 1), "% of the trials")
'''

C_DUAL = '''# 1. Tests of two hypothesized differences and the limits of the 95% interval
for theta0 in (0.0, 0.05, theta - 1.96 * se, theta + 1.96 * se):
    print("Hypothesized difference", round(100 * theta0, 2), "points: two-sided p =", round(2 * norm.sf(abs((theta - theta0) / se)), 4))

# 2. The 95% interval and whether it contains 0 and 0.05
low = theta - 1.96 * se
high = theta + 1.96 * se
print("95% CI:", round(100 * low, 2), "to", round(100 * high, 2), "; contains 0:", low < 0 < high, "; contains 0.05:", low < 0.05 < high)
'''

C_PFUN = '''# 1. P-value function at several hypothesized differences (points)
for theta0 in (-4, 0, 100 * theta, 2, 3, 4, 5, 6, 7):
    print("Hypothesized", round(theta0, 2), "points: p =", round(2 * norm.sf(abs((theta - theta0 / 100) / se)), 4))

# 2. The two hypotheses with the same p-value as zero, and the 90% interval
print("Same p-value as 0:", 0, "and", round(200 * theta, 2), "points; 90% CI:", round(100 * (theta - 1.645 * se), 2), "to", round(100 * (theta + 1.645 * se), 2))
'''

C_SVAL = '''# 1. S-values: bits of surprise, -log2(p)
for p in (0.52, 0.05, 0.033, 0.001):
    print("p =", p, ": S-value", round(-log2(p), 2), "bits")

# 2. The p-values of this trial in bits
print("Test of no difference:", round(-log2(2 * norm.sf(abs(theta / se))), 2), "bits; test of a 5-point loss:", round(-log2(2 * norm.sf(abs((theta - margin) / se))), 2), "bits")
'''

C_MISREAD = '''# 1. Resample the trial's patients 2,000 times and recompute the one-sided noninferiority p-value
rng = np.random.default_rng(15)
y = df["fail"].values
idx_s = np.where(df["allocated"] == "short")[0]
idx_c = np.where(df["allocated"] == "standard")[0]
p_boot = []
for repetition in range(2000):
    xs = y[rng.choice(idx_s, len(idx_s))]
    xc = y[rng.choice(idx_c, len(idx_c))]
    se_b = sqrt(xs.mean() * (1 - xs.mean()) / len(xs) + xc.mean() * (1 - xc.mean()) / len(xc))
    p_boot.append(norm.cdf((xs.mean() - xc.mean() - margin) / se_b))
p_boot = np.array(p_boot)
print("Smallest p:", float("%.2g" % p_boot.min()), "; median:", round(np.median(p_boot), 4), "; largest:", round(p_boot.max(), 3), "; rule met in", round(100 * (p_boot < 0.025).mean(), 1), "% of the resamples")

# 2. Power computed at the observed estimate, for the test of no difference
z_obs = theta / se
print("Observed z:", round(z_obs, 2), "; two-sided p =", round(2 * norm.sf(abs(z_obs)), 3), "; observed power:", round(norm.sf(1.96 - z_obs) + norm.cdf(-1.96 - z_obs), 3))
'''

C_IMPORTANT = '''# 1. The test of no difference with the observed difference and failure rates held fixed, for larger trials
for n_arm in (591, 3000, 10000, 30000):
    se_n = sqrt((p_s * (1 - p_s) + p_c * (1 - p_c)) / n_arm)       # standard error with n_arm patients in each arm
    z_n = theta / se_n
    print("Patients per arm", n_arm, ": z =", round(z_n, 2), "; two-sided p =", "%.2g" % (2 * norm.sf(abs(z_n))))
'''

C_FALSE = '''# 1. Share of significant results that are false, for each share of real hypotheses and power (alpha = 0.05)
for real in (0.5, 0.1, 0.01):
    shares = []
    for power in (0.8, 0.5, 0.2):
        shares.append(round((1 - real) * 0.05 / ((1 - real) * 0.05 + real * power), 3))
    print("Real hypotheses", round(100 * real), "%: power 0.8, 0.5, 0.2 ->", shares)

# 2. The example of 1,000 hypotheses, 100 of them real, power 0.50
false_positives = 900 * 0.05
true_positives = 100 * 0.50
print("False positives:", false_positives, "; true positives:", true_positives, "; share false:", round(false_positives / (false_positives + true_positives), 3))
'''

C_MULTI = '''# 1. Difference and Fisher's exact p-value at each of the 12 sites
site_p = []
for site, group in df.groupby("site"):
    a = group[group["allocated"] == "short"]["fail"]
    b = group[group["allocated"] == "standard"]["fail"]
    table = [[int(a.sum()), len(a) - int(a.sum())], [int(b.sum()), len(b) - int(b.sum())]]
    p_site = stats.fisher_exact(table)[1]
    site_p.append(p_site)
    print(site, ": short", int(a.sum()), "of", len(a), "; standard", int(b.sum()), "of", len(b), "; Fisher p =", round(p_site, 4))    # p = 1.0: almost the same failure rate in both arms
print("Sites with p < 0.05:", sum(p < 0.05 for p in site_p), "; Bonferroni threshold:", round(0.05 / 12, 4), "; chance of at least one in 12 independent tests:", round(1 - 0.95 ** 12, 3))

# 2. Shuffle the allocation labels 2,000 times (no difference by construction) and count the smallest site p-value
rng = np.random.default_rng(15)
y = df["fail"].values
labels = (df["allocated"] == "short").values
site_ix = [np.where(df["site"].values == s)[0] for s in sorted(df["site"].unique())]
any_005 = 0
any_bonf = 0
for repetition in range(2000):
    shuffled = rng.permutation(labels)
    smallest = 1
    for ix in site_ix:
        is_short = shuffled[ix]
        yy = y[ix]
        table = [[yy[is_short].sum(), is_short.sum() - yy[is_short].sum()], [yy[~is_short].sum(), (~is_short).sum() - yy[~is_short].sum()]]
        smallest = min(smallest, stats.fisher_exact(table)[1])
    any_005 = any_005 + (smallest < 0.05)
    any_bonf = any_bonf + (smallest < 0.05 / 12)
print("Shuffled trials with a site p < 0.05:", round(100 * any_005 / 2000, 1), "%; with a site p < 0.0042:", round(100 * any_bonf / 2000, 1), "%")
'''

C_PEEK = '''# 1. Shuffle the allocation labels 4,000 times and test after every 200 patients (six looks), two-sided
rng = np.random.default_rng(15)
labels = (df["allocated"] == "short").values
y = df["fail"].values
looks = [200, 400, 600, 800, 1000, 1200]
reject_196 = 0
reject_pocock = 0
reject_final = 0
for repetition in range(4000):
    shuffled = rng.permutation(labels)
    z_looks = []
    for n_look in looks:
        is_short = shuffled[:n_look]
        yy = y[:n_look]
        p_all = yy.mean()                                          # failure rate of all patients so far: the standard error under the null hypothesis
        se_look = sqrt(p_all * (1 - p_all) * (1 / is_short.sum() + 1 / (n_look - is_short.sum())))
        z_looks.append(abs(yy[is_short].mean() - yy[~is_short].mean()) / se_look)
    z_looks = np.array(z_looks)
    reject_196 = reject_196 + (z_looks > 1.96).any()
    reject_pocock = reject_pocock + (z_looks > 2.453).any()
    reject_final = reject_final + (z_looks[-1] > 1.96)
print("True null rejected: final look only", round(100 * reject_final / 4000, 1), "%; six looks at 1.96:", round(100 * reject_196 / 4000, 1), "%; six looks at 2.453:", round(100 * reject_pocock / 4000, 1), "%")
print("If the six looks were independent:", round(100 * (1 - 0.95 ** 6), 1), "%")
'''

C_SEQ = '''# 1. Correlation of the statistics at equally spaced looks: sqrt(t_i / t_j)
n_looks = 3
t = np.arange(1, n_looks + 1) / n_looks                       # information fractions 1/3, 2/3, 1
corr = np.sqrt(np.minimum.outer(t, t) / np.maximum.outer(t, t))
print("Correlation matrix of three looks:", np.round(corr, 3).tolist())

# 2. Pocock and O'Brien-Fleming boundaries for three looks, total one-sided level 0.025 (two-sided 0.05)
# 1 minus the joint normal probability of no crossing is the probability of crossing at any look; brentq searches for the boundary that makes it 0.025
mv3 = multivariate_normal(mean=np.zeros(3), cov=corr, seed=1, abseps=1e-8, releps=1e-8)
pocock = brentq(lambda c: 1 - mv3.cdf(np.array([c, c, c])) - 0.025, 1.5, 4)
obf_c = brentq(lambda c: 1 - mv3.cdf(np.array([c * sqrt(3 / k) for k in (1, 2, 3)])) - 0.025, 1.5, 4)
print("Pocock:", round(pocock, 3), "; O'Brien-Fleming:", [round(obf_c * sqrt(3 / k), 3) for k in (1, 2, 3)])
print("Nominal two-sided levels: Pocock", round(2 * norm.sf(pocock), 4), "; O'Brien-Fleming", [round(float(2 * norm.sf(obf_c * sqrt(3 / k))), 4) for k in (1, 2, 3)])

# 3. Lan-DeMets spending function at one third, two thirds, and the end
print("Spending:", [round(float(2 - 2 * norm.cdf(1.96 / sqrt(t_k))), 4) for t_k in (1 / 3, 2 / 3, 1)])

# 4. The Pocock boundary for six looks
t6 = np.arange(1, 7) / 6
mv6 = multivariate_normal(mean=np.zeros(6), cov=np.sqrt(np.minimum.outer(t6, t6) / np.maximum.outer(t6, t6)), seed=1, abseps=1e-8, releps=1e-8)
print("Pocock, six looks:", round(brentq(lambda c: 1 - mv6.cdf(np.array([c] * 6)) - 0.025, 1.5, 4), 3))

# 5. The trial at 400, 800, and 1,200 patients: evidence for noninferiority against the O'Brien-Fleming boundaries
evidence = []
for n_look, bound in ((400, obf_c * sqrt(3)), (800, obf_c * sqrt(3 / 2)), (1200, obf_c)):
    part = df.iloc[:n_look]
    a = part[part["allocated"] == "short"]["fail"]
    b = part[part["allocated"] == "standard"]["fail"]
    se_look = sqrt(a.mean() * (1 - a.mean()) / len(a) + b.mean() * (1 - b.mean()) / len(b))
    z_look = -(a.mean() - b.mean() - margin) / se_look
    evidence.append(z_look)
    print("Look at", n_look, ": difference", round(100 * (a.mean() - b.mean()), 2), "points; evidence", round(z_look, 2), "; boundary", round(bound, 2), "; crossed:", z_look > bound)
print("Final upper limit with the boundary:", round(100 * (theta + obf_c * se), 2), "points")
'''

C_STOP = '''# 1. Conditional power at the second look (information fraction 2/3), with the evidence of the second look and the final boundary
t_look = 2 / 3
z_look = evidence[1]
c_final = obf_c
print("Evidence at the second look:", round(z_look, 2), "; final boundary:", round(c_final, 3))
print("Conditional power:", round(norm.cdf((z_look / sqrt(t_look) - c_final) / sqrt(1 - t_look)), 3))
'''

C_BIAS = '''# 1. 10,000 simulated trials, 200 patients per arm per look, O'Brien-Fleming boundaries; true loss 2 points
rng = np.random.default_rng(15)
bounds = [obf_c * sqrt(3 / k) for k in (1, 2, 3)]                 # the O'Brien-Fleming boundaries of Section 15.14
p_standard = 0.095
true_loss = 0.02
stopped = {1: [], 2: [], 3: []}
for repetition in range(10000):
    standard_arm = rng.random(600) < p_standard
    short_arm = rng.random(600) < p_standard + true_loss
    for look in (1, 2, 3):
        n_look = 200 * look
        rate_standard = standard_arm[:n_look].mean()
        rate_short = short_arm[:n_look].mean()
        se_look = sqrt(rate_standard * (1 - rate_standard) / n_look + rate_short * (1 - rate_short) / n_look)
        if se_look > 0 and (rate_short - rate_standard - margin) / se_look < -bounds[look - 1]:
            stopped[look].append(rate_short - rate_standard)
            break

# 2. Where the trials declared noninferiority and what they estimated
declared = stopped[1] + stopped[2] + stopped[3]
print("Declared noninferiority:", round(100 * len(declared) / 10000, 1), "% of the trials; by look:", len(stopped[1]), len(stopped[2]), len(stopped[3]))
print("Mean estimate at each look (points):", [round(float(100 * np.mean(stopped[k])), 1) for k in (1, 2, 3)], "; among all declared:", round(float(100 * np.mean(declared)), 1), "; true: 2.0")
'''

EX1 = '''# 1. Noninferiority by allocation with margins of 3 and 6 points
for m in (0.03, 0.06):
    z_m = (theta - m) / se
    print("Margin (points):", round(100 * m), "; upper limit", round(100 * (theta + 1.96 * se), 2), "; z =", round(z_m, 2), "; one-sided p =", round(norm.cdf(z_m), 4), "; noninferior:", theta + 1.96 * se < m)
'''
EX2 = '''# 1. Per protocol and as treated (by the course received, all 1,200 patients)
rec_s = df[df["received"] == "short"]["fail"]
rec_c = df[df["received"] == "standard"]["fail"]
theta_at = rec_s.mean() - rec_c.mean()
se_at = sqrt(rec_s.mean() * (1 - rec_s.mean()) / len(rec_s) + rec_c.mean() * (1 - rec_c.mean()) / len(rec_c))
print("Per protocol: difference", round(100 * theta_pp, 2), "; upper limit", round(100 * (theta_pp + 1.96 * se_pp), 2))
print("As treated: short", int(rec_s.sum()), "of", len(rec_s), "; standard", int(rec_c.sum()), "of", len(rec_c))
print("Difference", round(100 * theta_at, 2), "; standard error", "%.2f" % (100 * se_at), "; upper limit", round(100 * (theta_at + 1.96 * se_at), 2), "; z =", round((theta_at - margin) / se_at, 2), "; one-sided p =", round(norm.cdf((theta_at - margin) / se_at), 3))
'''
EX3 = '''# 1. Sample sizes and power of 600 per arm
print("Equal courses: 80%", ceil((1.96 + 0.8416) ** 2 * (2 * 0.095 * 0.905) / 0.05 ** 2), "; 90%", ceil((1.96 + 1.2816) ** 2 * (2 * 0.095 * 0.905) / 0.05 ** 2))
print("True loss 1 point, 80%:", ceil((1.96 + 0.8416) ** 2 * (0.095 * 0.905 + 0.105 * 0.895) / 0.04 ** 2))
for loss in (0.0, 0.01, 0.02, 0.03):
    se_true = sqrt(0.095 * 0.905 / 600 + (0.095 + loss) * (0.905 - loss) / 600)
    print("True loss (points):", round(100 * loss), "; power", round(norm.cdf((0.05 - loss) / se_true - 1.96), 3))
'''
EX4 = '''# 1. Equivalence tests with margins of 5 and 3 points
for m in (0.05, 0.03):
    p_lo = norm.sf((theta + m) / se)
    p_hi = norm.cdf((theta - m) / se)
    print("Margin (points):", round(100 * m), "; lower p =", round(p_lo, 5), "; upper p =", round(p_hi, 4), "; TOST p =", round(max(p_lo, p_hi), 4), "; equivalent at 0.025:", max(p_lo, p_hi) < 0.025)
'''
EX5 = '''# 1. P-value function and the 90% interval
for theta0 in (-4, 0, 2, 4, 5, 6):
    print("Hypothesized", theta0, "points: p =", round(2 * norm.sf(abs((theta - theta0 / 100) / se)), 4))
print("Same p-value as 0:", 0, "and", round(200 * theta, 2), "; 90% CI:", round(100 * (theta - 1.645 * se), 2), "to", round(100 * (theta + 1.645 * se), 2))

# 2. The two hypothesized differences whose p-value is exactly 0.52: the estimate plus and minus se times the normal quantile
z_52 = norm.isf(0.52 / 2)
print("Differences with p = 0.52:", round(100 * (theta - z_52 * se), 2), "and", round(100 * (theta + z_52 * se), 2), "points")
'''
EX6 = '''# 1. S-values and their meaning in coin tosses
for p in (0.52, 0.05, 0.033, 0.001):
    print("p =", p, ": S-value", round(-log2(p), 2), "bits; heads in a row: about", round(-log2(p)))
'''
EX7 = '''# 1. The p-value of no difference for larger trials with the observed difference fixed
for n_arm in (591, 3000, 10000, 30000):
    z_n = theta / sqrt((p_s * (1 - p_s) + p_c * (1 - p_c)) / n_arm)
    print("Patients per arm", n_arm, ": two-sided p =", "%.2g" % (2 * norm.sf(abs(z_n))))
'''
EX8 = '''# 1. Share of false significant results with 20% real hypotheses, and the share of real hypotheses that gives 5%
for power in (0.8, 0.5, 0.2):
    print("Power", power, ": share false", round(0.8 * 0.05 / (0.8 * 0.05 + 0.2 * power), 3))
share_real = 0.95 / 1.75                                           # solves 0.95 * (1 - r) = 0.80 * r
print("Real hypotheses giving 5% false (power 0.8):", round(100 * share_real, 1), "%")
'''
EX9 = '''# 1. Differences and p-values by site, and the Bonferroni threshold
below_005 = []
below_bonferroni = []
for site, group in df.groupby("site"):
    a = group[group["allocated"] == "short"]["fail"]
    b = group[group["allocated"] == "standard"]["fail"]
    table = [[int(a.sum()), len(a) - int(a.sum())], [int(b.sum()), len(b) - int(b.sum())]]
    p_site = stats.fisher_exact(table)[1]
    if p_site < 0.05:
        below_005.append(site)
    if p_site < 0.05 / 12:
        below_bonferroni.append(site)
    print(site, ": difference", round(100 * (a.mean() - b.mean()), 1), "points; Fisher p =", round(p_site, 4))
print("Sites with p < 0.05:", below_005, "; sites below the Bonferroni threshold:", below_bonferroni)
print("Bonferroni threshold:", round(0.05 / 12, 4), "; chance of at least one p < 0.05 in 12 independent tests:", round(1 - 0.95 ** 12, 3))
'''
EX10 = '''# 1. Four looks (every 300 patients): rejection rates in 4,000 shuffles
rng = np.random.default_rng(15)
labels = (df["allocated"] == "short").values
y = df["fail"].values
hit_196 = 0
hit_pocock = 0
for repetition in range(4000):
    shuffled = rng.permutation(labels)
    z_four = []
    for n_look in (300, 600, 900, 1200):
        is_short = shuffled[:n_look]
        yy = y[:n_look]
        p_all = yy.mean()                                          # failure rate of all patients so far (standard error under the null hypothesis)
        z_four.append(abs(yy[is_short].mean() - yy[~is_short].mean()) / sqrt(p_all * (1 - p_all) * (1 / is_short.sum() + 1 / (n_look - is_short.sum()))))
    hit_196 = hit_196 + (max(z_four) > 1.96)
    hit_pocock = hit_pocock + (max(z_four) > 2.361)
print("Four looks at 1.96:", round(100 * hit_196 / 4000, 1), "%; at 2.361:", round(100 * hit_pocock / 4000, 1), "%")
'''
EX11 = '''# 1. Boundaries for four equally spaced looks and the spending function
# The correlation of the statistics at looks i and j is sqrt(t_i / t_j); brentq finds the boundary that makes the probability of crossing at any look 0.025
t4 = np.arange(1, 5) / 4
mv4 = multivariate_normal(mean=np.zeros(4), cov=np.sqrt(np.minimum.outer(t4, t4) / np.maximum.outer(t4, t4)), seed=1, abseps=1e-8, releps=1e-8)
pocock4 = brentq(lambda c: 1 - mv4.cdf(np.array([c] * 4)) - 0.025, 1.5, 4)
obf4 = brentq(lambda c: 1 - mv4.cdf(np.array([c * sqrt(4 / k) for k in (1, 2, 3, 4)])) - 0.025, 1.5, 4)
print("Pocock:", round(pocock4, 3), "; O'Brien-Fleming:", [round(obf4 * sqrt(4 / k), 3) for k in (1, 2, 3, 4)])
print("Spending at 0.25, 0.5, 0.75, 1:", [round(float(2 - 2 * norm.cdf(1.96 / sqrt(t_k))), 4) for t_k in (0.25, 0.5, 0.75, 1)])
'''
EX12 = '''# 1. Fixed-sample p-value of Z = 2.6, and the p-value that respects the design (first look, then the second look at least as extreme)
print("Fixed-sample two-sided p of Z = 2.6:", round(2 * norm.sf(2.6), 4), "; boundary at the second look:", round(obf_c * sqrt(3 / 2), 3))
c_first = obf_c * sqrt(3)                                          # boundary at the first look
r = sqrt(1 / 2)                                                    # correlation between the first and the second look
def_cdf = lambda a: quad(lambda x: norm.pdf(x) * norm.cdf((2.6 - r * x) / sqrt(1 - r ** 2)), -np.inf, a)[0]     # P(Z1 < a and Z2 < 2.6)
inside_first = (norm.cdf(c_first) - def_cdf(c_first)) - (norm.cdf(-c_first) - def_cdf(-c_first))               # P(-c < Z1 < c and Z2 > 2.6)
print("P-value of the design:", round(2 * norm.sf(c_first) + 2 * inside_first, 4))

# 2. Conditional power with evidence 1.5 at t = 2/3 and final boundary 2.004
print("Conditional power:", round(norm.cdf((1.5 / sqrt(2 / 3) - 2.004) / sqrt(1 / 3)), 3))
'''


def cells(lang):
    en = lang == "en"
    T = lambda a, b: a if en else b
    code = lambda c: c if en else tr(c)
    S = []

    def sec(num, title_en, title_pt, q_en=None, q_pt=None):
        S.append(("md", "### " + num + " " + T(title_en, title_pt) + (("\n\n*" + T(q_en, q_pt) + "*") if q_en else "")))

    def cell(c):
        S.append(("code", code(c)))

    sec("15.1", "Introduction: the data", "Introdução: os dados")
    cell(LOAD)
    plan = [
     ("15.2", "Noninferiority: the margin and the test", "Não inferioridade: a margem e o teste", C_NI,
      "Is the 7-day course not worse than the 14-day course by more than 5 points?", "O curso de 7 dias não é pior que o de 14 dias por mais de 5 pontos?"),
     ("15.3", "Intention to treat and per protocol", "Intenção de tratar e por protocolo", C_ITT,
      "Does the answer hold for the patients who received the course they were assigned?", "A resposta vale para os pacientes que receberam o curso designado?"),
     ("15.4", "Equivalence and two one-sided tests", "Equivalência e dois testes unilaterais", C_TOST,
      "Would the answer change if the aim were to show that the two courses are equivalent?", "A resposta mudaria se o objetivo fosse mostrar que os dois cursos são equivalentes?"),
     ("15.5", "Sample size and power of a noninferiority trial", "Tamanho da amostra e poder de um ensaio de não inferioridade", C_SIZE,
      "How many patients did the trial need?", "De quantos pacientes o ensaio precisava?"),
     ("15.6", "Confidence intervals and tests are one calculation", "Intervalos de confiança e testes são um só cálculo", C_DUAL,
      "Do the confidence interval and the test say the same thing?", "O intervalo de confiança e o teste dizem a mesma coisa?"),
     ("15.7", "The p-value function", "A função valor de p", C_PFUN,
      "Which differences between the courses are compatible with the data?", "Quais diferenças entre os cursos são compatíveis com os dados?"),
     ("15.8", "What a p-value means", "O que um valor de p significa", C_SVAL,
      "What does a p-value of 0.52 for no difference tell the committee, and what does it not?", "O que um valor de p de 0,52 para nenhuma diferença diz ao comitê, e o que não diz?"),
     ("15.9", "What a p-value does not mean", "O que um valor de p não significa", C_MISREAD,
      "What would the committee be wrong to conclude from the p-values of this trial?", "O que o comitê erraria ao concluir dos valores de p deste ensaio?"),
     ("15.10", "Significant versus important", "Significativo versus importante", C_IMPORTANT,
      "If a larger trial had made the difference of 1.2 points significant, would that change what the committee should do?", "Se um ensaio maior tornasse a diferença de 1,2 ponto significativa, isso mudaria o que o comitê deve fazer?"),
     ("15.11", "How many significant results are false", "Quantos resultados significativos são falsos", C_FALSE,
      "How many of the significant results of such trials are false?", "Quantos dos resultados significativos de tais ensaios são falsos?"),
     ("15.12", "Many tests: multiplicity and the Bonferroni correction", "Muitos testes: multiplicidade e a correção de Bonferroni", C_MULTI,
      "One site shows a benefit of the short course: is it real?", "Um centro mostra benefício do curso curto: é real?"),
     ("15.13", "Looking at the data again and again", "Olhar os dados repetidamente", C_PEEK,
      "Could the committee have looked at the data before the trial ended, and stopped?", "O comitê poderia ter olhado os dados antes do fim do ensaio, e parado?"),
     ("15.14", "Group-sequential boundaries and alpha spending", "Limites sequenciais em grupo e gasto de alfa", C_SEQ,
      "How should the committee have set its boundaries for three looks, at 400, 800, and 1,200 patients?", "Como o comitê deveria ter definido seus limites para três análises, com 400, 800 e 1.200 pacientes?"),
     ("15.15", "Stopping early: benefit, futility, harm, and the monitoring committee", "Parar cedo: benefício, futilidade, dano e o comitê de monitoramento", C_STOP,
      "For what reasons would the trial have been stopped, and who decides?", "Por que razões o ensaio teria sido interrompido, e quem decide?"),
     ("15.16", "The estimate after early stopping", "A estimativa depois da parada precoce", C_BIAS,
      "If the trial had stopped early, would its estimate be reliable?", "Se o ensaio tivesse parado cedo, sua estimativa seria confiável?"),
    ]
    for num, te, tp, c, qe, qp in plan:
        sec(num, te, tp, qe, qp)
        cell(c)
    exs = [("Margins of 3 and 6 points", "Margens de 3 e 6 pontos", EX1), ("Per protocol and as treated", "Por protocolo e como tratado", EX2),
           ("Sample sizes and power", "Tamanhos de amostra e poder", EX3), ("Equivalence tests", "Testes de equivalência", EX4),
           ("The p-value function", "A função valor de p", EX5), ("S-values", "Valores S", EX6),
           ("Significant versus important", "Significativo versus importante", EX7), ("False significant results", "Resultados significativos falsos", EX8),
           ("The twelve sites", "Os doze centros", EX9), ("Four looks", "Quatro análises", EX10),
           ("Boundaries for four looks", "Limites para quatro análises", EX11), ("An early stop and conditional power", "Uma parada precoce e o poder condicional", EX12)]
    return S, [(i + 1, T(a, b), code(c)) for i, (a, b, c) in enumerate(exs)]
