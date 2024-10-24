class Preson:
    def __init__(self, no, menu, money):
        self.no = no
        self.menu = menu
        self.money = money

    def total(self, arr):
        



n, m = map(int, input().split())
l = {k + 1: [int(input()), 0] for k in range(n)}

