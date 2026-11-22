"""Build the Chapter 12 companion notebook (one language per repository, see tools/LANG).

Companion, not the book: code and numeric results only. The explanations live in the book. One code cell per book
section that has a calculation (headed by the book's own number and title), then one cell per exercise that needs code.
Run from the repository root:  python tools/build_ch12_notebook.py
"""
from pathlib import Path
import sys
import nbformat as nbf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ch12_solutions import SOL
from ch12_cells import cells as all_cells

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "chapters" / "ch12"
FILES = {"en": "ch12_random_variables_en.ipynb", "pt": "ch12_variaveis_aleatorias_pt.ipynb"}

HEAD = {
 "en": """# Chapter 12 · Random Variables and Distributions: companion notebook
*Data Science and Artificial Intelligence in Health, Volume 1*

> **This notebook accompanies the book chapter; it does not reproduce it.** Definitions, derivations, and explanations are in the book. Here you run the calculations on the case and check the numbers. All data are **synthetic**, and the values are for teaching purposes only.

**Part A** follows the chapter's case, the record of a city's emergency call center, through the director's nine questions. **Part B** gives the written solution of every chapter exercise (statements are in the book) and, for the exercises whose solution needs a calculation, its code and result. Run the cells in order.

## Part A. The case

**Data.** `data/calls.csv`: 12,472 rows, one per call over 90 days, and six columns: `call_id`, `day`, `hour`, `second`, `wait_sec`, `ambulance` (yes/no). Each cell carries the number of the book section it belongs to.""",
 "pt": """# Capítulo 12 · Variáveis aleatórias e distribuições: caderno complementar
*Ciência de Dados e Inteligência Artificial em Saúde, Volume 1*

> **Este caderno acompanha o capítulo do livro; não o reproduz.** Definições, deduções e explicações estão no livro. Aqui você executa os cálculos do caso e confere os números. Todos os dados são **sintéticos** e os valores têm apenas finalidade didática.

A **Parte A** percorre o caso do capítulo, o registro da central de emergências de uma cidade, pelas nove perguntas da diretora. A **Parte B** traz a solução escrita de cada exercício do capítulo (os enunciados estão no livro) e, nos exercícios cuja solução exige cálculo, o código e o resultado. Execute as células em ordem.

## Parte A. O caso

**Dados.** `data/calls.csv`: 12.472 linhas, uma por ligação ao longo de 90 dias, e seis colunas: `call_id`, `day`, `hour`, `second`, `wait_sec`, `ambulance` (sim/não escritos `yes`/`no`). Cada célula traz o número da seção do livro a que pertence."""}
FOOT = {"en": "---\n*Synthetic data (seed 12, `generate_data.py`). Teaching values only; nothing here is an operational recommendation or an estimate for a real service.*",
        "pt": "---\n*Dados sintéticos (semente 12, `generate_data.py`). Valores apenas didáticos; nada aqui é recomendação operacional nem estimativa para um serviço real.*"}


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
        md(f"### 12.13 {'Exercise' if lang == 'en' else 'Exercício'} {k}. {title}")
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
