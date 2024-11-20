####################################################################################

import glob
import os
import shutil
from pathlib import Path
from datetime import datetime

now = datetime.now()
# フォント設定「Arial」など

# + コピーしたファイル名に使用
dir_name = "cliaringfand"

#とりあえずフルパスで片っ端からファイルを取得　ファイル名を指定
l = glob.glob(r'C:\\Users\\turnt\\OneDrive\\デスクトップ\\Python\\2024_python_practice\\test_py\\**\\position.csv', recursive=True)
ans_l = []
for i in range(len(l)):
#if dir_name in l[i]:
    ans_l.append(l[i])

if len(ans_l) == 0:
    print("取得対象がありません。。。")
    print("とりあえず Enter で終了しますか。。。")
    input()

#取得したファイルを格納するフォルダを指定
copy_dir = r"C:\Users\turnt\OneDrive\デスクトップ\output"

total_files = len(ans_l)

for i in range(len(ans_l)):
    get_timestamp = Path(ans_l[i])
    create_time = datetime.fromtimestamp(get_timestamp.stat().st_ctime)
    create_time_l = list(map(str, str(create_time).split()))
    timestamp = create_time_l[0]
    files_copy = shutil.copy(ans_l[i], copy_dir)
    find_files_copy = str(files_copy).rfind("\\")
    get_file_name = str(files_copy)[find_files_copy + 1:]
    shutil.move(files_copy, files_copy[:find_files_copy + 1] + timestamp + "_" + dir_name + "_" + str(i + 1) + ".csv")

    print(str(i + 1).zfill(5) + " / " + str(total_files).zfill(5) + "件" + " Copy OK !!!!")

print()
print("That's All !!!")
print()
final = datetime.now()
t = (final - now)
print("処理時間合計 " + str(t)[:7])
print()
print("Enter を押すと終了しまっす！")
input()
####################################################################################