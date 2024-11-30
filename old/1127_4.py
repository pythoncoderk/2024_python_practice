class Changes:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def ans(self):
        for i in range(self.n):
            if i != self.n - 1:
                print(self.arr[i], end=" ")
            else:
                print(self.arr[i])

n = int(input())
l = [input() for i in range(n)]
chan = Changes(n, l)
chan.ans()