class Total:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def ans(self):
        return self.one - self.two

one = int(input())
two = int(input())

total = Total(one, two)
print(total.ans())