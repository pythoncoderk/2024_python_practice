class Tv:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def ans(self):
        return  self.n * self.n - self.m

n = int(input())
m = int(input())
tv = Tv(n, m)
print(tv.ans())