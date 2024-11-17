class Total:
    def __init__(self, n):
        self.n = n

    def ans(self):
        x = 0
        for i in range(7):
            x += int(input())
        if self.n > x:
            return x
        return self.n

n = int(input())
total = Total(n)
print(total.ans())