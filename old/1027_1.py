class Total:
    def __init__(self, now_kg):
        self.now_kg = now_kg

    def ans(self):
        return self.now_kg - 10

n = int(input())
total = Total(n)
print(total.ans())