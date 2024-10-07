class employee(object):
    def __init__(self, gom, number, name):
        self.gom = gom
        self.number = number
        self.name = name

    def employee2

l = []
n = int(input())
for i in range(n):
    x = list(map(str, input().split()))
    if len(x) == 3:
        x2 = employee(x[i][0], x[i][1], x[i][2])
    else:
        x2 = employee(x[i][0], x[i][1], x[i][2])

