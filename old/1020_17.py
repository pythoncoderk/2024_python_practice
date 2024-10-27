class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return self.a * 2 + self.b * 2
a = int(input())
b = int(input())

total = Total(a, b)
print(total.ans())