class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.name

    def getnumber(self):
        return self.number
l = []
n = int(input())
for i in range(n):
    x = input().split()
    if x[0] == "make":
        l.append([int(x[1]), x[2]])
    elif x[0] == "getnum":
        number = int(x[1])
        print(l[number - 1][0])
    elif x[0] == "change_num":
        number = int(x[1])
        l[number - 1][0] = int(x[2])
    elif x[0] == "change_name":
        number = int(x[1])
        l[number - 1][1] = x[2]

    else:
        number = int(x[1])
        print(l[number - 1][1])
