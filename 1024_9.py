class Total:
    def __init__(self, money):
        self.money = money

    def ans(self):
        return self.money % 10

n = int(input())
total = Total(n)
print(total.ans())