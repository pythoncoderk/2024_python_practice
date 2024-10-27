n = int(input())

class Run:
    def __init__(self, m):
        self.m = m

    def ans(self):
        return self.m * 4

run = Run(n)
print(run.ans())