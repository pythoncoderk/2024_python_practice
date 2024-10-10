x = int(input())
n = int(input())

class Power:
    def __init__(self, charge, now):
        self.charge = charge
        self.now = now

    def ans(self):
        x = 100 - self.now
        y = x * self.charge
        return y


power = Power(x, n)
print(power.ans())