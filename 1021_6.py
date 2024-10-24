class Height:
    def __init__(self, height):
        self.height = height

    def ans(self):
        return self.height + 10

n = int(input())
height = Height(n)
print(height.ans())