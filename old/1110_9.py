class Total:
    def __init__(self, n, a):
        self.n = n
        self.a = a

    def ans(self):
        return self.n * self.a

n, a = map(int, input().split())
total = Total(n, a)
print(total.ans())