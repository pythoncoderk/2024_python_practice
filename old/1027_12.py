class Puls:
    def __init__(self, name_01, name_02):
        self.name_01 = name_01
        self.name_02 = name_02

    def ans(self):
        return self.name_01 + self.name_02
n = input()
m = input()
puls = Puls(n, m)
print(puls.ans())