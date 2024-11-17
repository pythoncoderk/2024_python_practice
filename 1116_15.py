class Ive:
    def __init__(self, n):
        self.ive = n

    def ans(self):
        return self.ive - 1

n = int(input())
ive = Ive(n)
print(ive.ans())