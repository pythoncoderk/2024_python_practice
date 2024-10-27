class Total:
    def __init__(self, up, multiplication):
        self.up = up
        self.multiplication = multiplication

    def ans(self):
        return 100 + self.up * self.multiplication

n = int(input())
m = int(input())

total = Total(n, m)
print(total.ans())