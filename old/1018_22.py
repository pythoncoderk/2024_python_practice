x, y = map(int, input().split())

class Snow:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def pulus(self):
        return self.one + self.two

snow = Snow(x, y)
print(snow.pulus())