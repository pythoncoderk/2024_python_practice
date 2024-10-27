class Names:
    def __init__(self, name):
        self.name = name

    def ans(self):
        return self.name * 3

s = input()
name_test = Names(s)
print(name_test.ans())