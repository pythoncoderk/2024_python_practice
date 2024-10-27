n = int(input())
m = int(input())

class Woter:
    def __init__(self, wont, woter):
        self.wont = wont
        self.woter = woter

    def ans(self):
        if self.wont >= self.woter:
            return "Yes"
        return "No"

woter = Woter(n, m)
print(woter.ans())