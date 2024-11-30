import pandas as pd

path_csv = r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\test_data3.csv"

df = pd.read_csv(path_csv, index_col=0)
print(df)

print(df.shape)

print(len(df))
print(len(df.columns))

print(df.size)
print(df.info())

print(df.T)