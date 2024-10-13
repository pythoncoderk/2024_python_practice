class Test:
    def __init__(self, x, t):
        self.x = x
        self.t = t

    def chk(self):
        time = self.t * 60
        return time // x

x, t = map(int, input().split())
test = Test(x, t)
print(test.chk())