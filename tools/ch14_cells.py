"""All code cells of the Chapter 14 notebook (Part A by book section, and Part B): one cell each, reasoning as numbered
comments, output as plain sentences. Beginner-friendly Python: print with commas, round(), no f-strings, no helper functions.
The cells are written once in English; the Portuguese cell is the same code with every comment and every printed text
translated whole through the PT table (a comment or a string literal is looked up as a whole; a missing translation stops the build)."""
import re

PT = {
 "3. Difference in rates (B - A) and its Newcombe 95% interval": "3. Diferença de taxas (B - A) e seu intervalo de Newcombe de 95%",
 "; Newcombe 95% CI": "; IC de Newcombe de 95%",
 "3. Exact binomial power of the z test against 15%, with 316 and 320 patients": "3. Poder binomial exato do teste z contra 15%, com 316 e 320 pacientes",
 "Exact power with": "Poder exato com",
 "patients:": "pacientes:",
 "Difference B - A:": "Diferença B - A:",
 "4. Variance ratio (B over A) and its two-sided p-value": "4. Razão das variâncias (B sobre A) e seu valor de p bilateral",
 "5. 95% confidence interval for the ratio": "5. Intervalo de confiança de 95% para a razão",
 "6. Levene test centered on the median, which does not need normal data": "6. Teste de Levene centrado na mediana, que não exige dados normais",
 "All 800: 95% CI": "Todos os 800: IC de 95%",
 "z =": "z =",
 "1. Patients for a difference of 0.5 day (alpha = 0.05, power 80%), with the exact normal quantiles": "1. Pacientes para uma diferença de 0,5 dia (alfa = 0,05, poder de 80%), com os quantis exatos da normal",
 "5. With the t test, which also estimates sigma: the smallest sample whose power reaches 80%": "5. Com o teste t, que também estima sigma: a menor amostra cujo poder chega a 80%",
 "Patients for the t test:": "Pacientes para o teste t:",
 "3. The z test, taking the standard deviation as known: two-sided p from the normal curve": "3. O teste z, tomando o desvio padrão como conhecido: p bilateral pela curva normal",
 "; two-sided p from the normal curve =": "; p bilateral pela curva normal =",
 "3. Levene test centered on the median, which does not need normal data": "3. Teste de Levene centrado na mediana, que não exige dados normais",
 "Levene (median): W =": "Levene (mediana): W =",
 "5. 95% interval of the mean change in all 800 patients": "5. Intervalo de 95% da variação média nos 800 pacientes",
 "6. Power of the paired test with 30 patients for the change seen in the 800": "6. Poder do teste pareado com 30 pacientes para a variação vista nos 800",
 "Power of a paired test with 30 patients for that change:": "Poder de um teste pareado com 30 pacientes para essa variação:",
 "4. Departure from the linear trend: the ordinary chi-square minus the trend chi-square, 2 degrees of freedom": "4. Desvio da tendência linear: o qui-quadrado comum menos o de tendência, 2 graus de liberdade",
 "Departure from linearity: chi-square =": "Desvio da linearidade: qui-quadrado =",
 "; 2 degrees of freedom; p =": "; 2 graus de liberdade; p =",
 "4. Difference in readmission between class 4 and class 1, with a Newcombe 95% interval": "5. Diferença de reinternação entre a classe 4 e a classe 1, com intervalo de Newcombe de 95%",
 "Class 4 minus class 1:": "Classe 4 menos classe 1:",
 "points; Newcombe 95% CI": "pontos; IC de Newcombe de 95%",
 "4. Power of the z test with the 800 patients if the true rate were the observed one": "4. Poder do teste z com os 800 pacientes se a taxa verdadeira fosse a observada",
 "Power with": "Poder com",
 "patients for": "pacientes para",
 "% against 10%:": "% contra 10%:",
 "Kirkwood version (statistic times (N - 1)/N):": "Versão de Kirkwood (estatística vezes (N - 1)/N):",
 "5. Weekend table: the chi-square with N - 1 in place of N, and Fisher if all three readmissions had been in hospital B": "5. Tabela de fim de semana: o qui-quadrado com N - 1 no lugar de N, e Fisher se as três reinternações estivessem todas no hospital B",
 "Chi-square with N - 1:": "Qui-quadrado com N - 1:",
 "Fisher if all three readmissions were in hospital B: p =": "Fisher se as três reinternações estivessem no hospital B: p =",
 "1. Admissions from Monday to Friday (weekend admissions are left out)": "1. Internações de segunda a sexta (as de fim de semana ficam de fora)",
 "Does the readmission rate differ from the 10% target?": "A taxa de reinternação difere da meta de 10%?",
 # comments
 "1. Read the registry: one row is one operated patient": "1. Ler o registro: cada linha é um paciente operado",
 "2. Count rows and columns": "2. Contar linhas e colunas",
 "The first five rows": "As cinco primeiras linhas",
 "1. The sample: length of stay of the 800 patients": "1. A amostra: permanência dos 800 pacientes",
 "2. The hypotheses: H0 is mu = 5; the alternative is two-sided": "2. As hipóteses: H0 é mu = 5; a alternativa é bilateral",
 "1. Standard error and the z statistic, taking the sample standard deviation as if it were known": "1. Erro padrão e estatística z, tomando o desvio padrão da amostra como se fosse conhecido",
 "2. Skewness and median of the stay": "2. Assimetria e mediana da permanência",
 "1. The z statistic and the two-sided and one-sided p-values from the normal curve": "1. A estatística z e os valores de p bilateral e unilateral pela curva normal",
 "1. 2,000 samples of 100 patients drawn with replacement: p-values testing the true mean and a false mean (5.0)": "1. 2.000 amostras de 100 pacientes sorteadas com reposição: valores de p testando a média verdadeira e uma média falsa (5,0)",
 "2. p-values of the true null in five equal bins from 0 to 1": "2. Valores de p da nula verdadeira em cinco faixas iguais de 0 a 1",
 "3. Rejections at alpha = 0.05 when the null is true (type I error) and when it is false": "3. Rejeições com alfa = 0,05 quando a nula é verdadeira (erro tipo I) e quando é falsa",
 "4. Type II error rate with 100 patients for the 0.34-day difference": "4. Taxa de erro tipo II com 100 pacientes para a diferença de 0,34 dia",
 "1. Patients for a difference of 0.5 day (alpha = 0.05, power 80%)": "1. Pacientes para uma diferença de 0,5 dia (alfa = 0,05, poder de 80%)",
 "2. Power with 100 patients for 0.5 day": "2. Poder com 100 pacientes para 0,5 dia",
 "3. Patients for the observed difference": "3. Pacientes para a diferença observada",
 "4. Patients to detect a rise in readmission from 10% to 15%": "4. Pacientes para detectar um aumento da reinternação de 10% para 15%",
 "1. One-sample t test against 5 days": "1. Teste t de uma amostra contra 5 dias",
 "2. 95% confidence interval for the mean": "2. Intervalo de confiança de 95% para a média",
 "1. Readmissions and the z test against 10%": "1. Reinternações e o teste z contra 10%",
 "2. Exact binomial test and Wilson interval": "2. Teste binomial exato e intervalo de Wilson",
 "1. Length of stay in each hospital": "1. Permanência em cada hospital",
 "2. Student test (pooled variance)": "2. Teste de Student (variância agrupada)",
 "3. Welch test and 95% interval for the difference": "3. Teste de Welch e intervalo de 95% para a diferença",
 "1. Variance ratio (B over A) and its two-sided p-value": "1. Razão das variâncias (B sobre A) e seu valor de p bilateral",
 "2. 95% confidence interval for the ratio": "2. Intervalo de confiança de 95% para a razão",
 "1. Pilot: the first 30 patients, change in pain from day 1 to day 3": "1. Piloto: os primeiros 30 pacientes, variação da dor do dia 1 ao dia 3",
 "2. Paired t test and 95% interval": "2. Teste t pareado e intervalo de 95%",
 "3. The same data treated, wrongly, as two independent groups": "3. Os mesmos dados tratados, de modo errado, como dois grupos independentes",
 "4. All 800 patients": "4. Todos os 800 pacientes",
 "1. Admissions from Monday to Friday (weekend admissions are emergencies and are left out)": "1. Internações de segunda a sexta (as de fim de semana são emergências e ficam de fora)",
 "2. Chi-square goodness of fit and the contribution of each day": "2. Qui-quadrado de aderência e a contribuição de cada dia",
 "1. Hospital by readmission table": "1. Tabela de hospital por reinternação",
 "2. Chi-square test of independence, without and with the Yates correction": "2. Teste qui-quadrado de independência, sem e com a correção de Yates",
 "3. Difference in rates (B - A) and its 95% interval": "3. Diferença das taxas (B - A) e seu intervalo de 95%",
 "4. Weekend patients: Fisher's exact test": "4. Pacientes de fim de semana: teste exato de Fisher",
 "1. Readmissions by ASA class": "1. Reinternações por classe ASA",
 "2. Trend statistic with scores 1, 2, 3, 4": "2. Estatística de tendência com escores 1, 2, 3, 4",
 "3. Ordinary chi-square with 3 degrees of freedom": "3. Qui-quadrado comum com 3 graus de liberdade",
 "1. One-sided t test for hospital A against 5.5 days": "1. Teste t unilateral para o hospital A contra 5,5 dias",
 "1. Two-sided and one-sided p-values against 5 days": "1. Valores de p bilateral e unilateral contra 5 dias",
 "1. Share of p-values below 0.05 in the 2,000 samples of 100 patients": "1. Fração dos valores de p abaixo de 0,05 nas 2.000 amostras de 100 pacientes",
 "1. Sample size for 0.3 day and power with the 800 patients": "1. Tamanho da amostra para 0,3 dia e poder com os 800 pacientes",
 "1. Sample size for 10% against 13%, compared with 10% against 15%": "1. Tamanho da amostra para 10% contra 13%, comparado com 10% contra 15%",
 "1. Hospital B against 10%: z test and exact binomial test": "1. Hospital B contra 10%: teste z e teste binomial exato",
 "1. Student and Welch tests with the interval for the difference": "1. Testes de Student e de Welch com o intervalo da diferença",
 "1. Variance ratio and its 95% interval": "1. Razão das variâncias e seu intervalo de 95%",
 "1. Pilot of 30 and all 800 patients: paired and unpaired tests": "1. Piloto de 30 e todos os 800 pacientes: testes pareado e não pareado",
 "1. Chi-square of each weekday": "1. Qui-quadrado de cada dia da semana",
 "1. Independence with and without correction, and Fisher at weekends": "1. Independência com e sem correção, e Fisher nos fins de semana",
 "1. Trend and 3-degree chi-square": "1. Tendência e qui-quadrado de 3 graus",
 # strings
 "The registry has": "O registro tem", "rows (one per patient) and": "linhas (uma por paciente) e", "columns.": "colunas.",
 "Patients:": "Pacientes:", "; mean stay": "; permanência média", "days; standard deviation": "dias; desvio padrão", "; distance from the target of 5 days:": "; distância da meta de 5 dias:",
 "H0: mu = 5 days. Ha: mu different from 5 days (two-sided).": "H0: mu = 5 dias. Ha: mu diferente de 5 dias (bilateral).",
 "Standard error:": "Erro padrão:", "; z =": "; z =",
 "Skewness:": "Assimetria:", "; median:": "; mediana:", "days": "dias",
 "t =": "t =", "; two-sided p =": "; p bilateral =", "; one-sided p =": "; p unilateral =",
 "True null, p-values in five equal bins:": "Nula verdadeira, valores de p em cinco faixas iguais:",
 "Null true: rejected in": "Nula verdadeira: rejeitada em", "% of the samples; null false: rejected in": "% das amostras; nula falsa: rejeitada em", "%": "%",
 "Type II error rate (beta):": "Taxa de erro tipo II (beta):",
 "Patients for 0.5 day:": "Pacientes para 0,5 dia:", "-> rounded up": "-> arredondado para cima",
 "Power with 100 patients:": "Poder com 100 pacientes:",
 "Patients for the observed difference of": "Pacientes para a diferença observada de", "day:": "dia:",
 "Patients for 10% to 15%:": "Pacientes para 10% a 15%:",
 "; degrees of freedom": "; graus de liberdade", "; two-sided p =": "; p bilateral =",
 "t multiple:": "Múltiplo t:", "; 95% CI:": "; IC de 95%:", "to": "a",
 "Readmitted:": "Reinternados:", "of": "de", "(": "(", "%); z =": "%); z =",
 "Exact binomial two-sided p =": "Binomial exato, p bilateral =",
 "Wilson 95%:": "Wilson de 95%:",
 "Hospital A:": "Hospital A:", "Hospital B:": "Hospital B:", "patients; mean": "pacientes; média", "; standard deviation": "; desvio padrão",
 "Student: t =": "Student: t =", "; p =": "; p =", "; pooled standard deviation": "; desvio padrão agrupado", "; standard error": "; erro padrão",
 "Welch: t =": "Welch: t =", "; standard error": "; erro padrão",
 "Difference B - A:": "Diferença B - A:", "days; 95% CI": "dias; IC de 95%",
 "F =": "F =", "; degrees of freedom": "; graus de liberdade", "and": "e",
 "95% CI for the ratio:": "IC de 95% da razão:",
 "Pilot: mean change": "Piloto: variação média", "; correlation of the two days": "; correlação dos dois dias",
 "Paired: t =": "Pareado: t =", "; 95% CI": "; IC de 95%",
 "Unpaired: t =": "Não pareado: t =",
 "All 800: mean change": "Todos os 800: variação média",
 "Observed:": "Observado:", "; total": "; total", "; expected per day": "; esperado por dia",
 "chi-square =": "qui-quadrado =", "; degrees of freedom 4; p =": "; 4 graus de liberdade; p =",
 "Contribution of each day:": "Contribuição de cada dia:",
 "Readmission rates: A": "Taxas de reinternação: A", "%; B": "%; B",
 "; with Yates": "; com Yates",
 "Expected counts:": "Contagens esperadas:",
 "points; 95% CI": "pontos; IC de 95%",
 "Weekend table (A: no, yes; B: no, yes):": "Tabela do fim de semana (A: não, sim; B: não, sim):", "; expected": "; esperado",
 "Fisher: odds ratio": "Fisher: razão de chances",
 "; rates": "; taxas", "of": "de",
 "Z =": "Z =", "; chi-square for trend =": "; qui-quadrado de tendência =",
 "Chi-square (3 degrees of freedom) =": "Qui-quadrado (3 graus de liberdade) =",
 "Mean": "Média", "; one-sided p =": "; p unilateral =",
 "True mean (": "Média verdadeira (", "):": "):", "%; false mean (5.0):": "%; média falsa (5,0):",
 "Patients:": "Pacientes:", "; power with 800 patients:": "; poder com 800 pacientes:",
 "10% to 13%:": "10% a 13%:", "; 10% to 15%:": "; 10% a 15%:", "; ratio": "; razão",
 "Hospital B:": "Hospital B:", "Exact binomial: two-sided p =": "Binomial exato: p bilateral =",
 "Student: p =": "Student: p =", "Welch: p =": "Welch: p =",
 "F =": "F =", "; 95% CI": "; IC de 95%",
 "Pilot (30): paired p =": "Piloto (30): p pareado =", "; unpaired p =": "; p não pareado =", "All 800: paired p =": "Todos os 800: p pareado =",
 "Weekday contributions:": "Contribuições por dia:", "largest:": "maior:",
 "chi-square, plain:": "qui-quadrado, simples:", "; Yates:": "; Yates:", "; Fisher p =": "; Fisher p =",
 "; chi-square =": "; qui-quadrado =", "; correlation": "; correlação", "; largest:": "; maior:", "; p of trend =": "; p da tendência =", "; t =": "; t =", "Patients: 10% to 13%:": "Pacientes: 10% a 13%:",
 "Trend chi-square:": "Qui-quadrado de tendência:", "; 3 degrees of freedom:": "; 3 graus de liberdade:",
}


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


LOAD = '''# 1. Read the registry: one row is one operated patient
import numpy as np
import pandas as pd
from math import sqrt
from scipy import stats

df = pd.read_csv("data/surgery.csv")

# 2. Count rows and columns
rows, columns = df.shape
print("The registry has", rows, "rows (one per patient) and", columns, "columns.")
df.head()                                      # The first five rows
'''

C_HYP = '''# 1. The sample: length of stay of the 800 patients
los = df["los_days"].values
n = len(los)
m = los.mean()
s = los.std(ddof=1)
print("Patients:", n, "; mean stay", round(m, 3), "days; standard deviation", round(s, 3), "; distance from the target of 5 days:", round(m - 5, 3))

# 2. The hypotheses: H0 is mu = 5; the alternative is two-sided
print("H0: mu = 5 days. Ha: mu different from 5 days (two-sided).")
'''

C_STAT = '''# 1. Standard error and the z statistic, taking the sample standard deviation as if it were known
se = s / sqrt(n)
z_stat = (m - 5) / se
print("Standard error:", round(se, 4), "; z =", round(z_stat, 2))

# 2. Skewness and median of the stay
print("Skewness:", round(stats.skew(los), 2), "; median:", np.median(los), "days")
'''

C_PVALUE = '''# 1. The z statistic and the two-sided and one-sided p-values from the normal curve
p_two = 2 * stats.norm.sf(abs(z_stat))
p_one = stats.norm.sf(z_stat)
print("z =", round(z_stat, 2), "; two-sided p =", round(p_two, 5), "; one-sided p =", round(p_one, 5))
'''

C_ERRORS = '''# 1. 2,000 samples of 100 patients drawn with replacement: p-values testing the true mean and a false mean (5.0)
rng = np.random.default_rng(14)
p_true = []
p_false = []
for repetition in range(2000):
    sample = los[rng.choice(n, 100, replace=True)]
    p_true.append(stats.ttest_1samp(sample, m).pvalue)
    p_false.append(stats.ttest_1samp(sample, 5.0).pvalue)
p_true = np.array(p_true)
p_false = np.array(p_false)

# 2. p-values of the true null in five equal bins from 0 to 1
print("True null, p-values in five equal bins:", np.histogram(p_true, bins=5, range=(0, 1))[0])

# 3. Rejections at alpha = 0.05 when the null is true (type I error) and when it is false
print("Null true: rejected in", round(100 * (p_true < 0.05).mean(), 2), "% of the samples; null false: rejected in", round(100 * (p_false < 0.05).mean(), 2), "%")

# 4. Type II error rate with 100 patients for the 0.34-day difference
print("Type II error rate (beta):", round(100 * (p_false >= 0.05).mean(), 2), "%")
'''

C_POWER = '''# 1. Patients for a difference of 0.5 day (alpha = 0.05, power 80%), with the exact normal quantiles
za = stats.norm.ppf(0.975)
zb = stats.norm.ppf(0.80)
n_half = (za + zb) ** 2 * s ** 2 / 0.5 ** 2
print("Patients for 0.5 day:", round(n_half, 1), "-> rounded up", int(np.ceil(n_half)))

# 2. Power with 100 patients for 0.5 day
shift = 0.5 / (s / sqrt(100))
power100 = stats.norm.sf(za - shift) + stats.norm.cdf(-za - shift)
print("Power with 100 patients:", round(100 * power100, 1), "%")

# 3. Patients for the observed difference
n_obs = (za + zb) ** 2 * s ** 2 / (m - 5) ** 2
print("Patients for the observed difference of", round(m - 5, 3), "day:", round(n_obs, 1))

# 4. Patients to detect a rise in readmission from 10% to 15%
n_prop = ((za * sqrt(0.10 * 0.90) + zb * sqrt(0.15 * 0.85)) / 0.05) ** 2
print("Patients for 10% to 15%:", round(n_prop, 1))

# 5. With the t test, which also estimates sigma: the smallest sample whose power reaches 80%
n_t = 10
power_t = 0
while power_t < 0.80:
    n_t = n_t + 1
    t_crit = stats.t.ppf(0.975, n_t - 1)
    shift_t = 0.5 / s * sqrt(n_t)
    power_t = stats.nct.sf(t_crit, n_t - 1, shift_t) + stats.nct.cdf(-t_crit, n_t - 1, shift_t)
print("Patients for the t test:", n_t)
'''

C_TTEST = '''# 1. One-sample t test against 5 days
result = stats.ttest_1samp(los, 5)
print("t =", round(result.statistic, 3), "; degrees of freedom", n - 1, "; two-sided p =", round(result.pvalue, 5))

# 2. 95% confidence interval for the mean
multiple = stats.t.ppf(0.975, n - 1)
print("t multiple:", round(multiple, 3), "; 95% CI:", round(m - multiple * se, 3), "to", round(m + multiple * se, 3))
# 3. The z test, taking the standard deviation as known: two-sided p from the normal curve
print("z =", round(z_stat, 3), "; two-sided p from the normal curve =", round(2 * stats.norm.sf(abs(z_stat)), 5))
'''

C_PROP = '''# 1. Readmissions and the z test against 10%
k = int((df["readmitted"] == "yes").sum())
p_hat = k / n
z_prop = (p_hat - 0.10) / sqrt(0.10 * 0.90 / n)
print("Readmitted:", k, "of", n, "(", round(100 * p_hat, 2), "%); z =", round(z_prop, 3), "; two-sided p =", round(2 * stats.norm.sf(abs(z_prop)), 4), "; one-sided p =", round(stats.norm.sf(z_prop), 4))

# 2. Exact binomial test and Wilson interval
print("Exact binomial two-sided p =", round(stats.binomtest(k, n, 0.10).pvalue, 4))
centre = (p_hat + za ** 2 / (2 * n)) / (1 + za ** 2 / n)
half = za * sqrt(p_hat * (1 - p_hat) / n + za ** 2 / (4 * n ** 2)) / (1 + za ** 2 / n)
print("Wilson 95%:", round(100 * (centre - half), 1), "to", round(100 * (centre + half), 1), "%")

# 3. Exact binomial power of the z test against 15%, with 316 and 320 patients
for size in (316, 320):
    counts = np.arange(size + 1)
    z_counts = (counts / size - 0.10) / sqrt(0.10 * 0.90 / size)
    rejected = np.abs(z_counts) > za
    print("Exact power with", size, "patients:", round(100 * stats.binom.pmf(counts, size, 0.15)[rejected].sum(), 1), "%")

# 4. Power of the z test with the 800 patients if the true rate were the observed one
se_null = sqrt(0.10 * 0.90 / n)
se_alt = sqrt(p_hat * (1 - p_hat) / n)
gap_rate = abs(p_hat - 0.10)
power_rate = stats.norm.sf((za * se_null - gap_rate) / se_alt) + stats.norm.cdf((-za * se_null - gap_rate) / se_alt)
print("Power with", n, "patients for", round(100 * p_hat, 1), "% against 10%:", round(100 * power_rate, 1), "%")
'''

C_TWO = '''# 1. Length of stay in each hospital
a = df[df["hospital"] == "A"]["los_days"].values
b = df[df["hospital"] == "B"]["los_days"].values
print("Hospital A:", len(a), "patients; mean", round(a.mean(), 2), "; standard deviation", round(a.std(ddof=1), 2))
print("Hospital B:", len(b), "patients; mean", round(b.mean(), 2), "; standard deviation", round(b.std(ddof=1), 2))

# 2. Student test (pooled variance)
student = stats.ttest_ind(b, a)
pooled = sqrt(((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / (len(a) + len(b) - 2))
print("Student: t =", round(student.statistic, 3), "; p =", round(student.pvalue, 5), "; pooled standard deviation", round(pooled, 3), "; standard error", round(pooled * sqrt(1 / len(a) + 1 / len(b)), 4))

# 3. Welch test and 95% interval for the difference
welch = stats.ttest_ind(b, a, equal_var=False)
va = a.var(ddof=1) / len(a)
vb = b.var(ddof=1) / len(b)
df_welch = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
diff = b.mean() - a.mean()
se_welch = sqrt(va + vb)
margin_welch = stats.t.ppf(0.975, df_welch) * se_welch
print("Welch: t =", round(welch.statistic, 3), "; degrees of freedom", round(df_welch, 1), "; p =", round(welch.pvalue, 5), "; standard error", round(se_welch, 3))
print("Difference B - A:", round(diff, 3), "days; 95% CI", round(diff - margin_welch, 2), "to", round(diff + margin_welch, 2))
'''

C_F = '''# 4. Variance ratio (B over A) and its two-sided p-value
ratio = b.var(ddof=1) / a.var(ddof=1)
df_b = len(b) - 1
df_a = len(a) - 1
p_ratio = 2 * min(stats.f.sf(ratio, df_b, df_a), stats.f.cdf(ratio, df_b, df_a))
print("F =", round(ratio, 3), "; degrees of freedom", df_b, "and", df_a, "; two-sided p =", p_ratio)

# 5. 95% confidence interval for the ratio
print("95% CI for the ratio:", round(ratio / stats.f.ppf(0.975, df_b, df_a), 2), "to", round(ratio * stats.f.ppf(0.975, df_a, df_b), 2))
# 6. Levene test centered on the median, which does not need normal data
levene = stats.levene(b, a, center="median")
print("Levene (median): W =", round(levene.statistic, 1), "; p =", levene.pvalue)
'''

C_PAIRED = '''# 1. Pilot: the first 30 patients, change in pain from day 1 to day 3
pilot = df.iloc[:30]
change = (pilot["pain_day3"] - pilot["pain_day1"]).values
print("Pilot: mean change", round(change.mean(), 3), "; standard deviation", round(change.std(ddof=1), 3), "; correlation of the two days", round(np.corrcoef(pilot["pain_day1"], pilot["pain_day3"])[0, 1], 2))

# 2. Paired t test and 95% interval
paired = stats.ttest_rel(pilot["pain_day3"], pilot["pain_day1"])
margin = stats.t.ppf(0.975, 29) * change.std(ddof=1) / sqrt(30)
print("Paired: t =", round(paired.statistic, 3), "; p =", round(paired.pvalue, 3), "; 95% CI", round(change.mean() - margin, 2), "to", round(change.mean() + margin, 2))

# 3. The same data treated, wrongly, as two independent groups
unpaired = stats.ttest_ind(pilot["pain_day3"], pilot["pain_day1"])
print("Unpaired: t =", round(unpaired.statistic, 3), "; p =", round(unpaired.pvalue, 3))

# 4. All 800 patients
everyone = stats.ttest_rel(df["pain_day3"], df["pain_day1"])
print("All 800: mean change", round((df["pain_day3"] - df["pain_day1"]).mean(), 3), "; t =", round(everyone.statistic, 2), "; p =", everyone.pvalue)
# 5. 95% interval of the mean change in all 800 patients
change_all = (df["pain_day3"] - df["pain_day1"]).values
margin_all = stats.t.ppf(0.975, 799) * change_all.std(ddof=1) / sqrt(800)
print("All 800: 95% CI", round(change_all.mean() - margin_all, 2), "to", round(change_all.mean() + margin_all, 2))

# 6. Power of the paired test with 30 patients for the change seen in the 800
t_crit_30 = stats.t.ppf(0.975, 29)
shift_30 = abs(change_all.mean()) / change_all.std(ddof=1) * sqrt(30)
power_30 = stats.nct.sf(t_crit_30, 29, shift_30) + stats.nct.cdf(-t_crit_30, 29, shift_30)
print("Power of a paired test with 30 patients for that change:", round(100 * power_30, 1), "%")
'''

C_GOF = '''# 1. Admissions from Monday to Friday (weekend admissions are left out)
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
observed = df[df["weekday"].isin(days)]["weekday"].value_counts().reindex(days).values
expected = observed.sum() / 5
print("Observed:", observed, "; total", observed.sum(), "; expected per day", round(expected, 1))

# 2. Chi-square goodness of fit and the contribution of each day
fit = stats.chisquare(observed)
print("chi-square =", round(fit.statistic, 2), "; degrees of freedom 4; p =", round(fit.pvalue, 4))
print("Contribution of each day:", np.round((observed - expected) ** 2 / expected, 2))
'''

C_INDEP = '''# 1. Hospital by readmission table
table = pd.crosstab(df["hospital"], df["readmitted"])
print(table)
size_a = table.loc["A"].sum()
size_b = table.loc["B"].sum()
rate_a = table.loc["A", "yes"] / size_a
rate_b = table.loc["B", "yes"] / size_b
print("Readmission rates: A", round(100 * rate_a, 1), "%; B", round(100 * rate_b, 1), "%")

# 2. Chi-square test of independence, without and with the Yates correction
plain = stats.chi2_contingency(table, correction=False)
yates = stats.chi2_contingency(table)
print("chi-square =", round(plain[0], 3), "; p =", round(plain[1], 3), "; with Yates", round(yates[0], 3), "; p =", round(yates[1], 3))
print("Expected counts:", np.round(plain[3], 2).tolist())

# 3. Difference in rates (B - A) and its Newcombe 95% interval
centre_a = (rate_a + za ** 2 / (2 * size_a)) / (1 + za ** 2 / size_a)
half_a = za * sqrt(rate_a * (1 - rate_a) / size_a + za ** 2 / (4 * size_a ** 2)) / (1 + za ** 2 / size_a)
centre_b = (rate_b + za ** 2 / (2 * size_b)) / (1 + za ** 2 / size_b)
half_b = za * sqrt(rate_b * (1 - rate_b) / size_b + za ** 2 / (4 * size_b ** 2)) / (1 + za ** 2 / size_b)
gap_ba = rate_b - rate_a
low_ba = gap_ba - sqrt((rate_b - (centre_b - half_b)) ** 2 + ((centre_a + half_a) - rate_a) ** 2)
high_ba = gap_ba + sqrt(((centre_b + half_b) - rate_b) ** 2 + (rate_a - (centre_a - half_a)) ** 2)
print("Difference B - A:", round(100 * gap_ba, 1), "points; Newcombe 95% CI", round(100 * low_ba, 1), "to", round(100 * high_ba, 1))

# 4. Weekend patients: Fisher's exact test
weekend = df[df["weekday"].isin(["Sat", "Sun"])]
table_weekend = pd.crosstab(weekend["hospital"], weekend["readmitted"])
fisher = stats.fisher_exact(table_weekend)
print("Weekend table (A: no, yes; B: no, yes):", table_weekend.values.tolist(), "; expected", np.round(stats.chi2_contingency(table_weekend, correction=False)[3], 2).tolist())
print("Fisher: odds ratio", round(fisher.statistic, 2), "; p =", round(fisher.pvalue, 3))
# 5. Weekend table: the chi-square with N - 1 in place of N, and Fisher if all three readmissions had been in hospital B
a_no, a_yes = table_weekend.loc["A", "no"], table_weekend.loc["A", "yes"]
b_no, b_yes = table_weekend.loc["B", "no"], table_weekend.loc["B", "yes"]
total_weekend = a_no + a_yes + b_no + b_yes
chi_n1 = (a_yes * b_no - a_no * b_yes) ** 2 * (total_weekend - 1) / ((a_no + a_yes) * (b_no + b_yes) * (a_no + b_no) * (a_yes + b_yes))
print("Chi-square with N - 1:", round(chi_n1, 2), "; p =", round(stats.chi2.sf(chi_n1, 1), 2))
print("Fisher if all three readmissions were in hospital B: p =", round(stats.fisher_exact([[a_no + a_yes, 0], [b_no + b_yes - 3, 3]]).pvalue, 3))
'''

C_TREND = '''# 1. Readmissions by ASA class
df["yes"] = (df["readmitted"] == "yes").astype(int)
events = df.groupby("asa_class")["yes"].sum().values
sizes = df.groupby("asa_class").size().values
print("Readmitted:", events, "of", sizes, "; rates", np.round(100 * events / sizes, 1), "%")

# 2. Trend statistic with scores 1, 2, 3, 4
scores = np.array([1, 2, 3, 4])
total = sizes.sum()
p_bar = events.sum() / total
numerator = (scores * (events - sizes * p_bar)).sum()
spread = (sizes * scores ** 2).sum() - (sizes * scores).sum() ** 2 / total
Z = numerator / sqrt(p_bar * (1 - p_bar) * spread)
print("Z =", round(Z, 2), "; chi-square for trend =", round(Z ** 2, 1), "; p =", 2 * stats.norm.sf(abs(Z)))
print("Kirkwood version (statistic times (N - 1)/N):", round(Z ** 2 * (total - 1) / total, 2))

# 3. Ordinary chi-square with 3 degrees of freedom
pearson = stats.chi2_contingency(np.array([events, sizes - events]))
print("Chi-square (3 degrees of freedom) =", round(pearson[0], 1), "; p =", pearson[1])

# 4. Difference in readmission between class 4 and class 1, with a Newcombe 95% interval
p4 = events[3] / sizes[3]
p1 = events[0] / sizes[0]
centre4 = (p4 + za ** 2 / (2 * sizes[3])) / (1 + za ** 2 / sizes[3])
half4 = za * sqrt(p4 * (1 - p4) / sizes[3] + za ** 2 / (4 * sizes[3] ** 2)) / (1 + za ** 2 / sizes[3])
centre1 = (p1 + za ** 2 / (2 * sizes[0])) / (1 + za ** 2 / sizes[0])
half1 = za * sqrt(p1 * (1 - p1) / sizes[0] + za ** 2 / (4 * sizes[0] ** 2)) / (1 + za ** 2 / sizes[0])
gap = p4 - p1
low = gap - sqrt((p4 - (centre4 - half4)) ** 2 + ((centre1 + half1) - p1) ** 2)
high = gap + sqrt(((centre4 + half4) - p4) ** 2 + (p1 - (centre1 - half1)) ** 2)
print("Class 4 minus class 1:", round(100 * gap, 1), "points; Newcombe 95% CI", round(100 * low, 1), "to", round(100 * high, 1))
'''

EX1 = '''# 1. One-sided t test for hospital A against 5.5 days
a = df[df["hospital"] == "A"]["los_days"].values
res = stats.ttest_1samp(a, 5.5, alternative="less")
se_a = a.std(ddof=1) / sqrt(len(a))
margin_a = stats.t.ppf(0.975, len(a) - 1) * se_a
print("Mean", round(a.mean(), 3), "; standard error", round(se_a, 4), "; t =", round(res.statistic, 2), "; one-sided p =", res.pvalue, "; 95% CI", round(a.mean() - margin_a, 2), "to", round(a.mean() + margin_a, 2))
'''
EX2 = '''# 1. Two-sided and one-sided p-values against 5 days
print("t =", round(stats.ttest_1samp(los, 5).statistic, 2), "; two-sided p =", round(stats.ttest_1samp(los, 5).pvalue, 5), "; one-sided p =", round(stats.ttest_1samp(los, 5, alternative="greater").pvalue, 5))
'''
EX3 = '''# 1. Share of p-values below 0.05 in the 2,000 samples of 100 patients
print("True mean (", round(m, 3), "):", round(100 * (p_true < 0.05).mean(), 2), "%; false mean (5.0):", round(100 * (p_false < 0.05).mean(), 2), "%")
'''
EX4 = '''# 1. Sample size for 0.3 day and power with the 800 patients
n_03 = (za + zb) ** 2 * s ** 2 / 0.3 ** 2
shift_03 = 0.3 / (s / sqrt(800))
print("Patients:", round(n_03, 1), "; power with 800 patients:", round(stats.norm.sf(za - shift_03) + stats.norm.cdf(-za - shift_03), 3))
'''
EX5 = '''# 1. Sample size for 10% against 13%, compared with 10% against 15%
n_13 = ((za * sqrt(0.10 * 0.90) + zb * sqrt(0.13 * 0.87)) / 0.03) ** 2
print("Patients: 10% to 13%:", round(n_13, 1), "; 10% to 15%:", round(n_prop, 1), "; ratio", round(n_13 / n_prop, 2))
'''
EX6 = '''# 1. Hospital B against 10%: z test and exact binomial test
k_b = int((df[df["hospital"] == "B"]["readmitted"] == "yes").sum())
n_b = int((df["hospital"] == "B").sum())
z_hb = (k_b / n_b - 0.10) / sqrt(0.10 * 0.90 / n_b)
print("Hospital B:", k_b, "of", n_b, "; z =", round(z_hb, 2), "; two-sided p =", round(2 * stats.norm.sf(abs(z_hb)), 4), "; one-sided p =", round(stats.norm.sf(z_hb), 4))
print("Exact binomial: two-sided p =", round(stats.binomtest(k_b, n_b, 0.10).pvalue, 4), "; one-sided p =", round(stats.binomtest(k_b, n_b, 0.10, alternative="greater").pvalue, 4))
'''
EX7 = '''# 1. Student and Welch tests with the interval for the difference
se_student = pooled * sqrt(1 / len(a) + 1 / len(b))
margin_student = stats.t.ppf(0.975, len(a) + len(b) - 2) * se_student
print("Student: p =", round(student.pvalue, 5), "; 95% CI", round(diff - margin_student, 2), "to", round(diff + margin_student, 2))
print("Welch: p =", round(welch.pvalue, 5), "; 95% CI", round(diff - margin_welch, 2), "to", round(diff + margin_welch, 2))
'''
EX8 = '''# 1. Variance ratio and its 95% interval
print("F =", round(ratio, 3), "; two-sided p =", p_ratio, "; 95% CI", round(ratio / stats.f.ppf(0.975, df_b, df_a), 2), "to", round(ratio * stats.f.ppf(0.975, df_a, df_b), 2))
'''
EX9 = '''# 1. Pilot of 30 and all 800 patients: paired and unpaired tests
print("Pilot (30): paired p =", round(paired.pvalue, 3), "; unpaired p =", round(unpaired.pvalue, 3), "; correlation", round(np.corrcoef(pilot["pain_day1"], pilot["pain_day3"])[0, 1], 2))
print("All 800: paired p =", everyone.pvalue, "; t =", round(everyone.statistic, 2))
'''
EX10 = '''# 1. Chi-square of each weekday
print("Weekday contributions:", np.round((observed - expected) ** 2 / expected, 2), "; chi-square =", round(fit.statistic, 2), "; largest:", days[int(np.argmax((observed - expected) ** 2 / expected))])
'''
EX11 = '''# 1. Independence with and without correction, and Fisher at weekends
print("chi-square, plain:", round(plain[0], 3), "; p =", round(plain[1], 3), "; Yates:", round(yates[0], 3), "; p =", round(yates[1], 3), "; Fisher p =", round(fisher.pvalue, 3))
'''
EX12 = '''# 1. Trend and 3-degree chi-square
print("Trend chi-square:", round(Z ** 2, 1), "; 3 degrees of freedom:", round(pearson[0], 1), "; p of trend =", 2 * stats.norm.sf(abs(Z)))
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

    sec("14.1", "Introduction: the data", "Introdução: os dados")
    cell(LOAD)
    sec("14.2", "Null and alternative hypotheses", "Hipóteses nula e alternativa",
        "Does the average stay differ from the target of 5 days, and what must be stated before it can be tested?",
        "A permanência média difere da meta de 5 dias, e o que precisa ser declarado antes que isso possa ser testado?")
    cell(C_HYP)
    sec("14.3", "The test statistic and its null distribution", "A estatística de teste e sua distribuição nula",
        "How far from 5 days is the sample mean, measured in standard errors?", "A que distância de 5 dias está a média amostral, medida em erros padrão?")
    cell(C_STAT)
    sec("14.4", "The p-value", "O valor de p",
        "How surprising is that distance if the true mean were 5 days?", "Quão surpreendente é essa distância se a média verdadeira fosse 5 dias?")
    cell(C_PVALUE)
    sec("14.5", "Significance level, decisions, and the two types of error", "Nível de significância, decisões e os dois tipos de erro",
        "How often would the committee decide wrongly, and in which direction?", "Com que frequência o comitê decidiria errado, e em que direção?")
    cell(C_ERRORS)
    sec("14.6", "Power and the sample size of a test", "Poder e tamanho da amostra de um teste",
        "How many patients are needed to detect a difference of half a day?", "Quantos pacientes são necessários para detectar uma diferença de meio dia?")
    cell(C_POWER)
    sec("14.7", "The one-sample t test for a mean", "O teste t de uma amostra para uma média",
        "Which test serves for the stay when the standard deviation must be estimated?", "Que teste serve para a permanência quando o desvio padrão precisa ser estimado?")
    cell(C_TTEST)
    sec("14.8", "The z test for a proportion", "O teste z para uma proporção",
        "Does the readmission rate differ from the 10% target?", "A taxa de reinternação difere da meta de 10%?")
    cell(C_PROP)
    sec("14.9", "The two-sample t test: Student and Welch", "O teste t de duas amostras: Student e Welch",
        "Do the two hospitals differ in average stay and in how much it varies?", "Os dois hospitais diferem na permanência média e em quanto ela varia?")
    cell(C_TWO)
    cell(C_F)
    sec("14.10", "The paired t test", "O teste t pareado",
        "Did pain change between day 1 and day 3?", "A dor mudou entre o primeiro e o terceiro dia?")
    cell(C_PAIRED)
    sec("14.11", "The chi-square goodness-of-fit test", "O teste qui-quadrado de aderência",
        "Are admissions spread equally over the weekdays?", "As internações se distribuem igualmente pelos dias úteis?")
    cell(C_GOF)
    sec("14.12", "The chi-square test of independence and Fisher's exact test", "O teste qui-quadrado de independência e o teste exato de Fisher",
        "Is readmission linked to the hospital?", "A reinternação está ligada ao hospital?")
    cell(C_INDEP)
    sec("14.13", "Trend tests across ordered groups", "Testes de tendência em grupos ordenados",
        "Is readmission linked to the ASA physical status class?", "A reinternação está ligada à classe de estado físico ASA?")
    cell(C_TREND)
    exs = [("Hospital A against 5.5 days", "Hospital A contra 5,5 dias", EX1), ("One-sided and two-sided p-values", "Valores de p unilateral e bilateral", EX2),
           ("P-values under a true and a false null", "Valores de p com nula verdadeira e falsa", EX3), ("Sample size and power for 0.3 day", "Tamanho da amostra e poder para 0,3 dia", EX4),
           ("Sample size for a proportion", "Tamanho da amostra para uma proporção", EX5), ("Readmission in hospital B", "Reinternação no hospital B", EX6),
           ("Student and Welch", "Student e Welch", EX7), ("Equality of two variances", "Igualdade de duas variâncias", EX8),
           ("Pain: paired and unpaired", "Dor: pareado e não pareado", EX9), ("Admissions by weekday", "Internações por dia da semana", EX10),
           ("Hospital and readmission; Fisher", "Hospital e reinternação; Fisher", EX11), ("Trend across ASA classes", "Tendência nas classes ASA", EX12)]
    return S, [(i + 1, T(a, b), code(c)) for i, (a, b, c) in enumerate(exs)]
