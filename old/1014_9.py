class Chk:
    def __init__(self, n):
        self.n = n

    def ans(self):
        if self.n >= 8:
            return "OK"
        return "NG"

n = int(input())
chk = Chk(n)
print(chk.ans())