import pandas as pd
import quandl, math
import numpy as np

# preprocessing for scaling
# svm = support vector machine
# model_selection for creating training and testing samples
from sklearn import preprocessing, svm, model_selection

# linear regression docs:
# 	- https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
from sklearn.linear_model import LinearRegression

print("\n")

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
# treated as outliers in dataset
df.fillna(-99999, inplace=True)

# predict out 1% of the data frame, var will be number of days
forecast_out = int(math.ceil(0.01 * len(df)))
print("FC out: " + str(forecast_out))

# shift index by desired number of periods (up in our case)
df["label"] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)

# X = features : input (one column of the data in input set)
X = np.array(df.drop(columns="label", axis=1))

# scale x - standardize a dataset along any axis
X = preprocessing.scale(X)

df.dropna(inplace=True)

# y = labels : output
y = np.array(df["label"])

# create training and testing sets
# shuffle features and labels, keeping x's and y's connected
# get different data for training and testing
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

# find classifier (a classifier is a type of machine learning algorithm used to assign a class label to a data input)
# use the n_jobs arg to set how many processes to run training on (-1 = as many as possible)
clf = LinearRegression(n_jobs=-1)
# fit / train classifier, fit features and labels
clf.fit(X_train, y_train)
# test classifier
accuracy = clf.score(X_test, y_test)

print(accuracy)

print()
