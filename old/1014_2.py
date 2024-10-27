class Limits:
    def __init__(self, woter, limi):
        self.woter = woter
        self.limi = limi

    def ans(self):
        x = self.limi // self.woter
        y = self.limi % self.woter
        print(x)
        print(y)

n = int(input())
m = int(input())

limits = Limits(n, m)
limits.ans()



