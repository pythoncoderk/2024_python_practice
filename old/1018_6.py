# coding: utf-8
# 例外処理を定義しよう

enemies = ["スライム", "ドラゴン", "魔王"]

number = 0
try:
    print("勇者は敵に遭遇した")
    print("勇者は" + enemies[2 / number] + "と戦った")

except ZeroDivisionError as e:
    print(e)
finally:
    print("勇者は勝利した")
