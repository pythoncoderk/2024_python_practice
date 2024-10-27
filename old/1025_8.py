class Total:
    def __init__(self, cm):
        self.cm = cm

    def ans(self):
        return self.cm // 4

n = int(input())
total = Total(n)
print(total.ans())