n = int(input())
l = [list(map(str, input().split())) for i in range(n)]
xxx = input()

class Test:
    def __init__(self, name, age, barth, add):
        self.name = name
        self.age = age
        self.barth = barth
        self.add = add


for i in range(n):
    x, x2, x3, x4 = l[i]
    xyz = Test(x, x2, x3, x4)
    if xyz.age == xxx:
        print(xyz.name)