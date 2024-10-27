class Power:
    def __init__(self, n):
        self.n = n

    def ans(self):
        if self.n <= 10:
            return "low"
        return self.n

n = int(input())

power = Power(n)
print(power.ans())