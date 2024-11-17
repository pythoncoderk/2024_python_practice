class Power:
    def __init__(self, n):
        self.n = n

    def ans(self):
        return pow(2, self.n)

n = int(input())
power = Power(n)
print(power.ans())