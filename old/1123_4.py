class Daruma:
    def __init__(self, s, n):
        self.s = s
        self.n = n

    def ans(self):
        return self.s[:self.n - 1] + self.s[self.n:]

s = input()
n = int(input())
daruma = Daruma(s, n)
print(daruma.ans())