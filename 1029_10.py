class Total:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def ans(self):
        x = self.a + self.b
        y = self.c + self.d
        if x < y:
            return x
        return y
a, b = map(int, input().split())
c, d = map(int, input().split())
total = Total(a, b, c, d)
print(total.ans())