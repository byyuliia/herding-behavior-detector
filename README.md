# Herding Behavior Detector

Does a group of stocks move independently, or does dispersion collapse
during volatile periods — a sign that trading is driven by following the
crowd rather than individual analysis?

This project implements the Chang, Cheng & Khorana (2000) CSAD
(Cross-Sectional Absolute Deviation) model to test for herding behavior
in a group of tech stocks (AAPL, MSFT, GOOGL, NVDA, AMD) over 2023.

Full write-up, methodology, and interpretation: [research_note.md](research_note.md)

## What it does
1. Pulls daily price data for a set of stocks via `yfinance`
2. Calculates daily returns and CSAD (cross-sectional dispersion)
3. Regresses CSAD against market return (absolute and squared) using
   `statsmodels`
4. Tests whether dispersion shrinks (herding) or grows (independent
   behavior) as market volatility increases

## Result
No evidence of herding was found in this group over 2023 — dispersion
actually increased on high-volatility days, consistent with independent
trading rather than approval-seeking behavior. Full result and
interpretation, including likely drivers, in the research note.

## Why this project
I'm a statistics and data analytics alongside psychology student (thesis work on approval motivation and
perfectionism) moving into quantitative finance. Herding is essentially
approval-seeking behavior expressed at a market level — this project was
a chance to test that idea with real data and a regression instead of
self-report scales. More on that connection in the research note.

## How to run it
```bash
git clone https://github.com/byyuliia/herding-behavior-detector.git
cd herding-behavior-detector
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python src/main.py
```

## Project structure

herding-behavior-detector/
src/
main.py # full pipeline: data → returns → CSAD → regression
research_note.md # full write-up: method, result, interpretation
requirements.txt
README.md


## Built with
Python, pandas, numpy, yfinance, statsmodels, matplotlib

## Limitations
This tests one small, tech-concentrated group over one year. A single
company's earnings move (NVDA, +24% in a day) can dominate the dispersion
signal independent of whether the group is actually herding — a broader
or less correlated set of stocks would be a fairer test. Details in the
research note.
