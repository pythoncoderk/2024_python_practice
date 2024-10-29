class Qupon:
    def __init__(self, yen, qupon):
        self.yen = yen
        self.q = qupon

    def ans(self):
        return self.yen - self.q

n, m = map(int, input().split())
qupon = Qupon(n, m)
print(qupon.ans())