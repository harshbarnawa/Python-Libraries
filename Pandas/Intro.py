## A fast powerful and flexible open source
## data analysis and manipulation library

import pandas as pd

# series -> is a 1d labeled array that can hold any data type
# like a single column of excel

data = [100, 102, 104, 202, 208]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])

print(series)
print(series.loc["a"])

series.loc["a"] = 99
print("Updated value:", series.loc["a"])
print("location by index:", series.iloc[0])

# filtering

print(series[series >= 200])
