class Total:
    def __init__(self, up, parsons):
        self.up = up
        self.parsons = parsons

    def ans(self):
        return 100 + self.up * self.parsons

n = int(input())
m = int(input())
total = Total(n, m)
print(total.ans())