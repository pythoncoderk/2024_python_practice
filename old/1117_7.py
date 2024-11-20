import math


class ProgramerDay:
    def __init__(self, n):
        self.day = n

    def ans(self):
        if (self.day & (self.day - 1)) == 0:
            return "OK"
        return "NG"

n = int(input())
proday = ProgramerDay(n)
print(proday.ans())