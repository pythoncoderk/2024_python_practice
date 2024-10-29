n, m = map(int, input().split())
a, b = map(int, input().split())

class Christmas:
    def __init__(self, n, m, a, b):
        self.n = n
        self.m = m
        self.a = a
        self.b = b

    def ans(self):
        if self.n > self.a:
            return "Yes"
        else:
            if self.m >= self.b:
                return "Yes"
            else:
                return "No"
chrismas = Christmas(n, m, a, b)
print(chrismas.ans())