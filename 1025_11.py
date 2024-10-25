class Names:
    def __init__(self, name):
        self.name = name
    
    def ans(self):
        if 10 - len(self.name) >= 0:
            return 10 - len(self.name)
        return 0
s = input()
names = Names(s)
print(names.ans())