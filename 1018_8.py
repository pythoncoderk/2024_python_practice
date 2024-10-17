# coding: utf-8
# 例外メッセージを指定しよう

import sys

enemies = ["スライム", "ドラゴン", "魔王"]

try:
    number = 0
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[2 / number] + "と戦った")
except ZeroDivisionError as e:
    sys.stderr.write("その敵は表示できません")
finally:
    print("勇者は勝利した")
