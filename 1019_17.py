n = int(input())
m = int(input())

class Total:
    def __init__(self, total, output):
        self.total = total
        self.output = output

    def ans(self):
        return self.total - self.output

total = Total(n, m)
print(total.ans())