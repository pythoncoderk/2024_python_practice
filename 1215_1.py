class Employee:
    def __init__(self, num, name):
        self.num = num
        self.name = name
    def make(self):
        return [self.num, self.name]
    def getnum(arr, no):
        return arr[no][0]

    def getname(self):
        return self.name
l = []
n = int(input())

for i in range(n):
    x = list(map(str, input().split()))
    x[1] = int(x[1])
    if x[0] == "make":
        emp = Employee(x[1], x[2])
        l.append(emp.make())
    elif x[0] == "getnum":
        print(l[x[1]-1][0])
    else:
        print(l[x[1]-1][1])


