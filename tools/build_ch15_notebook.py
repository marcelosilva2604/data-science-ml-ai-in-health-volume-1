"""Build the Chapter 15 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch15_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch15_solutions import SOL
from ch15_cells import cells as all_cells

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch15"
FILES = {"en": "ch15_pvalue_meaning_en.ipynb", "pt": "ch15_significado_valor_p_pt.ipynb"}

HEAD = {
 "en": """# Chapter 15 · The Meaning of a P-Value: Intervals, Noninferiority, and Interim Analyses: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, a randomized trial of 7 versus 14 days of antibiotics and the stewardship committee that reads it, through the committee's ten questions. **Part B** gives the written solution of every chapter exercise (statements are in the book) and, for the exercises whose solution needs a calculation, its code and result. Run the cells in order. The packages are listed in `requirements.txt`, and the notebook reads `data/trial.csv` from its own folder.

## Part A. The case

**Data.** `data/trial.csv`: 1,200 rows, one per enrolled patient, and six columns: `patient_id`, `site` (S01 to S12), `month` (1 to 24), `allocated` (short or standard), `received` (short or standard), `failure_30d` (yes or no). Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 15 · O significado de um valor de p: intervalos, não inferioridade e análises interinas: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, um ensaio randomizado de 7 contra 14 dias de antibiótico e o comitê de uso racional que o lê, pelas dez perguntas do comitê. A **Parte B** traz a solução escrita de cada exercício do capítulo (os enunciados estão no livro) e, nos exercícios cuja solução exige cálculo, o código e o resultado. Execute as células em ordem. Os pacotes estão listados em `requirements.txt`, e o caderno lê `data/trial.csv` da própria pasta.

## Parte A. O caso

**Dados.** `data/trial.csv`: 1.200 linhas, uma por paciente incluído, e seis colunas: `patient_id`, `site` (S01 a S12), `month` (1 a 24), `allocated` (short ou standard), `received` (short ou standard), `failure_30d` (yes ou no). Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (seed 1964, `generate_data.py`). Teaching values only; nothing here is an estimate for a real trial.*",
        "pt": "---\n*Dados sintéticos (semente 1964, `generate_data.py`). Valores apenas didáticos; nada aqui é estimativa para um ensaio real.*"}


def build(lang):
    cells = []
    md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip("\n")))
    code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip("\n")))
    md(HEAD[lang])
    part_a, exs = all_cells(lang)
    for kind, text in part_a:
        (md if kind == "md" else code)(text)
    md("## Part B. Exercise solutions" if lang == "en" else "## Parte B. Soluções dos exercícios")
    md("Part B reuses variables created in Part A (`theta`, `se`, `margin`, `theta_pp`, `se_pp`, `obf_c`): run Part A first." if lang == "en" else "A Parte B reutiliza variáveis criadas na Parte A (`theta`, `se`, `margin`, `theta_pp`, `se_pp`, `obf_c`): execute a Parte A primeiro.")
    code_of = {k: block for k, title, block in exs}
    for k in sorted(SOL[lang]):
        title, text = SOL[lang][k]
        md(f"### 15.18 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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
