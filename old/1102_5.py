class Total:
    def __init__(self, n):
        self.n = n

    def ans(self):
        return self.n * 540

n = int(input())
total = Total(n)
print(total.ans())