s = input()

class Names:
    def __init__(self, name):
        self.name = name

    def ans(self):
        return self.name[0] + self.name[-1]

names = Names(s)
print(names.ans())