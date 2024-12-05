import pandas as pd

path = r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\test_data.csv"

df = pd.read_csv(path)
print(df)

df = pd.read_csv(path, index_col=0)
print(df)

print(df.loc["佐藤"])

df = pd.read_csv(path, header=None)
print(df)

df = pd.read_csv(path, names=["C1", "C2", "C3", "C4", "C5", "C6"])
print(df)

df = pd.read_csv(path, index_col=0, na_values="22")
print(df)
