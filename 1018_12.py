# coding: utf-8
# 例外の種類を変更しよう その２

import sys

enemies = ["スライム", "ドラゴン", "魔王"]

try:
    number1 = 0
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[number2] + "と戦った")
except Exception as e:
    sys.stderr.write("未定義の変数を呼び出しています")


finally:
    print("勇者は勝利した")
