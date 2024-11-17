class Check:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ans(self):
        return max(len(self.a), len(self.b), len(self.c))

a = input()
b = input()
c = input()
ch = Check(a, b, c)
print(ch.ans())