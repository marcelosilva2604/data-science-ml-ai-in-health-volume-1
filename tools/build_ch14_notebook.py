"""Build the Chapter 14 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch14_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch14_solutions import SOL
from ch14_cells import cells as all_cells

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch14"
FILES = {"en": "ch14_hypothesis_testing_en.ipynb", "pt": "ch14_testes_hipoteses_pt.ipynb"}

HEAD = {
 "en": """# Chapter 14 · Hypothesis Testing: Logic and the Standard Tests: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, the surgical registry of two hospitals and a quality committee, through the committee's thirteen questions. **Part B** gives the written solution of every chapter exercise (statements are in the book) and, for the exercises whose solution needs a calculation, its code and result. Run the cells in order.

## Part A. The case

**Data.** `data/surgery.csv`: 800 rows, one per operated patient, and eight columns: `patient_id`, `hospital` (A or B), `weekday` (Mon to Sun), `asa_class` (1 to 4), `los_days`, `readmitted` (yes or no), `pain_day1`, `pain_day3`. Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 14 · Teste de hipóteses: lógica e os testes padrão: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, o registro cirúrgico de dois hospitais e um comitê de qualidade, pelas treze perguntas do comitê. A **Parte B** traz a solução escrita de cada exercício do capítulo (os enunciados estão no livro) e, nos exercícios cuja solução exige cálculo, o código e o resultado. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/surgery.csv`: 800 linhas, uma por paciente operado, e oito colunas: `patient_id`, `hospital` (A ou B), `weekday` (Mon a Sun), `asa_class` (1 a 4), `los_days`, `readmitted` (yes ou no), `pain_day1`, `pain_day3`. Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (seed 14, `generate_data.py`). Teaching values only; nothing here is an estimate for a real hospital.*",
        "pt": "---\n*Dados sintéticos (semente 14, `generate_data.py`). Valores apenas didáticos; nada aqui é estimativa para um hospital real.*"}


def build(lang):
    cells = []
    md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
    code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))
    md(HEAD[lang])
    part_a, exs = all_cells(lang)
    for kind, text in part_a:
        (md if kind == "md" else code)(text)
    md("## Part B. Exercise solutions" if lang == "en" else "## Parte B. Soluções dos exercícios")
    code_of = {k: block for k, title, block in exs}
    for k in sorted(SOL[lang]):
        title, text = SOL[lang][k]
        md(f"### 14.15 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
        md(text)
        if k in code_of:
            code(code_of[k])
    md(FOOT[lang])
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
    out = BASE / FILES[lang]
    nbf.write(nb, out)
    print("wrote", out.name, len(cells), "cells")


if __name__ == "__main__":
    build((Path(__file__).resolve().parent / "LANG").read_text().strip())
