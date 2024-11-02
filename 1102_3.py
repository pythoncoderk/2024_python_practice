class Total:
    def __init__(self, m):
        self.m = m

    def ans(self):
        return self.m * 1.5

n = int(input())
total = Total(n)
print(total.ans())