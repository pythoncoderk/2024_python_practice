class Counts:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return self.b % self.a

a = int(input())
b = int(input())

counts = Counts(a, b)
print(counts.ans())