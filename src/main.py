import yfinance as yf

data = yf.download("AAPL", start="2023-01-01", end="2024-01-01")

import pandas as pd
pd.set_option('display.max_columns', None)

tickers = ["AAPL", "MSFT", "GOOGL", "NVDA", "AMD"]
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")["Close"]
returns = data.pct_change().dropna()

market_return = returns.mean(axis=1)
csad = returns.sub(market_return, axis=0).abs().mean(axis=1)

import matplotlib.pyplot as plt

csad.plot(title="CSAD Over Time")

import statsmodels.api as sm

X = pd.DataFrame({"market_return_abs": market_return.abs(), "market_return_sq": market_return ** 2})
X = sm.add_constant(X)

model = sm.OLS(csad, X).fit()
print(model.summary())