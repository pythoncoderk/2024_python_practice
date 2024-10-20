n = int(input())
m = int(input())

class Calc:
    def __init__(self, parts, counts):
        self.parts = parts
        self.counts = counts

    def ans(self):
        return self.parts * self.counts

calc = Calc(n, m)
print(calc.ans())