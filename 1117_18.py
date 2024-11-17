class Check:
    def __init__(self, n):
        self.n = n

    def ans(self):
        if 40 <= self.n <= 60:
            return "OK"
        return "NG"

n = int(input())
ch = Check(n)
print(ch.ans())