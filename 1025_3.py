class Calc:
    def __init__(self, yen, up, down):
        self.yen = yen
        self.up = up
        self.down = down

    def ans(self):
        return self.yen + self.up - self.down

x = int(input())
y = int(input())
z = int(input())

calc = Calc(x, y, z)
print(calc.ans())