class Total:
    def __init__(self, wt):
        self.wt = wt

    def ans(self):
        return self.wt * 24 * 25

n = int(input())
total = Total(n)
print(total.ans())