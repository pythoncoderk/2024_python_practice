class Test:
    def __init__(self, name, age, bir, sta):
        self.name = name
        self.age = age
        self.bir = bir
        self.sta = sta

    def ans(self):
        print(self.name, self.age, self.bir, self.sta)


n, m = map(int, input().split())
l = [list(map(str, input().split())) for i in range(n)]

for i in range(m):
    x, y = map(str, input().split())
    x = int(x)
    l[x - 1][0] = y

for i in range(n):
    a, b, c, d = l[i]
    test = Test(a, b, c, d)
    test.ans()