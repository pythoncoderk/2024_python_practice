class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return self.a + self.b

a = int(input())
b = int(input())
total = Total(a, b)
print(total.ans())