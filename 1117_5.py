class Check:
    def __init__(self, n):
        self.chk = n

    def ans(self):
        l = []
        for i in range(len(self.chk)):
            l.append(self.chk.count(self.chk[i]))
        if max(l) >= 2:
            return "NG"
        return "OK"

n = input()
check = Check(n)
print(check.ans())