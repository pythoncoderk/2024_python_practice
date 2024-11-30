class Number:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def ans(self):
        return self.arr[self.n - 1]

n = int(input())
l = list(map(str, input().split()))
num = Number(n, l)
print(num.ans())