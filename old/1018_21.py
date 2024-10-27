x, y = map(int, input().split())

class Calc:
    def __init__(self, money, time):
        self.money = money
        self.time = time

    def ans(self):
        return int(self.money * (y / 60))

calc = Calc(x, y)
print(calc.ans())