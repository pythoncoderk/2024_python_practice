class Taxi:
    def __init__(self, fas=500, limits=3):
        self.fas = fas
        self.limits = limits

    def ans(self, n):
        over = n - self.limits
        if over < 0:
            return self.fas
        else:
            return (m * over) + self.fas


n, m = map(int, input().split())
taxi = Taxi()
print(taxi.ans(n))

