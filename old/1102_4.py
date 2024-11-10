class Total:
    def __init__(self, n):
        self.n = n

    def ans(self):
        total = 0
        for i in range(self.n):
            total += int(input())
        return total

n = int(input())
total = Total(n)
print(total.ans())