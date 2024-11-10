class Check:
    def __init__(self, n):
        self.n = n

    def ans(self):
        if self.n < 37.0:
            return "OK"
        return "NG"

n = float(input())
chk = Check(n)
print(chk.ans())