import math

x = int(input())
m = int(input())

class KaraokeTime:
    def __init__(self, money, time):
        self.money = money
        self.time = time

    def ans(self):
        return math.ceil(self.time / 30) * self.money

karaoke_time = KaraokeTime(x, m)
print(karaoke_time.ans())