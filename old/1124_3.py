import pandas as pd

df = pd.read_csv("test.csv")
print(df)

sum1 = df.loc[:, "a"].sum()
print(sum1)

print(df.dtypes[0][1])