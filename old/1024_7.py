class Last:
    def __init__(self, name):
        self.name = name

    def ans(self):
        return self.name[-1]

s = input()
last = Last(s)
print(last.ans())