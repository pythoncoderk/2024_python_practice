class Years:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ans(self):
        return f"{b}/{c}/{a}"

a = int(input())
b = int(input())
c = int(input())

ye = Years(a, b, c)
print(ye.ans())