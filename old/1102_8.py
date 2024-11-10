class Change:
    def __init__(self, n):
        self.n = n

    def ans(self):
        return self.n * 10

n = int(input())
change = Change(n)
print(change.ans())