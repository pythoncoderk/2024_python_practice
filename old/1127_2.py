class Judge:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr

    def ans(self):
        g = self.arr.count("G")
        p = self.arr.count("P")
        if g == p:
            return "Draw"
        elif g > p:
            return "P"
        else:
            return "G"

n = int(input())
l = list(map(str, input().split()))
jud = Judge(n, l)
print(jud.ans())