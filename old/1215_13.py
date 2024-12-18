class Calls:
    def __init__(self, st):
        self.st = st

    def ans(self):
        return self.st

n, m = map(int, input().split())
for i in range(m):
    ca = Calls(input())
    print(ca.ans())