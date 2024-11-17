class Ticket:
    def __init__(self, n, a, b, c):
        self.n = n
        self.a = a
        self.b = b
        self.c = c

    def ans(self):
        if self.n >= self.a:
            return self.n * self.b
        return self.n * self.c

n = int(input())
a, b, c = map(int, input().split())
tik = Ticket(n, a, b, c)
print(tik.ans())