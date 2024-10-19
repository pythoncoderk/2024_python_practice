n = int(input())
a = int(input())
b = int(input())

class Calc:
    def __init__(self, total, one, two):
        self.total = total
        self.one = one
        self.two = two

    def ans(self):
        x = self.one + self.two
        return self.total - x

test001 = Calc(n, a, b)
print(test001.ans())