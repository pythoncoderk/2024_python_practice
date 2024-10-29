class Change:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def ans(self):
        return f"{self.b} {self.a}"
n, m = map(int, input().split())
change = Change(n, m)
print(change.ans())
