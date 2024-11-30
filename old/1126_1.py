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

for i in range(files_count):
    df = pd.read_csv(dir_path + "\\" + files[i])
    df_all = df.sum()
    total_all.append(df_all[1])

    df_111 = df[df[1] == 111].sum()
    total_111.append(df_111[1])
