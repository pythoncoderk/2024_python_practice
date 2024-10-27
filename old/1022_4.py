class Names:
    def __init__(self, name):
        self.name = name

    def ans(self):
        return self.name + "A"

s = input()
names = Names(s)
print(names.ans())