# Quantifying Herding Behavior in Tech Stocks (2023)

## Question
Do AAPL, MSFT, GOOGL, NVDA, and AMD exhibit herding behavior — moving in
unison rather than independently — during periods of high market volatility?

## Method
Using the Chang, Cheng & Khorana (2000) CSAD (Cross-Sectional Absolute
Deviation) methodology, I calculated daily dispersion across the five
stocks' returns, then regressed CSAD against the absolute value and
squared value of the equal-weighted market return:

CSAD_t = α + β1|R_m,t| + β2(R_m,t)² + ε_t

A negative and statistically significant β2 indicates herding (dispersion
shrinks on high-volatility days). A positive β2 suggests the opposite —
dispersion increasing alongside volatility, consistent with stocks
reacting to information independently rather than converging on group
behavior.

## Data
- Tickers: AAPL, MSFT, GOOGL, NVDA, AMD
- Period: 2023-01-01 to 2024-01-01
- Source: Yahoo Finance (via yfinance)
- 249 daily observations after cleaning

## Result
=====================================================================================
                        coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
const                 0.0086      0.001     13.695      0.000       0.007       0.010
market_return_abs    -0.1039      0.062     -1.671      0.096      -0.226       0.019
market_return_sq     10.4842      1.180      8.888      0.000       8.161      12.808
==============================================================================
Omnibus:                       43.390   Durbin-Watson:                   2.166
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               76.802
Skew:                           0.932   Prob(JB):                     2.10e-17
Kurtosis:                       4.981   Cond. No.                     3.55e+03
==============================================================================

The model explains about half the day-to-day variation in dispersion
(R² = 0.498), with market_return_sq the clear driver of that
relationship (coef = 10.48, p < 0.001).

## Interpretation
My first instinct was that squaring the market return would make herding
undetectable, since a squared number is always positive. But the
coefficient the regression assigns to it can still be negative — that's
what would actually signal herding. Here it wasn't.

I didn't find herding here — actually the opposite happened. Dispersion
went up on the big days, not down, which is consistent with independent,
information-driven trading rather than approval-seeking behavior.

Part of this is probably driven by NVDA specifically. It jumped about 24%
in a single day in late May 2023 after strong AI-related earnings
guidance — a move driven by one company's news, not the group as a whole.
That kind of spike pulls dispersion up on its own, independent of whether
the other four stocks were herding or not. A less concentrated group, or
a full sector index instead of five hand-picked names, would probably be
a fairer test.

## Why this matters
Herding is, at its core, a market-level expression of approval motivation
— people following the crowd because "what others are doing must be
right," rather than acting on independent analysis. My psychology thesis
studies a related but distinct question: not whether people follow group
standards, but through what mechanism. In a cross-cultural study of
Ukrainian and Austrian young adults, I found socially prescribed
perfectionism dominant in both groups, with unusually low variability —
a similar shape to herding, in the sense that individual variation
collapses toward a shared external standard. The two samples reached
that standard differently: Austrians showed an "internalization" pattern,
absorbing external expectations as their own, while Ukrainians showed a
"compartmentalization" pattern, defensively protecting internal standards
under stress.

This project doesn't test which mechanism, if either, applies to market
behavior — that would need a different kind of data entirely. But it's
the same underlying question asked with a different method: does a group
converge on a shared standard, and if so, how tightly? Testing it here
with regression instead of self-report scales was, for me, a chance to
see the same psychological pattern from a completely different angle.
