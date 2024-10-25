class Total:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def ans(self):
        return self.a + self.b + self.c

a = int(input())
b = int(input())
c = int(input())
total = Total(a, b, c)
print(total.ans())