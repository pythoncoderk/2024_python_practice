n = int(input())
l = list(map(int, input().split()))

class Kg:
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr


    def ans(self):
        if self.n >= sum(self.arr):
            return "OK"
        return "NG"


kg = Kg(n, l)
print(kg.ans())