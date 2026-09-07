import pandas as pd

df = pd.read_csv("Pandas/data.csv", index_col="Name")
## selection by columns
# print(df["Name"].to_string())
print(df["Height"].to_string())
print(df["Weight"].to_string())

# print(df[["Name","Height","Weight"]].to_string())

## selection by rows

print(df)

print(df.loc["Pikachu"])