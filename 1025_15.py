class Total:
    def __init__(self, monye, count):
        self.monye = monye
        self.count = count

    def ans(self):
        return self.monye * self.count

n = int(input())
m = int(input())
total = Total(n, m)
print(total.ans())