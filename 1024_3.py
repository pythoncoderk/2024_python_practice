class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number

    def getname(self):
        return self.name


l = []
n = int(input())
for i in range(n):
    x = input().split()
    if x[0] == "make":
        number = int(x[1])
        name = x[2]
        l.append([number, name])
    elif x[0] == "getnum":
        employee = Employee(number, name)
        print(l[int(x[1]) - 1][0])
    else:
        employee = Employee(number, name)
        print(l[int(x[1]) - 1][1])

