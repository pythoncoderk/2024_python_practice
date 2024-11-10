class Point:
    def __init__(self, n):
        self.n = n

    def ans(self):
        if self.n >= 1000:
            return self.n // 10
        return 0

n = int(input())
point = Point(n)
print(point.ans())