# Foundations of Data Analysis in Health, Volume 1: companion notebooks

*Data, Study Design, Probability, and Classical Inference.* Part of the work **Data Science and Artificial Intelligence in Health**.

Companion notebooks to the book, one per chapter (English edition). They **do not reproduce the book**: definitions, derivations, and explanations stay in the book. Each notebook runs from the first cell to the last and has two parts:

- **Part A. The case**: the chapter's single case, with the calculations and figures.
- **Part B. Exercise solutions**: the code and numeric result for each chapter exercise (statements are in the book).

All data are **synthetic**; no real patients appear. Each chapter is self-contained and reads only its own data.

## Chapters

| Chapter | Case | Notebooks | Pages |
|---|---|---|---|
| 2. Populations, Samples, and Data | Hospital with 500 beds: audit of a sample of the January discharges to home | `chapters/ch02/ch02_populations_samples_data_en.ipynb` | `docs/ch02_en.html` |
| 10. Experimental and Quasi-Experimental Designs in Health | Hypertension service with ten clinics: single pill versus separate tablets | `chapters/ch10/ch10_experimental_designs_en.ipynb` | `docs/ch10_en.html` |
| 11. Probability: The Language of Uncertainty | Infection-control committee of a public maternity unit, 5,000 deliveries | `chapters/ch11/ch11_probability_en.ipynb` | `docs/ch11_en.html` |
| 13. Sampling and Estimation | Health department surveys schoolchildren for oral health: a list of 14,299 children in 48 schools | `chapters/ch13/ch13_sampling_estimation_en.ipynb` | `docs/ch13_en.html` |

## Layout

```
chapters/chNN/           notebook, data/, generate_data.py (everything the chapter needs)
docs/                    HTML pages (index.html + one page per chapter), ready for GitHub Pages
tools/                   build_chNN_notebook.py (writes the notebook), build_site.py (runs it, exports HTML), LANG
tests/                   test_chNN.py (checks the numbers quoted in the text against the data)
```

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
(cd chapters/ch11 && jupyter lab ch11_probability_en.ipynb)      # or open the notebook in VS Code
```

Rebuild the pages: `python tools/build_ch11_notebook.py && python tools/build_site.py`. Check the numbers: `python tests/test_ch11.py`.

## Revision

The Chapter 11 notebook follows the revised chapter of 2026-11-13 (maternity register with four columns and six committee questions).

## Notes

The data are synthetic and the values are for teaching purposes only; they have no correlation with the real world. Nothing here is a clinical recommendation or an estimate for a real unit.

## Online

Pages: https://marcelosilva2604.github.io/data-science-ml-ai-in-health-volume-1/ · Repository: https://github.com/marcelosilva2604/data-science-ml-ai-in-health-volume-1

**The repository name and the `main` branch are printed in the book's QR codes. Do not rename, move, or delete them.** If the pages move (for example to the publisher's site), update the links in this README; the QR codes keep pointing here.
