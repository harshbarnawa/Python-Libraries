import pandas as pd

# DataFrame - A tabular data structure with rows AND columns 2d
#            Similar to an Excel spreadsheett

data = {"Name": ["Harsh", "Devraj", "Aditya"],
        "Age": [22, 20, 21]
        } ##here I am using dictionary
df = pd.DataFrame(data, index = ["Student 1","Student 2","Student 3"])

print(df)


print(df.loc["Student 3"])
print(df.iloc[1])

## adding new column

df["Hobbies"] = ["Games", "Songs", "Badminton"]

print("\n",df)

## adding new row

new_row = pd.DataFrame([{"Name": "Bharat", "Age": 20, "Hobbies": "Movies"},
                        {"Name": "Anurag", "Age": 21, "Hobbies": "Coding"}
                        ], index = ["Student 4","Student 5"])

df = pd.concat([df, new_row])
print("\n",df)