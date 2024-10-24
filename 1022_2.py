class Calc:
    def __init__(self, remainder):
        self.remainder = remainder

    def ans(self):
        return self.remainder % 10

n = int(input())
calc = Calc(n)
print(calc.ans())