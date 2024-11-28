import pandas as pd

df = pd.read_csv(r"C:\Users\turnt\OneDrive\デスクトップ\pandas\001.csv", encoding='shift-jis')
print(df)

list_c = ["YES"]
list_num = [111]
x = df["No"].isin(list_num) & df["状態"].isin(list_c)

print(df[x].sum("USD JPY"))


