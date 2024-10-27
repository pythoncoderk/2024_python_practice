class Stock:
    def __init__(self, yen, up, down):
        self.yen = yen
        self.up = up
        self.down = down

    def ans(self):
        return self.yen + self.up - self.down

n = int(input())
m = int(input())
d = int(input())
stock = Stock(n, m, d)
print(stock.ans())