class Tiket:
    def __init__(self, yen):
        self.yen = yen

    def ans(self):
        return self.yen ** 2

n = int(input())
tiket = Tiket(n)
print(tiket.ans())