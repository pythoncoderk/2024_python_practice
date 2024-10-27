n, m = map(int, input().split())

class Price:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def ans(self):
        if self.n - self.m > 0:
            return self.n - self.m
        return 0

price = Price(n, m)
print(price.ans())