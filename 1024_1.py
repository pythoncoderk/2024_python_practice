class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def make(self, arr):
        arr.append([int(self.number), self.name])

    def getnum(self,arr):
        print(arr[int(self.number) - 1][0])

    def getname(self, arr):
        print(arr[int(self.number) - 1][1])


l = []
n = int(input())
for i in range(n):
    x = list(map(str, input().split()))
    if x[0] == "make":
        employee = Employee(x[1], x[2])
        employee.make(l)
    elif x[0] == "getnum":
        employee = Employee(int(x[1]), x[0])
        employee.getnum(l)
    else:
        employee = Employee(int(x[1]), x[0])
        employee.getname(l)
