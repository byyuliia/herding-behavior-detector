import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

pd.set_option('display.max_columns', None)

tickers = ["AAPL", "MSFT", "GOOGL", "NVDA", "AMD"]
data = yf.download(tickers, start="2023-01-01", end="2024-01-01")["Close"]
returns = data.pct_change().dropna()

market_return = returns.mean(axis=1)
csad = returns.sub(market_return, axis=0).abs().mean(axis=1)

csad.plot(title="CSAD Over Time")

X = pd.DataFrame({"market_return_abs": market_return.abs(), "market_return_sq": market_return ** 2})
X = sm.add_constant(X)

model = sm.OLS(csad, X).fit()
print(model.summary())

# Scatter: market return vs CSAD, with regression line overlaid
plt.figure(figsize=(8, 6))
plt.scatter(market_return, csad, alpha=0.5, s=15, label="Daily observations")

# Build the fitted regression line across the range of market returns
x_range = np.linspace(market_return.min(), market_return.max(), 100)
X_line = pd.DataFrame({
    "market_return_abs": np.abs(x_range),
    "market_return_sq": x_range ** 2
})
X_line = sm.add_constant(X_line, has_constant='add')
y_line = model.predict(X_line)

plt.plot(x_range, y_line, color="red", linewidth=2, label="Fitted regression")

plt.xlabel("Daily Market Return")
plt.ylabel("CSAD (Cross-Sectional Dispersion)")
plt.title("CSAD vs. Market Return (2023)")
plt.legend()
plt.tight_layout()
plt.savefig("csad_scatter.png", dpi=200)
plt.show()