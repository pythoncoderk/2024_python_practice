class Subsuc:
    def __init__(self, mounth):
        self.mounth = mounth

    def ans(self):
        return self.mounth * 12

n = int(input())
subsuc = Subsuc(n)
print(subsuc.ans())