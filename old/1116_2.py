################################################
import os

# 任意のファイルが存在するか確認する
# ファイルのフルパス
file_path = r"C:\Users\name\OneDrive\デスクトップ\Python\001.csv"

# ファイルが格納されているフォルダを指定
dir_path = r"C:\Users\name\OneDrive\デスクトップ\Python"

non_existent_path = 'non_exist'

print(os.path.isfile(file_path))
# True

################################################