class Rice:
    def __init__(self, n):
        self.n = n

    def ans(self):
        return self.n * 150

n = int(input())
rice = Rice(n)
print(rice.ans())