class ChocoCake:
    def __init__(self, s, n):
        self.s = s
        self.n = n

    def ans(self):
        if self.s == "chocolate":
            return self.n * 2
        return self.n * 5

s = input()
n = int(input())
choco = ChocoCake(s, n)
print(choco.ans())