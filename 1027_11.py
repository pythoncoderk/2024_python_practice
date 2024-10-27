class Names:
    def __init__(self, name):
        self.name = name

    def ans(self):
        return len(self.name)
s = input()
name = Names(s)
print(name.ans())