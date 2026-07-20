import pandas as pd

data = {
    "Name": ["Ram", "Sam", "John"],
    "Marks": [90, 85, 88]
}

df = pd.DataFrame(data)

print(df.head())