# Data Science and Artificial Intelligence in Health, Volume 1: companion notebooks

One notebook per chapter. Each notebook runs from the first cell to the last and has two parts:

- **Part A. The case**: the chapter's single case, with the calculations and figures.
- **Part B. Exercise solutions**: every chapter exercise, stated and solved, with the code that checks it.

All data are **synthetic**; no real patients appear. Each chapter is self-contained and reads only its own data.

## Chapters

| Chapter | Case | Notebook | Page |
|---|---|---|---|
| 11. Probability: The Language of Uncertainty | Public maternity unit, 5,000 deliveries | `chapters/ch11/ch11_probability.ipynb` | `docs/ch11.html` |

## Layout

```
chapters/chNN/           notebook, data/, generate_data.py (everything the chapter needs)
docs/                    HTML pages (index.html + one page per chapter), ready for GitHub Pages
tools/                   build_chNN_notebook.py (writes the notebook), build_site.py (runs it, exports HTML)
tests/                   test_chNN.py (checks the numbers quoted in the text against the data)
```

## Run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cd chapters/ch11 && jupyter lab ch11_probability.ipynb      # or open the notebook in VS Code
```

Rebuild the pages: `python tools/build_ch11_notebook.py && python tools/build_site.py`. Check the numbers: `python tests/test_ch11.py`.

## Notes

The synthetic data and every teaching assumption (the 4-day allowance, the one-day alert rule) are stated in the notebook. Nothing here is a clinical recommendation or an estimate for a real unit.
