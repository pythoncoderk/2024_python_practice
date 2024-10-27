a, b = map(int, input().split())

class TrainAndBus(object):
    def __init__(self, bus, train):
        self.bus = bus
        self.train = train

    def prices(self, bus, train):
        print(bus + train)


TrainAndBus().prices(a, b)