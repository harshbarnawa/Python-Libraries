import pandas as pd

cal = {"day 1": 1750,"day 2": 2100,"day 3": 3000}

series = pd.Series(cal)

print(series)
series.loc["day 3"] += 100
print(series.loc["day 3"])