class Cord:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        if self.a + self.b == 21:
            return "Win"
        return self.a + self.b
a = int(input())
b = int(input())
cord = Cord(a, b)
print(cord.ans())
