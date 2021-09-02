import pandas as pd
import quandl
import math

# find tickers to use in get function from Quandl's website
# returns data set from stocks
# 	- https://www.quandl.com/
# df = data frame
df = quandl.get("WIKI/GOOGL")

# only get these values
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Volume"]]
# high-low percent
df["HL_PCT"] = (df["Adj. High"] - df["Adj. Close"]) / df["Adj. Close"] * 100
# daily percent change
df["PCT_change"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"] * 100

# take only important values
df = df[["Adj. Close", "HL_PCT", "PCT_change", "Adj. Volume"]]

# guess future values
forecast_col = "Adj. Close"
# replace NaN values
df.fillna(-99999, implace=True)

# predict out 10% of the data frame
forecast_out = int(math.ceil(0.1 * len(df)))

# shift index by desired number of periods (up in our case)
df["label"] = df[forecast_col].shift(-forecast_out)

print(df.head)
