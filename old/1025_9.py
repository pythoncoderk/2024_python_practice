class Names:
    def __init__(self, name):
        self.name = name

    def ans(self):
        return "paiza" + self.name
s = input()
names = Names(s)
print(names.ans())