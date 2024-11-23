class Max:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def ans(self):
        x = min(self.arr)
        return self.n * x

n = int(input())
arr = list(map(int, input().split()))
m = Max(n, arr)
print(m.ans())