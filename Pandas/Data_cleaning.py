import pandas as pd

# Data cleaning = the process of fixing/removing
#                 incomplete, incorrect, or irrelevant data.
#                 ~75% of work done with Pandas is data cleaning

df = pd.read_csv("Pandas/data.csv")

# 1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

# 2. Handle missing data
# df = df.dropna(subset=["Type2"])
df = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values

# df["Type1"] =df["Type1"].replace({"Grass": "GRASS",
#                                   "Fire":"FIRE",
#                                   "Water":"WATER"})

# 4. Standardize text
df["Name"] =df["Name"].str.lower()

# 5. Fixing data types
df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate values
df = df.drop_duplicates()  # if any duplicate name it will remove
print(df.to_string())