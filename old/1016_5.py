# coding: utf-8
# 学生メソッドを呼び出す

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    def sum(self):
        return str(self.kokugo + self.sansu)

# この下に、必要な処理を記述します
yamada = Gakusei(70, 43)
print("合計は" + yamada.sum() + "点です")
