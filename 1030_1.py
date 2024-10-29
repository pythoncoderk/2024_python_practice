class Str:
    def __init__(self, str, tr, index):
        self.str = str
        self.tr = tr
        self.index = index

    def ans(self):
        if self.str[self.index - 1] == self.tr:
            return "Yes"
        return "No"



s = input()
t = input()
n = int(input())
ss = Str(s, t, n)
print(ss.ans())