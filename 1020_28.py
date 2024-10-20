n = int(input())
m = int(input())

class Longs:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def ans(self):
        return self.one + self.two

longs = Longs(n, m)
print(longs.ans())