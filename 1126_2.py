class Total:
    def __init__(self, m, v, f):
        self.m = m
        self.v = v
        self.f = f

    def ans(self):
        return ((self.m * (self.v ** 2)) / (2 * self.f))

m, v, f = map(int, input().split())
total = Total(m, v, f)
print(int(total.ans()))