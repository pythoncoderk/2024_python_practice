class Calc:
    def __init__(self, count):
        self.count = count

    def ans(self):
        return self.count // 10

n = int(input())
calc = Calc(n)
print(calc.ans())