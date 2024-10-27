class Item:
    tax = 1.08
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def total(self):
        return int(self.price * self.quantity * Item.tax)

apple = Item(120, 15)
total = apple.total()
print("合計は" + str(total) + "円です！")

orange = Item(85, 32)
print("合計は" + str(orange.total()) + "円です！")
