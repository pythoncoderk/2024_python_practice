class Batter:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def ans(self):
        x = self.m // self.n
        y = self.m % self.n
        return [x, y]

n = int(input())
m = int(input())
bat = Batter(n, m)
print(bat.ans()[0])
print(bat.ans()[1])