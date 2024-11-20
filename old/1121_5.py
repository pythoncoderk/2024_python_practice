class ThankYou:
    def __init__(self, n, m):
        self.n = n
        self.m = m

    def ans(self):
        if self.n >= self.m:
            return "Thank you"
        return self.m - self.n
n = int(input())
m = int(input())
thanks = ThankYou(n, m)
print(thanks.ans())