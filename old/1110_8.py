class Rev:
    def __init__(self, n, s):
        self.n = n
        self.s = s

    def ans(self):
        return self.s[::-1]

n = int(input())
s = input()
rev = Rev(n, s)
print(rev.ans())