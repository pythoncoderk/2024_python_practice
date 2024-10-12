class Strings:
    def __init__(self, total, st):
        self.total = total
        self.st = st

    def ans(self):
        return self.st * self.total

n = int(input())
s = input()
strings = Strings(n, s)
print(strings.ans())