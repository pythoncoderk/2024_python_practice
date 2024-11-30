import pandas as pd

df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\test_data.csv")
print(df)

df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\test_data.csv", index_col=0)
print(df)

print(df.loc["佐藤"])

df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\test_data.csv", header=1)
print(df)

df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\test_data.csv", header=None)
print(df)

df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\test_data.csv", names=["A", "B", "C", "D", "E", "F", "G", "H"])
print(df)


df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\population.csv", encoding="shift-jis")
print(df)
