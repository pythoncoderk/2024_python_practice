a, b = map(int, input().split())

class Total:
    def __init__(self, bus, train):
        self.bus = bus
        self.train = train

    def total_price(self):
        return self.bus + self.train


total = Total(a, b)
print(total.total_price())