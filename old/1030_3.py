class Chk:
    def __init__(self, n):
        self.n = n

    def ans(self):
        return 222 - self.n

n = int(input())
chk = Chk(n)
print(chk.ans())
