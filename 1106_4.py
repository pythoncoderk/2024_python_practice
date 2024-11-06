class Years:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def ans(self):
        return self.two - self.one

n = int(input())
m = int(input())
year = Years(n, m)
print(year.ans())