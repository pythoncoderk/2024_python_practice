class Mounten:
    def __init__(self, n, a):
        self.n = n
        self.a = a

    def ans(self):
        x = self.n // 10
        return x * self.a

n = int(input())
a = int(input())

mon = Mounten(n, a)
print(mon.ans())