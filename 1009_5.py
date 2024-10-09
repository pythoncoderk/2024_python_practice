a, b = map(int, input().split())

class BusAndTrain(object):
    def __init__(self, bus, train):
        self.bus = bus
        self.train = train


bus_and_train = BusAndTrain(a, b)
print(bus_and_train.bus + bus_and_train.train)