import pandas as pd

# DataFrame - A tabular data structure with rows AND columns 2d
#            Similar to an Excel spreadsheett

data = {"Name": ["Harsh", "Devraj", "Aditya"],
        "Age": [22, 20, 21]
        } ##here I am using dictionary
df = pd.DataFrame(data)

print(df)