import pandas as pd

df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\test_data.csv", index_col=0)
print(df)

print(df["国語"])
print(df.国語)

print(df[["国語", "理科"]])

print(df.iloc[0])