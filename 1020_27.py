n = int(input())
m = int(input())

class Stock:
    def __init__(self, buy, sell):
        self.buy = buy
        self.sell = sell

    def ans(self):
        if self.buy > self.sell:
            return "No"
        return "Yes"

stock = Stock(n, m)
print(stock.ans())