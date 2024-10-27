class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return self.a + self.b

n = int(input())
m = int(input())

total = Total(n, m)
print(total.ans())