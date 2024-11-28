import glob
import pandas as pd

target_path = r"C:\Users\turnt\OneDrive\デスクトップ\pandas\*.csv"

file_paths = glob.glob(target_path)
print(file_paths)

files_count = len(file_paths)
total_all = []
total_d = []
total_p = []

for i in file_paths:
    df = pd.read_csv(i, encoding='shift_jis')
    df_all = pd.DataFrame(df["USD JPY"])
    df_ans_all = df_all.sum()
    total_all.append(df_ans_all.iloc[-1])





