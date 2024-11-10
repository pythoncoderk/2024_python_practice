class Wat:
    def __init__(self, n):
        self.n = n

    def ans(self):
        return self.n * 25 * 24

n = int(input())
wat = Wat(n)
print(wat.ans())