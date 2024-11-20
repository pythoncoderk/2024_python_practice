class Name:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def ans(self):
        for i in range(self.n):
            print(self.s[i])

n = int(input())
s = input()
names = Name(n, s)
names.ans()