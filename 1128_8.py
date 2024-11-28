import numpy as np
import glob

target_path = r"C:\Users\turnt\OneDrive\デスクトップ\pandas\*.csv"

file_paths = glob.glob(target_path)
print(file_paths)

files_count = len(file_paths)
total_all = []
total_d = []
total_p = []

for i in file_paths:
    data = np.loadtxt(i, skiprows=1, delimiter=',', usecols=(1))
    total_all.append(np.sum(data))

print(total_all)