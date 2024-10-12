class Changes:
    def __init__(self, total_price, money):
        self.total_price = total_price
        self.money = money

    def ans(self):
        return self.money - self.total_price

total = int(input())
money = int(input())

changes = Changes(total, money)
print(changes.ans())