class PlasticBag:
    def __init__(self, total_price):
        self.price = total_price

    def ans(self):
        if self.price >= 1000:
            return self.price + 3
        return self.price

yen = int(input())
plastic_bag_and_total = PlasticBag(yen)
print(plastic_bag_and_total.ans())