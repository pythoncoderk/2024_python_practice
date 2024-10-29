class Total:
    def __init__(self, n, m):
        self.n = n
        self.m = m
    
    def ans(self):
        return self.n - self.m

n = int(input())
m = int(input())
total = Total(n, m)
print(total.ans())