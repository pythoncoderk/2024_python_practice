class Names:
    def __init__(self, name_001, name_002):
        self.name_001 = name_001
        self.name_002 = name_002

    def ans(self):
        if len(self.name_001) > len(self.name_002):
            return self.name_002
        return self.name_001

n = input()
m = input()
names = Names(n, m)
print(names.ans())