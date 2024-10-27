class Wether:
    def __init__(self, rain):
        self.rain = rain

    def ans(self, time=24):
        return self.rain * time


n = int(input())
wether = Wether(n)
print(wether.ans())
