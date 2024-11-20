class Bin:
    def __init__(self, n):
        self.n = n

    def ans(self):
        if self.n == "A":
            return 10
        elif self.n == "B":
            return 11
        else:
            return self.n

n = input()
bi = Bin(n)
print(bi.ans())