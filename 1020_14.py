class Total:
    def __init__(self, g):
        self.g = g

    def ans(self):
        return self.g * 13

n = int(input())

total = Total(n)
print(total.ans())