l = list(map(str, input().split()))

class Calc:
    def __init__(self, arr):
        self.arr = arr

    def ans(self):
        self.arr[0] = int(self.arr[0])
        self.arr[2] = int(self.arr[2])
        if self.arr[1] == "+":
            return self.arr[0] + self.arr[2]
        return self.arr[0] - self.arr[2]

calc = Calc(l)
print(calc.ans())