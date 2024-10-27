class Rice:
    def __init__(self, g):
        self.g = g

    def ans(self):
        return int(self.g * 1.4)

n = int(input())
rice = Rice(n)
print(rice.ans())