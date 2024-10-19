class Metre:
    def __init__(self, m):
        self.m = m

    def ans(self):
        return self.m // 80

m = int(input())
metre = Metre(m)
print(metre.ans())