class Mochi:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def ans(self):
        return self.n * self.m

n = int(input())
m = int(input())
mochi_001 = Mochi(n, m)
print(mochi_001.ans())