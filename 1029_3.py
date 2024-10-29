class Count:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def ans(self):
        return str(self.s).count(self.n)
n = input()
s = input()
test = Count(n, s)
print(test.ans())