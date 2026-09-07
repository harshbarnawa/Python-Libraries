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

print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])

print(df.iloc[0:11])
print(df.iloc[0:11:2]) # for every 2nd row
print(df.iloc[0:11:2, 0:3]) # for every 2nd row and col selection too