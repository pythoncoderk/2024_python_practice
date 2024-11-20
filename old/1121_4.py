class Test:
    def __init__(self, s, n):
        self.s = s
        self.n = n


    def ans(self):
        x = self.s.count("R")
        if x >= n:
            return "Yes"
        return "No"

s = input()
n = int(input())

tes = Test(s, n)
print(tes.ans())

