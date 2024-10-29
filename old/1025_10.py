class Total:
    def __init__(self, kg):
        self.kg = kg

    def ans(self):
        return self.kg * 5

n = int(input())
total = Total(n)
print(total.ans())