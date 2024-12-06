import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#%matplotlib inline

aapl = yf.Ticker("AAPL")

days = 5

hist = aapl.history(period=f"{days}d")

hist.index = hist.index.strftime("%d %B %Y")

hist = hist[["Close"]]

hist.columns = ["apple"]

hist = hist.T

hist.index.name = "Name"

print(hist.head())

# print(hist.columns)

# #print(hist.reset_index())

# hist_msft = yf.Ticker("MSFT").history(period=f"{days}d")

# hist_2 = pd.concat([hist,hist_msft],axis=1).head

# print(hist_2)


