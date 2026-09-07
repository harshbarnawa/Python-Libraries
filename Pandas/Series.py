import pandas as pd
## using dictionary
cal = {"day 1": 1750,"day 2": 2100,"day 3": 3000}

series = pd.Series(cal)

print(series)
series.loc["day 3"] += 100
print(series.loc["day 3"])

print(series[series >= 2000])
print(series[series < 2000])