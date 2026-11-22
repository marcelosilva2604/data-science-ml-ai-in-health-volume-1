"""All code cells of the Chapter 12 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered
comments, output as plain sentences. Beginner-friendly Python: print with commas, round(), no f-strings, no helper functions.
The cells are written once in English; the Portuguese cell is the same code with the comments and printed text translated
through the TR table (exact substrings, longest first)."""

TR = [
 ("# 5. Days within one standard deviation of the mean (5 to 10 calls) and days with more than 13 calls", "# 5. Dias a menos de um desvio padrão da média (5 a 10 ligações) e dias com mais de 13 ligações"),
 ("Days with 5 to 10 calls:", "Dias com 5 a 10 ligações:"), ("; days with more than 13 calls:", "; dias com mais de 13 ligações:"),
 ("; statistic / 89:", "; estatística / 89:"),
 ("# 5. A fire: chance of 30 or more calls in the hour, under the Poisson model", "# 5. Um incêndio: chance de 30 ou mais ligações na hora, pelo modelo de Poisson"),
 ("; about one in", "; cerca de uma em"), ('"billion"', '"bilhão"'),
 ("Variance of one call:", "Variância de uma ligação:"),
 ("; third quarter hour:", "; terceiro quarto de hora:"),
 ("# 4. If the calls arrived without interruption between hours (rate of the 90 days)", "# 4. Se as ligações chegassem sem interrupção entre as horas (taxa dos 90 dias)"),
 ("Mean gap at the hourly rate:", "Distância média pela taxa horária:"), ("s; three gaps:", "s; três distâncias:"), ("s; standard deviation of three gaps, model:", "s; desvio padrão de três distâncias, modelo:"), ("; triples in the record:", "; trios no registro:"),
 ("# 4. Waits of 240 seconds or more, and of more than 420 seconds (outside the density figure)", "# 4. Esperas de 240 segundos ou mais e de mais de 420 segundos (fora da figura da densidade)"),
 ("240 s or more:", "240 s ou mais:"), ("; more than 420 s:", "; mais de 420 s:"),
 ("# 1. Read the record: one row is one call", "# 1. Ler o registro: cada linha é uma ligação"),
 ("# 2. Count rows and columns", "# 2. Contar linhas e colunas"),
 ("The record has", "O registro tem"), ("rows (one per call) and", "linhas (uma por ligação) e"), ("columns.", "colunas."),
 ("# The first five rows", "# As cinco primeiras linhas"),
 # 12.2
 ("# 1. Calls between 18:00 and 18:59 on each of the 90 days (a day without a call counts as 0)", "# 1. Ligações entre 18:00 e 18:59 em cada um dos 90 dias (um dia sem ligação conta como 0)"),
 ("# 2. How many days had each count", "# 2. Quantos dias tiveram cada contagem"),
 ('"days"', '"dias"'),
 ("# 3. Expected value, variance, and standard deviation (the book divides by 90 days)", "# 3. Valor esperado, variância e desvio padrão (o livro divide por 90 dias)"),
 ("Mean:", "Média:"), ("; variance:", "; variância:"), ("; standard deviation:", "; desvio padrão:"),
 ("; standard deviation", "; desvio padrão"),
 ("Range:", "Variação:"), ("; range:", "; variação:"), ('"to"', '"a"'),
 ("# 4. The hour 19:00-19:59 and the sum of the two means", "# 4. A hora de 19:00 a 19:59 e a soma das duas médias"),
 ("Mean of 19:00-19:59:", "Média de 19:00 a 19:59:"), ("; sum of the two means:", "; soma das duas médias:"), ("; mean of the daily totals:", "; média dos totais diários:"),
 # 12.3
 ("# 1. Poisson probability of exactly 7 calls, with the mean of the 90 days", "# 1. Probabilidade de Poisson de exatamente 7 ligações, com a média dos 90 dias"),
 ("; expected days:", "; dias esperados:"), ("; observed days:", "; dias observados:"),
 ("# 2. Cumulative distribution function and the rush of 14 or more calls", "# 2. Função de distribuição acumulada e o pico de 14 ou mais ligações"),
 ("# 3. Days with 14 or more calls: expected and observed", "# 3. Dias com 14 ou mais ligações: esperados e observados"),
 ("Days with 14 or more calls: expected", "Dias com 14 ou mais ligações: esperados"), ("; observed", "; observados"),
 ("# 4. Is the variance close to the mean? Ratio and dispersion test (chi-square, 89 degrees of freedom)", "# 4. A variância é próxima da média? Razão e teste de dispersão (qui-quadrado, 89 graus de liberdade)"),
 ("Variance / mean:", "Variância / média:"), ("; statistic:", "; estatística:"),
 # 12.4
 ("# 1. Fraction of calls with an ambulance", "# 1. Fração de ligações com ambulância"),
 ("Ambulance sent for", "Ambulância enviada para"), ('"of", len(df), "calls ="', '"de", len(df), "ligações ="'),
 ('"of", len(w), "="', '"de", len(w), "="'), ('"of 90 ="', '"de 90 ="'), ('"of", len(blocks), "="', '"de", len(blocks), "="'),
 ("# 2. Mean, variance, and standard deviation for 12 calls", "# 2. Média, variância e desvio padrão para 12 ligações"),
 ("# 3. Four ambulances free: more than four ambulance calls among 12", "# 3. Quatro ambulâncias livres: mais de quatro ligações com ambulância entre 12"),
 ("# 4. Check with blocks of 12 consecutive calls", "# 4. Conferência com blocos de 12 ligações consecutivas"),
 ("Blocks:", "Blocos:"), ("; with 5 or more:", "; com 5 ou mais:"), ("; the model expects about", "; o modelo espera cerca de"),
 # 12.5
 ("# 1. Day 1: calls and ambulance calls", "# 1. Dia 1: ligações e ligações com ambulância"),
 ("Day 1:", "Dia 1:"), ("calls,", "ligações,"), ("with an ambulance", "com ambulância"),
 ("# 2. One audit in detail: 10 recordings drawn at random, without replacement", "# 2. Uma auditoria em detalhe: 10 gravações sorteadas, sem reposição"),
 ("Ambulance calls among the 10 recordings:", "Ligações com ambulância entre as 10 gravações:"),
 ("# 3. Four more audits: each draw gives a different list of calls", "# 3. Mais quatro auditorias: cada sorteio dá uma lista diferente de ligações"),
 ("Audit", "Auditoria"), ("- ambulance sent:", "- ambulância enviada:"), ("- ambulance calls:", "- ligações com ambulância:"),
 ("# 4. Expected number and hypergeometric probabilities for 10 recordings", "# 4. Número esperado e probabilidades hipergeométricas para 10 gravações"),
 ("Expected ambulance calls among the 10:", "Ligações com ambulância esperadas entre as 10:"),
 ("# 5. The binomial with the same fraction, for comparison", "# 5. A binomial com a mesma fração, para comparação"),
 ("Binomial P(X = 0):", "Binomial P(X = 0):"), ("Variance: hypergeometric", "Variância: hipergeométrica"), ("; binomial", "; binomial"),
 ("# 6. Ten thousand audits: share of audits with each count, against the formula", "# 6. Dez mil auditorias: fração de auditorias com cada contagem, contra a fórmula"),
 ("x =", "x ="), ("; share of audits:", "; fração das auditorias:"), ("; formula:", "; fórmula:"),
 # 12.6
 ("# 1. Summary of the waits", "# 1. Resumo das esperas"),
 ("; median:", "; mediana:"), ("; longest:", "; maior:"),
 ("# 2. Fractions of calls answered within 60, 120, and 240 seconds", "# 2. Frações de ligações atendidas em até 60, 120 e 240 segundos"),
 ("Waited 60 s or less:", "Esperaram 60 s ou menos:"), ("; 120 s or less:", "; 120 s ou menos:"), ("; 240 s or less:", "; 240 s ou menos:"),
 ("# 3. Waits of more than 240 seconds", "# 3. Esperas de mais de 240 segundos"),
 ("More than 240 s:", "Mais de 240 s:"),
 # 12.7
 ("# 1. Normal model on the raw seconds", "# 1. Modelo normal sobre os segundos brutos"),
 ("Normal model: P(X < 0) =", "Modelo normal: P(X < 0) ="), ("; P(X > 240) =", "; P(X > 240) ="),
 ("# 2. The logarithm of the wait", "# 2. O logaritmo da espera"),
 ("Log of the wait: mean", "Log da espera: média"), ("; skewness", "; assimetria"),
 ("# 2. Lognormal model: median, mean, standard score of 240 s, and P(Y > 240)", "# 2. Modelo lognormal: mediana, média, escore padrão de 240 s e P(Y > 240)"),
 ("Lognormal model: median", "Modelo lognormal: mediana"), ("; mean", "; média"),
 ("; P(Y > 240) =", "; P(Y > 240) ="),
 ("# 4. Fraction of logarithms within 1 and 2 standard deviations of the mean", "# 4. Fração dos logaritmos a menos de 1 e de 2 desvios padrão da média"),
 ("Within 1 standard deviation:", "A menos de 1 desvio padrão:"), ("; within 2:", "; a menos de 2:"),
 # 12.8
 ("# 1. Draw 10,000 samples of 10 logarithms, with replacement (seed 12)", "# 1. Sortear 10.000 amostras de 10 logaritmos, com reposição (semente 12)"),
 ("# 2. Mean and standard deviation of each sample, and the standardized mean with sigma and with s", "# 2. Média e desvio padrão de cada amostra, e a média padronizada com sigma e com s"),
 ("# 3. Share of samples beyond the limits", "# 3. Fração das amostras além dos limites"),
 ("Known sigma, beyond 1.96:", "Sigma conhecido, além de 1,96:"), ("; with s, beyond 1.96:", "; com s, além de 1,96:"), ("; with s, beyond 2.262:", "; com s, além de 2,262:"),
 ("# 4. Chi-square and F quantities", "# 4. Quantidades qui-quadrado e F"),
 ("Chi-square above", "Qui-quadrado acima de"), ("; F above", "; F acima de"),
 ("# 5. Limits of the three distributions", "# 5. Limites das três distribuições"),
 ("Student t, 9 df, 97.5%:", "t de Student, 9 gl, 97,5%:"), ("; chi-square, 9 df, 95%:", "; qui-quadrado, 9 gl, 95%:"), ("; F, 9 and 9 df, 95%:", "; F, 9 e 9 gl, 95%:"),
 # Part B
 ("# 1. Calls between 12:00 and 12:59 on each day", "# 1. Ligações entre 12:00 e 12:59 em cada dia"),
 ("# 2. Mean and variance of the counts", "# 2. Média e variância das contagens"),
 ("# 1. Poisson probabilities with the mean of 18:00-18:59", "# 1. Probabilidades de Poisson com a média de 18:00 a 18:59"),
 ("Days with 10 or more calls:", "Dias com 10 ou mais ligações:"),
 ("# 1. Calls between 03:00 and 03:59 on each day", "# 1. Ligações entre 03:00 e 03:59 em cada dia"),
 ("# 2. Poisson probabilities of no call and of 5 or more calls, and the fractions of days", "# 2. Probabilidades de Poisson de nenhuma ligação e de 5 ou mais, e as frações de dias"),
 ("Days with no call:", "Dias sem ligação:"), ("; days with 5 or more:", "; dias com 5 ou mais:"),
 ("# 1. Binomial probabilities for 12 calls with the fraction of ambulance calls", "# 1. Probabilidades binomiais para 12 ligações com a fração de ligações com ambulância"),
 ("# 2. Blocks of 12 consecutive calls with 3 or more ambulance calls", "# 2. Blocos de 12 ligações consecutivas com 3 ou mais ligações com ambulância"),
 ("Blocks with 3 or more:", "Blocos com 3 ou mais:"),
 ("# 1. Hypergeometric and binomial probabilities of exactly 2 ambulance calls", "# 1. Probabilidades hipergeométrica e binomial de exatamente 2 ligações com ambulância"),
 ("Hypergeometric P(X = 2):", "Hipergeométrica P(X = 2):"), ("; binomial P(X = 2):", "; binomial P(X = 2):"),
 ("# 1. Fractions of the waits and the lognormal values", "# 1. Frações das esperas e os valores do modelo lognormal"),
 ("Record: 60 s or less", "Registro: 60 s ou menos"), ("; 120 s or less", "; 120 s ou menos"), ("; more than 300 s", "; mais de 300 s"),
 ("Lognormal: 60 s or less", "Lognormal: 60 s ou menos"),
 ("# 1. Normal model with the mean and standard deviation of the waits", "# 1. Modelo normal com a média e o desvio padrão das esperas"),
 ("# 1. Lognormal model: more than 180 seconds, and the 99th percentile", "# 1. Modelo lognormal: mais de 180 segundos e o percentil 99"),
 ("P(Y > 180) =", "P(Y > 180) ="), ("; observed:", "; observado:"),
 ("99th percentile of the model:", "Percentil 99 do modelo:"), ("; of the record:", "; do registro:"),
 ("# 1. Standardized mean of 10,000 samples of 10 logarithms (seed 12)", "# 1. Média padronizada de 10.000 amostras de 10 logaritmos (semente 12)"),
 ("Beyond 1.96:", "Além de 1,96:"), ("; beyond 2.262:", "; além de 2,262:"),
 ("# 1. Gaps between ambulance calls: calls from one ambulance call to the next (the next one included)", "# 1. Distâncias entre ligações com ambulância: ligações de uma ligação com ambulância até a seguinte (a seguinte incluída)"),
 ("Gaps:", "Distâncias:"), ("; model mean:", "; média do modelo:"), ("; model variance:", "; variância do modelo:"), ("; record:", "; registro:"),
 ("# 2. Geometric probabilities against the record", "# 2. Probabilidades geométricas contra o registro"),
 ("# 3. Calls until the third ambulance call: groups of three gaps (negative binomial, r = 3)", "# 3. Ligações até a terceira ligação com ambulância: grupos de três distâncias (binomial negativa, r = 3)"),
 ("Groups:", "Grupos:"),
 ("# 1. Second of arrival of the calls of 18:00-18:59 (uniform model)", "# 1. Segundo de chegada das ligações de 18:00 a 18:59 (modelo uniforme)"),
 ("Calls:", "Ligações:"), ("; mean second:", "; segundo médio:"), ("; uniform mean: 1800; first 15 minutes:", "; média uniforme: 1800; primeiros 15 minutos:"), ("%; model: 25%", "%; modelo: 25%"),
 ("# 2. Gaps between consecutive calls inside the hour, day by day (exponential model)", "# 2. Distâncias entre ligações consecutivas dentro da hora, dia a dia (modelo exponencial)"),
 ("P(gap > 600):", "P(distância > 600):"), ("; P(gap <= 120):", "; P(distância <= 120):"), ("; P(gap > 1200):", "; P(distância > 1200):"),
 ("# 3. Time to the third call: sums of three consecutive gaps (gamma, shape 3)", "# 3. Tempo até a terceira ligação: somas de três distâncias consecutivas (gama, forma 3)"),
 ("Triples:", "Trios:"), ("; P(sum <= 1200):", "; P(soma <= 1200):"),
 ("# 2. The next 200 calls: exact binomial and normal approximation, without and with the continuity correction", "# 2. As próximas 200 ligações: binomial exata e aproximação normal, sem e com a correção de continuidade"),
 ("P(X >= 45): exact", "P(X >= 45): exata"), ("; normal", "; normal"), ("; with correction", "; com correção"),
 ("# 3. Blocks of 200 consecutive calls in the record", "# 3. Blocos de 200 ligações consecutivas no registro"),
 ("Blocks of 200:", "Blocos de 200:"), ("; with 45 or more:", "; com 45 ou mais:"),
 ("# 1. The logarithm of the wait", "# 1. O logaritmo da espera"),
 ("# 3. Fraction of logarithms within 1 and 2 standard deviations of the mean", "# 3. Fração dos logaritmos a menos de 1 e de 2 desvios padrão da média"),
 ("# 4. Quantiles: the wait exceeded by 10% and by 5% of the callers", "# 4. Quantis: a espera superada por 10% e por 5% das pessoas"),
 ("0.90-quantile:", "Quantil 0,90:"), ("s; record:", "s; registro:"), ("; 0.95-quantile:", "; quantil 0,95:"),
 ("# 1. Geometric probabilities with p = 0.1786", "# 1. Probabilidades geométricas com p = 0,1786"),
 ("# 1. Calls until the second ambulance call: model and record", "# 1. Ligações até a segunda ligação com ambulância: modelo e registro"),
 ("Model mean:", "Média do modelo:"), ("; record mean:", "; média do registro:"),
 ("# 1. Second of arrival in 18:00-18:59: mean and last 15 minutes", "# 1. Segundo de chegada em 18:00-18:59: média e últimos 15 minutos"),
 ("Mean second:", "Segundo médio:"), ("; last 15 minutes:", "; últimos 15 minutos:"), ("%; uniform: 1800 and 25%", "%; uniforme: 1800 e 25%"),
 ("# 1. Gaps of more than 5 minutes", "# 1. Distâncias de mais de 5 minutos"), ("P(gap > 300):", "P(distância > 300):"),
 ("# 1. 40 or more ambulance calls among 200 calls", "# 1. 40 ou mais ligações com ambulância entre 200 ligações"),
 ("Exact:", "Exata:"), ("; normal:", "; normal:"), ("; with correction:", "; com correção:"),
]


def tr(code):
    for en, pt in sorted(TR, key=lambda x: -len(x[0])):
        code = code.replace(en, pt)
    return code


LOAD = '''# 1. Read the record: one row is one call
import numpy as np
import pandas as pd
from math import sqrt, log, exp
from scipy import stats

df = pd.read_csv("data/calls.csv")

# 2. Count rows and columns
rows, columns = df.shape
print("The record has", rows, "rows (one per call) and", columns, "columns.")
df.head()                                      # The first five rows
'''

C_COUNTS = '''# 1. Calls between 18:00 and 18:59 on each of the 90 days (a day without a call counts as 0)
counts = df[df["hour"] == 18].groupby("day").size().reindex(range(1, 91), fill_value=0)

# 2. How many days had each count
days_by_count = counts.value_counts().sort_index()
display(days_by_count.to_frame("days"))

# 3. Expected value, variance, and standard deviation (the book divides by 90 days)
probability = days_by_count / 90
mean = (probability.index * probability).sum()
variance = (((probability.index - mean) ** 2) * probability).sum()
print("Mean:", round(mean, 2), "; variance:", round(variance, 2), "; standard deviation:", round(sqrt(variance), 2))
print("Range:", counts.min(), "to", counts.max())

# 4. The hour 19:00-19:59 and the sum of the two means
counts19 = df[df["hour"] == 19].groupby("day").size().reindex(range(1, 91), fill_value=0)
print("Mean of 19:00-19:59:", round(counts19.mean(), 2), "; sum of the two means:", round(counts.mean() + counts19.mean(), 2), "; mean of the daily totals:", round((counts + counts19).mean(), 2))

# 5. Days within one standard deviation of the mean (5 to 10 calls) and days with more than 13 calls
print("Days with 5 to 10 calls:", ((counts >= 5) & (counts <= 10)).sum(), "; days with more than 13 calls:", (counts > 13).sum())
'''

C_POISSON = '''# 1. Poisson probability of exactly 7 calls, with the mean of the 90 days
mu = counts.mean()
p7 = stats.poisson.pmf(7, mu)
print("P(X = 7):", round(p7, 3), "; expected days:", round(90 * p7, 1), "; observed days:", (counts == 7).sum())

# 2. Cumulative distribution function and the rush of 14 or more calls
f13 = stats.poisson.cdf(13, mu)
print("F(13):", round(f13, 4), "; P(X >= 14):", round(1 - f13, 4))

# 3. Days with 14 or more calls: expected and observed
print("Days with 14 or more calls: expected", round(90 * (1 - f13), 2), "; observed", (counts >= 14).sum())

# 4. Is the variance close to the mean? Ratio and dispersion test (chi-square, 89 degrees of freedom)
ratio = counts.var(ddof=0) / counts.mean()
statistic = ((counts - counts.mean()) ** 2).sum() / counts.mean()
print("Variance / mean:", round(ratio, 2), "; statistic:", round(statistic, 1), "; statistic / 89:", round(statistic / 89, 2), "; p =", round(1 - stats.chi2.cdf(statistic, 89), 2))

# 5. A fire: chance of 30 or more calls in the hour, under the Poisson model
chance30 = stats.poisson.sf(29, mu)
print("P(X >= 30):", chance30, "; about one in", round(1 / chance30 / 1e9, 1), "billion")
'''

C_BINOMIAL = '''# 1. Fraction of calls with an ambulance
ambulance = df["ambulance"] == "yes"
p = ambulance.mean()
print("Ambulance sent for", ambulance.sum(), "of", len(df), "calls =", round(p, 4))
print("Variance of one call:", round(p * (1 - p), 4))

# 2. Mean, variance, and standard deviation for 12 calls
n = 12
print("Mean:", round(n * p, 2), "; variance:", round(n * p * (1 - p), 2), "; standard deviation:", round(sqrt(n * p * (1 - p)), 2))

# 3. Four ambulances free: more than four ambulance calls among 12
p5 = 1 - stats.binom.cdf(4, n, p)
print("P(X >= 5):", round(p5, 4))

# 4. Check with blocks of 12 consecutive calls
blocks = ambulance.values[: (len(df) // n) * n].reshape(-1, n).sum(axis=1)
print("Blocks:", len(blocks), "; with 5 or more:", (blocks >= 5).sum(), "=", round(100 * (blocks >= 5).mean(), 1), "%; the model expects about", round(len(blocks) * p5), "(", round(100 * p5, 1), "%)")
'''

C_HYPER = '''# 1. Day 1: calls and ambulance calls
day1 = df[df["day"] == 1]
N = len(day1)
K = (day1["ambulance"] == "yes").sum()
m = 10
print("Day 1:", N, "calls,", K, "with an ambulance")

# 2. One audit in detail: 10 recordings drawn at random, without replacement
rng = np.random.default_rng(12)
audit = day1.iloc[rng.choice(N, size=m, replace=False)].sort_values("call_id")
display(audit[["call_id", "hour", "wait_sec", "ambulance"]])
print("Ambulance calls among the 10 recordings:", (audit["ambulance"] == "yes").sum())

# 3. Four more audits: each draw gives a different list of calls
for k in range(2, 6):
    audit = day1.iloc[rng.choice(N, size=m, replace=False)]
    print("Audit", k, "- ambulance sent:", audit["ambulance"].tolist(), "- ambulance calls:", (audit["ambulance"] == "yes").sum())

# 4. Expected number and hypergeometric probabilities for 10 recordings
print("Expected ambulance calls among the 10:", round(m * K / N, 2))
print("P(X = 0):", round(stats.hypergeom.pmf(0, N, K, m), 3), "; P(X <= 1):", round(stats.hypergeom.cdf(1, N, K, m), 3), "; P(X >= 3):", round(1 - stats.hypergeom.cdf(2, N, K, m), 3))

# 5. The binomial with the same fraction, for comparison
print("Binomial P(X = 0):", round(stats.binom.pmf(0, m, K / N), 3), "; P(X >= 3):", round(1 - stats.binom.cdf(2, m, K / N), 3))
print("Variance: hypergeometric", round(stats.hypergeom.var(N, K, m), 2), "; binomial", round(m * (K / N) * (1 - K / N), 2))

# 6. Ten thousand audits: share of audits with each count, against the formula
is_ambulance = (day1["ambulance"] == "yes").to_numpy()
audits = np.array([is_ambulance[rng.choice(N, size=m, replace=False)].sum() for _ in range(10000)])
for x in range(6):
    print("x =", x, "; share of audits:", round((audits == x).mean(), 3), "; formula:", round(stats.hypergeom.pmf(x, N, K, m), 3))
'''

C_WAIT = '''# 1. Summary of the waits
w = df["wait_sec"]
print("Mean:", round(w.mean(), 1), "; standard deviation:", round(w.std(ddof=0), 1), "; median:", w.median(), "; longest:", w.max())

# 2. Fractions of calls answered within 60, 120, and 240 seconds
print("Waited 60 s or less:", round(100 * (w <= 60).mean(), 1), "%; 120 s or less:", round(100 * (w <= 120).mean(), 1), "%; 240 s or less:", round(100 * (w <= 240).mean(), 1), "%")

# 3. Waits of more than 240 seconds
print("More than 240 s:", (w > 240).sum(), "of", len(w), "=", round(100 * (w > 240).mean(), 2), "%")

# 4. Waits of 240 seconds or more, and of more than 420 seconds (outside the density figure)
print("240 s or more:", (w >= 240).sum(), "; more than 420 s:", (w > 420).sum())
'''

C_NORMAL = '''# 1. Normal model on the raw seconds
wait_mean = w.mean()
wait_sd = w.std(ddof=0)
print("Normal model: P(X < 0) =", round(stats.norm.cdf(0, wait_mean, wait_sd), 3), "; P(X > 240) =", round(stats.norm.sf(240, wait_mean, wait_sd), 3))

# 2. The next 200 calls: exact binomial and normal approximation, without and with the continuity correction
n200 = 200
mean200 = n200 * p
sd200 = sqrt(n200 * p * (1 - p))
print("Mean:", round(mean200, 2), "; standard deviation:", round(sd200, 2))
print("P(X >= 45): exact", round(1 - stats.binom.cdf(44, n200, p), 4), "; normal", round(stats.norm.sf(45, mean200, sd200), 4), "; with correction", round(stats.norm.sf(44.5, mean200, sd200), 4))

# 3. Blocks of 200 consecutive calls in the record
blocks200 = ambulance.values[: (len(df) // n200) * n200].reshape(-1, n200).sum(axis=1)
print("Blocks of 200:", len(blocks200), "; with 45 or more:", (blocks200 >= 45).sum(), "; mean:", round(blocks200.mean(), 1), "; standard deviation:", round(blocks200.std(), 1))
'''

C_LOGN = '''# 1. The logarithm of the wait
lw = np.log(w)
log_mean = lw.mean()
log_sd = lw.std(ddof=0)
print("Log of the wait: mean", round(log_mean, 3), "; standard deviation", round(log_sd, 3), "; skewness", round(stats.skew(lw), 3))

# 2. Lognormal model: median, mean, standard score of 240 s, and P(Y > 240)
z = (log(240) - log_mean) / log_sd
print("Lognormal model: median", round(exp(log_mean), 1), "; mean", round(exp(log_mean + log_sd ** 2 / 2), 1), "; z =", round(z, 2), "; P(Y > 240) =", round(stats.norm.sf(z), 3))

# 3. Fraction of logarithms within 1 and 2 standard deviations of the mean
print("Within 1 standard deviation:", round(100 * ((lw > log_mean - log_sd) & (lw < log_mean + log_sd)).mean(), 1), "%; within 2:", round(100 * ((lw > log_mean - 2 * log_sd) & (lw < log_mean + 2 * log_sd)).mean(), 1), "%")

# 4. Quantiles: the wait exceeded by 10% and by 5% of the callers
print("0.90-quantile:", round(exp(log_mean + stats.norm.ppf(0.90) * log_sd), 1), "s; record:", round(w.quantile(0.90), 1), "; 0.95-quantile:", round(exp(log_mean + stats.norm.ppf(0.95) * log_sd), 1), "s; record:", round(w.quantile(0.95), 1))
'''

C_GEOM = '''# 1. Gaps between ambulance calls: calls from one ambulance call to the next (the next one included)
positions = np.where(ambulance.values)[0]
gaps_calls = np.diff(positions)
print("Gaps:", len(gaps_calls), "; mean:", round(gaps_calls.mean(), 2), "; variance:", round(gaps_calls.var(), 1), "; model mean:", round(1 / p, 2), "; model variance:", round((1 - p) / p ** 2, 1))

# 2. Geometric probabilities against the record
print("P(X = 1):", round(stats.geom.pmf(1, p), 3), "; record:", round((gaps_calls == 1).mean(), 3))
print("P(X <= 5):", round(stats.geom.cdf(5, p), 3), "; record:", round((gaps_calls <= 5).mean(), 3), "; P(X > 10):", round(stats.geom.sf(10, p), 3), "; record:", round((gaps_calls > 10).mean(), 3))

# 3. Calls until the third ambulance call: groups of three gaps (negative binomial, r = 3)
groups = gaps_calls[: len(gaps_calls) // 3 * 3].reshape(-1, 3).sum(axis=1)
print("Groups:", len(groups), "; mean:", round(groups.mean(), 2), "; model mean:", round(3 / p, 2), "; variance:", round(groups.var(), 1), "; model variance:", round(3 * (1 - p) / p ** 2, 1))
print("P(X <= 10):", round(stats.nbinom.cdf(10 - 3, 3, p), 3), "; record:", round((groups <= 10).mean(), 3), "; P(X > 25):", round(stats.nbinom.sf(25 - 3, 3, p), 3), "; record:", round((groups > 25).mean(), 3))
'''

C_ARRIVALS = '''# 1. Second of arrival of the calls of 18:00-18:59 (uniform model)
seconds = df[df["hour"] == 18]["second"]
print("Calls:", len(seconds), "; mean second:", round(seconds.mean(), 1), "; uniform mean: 1800; first 15 minutes:", round(100 * (seconds < 900).mean(), 1), "%; model: 25%; third quarter hour:", round(100 * ((seconds >= 1800) & (seconds < 2700)).mean(), 1), "%")

# 2. Gaps between consecutive calls inside the hour, day by day (exponential model)
gap_list = []
for day, rows_of_day in df[df["hour"] == 18].groupby("day"):
    gap_list = gap_list + list(np.diff(np.sort(rows_of_day["second"].values)))
gaps = np.array(gap_list)
mean_gap = gaps.mean()
print("Gaps:", len(gaps), "; mean:", round(mean_gap, 1), "s")
print("P(gap > 600):", round(exp(-600 / mean_gap), 3), "; record:", round((gaps > 600).mean(), 3), "; P(gap <= 120):", round(1 - exp(-120 / mean_gap), 3), "; record:", round((gaps <= 120).mean(), 3), "; P(gap > 1200):", round(exp(-1200 / mean_gap), 3), "; record:", round((gaps > 1200).mean(), 3))

# 3. Time to the third call: sums of three consecutive gaps (gamma, shape 3)
triple_list = []
for day, rows_of_day in df[df["hour"] == 18].groupby("day"):
    day_gaps = np.diff(np.sort(rows_of_day["second"].values))
    n_triples = len(day_gaps) // 3
    if n_triples > 0:
        triple_list = triple_list + list(day_gaps[: n_triples * 3].reshape(-1, 3).sum(axis=1))
triples = np.array(triple_list)
print("Triples:", len(triples), "; mean:", round(triples.mean(), 1), "; model mean:", round(3 * mean_gap, 1), "; P(sum <= 1200):", round(stats.gamma.cdf(1200, 3, scale=mean_gap), 3), "; record:", round((triples <= 1200).mean(), 3))

# 4. If the calls arrived without interruption between hours (rate of the 90 days)
print("Mean gap at the hourly rate:", round(3600 / counts.mean(), 1), "s; three gaps:", round(3 * 3600 / counts.mean(), 1), "s; standard deviation of three gaps, model:", round(sqrt(3) * mean_gap, 1), "; triples in the record:", round(triples.std(ddof=0), 1))
'''

C_TESTS = '''# 1. Draw 10,000 samples of 10 logarithms, with replacement (seed 12)
rng = np.random.default_rng(12)
draws = lw.values[rng.integers(0, len(lw), size=(10000, 10))]

# 2. Mean and standard deviation of each sample, and the standardized mean with sigma and with s
sample_mean = draws.mean(axis=1)
sample_sd = draws.std(axis=1, ddof=1)
z_known = (sample_mean - log_mean) / (log_sd / sqrt(10))
t_stat = (sample_mean - log_mean) / (sample_sd / sqrt(10))

# 3. Share of samples beyond the limits
print("Known sigma, beyond 1.96:", round(100 * (abs(z_known) > 1.96).mean(), 1), "%; with s, beyond 1.96:", round(100 * (abs(t_stat) > 1.96).mean(), 1), "%; with s, beyond 2.262:", round(100 * (abs(t_stat) > stats.t.ppf(0.975, 9)).mean(), 1), "%")

# 4. Chi-square and F quantities
chi_square = 9 * sample_sd ** 2 / log_sd ** 2
second_sample = lw.values[rng.integers(0, len(lw), size=(10000, 10))]
f_ratio = sample_sd ** 2 / second_sample.std(axis=1, ddof=1) ** 2
print("Chi-square above 16.92:", round(100 * (chi_square > stats.chi2.ppf(0.95, 9)).mean(), 1), "%; F above 3.18:", round(100 * (f_ratio > stats.f.ppf(0.95, 9, 9)).mean(), 1), "%")

# 5. Limits of the three distributions
print("Student t, 9 df, 97.5%:", round(stats.t.ppf(0.975, 9), 3), "; chi-square, 9 df, 95%:", round(stats.chi2.ppf(0.95, 9), 2), "; F, 9 and 9 df, 95%:", round(stats.f.ppf(0.95, 9, 9), 2))
'''

EX1 = '''# 1. Calls between 12:00 and 12:59 on each day
counts12 = df[df["hour"] == 12].groupby("day").size().reindex(range(1, 91), fill_value=0)

# 2. Mean and variance of the counts
print("Mean:", round(counts12.mean(), 2), "; variance:", round(counts12.var(ddof=0), 2), "; range:", counts12.min(), "to", counts12.max())
'''
EX3 = '''# 1. Poisson probabilities with the mean of 18:00-18:59
print("P(X = 5):", round(stats.poisson.pmf(5, mu), 4), "; P(X <= 5):", round(stats.poisson.cdf(5, mu), 4), "; P(X >= 10):", round(1 - stats.poisson.cdf(9, mu), 4))
print("Days with 10 or more calls:", (counts >= 10).sum(), "of 90 =", round(100 * (counts >= 10).mean(), 1), "%")
'''
EX4 = '''# 1. Calls between 03:00 and 03:59 on each day
counts3 = df[df["hour"] == 3].groupby("day").size().reindex(range(1, 91), fill_value=0)
mu3 = counts3.mean()
print("Mean:", round(mu3, 2), "; variance:", round(counts3.var(ddof=0), 2))

# 2. Poisson probabilities of no call and of 5 or more calls, and the fractions of days
print("P(X = 0):", round(stats.poisson.pmf(0, mu3), 4), "; P(X >= 5):", round(1 - stats.poisson.cdf(4, mu3), 4))
print("Days with no call:", (counts3 == 0).sum(), "=", round(100 * (counts3 == 0).mean(), 1), "%; days with 5 or more:", (counts3 >= 5).sum(), "=", round(100 * (counts3 >= 5).mean(), 1), "%")
'''
EX5 = '''# 1. Binomial probabilities for 12 calls with the fraction of ambulance calls
print("p =", round(p, 4), "; P(X = 0):", round(stats.binom.pmf(0, 12, p), 4), "; P(X >= 3):", round(1 - stats.binom.cdf(2, 12, p), 4))

# 2. Blocks of 12 consecutive calls with 3 or more ambulance calls
print("Blocks with 3 or more:", (blocks >= 3).sum(), "of", len(blocks), "=", round(100 * (blocks >= 3).mean(), 1), "%; the model expects about", round(len(blocks) * (1 - stats.binom.cdf(2, 12, p))))
'''
EX6 = '''# 1. Hypergeometric and binomial probabilities of exactly 2 ambulance calls
print("Hypergeometric P(X = 2):", round(stats.hypergeom.pmf(2, N, K, m), 4), "; binomial P(X = 2):", round(stats.binom.pmf(2, m, K / N), 4))
'''
EX11 = '''# 1. Fractions of the waits and the lognormal values
print("Record: 60 s or less", round(100 * (w <= 60).mean(), 2), "%; 120 s or less", round(100 * (w <= 120).mean(), 2), "%; more than 300 s", round(100 * (w > 300).mean(), 2), "%")
print("Lognormal: 60 s or less", round(100 * stats.norm.cdf((log(60) - log_mean) / log_sd), 1), "%; 120 s or less", round(100 * stats.norm.cdf((log(120) - log_mean) / log_sd), 1), "%; more than 300 s", round(100 * stats.norm.sf((log(300) - log_mean) / log_sd), 1), "%")
'''
EX12 = '''# 1. Normal model with the mean and standard deviation of the waits
print("P(X < 0) =", round(stats.norm.cdf(0, wait_mean, wait_sd), 4), "; P(X > 240) =", round(stats.norm.sf(240, wait_mean, wait_sd), 4))
'''
EX13 = '''# 1. Lognormal model: more than 180 seconds, and the 99th percentile
z180 = (log(180) - log_mean) / log_sd
print("z =", round(z180, 2), "; P(Y > 180) =", round(stats.norm.sf(z180), 3), "; observed:", round((w > 180).mean(), 3))
print("99th percentile of the model:", round(exp(log_mean + stats.norm.ppf(0.99) * log_sd), 1), "; of the record:", round(w.quantile(0.99), 1))
'''
EX15 = '''# 1. Standardized mean of 10,000 samples of 10 logarithms (seed 12)
rng = np.random.default_rng(12)
draws = lw.values[rng.integers(0, len(lw), size=(10000, 10))]
t_stat = (draws.mean(axis=1) - log_mean) / (draws.std(axis=1, ddof=1) / sqrt(10))
print("Beyond 1.96:", round(100 * (abs(t_stat) > 1.96).mean(), 1), "%; beyond 2.262:", round(100 * (abs(t_stat) > stats.t.ppf(0.975, 9)).mean(), 1), "%")
'''


EX7 = '''# 1. Geometric probabilities with p = 0.1786
print("P(X = 3):", round((1 - p) ** 2 * p, 4), "; P(X <= 5):", round(stats.geom.cdf(5, p), 3), "; record:", round((gaps_calls <= 5).mean(), 3), "; P(X > 10):", round(stats.geom.sf(10, p), 3), "; record:", round((gaps_calls > 10).mean(), 3))
'''
EX8 = '''# 1. Calls until the second ambulance call: model and record
pairs = gaps_calls[: len(gaps_calls) // 2 * 2].reshape(-1, 2).sum(axis=1)
print("Model mean:", round(2 / p, 2), "; model variance:", round(2 * (1 - p) / p ** 2, 1), "; record mean:", round(pairs.mean(), 2))
'''
EX9 = '''# 1. Second of arrival in 18:00-18:59: mean and last 15 minutes
print("Mean second:", round(seconds.mean(), 1), "; last 15 minutes:", round(100 * (seconds >= 2700).mean(), 1), "%; uniform: 1800 and 25%")
'''
EX10 = '''# 1. Gaps of more than 5 minutes
print("P(gap > 300):", round(exp(-300 / mean_gap), 3), "; record:", round((gaps > 300).mean(), 3))
'''
EX14 = '''# 1. 40 or more ambulance calls among 200 calls
print("Exact:", round(1 - stats.binom.cdf(39, n200, p), 4), "; normal:", round(stats.norm.sf(40, mean200, sd200), 4), "; with correction:", round(stats.norm.sf(39.5, mean200, sd200), 4))
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

    sec("12.1", "Introduction: the data", "Introdução: os dados")
    cell(LOAD)
    sec("12.2", "Calls in the evening hour", "As ligações da hora da noite",
        "How many calls arrive between 18:00 and 18:59, and how much does that number vary from day to day?",
        "Quantas ligações chegam entre 18:00 e 18:59, e quanto esse número varia de um dia para outro?")
    cell(C_COUNTS)
    sec("12.3", "A model for counts in an hour: the Poisson distribution", "Um modelo para contagens em uma hora: a distribuição de Poisson",
        "How likely is a rush of 14 or more calls in that hour?", "Qual a chance de um pico de 14 ou mais ligações nessa hora?")
    cell(C_POISSON)
    sec("12.4", "Ambulance or not: the Bernoulli and binomial distributions", "Ambulância ou não: as distribuições de Bernoulli e binomial",
        "Of the next 12 calls, how many will need an ambulance?", "Das próximas 12 ligações, quantas precisarão de ambulância?")
    cell(C_BINOMIAL)
    sec("12.5", "Recordings drawn without replacement: the hypergeometric distribution", "Gravações sorteadas sem reposição: a distribuição hipergeométrica",
        "Suppose a supervisor listened to 10 recordings drawn at random from the 142 calls of day 1. In how many of these 10 was it necessary to send an ambulance?",
        "Suponha que um supervisor ouviu 10 gravações sorteadas entre as 142 ligações do dia 1. Em quantas dessas 10 foi preciso enviar ambulância?")
    cell(C_HYPER)
    sec("12.6", "Waiting for the next ambulance call: the geometric and negative binomial distributions", "À espera da próxima ligação com ambulância: as distribuições geométrica e binomial negativa",
        "How many calls will pass until the next ambulance call, and until the third?", "Quantas ligações passarão até a próxima ligação com ambulância, e até a terceira?")
    cell(C_GEOM)
    sec("12.7", "When calls arrive: the uniform, exponential, and gamma distributions", "Quando as ligações chegam: as distribuições uniforme, exponencial e gama",
        "At what second of the hour does a call arrive, how long until the next call, and how long until the third?",
        "Em que segundo da hora uma ligação chega, quanto tempo até a próxima ligação e quanto tempo até a terceira?")
    cell(C_ARRIVALS)
    sec("12.8", "The wait: a measurement that is not a count", "A espera: uma medida que não é uma contagem",
        "How long does a caller wait for an operator?", "Quanto tempo quem liga espera por um atendente?")
    cell(C_WAIT)
    sec("12.9", "The normal distribution", "A distribuição normal",
        "Which model gives the chance of a wait of more than four minutes?", "Qual modelo dá a chance de uma espera de mais de quatro minutos?")
    cell(C_NORMAL)
    sec("12.10", "Skewed durations: the lognormal distribution", "Durações assimétricas: a distribuição lognormal",
        "Within what wait does the model estimate that nine callers in ten, or 19 in 20, are answered?", "Em que tempo o modelo estima que nove de cada dez pessoas, ou 19 de cada 20, são atendidas?")
    cell(C_LOGN)
    sec("12.11", "Three distributions that the tests will need", "Três distribuições de que os testes precisarão",
        "Which distributions will the later chapters use to compare days or shifts?", "Quais distribuições os capítulos seguintes usarão para comparar dias ou turnos?")
    cell(C_TESTS)
    exs = [("Calls from 12:00 to 12:59", "Ligações de 12:00 a 12:59", EX1), ("The Poisson model for 18:00 to 18:59", "O modelo de Poisson para 18:00 a 18:59", EX3),
           ("Calls from 03:00 to 03:59", "Ligações de 03:00 a 03:59", EX4), ("Ambulances among 12 calls", "Ambulâncias entre 12 ligações", EX5),
           ("Drawing without replacement", "Sorteio sem reposição", EX6), ("Calls until the first ambulance call", "Ligações até a primeira ligação com ambulância", EX7),
           ("Calls until the second ambulance call", "Ligações até a segunda ligação com ambulância", EX8), ("The second of arrival", "O segundo de chegada", EX9),
           ("Time between calls", "Tempo entre ligações", EX10), ("Fractions of the waits", "Frações das esperas", EX11),
           ("The normal model for the wait", "O modelo normal para a espera", EX12), ("The lognormal model", "O modelo lognormal", EX13),
           ("The normal approximation for 200 calls", "A aproximação normal para 200 ligações", EX14), ("Standardized means of samples of 10", "Médias padronizadas de amostras de 10", EX15)]
    nums = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    return S, [(nums[i], T(a, b), code(c)) for i, (a, b, c) in enumerate(exs)]
