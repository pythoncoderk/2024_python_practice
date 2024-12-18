import pandas as pd

path = r"C:\Users\turnt\OneDrive\デスクトップ\pandas_lecture\data\population.csv"
df = pd.read_csv(path, encoding="shift-jis")

print(df)