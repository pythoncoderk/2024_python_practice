class Atm:
    def __init__(self, money):
        self.money = money

    def ans(self):
        get_money = self.money - 120
        if get_money > 0:
            return get_money
        return 0
n = int(input())
atm = Atm(n)
print(atm.ans())