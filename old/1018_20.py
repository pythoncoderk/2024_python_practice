n = int(input())
m = int(input())

class Calc:
    def __init__(self, tish, box):
        self.tish = tish
        self.box = box

    def ans(self):
        return self.box // self.tish

calc = Calc(n, m)
print(calc.ans())