n = int(input())
a = int(input())

class TotalKg:
    def __init__(self, cakes, kg):
        self.cakes = cakes
        self.kg = kg

    def ans(self):
        return self.cakes * self.kg

wagashi = TotalKg(n, a)
print(wagashi.ans())