class Massule:
    def __init__(self, kin):
        self.kin = kin

    def ans(self):
        return 1500 * self.kin

n = int(input())
mus = Massule(n)
print(mus.ans())
