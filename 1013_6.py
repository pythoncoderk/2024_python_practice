class Total:
    def __init__(self, n, kg):
        self.n = n
        self.kg = kg

    def answer(self):
        return self.n * self.kg

n = int(input())
kg = int(input())

total = Total(n, kg)
print(total.answer())