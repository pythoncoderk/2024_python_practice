import os
import pandas as pd

dir_path = r"C:\Users\turnt\OneDrive\デスクトップ\pandas"

files = os.listdir(dir_path)
files_count = len(files)
print(files)
print(files_count)

total_all = []
total_111 = []
total_222 = []

for i in files:
    df = pd.read_csv(os.path.join(dir_path, i))
    total_all.append(df["USD"].sum())

    df_111 = df.query('(No == 111)')
    total_111.append(df_111["USD"].sum())

    df_222 = df.query('(No == 222)')
    total_222.append(df_222["USD"].sum())

print(sum(total_all) / files_count)
print(max(total_all))