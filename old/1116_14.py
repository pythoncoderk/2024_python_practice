class Diff:
    def __init__(self, p1, p2, n):
        self.p1 = p1
        self.p2 = p2
        self.n = n

    def ans(self):
        print(self.p1 - self.n, self.p2 - self.n)

a, b = map(int, input().split())
n = int(input())

diff = Diff(a, b, n)
diff.ans()