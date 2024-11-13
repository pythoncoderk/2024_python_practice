class Wether:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return self.a - self.b

a, b = map(int, input().split())
wether = Wether(a, b)
print(wether.ans())