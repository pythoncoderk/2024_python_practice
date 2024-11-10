class Hot:
    def __init__(self, n):
        self.n = n

    def ans(self):
        if 30 <= self.n < 35:
            return "M"
        return self.n

n = int(input())
hot = Hot(n)
print(hot.ans())