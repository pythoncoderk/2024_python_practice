class Test:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def ans(self):
        if self.z <= self.x:
            return self.x + self.y
        return self.x
x, y = map(int, input().split())
z = int(input())
test = Test(x, y, z)
print(test.ans())
