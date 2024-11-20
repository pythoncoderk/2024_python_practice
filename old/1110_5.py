class Address:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ans(self):
        return self.a + "-" + self.b + "-" + self.c

a = input()
b = input()
c = input()

add = Address(a, b, c)
print(add.ans())