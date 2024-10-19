m = int(input())

class Mounth:
    def __init__(self, mounth):
        self.mounth = mounth

    def ans(self):
        x = self.mounth + 2
        if x <= 12:
            return x
        return x - 12

mounth = Mounth(m)
print(mounth.ans())