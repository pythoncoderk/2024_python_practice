class Str:
    def __init__(self, s):
        self.s = s

    def ans(self):
        return self.s[:3]
s = input()
ss = Str(s)
print(ss.ans())